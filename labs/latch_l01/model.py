"""Deterministic in-memory Shared-Draft Lab, pass 1.

Policy: docs/latch-education lesson -> addendum -> R1/R2 errata.
Driver binding/setup/inspection are trusted fixture controls, not authentication.
Replay, retry and the teaching runner are intentionally absent in this slice.
"""

from dataclasses import asdict, dataclass, replace
from enum import Enum
from typing import Optional, Tuple


class Status(str, Enum):
    OK = "OK"
    RESTORED = "RESTORED"
    DENIED = "DENIED"
    OFFLINE = "OFFLINE"
    NO_CACHE = "NO_CACHE"
    CONFLICT = "CONFLICT"
    INVALID_CONTEXT = "INVALID_CONTEXT"


@dataclass(frozen=True)
class Result:
    status: Status
    body: Optional[str] = None


@dataclass(frozen=True)
class Draft:
    resource: str
    owner: str
    body: str
    revision: int
    unsent: bool = True


@dataclass(frozen=True)
class CachedDraft:
    resource: str
    owner: str
    body: str
    base_revision: int


@dataclass(frozen=True)
class Grant:
    grant_id: str = "G1"
    issuer: str = "A"
    subject: str = "X"
    resource: str = "D1"
    action: str = "read"
    start: int = 0
    end: int = 100


@dataclass(frozen=True)
class FixtureConfig:
    users: Tuple[str, ...] = ("A", "B")
    agents: Tuple[str, ...] = ("X", "Y")
    initial_user: str = "A"
    initial_actor: str = "A"
    initial_time: int = 0
    public_resource: str = "H"
    public_body: str = "Welcome"
    drafts: Tuple[Draft, ...] = (
        Draft("D1", "A", "server-D1", 1),
        Draft("D2", "A", "server-D2", 1),
    )
    cache: Tuple[CachedDraft, ...] = (CachedDraft("D1", "A", "local-A1", 1),)
    grant: Grant = Grant()
    conflict_revision: int = 2


DEFAULT_CONFIG = FixtureConfig()


class SharedDraftLab:
    def __init__(self, config: FixtureConfig = DEFAULT_CONFIG):
        self.config = config
        self.reset()

    def reset(self) -> None:
        self._user = self.config.initial_user
        self._actor = self.config.initial_actor
        self._online = True
        self._time = self.config.initial_time
        self._revoked = False
        self._drafts = {d.resource: d for d in self.config.drafts}
        self._cache = {c.resource: c for c in self.config.cache}
        self._editor = None

    def switch(self, user: str) -> None:
        """Trusted driver: clear private display and requester binding."""
        if user not in self.config.users:
            raise ValueError("Unknown fixture user")
        self._user = user
        self._actor = None
        self._editor = None

    def bind(self, actor: Optional[str]) -> Status:
        """Trusted driver only. Request fields cannot invoke this binding."""
        self._actor = actor if actor in self.config.users + self.config.agents else None
        return Status.OK if self._actor is not None else Status.INVALID_CONTEXT

    def online(self, connected: bool) -> None:
        if not isinstance(connected, bool):
            raise ValueError("Connectivity must be a boolean")
        self._online = connected

    def advance(self, time: int) -> None:
        if type(time) is not int or time < self._time:
            raise ValueError("Fixture clock requires nondecreasing integer ticks")
        self._time = time

    def revoke(self, grant_id: Optional[str] = None) -> None:
        if grant_id is None:
            grant_id = self.config.grant.grant_id
        if grant_id != self.config.grant.grant_id:
            raise ValueError("Unknown fixture grant")
        self._revoked = True

    def set_server_text(self, draft_id: str, text: str) -> None:
        """Trusted setup for the contract's D1 instruction-text scenario."""
        draft = self._setup_draft(draft_id)
        initial = next(d for d in self.config.drafts if d.resource == draft_id)
        if not isinstance(text, str) or draft.revision != initial.revision:
            raise ValueError("Text setup requires initial revision and string text")
        self._drafts[draft_id] = replace(draft, body=text)

    def set_server_revision(self, draft_id: str, revision: int) -> None:
        """Trusted setup for the contract's D1 revision-conflict scenario."""
        draft = self._setup_draft(draft_id)
        if type(revision) is not int or revision != self.config.conflict_revision:
            raise ValueError("Use the configured conflict revision")
        self._drafts[draft_id] = replace(draft, revision=revision)

    def _setup_draft(self, draft_id: str) -> Draft:
        if draft_id != self.config.grant.resource:
            raise ValueError("Setup mutation is limited to the delegated fixture draft")
        return self._drafts[draft_id]

    def _gate(self, action: str, resource: str, claimed_actor: Optional[str]) -> Status:
        if self._actor is None or self._user not in self.config.users:
            return Status.INVALID_CONTEXT
        if not self._online:
            return Status.OFFLINE
        if claimed_actor is not None and claimed_actor != self._actor:
            return Status.DENIED
        if self._actor in self.config.users and self._actor != self._user:
            return Status.DENIED
        if not isinstance(resource, str):
            return Status.DENIED
        if action == "read" and resource == self.config.public_resource:
            return Status.OK
        draft = self._drafts.get(resource)
        if draft is None:
            return Status.DENIED
        if self._actor in self.config.users and self._actor == draft.owner:
            return Status.OK
        grant = self.config.grant
        if (action == grant.action and resource == grant.resource
                and self._actor == grant.subject and self._user == grant.issuer
                and draft.owner == grant.issuer and not self._revoked
                and grant.start <= self._time < grant.end):
            return Status.OK
        return Status.DENIED

    def read(self, resource: str, claimed_actor: Optional[str] = None) -> Result:
        status = self._gate("read", resource, claimed_actor)
        if status != Status.OK:
            return Result(status)
        body = (self.config.public_body if resource == self.config.public_resource
                else self._drafts[resource].body)
        return Result(Status.OK, body)

    def restore(self, resource: str, claimed_actor: Optional[str] = None) -> Result:
        status = self._gate("restore", resource, claimed_actor)
        if status != Status.OK:
            return Result(status)
        cached = self._cache.get(resource)
        if cached is None or cached.owner != self._user:
            return Result(Status.NO_CACHE)
        if cached.base_revision != self._drafts[resource].revision:
            return Result(Status.CONFLICT)
        # R1: only local editor installation; server and cache are unchanged.
        self._editor = {"resource": resource, "body": cached.body, "unsent": True}
        return Result(Status.RESTORED, cached.body)

    def inspect(self) -> dict:
        """Trusted driver snapshot; never exposed as an application response."""
        return {
            "user": self._user, "actor": self._actor,
            "online": self._online, "time": self._time,
            "grant": {**asdict(self.config.grant), "revoked": self._revoked},
            "drafts": {key: asdict(value) for key, value in self._drafts.items()},
            "cache": {key: asdict(value) for key, value in self._cache.items()},
            "editor": None if self._editor is None else dict(self._editor),
        }

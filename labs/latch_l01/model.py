"""Deterministic in-memory Shared-Draft Lab, passes 1 and 2.

Policy: docs/latch-education lesson -> addendum -> R1/R2 errata.
Driver binding/setup/inspection are trusted fixture controls, not authentication.
The public adapter and teaching runner live in separate surface/visible_cases modules.
"""

from dataclasses import asdict, dataclass, replace
from enum import Enum
from typing import Dict, List, Optional, Tuple


class Status(str, Enum):
    OK = "OK"
    RESTORED = "RESTORED"
    DENIED = "DENIED"
    OFFLINE = "OFFLINE"
    NO_CACHE = "NO_CACHE"
    CONFLICT = "CONFLICT"
    INVALID_CONTEXT = "INVALID_CONTEXT"
    QUEUED = "QUEUED"
    NOT_OFFLINE = "NOT_OFFLINE"
    QUEUE_FULL = "QUEUE_FULL"
    NO_PENDING = "NO_PENDING"
    RETRY_REQUIRED = "RETRY_REQUIRED"
    ALREADY_COMPLETED = "ALREADY_COMPLETED"


class IntentState(str, Enum):
    PENDING = "PENDING"
    BLOCKED_SESSION = "BLOCKED_SESSION"
    BLOCKED_ACTOR = "BLOCKED_ACTOR"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"


@dataclass(frozen=True)
class Result:
    status: Status
    body: Optional[str] = None
    intent_id: Optional[str] = None


@dataclass(frozen=True)
class Intent:
    intent_id: str
    actor: str
    user: str
    resource: str
    state: IntentState = IntentState.PENDING


@dataclass(frozen=True)
class RecoveryEffect:
    intent_id: str
    action: str = "restore"


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
    intent_prefix: str = "intent-"
    initial_intent_sequence: int = 1


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
        self._intents: Dict[str, Intent] = {}
        self._pending_id: Optional[str] = None
        self._next_intent_sequence = self.config.initial_intent_sequence
        self._effects: List[RecoveryEffect] = []

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

    def _valid_context(self) -> bool:
        return self._actor is not None and self._user in self.config.users

    def _request_status(self) -> Optional[Status]:
        if not self._valid_context():
            return Status.INVALID_CONTEXT
        if not self._online:
            return Status.OFFLINE
        return None

    def _gate(self, action: str, resource: str, claimed_actor: Optional[str]) -> Status:
        status = self._request_status()
        if status is not None:
            return status
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

    def queue_replay(self, resource: str) -> Result:
        """Store an offline restore intent, never an authorization decision."""
        if not self._valid_context():
            return Result(Status.INVALID_CONTEXT)
        if self._online:
            return Result(Status.NOT_OFFLINE)
        if self._pending_id is not None:
            return Result(Status.QUEUE_FULL)
        intent_id = self.config.intent_prefix + str(self._next_intent_sequence)
        intent = Intent(intent_id, self._actor, self._user, resource)
        self._intents[intent_id] = intent
        self._pending_id = intent_id
        self._next_intent_sequence += 1
        return Result(Status.QUEUED, intent_id=intent_id)

    def reconnect_and_replay(self) -> Result:
        if not self._valid_context():
            return Result(Status.INVALID_CONTEXT)
        self._online = True
        if self._pending_id is None:
            return Result(Status.NO_PENDING)
        intent = self._intents[self._pending_id]
        if intent.state != IntentState.PENDING:
            return Result(Status.RETRY_REQUIRED)
        return self._execute_intent(intent, block_on_mismatch=True)

    def retry(self, intent_id: str) -> Result:
        status = self._request_status()
        if status is not None:
            return Result(status)
        intent = self._intents.get(intent_id)
        if intent is None or intent.state in (IntentState.REJECTED, IntentState.PENDING):
            # AX-L01-01: a PENDING intent exists but is not retry-eligible.
            return Result(Status.NO_PENDING)
        if intent.state == IntentState.COMPLETED:
            if self._user != intent.user or self._actor != intent.actor:
                return Result(Status.DENIED)
            return Result(Status.ALREADY_COMPLETED)
        return self._execute_intent(intent, block_on_mismatch=False)

    def _execute_intent(self, intent: Intent, block_on_mismatch: bool) -> Result:
        mismatch = None
        if self._user != intent.user:
            mismatch = IntentState.BLOCKED_SESSION
        elif self._actor != intent.actor:
            mismatch = IntentState.BLOCKED_ACTOR
        if mismatch is not None:
            if block_on_mismatch:
                self._intents[intent.intent_id] = replace(intent, state=mismatch)
            return Result(Status.DENIED)

        # Origin equality is not authority: restore rechecks current policy/cache.
        result = self.restore(intent.resource)
        if result.status == Status.RESTORED:
            state = IntentState.COMPLETED
            self._effects.append(RecoveryEffect(intent.intent_id))
        elif result.status in (Status.DENIED, Status.NO_CACHE, Status.CONFLICT):
            state = IntentState.REJECTED
        else:
            return result
        self._intents[intent.intent_id] = replace(intent, state=state)
        self._pending_id = None
        return result

    def inspect(self) -> dict:
        """Trusted driver snapshot; never exposed as an application response."""
        return {
            "user": self._user, "actor": self._actor,
            "online": self._online, "time": self._time,
            "grant": {**asdict(self.config.grant), "revoked": self._revoked},
            "drafts": {key: asdict(value) for key, value in self._drafts.items()},
            "cache": {key: asdict(value) for key, value in self._cache.items()},
            "editor": None if self._editor is None else dict(self._editor),
            "pending_intent_id": self._pending_id,
            "intents": {key: {**asdict(value), "state": value.state.value}
                        for key, value in self._intents.items()},
            "completed_ids": [key for key, value in self._intents.items()
                              if value.state == IntentState.COMPLETED],
            "next_intent_sequence": self._next_intent_sequence,
            "effects": [asdict(effect) for effect in self._effects],
        }

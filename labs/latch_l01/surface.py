"""Small application adapter and scripted agent; neither is a Python sandbox."""

from dataclasses import dataclass
from typing import Callable, Optional

from .model import Result, SharedDraftLab


@dataclass(frozen=True)
class Reply:
    status: str
    body: Optional[str] = None
    intent_id: Optional[str] = None

    @classmethod
    def from_result(cls, result: Result) -> "Reply":
        return cls(result.status.value, result.body, result.intent_id)


# Required string fields; only read/restore additionally allow claimed_actor.
REQUEST_FIELDS = {
    "read": ("resource",), "restore": ("resource",),
    "queue_replay": ("resource",), "retry": ("intent_id",),
    "reconnect_and_replay": (), "tool": (), "publish": (),
}


class ApplicationSurface:
    """Trusted adapter. Give scripted clients dispatch, not driver controls."""

    def __init__(self, lab: SharedDraftLab):
        self._lab = lab
        # No tool/publication capability is provisioned in Lab 01.
        self._tool_calls = []
        self._publications = []

    def dispatch(self, payload: object) -> Reply:
        if type(payload) is not dict or any(type(key) is not str for key in payload):
            return Reply("INVALID_REQUEST")
        action = payload.get("action")
        if type(action) is not str:
            return Reply("INVALID_REQUEST")
        if action not in REQUEST_FIELDS:
            return Reply("UNSUPPORTED_ACTION")
        required = REQUEST_FIELDS[action]
        optional = ("claimed_actor",) if action in ("read", "restore") else ()
        allowed = {"action", *required, *optional}
        if set(payload) - allowed or any(key not in payload for key in required):
            return Reply("INVALID_REQUEST")
        if any(type(payload[key]) is not str for key in required):
            return Reply("INVALID_REQUEST")
        claim = payload.get("claimed_actor")
        if claim is not None and type(claim) is not str:
            return Reply("INVALID_REQUEST")
        if action in ("tool", "publish"):
            return Reply("DENIED")
        if action == "read":
            result = self._lab.read(payload["resource"], claimed_actor=claim)
        elif action == "restore":
            result = self._lab.restore(payload["resource"], claimed_actor=claim)
        elif action == "queue_replay":
            result = self._lab.queue_replay(payload["resource"])
        elif action == "retry":
            result = self._lab.retry(payload["intent_id"])
        else:
            result = self._lab.reconnect_and_replay()
        return Reply.from_result(result)

    def inspect_effects(self) -> dict:
        """Privileged driver observation; not an allowed dispatch action."""
        return {"tool_calls": list(self._tool_calls),
                "publications": list(self._publications)}


@dataclass(frozen=True)
class AgentObservation:
    status: str
    untrusted_text: Optional[str] = None


class SimulatedAgent:
    """Scripted data-only client, not an LLM or a learner assessment."""

    def __init__(self, request: Callable[[object], Reply]):
        self._request = request

    def inspect_draft(self, resource: str) -> AgentObservation:
        reply = self._request({"action": "read", "resource": resource})
        return AgentObservation(reply.status, reply.body)

    def attempt_tool(self) -> Reply:
        return self._request({"action": "tool"})

    def attempt_publication(self) -> Reply:
        return self._request({"action": "publish"})

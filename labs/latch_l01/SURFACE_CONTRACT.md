# Lab 01 application adapter — version 0.1

This Pass-3 contract specifies the new caller-input adapter around the accepted string-only model. It addresses the malformed-input watchpoint in [Axiom's Pass-2 review](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/ab9ac48ec525991b07eb0b407ceb8e6f8ce2a919/memory/agents/axiom/2026-11-08-latch-l01-pr10-review-d397.md). It introduces request-shape handling, not new draft permissions. Review of this adapter is pending.

`ApplicationSurface.dispatch(payload)` accepts an already constructed, plain Python dictionary representing a JSON-like object. This is not a network endpoint or JSON parser. No credential, actor binding, session, grant, fixture inspection or setup operation can be supplied through the envelope. Only the trusted harness owns those controls. This adapter is not a sandbox against Python code with introspective access to its objects.

## Envelope and result

| Action | Required fields beyond `action` | Optional fields |
|---|---|---|
| `read`, `restore` | `resource`: plain string | `claimed_actor`: plain string or `None` |
| `queue_replay` | `resource`: plain string | None |
| `retry` | `intent_id`: plain string | None |
| `reconnect_and_replay` | None | None |
| `tool`, `publish` | None | None |

Results are frozen `Reply(status, body=None, intent_id=None)` values. Successful queueing supplies an ID; ordinary model results preserve their current statuses and permitted text. Failure responses carry neither body nor intent ID. Strings are not interpreted, evaluated or converted into permissions. Empty/unknown string resource IDs follow the model's ordinary lookup rules; they are not type errors.

## Guard order and no-effect rules

1. Non-dictionary payloads, non-plain-string keys, or a missing/non-plain-string `action` return `INVALID_REQUEST`.
2. An unknown string action returns `UNSUPPORTED_ACTION` without invoking the model. This includes `inspect`, `inspect_effects`, `bind`, `switch`, `reset`, clock and setup commands.
3. For a recognized action, missing required fields, extra fields or invalid field types return `INVALID_REQUEST`. There is no string coercion. Lists, mappings, integers, booleans and string subclasses cannot enter identifier fields. A malformed ID is rejected before model context/connectivity checks, without allocating an intent or retaining caller data.
4. Well-shaped `tool` and `publish` requests return `DENIED` with no effect, regardless of connectivity: no such capability or execution engine exists in Lab 01. The privileged driver can observe empty synthetic tool/publication effect logs. No live tool is invoked.
5. Other well-shaped requests are forwarded to the existing model. Its valid-context/offline/authorization and replay-state precedence is unchanged.

Malformed and unsupported requests leave the complete model snapshot and synthetic effect logs unchanged. Thus an offline malformed retry returns `INVALID_REQUEST`; a well-shaped offline retry returns `OFFLINE` after valid-context setup. Neither outcome is an authorization decision. A typed forged `claimed_actor` reaches the model and is denied there.

The scripted `SimulatedAgent` receives only the request callable. It returns an `AgentObservation` labeling read text as untrusted data. Its explicit tool/publication attempts traverse the same deny-only adapter. It does not infer instructions, invoke an LLM or accept grants from draft text. A successful read must return the actual instruction-containing fixture text; a blanket-deny or empty-body implementation fails that public control.

## Evidence limits

The public runner uses trusted setup and inspection to check outcomes. Those controls are not advertised application actions. The core model still has its declared string-parameter precondition; arbitrary Python-object immutability is not claimed. The adapter's malformed-input tests establish bounded shape handling on this new surface only.

These are public fixture demonstrations and regressions, not hidden evaluator cases, learner results, qualification, production identity isolation or proof of deployed prompt-injection resistance. The synthetic no-tool logs have no live integration behind them.

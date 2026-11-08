# Shared-Draft Lab — public teaching fixture

This is a deterministic, in-memory teaching fixture. It implements direct read authorization, local recovery, and immutable-origin replay/retry from the accepted [lesson](../../docs/latch-education/Latch_L01_Instructional_Checkpoint.md), [addendum](../../docs/latch-education/Latch_L01_Review_Addendum.md) and [R1/R2 errata](../../docs/latch-education/Latch_L01_R1_R2_Errata.md), in that precedence order. The [three-pass plan](../../docs/latch-education/L01_FIXTURE_IMPLEMENTATION_PLAN.md) defines this slice.

Run the public fixture regression controls from the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_latch_l01*.py' -v
```

A small direct demonstration:

```python
from labs.latch_l01.model import SharedDraftLab

lab = SharedDraftLab()
lab.bind("X")                         # trusted harness binding, not request data
print(lab.read("D1").status.value)    # OK: current scoped delegation
print(lab.read("D2").status.value)    # DENIED
lab.bind("A")
print(lab.restore("D1").body)         # local-A1: local unsent recovery
print(lab.read("D1").body)            # server-D1: server content unchanged
```

## Interfaces and state

`SharedDraftLab` takes a frozen `FixtureConfig`; its immutable default records hold all initial principals, drafts, cache, grant, clock and public text. Each instance has isolated mutable state. `reset()` restores that configuration. The fixture has no dependency on wall time, files, network or credentials.

| Surface | Interface and trust |
|---|---|
| Application requests | `read(resource, claimed_actor=None)` and `restore(resource, claimed_actor=None)` return a frozen `Result(status, body, intent_id)`; the new optional `intent_id` defaults to `None`, preserving Pass-1 construction and equality. Only successful queueing supplies an ID. Failures carry no body. Resource and claimed actor are request data. |
| Harness context | `switch(user)` clears the editor and requester binding; the driver then calls `bind(actor)`. Binding is trusted out-of-band setup, not a callable user-request field. Missing/unknown binding produces `INVALID_CONTEXT`; a bound human in another user's session is denied by policy. |
| Harness controls | `online(bool)`, `advance(non_decreasing_integer_tick)`, and `revoke(grant_id)` control connectivity, time and G1. No renewal or privilege expansion is implemented. |
| Scenario setup | `set_server_text(D1,text)` operates at D1's initial revision; `set_server_revision(D1,2)` creates the specified conflict. Invalid trusted setup raises `ValueError`; it is not an authorization response. |
| Driver inspection | `inspect()` returns detached synthetic state, including private bodies, for assertions. It is privileged fixture inspection and must never be exposed as an application response. |

Valid-context offline server requests return `OFFLINE` before authorization is evaluated. Online checks use the bound actor and current session, never a supplied identity claim. A can read both owned drafts and restore cached D1; uncached D2 gives `NO_CACHE` only after authorization. X may read D1 only under current G1 in A's session. X and Y can read public H in either active user session without a private-draft grant. Current time must be within G1's inclusive start and exclusive end.

Successful restore installs local unsent editor text without changing server body/revision or cache text/base. For direct reads/restores, denial, offline, missing-cache and conflict results leave existing data and editor unchanged. Replay also records its specified intent-state transitions; it preserves server/cache and leaves the editor unchanged on failure. Switching users clears the editor and binding while retaining A's cache for later A recovery.

## What is actually checked

The public tests specify expected statuses and real allowed text independently of the model's policy helper. They cover the user/actor/resource read and restore matrices, forged claims, expiry boundary, revocation during offline time, legitimate recovery after revocation, offline precedence, invalid context, local-only effects, missing cache, conflict, switch/back recovery, detached inspection and reset/isolation. Failure cases compare full driver state and require a body-free response. Matrix controls include valid owner, delegated and public neighbors.

An instruction-like string is read verbatim as inert text without changing fixture state. This does not exercise a reasoning agent or tool dispatch and cannot establish prompt-injection resistance in a deployed system. Tests are public fixture regressions authored by the implementer; independent implementation review remains pending.

## Queue and retry — pass 2

`queue_replay(resource)` derives its immutable originating actor and user from the current trusted binding. It queues an offline restore request, not a grant. Valid context is required first; online queueing gives `NOT_OFFLINE` before the occupied-slot check; offline occupied queueing gives `QUEUE_FULL`. Refusals allocate no ID. Queueing itself neither reads draft text nor performs restoration.

`online(True)` alone never replays. `reconnect_and_replay()` connects and attempts only a `PENDING` intent. A session mismatch takes precedence over actor mismatch, producing `BLOCKED_SESSION` or `BLOCKED_ACTOR` and a body-free `DENIED`. Repeated reconnect calls for blocked work give `RETRY_REQUIRED`. Only explicit `retry(id)` can resume blocked work; both current actor and session must match the origin, then `restore` checks current policy, cache availability and revision again. A mismatched retry preserves the existing blocked state.

An online retry of a still-`PENDING` ID returns `NO_PENDING` (no retry-eligible intent), preserving the valid automatic-replay path. Rejected/unknown IDs also give `NO_PENDING`. Offline retry returns `OFFLINE` without changing state, regardless of ID state, after valid-context setup.

Success installs local unsent text, records one `{intent_id, action}` recovery effect, marks `COMPLETED` and frees the pending slot. Permission denial, missing cache and conflict mark `REJECTED` and free the slot without a recovery effect. Completed-ID retry checks origin before returning `ALREADY_COMPLETED`; it never reinstalls editor text or consumes another pending intent. Completed and rejected records persist only for the current fixture run. Reset clears them, effects and the ID sequence; test cases must not carry references across reset epochs.

`inspect()` now includes pending ID, detached origin/state records, completed IDs, next sequence and recovery effects. These remain privileged driver data. Intent/effect records contain no draft bodies. There is deliberately no cancellation: a blocked slot awaits its origin's explicit retry or trusted reset. Direct online owner recovery remains available.

A replay example (trusted driver calls):

```python
lab = SharedDraftLab()
lab.online(False)
queued = lab.queue_replay("D1")
lab.switch("B")
lab.bind("B")
print(lab.reconnect_and_replay().status.value)  # DENIED, blocked session
lab.switch("A")
lab.bind("X")
print(lab.retry(queued.intent_id).status.value) # DENIED, no actor substitution
lab.bind("A")
print(lab.retry(queued.intent_id).status.value) # RESTORED
print(lab.retry(queued.intent_id).status.value) # ALREADY_COMPLETED
```

The 24 public replay tests cover the two Axiom counterexamples, both blocked origins, explicit retry and fresh revision checking, agent denial versus owner recovery, rejected-slot reuse, old completed IDs alongside new pending work, offline precedence, no-cache/conflict outcomes, reset and duplicate-effect suppression. Expected responses and state are specified from the contract; they do not use the policy helper to construct an oracle. These are implementer-authored fixture tests pending independent review, not learner qualification trials.

## Public teaching runner — pass 3

Run the 16 named public teaching cases from the repository root:

```bash
python3 -m labs.latch_l01
python3 -m labs.latch_l01 --json
```

The first nine cases correspond to the original lesson; later cases cover identity claims, missing cache, actor retry/idempotence, the two Axiom counterexamples, old-completed/new-blocked isolation, malformed identifiers and harness separation. Each case gets a fresh fixture. Expected decisions and text are literal public oracles in `visible_cases.py`, not computed with the model's policy helper.

The CLI exits 0 only for a nonempty set of passing cases; a failed comparison, case exception or empty run exits 1. JSON output includes `successful`, case counts and per-check outcomes, and always states `qualification_assessed: false`. Unit tests deliberately substitute blanket-deny, empty-read and server-writing fixtures to check that the public controls fail. These are tests of the teaching runner, not learner scores.

The new [surface contract](SURFACE_CONTRACT.md) defines request shape and precedence before untyped caller data reaches the model. Malformed identifiers return `INVALID_REQUEST` without state changes. Harness commands return `UNSUPPORTED_ACTION`. Well-shaped application requests preserve the existing model rules. The scripted agent receives only a request callable and labels returned draft text as untrusted. It has no language model or interpreter; explicit tool/publication requests are denied and synthetic effect logs remain empty. No live tool engine exists behind those logs.

An [independent implementation review handoff](../../docs/latch-education/L01_PASS3_REVIEW_HANDOFF.md) accompanies this slice. Current-head acceptance remains pending. Until that review and Latch's gate are complete, do not treat these public examples as an accepted learner assessment.

## Deferred and excluded

The edit API, delegation issuance/renewal, live publication, cancellation and production agent integrations remain unimplemented. No hidden evaluator cases are supplied. The surface is an already-parsed dictionary adapter, not a network/JSON-parser or Python-sandbox boundary.

No production authentication, storage isolation, cryptography, OS compromise, learner exercise or skill qualification is claimed. All driver controls are trusted test setup, not security barriers against Python code with access to the fixture object. Follow-up work stays gated by Latch's current-head acceptance.

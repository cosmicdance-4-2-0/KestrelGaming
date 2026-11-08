# Shared-Draft Lab — pass 1

This is a deterministic, in-memory teaching fixture. It implements direct read authorization and local recovery from the accepted [lesson](../../docs/latch-education/Latch_L01_Instructional_Checkpoint.md), [addendum](../../docs/latch-education/Latch_L01_Review_Addendum.md) and [R1/R2 errata](../../docs/latch-education/Latch_L01_R1_R2_Errata.md), in that precedence order. The [three-pass plan](../../docs/latch-education/L01_FIXTURE_IMPLEMENTATION_PLAN.md) defines this slice.

Run the public pass-1 regression controls from the repository root:

```bash
python3 -m unittest discover -s tests -p test_latch_l01.py -v
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
| Application requests | `read(resource, claimed_actor=None)` and `restore(resource, claimed_actor=None)` return a frozen `Result(status, body)`. Failures carry no body. Resource and claimed actor are request data. |
| Harness context | `switch(user)` clears the editor and requester binding; the driver then calls `bind(actor)`. Binding is trusted out-of-band setup, not a callable user-request field. Missing/unknown binding produces `INVALID_CONTEXT`; a bound human in another user's session is denied by policy. |
| Harness controls | `online(bool)`, `advance(non_decreasing_integer_tick)`, and `revoke(grant_id)` control connectivity, time and G1. No renewal or privilege expansion is implemented. |
| Scenario setup | `set_server_text(D1,text)` operates at D1's initial revision; `set_server_revision(D1,2)` creates the specified conflict. Invalid trusted setup raises `ValueError`; it is not an authorization response. |
| Driver inspection | `inspect()` returns detached synthetic state, including private bodies, for assertions. It is privileged fixture inspection and must never be exposed as an application response. |

Valid-context offline server requests return `OFFLINE` before authorization is evaluated. Online checks use the bound actor and current session, never a supplied identity claim. A can read both owned drafts and restore cached D1; uncached D2 gives `NO_CACHE` only after authorization. X may read D1 only under current G1 in A's session. X and Y can read public H in either active user session without a private-draft grant. Current time must be within G1's inclusive start and exclusive end.

Successful restore installs local unsent editor text without changing server body/revision or cache text/base. Denial, offline, missing-cache and conflict results leave existing data and editor unchanged. Switching users clears the editor and binding while retaining A's cache for later A recovery.

## What is actually checked

The public tests specify expected statuses and real allowed text independently of the model's policy helper. They cover the user/actor/resource read and restore matrices, forged claims, expiry boundary, revocation during offline time, legitimate recovery after revocation, offline precedence, invalid context, local-only effects, missing cache, conflict, switch/back recovery, detached inspection and reset/isolation. Failure cases compare full driver state and require a body-free response. Matrix controls include valid owner, delegated and public neighbors.

An instruction-like string is read verbatim as inert text without changing fixture state. This does not exercise a reasoning agent or tool dispatch and cannot establish prompt-injection resistance in a deployed system. Tests are public fixture regressions authored by the implementer; independent implementation review remains pending.

## Deferred and excluded

Pass 2 will implement `queue_replay`, `reconnect_and_replay`, `retry`, pending/blocked/terminal states, completed IDs and recovery-effect logs. Those methods are absent here; there are no success stubs. Pass 3 will add the public case runner and simulated agent/tool effect checks. The agent-context simulation, edit API, delegation issuance/renewal, publication and cancellation are not implemented in pass 1.

No production authentication, storage isolation, cryptography, OS compromise, hidden evaluator cases, learner exercise or skill qualification is claimed. All driver controls are trusted test setup, not security barriers against Python code with access to the fixture object. Follow-up work stays gated by Latch's current-head acceptance.

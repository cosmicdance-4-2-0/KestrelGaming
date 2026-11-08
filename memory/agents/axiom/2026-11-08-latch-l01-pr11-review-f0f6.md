---
schema: 1
id: 2026-11-08-latch-l01-pr11-review-f0f6
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom-review-session
created: 2026-11-08
updated: 2026-11-08
sources: "LATCH-L01-PASS3-REVIEW-01; KestrelGaming PR #11 head f0f6cbbddcec52652233f9bca847a51dc5316b87 versus base ca49d6eabd6e6f17bfd139efd0d3804a16d351c8; local full-source verification, 102-test execution, CLI runs and linked public reviewer probes; Axiom home ab9ac48ec525991b07eb0b407ceb8e6f8ce2a919."
---

# REQUEST CHANGES — Pass 3 runner review at f0f6cbb

## Summary

**One bounded P2 finding blocks acceptance of the standalone teaching runner.** A fixture that writes server content only during queued restoration still produces 16/16 passing public cases and exit 0 in both CLI modes. The successful replay cases omit the server/cache stability observation required by R1 and the implementation plan.

The shipped core model does not perform that write. Its executable AST is unchanged from the accepted Pass-2 baseline, excluding the module docstring. The existing focused Pass-2 regression rejects the injected faulty variant. This finding concerns the new public runner's oracle, not a demonstrated unauthorized write in the current core.

The new adapter correctly closes the previous malformed-ID observation for its advertised request envelope. Preserve that implementation, the core, existing tests and explicit evidence limits.

| Source receipt | Exact source |
| --- | --- |
| Assignment | LATCH-L01-PASS3-REVIEW-01, owner-delivered handoff |
| PR | [KestrelGaming #11](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/11), mothlight/latch-education → agents/latch-v1 |
| Reviewed head | `f0f6cbbddcec52652233f9bca847a51dc5316b87` |
| Direct parent / PR base | `ca49d6eabd6e6f17bfd139efd0d3804a16d351c8` |
| Reconstructed head tree | `d74b52c4f868fe4ceafd9061baae6d3ea6ef43bc` |
| Reconstructed base tree | `3556616e95d0a8db9ba9de16e82627307d3981e8` |
| Axiom identity / memory home | agents/axiom-v1 at `ab9ac48ec525991b07eb0b407ceb8e6f8ce2a919` |
| Environment | Managed Linux x86_64 container, Python 3.12.14, Git 2.52.0; GitHub connector and local materialization |
| Scope | Independent implementation review; no fixes, merge, hidden evaluator cases or learner assessment |

Read the handoff, accepted lesson/addendum/errata and three-pass plan, new surface contract, adapter, scripted agent, public cases, CLI, README and new tests. Retained Axiom's loaded identity and shared procedures. Compared all ten changed files with the actual base; existing tests and executable core behavior are preserved. Initial assessment was recorded before inspecting PR discussion conclusions; the returned PR #11 discussion was empty.

## Evidence

### AX-L01-P3-01 — P2: queued server writes can pass the entire public runner

**Locations:** [visible_cases.py switched_replay, line 102](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0f6cbbddcec52652233f9bca847a51dc5316b87/labs/latch_l01/visible_cases.py#L102), successful replay/retry cases at lines 169–213, and [runner mutation tests at test_latch_l01_surface.py line 173](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0f6cbbddcec52652233f9bca847a51dc5316b87/tests/test_latch_l01_surface.py#L173).

**Required invariant:** R1 says a successful queued restore installs local unsent editor text without changing server body/revision or cached text/base. The implementation plan requires server/cache stability observations where consequential. The existing C07 owner-positive case checks these for direct restoration, but the queued success paths do not compare those stores before/after recovery.

**Minimal controlled variant:** use the runner's documented trusted factory override to inject this intentionally broken fixture:

```python
class QueuedWriteOnly(SharedDraftLab):
    def _execute_intent(self, intent, block_on_mismatch):
        result = super()._execute_intent(intent, block_on_mismatch)
        if result.status == Status.RESTORED:
            self._drafts[intent.resource] = replace(
                self._drafts[intent.resource], body=result.body)
        return result

outcomes = run_visible_cases(QueuedWriteOnly)
assert all(case.passed for case in outcomes)  # observed: 16/16
```

**Preconditions and sequence:** fresh default fixture, online A actor/A session; go offline; queue D1; reconnect. The variant returns `RESTORED/local-A1`, records the normal single recovery effect and additionally changes server D1 body from `server-D1` to `local-A1`. Direct restoration remains unchanged, so C07 does not expose this fault.

| Observation | Expected | Executed result |
| --- | --- | --- |
| Public cases on the queued-only writing variant | At least a queued-recovery case fails R1 stability | All 16 cases pass |
| Text CLI with that runner factory injected | Exit 1 and visible failed check | Exit 0, “16/16 public cases passed” |
| JSON CLI with that runner factory injected | successful=false, failed>0, exit 1 | successful=true, passed=16, failed=0, exit 0 |
| Existing Pass-2 `test_success_has_one_local_effect_no_server_or_cache_write` on same variant | Reject the server write | Fails as expected |

**Impact:** a consequential recovery-versus-synchronization violation can be absent from the standalone teaching run's reported failures. This does not establish that the complete repository suite accepts the bad model; the focused regression already catches it. The demonstration uses controlled test instrumentation, not an application attack or an edit to the shipped model.

**Smallest correction:** capture/assert server draft and cache snapshots around the public successful queued restoration path(s), including the body/revision and text/base fields. Add this queued-only mutation as a public runner negative control and verify text/JSON failure reporting. A two-store comparison in an existing queued-positive case can catch the demonstrated class; preserve explicit observations in other consequential recovery scenarios as appropriate. No new production authorization, model rewrite or general mutation framework is requested.

**Acceptance check:** retain the real model's 16/16 successful run and all legitimate neighbors, while this variant causes an attributable R1 comparison failure, successful=false and nonzero CLI exit. Keep the original oracle rather than adjusting expected server content to the mutation.

### Adapter and trust boundary results

[ApplicationSurface.dispatch](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0f6cbbddcec52652233f9bca847a51dc5316b87/labs/latch_l01/surface.py#L37) implements the new surface contract's stated order:

1. Plain dictionary and plain-string keys/action.
2. Unknown string action → `UNSUPPORTED_ACTION`, before recognized-action field validation.
3. Required/optional field and exact-type checks → `INVALID_REQUEST`.
4. Well-shaped deny-only tool/publication calls → `DENIED`, without model dispatch.
5. Well-shaped model operations retain existing context/connectivity/authorization/replay precedence.

I executed **570** combinations of malformed, unsupported and deny-only envelopes across online, offline, invalid-context, occupied, blocked and completed fixture conditions. Instrumented model entry points recorded **zero calls** for these requests. Full model snapshots and synthetic effect logs were unchanged. Tests included mutable/unhashable identifiers, booleans/integers/bytes/tuples, string/dictionary subclasses, forged extra actor fields, and an object whose string conversion would raise if attempted. No coercion occurred.

The previous list-resource alias and list-retry exception are rejected at this adapter before the raw string-only model is called. The raw model's typed precondition remains documented, rather than being silently changed. Valid owner, delegated and public neighbors still return real expected text; typed forged claims reach the existing authorization check and deny.

Harness setup/inspection actions have no advertised dispatch route. The scripted client receives the dispatch callable; authorized instruction-containing text reaches it verbatim as `untrusted_text`. Explicit tool/publication attempts are denied with no model or synthetic-effect changes. The adapter is not a Python sandbox; direct object introspection and harness access remain outside the asserted boundary.

### Public cases, runner and CLI results

The first nine named cases correspond to the original visible sequences. Cases 10–16 add forged identity, missing cache, actor retry/idempotence, PENDING/full conjunctions, old-completed/new-blocked work, malformed IDs and harness separation. These contain meaningful literal expected statuses/text and state checks, with the queued-store observation gap above. Expected decisions do not call the core authorization helper.

The runner correctly rejects separately injected blanket-deny reads, empty successful read bodies, and writes performed by the shared direct `restore` method. Both CLI modes exit 1 for each of those variants. It retains all 16 outcomes and error strings for a factory that raises, rather than silently dropping failed cases. Empty runs exit 1 with successful=false. Each normal case has checks; an empty check list cannot pass.

Normal JSON reports a public fixture run with qualification_assessed=false. Text output retains failed-check details and case errors. These presentation/exit mechanisms work; the blocker is the missing queued-state comparison before success is calculated.

### Independently reproduced execution

| Check at reviewed head | Observed result |
| --- | --- |
| Full source materialization | All 89 head blobs verified, including binary avatar |
| Base and head Git trees | Independently reconstructed and matched published commits |
| Core semantic comparison | AST identical to base after excluding module docstring |
| `python3 -m labs.latch_l01` | PASS, 16/16 cases, exit 0 |
| `python3 -m labs.latch_l01 --json` | PASS, passed=16, failed=0, successful=true, qualification_assessed=false; 188 per-check observations |
| `python3 -m unittest discover -s tests -v` | PASS, 102 tests; all 84 previous tests retained, 18 added |
| `python3 tools/validate_seed.py` | PASS |
| `git diff --check 3556616e95d0a8db9ba9de16e82627307d3981e8 d74b52c4f868fe4ceafd9061baae6d3ea6ef43bc` | PASS for the complete PR delta |
| Reviewer input-surface matrix | PASS, 570 no-model-call/no-mutation requests |
| Reviewer runner/CLI mutations | Three supplied fault classes rejected; queued-only server write escapes as documented above |

The [reproducible public reviewer probe](evidence/2026-11-08-l01-pass3-review-probes.py) includes the input matrix, mutation controls, text/JSON checks, case-error/empty-run checks and the existing-regression comparison:

```sh
python3 memory/agents/axiom/evidence/2026-11-08-l01-pass3-review-probes.py PATH_TO_REVIEWED_REPOSITORY
```

These are public synthetic implementation-review controls, not hidden learner trials. The deliberate mutant assertions characterize current behavior and must be revised when the runner correction makes that mutant fail.

## Decision and next action

Return one bounded runner correction to Mothlight on the existing working branch, then re-review the exact revised head. Preserve the core and adapter. Latch's separate exact-head acceptance remains pending, and PR #11 remains draft. No learner evaluation or qualification follows from this review.

Only this Axiom continuity record, its index and linked public evidence are changed by this review. No target implementation, tests, contract, Latch identity/memory, PR comment/review or merge is changed. Own-home validation defects remain separately recorded and are checked against their unchanged baseline during persistence.

## Revisit when

Mothlight adds the queued-store observation and mutation control, PR head/base changes, Latch issues an integration decision, or later public/evaluator work changes the asserted trust surface.

---
schema: 1
id: 2026-11-08-l01-pr11-pass3-acceptance-cbf9-lk17
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-review-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "GitHub PR #11 at cbf9a0c5e05b42b7d9fb2aa128ed41ca4878e3d0 versus old f0f6cbbddcec52652233f9bca847a51dc5316b87 and base ca49d6eabd6e6f17bfd139efd0d3804a16d351c8; Axiom followup at f0ec29948cf10f60e627c8c0696209faed586bc4, memory/agents/axiom/2026-11-08-latch-l01-pr11-followup-cbf9.md and public evidence/2026-11-08-l01-pass3-followup-probes.py; Latch submitted GitHub review COMMENT 5820130848."
---

# Latch — PR #11 Pass 3 acceptance

**Assignment:** LATCH-L01-PASS3-REVIEW-01  
**PR:** https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/11  
**Exact accepted head:** `cbf9a0c5e05b42b7d9fb2aa128ed41ca4878e3d0`  
**Prior rejected head:** `f0f6cbbddcec52652233f9bca847a51dc5316b87`  
**PR base:** `ca49d6eabd6e6f17bfd139efd0d3804a16d351c8`  
**Verdict:** **ACCEPT integration of Pass 3 for this exact head**, subject to architect/owner merge decision. Prior P2 runner coverage finding AX-L01-P3-01 CLOSED.
**GitHub review:** COMMENT ID `5820130848`; not a GitHub APPROVE or merge.

## Summary

Mothlight repaired the sole known Pass 3 public-oracle blocker without changing the already accepted core authorization model or application adapter. The correction is exactly one commit touching three files: `labs/latch_l01/visible_cases.py`, `tests/test_latch_l01_surface.py` and `labs/latch_l01/README.md`. Axiom independently validated the corrected runner at the same exact head and supplies reproducible negative controls. I have accepted the correction and documented that the implementation is a bounded public teaching fixture, not a completed learning assessment or a production security system.

## Evidence

**Direct Latch inspection through GitHub connector:**
- PR #11 remains open/draft, same head and base when reviewed. Comparison `f0f6cbb...` → `cbf9a0c...` returned exactly one commit and three files, without altering `model.py`, `surface.py` or `__main__.py`.
- The exact new runner `labs/latch_l01/visible_cases.py` (Git blob `c2f39b528e55ef7370116fa56cdc9c52d7dc4296`) introduces `CaseContext.recover`. It captures `before = lab.inspect()` and `after = lab.inspect()` across an expected `RESTORED` and asserts `drafts` and `cache` records equal the detached pre-state. It invokes the method five times: C05 session-blocked retry, C12 actor-blocked retry, C13 automatic pending replay, and C14's two completions.
- The new surface tests (Git blob `687882ff7c4e2b764db2c9dc8b415a52813e7c81`) define `QueuedWriteOnly`, `QueuedRetryWriteOnly`, `QueuedCacheWriteOnly`, and `QueuedRevisionWriteOnly` fault variants. Tests require named R1 check failures and truthful text/JSON CLI exit 1 for the queued server-write variant. The original valid runner and legitimate owner/delegate/public neighbors are retained.
- [Axiom acceptance](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0ec29948cf10f60e627c8c0696209faed586bc4/memory/agents/axiom/2026-11-08-latch-l01-pr11-followup-cbf9.md) inspected at Git blob `0e7ef5743dad2b7256514436ba363ec26c17c31d` and [reproducible probe script](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0ec29948cf10f60e627c8c0696209faed586bc4/memory/agents/axiom/evidence/2026-11-08-l01-pass3-followup-probes.py) at blob `98e50205b9866a53d45f6164d7ea2d475f2fdb72`.

**Axiom's separately attributed executable results (not rerun by Latch):** 106/106 full repository tests PASS, 16/16 real public cases PASS, 570 no-mutation adapter probes PASS; queued-only server-write mutant FAILS C05/C12/C13/C14, text/JSON exit 1, JSON `successful=false`, `passed=12` and `failed=4`. Additional injected revision/cache/retry-only mutations are caught; validator and complete diff whitespace checks PASS. Axiom independently reconstructed the full head tree `c63f58ea78d264b2cbc0ec687ac3094c2baa3d99`. These are direct observations *reported by Axiom*, not firsthand Latch execution.

**CI/authority limits:** GitHub returned no commit statuses/workflow runs for the reviewed SHA. GitHub's shared-account rules prevent a formal self-approval; only COMMENT with explicit engineering verdict was submitted. Latch did not merge PR #11, create hidden learner trials, or assess his own L01 competency.

## Change in evidence, decision, and scope

Previous PR #11 review at `f0f6cbb...`: **REQUEST CHANGES**, because an intentionally broken queued-write-only fixture generated a false-positive 16/16 public runner pass. The Pass 2 regression already detected it; the core was not proven vulnerable.

Current PR #11 review at `cbf9a0c...`: **ACCEPT**. The runner now observes exactly the R1 state invariant it claims to test; deliberate queued server/cache mutations reliably fail, and valid neighboring operations remain accepted. This is a revision-specific correction and does not retroactively modify the earlier report.

The teaching fixture remains restricted to deterministic in-memory simulation: not a Python sandbox, no live tools or publication, no deployed authentication, no unrestricted prompt-injection claim. The public runner is a training/example oracle, not an independent test of Latch's security engineering competence. The reference seven's identity/agent-memory contracts are unaffected.

## Next decisive check

The architect/authorized integrator may complete the PR #11 workflow after considering full repository gates. A separate future owner-approved assignment should introduce independent learner-facing L01 assessments and fair held-out evaluation under source provenance, explicit false-positive cases and transparent promotion criteria. The original eighteen-skill roadmap remains draft; no new skills are declared qualified merely because the teaching fixture now passes its own public checks.

## Revisit when

PR head/base changes, further reproducible counterexamples appear, integration changes behavior, or a controlled learner trial establishes new performance evidence.

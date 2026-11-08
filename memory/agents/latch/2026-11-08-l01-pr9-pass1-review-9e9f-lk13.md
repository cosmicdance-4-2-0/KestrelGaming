---
schema: 1
id: 2026-11-08-l01-pr9-pass1-review-9e9f-lk13
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-review-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "GitHub PR #9 source head 9e9f311bbb83e6d8f59b5dafa125ff4d48679589, base 35e03010b505ee59002e28c190bf668a33f0256b; labs/latch_l01/model.py Git blob 594c02e1ee1c2e8d60664d63ef3feb8d19b9fd67; tests/test_latch_l01.py Git blob c5cb2f190c57048d64df3378470323d6b14bfd93; Latch independently reconstructed exact blobs and executed 19 submitted tests, 2304 independently authored cross-product cases and four further sequences; GitHub review 5817375252."
---

# Latch — PR #9 Pass 1 independent implementation review

**Assignment:** LATCH-L01-PASS-1  
**PR:** https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/9  
**Exact reviewed head:** `9e9f311bbb83e6d8f59b5dafa125ff4d48679589`  
**PR base:** `35e03010b505ee59002e28c190bf668a33f0256b` (PR #8 merged)  
**Review submitted:** GitHub `COMMENT` ID `5817375252`, explicit **ACCEPT for Pass 1 scope**; not GitHub APPROVE, merge, or skill certification.

## Summary

The PR implements the first runnable slice of L01's synthetic Shared-Draft Lab, without adding production authentication, network interfaces, persistent secrets, actual agents or replay mechanisms. I independently verified the exact submitted Python model and tests against Git blob IDs, reproduced all 19 focused public tests, and ran a separately designed 2,304-case policy matrix plus four boundary sequences. The observed results match the accepted policy in the tested scope. **No blocking Pass 1 flaw found.** The next step is authorized integration and separately assigned Pass 2 replay implementation.

## Evidence

### Source inspection

- GitHub PR #9: open/draft/mergeable at initial inspection, one commit ahead of merged PR #8, six changed files; source is only `labs/__init__.py`, `labs/latch_l01/{__init__.py,README.md,model.py}`, `tests/test_latch_l01.py`, and one workshop README change.
- Read the exact `model.py` and `test_latch_l01.py` sources from the GitHub connector at the target head.
- Compared rule semantics to the accepted original lesson, F1–F4 addendum, R1/R2 errata, and three-pass plan. Checked claimed actor vs harness-bound requester, online authorization and offline precedence, current G1 delegation, human owner paths, denial before cache lookup, local-only RESTORED, conflict and no-effect behavior, public H reads, user-switch isolation, and explicit deferred scope.

### Actual independent local execution

Network checkout could not resolve github.com. To avoid conflating an unavailable full clone with an execution result, I **reconstructed only the two submitted source files** in a separate local Python directory and used `git hash-object` to prove byte-for-byte Git blob identity:
- `labs/latch_l01/model.py` => `594c02e1ee1c2e8d60664d63ef3feb8d19b9fd67` (matches source blob).
- `tests/test_latch_l01.py` => `c5cb2f190c57048d64df3378470323d6b14bfd93` (matches source blob).

Executed `python3 -m unittest discover -s tests -p test_latch_l01.py -v` against these exact blobs, with only package-marker files additionally created locally: **19 tests PASS**, observed in about 0.004s.

Executed a separately authored script (not part of PR or preserved as an authoritative project artifact) with an explicit, independent expected-outcome table derived from the accepted policy. Cartesian dimensions: user A/B, trusted actor A/B/X/Y, resource D1/D2/H/missing, action read/restore, clock 0/99/100, revoked false/true, online false/true and claimed actor none/matching/forged. **2,304 cases; zero discrepancies** in status, returned data or unintended state mutation. Also checked four supplementary sequences: owner restore after session switch and revoked grant, forged public identity vs legitimate Y read, repeated direct local restore without server/cache mutation, and unauthorized claimed-actor requests against multiple resources. **All passed.**

These test oracles were independently written for a known public teaching policy, not held-out learner qualification tests. Their success demonstrates narrow fixture behavior, not general security.

### Attributed evidence and limitations

- PR author reports full repository `python3 -m unittest discover -s tests -v` **60 tests PASS** (41 existing + 19 new), `python3 tools/validate_seed.py` PASS and whitespace PASS. **These full-tree commands were not independently rerun**; local GitHub clone failed on DNS resolution. No associated CI status/workflow run was returned from GitHub at review time.
- The intended fixture deliberately permits trusted `bind`, `switch`, `inspect`, setup controls and access to private stored test data. Those are **driver-only**, not security mechanisms against a direct Python caller with a fixture reference. The `inspect()` view is intentionally privileged and must not be introduced as an application-facing method in later passes.
- Does not evaluate the absent replay/retry transition model, simulated tool/publication effects, physical storage isolation, production authentication or prompt-injection resilience.
- No independent blind evaluator, Latch learner trial, capability promotion, identity certification or merge decision is implied.
- Review submitted to GitHub at exact head `9e9f311...` as COMMENT, returned ID `5817375252`.

## Reasoned verdict

**ACCEPT Pass 1 implementation for the exact reviewed head.** The actual local tests exercise both denied and legitimate-positive operations, return real allowed content rather than stubs, and verify that recovery cannot mutate server or cached state. The independent matrix adds evidence beyond the implementer's own 19 tests.

The full-repository gate is still dependent on author-attributed results or a later independent full checkout. Owner/architect may decide integration after checking that gate; this verdict is not a GitHub formal approval.

No remediation requested for the first slice. Maintain the privileged inspect boundary when adding learner-facing and simulated agent surfaces.

## Next decisive check

Merge only through authorized integration workflow after full repository checks. Then commission Pass 2 as a separate implementation checkpoint: one-slot queued intent, bound origin actor/session, blocker transitions, stale authorization, current grant/owner policy, retry precedence, completed-ID effects, and legitimate owner recovery, using separately specified expected outcomes. Return the exact new head for review and repeat independent counterexamples. Do not call the whole L01 fixture complete until Pass 3 and independent implementation review.

## Revisit when

PR head/base changes, independent full-tree validation contradicts author report, Pass 2 is implemented, an observed counterexample appears, or an evaluator actually assesses Latch's L01 performance.

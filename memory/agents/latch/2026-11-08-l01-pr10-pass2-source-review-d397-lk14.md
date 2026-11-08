---
schema: 1
id: 2026-11-08-l01-pr10-pass2-source-review-d397-lk14
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-review-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "GitHub KestrelGaming PR #10 exact head d39761409aa72b1be0b482952fc117d3dc15bfca, base c04331d4ad39ac4c95a1e42d9cd303964715b56a; inspected all five changed file patches; labs/latch_l01/model.py blob 425535b6724108cd34aa157ba8b1306cf9b6064f; tests/test_latch_l01_replay.py blob 971e3ba7424f1d1334fca833fb42f0fff01ba7a4; prior Pass 1 tests blob c5cb2f190c57048d64df3378470323d6b14bfd93; accepted L01 lesson, F1-F4 addendum and R1-R2 errata; GitHub COMMENT review ID 5819848427."
---

# Latch — L01 PR #10 Pass 2 source-contract review

**PR:** https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/10  
**Assignment:** LATCH-L01-PASS-2  
**Exact reviewed head:** `d39761409aa72b1be0b482952fc117d3dc15bfca`  
**Base:** `c04331d4ad39ac4c95a1e42d9cd303964715b56a` (merged PR #9)  
**GitHub review:** COMMENT ID `5819848427` (not a formal APPROVE), attached to the reviewed commit.  
**Verdict:** **SOURCE-CONTRACT ACCEPT; INTEGRATION CONDITIONAL** on independently reproducible executable checks, and the architect's merge authorization. No blocking semantics flaw identified through source inspection.

## Summary

Mothlight implemented the accepted deterministic one-slot queue and replay/retry state machine, retaining immutable originating actor and session, fresh authorization at replay, body-free denied outcomes, blocked session/actor states, terminal rejection, single recovery effect and a completed-ID guard. The 24 new public transition test definitions complement the 19 previously accepted Pass 1 tests. Source review against the accepted contract found no substantive implementation contradiction.

This is **not an independently executed runtime acceptance**: the review environment could read GitHub files through the connector, but a direct local `git ls-remote` could not resolve github.com. The GitHub connector returned no commit statuses or PR-triggered workflow runs. The author's reported 84 passing tests and validator success remain attributed to Mothlight.

## Evidence

- **Direct observation:** PR #10 initially open, draft and mergeable, with five changed files and one commit; PR #9 merged at `c04331d4ad39ac4c95a1e42d9cd303964715b56a`.
- **Inspected exact source:** `labs/latch_l01/model.py`, `tests/test_latch_l01_replay.py`, preserved `tests/test_latch_l01.py`, readmes, accepted lesson/addendum/errata.
- **Static evidence:** Guard order is valid context → online refusal → slot occupied; no ID is allocated on refusal. `Intent` is a frozen dataclass holding ID, actor, user, resource and state, not draft body or authorization. PENDING explicit `retry` returns `NO_PENDING`; `reconnect_and_replay` handles PENDING only and sets online. Session mismatch takes precedence over actor mismatch; mismatches block without executing. `_execute_intent` calls current `restore` after exact-origin equality, and marks `COMPLETED` or `REJECTED` and frees the slot after terminal results. `RecoveryEffect` records ID/action, not content. Completed-ID retry checks origin before `ALREADY_COMPLETED`.
- **Static test inventory:** 24 new test functions plus 19 preserved Pass 1 test functions. New tests cover the Axiom pending/queue cases, both blocked states, permission revalidation, revision conflict, missing cache, completed-ID idempotence, rejected slot reuse and reset.
- **Attributed only to Mothlight (NOT independently rerun):** full repository 84 tests PASS; 24 new tests PASS; `python3 tools/validate_seed.py` PASS; whitespace PASS; replay example outputs DENIED, DENIED, RESTORED, ALREADY_COMPLETED; published tree `69b7155931cf83d23c3c8d859d1daf02d5cd769a` verified by author. These are claims in the PR description, not observations made by Latch.
- **Tool limits:** `git ls-remote` via local container failed with DNS resolution error for github.com. GitHub commit statuses and workflow run queries returned empty. A separate source-level rule-check script inspecting the fetched model and test text returned 11 source-contract structural checks true; this is not behavioral testing.
- **Review submission:** `mcp__GitHub__add_review_to_pr` returned success with review ID `5819848427`, tied to `d397614...`. No code or PR state was modified by Latch.

## Scope and nonblocking watchpoint

The fixture's trusted harness `bind`, `switch`, `inspect`, state mutation and direct Python access are not production authorization boundaries. Its `inspect()` exposes full synthetic bodies intentionally for testing and must remain unavailable to the later learner-facing or agent-facing surface.

**Potential input robustness question (NOT a demonstrated failing test):** `retry(intent_id)` uses `self._intents.get(intent_id)` without runtime type normalization. An unhashable non-string value such as a list would cause a Python `TypeError`, rather than returning `NO_PENDING`. The fixture contract speaks of generated string IDs, so this is not presently a blocker. If Pass 3 accepts arbitrary agent-provided IDs, define boundary validation and test malformed inputs there rather than broadening Pass 2's already accepted behavior silently.

The currently missing teaching runner and simulated agent/tool interface, real authentication, deployed prompt-injection resistance, hidden evaluator suite and learner assessment are explicitly outside this pass. Success of the authored public regression suite would not prove Latch's competence.

## Reasoning and decision

The important property is that the intent's origin is historical *context*, never historical *authority*. The code compares current actor/session to the stored origin and then invokes live `restore` authorization and revision checking. Blocked intents require explicit retry; denied agent restore is terminal. A's valid recovery works after user switching and G1 revocation, preserving the legitimate task. Source control contracts align; the remaining material uncertainty is independent execution.

**Recommendation:** Have Axiom or Gauge perform an independent exact-head executable reproduction (at least focused replay transitions plus full repository validation), or acquire independently inspectable CI results. If those checks agree, integration should proceed without redesign; if they disagree, reopen only the affected behavior. Latch's current GitHub COMMENT is not integration approval, merge or permission to begin Pass 3.

## Next decisive check

At exact head `d397614...`, independently run `python3 -m unittest discover -s tests -p 'test_latch_l01*.py' -v`, the full `python3 -m unittest discover -s tests -v`, `python3 tools/validate_seed.py` and `git diff --check`; include a non-implementer-authored origin-mismatch, blocked retry and idempotence case. Publish actual command, revision, environment and outcome, then request a new head-pinned integration decision. The architect retains merge authorization.

## Revisit when

The PR head/base changes, executable counterevidence arrives, an independent reviewer reproduces tests, implementation is integrated, or a later agent-facing surface changes the allowed request inputs.

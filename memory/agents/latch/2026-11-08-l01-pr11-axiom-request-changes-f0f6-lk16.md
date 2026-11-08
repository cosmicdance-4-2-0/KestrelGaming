---
schema: 1
id: 2026-11-08-l01-pr11-axiom-request-changes-f0f6-lk16
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-review-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "GitHub PR #11 exact head f0f6cbbddcec52652233f9bca847a51dc5316b87, base ca49d6eabd6e6f17bfd139efd0d3804a16d351c8; Axiom review blob 7847909557c05f43778a01825ef38d6be2eb2f95 at Axiom home a9389f8ad40ffbb565a10d3a96d4e89f09a62950, and probe blob e02b9578af15c7d8a0ea25821d86aca1248876bc; PR #11 visible_cases.py blob 5ea78dc57d9a6ea7d61c57eac34ec2644576d5ff; surface tests blob 61bd5f23f3ea83b95be204cf101beab62b311375; GitHub review COMMENT ID 5820074202."
---

# Latch — PR #11 Axiom finding and correction handoff

**PR:** https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/11  
**Scope:** L01 Pass 3 public teaching runner, application adapter and simulated agent  
**Reviewed head:** `f0f6cbbddcec52652233f9bca847a51dc5316b87`  
**Base:** `ca49d6eabd6e6f17bfd139efd0d3804a16d351c8` (Pass 2 integrated via PR #10)  
**Verdict:** **REQUEST CHANGES (P2) before Pass 3 integration**, delivered by GitHub review **COMMENT**, ID `5820074202`. Formal REQUEST_CHANGES attempt was rejected by GitHub 422 because the shared account cannot request changes on its own PR. COMMENT is therefore not a platform-enforced review block. No merge performed.

## Summary

The user corrected the review context and supplied Axiom's independent review on PR #11. My prior acceptance of **PR #10 Pass 2** does not imply that the newer **PR #11 Pass 3** runner is complete. The scopes and heads are distinct.

Axiom observed a bounded but consequential runner-oracle defect: a controlled `QueuedWriteOnly` subclass can change server D1 content after queued restore, yet all **16/16 public cases PASS** and both text and JSON CLI falsely report success with exit zero. The existing Pass 2 focused regression **rejects that mutant**, and the shipped core model is unchanged except for docstring. Thus this is **not a demonstrated core vulnerability or unauthorized write in the shipped fixture**. It is a failure of the standalone teaching runner to detect a violation of the explicitly accepted R1 local-only recovery invariant.

## Evidence

- **Axiom report inspected:** `memory/agents/axiom/2026-11-08-latch-l01-pr11-review-f0f6.md` at `a9389f8ad40ffbb565a10d3a96d4e89f09a62950`, exact PR head `f0f6cbb...`; reports full source/tree checks, `python3 -m unittest discover -s tests -v` **102 PASS**, `python3 tools/validate_seed.py` PASS, full diff whitespace PASS, standalone runner **16/16** PASS, malformed input adapter matrix **570** checks PASS, and intentional queued-server-write mutant accepted by runner in text and JSON modes.
- **Axiom probe source inspected:** `memory/agents/axiom/evidence/2026-11-08-l01-pass3-review-probes.py`; contains `QueuedWriteOnly` override that changes `_drafts[intent.resource].body` only following `RESTORED` in `_execute_intent`. It checks all sixteen public cases pass, both CLI modes exit zero, and the older Pass 2 focused regression rejects the mutant.
- **Direct Latch source inspection:** `labs/latch_l01/visible_cases.py` at PR head, C07 `owner_positive` lines 127–135 checks before/after server drafts and cache for **direct restore**, but the successful queued paths C05 `switched_replay` lines 102–113, C12 `actor_retry` lines 169–181, C13 `pending_and_full` 184–196, and C14 `old_id_new_blocked` 199–213 omit equivalent server/cache comparisons. `tests/test_latch_l01_surface.py` line 173 tests a server write on shared direct `restore`, not the queued-only variant.
- **Boundary discipline:** The adapter's explicit string-only request interface and deny-only tool/publication handling are not contested by this finding. Axiom's reported 570 no-model-call/no-mutation probes are attributed independent execution, not Latch-run trials. I did not execute the probe or the full 102-test suite in this session. No hidden evaluator or actual learner trial is claimed.
- **GitHub action:** Attempted `add_review_to_pr(action=REQUEST_CHANGES)` on exact head, rejected with 422 `Review Can not request changes on your own pull request`. Re-submitted the same engineering verdict as `action=COMMENT`, success with review ID `5820074202` tied to `f0f6cbb...`. Do not represent COMMENT as GitHub-enforced REQUEST_CHANGES.

## Required bounded correction

Mothlight should add source-of-truth R1 observations to the **public runner's queued success paths**: compare snapshots of server draft body/revision and cached text/base before and after at least one automatic replay and one blocked explicit retry if feasible; each named check should fail on unexpected mutation. Expected values must come from the accepted policy/previous independent state, not the implementation's current mutation. The public runner must reject `QueuedWriteOnly` with a visible named R1 check failure, CLI text and JSON exit 1, and JSON `successful=false`, `failed>0`. A passing real model must still yield 16/16 successes, valid owner/delegated/public neighbors, and correct offline replay.

Do not change the accepted core model, adapter, authorization policies, or memory/governance schemas to address a missing assertion in runner tests. Keep the correction local and reviewable. Rerun focused mutation control, text and JSON CLI, complete repository tests, seed validation and whitespace checks at the new exact head. Return for new Latch/Axiom review as appropriate.

## Revision and decision

The earlier Pass 2 integration acceptance was legitimate, scoped and eventually merged. There is no reason to retract it. **The user corrected which PR was under consideration**; PR #11 is a new artifact and cannot inherit Pass 2's verdict. Axiom's new evidence alters the Pass 3 decision. A targeted educational correction teaches the distinction between an invariant being enforced by a lower-level test and actually being observed by the user-facing public harness.

**PR #11 remains draft, not integration-accepted.** Neither independent test execution on the corrected variant nor Latch's L01 qualification has occurred. No merge, implementation or other agent's branch changes were made in this session.

## Next decisive check

Inspect Mothlight's revised exact head for a before/after queued store/cache comparison and corresponding public mutant test. Independently repeat the `QueuedWriteOnly` control or attribute its reproduction correctly; confirm both CLI modes fail on the mutation, while normal 16/16 and all structural/tests still pass. If no blocker remains, issue explicit head-pinned acceptance; do not inherit it from current source-only judgment.

## Revisit when

Mothlight posts the correction, PR head/base changes, Axiom provides contradictory evidence, or independent execution reveals a new defect.

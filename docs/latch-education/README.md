# Latch education workshop

**Assignment:** LATCH-EDU-WRITER-01
**Working branch:** `mothlight/latch-education`
**PR target:** `agents/latch-v1`
**Author:** Mothlight; receiving reviewer and acceptance authority: Latch.

Kisuul authorized this branch for the duration of this project. Continue project work here. Mothlight remains the assigned writer; the inherited root branch selection does not change that assignment. Latch retains stewardship of its home branch and identity.

## Current review bundle

Read these documents in order. Later corrections govern conflicting Lab 01 semantics; the original submissions are preserved for traceability.

1. [Instructional checkpoint](Latch_L01_Instructional_Checkpoint.md) — curriculum, first lesson, fictional fixture and proposed evaluation.
2. [First clarification addendum](Latch_L01_Review_Addendum.md) — F1–F4 responses.
3. [R1/R2 errata](Latch_L01_R1_R2_Errata.md) — local-only restoration and actor/session equality for replay and retry; supersedes conflicting effects in the addendum.

[PR #7](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/7) merged at `d3cf43c5d4a2146371d05bf8c28712c5f1cf5266` after [Latch's integration acceptance](../../memory/agents/latch/2026-11-08-l01-pr7-acceptance-ca0d-lk11.md) and [Axiom's independent acceptance](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/53d5b0921e1001f64bab8ecf6ce2cea2583c33e3/memory/agents/axiom/2026-11-08-latch-l01-followup-ca0d.md), both pinned to source head `ca0dedef1b8ad9f02aa8f296b07f5059782a4bb8`. The instructional package is integrated; no lab runtime or behavioral qualification has been established.

**Implementation plan:** [PR #8](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/8) integrated the [three-pass plan](L01_FIXTURE_IMPLEMENTATION_PLAN.md) after Latch accepted source head `da83b322eb19655500c245315ba4b663ae694fa5`.

**Current slice:** [Pass-1 fixture and public tests](../../labs/latch_l01/README.md) implement direct reads and local recovery. Implementation acceptance is pending; replay/retry and the teaching runner remain later passes. Repository test results verify this fixture slice, not learner capability or qualification.

The submitted files remain available in Git history at `43b0dc68d36415b844009aae1dad735be88c9216`. Relative source links replace personal attachment URLs in the current copies; uploaded-original hashes identify those submissions, not subsequently edited repository copies.

## Axiom review follow-up

Axiom's initial review identified AX-L01-01 and AX-L01-02. The addendum now defines PENDING retry refusal and queue guard precedence, with public controls and the intentional blocked-slot limitation. Axiom's linked follow-up closed both findings at the accepted source head. Future implementation still needs executed behavior and independent review.

## Integration gate

PR #7 is merged. For subsequent project PRs, keep each PR in draft while Latch's acceptance is pending. Merge requires Latch's explicit acceptance tied to the PR's exact current head, the required repository checks, and resolution of any review blockers. Subsequent changes require Latch to assess the new head; earlier acceptance does not silently carry forward. Record the attributable review artifact and commit before marking the gate satisfied. Silence and this README are not acceptance.

This is a project workflow gate. No branch protection, authenticated reviewer identity, CI approval enforcement or automatic merge mechanism is installed by this change. Latch's requested independent Axiom review precedes any separately authorized fixture implementation. The present work is documentation; implementation and qualification remain pending.

## Verification

Repository checks: `python3 tools/validate_seed.py`, `python3 -m unittest discover -s tests -v`, and `git diff --check`. These check repository structure and existing regressions; they do not execute the proposed lab or qualify a security capability.

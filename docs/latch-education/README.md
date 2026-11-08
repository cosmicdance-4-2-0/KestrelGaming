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

Latch's [PR #7 review](../../memory/agents/latch/2026-11-07-l01-pr7-review-lk10.md) accepts the instructional and Lab 01 contract content at `43b0dc68d36415b844009aae1dad735be88c9216`, including R1/R2, while withholding integration approval pending portable links and fresh passing checks. The revised head requires renewed integration review. These documents describe proposed teaching and test contracts; no lab runtime or behavioral qualification has been established.

The submitted files remain available in Git history at `43b0dc68d36415b844009aae1dad735be88c9216`. Relative source links replace personal attachment URLs in the current copies; uploaded-original hashes identify those submissions, not subsequently edited repository copies.

## Axiom review follow-up

[Axiom’s review of `8eabb63f48c37f99458557cab5f25cc339bf3605`](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/4324baeac877c99a8f6bf29802fbc4da473a224a/memory/agents/axiom/2026-11-08-latch-l01-axiom-review-8eab.md) returned **REQUEST CHANGES** for two P2 specification gaps. The addendum’s F3 table now defines online retry of `PENDING` as `NO_PENDING` with state preserved (AX-L01-01), and orders queue guards as valid context → online refusal → occupied refusal → queue (AX-L01-02). Additional public controls and the intentional blocked-slot limitation are documented there. These are author corrections awaiting exact-head re-review, not Axiom acceptance or executed lab results.

## Integration gate

Keep the PR in draft while Latch's acceptance is pending. Merge requires Latch's explicit acceptance tied to the PR's exact current head, the required repository checks, and resolution of any review blockers. Subsequent changes require Latch to assess the new head; earlier acceptance does not silently carry forward. Record the attributable review artifact and commit before marking the gate satisfied. Silence and this README are not acceptance.

This is a project workflow gate. No branch protection, authenticated reviewer identity, CI approval enforcement or automatic merge mechanism is installed by this change. Latch's requested independent Axiom review precedes any separately authorized fixture implementation. The present work is documentation; implementation and qualification remain pending.

## Verification

Repository checks: `python3 tools/validate_seed.py`, `python3 -m unittest discover -s tests -v`, and `git diff --check`. These check repository structure and existing regressions; they do not execute the proposed lab or qualify a security capability.

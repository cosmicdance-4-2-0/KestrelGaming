---
schema: 1
id: 2026-11-06-auralprint-117-f1-analysis-contract-c82d
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "cosmicdance-4-2-0/Auralprint1 v117_dev ff547056542a10e3fbf1ae2010248d4558e55dda, architecture/117-analysis-contract-f1 4bae29a44811af7ce1ce9471d68bedaac2c569fb; PR #112; pinned source, tests, Git tree and PR inspection 2026-11-06."
---

# Auralprint 117 — F1 Analysis interface design and proof obligations

## Summary

**Outcome: PARTIAL — candidate design delivered and submitted; F1 owner acceptance and independent proof pending.** User directed Axiom to proceed from F0 into F1. At pickup, Auralprint `v117_dev@ff547056542a10e3fbf1ae2010248d4558e55dda` was unchanged, F0 PR #111 remained open/unmerged, and Visualizer PR #109 was still held. Created `architecture/117-analysis-contract-f1` **from accepted `v117_dev`**, not F0, and submitted [F1 PR #112](https://github.com/cosmicdance-4-2-0/Auralprint1/pull/112) on exact head `4bae29a44811af7ce1ce9471d68bedaac2c569fb`. No merge or production edit.

The [full design proposal](https://github.com/cosmicdance-4-2-0/Auralprint1/blob/4bae29a44811af7ce1ce9471d68bedaac2c569fb/docs/development/build-117-f1-analysis-contract.md) introduces candidate `AnalysisReader` v1, independent producer/deriver/definition/writer/reader responsibilities and seven owner review decisions. It requires new contract proof before Stage 3 producer migration and does not alter schema 16, CONFIG, source ownership, scheduler, math, visualizers or Canon.

## Evidence

**Directly source-observed:** `main.js` calls `updateAnalysisFrame(frame, AudioEngine.sample(), state.bands)` in the existing delivered rAF. `AnalysisFrame` and its channel objects are reused; arrays are producer-owned references and can be overwritten each sample or replaced on `BandBank.rebuild`. Neither `ready` nor JS object identity is a freshness token. `AudioEngine.sample()` reads L, R and the genuine C analyser graph after adaptive center mixing. `BandBankController` keys on settings and checks actual-rate known/effective-ceiling changes; a hypothetical changed rate at the same effective ceiling is a **new proof case**, not an established production bug. Analysis UI, Orb picker/editor, UI reset and VisualizerRuntime also read direct band state/names; merely creating a new frame facade does not fully decouple the consumers.

**Proposed, not accepted:** Three runtime-local dimensions—publication revision, source epoch from the accepted source owner, successful active definition revision—plus a reader-only borrowed view invalidated *before* producer buffer mutation; atomic ready/unavailable publication; explicit monotonic observation-end time (not audio or media time); no automatic deep-copy snapshot/independent scheduler; definition compatibility and legacy bridge. The 14 tests AN-01–AN-14 are **unexecuted specifications** (stale borrow, source race, partial L/R/C, unchanged-cap sample rate, collapsed bands, independent mock producer/consumer, numerical/preset parity, perf evidence).

**Remote verification:** The head comparison against accepted `v117_dev` yielded exactly two Markdown paths (`docs/development/build-117-f1-analysis-contract.md`, and a follow-on pointer in `docs/development/build-117-architecture-preparation.md`); two commits ahead, zero behind. GitHub's exact tree contained all 68 tested local Markdown link destinations; no trailing whitespace, unmatched fences or duplicate AN/D identifiers; no protected source/tests/scripts/Canon/package/CONFIG/fixture/version path changed. [PR #112](https://github.com/cosmicdance-4-2-0/Auralprint1/pull/112) was created, not merged. Direct `git ls-remote` failed DNS resolution, so no runnable checkout, `npm ci`, tests, build, `git diff --check`, independent producer proof, device run, benchmark or Canon hash recalc was performed. Historic B0–B2 results stay historic.

## Revisit when

- PR #112 gets independent critique or owner disposition. Verify exact head and recheck D1–D7, especially whether three revision dimensions are the smallest sufficient, when borrow invalidates, source-graph lineage ownership, and whether a full definition rebuild really needs a new revision.
- F0 PR #111 is accepted/revised. Reconcile only affected invariant references; do not quietly assume F0 approval from the F1 branch.
- Owner approves a versioned Analysis interface and a **separate isolated proof**. Implement a synthetic producer plus independent consumer with AN-01–AN-14 positive/negative evidence before any real `AudioEngine`/BandBank/Visualizer migration. F1 design submission is not that proof.
- Stage 0 B3–B7/owner Hero/device evidence appears, or accepted `v117_dev` moves. Distinguish measurement acceptance, structural acceptance, behavioral fidelity and performance; re-pin all source/artifact hashes.

**Next useful action:** Assign independent F1 contract review to a Kestrel engineering peer; resolve concrete counterexamples and ownership/clock questions; seek owner acceptance before selecting an executable interface/Stage 3 isolated proof. Preserve unmerged PR #109 and immutable Build 116.

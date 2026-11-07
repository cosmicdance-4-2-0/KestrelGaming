---
schema: 1
id: 2026-11-07-ap117-cp2-publication-correction-5cf8
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-implementation-session
created: 2026-11-07
updated: 2026-11-07
sources: "Flint PR #2 audit at 47ac4006bdfc717c47f8f79b8497d90c1455362d; Gauge prior CP2 numerical/continuity audit; application fix 5cf81245fc6087fb83a4cfba660f17e32f37cfe0; GitHub Actions 42354884756."
---

# Axiom CP2 publication correction — Flint and Gauge audit follow-up

## Summary

**Outcome: COMPLETE bounded application correction and exact-head GitHub CI; independent acceptance and owner merge remain pending.** The application PR #2, [ap_117_KESTREL](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2), advanced from Flint-reviewed `47ac4006bdfc717c47f8f79b8497d90c1455362d` to `5cf81245fc6087fb83a4cfba660f17e32f37cfe0` on `foundation/axiom-file-pcm-cp2` without merge.

Flint identified four integrity seams: accepted mutable injected analyzer results, missing finite-window placement validation, borrowed mutable generator provenance, and final-block -> exception -> EOF recovery. Gauge's earlier stream/epoch/continuity corrections were already implemented at the prior head and were deliberately preserved.

## Evidence

- Commit [5cf81245](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/commit/5cf81245fc6087fb83a4cfba660f17e32f37cfe0) changes exactly four paths relative to `47ac4006`: `src/analysis/rms.js`, `src/analysis/pipeline.js`, `docs/CP2_FILE_PCM.md`, and new `tests/publication-integrity.test.js`. GitHub compare confirms one commit ahead, zero behind.
- `measureRms` now takes a frozen scalar-only plain-record snapshot of source generator metadata (finite numbers, strings, booleans, null); nested mutable metadata is rejected. `AnalysisPipeline` validates `sampleSpan.placement === "whole-block"`, digital-normalized calibration and existing provenance before publishing a separate owned, frozen measurement/span/generator snapshot. Unknown extra analyzer properties are not carried forward. Waveform typed-array samples retain their documented consumer read-only contract, not transitive freezing.
- An exception during the post-final EOF read latches `faulted`; later `null` cannot silently recover the stream. Pre-final, no-consumption transient recovery remains possible only at the exact expected sample frame, as before.
- Five added negative/positive tests cover standalone generator snapshot ownership, mutable injected analyzer snapshot lifetime, incorrect whole-file placement with uncommitted cursor, nested metadata rejection, and post-final exception latch followed by explicit replacement.
- [Exact-head GitHub Actions run 42354884756](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42354884756) completed successfully: **48 tests, 48 pass, zero failures**, static build, official Nu built/rendered HTML validation, Chromium browser/offline smoke, whitespace gate; browser evidence artifact uploaded. These are hosted CI observations, not local suite execution. No PCM16 arithmetic, RMS formula, decoder, rendering, or scheduling changes were made.
- **Limits:** No independent Flint or Gauge re-review of `5cf81245` yet; no direct local full-repository run (this executor could not resolve github.com for checkout). Gauge's exhaustive 65,536-code numeric oracle remains attributed to Gauge's earlier head and was not repeated. Physical devices, hardware calibration, other browsers and maximum-file latency remain unverified.

## Next action

Ask Flint and/or Gauge to independently challenge the exact new SHA with their prior counterexamples and added tests. The owner decides CP2 PR #2 integration **only after independent acceptance**; no merge or CP3 work was performed here.

## Revisit when

PR #2 advances or is merged, an independent audit finds a new publication or terminal-state counterexample, a new method needs versioned measurement semantics, or a source needs a more expressive discontinuity contract.

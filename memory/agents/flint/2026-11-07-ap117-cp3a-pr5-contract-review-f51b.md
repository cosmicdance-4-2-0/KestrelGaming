---
schema: 1
id: 2026-11-07-ap117-cp3a-pr5-contract-review-f51b
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-cp3a-review-session
created: 2026-11-07
updated: 2026-11-07
sources: "ap_117_KESTREL PR #5 head 23da63f8e8427d9b23c3f63794aeef6634fd466b vs main@790e71f300ad24e01ec97c7ef42f4ca500ba1080; review 5815954595; CI 42377361628; exact source-executed isolated V8 probe; Harbor and Gauge PR reviews."
---

# Flint — CP3-A spectral interchange minimality review at PR #5

## Summary

**Outcome: REVIEW COMPLETE, REQUEST CHANGES for a bounded interface decision** at pinned PR #5 head `23da63f8e8427d9b23c3f63794aeef6634fd466b`. Submitted [GitHub review 5815954595](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5#pullrequestreview-5815954595) as COMMENT because the connected account owns the PR. No merge, app modifications, CP3-B work, or deployment.

The CP3-A decomposition is proportionate: same accepted CP2 PCM acquisition and copied waveform, independent spectrum math, bounded overlapping sample window assembler, typed peak-amplitude observation, renderer-neutral SpectrumScope model and Canvas2D presenter, and single FrameHost. No duplicated source reads, runtime dependencies, new animation loop, or changed CP2 scientific methods were seen in the inspected code.

**Narrow requested correction:** the exported `createSpectrumStream.accept` only partially validates the CP2 measurement that it calls already validated. A forged `ready` CP2-like publication with `schema:not-cp2` and `validity:invalid`, or with incompatible `unit`, `reference`, `method`, or `calibration`, can generate a new ready spectrum.

## Evidence

- **Source inspection:** Entire `src/analysis/fft-amplitude.js`, `src/analysis/spectrum-stream.js`, `src/main.js`, `src/analysis/pipeline.js`, `src/config.js`, SpectrumScope model/Canvas presenter, changed contracts/HTML, and relevant Node/Chromium tests fetched at exact PR head. GitHub compare reports 15 commits ahead, zero behind, 16 files, 824 additions and 13 deletions against accepted CP2.1 baseline `790e71f`.
- **Independent execution:** Original FFT and stream functions fetched from exact head, wrapped in an isolated V8 evaluator with only module import/export syntax adapted. An 8-frame synthetic `ready` publication with constant 0.25 samples, coherent channel/span/clock and deliberately invalid `schema` and `validity` returned `status:ready`, DC bin 0.25. Six separate single-field metadata mutations (`schema`, `validity`, `unit`, `reference`, `method`, `calibration`) all returned ready while a correct control returned ready. This independently confirms and extends Gauge's separately reported schema/validity finding; no second copy of CP2 source is shown to emit these forged values.
- **Normal app boundary:** `AnalysisPipeline` validates and snapshots real CP2 `ap117.measurement/2` fields before its publication. Therefore the forged input is an **interchange seam** defect, not an observed normal CP3-A app failure.
- **CI-attributed:** [run 42377361628](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42377361628) completed success on exact head: 66 tests passing, 0 failing, static build, Nu/Chromium gates. CI measured 1024 FFT median 0.042ms and p95 0.138ms on hosted runner, not a device SLA. Job metadata/log inspected, **no independent full local repository checkout/browser run**.
- **Peer attribution:** Harbor's lifecycle PASS and Gauge's numerical PASS / conditional interface findings are separate assessments. No claim of independently reproducing their entire test coverage.

## Decision and proportional correction

Preferred: require at least CP2 measurement `schema` and `validity` explicitly at `createSpectrumStream.accept`; decide whether this exported seam promises the entire RMS type fingerprint, adding one table-driven negative test with positive controls. Alternative: explicitly state that `accept` requires trusted validated pipeline output and does not validate it independently. Do **not** invent a generic validation framework or redesign source/DSP geometry.

Low-priority label drift: `index.html` repeats periodic Hann/M=1024/H=512, instead of deriving these from `CONFIG.spectrum`; correct or use policy-neutral copy when configurability grows. No present mismatched numeric label.

## Revisit when

Axiom submits an amended head or owner decides on trusted-boundary policy. Rerun the forged-publication negative cases and full exact-head CI after the change; do not carry approval forward to a different SHA. Preserve CP3-A spectral method, FFT normalization, CP2 source clock, one FrameHost, and Harbor's recovery behaviors.

---
schema: 1
id: 2026-11-07-ap117-cp2-mainline-review-7a8d
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-review-session
created: 2026-11-07
updated: 2026-11-07
sources: "ap_117_KESTREL main@7a8df54a35f4743e4c223001337d8382dda21122; PR #2 and #3; Actions 42363792862; fetched source, docs, tests and job log."
---

# Auralprint 117 — CP2 merged-mainline review

## Summary

**Outcome: REVIEW COMPLETE (source/CI inspection; no application modification).** The active Auralprint 117 application repository is [cosmicdance-4-2-0/ap_117_KESTREL](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL). CP1 [PR #1](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/1), CP2 [PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2) and Flint's single-render-loop fix [PR #3](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/3) are merged. Current main is `7a8df54a35f4743e4c223001337d8382dda21122`. No open PR was found in the current PR search.

## Evidence

- Exact mainline [Actions run 42363792862](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42363792862) reports success. Fetched job log confirms **49/49 Node tests**, static build, offline entry check, official Nu built/rendered HTML validation, Chromium browser smoke, artifact upload and whitespace check.
- Inspected current source modules: `src/analysis/{pipeline,rms}.js`, `src/audio/{wav-pcm16,pcm-buffer-source,synthetic-sine,file-import}.js`, `src/rendering/{frame-host,canvas-2d-backend}.js`, `src/visualizers/signal-scope/*`, `src/camera/orthographic-2d.js`, `src/main.js` and config. The implemented boundaries remain source -> versioned source/clock validation -> finite-window RMS publication -> graphics-neutral model -> Camera2D/Canvas2D presenter with a host-owned frame loop.
- Inspected negative test definitions for stream gap/overlap, premature EOF, mutable provenance, post-final exception and reentrant frame restart. Flint's PR #3 guards its successor request after an in-callback stop/start. These statements are source-inspection and CI observations, **not** new independent adversarial execution.
- **Boundary for CP3:** `AnalysisPipeline` currently validates the exact `rms-amplitude` / `unweighted-mean-square-sqrt/1` method and `whole-block` placement. FFT/PSD cannot be inserted as an interchangeable measurement without designing versioned method-specific observation envelopes and window/sample-span ownership. The waveform typed array remains read-only only by consumer contract.
- **Nonblocking documentation drift:** `docs/CHECKPOINTS.md` still describes CP2 as not promoted/awaiting owner review although PR #2 has merged. Treat historical PR-body statements as history, not current state.
- **Not established:** independent local full-suite run, cross-browser/device behavior, physical audio timing/calibration, maximum WAV responsiveness, multi-renderer interoperability, or CP3 readiness. No CP3 implementation was found in this mainline inspection.

## Revisit when

CP3 observation/window/FFT normalization contracts are proposed; the mainline or CI head changes; a new adversarial sample-clock/publication defect is demonstrated; or documentation is reconciled with CP2 integration status.

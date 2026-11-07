---
schema: 1
id: 2026-11-06-auralprint-117-accuracy-backends-a91f
kind: decision
scope: agent:axiom
status: active
evidence: user-stated
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "User Auralprint 117 accuracy/modularity requirements, 2026-11-06; Kisuul/KestrelGaming audio skills branch 435a3b10c6e23cca2aba4712fb03fd148d65a13a; Auralprint1 v117_dev ff547056542a10e3fbf1ae2010248d4558e55dda; Auralprint F1 PR #112 (unmerged)."
---

# Auralprint 117 — Accuracy-first Analysis and backend-neutral architecture

## Summary

**User-stated design priority:** Analysis is first-tier. Preserve accuracy as a mandatory acceptance property; balance robustness and speed without silently trading away truthful measurement. Offer explicit methodological/performance alternatives where they have declared units, accuracy limits, latency, calibration and provenance. Analysis, rendering, Camera and Visualizers must each be maximally modular; future 3D and alternative rendering cores (Three.js, PixiJS or other backends) are in scope as *architecture possibilities*, not authorization to replace current Canvas 2D now.

**Axiom assessment:** F1 PR #112 is incomplete as a *measurement* contract: it discusses freshness, borrowed arrays and source/definition epochs but does not sufficiently state sample-index timebase, measured quantity versus display proxy, spectral units/window/hop/normalization, source/channel-map lineage and uncertainty. **Do not freeze F1's ABI or begin producer migration solely on the current PR.** Amend the design with an explicit measurement contract and an independent backend-neutral representation/Camera/Visualizer capability seam before implementation; this is a recommendation, not owner-approved detailed ABI.

## Evidence

- Reviewed Kisuul/KestrelGaming `skills/audio-dsp-core-foundation-2026-11-03@435a3b10` through GitHub. The audio catalog has **19/73 developed modules** (54 pending) and PR #2 remains open/unmerged by owner's all-73 requirement; latest branch CI was reported successful. The library is a rigorous **skill/reference/testing curriculum**, not automatically an installed Auralprint production DSP engine.
- Relevant skills include `audio-dsp-core`, `audio-fft-spectrum`, `audio-window-functions`, `audio-power-spectral-density`, `audio-timebase-sync`, `audio-analysis-provenance`, `audio-numerical-stability`, `audio-dsp-test-fixtures`, `audio-channel-mapping` and `audio-stream-buffering`. They separate measurement quantities, sample clocks, validity/gaps, FFT/PSD normalization, calibration/uncertainty and independent oracles from presentation.
- The PPM educational reference explicitly fails the published EBU Type IIb flatness requirement at 31.5Hz and 16kHz and does **not** claim instrument compliance. Its code/tests preserve this failed standards property despite passing its bounded test suite. This is desirable maturity-labeling, not verified PPM accuracy.
- Auralprint `src/js/audio/band-bank.js` `computeEnergiesFromAnalyser()` averages `clamp((freqDb - minDb)/(maxDb-minDb),0,1)` per bin; its `energies01` is a normalized spectral **activity/display proxy**, not calibrated band power or PSD. `AudioEngine.sample()` gets browser `getFloatFrequencyData()`, which returns smoothed decibel bins without exact PCM sample-span provenance. The current C signal is **derived from an adaptive stereo mix** via sum gains; it is not a native independent center speaker channel. These current 116 visual behaviors must remain compatible, but future scientifically meaningful measures should be separately typed, never silently reinterpreted.
- The future renderer should not own DSP definitions. Separate Audio capture/PCM adapters, quantity-aware measurement services, observation/publication contract, Visualizer model, dimensioned world geometry, Camera/projection models, and renderer-specific Canvas/Pixi/Three adapters. Keep Clock/recording ownership and CONFIG→preferences→runtime.settings→state hierarchy independent. Capability-specific rendering paths are preferable to a restrictive universal draw-command representation. Future 3D must not retroactively change canonical 2D camera/Scene schema.

## Revisit when

- Before F1 PR #112 approval: re-review sample provenance, clock domains, window/hop/FFT calibration, uncertainty, typed quantities and explicit legacy visual-proxy classification; consider a narrowly scoped F1 amendment instead of implementation.
- Before generic Visualizer/renderer contract acceptance: specify Camera/projection and 2D/3D coordinate spaces, dimensions/units, capability negotiation, backend-specific adapters, Canvas fidelity/recording parity and performance fallbacks. Three.js/PixiJS remain options, not decided dependencies.
- Any new analysis method must have independently testable analytic/SciPy or alternative oracle comparisons, negative fixtures, valid ranges, declared tolerances and separate native/device performance evidence. Faster algorithms cannot be allowed to relabel or distort measured quantities; choose supported reduction of visual cadence/optional computations when necessary.
- Keep Build 116 compatibility and Canon immutable; F0/#111 and F1/#112 owner acceptance, Stage 0 B3–B7, and held Visualizer PR #109 remain separate gates. No Auralprint files were modified for this exploratory assessment.

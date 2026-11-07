---
schema: 1
id: 2026-11-06-ap117-kestrel-cp1-foundation-0d71
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "cosmicdance-4-2-0/ap_117_KESTREL PR #1, head e4b95b32a5aa239e621d37ac5b297399ae059223; CI 42327594695; owner request 2026-11-06 to use new repository, first narrow executable slice; prior Kestrel DSP skill and Auralprint 116/F0/F1 architectural discussion."
---

# Auralprint 117 — Axiom's first runnable foundation checkpoint

## Summary

**Outcome: reviewable implementation submitted, not owner-accepted or merged.** New repo [cosmicdance-4-2-0/ap_117_KESTREL](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL) began with only an initial README. Axiom created [PR #1](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/1), branch `foundation/axiom-signal-scope-cp1`, base `main@730b5dbc75d88b5c594df8f7e6986effebcd7473`, exact final reviewed head `e4b95b32a5aa239e621d37ac5b297399ae059223`. The PR includes a dependency-free, runnable browser ES-module SignalScope prototype.

**User-stated requirements:** The whole Kestrel agent team may contribute later; Axiom starts by engineering the foundation. Maintain a working prototype and build in narrow vertical slices. Analysis correctness is first-tier; robust, fast and honest numerical observations take precedence over eye candy. Analysis, Camera, Visualizers, renderer and future compositor are distinct modular concerns. All Canvas2D/PixiJS/Three.js are possible future backend choices by individual Visualizers; the host must own actual rendering resources and frame scheduling. LegacyOrb, LegacyRing and 116 Preset Loader belong to **other** work, not this checkpoint.

## Evidence

- **Delivered architecture:** `src/audio/synthetic-sine.js` emits contiguous mono Float32 PCM at sample-frame coordinates; `src/analysis/rms.js` produces unweighted RMS with source ID, epoch, parameter revision, channel/tap, exact BigInt sample span, explicit digital-linear reference and validity. `src/analysis/pipeline.js` invalidates before sampling, fails closed and copies waveform for snapshot ownership. `src/visualizers/signal-scope/model.js` has no rendering imports. `src/camera/orthographic-2d.js` projects world to CSS pixels. `src/rendering/canvas-2d-backend.js` owns context, DPR and surface; a SignalScope-specific Canvas presenter draws; `frame-host.js` owns only rAF. Application assembly is in `src/main.js` and defaults in `src/config.js`.
- **Runnable tooling:** `npm run dev` launches the built-in localhost Node server; `npm test` runs Node's native test harness; `npm run build` copies a static self-contained application to `dist/`; `npm run preview` serves it. No dependencies or CDNs are added. This initial toolchain is a deliberately reversible alternative to the earlier TypeScript/Vite suggestion.
- **Observed CI:** [GitHub Actions 42327594695](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42327594695) at exact `e4b95b32` completed **success** with 21 Node tests passing, zero failing, zero skipped; static build and remote-script/stylesheet check passed. Tests cover independently calculable 1kHz/48kHz/0.5 sine RMS (480 frames -> 0.5/sqrt(2)), DC, genuine silence, partition continuity, parameter changes, invalid/nonfinite PCM, stale publication invalidation, copy ownership, renderer-independent advancement, Camera2D, DPR and frame scheduling. An integration test imports the real `main.js` against a simulated DOM/Canvas host, actuating the controls, analysis tick, drawing, pause/resume and pagehide lifecycle.
- **Evidence limits:** CI's simulated DOM is **not** a real browser screenshot or graphics fidelity/device test. Browser interactive smoke, resize on real DPR hardware, audio capture, recording, real-time latency, cross-backend swapping, GPU resource behavior and upstream Canon 116 compatibility are unverified. No claim of real audio output or standardized instrument calibration. Browser interval cadence cannot be equated with sample-clock timestamps.
- **Diff scope:** PR #1 has 25 new/modified app/docs/tests/CI paths, one branch-only initial implementation and one follow-up test commit. Original `main` branch and `cosmicdance-4-2-0/Auralprint1` remain untouched. PR #1 is open, owner acceptance pending.

## Revisit when

1. Inspect PR #1 exact head and CI, conduct manual live browser interaction/visual smoke before accepting CP1, and solicit independent Flint minimum-mechanism, Gauge numerical-oracle, Harbor lifecycle, and Mothlight usability review as applicable. Separate their actual findings; never invent consensus.
2. Address any independently demonstrated correctness gap, preserve zero-dependency working prototype, then owner decides merge. Do not port LegacyOrb/LegacyRing/schema-116 loader under this checkpoint.
3. CP2 candidate: real PCM acquisition with explicit channel, frame-span and epoch lineage, while preserving renderer-free Analysis. Future FFT/PSD must use accurately typed calibrated quantities and independent references; PixiJS/Three.js/Cam3D and mixed-surface capture require later distinct gates.
4. Continue using Auralprint1 116 Canon as historical reference, not as accepted functionality of the new repo. Auralprint1 F0/F1 PRs #111/#112 remain historical proposals and are not automatically merged here.

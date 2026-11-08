---
schema: 1
id: 2026-11-07-ap117-analysis-providers-consumers-0531
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-architecture-reconciliation-session
created: 2026-11-07
updated: 2026-11-07
sources: "Owner instrumentation-panel directive in project conversation; ap_117_KESTREL accepted main@0531e734a2ece59cd877ea8659069efee2e0a905; src/analysis/spectrum-stream.js, rendering/frame-host.js; B1 issue #6 comment 6716853036, B2 issue #7 comment 6716855268; Gauge G05, Flint 6716513401, Harbor 6716755145."
---

# Auralprint 117 — modular analysis providers/consumers, instrumentation-panel direction

## Summary

**Owner design direction (user-asserted requirement):** Auralprint should evolve into a configurable instrumentation panel where multiple user-selected visualizations, e.g. highly detailed spectral plots, VU-style level instruments and BPM/onset/envelope-driven particle scenes, coexist. **Accurate analysis is primary; accurate, independent presentation follows.** Frame/render rate will differ from analysis cadence; the application must not dictate how users visualize, and modules may operate as **providers, consumers, or both**. Every downstream analysis consumer should have access to the appropriately accurate, timely observations it needs, not just a global last-painted measurement.

**Axiom consequence:** The prior integrator recommendation of narrow option C PSD derived from *latest-only CP3-A spectrum snapshots* remains numerically valid for one observed window but **is not an adequate universal analysis-to-analysis distribution contract**. Flint and Harbor observed that one PCM block may form multiple windows while `spectrum.readCurrent()` shows only the last. If a future spectral-flux/onset consumer needs every window, irrevocably hiding intermediate frames before analysis fanout would corrupt downstream behavior despite accurate per-window FFT. **Reopen D3 (latest observable only)** in B1 planning rather than silently approving it as the architecture's default for all analyzers.

## Current source evidence

`main@0531e734a2ece59cd877ea8659069efee2e0a905`: `src/analysis/spectrum-stream.js` runs FFT every complete window inside `accept`, increments spectrum revision and overwrites one `current` publication; `readCurrent` returns only latest. `src/rendering/frame-host.js` owns the sole rAF and is already separated from analysis scheduling. The strict CP2 PCM source clock and channel/epoch constraints, full CP3-A FFT correctness and calibration, and existing dual-Canvas prototype are accepted and unchanged.

## Proposed architecture (not frozen/implemented)

- **Acquisition provider:** a single validated PCM read/source; preserve exact channel, sample clock, source epoch, revision and continuity. Different analysis specifications can share PCM while producing independent derived results.
- **Typed analysis providers:** emit complete measurement events when logically computed (not on rAF); each carries schema/version, quantity, method, unit/reference/calibration, source clock/BigInt interval, revision, validity, lineage and lifecycle/discontinuity. A node may consume upstream typed events and itself publish typed derived observations.
- **Per-subscriber delivery policy:** distinguish `all-complete` lossless/ordered analysis subscriptions from intentional `latest` coalesced presentation subscriptions, with finite boundedness. A lossless subscriber must receive every accepted complete window *or detect that an interval was lost*; never silently report complete scientific continuity when overloaded. Offline pausable inputs may support bounded backpressure/replay; nonpausable live sources require explicit overrun/invalidation policies. Do not introduce unlimited history or promise infinite real-time throughput.
- **Presentation/scene consumers:** visualization timing, animation extrapolation and rendering backend may vary independently; visualization may subscribe to multiple measurement types and may also provide distinctly typed derived animation/control observations. Visual scaling/color effects do not alter scientific data. VU-like ballistics and BPM/onset/attack envelopes are separate methods requiring explicit semantics; plain CP2 RMS is not automatically a calibrated VU.
- **Provider reuse:** equivalent requested FFT/window/epoch settings may share computation; distinct consumers' analytic window/hop requirements must not be forced to share one chosen global FFT merely for drawing convenience.
- **Graph safety:** provider/consumer relationships need explicit ownership/disposal, ordering, source-clock coherence, dependency-cycle prevention or defined delays, failure/epoch propagation and versioned schemas. Avoid inventing a generic event bus/visualization framework until a narrow slice proves necessary.

## Next small design proof / team work

Working label **CP3-B0**: smallest provider-to-subscriber seam preserving CP3-A math and prototype. Proposed falsifier: input 20 frames with M8/H4, one PCM block vs partitioned produces **four ordered complete FFT observations** to an `all-complete` analysis subscriber in both cases; the `latest` visualization sees exactly the same final source interval `[12,20)`. Attach dependent typed B1 PSD (Gauge's correct algebraic option C) to **each required complete spectrum event**, not just `readCurrent`; do not introduce a second source read/FFT. Test dual subscribers, false/duplicate stamps, source epoch resets/Harbor live-currentness, overrun/backpressure policies, BigInt spans, failure isolation, and single FrameHost. This is a design hypothesis, not permission for broad refactoring.

**Public coordination posted:**
- [B1 issue #6 new architecture premise](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716853036) for Gauge/Flint/Harbor to challenge.
- [B2 issue #7 presentation implication](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/7#issuecomment-6716855268) for Mothlight/Kite/Flint. A mode toggle is a prototype choice, not a mandated exclusive multi-instrument UI.

Owner has **not** explicitly selected final subscription semantics or authorized B1 code implementation. No application branches, code PRs, merges, or deploys in this conversation turn. Integrator must reconcile competing requirements before committing a provider API.

## Revisit when

Owner refines data delivery quality requirements, Gauge/Flint/Harbor critique per-window fanout, Mothlight/Kite propose panel UX, B1 delivery contract and backlog/overrun policies become explicit, or accepted app source/clock interfaces change.

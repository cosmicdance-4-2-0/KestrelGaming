---
schema: 1
id: 2026-11-07-ap117-cp3b1-harbor-live-fence-0531
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-design-reconciliation-session
created: 2026-11-07
updated: 2026-11-07
sources: "ap_117_KESTREL Issue #6 Harbor comment 6716755145, Axiom reconciliation 6716785731, accepted main@0531e734a2ece59cd877ea8659069efee2e0a905; Gauge G05 and Flint issue comment 6716513401."
---

# Auralprint 117 CP3-B1 — Harbor stale-replay challenge and integrator solution

## Summary

**Outcome: Harbor CONDITIONAL design PASS; Axiom proposed precise currentness/fence contract; owner D1–D4 scope approval still pending. NO PSD IMPLEMENTATION/BRANCH/PR.** Harbor independently executed accepted CP3-A functions and reproduced stale frozen ready snapshots remaining externally accessible after invalidate/reset. Harbor's stronger counterexample proved that a consumer remembering only its last accepted CP3-A revision could accept a producer revision it never consumed, *after the producer has already reset to a higher revision*. Harbor posted [full report](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716755145); Axiom posted [integrator reconciliation](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716785731). Both are design only, not claims about nonexistent B1 code.

## Evidence and design consequence

Actual CP3-A `createSpectrumStream` preserves a frozen ready object and revision across a partial input block, then increments its live producer revision on `invalidate` and `reset`. Observed example: rev2 ready, rev3 invalidated, rev4 reset/unavailable, rev5 new epoch ready. Distinct old rev2/rev3 ready objects retain ready text forever as immutable historical snapshots; this is correct snapshot behavior. A dependent PSD adapter cannot infer currentness solely from snapshot's `status` or `revision > lastConsumed`. A reset fence must use the **live upstream's current revision**, even if the PSD consumer missed intermediate ready events.

**Proposed contract:** `createPsdAdapter({ readSpectrumCurrent: spectrum.readCurrent })` bound once to the existing producer. No externally supplied `accept(snapshot)` interface; `observe()` synchronously calls the trusted live producer to obtain its current canonical record. Tests can inject fake callback, but production binds actual CP3-A. Store bounded `upstreamHighWater`, `resetFence`, own PSD revision/current status, optional *current* producer object identity and source tuple, disposed state. `reset`/withdraw after CP3-A unavailable samples **live** revision as fence and retains high-water across reset. Ready must be strictly newer than fence and valid under expected source/parameter transition. No generic event bus, second sample cursor, PCM assembler, FFT, rAF or imported microphone.

**Dedup policy:** Exact same current producer object/stamp as previously accepted while ready -> strict no-op, preserving PSD object and revision. Distinct object with identical producer stamp (including cloned/equivalent) -> conservative reject, withdraw and throw; no unrecognized snapshot aliasing. Reset/invalidation makes even identical old objects stale. New higher current records may skip complete spectral windows (large source blocks); do not require successive start samples to differ by H. Producer live-currentness does not cryptographically prove the measurement's origin; the CP2/CP3-A validation and host wiring remain trusted boundary.

**Host order:** `advance` runs CP2 `pipeline.advance()` then CP3-A `spectrum.accept(publication)` then B1 `psd.observe()`, all synchronously. On parameter edit/render failure/source switch/file loading/import error, first invalidate/reset CP2 and CP3-A in existing order, *then* B1 withdraw or reset (capturing live upstream unavailable revision). Retry after final-frame render fault cannot resurrect the consumed window or bypass explicit `EOF — REPLAY REQUIRED`. A normal clean EOF retains the latest genuinely complete historic spectral interval unchanged; a 481/1023-frame file never publishes fabricated PSD. Adapter-only invalid input fails closed and throws to host; B1 must never silently invalidate CP3-A on its own. On pagehide/BFCache, B1 disposed and refuses future calls; new page gets new adapter.

**Tests:** Harbor's rev2 consumed / rev3 unconsumed / rev4 upstream reset / cached rev3 forged / new live rev5 control; Flint one-block-vs-partitioned latest-only M8 H4; source epoch/revision and `BigInt` offsets; repeated unchanged stamp, conflicting same-stamp clone, invalid upstream fingerprint/window/bin/ENBW, clean incomplete EOF vs failed-render EOF, any Canvas exception, retry, replay, file import cancellation, pagehide and no new timer/rAF. Preserve Gauge independent Parseval and density normalization tests.

## Decision authority and exclusions

**Recommended D1–D4:** C only for existing complete CP3-A windows, same window parameters, unaveraged high-variance modified periodogram, latest externally observable CP3-A publication only, supported rectangular/periodic-Hann positive-S1 current FFT method; no Welch/history/independent detrend/window. Axiom recommends this intentionally limited B1. These product scope choices still require owner approval, and Harbor's condition is not an owner decision.

No code implementation, application PR, merge, CP3-B2 or CP4 work was created by this design reconciliation. Next actual implementation PR must pin accepted main, commit B1 contract and targeted negative tests, then get Gauge numerical, Flint boundary and Harbor lifecycle review.

## Revisit when

Owner accepts or changes D1–D4, B1 contract is versioned into application source, new implementation head exists, a reviewer finds a counterexample to the live-producer fence, or CP3-A revision semantics change.

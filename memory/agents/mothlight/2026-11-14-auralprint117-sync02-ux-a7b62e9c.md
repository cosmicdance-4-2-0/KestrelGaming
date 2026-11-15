---
schema: 1
id: 2026-11-14-auralprint117-sync02-ux-a7b62e9c
kind: handoff
scope: agent:mothlight
status: active
evidence: observed
author: mothlight
created: 2026-11-14
updated: 2026-11-14
sources: "Axiom AP117 Team Synchronization 02 user-supplied handoff prepared 2026-11-07; ap_117_KESTREL main@0531e734a2ece59cd877ea8659069efee2e0a905; Mothlight issue #8 independent comment 6889909855; KestrelGaming agents/mothlight-v1@458ec8603f31b6436af70da03900fb25b442e6d8."
---

# Auralprint 117 — Mothlight independent UX and accessibility synchronization

## Summary

**COMPLETE: independent design response submitted** to [Auralprint issue #8](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8#issuecomment-6889909855). This was Axiom's six-engineer synchronization assignment, specifically Mothlight's first pass on simultaneous instruments, varied analysis/render cadences, truthful freshness, display coalescing, gaps and accessibility. No application implementation, PR, merge, schema acceptance or actual tests were authorized or performed. Other engineers' new issue responses were not read before posting; no peer consensus or reciprocal review is claimed.

## Evidence

**Verified source:** project `main@0531e734a2ece59cd877ea8659069efee2e0a905` was still current on 2026-11-14. Loaded own branch contract/identity and relevant memory index, then inspected CP3-A code: `src/main.js`, `src/analysis/pipeline.js`, `spectrum-stream.js`, `src/rendering/frame-host.js`, visualizer models and Canvas presenters, `index.html`, `styles.css`, `docs/CP3_FREQUENCY.md`, project contract and architecture. CP3-A accepts complete FFT windows, but externally exposes the latest through `readCurrent()`; the current SpectrumScope presenter and DOM status reduce multiple non-ready conditions to generic “waiting”, which is inadequate for a multi-instrument interface but not an asserted CP3-A test regression.

**Owner requirements from handoff:** correct analysis first, no wall/rAF-derived sample clock, panels can consume or publish analyses, simultaneous instruments may have distinct methods/window policies and render cadences. Full-delivery subscribers require ordered observations or explicit gaps; latest-display coalescing must not masquerade as analysis loss. Subscriber API, C-stream and CP3-B0 are still proposals.

**Independent finding:** A panel needs separately observable (1) **measurement validity and producer currentness** with exact method, units, source, epoch and BigInt half-open sample span; (2) **delivery continuity** (complete, intentional latest coalescing, detected loss/overrun); and (3) **presentation receipt** (last actually painted revision/span versus latest eligible upstream). A slow plot can show an old, still mathematically valid spectrum but cannot call it *present-current*; after reset/invalidate a cached ready object must not resurrect as fresh.

**Counterexample:** M=8, H=4, Nfft=8, twenty source frames yield four spans `[0,8),[4,12),[8,16),[12,20)`. Fast subscriber receives all; renderer may draw first and fourth only. Missing intermediate *draws* are not an analysis gap. Separate Harbor revision-3 stale snapshot followed by producer unavailable revision-4 test. Never invent source high-water or wall-time age from a Canvas animation timestamp.

**Proposed bounded next proof:** pure read-only, source-fenced `instrument-status` projection over scripted producer/delivery/last-drawn receipts; no DSP changes, schema freeze, new rAF, plugin framework or compositor. Eleven proposed UX-M01..11 negative/positive paper scenarios cover slow rendering, reset, short file/error, overrun versus coalescing, method separation, keyboard composition, actual screen-reader check, reduced motion/zoom, EOF/replay, isolated render failure and BigInt spans. Paper scenarios are **not executed**. Note that today's `failRendering()` deliberately pauses the source and invalidates both displays; decoupling renderer-only failure remains **future owner-reviewed architecture policy**, not a change claimed here.

**Publication link:** [AP117-SYNC02-MOTH-01 independent first-pass report](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8#issuecomment-6889909855).

## Revisit when

Axiom reconciles other independent reports, the owner chooses a minimal delivery seam/CP3-B0, or new metadata/renderer error policies affect the panel's ability to tell source gaps from drawing skips. Recheck actual main SHA and adopted APIs; never present this source-pinned candidate as current implementation. Prefer validating rendered accessible UI with actual keyboard/screen reader/browser tools after a separately authorized prototype.

**Authorial scope:** Mothlight — The Invisible Stagehand. Shared account attribution is not cryptographic agent identity.

---
schema: 1
id: 2026-11-07-ap117-pr5-cp3a-dual-surface-lifecycle-hd01
kind: lesson
scope: agent:harbor
status: superseded
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Private Auralprint 117 PR #5 candidate 23da63f8e8427d9b23c3f63794aeef6634fd466b against accepted CP2.1 main 790e71f300ad24e01ec97c7ef42f4ca500ba1080; independently executed V8 module + controlled DOM/rAF/timer cases; exact-head GitHub Actions 42377361628; PR review 5815511122."
---

# Harbor — Auralprint 117 PR #5 CP3-A dual-view lifecycle review

## Summary

**Outcome: COMPLETE; Harbor lifecycle/recovery PASS**, exact candidate `23da63f8e8427d9b23c3f63794aeef6634fd466b`. Application PR [#5](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5) adds a separately typed one-sided peak-amplitude FFT observation and a second host-owned Canvas2D surface to the accepted CP2.1 source/clock/RMS pipeline. Baseline `main@790e71f300ad24e01ec97c7ef42f4ca500ba1080`; PR open and not merged at review. The source and rendering code were read and exercised independently; no lifecycle blockers reproduced. Numerical oracle and broader interface acceptance remain assigned to Gauge and Flint, respectively.

**Scope:** Review only. No application edits, merge, deployment or CP3-B PSD. Harbor posted a GitHub COMMENTED review with explicit PASS (review ID 5815511122); it is not a GitHub-enforced approval. Owner decides integration after separate peer reviews.

## Evidence

**Independent method:** Retrieved exact candidate production JS bodies using GitHub, adapted static ES module imports/exports in V8 and injected deterministic host adapters for DOM, Canvas2D, requestAnimationFrame, timers, user controls and file reads. This executes production function bodies, not a locally cloned repository or physical browser. Additional direct spectrum-stream window-length matrix independently checked half-open spans, final complete vs incomplete cases and stale-publication invalidation. One exploratory local assertion comparing spectral DC to `0.25` used exact equality and initially flagged `0.2499999999999999`; corrected acceptance uses a suitable floating-point tolerance. No arithmetic discrepancy established by that assertion.

**Observed lifecycle positive/negative controls:**
- Exactly one `readBlock` per analysis advance and none on render callbacks; one interval and one frame scheduler drive both surfaces.
- Pause and resume preserve sample/epoch continuity and pending FFT assembly. A full window assembled across prior partial blocks is `[0,1024)`.
- Initial or successor rAF scheduling exception and a fault in **either** Canvas surface invalidate both publications, stop analysis timer and rAF, and permit explicit retry; no repeated error loop. A partial spectral assembler continues only with contiguous accepted PCM after retry; no invented zero padding or sample gap. Second-surface recovery can produce next overlap window `[512,1536)`.
- Synthetic parameter edits invalidate old readings and reset incomplete prior-revision spectral input; updated window `[960,1984)` records new source revision while epoch and absolute sample clock remain unchanged.
- Short 481-frame stereo WAV retains exact one-frame RMS (left `0.25`, right `0.5`) and `INSUFFICIENT WINDOW`, with no fake FFT sample. Channel replacement withdraws spectrum and allocates a new source epoch.
- Clean 2048-frame mono constant WAV ends with truthful `COMPLETE`, RMS `0.25` and latest full FFT span `[1024,2048)` with DC amplitude `~0.25`. Last-block Canvas fault followed by Retry yields `EOF — REPLAY REQUIRED`, not republished stale RMS/spectrum; Replay creates a new epoch.
- Canceled pending WAV import after synthetic replacement does not adopt stale bytes. Pagehide with pending read removes both publications and services; simulated BFCache persisted pageshow reloads.
- Direct spectral window-length sweep at `1,480,1023,1024,1025,1535,1536,2048,2049,2560` PCM frames emitted only expected full windows, with exact span origin and no padding. Stream invalidation at EOF did not resurrect a previously valid spectral measurement; source replacement reset prior spectrum/assembler state.

**CI attributed:** GitHub Actions [run 42377361628](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42377361628), exact PR head, completed success: **66/66 Node tests**, static/offline build, Nu HTML validation, Chromium browser smoke including dual Canvas/DPR/mobile, artifact upload and committed-diff whitespace gate. Sample FFT1024 median `0.042ms`, p95 `0.138ms` on hosted runner only, **not** target device or realtime timing assurance.

**One nonblocking configuration-truth concern:** Static `index.html` repeats `PERIODIC HANN · 1024 FRAMES · HOP 512` rather than deriving it from `CONFIG.spectrum`. Defaults currently match; a future config-only geometry edit could make this display label false. Recommend dynamic source-of-truth label or removing duplicated numbers before making FFT configuration user-editable. This is not a demonstrated current lifecycle/measurement defect.

**Evidence boundaries:** Native Chromium cancellation assumed; force-delivering canceled callbacks would require a custom scheduler generation guarantee, not presently demonstrated. Actual BFCache navigation, Firefox/Safari, cross-device/GPU frame pacing, audio realtime guarantees and physical instrument calibration not tested. No full independent checkout run; distinguish own V8 cases from GitHub CI.

## Revisit when

PR #5 head advances, Gauge or Flint finds a new acceptance blocker, FFT configuration becomes mutable, a custom scheduler/backend is added, or real-BFCache/device scheduling becomes an explicit acceptance gate. Always re-pin source and CI. Preserve the accepted CP2.1 sample/epoch and immutable numerical publication contracts.

## Superseded by latest PR #5 revision

[Corrective-head review — PASS](2026-11-07-ap117-pr5-cp3a-interchange-recheck-hd02.md) on exact head `146a8c92ef54069f679b82f63b96608ae727415d`. The original evidence remains accurate only for `23da63f8e8427d9b23c3f63794aeef6634fd466b`.

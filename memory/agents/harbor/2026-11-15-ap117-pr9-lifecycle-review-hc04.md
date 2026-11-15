---
schema: 1
id: 2026-11-15-ap117-pr9-lifecycle-review-hc04
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-pr9-lifecycle-review-session
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint 117 PR #9 AP117-002 dispatch issuecomment-6891240452; exact feature head 35ae476ec8d59c300de877381f84ec7b8c59a1fa, accepted base 0531e734a2ece59cd877ea8659069efee2e0a905; implementation record docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md; Harbor home agents/harbor-v1@db2aca24c692cbb4edebc8b512978fa46598c41a; isolated source-executed V8 fixtures and GitHub Actions run 43690871559 (attributed)."
---

# Harbor — AP117-002 PR #9 independent lifecycle and EOF review

**Task:** Focused Harbor review: recovery, EOF draining, post-final rejection, reset/currentness fences, overrun/resync, source replacement/import cancellation, pagehide and BFCache.  
**Reviewed application:** `cosmicdance-4-2-0/ap_117_KESTREL` PR [#9](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9) **exact head** `35ae476ec8d59c300de877381f84ec7b8c59a1fa` against accepted `main@0531e734a2ece59cd877ea8659069efee2e0a905`. The PR was open/draft and main unchanged at recheck.  
**Home before review:** `KestrelGaming/agents/harbor-v1@db2aca24c692cbb4edebc8b512978fa46598c41a`.  
**Deliverable:** PASS for Harbor's focused lifecycle/EOF scope, **no blocking defect found**. Exact-head evidence; integration remains Axiom/owner-held pending other independent reviews. No application implementation or merge.

## Summary

The bounded complete-spectrum delivery proof preserves the accepted CP2 input clock/epoch and CP3-A peak-amplitude definitions while adding future-only per-subscriber ordered delivery. Source-inspected [`src/analysis/spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-delivery.js#L1-L164) keeps independent capacity-limited subscriber queues, sticky overrun/fence states, live generation/continuityRevision and explicit resync/disposal. [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-stream.js#L1-L210) stages an entire successful input before committing complete FFT windows. Historical same-generation windows are valid for complete consumers without passing the latest-only `isCurrent` check, but old cached ready windows are ineligible after a continuity fence.

**PASS (scope-specific), not approval of a new production API, hardware SLA, PSD/B2 panel, plugin sandbox, or future per-panel render-failure isolation.** The current accepted host-wide render-fault stop/invalidation and `EOF — REPLAY REQUIRED` policy remain intentionally unchanged.

## Evidence

### Directly inspected exact-head sources and tests

- [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-stream.js#L32-L209) and [`src/analysis/spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-delivery.js#L31-L164): input finality, events, queue admission, generation/ordinal fences, resync, terminal draining and disposal.
- [`src/audio/file-import.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/audio/file-import.js), [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/main.js#L80-L285) and [`src/rendering/frame-host.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/rendering/frame-host.js): host import generation, render failure, retry, file EOF, pagehide disposal, persisted pageshow reload.
- [`tests/spectrum-delivery-lifecycle.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery-lifecycle.test.js), [`tests/spectrum-delivery-atomic.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery-atomic.test.js), [`tests/spectrum-delivery.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery.test.js), [`tests/spectrum-delivery-math.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/spectrum-delivery-math.test.js), [`tests/app-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/tests/app-integration.test.js), AP117-002 handoff, PR file-level diff and changed-file stats. The FFT, CP2 analysis, FrameHost and visualizer implementation files are unchanged by this PR.
- Previously authored [Harbor reset-counterexample](2026-11-07-cp3b1-psd-reset-fence-he01.md) and [Sync 02 lifecycle requirement](2026-11-14-ap117-six-engineer-sync02-hc03.md) were rechecked as historical, not transposed to an automatic verdict.

### Independently source-executed checks (observed)

For the isolated V8 tests, I fetched the **exact PR-head** contents of `fft-amplitude.js`, `spectrum-delivery.js`, `spectrum-stream.js` and `file-import.js`; stripped static ESM declarations while keeping implementation code unchanged, and evaluated through the JavaScript `Function` constructor with explicit injected dependencies. Used valid, synthetic `ap117.measurement/2` envelopes, Float32 PCM, M=8/H=4/Nfft=8 periodic Hann with explicit small delivery budget. **This is source-executed control logic, not Node package-suite or real-browser coverage.**

| Probe | Actual observed result |
| --- | --- |
| Single complete 20-frame batch and 8+4+4+4 direct-adapter partitions | Four ordered `[0,8),[4,12),[8,16),[12,20)` and terminal `ended` after queue drain |
| Cached ready-after-missed-ready reset case | Generation changes; old `ready` not eligible; new-epoch complete observation delivered correctly after explicit resync |
| Earlier same-generation completed observation | Remains eligible despite `isCurrent(oldPublicationRevision)===false` |
| Four-window atomic batch vs capacity-2 subscriber | Sticky `subscriber-delivery-overrun`; queue length zero; explicit resync abandons backlog and continues from new frontier |
| Final with no new FFT (8 + 2 samples), final with new FFT (8 + 4) and <M short final (7) | Exactly the real complete windows drain before `ended`; short-final `insufficient-complete-window`, no fabricated padding |
| Post-final ready input | Rejected with `reset required`; sticky `input-after-end`; resync remains ended until explicit reset |
| Final render invalidation and subsequent EOF status | Cached latest loses currentness; queued observation fenced; `resync` shows ended and repeated upstream `ended` does not resurrect a measurement |
| Source-revision parameter segmentation, source-epoch mismatch | Segment reset/fence and new-generation observations; invalid epoch clears undrained queue and fails closed |
| Terminal disposal, unsubscribed handle | `producer-disposed` control and irreversible ended after resync; closed subscription never reopens |
| Clean-final overflow, capacity 2 | Sticky break then explicit resync leads directly to `ended`; no invented recovery of lost final windows |
| Late NaN in 20-frame publication | Entire waveform prevalidation throws before any FFT (`Math.hypot` counter stayed zero); latest revision advances only for unavailable; no partial queued ready |
| Injected exception on bin 6 after first newly completed FFT window staged | No partial batch leaked; previous undrained queued publication also fenced; latest became unavailable with one failure revision |
| Slow/throwing consumer | Exceptions after `take` do not invoke consumer code inside producer `accept`; another subscriber and producer continue |
| Canceled/late and disposed asynchronous file import | Generation fence or disposal prevents the late `arrayBuffer()` completion from calling source-install `accept` |

**Fixture correction transparency:** Two exploratory assertions initially failed because my test code, not the application, incorrectly expected (a) no newly completed window immediately after a valid explicit new-epoch resync and (b) a [4,12) complete window after adding only 2 samples to an initial 8. The first was corrected and the reset case then PASS; the second was corrected with separate 8+2 and 8+4 final cases, both PASS. Neither erroneous fixture demonstrates an application defect. A corrected targeted run for final cases was **3/3 PASS** and a separate focused atomic/import run **5/5 PASS**; remaining correct assertions in earlier broad isolated runs also passed. No claim of one uninterrupted full-suite run.

**CI attribution:** GitHub Actions [run 43690871559](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43690871559) had `head_sha=35ae476e...`, `conclusion=success`; Axiom/implementer report 93 Node tests and static/HTML/Chromium checks. These results belong to that CI/implementer, not to my isolated V8 checks.

**Execution limits:** Attempted local `git ls-remote` against GitHub for a full checkout; DNS failed (`Could not resolve host: github.com`). Therefore **no local `npm run verify`, Chromium, true BFCache navigation, Node test-suite rerun, source playback, hardware CPU/GC measurements or hostile module test** by Harbor. The current app has no complete subscriber and the browser smoke tests its unchanged latest-only display, not future multi-panel behavior.

### Severity-ranked disposition

**Critical: none reproduced. Important blocking: none reproduced in Harbor remit.**

**Nonblocking compatibility caveats:**
1. [`src/main.js` render failure](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/main.js#L82-L97) still globally stops analysis and invalidates both displayed streams. This is accepted CP3-A policy, **not** per-panel recovery; replacing it requires separate owner approval and integration tests. A mere consumer processing exception should not be represented as a producer fault; the independent pure pull path appears correctly isolated.
2. [`readStatus()`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-delivery.js#L55-L85) can report `ended` with `queuedObservations>0`. This is deliberate, documented, and not a delivery failure; consumers must drain via `take()` until it returns `ended`. Resync at the ended frontier deliberately drops any remaining backlog.
3. [`pagehide/pageshow`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/main.js#L270-L283) wiring and file-import generation were inspected and the async import cancellation logic source-executed; real browser BFCache restoration or post-disposal event scheduling remains **not independently run**. No claim of browser-platform certification.
4. If a future caller bypasses the accepted CP2 pipeline and forges an early `status:"ended"`, the exported spectrum adapter trusts the upstream terminal status. Actual CP2 rejects premature EOF. This is a **trusted-upstream assumption**, not a demonstrated regression for supported data flows or a reason for speculative security infrastructure.

**Recommendation:** PASS Harbor's exact-head lifecycle/EOF review. Preserve the explicit stale-ready generation fences, subscriber-local sticky overrun and resync-at-frontier contract, clean final drain, terminal input rejection, pagehide terminal dispose, and old latest-only interface. No corrections required from Harbor on `35ae476e`. Other independent specialist review, full merge decision and eventual user-visible per-panel recovery remain open.

## Revisit when

PR #9 head changes; new reviewer finds a reproducer; Mothlight/Axiom choose different status semantics; an accepted owner task adds per-panel fault isolation or user-added modules; or an actual downstream complete consumer is integrated. Re-run focused and full tests on **the exact changed head**, including offline/BFCache/hardware limitations. Shared GitHub account authentication does not prove independent Harbor runtime identity.

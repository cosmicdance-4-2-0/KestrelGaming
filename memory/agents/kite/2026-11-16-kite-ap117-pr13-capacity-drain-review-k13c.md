---
schema: 1
id: 2026-11-16-kite-ap117-pr13-capacity-drain-review-k13c
kind: decision
scope: agent:kite
status: draft
evidence: observed
author: kite-session
created: 2026-11-16
updated: 2026-11-16
sources: "ap_117_KESTREL PR #13 head 2d417adab3f28315c0cbde63048851ae6e44bca8 vs main bdead48ae672ed6834eae274c8876944a79104bc; Axiom issue comments 6913221997 and 6914016022; GitHub CI 43844573608; Kite agents/kite-v1@ca23a1dda347f29165d3741d5f51e05fb08596d5; isolated V8 exact-source tests."
---

# Kite — AP117-004 PR #13: capacity, drain and performance-boundary independent review

**Assignment:** Axiom's exact-head independent six-engineer dispatch in [PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6914016022) and [initial review request](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6913221997). My remit is bounded capacity/drain, no-data polling, true source/FFT/scheduler paths, larger-geometry explicit overrun and Issue #11 operating limits.
**Exact app head/source:** `task/codex-ap117-004@2d417adab3f28315c0cbde63048851ae6e44bca8` vs accepted `main@bdead48ae672ed6834eae274c8876944a79104bc`. PR inspected as open/draft/unmerged, 10 changed paths, one commit. Live main matched accepted SHA, and exact-head GitHub Actions run `43844573608` reported completed/success.
**Agent:** Kite — The Unlicensed Inventor, branch `agents/kite-v1@ca23a1dda347f29165d3741d5f51e05fb08596d5`. Read own Kestrel branch-local `AGENTS.md`, `KESTREL.md`, `agents/kite/AGENT.md`, `agents/kite/PROFILE.json`, prior indexed PR #9/12 analysis and authorization, `kestrel/MEMORY_PROTOCOL.md` and `STATE_PROTOCOL.md`. The target app `AGENTS.md` was read. Public source, no personal audio or secrets.
**Independence limit:** The first broad PR timeline fetch displayed Axiom's task and **already-posted Mothlight, Flint and Gauge review text** before this report. I did not use their findings as an oracle or claim a blind review. The experiments below were independently constructed from the pinned production implementation and compared with its stated contract. Shared GitHub account is attribution, not separate authenticated agent runtime.
**Mode/authorization:** REVIEW ONLY. No app implementation, schema ratification, deployment or merge. Authorized own Kite branch continuity only.

## Summary

**PASS for Kite's capacity/drain/scheduling remit at this exact head.** No new demonstrated source-level or V8-executed failure in the assigned checks. This is **specialist PASS**, not six-agent consensus or owner merge authorization.

The new `createPsdSession` takes a host-selected actual spectrum producer, asks it for a complete-spectrum subscription itself, transfers the native handle to `createPsdProcessor`, retains **one latest PSD** plus bounded counters/status, and exposes a finite `drain()` receipt batch of at most its admitted `capacityObservations`. It does not accept external subscription, receipt or callbacks, and contains no DSP math, source reads or rendering. `main.advance()` admits the subscription on the first legitimate CP2 `ready` **before** calling accepted `spectrum.accept(publication)`, then drains immediately after each successful accept, before final `stop("complete")`. Latest-only peak drawing still uses the existing one FrameHost, independently of PSD. A truthful sticky break, not hidden catch-up, is the proper result when a legal atomic burst exceeds capacity.

**Critical remaining boundary:** This proof bounds per-drain *number of downstream windows* but **does not bound CPU elapsed time, browser GC, upstream FFT work or source processing with arbitrary future configurations**. The existing Issue #11 is correctly deferred. Do not certify hard realtime or unrestricted user-configurable instrumentation from the accepted CI.

## Source and configuration receipt

At `2d417adab3f28315c0cbde63048851ae6e44bca8`:
- `src/host/psd-session.js` blob `005e8f77fd7d71e5be51780a6cdbefa525bb2377`: lines 3–38 key whitelist, real producer admission, native handoff and cleanup; 39–76 bounded session state and status; 80–118 bounded drain and control; 119–138 idempotent disposal/no resync.
- `src/main.js` blob `d61c386c308dd3978331877eb0b00b8486abfa8a`: first-ready admission in `admitPsd`, current `advance` and draw paths, source switch/disposal, file/import and render failure. Direct source static occurrence check identified exactly one lexical `pipeline.advance()`, one `spectrum.accept(publication)`, one `psdSession?.drain()`, one `createFrameHost(` and one `window.setInterval(`; `drawFrame` section has no `drain(` call. These counts are **call sites**, not runtime source-read counts by themselves.
- `src/config.js` blob `c5b692a2d984f3ba0f0c863048835e5e9617da70`: frozen `psd.capacityObservations=4`; producer budgets unchanged (`maxSubscriptions=8`, per-handle `maxCapacityObservations=64`, `maxRetainedBins=262144` and `maxInputFrames=8192`), default M1024/H512/N1024, maxFFT16384, block480/nominal 10 ms.
- `docs/AP117_004_HOST_PSD_SESSION.md` blob `a63e6b6e6348ac23edffc3d889938dcda09a419c`: candidate host contract, trust limit, deliberately held break/no resync, source class and unmeasured performance.
- `tests/psd-session.test.js` blob `cae8b889ff20a6694e6346f02fdd41decea45242`: end-of-source four finals, cap2 break, mixed producers, later subscription, source fences, faulty/throwing consumers, no-data/disposal. `tests/app-integration.test.js` blob `924cd5b79199cdc3a8ce3c2a6bff9573986fb7e1` uses test-only Node module hooks to observe real main path; `tests/browser-smoke.mjs` blob `cebe99e50dbcf386f9a5047d5b223ff5327343d3` checks diagnostic and browser state. `index.html` has exactly two canvases and read-only `#psd-status`, not a third visualizer.
- Accepted DSP files `src/analysis/rms.js` blob `6f9bd57e56077726b2b80f1c669e1b40d204809e`, `fft-amplitude.js` blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`, `spectrum-delivery.js` blob `ef19cd748de41226ab0cd8375949e278f7aeb76f`, `spectrum-stream.js` blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc`, `psd-processor.js` blob `1f3937cbdaf77514c435da30879975e6a13f16ef` unchanged. No new readBlock, FFT or rAF engine in the host module.

## Executed independent V8 falsification: actual source bodies

**Method:** Used the GitHub connector to fetch production `rms.js`, `fft-amplitude.js`, `spectrum-delivery.js`, `spectrum-stream.js`, `psd-processor.js`, and **new** `host/psd-session.js` from the exact head. In a separate isolated JavaScript V8 environment, stripped only their ES-module import/export declarations and supplied the original exported dependency functions. No production function bodies or mathematical algorithms modified. Built correct CP2 RMS-fingerprint `ready` envelopes using actual `measureRms` and finite Float32 PCM. This is more than arithmetic inspection but **not** execution through Node's module loader, app integration, Chromium, real audio devices or user DOM.

**Test A: M8/H4/N8, periodic Hann, fs48000, 20 Float32 samples `x[n]=(n+1)/32`, final input, capacity4.**
- Three sequential `session.drain()` calls before any input returned zero observations, status `processing`, last-result `empty`, with no fabricated PSD.
- Once final 20-frame CP2-ready input was accepted, accepted spectrum produced exactly four complete overlapping windows, final latest peak revision 5, source start12.
- Before host drain, session correctly reported `source-ended-drain-pending`, queue4, producer upstream `ended`.
- One `session.drain()` returned four ordered PSD observations with exact BigInt spans `[0,8),[4,12),[8,16),[12,20)`, completion ordinals 1–4, DC PSD values `2.7126736111111112e-6,8.7890625e-6,1.8337673611111112e-5,3.1358506944444444e-5`. Returned status `drained`, `lastResult=ended`, `maxDrainCalls=5` and historical-last status. A repeated drain yielded zero new observations and did not advance count.
- Counting actual `Math.hypot` calls across FFT gave 20 one-sided bin computations = 4 original 8-point FFTs × 5 bins. No FFT or source-reading function is reachable from `psd-session.js`. These controls do not certify an independent complex-DFT numerical oracle; Gauge/accepted PSD tests own comprehensive math.

**Test B: same input, capacity2.**
- Producer computed all four FFT windows, retained normal latest peak (revision5 and [12,20)), and returned subscription `break` / `subscriber-delivery-overrun` with queue0. `session.drain()` returned **zero** PSD windows, sticky `broken`, `failureScope=subscriber-delivery`, and no partial misleading history. Producer `Math.hypot` count still 20. Capacity2 `maxDrainCalls=3` remains a ceiling, not actual pressure recovery.

**Test C: larger geometry M8/H1/N8, final 20 frames, capacity4.**
- Exact producer computes Q=`floor((20-8)/1)+1=13` FFT windows; final latest peak revision14 and start12; actual `Math.hypot` count=65 (=13×5). Session returns **zero** PSD windows and explicit sticky overrun, not partial catch-up. This is a legal producer configuration given the existing admission limits, and demonstrates that current host capacity4 is a **source/geometry-specific choice**, not a universal guarantee.

**Test D: currently supported normal host geometry M1024/H512/N1024, eight consecutive 480-frame valid accepted CP2-ready blocks.**
- Actual producer/session functions delivered 6 complete windows on blocks 2–7 (0-indexed), 0 on blocks 0–1. This is correct for 3840 input frames and the 1024/512 complete-window assembler. Each empty `session.drain` invoked processor `take` exactly **once**; each one-observation drain invoked it exactly **twice** (observation + empty control), under the 4+1 cap. An additional empty drain returned no new windows with one control `take`. We injected a test-only delegating wrapper *around the actual accepted processor's take method* solely to count calls; native source/process math remained original.
- Counted `Math.hypot` in accepted producer = **3078** bin-magnitude calculations = 6 transforms × 513 bins; zero additional calls occurred inside PSD drains. A full source `readBlock` count was **not** measured in this V8 test (the harness submitted valid CP2 envelopes), so single physical acquisition is supported by inspected main wiring and externally reported integration tests, not our own direct source adapter count.
- Static `src/main.js` occurrence control found only one each of `pipeline.advance()`, `spectrum.accept(publication)`, `psdSession?.drain()`, `createFrameHost(` and `window.setInterval(`; there was no PSD drain inside `drawFrame`. Call-site counts alone do not establish measured browser scheduling, but do falsify hidden second paths in this exact source.

**Combined independent source-executed V8 check outcome:** all four trial suites passed expected assertions. No rejected-window partial delivery, silent gap or render-triggered science was observed. No code change or full app checkout needed.

## Performance, retained state and alternatives

**Finite session state observed:** `createPsdSession` stores one `latest` immutable PSD; a monotonically advancing completed count, last source descriptor, last status/failure and disposal flags. Its transient `drain()` array is bounded at most admitted capacity and is frozen at return; caller-held arrays/PSD objects are **outside** the internal retention bound. Existing per-handle spectrum queues are admitted against named CONFIG resources. `readStatus()` takes an ordinary producer/consumer snapshot; a repeated empty drain does no FFT and no PSD derivation.

**One accepted source class:** For current 480-frame blocks and H512, each `accept` yields at most one window in steady state; capacity4 is more than the per-accept peak. Synchronous host drain in `advance` is a reasonable minimal arrangement for this prototype because each successful complete observation has only B=Nfft/2+1=513 PSD bins. But "bounded number of windows" is not bounded *elapsed time*: heavy consumer math or worst-case upstream FFT still occupies the same main JS thread. Timing/GC/browser responsiveness and multiple configured providers were **not** measured. Issue #11 remains open, separate from this no-duplicate-work headless integration proof.

**No extra buffering proposed:** Growing capacity, adding backpressure, worker queues, altering DSP methods or introducing another scheduler would expand this checkpoint without a demonstrated defect. For legal larger M/H or atomic source chunks where Q>capacity, the correct current behavior is a machine-readable loss/break and truthful diagnostic. Any future mandate to remain continuous needs an owner-accepted capacity/work admission policy and performance tests.

**Recovery tradeoff, not hidden numerical bug:** Session deliberately has no public resync. A legitimate synthetic parameter fence leaves PSD broken until explicit source restoration/replay, even as accepted RMS/peak resume. This is intentional, documented and visible; whether that is acceptable instrument UX belongs to owner/Axiom integration reconciliation and other specialist reviews. It should not be silently fixed by Kite. A host feeding a wrong/hostile producer is not authenticated by this first-slice session; Issue #10 still owns host origin acceptance.

**Other alternatives**: A host-level per-window synchronous callback would remove some queue machinery but violates previously accepted rejected-batch atomicity without transaction staging; an independent timer-driven PSD consumer would decouple CPU scheduling but would introduce a second scheduling policy, throughput/resource complexity and explicit source-time backlog handling. Neither is justified by current experiments. Preserve existing correct bounded synchronous host drain.

## CI attribution and evidence limits

GitHub Actions run [43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) returned `completed/success` for the exact PR head. Axiom's reviewed job log claims **131/131 Node tests**, static build, Nu HTML verification, Chromium offline/browser smoke including 3-window WAV 2048, 481-frame short EOF, pause/fence, replay and BFCache, and whitespace check. PR implementer also reports the same result and 12 focused tests. **This CI ran on GitHub, not in Kite's V8 sandbox.** I did not independently run `npm verify`, Node `registerHooks` app integration, browser, GC/heap profiler, physical hardware, or a timed full pipeline. No false real-time or production performance certification.

**Remaining protected constraints:** accepted `ap117.measurement/2` RMS and CP2 sample spans/epochs, `ap117.spectrum/1` peak amplitude, `ap117.psd/1` weighted density math and distinct producer/consumer meanings, no extra PCM acquisition, host-owned presentation/FrameHost, source/reset and global render-failure policy. No application, contract or other agent files edited.

**Decision:** `COMMENTED — PASS for Kite exact-head performance/capacity/scheduling remit`, no new correction requested. PR remains Axiom REVIEW HOLD until six source-pinned individual reviews reconciled and owner authorizes adoption/merge. Keep Issue #10 (host trust/recovery integration), Issue #11 (work/GC operating envelope), Issue #7 (PSD visualization) open as directed.

## Evidence

Observed pinned source and externally reported successful GitHub CI; independently **executed original production module function bodies** in isolated JavaScript V8 with ESM-declaration adaptation (plus one explicitly test-only take counter wrapper), with recorded exact inputs/results above; inferred applicability limited to current source geometry and stated trusted host boundaries. Peer PR reviews were visible in the initial broad comment fetch, but independent assertions are based on own source and executable probes. No local application/Chromium run or real-time performance measured. Individual attribution is a task-scoped Kite working persona, not independently authenticated agent identity.

## Revisit when

Axiom reconciles six specialist findings; the owner changes capacity or source class; the PR head changes; a fully instrumented live/browser performance test reveals unacceptable `drain` latency or GC; Issue #11 defines an adopted resource envelope; source-parameter hold/restart UX is revised; or independent Node/Chromium execution contradicts any V8 source-function trace.

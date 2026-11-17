---
schema: 1
id: 2026-11-16-ap117-pr13-gauge-host-chronology-r10
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-16
updated: 2026-11-16
sources: "Axiom assignment in Auralprint PR #13 Issue comment 6914016022; application exact head 2d417adab3f28315c0cbde63048851ae6e44bca8 against accepted main bdead48ae672ed6834eae274c8876944a79104bc; pinned actual JS bodies executed in isolated V8; independent time-weighted Parseval and BigInt controls; exact-head CI run 43844573608 job 133221415339; Gauge home 16c92243b06bb710796a79b811c3b54bc9d676c4 before new record."
---

# Gauge — AP117-004 PR #13: independent host PSD chronology and numerical audit

**Status:** COMPLETE — source-pinned independent technical review, no application changes.
**Verdict:** **PASS within Gauge's assigned per-window numerical-integrity and chronology remit.** No reproduced numerical, sample-interval, duplicate-FFT or omitted-eligible-window blocker in exercised fixtures. **Not a full PR approval, Issue #10 closure, runtime/GC performance claim, schema ratification or merger instruction.**
**Target:** [Auralprint PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13), **exact candidate head** [`2d417adab3f28315c0cbde63048851ae6e44bca8`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/2d417adab3f28315c0cbde63048851ae6e44bca8), **accepted main** `bdead48ae672ed6834eae274c8876944a79104bc`.
**Assignment:** [Axiom's six-engineer integration handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6914016022), Gauge focus: per-window math, no second PCM/FFT, 2048/481 WAV, two legal 20-frame partitions, exact sample/source/BigInt chronology, independent peak latest projection and coalescence immunity.
**Own previous work:** [R08 first PSD numerical review](2026-11-15-ap117-pr12-gauge-psd-numerical-audit-r08.md), [R09 constructor ceiling correction](2026-11-15-ap117-pr12-gauge-constructor-recheck-r09.md).
**Own home revision before this record:** `agents/gauge-v1@16c92243b06bb710796a79b811c3b54bc9d676c4`. Loaded `AGENT.md`/`PROFILE.json`, scoped project index and app `AGENTS.md`. All new findings below were derived from exact source, independent executable probes and exact CI metadata/log.
**Independence limitation:** Requesting the PR's full comments initially exposed **one existing Flint first-pass review** alongside Axiom's assignment. That review was not used to construct the numerical experiments, findings or verdict. Do **not** describe this as a perfectly blind first pass. Axiom's instructions and direct code were used thereafter; no peer's result was treated as an oracle.

## Summary

**The first host-owned complete-window PSD association is numerically and chronologically sound on tested inputs.** `src/main.js` creates the session from the first accepted CP2 sample-span descriptor **before** it calls `spectrum.accept(publication)`, then calls `psdSession?.drain()` on each successfully accepted producer publication (`src/main.js:226–255`). `drawFrame()`/rAF reads only the latest peak projection and textual PSD status (`:188–212`); it does not dequeue analysis data. `createPsdSession` obtains the native subscription from the **actual selected** producer, bounds each drain to admitted capacity+one control call and retains one latest PSD observation (`src/host/psd-session.js:11–39,80–118`). These are exact source observations, not developer prose alone.

**Own independent source-executed evidence**, using the original exact-head production JS function bodies (only ESM import/export binding syntax adapted in an isolated V8 evaluation):
- **2048-frame valid WAV-equivalent PCM, actual accepted blockFrames480, periodic Hann M1024/H512/Nfft1024:** 6 PCM source reads **including EOF**; exactly 3 completed FFT windows, only one 513-bin FFT per complete window (1,539 `Math.hypot` bin operations observed); 3 PSD observations with exact frames `[0,1024), [512,1536), [1024,2048)`; completing CP2 revisions `[6,8,10]`; last peak `[1024,2048)`; terminal `drained`. The independent integrated one-sided PSD vs window-weighted mean-square discrepancy is at most **2.1510571102112408e−16 PCM²** for the synthetic waveform `x[n]=0.1+0.32 sin(2π37n/1024)`. This tests real accepted file-PCM acquisition semantics with a constructed decoded array; it is **not** a second WAV decoder/browser run.
- **481-frame short final file-equivalent PCM, blockFrames480, same M/H/N:** exactly 3 source reads incl EOF; **zero** complete FFT windows, zero FFT-bin operations, zero PSD observations, terminates `drained` without padding.
- **Gauge's 20 exact Float32 samples `x[n]=(n+1)/32`, fs48000, periodic Hann M8/H4/N8:** one final 20-frame CP2 block and five legal 4-frame CP2 blocks both yield **four** ordered PSD windows `[0,8),[4,12),[8,16),[12,20)` with exactly matching density and weighted integrated PSD values, but deliberately different completing CP2 publication revisions: **`[2,2,2,2]` vs `[4,6,8,10]`**. Each uses exactly four five-bin spectrum operations (=20 `Math.hypot` calls) and exactly the expected source reads including EOF (`2` vs `6`). Integrated-PSD Parseval discrepancy ≤**5.551115123125783e−17 PCM²**. Both preserve final latest-only peak `[12,20)` separately from the four PSD observations.
- **Four complete windows with subscriber capacity2:** no partial PSD deliveries, `subscriber-delivery-overrun` visible as **broken**, source latest peak remains valid `[12,20)`. This is a **consumer delivery discontinuity**, not source PCM corruption or a fabricated PSD history.
- **Legal different geometry M8/H1/N8 final20, capacity4:** 13 FFT windows computed (65 total bin operations) but **zero** PSD windows falsely claimed delivered; `subscriber-delivery-overrun` breaks the subscriber atomically. This is an intentionally unsupported complete-history capacity for the selected host policy, not silent window coalescing.
- **Far-BigInt trusted adapter (not CP2 full-pipeline acquisition):** start frame `2^80+1055`, rectangular M8/H4/N16, fs96000, channel `right`, epoch `large-epoch:right`, source revision3, source tap `file-pcm` and file sample clock. All four exact half-open spans, descriptor fields, completion ordinals and metadata match; four FFT windows =36 FFT-bin operations, **no additional `Math.hypot` calls during `session.drain()`**; latest peak and latest PSD refer to final `[start+12,start+20)` only. The accepted full CP2 pipeline's first block is required to begin at frame0, so the far-offset case is explicitly **trusted-adapter-only**.

**Verified CI provenance:** Exact-head [Actions run 43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608), job `133221415339`, was fetched and its log inspected: **131/131 Node tests passed, 0 failed, 0 skipped**, static build, vnu HTML, Chromium smoke and representative rendered HTML succeeded. The log explicitly includes app PSD diagnostic, synthetic pause/parameter fence, 2048/481-frame cases, two Canvas surfaces, DPR2/mobile, source/replay/cancel, pagehide/BFCache, and zero remote requests. These are **CI-attributed** execution results, not a local npm/browser suite rerun here. The implementer's claimed local run also appears in the PR, and was not substituted for the independent tests.

**Verdict boundary:** **PASS** for assigned numerical/chronology checkpoint at this SHA. Axiom retains REVIEW HOLD until all disciplines report; accepted method and typed PSD schemas were unchanged by this integration PR. No unauthorized application changes.

## Evidence

### Pinned file receipts and applicable contract

| Exact PR-head source | Git blob SHA | Relevant logic |
| --- | --- | --- |
| [`src/host/psd-session.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/host/psd-session.js) | `005e8f77fd7d71e5be51780a6cdbefa525bb2377` | Native subscription origin at lines 11–38, 4+1 bounded drain at 39, 80–118 |
| [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/main.js) | `d61c386c308dd3978331877eb0b00b8486abfa8a` | First accepted CP2 descriptor 109–134, advance/admit-before-FFT/drain 226–255, render-only 188–212, dispose-before-reset 267–276 |
| [`src/config.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/config.js) | `c5b692a2d984f3ba0f0c863048835e5e9617da70` | Production source block480/sample-rate48000, M1024/H512/Nfft1024, PSD capacity4 |
| [`src/analysis/psd-processor.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/psd-processor.js) | `1f3937cbdaf77514c435da30879975e6a13f16ef` | Accepted single-window periodogram conversion, unchanged from merged PR12 |
| [`src/analysis/fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/fft-amplitude.js) | `ee35e0793aceb5eb9e3fc49d27f293a1719effc5` | Accepted FFT, no new transform |
| [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/spectrum-stream.js) | `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc` | Accepted once-per-complete-window stream |
| [`src/analysis/spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/spectrum-delivery.js) | `ef19cd748de41226ab0cd8375949e278f7aeb76f` | Producer-specific ordered observation queue, capacity loss semantics |
| [`src/analysis/pipeline.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/analysis/pipeline.js) | `25f396217a54501d3ea3565bac1b8e2eb0c46b0f` | Single CP2 source acquisition and own validated PCM sample spans |
| [`src/audio/pcm-buffer-source.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/src/audio/pcm-buffer-source.js) | `7fd18ecb6a579dcc7f1fc70c64974602f0c9c0fb` | File source block and legal final short tail |
| [`tests/psd-session.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/psd-session.test.js) | `cae8b889ff20a6694e6346f02fdd41decea45242` | New host session positive/negative and provenance controls |
| [`tests/app-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/tests/app-integration.test.js) | `924cd5b79199cdc3a8ce3c2a6bff9573986fb7e1` | Tests production `main.js` with delegating Node module hooks; CI verifies actual host path |
| [`docs/AP117_004_HOST_PSD_SESSION.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2d417adab3f28315c0cbde63048851ae6e44bca8/docs/AP117_004_HOST_PSD_SESSION.md) | `a63e6b6e6348ac23edffc3d889938dcda09a419c` | Candidate source/status/coverage contract, explicit no-resync tradeoff, no PSD panel |

The GitHub [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) gate requires actual subscription/producer binding, truthful terminal drain, explicit lost coverage and no general broker. PR13 is a narrow *host integration proof*, not automatic final closure of Issue #10 or performance Issue #11.

### Numerical contract

The exact unchanged PSD method is `ap117.psd/1`, `real-one-sided-windowed-periodogram-density/1`; digital density, no physical calibration or Welch average.

For original M samples and FFT Nfft≥M, one-sided peak bins `A[k]`, sample rate `fs` and `ENBW = fs U/S1²` where `U=Σw²` and `S1=Σw`:

    c[k] = 1 at DC and Nyquist, 2 at interior bins
    P[k] = A[k]^2/(c[k] ENBW) = c[k] |X[k]|^2/(fs U)
    sum_k P[k] (fs/Nfft) = sum_n (x[n]w[n])²/U

**The integrated PSD is window-weighted power and is not interchangeable with accepted CP2 whole-block unweighted RMS².** Zero padding alters bin spacing, not original Hann ENBW. PR13 adds no second FFT, no second PCM source read, no rendering-controlled analysis cadence, and no physical-value extrapolation.

**Method and source invariants independently checked:**
1. Observation `quantity=power-spectral-density`, `unit=normalized-pcm-amplitude-squared-per-hz` and method exactly matching existing accepted `ap117.psd/1` in separate BigInt/right-channel fixture.
2. All `sampleSpan` values preserve exact BigInt half-open frame intervals, sourceId, sourceEpoch, sourceRevision, channelId, tap, clockDomain and fs, across actual CP2 and far BigInt trusted adapter.
3. Completing CP2 revision is attached to its final contributor block and may differ with valid partitions while scientific intervals and PSD densities match.
4. 3×513=1539 FFT bin magnitudes for the valid WAV2048, no extra FFT on `session.drain`, and only one source acquisition per CP2 advance.
5. Latest peak read is the last completed spectrum but PSD session consumed all windows; scientific delivery must not be calculated from Canvas drawing frequency.

### Measured window witness table

| Input | Complete-window spans | Own FFT bin operations | Source reads incl EOF | Terminal |
| --- | --- | ---: | ---: | --- |
| 2048 frames, block480, M1024/H512/Nfft1024 | `[0,1024),[512,1536),[1024,2048)` | 1539 | 6 | drained, 3 PSD |
| 481 frames, block480, same M/H/N | none | 0 | 3 | drained, 0 PSD |
| 20 frames final20, M8/H4/N8 | `[0,8),[4,12),[8,16),[12,20)` | 20 | 2 | drained, 4 PSD |
| 20 frames 5×4, M8/H4/N8 | same four | 20 | 6 | drained, 4 PSD |
| 20 final, M8/H4/N8, capacity2 | producer computes 4, **consumer receives 0** | 20 | 2 | broken, `subscriber-delivery-overrun` |
| 20 final, M8/H1/N8, capacity4 | producer computes 13, **consumer receives 0** | 65 | 2 | broken, `subscriber-delivery-overrun` |

In both successful Gauge partitions, DC densities are exactly `[2.7126736111111112e−6, 8.7890625e−6, 1.8337673611111112e−5, 3.1358506944444444e−5]` normalized PCM²/Hz, independent of block partition. One 20-frame block completes all with CP2 revision2; five4 completion stamps are `4,6,8,10`. In both, spectrum `readCurrent` has final `[12,20)` while PSD `completedObservations=4`. No silent history loss.

**Independent time-domain oracle** used separate window-weight sums of actual Float32 PCM and compared to integrated PSD. Maximum discrepancy for 2048-frame waveform 2.1510571102112408e−16; for Gauge20 5.551115123125783e−17 (normalized PCM²). This is a numerical comparison, not a proof over arbitrary real waveforms, or a browser device-timing test. `Math.hypot` function-call counts use original FFT implementation, not a generic full CPU profiler.

### Lifecycle and outstanding boundaries

**Confirmed by exact source:** `src/main.js:151–159` authorized slider setter records source revision and publishes spectrum invalidation; `:60–92` status marks broken output and historical PSD; `:94–108,267–276` closes old session before spectrum reset when source is replaced; `:226–255` drains PSD after accepted spectrum publication and before final `stop("complete")`; `:188–212` renders latest peak without dequeuing PSD. The old status is historical and from the prior association, not a recovered uninterrupted series.

**Deliberate hold-on-break:** A lawful synthetic parameter edit can permanently render the current PSD session unavailable while PCM/peak continue. This is **not silently represented as current or complete**; the host exposes lost coverage and requires explicit source restoration, replacement or replay. It is a product recovery tradeoff for Mothlight/Harbor/owner, **not an observed numerical computation failure**. The host intentionally has no resync/backfill. Re-admission from a later window would lose earlier discontinuity, so its absence is defensible until a deliberate future policy is adopted.

**Correct use of UI:** The new PSD text is a *status diagnostic* and explicitly says single-window periodogram; it is not a plotted PSD, noise-floor estimator, physical dB reading, continuous historical spectrogram or a third scientific observation clock. The last painted peak span is presentation history, not analyzer sample chronology.

**Remaining unverified:** Full independent execution of `src/main.js` browser harness here (CI ran it); all browser/GC overhead and source-class pressure; adversarial same-realm producer/host substitution; generic configuration changes in live app; physical acoustic calibration; complete-host async consumer scheduling; deep memory profiling; different application scheduler configurations; future Issue #7 PSD visual panels. No claim of real-time/deterministic device performance.

**No new contract authority:** Issue #10 remains open pending Axiom reconciliation, Issue #11 performance/GC deferred; candidate `ap117.psd-session/1` status is subject to owner acceptance. This report neither certifies security boundary beyond trusted host nor claims independent runtime identity from a shared GitHub login.

### Reviewer verdict

**PASS — Gauge mathematical and source-chronology remit at exact `2d417adab3f28315c0cbde63048851ae6e44bca8`.** I request **no new mathematical correction**. Do not modify protected CP2/FFT/PSD algorithms to solve a non-reproduced numerical defect. Preserve the once-per-completion subscription path, BigInt source lineage, truthful discontinuity labels and distinct latest-value presentation. The other five reviewers' domain findings and owner decision must be reconciled independently before a merge decision.

**Counterexamples which would change my verdict:** (a) a legal CP2 source partition loses a complete window without explicit subscriber break, (b) an actual new `src/main.js` path introduces a second source read/FFT, (c) a BigInt span/source-revision mismatch, (d) a density value that fails independent same-window DFT/Parseval, (e) a footer or display claiming continuous current PSD after an intentional fence, or (f) a terminal buffer with undrained pending complete windows shown as finished.

**Attribution:** Own theoretical and executable checks, exact source SHA and CI provenance preserved; no app implementation, test changes, merge, deployment or other agent home was modified.

## Revisit when

PR #13 head changes, Axiom reconciles first passes, Stage 4 of PSD extends methods, a new source class/geometry is authorized, host source/epoch/revision rules change, or Issue #10's recovery/closure requires additional tests. At that time pin the new SHA and rerun: 2048/481 source partitions, Gauge20 split/final, overrun cases, far BigInt, observer/renderer independence and numerical Parseval.

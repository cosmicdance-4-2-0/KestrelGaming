---
schema: 1
id: 2026-11-14-ap117-sync02-gauge-completeness-r06
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-14
updated: 2026-11-14
sources: "Owner-delivered Auralprint 117 Team Synchronization 02, Axiom authored 2026-11-07, local uploaded document; application main 0531e734a2ece59cd877ea8659069efee2e0a905; source-executed exact modules and independent Python cmath DFT 2026-11-14; Gauge own prior B1 design G05; no new team replies consulted."
---

# Gauge → Axiom — Team Synchronization 02: what “complete” must mean

**From:** Gauge — The Witness (authorial engineering perspective, not authenticated separate process).
**To:** Axiom — The Geometer (primary integrator) via [Auralprint Issue #8](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8).
**Task:** Independent measurement-integrity challenge; synchronization design only.
**Accepted exact application SHA:** [`0531e734a2ece59cd877ea8659069efee2e0a905`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/0531e734a2ece59cd877ea8659069efee2e0a905), also verified current `main` on 2026-11-14.
**Gauge identity/authorization:** `agents/gauge-v1`, starting at `4b6068443beab7ceb86e418fafdc16edd7c6a9d2`; loaded branch `AGENTS.md`, `KESTREL.md`, Gauge `AGENT.md` and `PROFILE.json`, scoped memory protocol, project continuity index and own B1 numerical design [G05](2026-11-07-ap117-cp3b1-gauge-psd-design-g05.md).
**Disposition:** **COMPLETE — independent design and bounded exact-source test only.** No application code change, PR, B1/B2 implementation, schema adoption, merge, deployment, or other agent memory modification.
**Verdict:** **ALIGN ON OWNER'S ANALYSIS-FIRST GOAL; REQUEST A DEFINED COMPLETE-DELIVERY CONTRACT BEFORE IMPLEMENTING THE NEXT ANALYSIS CONSUMER.** Exact C-stream transport is an engineering choice, not yet accepted. Current mathematical B1 option C survives, but its *latest-only condition* must not be treated as a universal provider restriction.

## Summary

**Completeness belongs to a specific observation sequence *and* a specific consumer delivery policy, not simply to the FFT calculation.**

The current source computes all actual complete overlapping windows in an `accept()` call, increments its spectrum publication revision for each, but only exposes the **last** through `readCurrent()`. This works for SpectrumScope's current latest-value presentation. It cannot feed a consumer claiming complete ordered history if two or more FFT windows finish during one source block. An unobserved revision jump is not the lost bins, and no downstream numerical transformation can reconstruct those absent windows from the last peak-amplitude bins alone.

**Important correction to the handoff's illustrative partition B:** the baseline CP2 `AnalysisPipeline` requires every non-final PCM block to contain precisely its configured `blockFrames` count (`samples.length < blockFrames && !final` is rejected). Thus `8,4,4,4` is not a legal sequence through a **single accepted pipeline with blockFrames=8** (the second non-final 4-frame block fails). It is a legitimate *conceptual spectral-adapter partition*, provided the adapter is fed correctly shaped CP2 publication objects directly, but should **not** be called a verified end-to-end CP2 partition. I verified the same substantive invariant with two legal real-CP2 partitions: **one final 20-frame block** (`blockFrames=20`) versus **five 4-frame blocks** (`blockFrames=4`), identical 20 PCM samples and source identity. This is a fixture correction, not rejection of Axiom's delivery concern.

**Prior G05 adjustment:** A **single** `ap117.psd/1` no-detrend, single-window periodogram is statistically/mathematically valid from one corresponding `ap117.spectrum/1` observation. It needs *every* FFT window **only if** B1 contract promises a PSD *series covering every configured complete window*, or serves a subsequent all-window average/history. Make that choice explicit. A renderer-only PSD latest value need not demand every window; a Welch/spectral-flux/onset/temporal estimator must receive its declared sequence without silent loss or invalidate the result. The math `P[k]=A[k]^2/(c[k] ENBWHz)` is unchanged for the matching configured window; no extra FFT is intrinsically required.

**Most dangerous boundary:** A frozen `ready` object can survive upstream reset. Publication immutability does not guarantee currentness. A consumer must verify the live producer's epoch/fence **at consumption**, or rely on a demonstrably complete ordered event lifecycle with reset/discontinuity barriers. A stale ready object must not become fresh by replaying a queue.

## Evidence

### Source receipts and limits

Inspected exact accepted application files:

| Pinned source | Git blob | Finding |
| --- | --- | --- |
| [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/spectrum-stream.js) | `19c34cb8958c204e1ee529ee2c1adc773c8b37c2` | Four complete windows are computed per 20-frame accept at M8/H4; only `current` is externally readable. `revision` increases per completed window; `reset` invalidates current without deleting an old externally held frozen object; `isCurrent` queries live readiness. |
| [`src/analysis/fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/fft-amplitude.js) | `ee35e0793aceb5eb9e3fc49d27f293a1719effc5` | Accepted peak-amplitude normalization, Hann coefficient sums, ENBW, one-sided DC/Nyquist behavior. |
| [`src/analysis/pipeline.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/pipeline.js) | `25f396217a54501d3ea3565bac1b8e2eb0c46b0` | Strict non-final block length, source identity, BigInt contiguous PCM chronology, copied Float32 PCM, currentness fence. |
| [`src/audio/pcm-buffer-source.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/audio/pcm-buffer-source.js) | `7fd18ecb6a579dcc7f1fc70c64974602f0c9c0fb` | Legal single 20-frame final file versus five 4-frame source blocks through existing CP2. |
| [`src/analysis/rms.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/rms.js) | `6f9bd57e56077726b2b80f1c669e1b40d204809e` | Actual CP2 RMS method used for source-executed fixture; not a PSD. |
| [`src/config.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/config.js) | `414e695e4fc5f00f0c388e9f87fa9c756ac333f6` | Default spectrum M1024/H512/Nfft1024 periodic Hann; defaults are not global future analyzer policy. |
| [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/main.js) | `4c7ffc085da934ff76a4b9e15d611eb6b26b796d` | One `createAnalysisPipeline.advance` source read, then `spectrum.accept`; two view models render via one FrameHost and no source re-read by SpectrumScope. |
| [`tests/spectrum.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/tests/spectrum.test.js) | `59f6a26bf9575c176c58d8167f4e7a8c72a22b02` | Existing partition test uses 13 and 16 frame blocks ≤ hop16 so each new FFT window is externally observable. It does not cover a multiwindow *single* `accept()`. |
| [`docs/CP3_FREQUENCY.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/docs/CP3_FREQUENCY.md) | `0d65f1aa912cd3c7d19884c4472acc8622172e28` | Explicit latest-only CP3-A display contract, owned complete-window FFT, no PSD. |

[Post-merge CI 42438949177](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42438949177) has a successful `verify` job, including numeric/boundary tests and Chromium browser smoke. This is historical baseline evidence, **not** a validation of any contemplated subscription seam, multi-display UI, live hardware or high-frequency processing. The handoff reports 67/67 tests; I inspected the successful job step list this turn but did not rerun the suite.

**Independent source-executed control, 2026-11-14:** Fetched the exact five production modules `rms.js`, `fft-amplitude.js`, `spectrum-stream.js`, `pipeline.js` and `pcm-buffer-source.js` from the pinned commit. In an isolated V8 function, stripped only module import/export declaration syntax and evaluated the original implementations without changing function bodies. Fed source PCM `x[n]=(n+1)/32` for n=0..19 (exact Float32 representable) at `fs=48000`, `M=8,H=4,Nfft=8,periodic-hann` through actual CP2 pipeline plus spectral adapter.

| Legal partition | CP2 input spans | What successive `readCurrent()` calls exposed |
| --- | --- | --- |
| A, `blockFrames=20` | `[0,20)` final | One latest `[12,20)` at spectrum revision 5, DC amplitude 0.53125; preceding 3 windows not externally retrievable |
| B, `blockFrames=4` | `[0,4) [4,8) [8,12) [12,16) [16,20)` | Initially unavailable; then `[0,8)` at revision2, `[4,12)` rev3, `[8,16)` rev4, `[12,20)` rev5; DC amplitudes 0.15625, 0.28125, 0.40625, 0.53125 |
| Attempted handoff partition `8,4,4,4` under `blockFrames=8` | first `[0,8)` ready; next four-frame non-final block | Second `pipeline.advance()` returns `status=invalid` and reason `Source returned an incomplete PCM block` |

The normalized **full-window FFT math and source intervals are identical** across legal partitions. CP2 input-publication revisions **are not identical** across partitions and should not be expected to be: A completes all windows with the same last source block, while B uses different completing CP2 records. The `inputPublicationRevision` on a published spectrum identifies the **triggering** CP2 publication, not necessarily all CP2 publications containing samples in an overlapped window.

**Reset control executed on same exact source:** After storing old ready object at spectrum revision5, `reset("source-replaced")` publishes unavailable revision6 and `isCurrent(5)` becomes false, while the old frozen JS object still reads `status=ready`. Consumers must use a live currentness fence or enforce a reset barrier. This is an observed property, not a claim of an existing exploit in the present single-view host.

**Independent numeric oracle (separate from production FFT):** Python standard-library complex direct DFT of the exact 20-sample series and independent sums of periodic Hann weights. `S1=4`, `U=3`, `df=6000 Hz`, `ENBW=9000 Hz`. Across four complete windows:

| Source span | independent DC peak amplitude `A[0]` | independent density `P[0]` (PCM²/Hz) | integrated density / weighted mean square |
| --- | --- | --- | --- |
| `[0,8)` | 0.15625 | 2.71267361111111e−6 | 0.02566508650732670 |
| `[4,12)` | 0.28125 | 8.78906250000000e−6 | 0.08035258650732670 |
| `[8,16)` | 0.40625 | 1.83376736111111e−5 | 0.16629008650732670 |
| `[12,20)` | 0.53125 | 3.13585069444444e−5 | 0.28347758650732670 |

For all four, `sum_k PSD[k] * df` agrees with independently summed `sum_n x[n]^2*w[n]^2/U` within **5.56e−17** absolute normalized PCM² in this small direct-DFT fixture. These are *mathematical oracle computations*, not a test of proposed C-stream implementation (none exists). A latest-only result can produce only the final line; it cannot satisfy an oracle requiring all four distinct lines.

**Not executed:** No new application checkout or npm suite, no new provider/consumer implementation, no browser or microphone streaming timing test, no performance benchmark of event delivery, no real bounded-queue experiment, no physical calibration or multidevice certification. All numerical comparisons above are isolated controls on source and equations.

## 1. Define completeness per method and subscriber, not per canvas

Let one valid contiguous *analysis configuration epoch* have start `o`, frame count `L`, complete window width `M`, hop `H` (1≤H≤M), and FFT size `Nfft≥M`. If there are no parameter/epoch resets or source gaps, the set of **required complete window intervals** is:

    q = 0 ... max(−1, floor((L−M)/H))
    W_q = [o + q H, o + q H + M)
    window_count = 0                         if L < M
                   1 + floor((L−M)/H)        otherwise

For `L=20,M=8,H=4`, exact windows are `[0,8),[4,12),[8,16),[12,20)`. This is **4 windows but 20 distinct source samples**, not 32 unique PCM frames simply because four 8-frame windows overlap. End-of-source incomplete tail does not become a fabricated window. A reset at source revision or method configuration change starts a **new analysis-configuration epoch** at its specified first frame; do not demand the old hop grid bridge over invalid mixed-revision samples.

**Necessary separation:**
- **Mathematical completeness:** all needed source samples for a specific window were valid, finite, contiguous and same source/epoch/channel/tap/revision/method context; FFT returns one documented valid observation.
- **Provider generation completeness:** all qualifying complete windows for a declared provider configuration were computed and assigned identifiable sequence positions, or a provider fault/discontinuity explicitly says otherwise.
- **Subscriber delivery completeness:** a subscriber with policy `every` observed those ordered positions **or a definite gap/lifecycle barrier**; a viewer with policy `latest` intentionally may observe only one position, with honest sample age and status.
- **Estimator completeness:** a higher-order method only claims an output when it received whatever **coverage** its mathematical definition requires. A spectral-flux algorithm's lost previous window is a broken adjacent pair; a particular PSD point estimate does not have that dependency.

A spectrum window is not intrinsically "late" merely because the canvas renders infrequently; conversely, a fresh canvas redraw of last week's historical window does not make the measurement current. The clock comes from source frames and explicit producer lifecycle, not rAF.

### Which algorithms require which policy?

| Computation / use | Needs every selected window? | Valid consumer behavior |
| --- | --- | --- |
| **Single-window PSD periodogram at latest available window** | **No** | `latest` is mathematically sufficient; disclose historic span and no history guarantee |
| **All-window PSD series / time-frequency heatmap with true history** | **Yes**, for promised coverage | `every`, ordered windows, explicit discontinuity markers; never fill absent bins with guesses |
| **Welch-style average across a declared set of overlapping periodograms** | **Yes**, for that estimator's coverage | `every` across included windows; gap causes reduced/invalid coverage and method-specific rebase, not silently unbiased/full coverage |
| **Spectral flux, phase-change, onset detector on successive FFT frames** | **Yes**, if their method explicitly uses adjacent hops | On missing frame, invalidate adjacency-based difference/derivative and re-establish baseline only after a known new starting pair |
| **Tempo estimator from derived onset event stream** | Conditional | May consume events or deliberate resampled/lowered-rate data if its method specifies that policy; no silent event drop under a claimed complete event history |
| **Current frequency indicator, latest displayed band estimator, SpectrumScope painting** | **No** if single-window/latest-defined | Coalescing is deliberate visual policy, not a new spectral measurement |
| **CP2 block RMS** | Independent block measurement | Do not relabel as VU, loudness or integrated PSD; its own block/source provenance persists |

**Do not assert that averaging overlapping spectra reconstructs the unweighted full-file RMS.** Overlapping Hann windows assign unequal sample weights and a Welch estimate has its own statistical method and coverage. Multiple PSD panels can use the same upstream numerical method when compatible, but no analysis result gains precision merely because more canvases display it.

## 2. Proposed measurable provider/consumer invariants

**M1 — Single acquisition truth.** One source `readBlock` per accepted PCM advance. Every downstream analyzer consumes the CP2 validated copy/identity/clock, not a second source read. Different FFT configurations may legitimately require **additional FFT computation** from that same PCM stream; do not promise zero duplicate DSP work for incompatible configurations.

**M2 — Window selection and unit fidelity.** Every spectral observation has exact BigInt half-open sample span, sourceId, sourceEpoch, channelId, tap, sourceRevision and clock domain/sampleRate; configured method and window/FFT geometry identify the exact one-sided peak-amplitude convention. A subscription that needs M8/H4 is not satisfied by silently changing it to M1024/H512 or vice versa. Configuration change must be explicit and versioned; same-window PSD conversion only when window and ENBW fingerprints match.

**M3 — Ordered sequence coverage.** Within a producer instance/generation and stable method configuration, each actually completed FFT window has a unique monotone *observation sequence position*, with start/end from its analysis hop grid. An `every` subscriber sees every position in order, **or** an explicit gap describing missing range/status. No silent skip or duplicate delivery is counted as valid coverage. A provider's `publication revision` is not a surrogate for its sample count or event count; invalidation revisions also increment, and a single source block may complete many windows.

**M4 — Preservation of the existing latest projection.** The host still offers `readCurrent()` returning the last valid accepted complete observation, or an explicit unavailable state, with its original span and method. A renderer may coalesce window deliveries; this must not destroy the ordered source of observations for another analyzer. An intentionally repeated frame is a repeated *visualization* of an old measured observation, never a new revision or pretend sample.

**M5 — Subscriber-specific delivery failures.** A queue overflow on a slow consumer means `subscriber-delivery-overrun` at that consumer boundary, not `PCM-source-discontinuity` for all consumers. A genuine CP2 source gap/invalid input means a source/producer fault affecting all dependent analyses. Both are explicit but not conflated. If a subscriber cannot accept the stream, it must not continue silently labelling derived flux/Welch output continuous.

**M6 — Bounded pressure, not infinite history.** An offline/pausable source may stop advancing CP2 until bounded consumer capacity is available, or use explicit replay if permitted. A real nonpausable source may advance with explicit dropped-window gap and consumer invalidation/rebase. Consumer exception/disposal must not silently mutate accepted sample chronology or resurrect stale current; isolate and report. No unbounded queue and no fabricated hard real-time guarantee.

**M7 — Live producer lifecycle fence.** A queued/buffered ready observation is merely *historically valid*. It is current for adoption only while its producer instance+generation+epoch/configuration fence is live. Reset/invalidate/source replacement must revoke old ready's adoptability; a stale frozen `ready` after revision 4 cannot become fresh just because a slow subscriber finally dequeued it. Provide either an explicit currentness inquiry tied to generation **or** a linearized lifecycle event queue that makes resurrection impossible. Reset barriers order before any post-reset ready from a new generation. `isCurrent` works for the existing single-current view but is not by itself a history delivery protocol.

**M8 — Lineage without a false single-block attribution.** Every spectrum `sampleSpan` accurately names the source interval; a single `inputPublicationRevision` names the CP2 publication that **completed** that window, which may include samples from preceding CP2 blocks. If the product demands a comprehensive input lineage, define an optional exact source-revision/block-coverage reference, not a fabricated claim that every FFT sample came from the completing block. For PSD C-stream, record the **specific** upstream spectrum provider identity/sequence/epoch/window span and method; no independent PSD PCM clock.

**M9 — Mathematical equivalence across legal acquisition partitions.** For identical finite PCM, source epoch, revision, method, M/H/Nfft, and window origin: four windows must have identical source spans and amplitudes (within declared numerical tolerance) whether the accepted CP2 source arrives as one 20-frame block or five 4-frame blocks. The **CP2 input-publication IDs must NOT be required to match**; they reflect actual block partitions. The PSD derived from each must match an independently computed direct DFT and Parseval oracle.

**M10 — No silent chronology after loss.** Following a gap, adapters needing adjacent windows (onset, flux) must reset or explicitly rebuild continuity. Producers may resume later complete windows but the consumer cannot reuse a pre-gap frame as the immediate predecessor. Offline historical replay can be offered only with explicit source/version lineage and without suppressing the gap.

## 3. Smallest first runnable proof, without blessing a universal broker

**Suggested owner-scoped CP3-B0 experiment (name only provisional):**

1. Keep CP2 `AnalysisPipeline` and CP3-A FFT math unchanged. Extend only the spectrum assembler's **output seam** to make each complete window individually observable while maintaining `readCurrent()` as a compatibility projection. A bounded per-`accept()` ordered completion list returned to the host is one disposable option; a guarded completion callback or small bounded queue may be smaller under measured circumstances. **Interface selection belongs to Axiom/Flint after review.**
2. Add one tiny **every-window mathematical sink** and one **latest-value renderer-like sink**, driven by the **same** validated PCM feed. Do not create a second readBlock, compositing system, UI registry, or independent source clock.
3. Use legal file PCM fixture `x[n]=(n+1)/32`, 20 actual frames, fs48000, Hann M8/H4/Nfft8. Repeat A (`blockFrames=20`) and B (`blockFrames=4`). Required event sequence: four own immutable amplitude observations in correct source order and one latest `[12,20)` projection after either partition. A read after the sole 20-frame `accept()` must still be able to enumerate all four through the chosen *new seam*; current `readCurrent()` alone cannot pass.
4. Convert **each** exposed peak spectrum to a distinct typed PSD observation using `P[k]=A[k]^2/(c[k] ENBWHz)` and compare every bin against independently calculated direct DFT. Check all four integrated PSD powers against the time-domain window-weighted mean squares listed in Evidence. `inputPublicationRevision` differences are permitted; source spans/numerics must not differ.
5. Freeze/test consumer policies: two simultaneous downstream consumers (one full-window fast, one slow/bounded) and latest renderer-like reader; inject limited queue capacity, a consumer exception, source reset, source revision change, incomplete final file, repeated historical ready, reordered/duplicate publication, BigInt index offset beyond Number.MAX_SAFE_INTEGER (at adapter-only level), and a late stale callback. Every loss or lifecycle barrier must be observed by the affected consumer.
6. Exercise at least one **paired exact-provenance case** and one **counterexample**: same four windows both partitions, then force loss of middle windows and prove a flux/Welch consumer does **not** claim the same complete result. Verify a latest-only PSD renderer can still display the last actual measurement with its honest age/status.
7. Preserve existing CP2/CP3-A acceptance fixtures and browser smoke; separately measure bounded event-seam compute and allocation on representative browser/device and declared sample source. A Node FFT microbenchmark is not a display FPS or live-device delivery SLA.

**Independent oracle MUST inspect each of four outputs**, not only final sample span, count of internal FFT invocations, a final numerical agreement, or a publication-revision jump. For source `x[n]=(n+1)/32` the four distinct `A0` and `P0` values from the Evidence table are locked controls. A candidate that returns only `[12,20)` necessarily fails even if its final bins, last revision and screen rendering are correct.

**Do not compare full publication envelopes across the two legal partitions byte for byte** because CP2 revisions and the particular finishing source block differ. Compare the source span, configuration/method, FFT math and source lineage *validity*. Compare lifecycle/sequence **relative to a declared provider generation**, not unrelated per-source publication stamps.

### Criteria for changing my recommendation

- **Reject C-stream** if an independent direct DFT or Parseval reference shows a valid same-window peak-amplitude observation cannot produce accurate PSD under the accepted normalization, or if preserving all completed windows demonstrably requires unbounded/unmanageable buffering. Existing math supplies no such failure; delivery is currently the gap.
- **Choose A (independent PSD analyzer)** if B1 is intentionally configured with a different window/hop/FFT, detrending/weighting, distinct observation availability or another estimand that cannot be derived from the upstream peak-amplitude bins.
- **Consider B (shared complex-FFT primitive)** only if multiple independently needed consumers and measured end-to-end target costs justify its enlarged regression/ownership surface; abstract reuse alone is insufficient.
- **Accept latest-only B1** if the owner explicitly scopes B1 to a point PSD with truthful latest-value status, *provided the general provider contract remains able to support complete delivery for future stateful consumers*. Do not pretend it is Welch or spectrogram history.
- **Defer subscriber framework adoption** if a minimal completion-batch/host test supports the two target delivery policies and proper lifecycle fencing without a general broker.

## 4. Explicit alignment, uncertainty, boundaries and dissent

**Owner-required (per Axiom's owner-paraphrased synchronization):** analysis-first accurate observations; sample-time correctness independent of render cadence; user-configurable instrumentation with simultaneous instruments; provider/consumer/both roles; no forced visualization-driven analytics; scene compositing separate. These are product directions, not an already chosen subscription API.

**Accepted current baseline:** CP2 RMS + waveform copy, CP3-A latest peak-amplitude FFT, one acquisition, sample/epoch truth, two Canvas surfaces and current error/EOF policy. No PSD or VU/loudness/tempo certification exists.

**Open Axiom proposals:** a shared typed delivery envelope, the delivery API implementation, complete ordered streams for analyzers versus coalescing for renderers, C-stream for same-window PSD, a separate A analyzer for divergent methods, a small CP3-B0 checkpoint name. Naming, shape, buffer capacity, failure-state words and exact consumer backpressure are not yet ratified. The old B1 latest-only C proposal was conditional on a narrower requirement, **not an unconditional prohibition** of later C-stream. B2's one-selector UI would be only a prototype choice, not architecture policy.

**My dissent:** "Every FFT window" is too broad as an unqualified requirement on **PSD**. A single-window periodogram does not depend on its predecessor. The mathematically meaningful obligation is **every window specified by the declared consumer method**, which for some stateful estimators is indeed all consecutive windows, and for latest-only point PSD is not. A generic event broker is premature; conversely, exposing only `readCurrent()` is demonstrably insufficient for any purported every-window consumer.

**Hard boundary:** No one may use a queue overrun to claim an uninterrupted spectrogram, a dropped onset sequence as complete BPM evidence, new-epoch data as a predecessor to old-epoch flux, CP2 input-publication revision as a stand-in for all sample-frame lineage, or multiple rendered views as multiple independent source measurements.

**Unverified:** performance at 48k/192k on real hardware, allocation/fanout GC, high-rate multiple providers, multichannel synchronization, true live-device overrun handling, user visual comprehension/accessibility, full downstream PSD integration, Welch/noise statistical estimates, actual chosen delivery API. None is asserted implemented or passed here.

**Paths/interfaces affected only if owner later authorizes engineering:** `src/analysis/spectrum-stream.js` output boundary, host wiring (`src/main.js` or appropriate extraction), new minimal delivery/consumer test, `docs/CP3_FREQUENCY.md` compatibility addendum and B1 design, CP3-B0 scope/roadmap if adopted. CP2/CP3-A numeric fixtures and `src/analysis/fft-amplitude.js` protected; do not change without independent mathematical justification. Future structured method/status envelope needs version discipline.

## Revisit when

Axiom reconciles all independent synchronization passes, the owner selects B1 single-point versus full PSD-series contract and allows a narrowly scoped provider prototype, a complete-window implementation is submitted for exact-source review, a proposed queue/overrun failure path demonstrates a counterexample, or a target-browser/device benchmark shows an actual boundedness violation. Re-pin source SHAs and rerun controls. Until then **the application remains unchanged and C-stream is a hypothesis, not accepted code**.

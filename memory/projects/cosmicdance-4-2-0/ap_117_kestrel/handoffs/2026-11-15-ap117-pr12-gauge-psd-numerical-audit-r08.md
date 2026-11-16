---
schema: 1
id: 2026-11-15-ap117-pr12-gauge-psd-numerical-audit-r08
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-15
updated: 2026-11-15
sources: "Owner requested independent numerical review of Auralprint PR #12; exact application head 0880fc8df9182cce9ed2c645e324a2d291375281 against accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; actual PR patch and six files, Issues #6/#10 requirement bodies, CI run 43789892097, source-executed original functions in isolated V8 with independently authored complex DFT and Python cmath; Gauge home c013c519bdd64d1b37906f1aec8fdea54909ba07 before record. No new PR12 peer reviews read."
---

# Gauge — Auralprint AP117-003 / PR #12 PSD numerical review (R08)

**Verdict: NUMERICAL PASS at exact PR head, without approval of the proposed interface or merger.**

**Application PR:** [#12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12) — proposed complete-window PSD consumer. **Pinned head:** `0880fc8df9182cce9ed2c645e324a2d291375281`; **accepted base:** `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. PR was open, draft and unmerged on review. Scope is **read-only mathematical verification** and bounded source-level interoperability checks. No production code, PR patch or merge was changed. The exact proposed `ap117.psd/1` and `ap117.psd-delivery/1` schemas are **not yet accepted contracts**.

**Gauge identity/continuity:** Loaded `agents/gauge/AGENT.md`, the branch-local project continuity index and project `AGENTS.md`. Prior [B1 mathematical design](2026-11-07-ap117-cp3b1-gauge-psd-design-g05.md), [R06 completion delivery falsifier](2026-11-14-ap117-sync02-gauge-completeness-r06.md) and [R07 PR9 numerical pass](2026-11-15-ap117-pr9-gauge-numerical-review-r07.md) establish the pre-existing oracle, but not this new implementation's success. No new PR #12 first-pass engineering reviews were read before recording this one. Shared GitHub authorization supplies attributable posting, not independently authenticated process identity.

## Summary

PR #12 makes the first downstream headless analysis consumer of the accepted `subscribeComplete` boundary. It derives one PSD observation for each actually consumed compatible, completed spectrum window, does not obtain new PCM or call an FFT itself, and retains an explicitly historical latest result. The code does **not** implement Welch averaging, physical acoustic calibration, a separate FFT geometry, UI panel or renderer-driven computation.

**Result:** no input in the independent finite-fixture sweep produced incorrect PSD bin values, extra/missing complete windows, wrong source intervals, incorrect completing CP2 publication lineage or weighted Parseval error beyond floating-point tolerance. No numerical correction required at this exact head.

Independent evidence, not simply restating Codex's tests:

- Original **production source function bodies** from exactly `0880fc8…` executed in isolated V8, with ESM imports/exports adapted to scope-local closures. Components used actual `createPcmBufferSource → createAnalysisPipeline → createSpectrumStream → createPsdProcessor` code, not mocked PSD equations.
- **11 fixture configurations**, **80 completed PSD windows**, **2,796 one-sided density bins** checked bin-by-bin against an independently authored O(M×N) complex DFT and time-domain weighted mean-square sum; one short-source control correctly produced zero windows.
- Independent maximum per-bin **absolute** PSD difference: `8.998878031629687e−18` normalized PCM²/Hz. Largest relative error among DFT reference bins above `1e−12` was `1.904249086224719e−11`; this is a near-cancellation relative metric, not an error at the signal's dominant peak. Absolute result is the more stable discriminator for tiny bins. Maximum integrated PSD minus independently window-weighted mean square: `2.7755575615628914e−16` normalized PCM².
- An additional Python standard-library `cmath` direct DFT, independent of V8 and production FFT, recomputed all four exact Gauge DC density values and sample-window powers; maximum absolute Parseval discrepancy in that four-window oracle: `5.551115123125783e−17`.
- GitHub Actions [run 43789892097](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43789892097), job `133045679451`: independently inspected runner job/log showing **119/119 Node tests, 0 failed**, a static build/HTML verification and existing browser smoke. This is **CI-attributed**, not a newly executed local npm/Chromium suite. In particular the browser smoke does **not** exercise a new PSD UI or host integration, because neither ships.

**Disposition:** NUMERICAL PASS only. Axiom and owner retain the review/merge gate; Flint, Harbor, Latch, Mothlight and Kite own the distinct interface/ownership/lifecycle/status/performance investigations.

## Evidence

### Source receipt and exact scope

**PR diff:** six **new** files, 1,312 added lines, no old code removed or modified. Inspected actual patches, implementation, documentation, math/integration/boundary/lifecycle tests, and [Issue #6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6) and [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) request bodies. No other agents' new PR #12 review comments were consulted.

| New file | Blob SHA | Evidence |
| --- | --- | --- |
| [`src/analysis/psd-processor.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/src/analysis/psd-processor.js) | `8cca1cd0da4e4c79e2182aa3d219d55880f2efb3` | `18–32` canonical window sums; `134–190` exact same-window PSD conversion, finite/nonnegative result, owned frozen density array, metadata; `192–237` one-at-a-time pull and validation |
| [`docs/AP117_003_PSD_CONSUMER.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/docs/AP117_003_PSD_CONSUMER.md) | `aa46ec26ac95044cfe0759b15efce64ae6fb1f7c` | ``17–36` mathematical contract and numerical exclusions; ``55–125` ownership, source lineage, lifetime, proposed schema |
| [`tests/psd-math.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-math.test.js) | `a12bcad17adbdc17989d13e34afd773616688ab0` | 1,312 bins / 32 independent fixtures as reported by CI; DFT, Hann endpoint counterexample, zero padding and far-BigInt |
| [`tests/psd-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-integration.test.js) | `c6c6d059210ae3ac95e4e90b3aece5805de5a242` | Legal 20 versus five ×4 CP2 partitions, four PSD observations, same FFT count and one source-read stream, EOF/own lineage |
| [`tests/psd-lifecycle.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-lifecycle.test.js) | `abf439ef4e1fea87346ca9d708406110ea2f2bf9` | Producer fence, subscription overrun, new source and ownership, terminal drain and retention; reviewed source, not all cases separately rerun |
| [`tests/psd-boundary.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-boundary.test.js) | `1b14bd04f206dbd5113aa870a0638cc510c256fd` | Explicit forged fingerprint/bin/geometry/lineage controls; reviewed source, not all cases separately rerun |

No existing `src/analysis/fft-amplitude.js`, `src/analysis/spectrum-stream.js`, `src/analysis/pipeline.js`, `src/audio/pcm-buffer-source.js`, FrameHost, Canvas, CONFIG or other production path was modified in this PR. Mathematical verification therefore examines new PSD conversion, source consumption and the existing accepted upstream functions.

### Mathematical contract and independent falsifiers

For one real M-sample window, periodic Hann `w[n]=0.5−0.5cos(2πn/M)` or rectangular `w[n]=1`, sample rate `fs` and unnormalized N-point FFT (`N≥M`), define

    S1 = Σ w[n] > 0 ; U = Σ w[n]² > 0
    X[k] = Σ x[n] w[n] exp(-i2πkn/N)
    ENBW = fs*U/S1² ; Δf=fs/N
    c[k] = 1 if k=0 or N/2 ; c[k]=2 otherwise
    A[k] = c[k]|X[k]|/S1
    P[k] = A[k]²/(c[k]*ENBW) = c[k]|X[k]|²/(fs*U)
    Σ_(k=0..N/2) P[k]*Δf = Σ_(n=0..M-1) (x[n]w[n])²/U

**Correctness qualifications:** This is a **one-sided, no-detrend, no-averaging single-window periodogram**, units normalized PCM amplitude²/Hz. Integral is **window-weighted** mean-square, *not* automatically the CP2 unweighted whole-block RMS². The DFT zero-padding to N>M changes `Δf` and the sampled Fourier grid, not source-window ENBW or actual resolution. DC and Nyquist have c=1 regardless of padding; interior bins c=2. Finite, nonnegative input spectra are demanded.

**Gauge exact fixture:** 20 exact Float32 samples `x[n]=(n+1)/32` at fs48000, periodic Hann M8/H4/Nfft8, `S1=4,U≈3,ENBW≈9000 Hz,Δf=6000 Hz`. Actual new output windows:

| Source span | A[0] accepted peak amplitude | Computed PSD[0] (PCM²/Hz) | Independently integrated PSD (weighted PCM²) |
| --- | ---: | ---: | ---: |
| `[0,8)` | `0.15625` | `2.71267361111e−6` | `0.0256650865073` |
| `[4,12)` | `0.28125` | `8.7890625e−6` | `0.0803525865073` |
| `[8,16)` | `0.40625` | `1.83376736111e−5` | `0.166290086507` |
| `[12,20)` | `0.53125` | `3.13585069444e−5` | `0.283477586507` |

The **one 20-frame final block** produces four PSD windows with `inputSpectrum.inputPublicationRevision=[2,2,2,2]`; the equally legal **five 4-frame source blocks** produce the same bins/spans, completing CP2 publication revisions `[4,6,8,10]`. The originating spectrum's own publication revision/ordinal and source intervals remain correct. CP2 input publication revisions are finishing-block metadata, not IDs for every sample in overlapped windows. The illegal 8/4/4/4 with fixed blockFrames8 must remain an *invalid* CP2 control, not a positive alternate partition.

**Additional independently executed V8 cases** (all use real CP2+FFT+PSD functions and a separate trigonometric direct DFT):

| Case | M/H/Nfft; sample rate, window, waveform | Completed windows | Tested bins |
| --- | --- | ---: | ---: |
| Gauge one 20-frame source block | 8/4/8; 48000 Hann, arithmetic PCM | 4 | 20 |
| Gauge five 4-frame blocks | same signal/config, legal partition | 4 | 20 |
| Rectangular off-bin plus DC | 8/2/8; 44100 rectangular | 11 | 55 |
| Mixed off-bin with 4× zero padding | 64/16/256; 48000 Hann | 5 | 645 |
| Nyquist alternating + DC and 4× padding | 32/8/128; 192000 rectangular | 5 | 325 |
| Hop1 repeated localized impulses | 16/1/32; 96000 Hann | 45 | 765 |
| Hann zero-endpoint impulse | 64/64/256; 48000 Hann | 1 | 129 |
| Hann midpoint impulse | 64/64/256; 48000 Hann | 1 | 129 |
| Coherent sine at bin37 | 1024/1024/1024; 48000 Hann | 1 | 513 |
| Silence | 32/16/128; 48000 rectangular | 3 | 195 |
| Short EOF | 64/32/128; 44100 Hann, 39 samples | 0 | 0 |
| **TOTAL** | | **80** | **2,796** |

The maximum PSD **absolute** discrepancy compared to independently evaluated `c|X|²/(fsU)` was `8.998878031629687e−18`. Maximum integrated PSD vs independently computed window-weighted mean-square discrepancy: `2.7755575615628914e−16`. The largest relative difference, `1.904249086224719e−11`, occurred at a near-cancellation bin above the chosen `1e−12` relative-comparison floor. The absolute floating-point scale, and zero error for the silence and zero-weight Hann endpoint, are the important accuracy controls here.

Independent Python `cmath` direct DFT for four Gauge windows gave max integrated Parseval difference `5.551115123125783e−17`. That was a separate interpreter and code path from V8 production and V8 test oracle.

**Counterexample that the code passes:** A unit impulse at `n=0` of a periodic Hann window has window weight zero. Every PSD bin and integrated PSD must therefore equal zero while unweighted CP2 RMS² remains strictly positive (`1/M`). Conversely, a midpoint impulse contributes `w(mid)²/U` to the integrated PSD, different from unweighted RMS². Both are explicitly covered by source-tested cases and independently recomputed. Do **not** subsequently rename PSD integral to CP2 RMS².

### Numerical metadata, chronology and deliverability

- New `ap117.psd/1` output retains an owned frozen `densities` numeric array; no borrowed Float32 spectrum buffer or PCM waveform is exposed. Its source interval remains an exact half-open BigInt span, matching the parent spectrum. These are inspectable source properties, not a security boundary against hostile same-realm code.
- PSD carries `power-spectral-density`, linear normalized-PCM amplitude²/Hz, reference to digital full-scale amplitude²1, method `real-one-sided-windowed-periodogram-density/1`, detrend/averaging `none` and versioned rectangular/Hann window, plus source/epoch/channel/tap/revision/samplerate.
- The `inputSpectrum` lineage distinguishes parent generation, ordinal, continuity revision, spectrum-publication revision and *completing* CP2 publication revision. No pseudo-time based on canvas or rendering is fabricated.
- `createPsdProcessor` consumes via an actual supplied subscription's zero-argument `take()`, validates expected source/geometry/method, checks continuity and ordinal order, and withdraws readiness after malformed data or a break. The producer's backlog can be read through a clean terminal EOF; consumer drain is only reported after `take()` reaches ended. This source-level observation aligns with Issue #10; I did **not** independently execute all adversarial forged-handle/lifecycle tests assigned to Latch/Harbor.
- The PR does **not** add a second FFT or source read to the new PSD processor's implementation. The integration test instruments accepted FFT scratch allocations and source reads, reporting exactly four FFTs and 2 versus 6 CP2 reads including EOF for the legal partition pair. I inspected this test; the full CI test execution is attributed to GitHub Actions, not my local instrumentation.

### Residual questions, severity and remedies

| Severity | Finding | Decision |
| --- | --- | --- |
| **PASS (numerical)** | Correct one-sided factors, ENBW, bins and weighted Parseval over independently tested cases | No numeric correction required |
| **PASS (lineage, tested positive)** | Four-window block partition invariance, parent sample spans and CP2 completing-block revision | Preserve methods/metadata; don't compare full input publication envelopes between partition variants |
| **NOTICE (accepted/explicit)** | Same-epoch parameter change can forfeit first new-segment windows while a subscriber is broken | Must remain an **explicit continuity break**. Resync cannot invent the lost period; Harbor/Axiom own policy acceptance |
| **NOTICE (contract precision)** | Absolute PSD error can be tiny while relative error grows at almost-zero bins | Record absolute+relative tolerances with meaningful small-bin floor; do not treat near-zero relative metric alone as failure |
| **OPEN (not numerical)** | Bound-handle ownership, source/config wiring, entire mismatch/fence/EOF graph | Await Latch, Flint, Harbor and Mothlight review; source/test claims are not comprehensive independent re-execution |
| **OPEN (performance)** | Constructor O(M) recomputes window, each `take()` O(N/2+1) densities and allocations | No observed realtime/GC budget; Issue #11 and Kite's operating envelope are deferred |

A **nonblocking hardening consideration for Flint/Kite**, not a demonstrated numerics failure: `windowDescriptor` allows a descriptor with potentially very large `M` (up to its `N≤2^30` policy) and then performs an O(M) loop before verifying against the actual producer configuration. This assumes a trusted, bounded host-supplied descriptor consistent with the accepted spectrum's `maxFftFrames`. The host should constrain descriptors to its configured producer and resource limit; do not claim a general adversarial-plugin admission bound from this constructor alone. No huge allocation or runtime stall was executed here.

**No mathematical correction requested at `0880fc8…`.** Preserve the proposed PSD as distinct from spectrum peak-amplitude and RMS; do not expand this review into PSD smoothing, Welch, an independent FFT, host UI, generic registry or forced cleanup.

## Verification and limits

**Executed in this review:** exact PR source and upstream accepted module bodies, with only ESM declaration/scope adaptation, run in isolated JavaScript V8. A separately authored direct complex DFT and time-domain weighted mean-square calculation checked 2,796 values over 80 completed windows. A second Python standard-library complex DFT independently checked four canonical windows. The accepted main's existing spectrum delivery and CP2 functions were reused, not reimplemented.

**CI independently inspected:** GitHub Actions run `43789892097`/job `133045679451` is successful, log shows Node `119 tests / 119 pass / 0 fail`, added `psd-math.test.js` output reporting `1,312 bins`, static/HTML checks, Chromium browser smoke. The Chromium check covers the **existing UI**, not a new PSD display. No local repository checkout or full npm suite executed. No hardware/device measurement, physical noise calibration, runtime GC profiling, SciPy comparison or formal proof over all supported PCM values.

**Independence and authority:** No other agent's new PR12 findings read before publication; no implementation, PR merge, application branch write, agent-profile edit or foreign-agent-memory edit. This Gauge branch project handoff is the preserved record. A GitHub comment/review may communicate it using the shared human account but remains attributable reported work, not authenticated independent execution.

## Revisit when

PR #12 head changes; a corrected branch changes `src/analysis/psd-processor.js`, output method/version, window derivation or mandatory source lineage; another reviewer finds a reproducible counterexample; an owner ratifies the interface; or a later B1 independent PSD algorithm with different geometry/detrend/Welch is proposed. Repeat exact-source direct DFT, zero-padding and Hann impulse/RMS negative, legal 20-vs-5×4 source partitions, chronological/resync coverage, and the 80-window oracle before carrying this PASS to a new SHA.

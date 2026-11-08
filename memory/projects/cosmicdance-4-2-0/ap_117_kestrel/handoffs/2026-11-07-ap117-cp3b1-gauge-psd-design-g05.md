---
schema: 1
id: 2026-11-07-ap117-cp3b1-gauge-psd-design-g05
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-07
updated: 2026-11-07
sources: "Axiom CP3-B1 Gauge assignment uploaded 2026-11-07; Issue #6; ap_117_KESTREL main@0531e734a2ece59cd877ea8659069efee2e0a905; production CP3-A FFT/source; independent Python cmath, SciPy 1.17.0 and source-executed V8 oracles; postmerge CI 42438949177"
---

# Gauge → Axiom: CP3-B1 PSD contract and falsifiers

**Target:** [Auralprint 117 design Issue #6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6). **Pinned integrated baseline:** [main@0531e734a2ece59cd877ea8659069efee2e0a905](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/0531e734a2ece59cd877ea8659069efee2e0a905). Prepared independently by Gauge, 2026-11-07 America/Los_Angeles.

## Summary

**Task outcome: COMPLETE — independent *design only*.** Nothing implemented, merged, deployed, or changed in the application. This proposal is not yet agreed with Axiom, Flint, Harbor, or owner.

**Numerical verdict: high confidence.** Select a one-sided, complete-window, no-detrend **modified periodogram**, with linear normalized PCM amplitude squared per Hz. Normalize with the **sum of squared window coefficients** and the source sample rate; do not reuse the coherent-amplitude normalization as PSD. There is no physical power, dB, loudness, band-energy or statistical noise-floor certification.

**Architecture verdict: conditional preference for a third, smaller option C.** CP3-A already owns a correctly scaled one-sided peak-amplitude spectrum with complete-window sample spans and equivalent noise bandwidth. If B1 is required to report **the same windows, same configuration and latest complete spectrum only**, it can derive exact density from the existing observation with no second FFT, while producing its **own separate typed publication**. This is an algebraic identity, not naive squaring or a reinterpretation of CP3-A. If independent PSD window/detrending/coverage is a requirement, **choose A (separate PSD analyzer/stream)**; defer B (shared complex-FFT refactor) until justified.

**Outstanding owner decisions:** Is the B1 goal the smallest PSD observation for CP3-A windows, or a standalone independently configurable PSD service? Is a single-window periodogram acceptable despite its high stochastic variance? Does latest-complete-only output meet B1 requirements? Confidence is high for equations and tested equivalence, medium for conditional architecture choice, unverified for real-device performance.

## 1. Exact PSD definition, units and invariant

For real finite PCM x[n], M actual complete sample frames, source rate fs samples/second, explicit real window w[n], Nfft>=M, and an **unnormalized** forward DFT of x[n]w[n] plus optional transform-only zero padding:

    X[k] = sum(n=0..M-1) x[n] w[n] exp(-i 2π k n/Nfft)
    S1 = sum_n w[n]                  (amplitude coherent-gain sum)
    U  = sum_n w[n]^2               (PSD window-energy sum)
    c[k] = 1 for k=0 and k=Nfft/2; 2 for interior k  [even Nfft]
    P[k] = c[k] * |X[k]|^2 / (fs * U)
    df = fs/Nfft
    f[k] = k*fs/Nfft,  k=0..Nfft/2

For power-of-two Nfft as currently accepted, Nyquist exists. Required fs>0, finite samples and coefficients, U>0. P has units normalized PCM amplitude²/Hz. Only interior one-sided **power** gets the factor of 2. No DC subtraction, detrending, weighting or smoothing. This is an *estimate of spectral density on a finite window*, not a physical unit such as watts or a sound pressure estimate.

**Discrete Parseval derivation:** sum_{k=0}^{Nfft-1}|X[k]|²/Nfft = sum_{n=0}^{M-1}(x[n]w[n])². Conjugate pairing for real samples yields:

    sum(k=0..Nfft/2) P[k] * df
       = sum(n=0..M-1) x[n]^2 w[n]^2 / U

This is the **window-weighted mean square**, exactly for the chosen finite samples (within numerical rounding). Nfft padding changes df but not U, ENBW or the integral. It is **not** generally equal to CP2 RMS²: CP2 uses an unweighted typically 480-frame block, while B1 uses an overlapped 1024-frame window.

For rectangular w=1: S1=U=M, so the integral is the unweighted mean square over those M samples. It only equals a CP2 RMS² when *channel, tap, sample interval and samples* are identical.

For periodic Hann w[n]=0.5−0.5 cos(2πn/M), M>=4: S1=M/2, U=3M/8, coherentGain=0.5, mean-square window gain=3/8, ENBW=fs U/S1²=1.5 fs/M. For default M=Nfft=1024, fs=48000: S1=512, U=384, df=46.875Hz, ENBW=70.3125Hz, hop512=10.667ms of *source sample time*, window duration 21.333ms. On fs=192000, source sample hop 2.667ms; browser timer cadence is a separate issue.

**Algebraic C conversion:** The unchanged CP3-A contract publishes A[k]=c[k]*|X[k]|/S1. Therefore:

    P[k] = A[k]^2 * S1^2/(c[k]*fs*U)
         = A[k]^2/(c[k]*ENBW_Hz)

At DC/Nyquist c=1, at interior bins c=2. **Do not** use P=A², use factor 2 in the *denominator* for interior CP3-A peak-amplitude bins, and do not confuse ENBW with df. This conversion is exact in real arithmetic for the **same positive-S1 window and FFT bins**; finite floating-point error must be tested.

If M=64, fs=48000 and periodic Hann, ENBW=1125Hz. Nfft=256 gives df=187.5Hz and ENBW spans **6 fine-grid bins**, not 1.5 fine-grid bins. Zero padding increases Fourier-grid sampling, not source duration or spectral resolution.

**Statistical caution:** A single periodogram is not a smooth/stable estimator of a random process's underlying PSD. A particular seeded noise record's integral equals **its observed weighted sample mean square**, not necessarily ensemble variance. Future Welch would average *linear densities* and introduce segment counts, overlap correlation, and an explicitly different method/contract.

## 2. Proposed versioned publication and ingress

Propose **ap117.psd/1**, distinctly typed from existing **ap117.spectrum/1**:

| Field | Proposed contract |
| --- | --- |
| schema / quantity | ap117.psd/1 / power-spectral-density |
| unit | normalized-pcm-amplitude-squared-per-hz |
| reference | pcm-full-scale-amplitude-squared-1 (normalized digital PCM peak-scale amplitude 1 squared; not watts or acoustics) |
| method | real-one-sided-windowed-periodogram-density/1 |
| derivation | from-ap117.spectrum/1-peak-amplitude/1 under C; direct-windowed-complex-dft/1 under A |
| detrend / calibration / validity | none / digital-normalized-no-physical-calibration / valid |
| bins | own frozen array of Nfft/2+1 finite nonnegative linear density numbers, never aliases of CP3-A amplitudes |
| sampleSpan | frozen sourceId, sourceEpoch, sourceRevision, channelId, tap, clockDomain, sampleRateHz; BigInt startFrame/endFrameExclusive, end-start=M, placement=left-aligned-complete-window |
| window | versioned exact coefficient definition (periodic-hann/1 or rectangular/1), kind, M, Nfft, H, S1, U, coherentGain, ENBWHz. Do not store M redundant coefficients for a fully identified window |
| frequency | binCount=Nfft/2+1, binSpacingHz=fs/Nfft, f[k]=k*fs/Nfft, DC=0, Nyquist=fs/2 |
| provenance | independent monotonically increasing publication revision; inputSpectrumPublicationRevision and original inputPublicationRevision; no source read or wall-clock sample timestamp |
| availability | ready iff one complete validated window; otherwise status=unavailable, measurement=null, reason explicit, old stamps invalidated; no fabricated spectral history |

**Legitimate ready example:** all-zero actual PCM of 1024 frames, fs=48000, periodic Hann, at exact [0n,1024n):

    {
      revision: 7, status: "ready", reason: null,
      measurement: {
        schema: "ap117.psd/1", quantity: "power-spectral-density",
        unit: "normalized-pcm-amplitude-squared-per-hz",
        reference: "pcm-full-scale-amplitude-squared-1",
        method: "real-one-sided-windowed-periodogram-density/1",
        derivation: "from-ap117.spectrum/1-peak-amplitude/1",
        calibration: "digital-normalized-no-physical-calibration",
        detrend: "none", validity: "valid",
        inputSpectrumPublicationRevision: 9,
        inputPublicationRevision: 11,
        sampleSpan: {
          sourceId: "synthetic-sine", sourceEpoch: "synthetic-sine:0",
          sourceRevision: 0, channelId: "mono", tap: "generated-pcm",
          clockDomain: "synthetic-sample-frames", sampleRateHz: 48000,
          startFrame: 0n, endFrameExclusive: 1024n,
          placement: "left-aligned-complete-window"
        },
        window: {
          kind: "periodic-hann", definition: "periodic-hann/1",
          sampleFrames: 1024, fftFrames: 1024, hopFrames: 512,
          sumWeights: 512, sumSquaredWeights: 384,
          coherentGain: 0.5, equivalentNoiseBandwidthHz: 70.3125
        },
        binCount: 513, binSpacingHz: 46.875,
        psd: Object.freeze(Array(513).fill(0))
      }
    }

Actual emitted publication, metadata/span and window objects must be fully owned and frozen. Example revision numbers are illustrative, **not an observed application trace**; the sample clock domain value must match real upstream source metadata. This is JS, not JSON (BigInt cannot be serialized to JSON without an explicit separate encoding contract).

**Fail-closed C adapter boundary:** Explicitly validate input CP3-A ready publication schema/quantity/validity/unit/reference/method/calibration, complete owned immutable nonnegative finite bin array, binCount and Nfft geometry, configured window definition and S1/U/ENBW, fs/df consistency, unique/current revision, source epoch/tap/clock/channel, BigInt span length, and no stale/change-of-source adoption. Check all finite values, positive U and positive S1. On a purported ready forgery or chronology contradiction: invalidate output and throw, never retain stale density. On a normal upstream unavailable/reset: emit unavailable/null. Never silently reinterpret prior CP3-A numerics or reconstruct a missing observation. The existing CP2 pipeline and CP3-A adapter remain the only owners of actual PCM chronology and CP2 fingerprint checks. The new adapter validates its own boundary, but does **not** recompute upstream RMS or claim to independently authenticate input samples.

A repeated identical input spectrum stamp should not publish a fresh revision; only each new ready complete-window input triggers a new PSD revision. Clean final EOF may preserve the latest *actually complete* window's historic interval. Incomplete file shorter than M explicitly yields insufficient-window, not valid zero PSD.

## 3. Window assembly and interruption policy

**B1 scope lock under C:** Reuse CONFIG.spectrum defaults **M1024/H512/Nfft1024/periodic Hann**, not duplicated magic numbers or new hidden numerical settings. CP3-A already assembles complete windows across independent 480-frame CP2 source blocks. PSD derives only from its accepted complete window output. No extra source read, FFT, partial buffer, rAF loop or wall-time cursor. Its latest-complete-only publication means a large PCM read creating multiple windows exposes the final one only; B1 does **not** promise a spectrogram/history.

Synthetic parameter revision: CP3-A discards incomplete mixed-revision frames, sets new window start at exact change boundary, and B1 withdraws old density until the next complete window. Source replacement, replay and channel selection reset epoch/freshness. Render error and invalid upstream observation clear PSD readiness; retry cannot synthesize skipped samples or silently advance clock. PCM gap/overlap/malformed data is rejected by the existing CP2 pipeline; B1 must not bypass that boundary. A clean EOF with a partial tail retains the latest *complete* window with its own span, not the whole file. Post-final render failures obey existing replay-required policy.

A distinct FFT zero-padding Nfft>M may be permitted by CONFIG if the accepted CP3-A method supports it; **never** zero-pad an incomplete real PCM window to reach M. Keep input sample spans as exact half-open BigInt and ensure no conversion of large frame offsets through JS Number.

If architecture A is selected, a separate bounded PSD assembler must reproduce these chronological guarantees independently and use the accepted CP2 copied waveform once, including short final, revision reset, gaps, source replacement and retry. Do not create a second readBlock.

## 4. Architecture comparison and smallest safe path

| Architecture | Advantage | Quantifiable cost / risk | Verdict |
| --- | --- | --- | --- |
| **A — separate bounded PSD analyzer/stream from accepted CP2 PCM** | Independent PSD policy, direct textbook periodogram, no CP3-A API dependency | second overlap-window memory and FFT/allocation per complete window, duplicated chronology and reset logic, possible different latest-window selection | **Fallback** when independence or different detrend/window/history is required |
| **B — shared internal complex FFT/window primitive for CP3-A and PSD** | reuse complex bins directly; extensible for several future spectral methods | refactor protected accepted CP3-A math/interfaces, new borrowing/lifetime decisions, much larger comparative proof and regression surface | **Defer** without demonstrated need and measured cost |
| **C — derive typed PSD from existing CP3-A peak bins and ENBW** | exactly same source window; O(Nfft) arithmetic + one immutable PSD array, **zero extra FFT/PCM copy/source read**, no CP3-A implementation changes | coupled method/window policy; requires strict fingerprint, cannot use PSD-valid zero-S1 window, independent detrending/Welch or hidden intermediate windows | **Preferred** for explicitly same-window, latest-only B1 |

**Serious veto of C:** A zero-sum real window can have U>0 and a mathematically valid PSD, but CP3-A coherent-amplitude normalization by S1 becomes undefined. Independent detrending, a different PSD window/hop, complete multiwindow streaming, or operation without CP3-A are likewise impossible with C alone. If any are part of B1's required meaning, **select A instead**. Do not advocate B on aesthetic grounds.

**Counterexample to a wrong estimand:** M=64 unit impulse at n=0 under periodic Hann: w[0]=0, all density bins=0 and integrated density=0. Unweighted mean square is 1/64=0.015625. A unit impulse at n=32 yields weighted integral 1/U=1/24≈0.04166667, while unweighted mean square remains 1/64. The periodogram identity is true; claiming it always equals CP2 RMS² would be false. If the product needs time-domain impulsive energy, that is a different measurement.

## 5. Numerical oracles and falsification matrix

Proposed tolerances for normal finite normalized Float32 input at 48kHz: **per bin** absolute 1e-13 plus relative 5e-10 against independent double-complex DFT, with additional relative checks for prominent bins; **integrated density** absolute 1e-10 plus relative 1e-9 against separately summed time-domain x²w²/U. Reassess at maximum M, Nfft, fs and extreme magnitudes. All-silent actual input must give exactly zero bins; outputs must be finite/nonnegative. These are proposed acceptance thresholds, not proved universal error bounds. Match the *actual Float32 samples*, not unquantized sine formula samples.

| Input and test | Independently expected / falsifier |
| --- | --- |
| Silence, both windows | zero at all bins with valid complete-window status |
| Constant .25, M=Nfft=64, fs=48k | integrated .0625; rectangular DC P0=0.00008333333333; periodic Hann DC P0=0.00005555555556 plus Hann leakage |
| Alternating +/- .25 | Nyquist not doubled; integral .0625 |
| Peak .7 coherent sine k=7 | integral≈.245; rectangular peak density .0003266666667; periodic Hann peak .0002177777778 with neighboring leakage |
| Off-bin 7.5-tone, arbitrary phase | all bins vs independent DFT; actual finite-window weighted MS, not blindly .7²/2 |
| Rectangular unit impulse M64 | integral 1/64 |
| Hann unit impulse at n=0 vs n=32 | 0 vs 1/24; proves window-weighted power differs from unweighted RMS² |
| Mixed-phase two-tone and seeded noise-like record | all bins against separate DFT; Parseval on observed record, not arbitrary ensemble variance |
| Explicit FFT zero padding M64→Nfft256 | df 187.5Hz, periodic Hann ENBW still1125Hz; same integrated power |
| One-sided bin mapping | k fs/Nfft; DC and even-Nfft Nyquist factor1, all other positive bins factor2 in **power** |
| Shape/parameter negatives | reject M invalid, non-power-of-two/bounds Nfft, Nfft<M, invalid fs/U/S1 for C, H<=0/H>M, unknown window version, nonfinite sample/bin |
| Forged CP3-A publication | reject invalid schema/quantity/unit/reference/method/calibration, negative/NaN density or amplitudes, bin count/df/ENBW mismatch, stale revision, invalid span; revoke prior ready |
| Forged upstream CP2 envelope | current CP3-A exported adapter must continue rejecting CP2 fingerprint forgeries; B1 may not bypass |
| Source partitions and BigInt | 1/13-7-3/480/512/2048 frame partitions yield identical latest complete source interval/bins; 2^58-scale pure-adapter BigInt offsets exact |
| Source interruption | incomplete final 481/1023 => unavailable; 1024=>[0,1024); 1536=>[512,1536); 2049=>[1024,2048); gap/revision/epoch change cannot bridge partial windows |
| Stochastic ensemble (later) | for white zero-mean variance sigma², expected interior P≈2 sigma²/fs and endpoints≈sigma²/fs, but each actual realization fluctuates |

**Precision and semantics pitfalls:** relative error is meaningless near true zero; Hann suppresses endpoint impulse; deterministic sine sample quantization alters expected power; zero-padding to Nfft differs from padding missing input to M; overlapping windows have correlated estimates; a PSD bin height is not integrated band power or exact tone amplitude; plot clipping is not a numerical normalization; sample clock is not rAF time. A suitable scipy.signal.periodogram reference must explicitly choose **detrend=False** (SciPy defaults to constant detrending and would erase DC), scaling="density", one-sided, DFT-periodic window and the same Nfft.

## Evidence

**Independently executed:**

1. Disposable **Python stdlib cmath** direct DFT plus separately calculated window weights, energy sums and algebraic CP3-A conversion, **36 cases**: 9 signals (silence, DC, Nyquist, coherent/off-bin tones, edge/center impulse, mixed phases, seeded noise-like) × rectangular/periodic Hann × Nfft=64/256. Maximum absolute Parseval error **1.94e-16** (in integrated normalized squared amplitude); maximum absolute density conversion disagreement **5.05e-29**. This validates the equations and demonstrates non-identity with unweighted MS on nonstationary Hann inputs.
2. Separately ran **SciPy 1.17.0 periodogram**, **24 comparisons** (6 signals × 2 windows × 2 FFT sizes), explicitly scaling=density, detrend=False, one-sided and DFT-periodic window, against Python cmath direct DFT. Maximum absolute density-bin discrepancy **3.25e-19**. At DC .25 with Hann, P[0]≈5.5555555555555565e-05 with detrend=False and **zero** with detrend="constant".
3. Independently fetched exact CP3-A production [FFT module](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/fft-amplitude.js) blob **ee35e0793aceb5eb9e3fc49d27f293a1719effc5**, executing the source function in isolated V8 (only ESM declaration adapted). **10** selected cases included 1024-point Hann multi-signal and rectangular/Hann padded comparisons. Algebraic density-from-amplitude vs separate direct complex DFT PSD maximum absolute difference **1.95e-18**. One actual Float32 1024-case integral: **0.12002687436855014** from amplitude bins, independent weighted mean square **0.12002687436855056**, unweighted mean square **0.11289649681897684**. The latter difference is expected.
4. Inspected pinned [CP3-A spectrum stream](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/spectrum-stream.js) blob **19c34cb8958c204e1ee529ee2c1adc773c8b37c2**, [CONFIG](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/config.js) blob **414e695e4fc5f00f0c388e9f87fa9c756ac333f6**, [RMS](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/rms.js) blob **6f9bd57e56077726b2b80f1c669e1b40d204809e**, and [pipeline](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/src/analysis/pipeline.js) blob **25f396217a54501d3ea3565bac1b8e2eb0c46b0**; inspected [CP3-A contract](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0531e734a2ece59cd877ea8659069efee2e0a905/docs/CP3_FREQUENCY.md), Kestrel's [PSD calibration](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/skills/audio-dsp-core-foundation-2026-11-03/skills/audio-power-spectral-density/references/PSD_CALIBRATION.md), and [SciPy periodogram documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.periodogram.html).
5. Verified pinned postmerge [GitHub CI 42438949177](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42438949177) green: **67/67 Node tests**, Chromium browser smoke. CI FFT1024 compute-only median **0.061 ms**, p95 **0.193 ms**, hosted Node hardware only. These do **not** establish PSD performance, physical calibration, or real browser frame-budget behavior.

**Not executed or observed:** No B1 implementation, no implementation review/PR, no full local application checkout, no browser/device PSD timing or end-to-end GC profiling, no actual source-driven PSD UI, no physical calibration, no Firefox/Safari, no noise ensemble statistical confidence experiment, no microphone or real-time capture. All source-executed results are isolated mathematical checks; none constitutes shipped PSD functionality or an instrument certification.

### Performance evidence plan

Only benchmark what distinguishes A versus C or could justify B. On the same real target browser/device, same synthetic/local PCM, source block chronology, source rate (48k/192k), M/H/Nfft/window, observation count and two Canvas views, measure separately analysis+PSD CPU time per consumed PCM block/window, p50/p95/p99 and max, allocations/GC, scheduled-versus-processed sample windows, main-thread responsiveness and actual frame pacing. Compare CP3-A baseline to A's extra PSD FFT and C's O(Nfft) conversion. Do not infer from Node FFT microbenchmark or claim sample-time cadence is a browser-time SLA: 480 frames/48k is 10ms, 480 frames/192k 2.5ms. Owner must set target-device budget; no invented performance threshold, persistent telemetry or extra app framework. Prefer mathematical correctness over microbenchmark wins.

## Next action — decisions to reconcile before implementation

1. Axiom and owner decide the *estimand*: no-detrend **single-window periodogram** with window-weighted mean-square integral, versus an independently configurable PSD or averaged statistical noise-floor estimator. If the latter, this C proposal is not sufficient and A becomes appropriate.
2. Decide C vs A explicitly with Flint. C is best for minimal B1 under the accepted CONFIG.spectrum shared window and latest-only output; A is best for independent PSD method lifetime/configuration. B shared-core refactor lacks current demonstrated necessity.
3. Ratify new **ap117.psd/1** schema and exact field strings, method versus derivation semantics, immutability, lineage, invalidation, late EOF/replay and full CP3-A fingerprint gate before any code. CP3-A peak-amplitude schema and its existing acceptance fixtures must remain unchanged.
4. Commit independent DFT, SciPy detrend=False, Parseval, Hann endpoint impulse, one-sided edge factors, zero padding, random phase, real Float32 quantization and source chrono negatives as owner-protected tests. Peer review by Flint/Harbor; Mothlight/Kite CP3-B2 presentation must not alter B1 math.
5. Only after design reconciliation should Axiom open a bounded B1 implementation branch. **Gauge does not authorize implementation, merge, deployment or CP3-B2 by this handoff.**

## Revisit when

Issue #6 design is reconciled, the owner changes PSD semantics, CP3-A method/window/stream contract changes, a separate independent PSD configuration/Welch is required, direct-DFT counterexamples change, or actual target-device profiling alters the performance tradeoff. Re-pin main SHA and do not treat this proposal as consensus or integrated code.

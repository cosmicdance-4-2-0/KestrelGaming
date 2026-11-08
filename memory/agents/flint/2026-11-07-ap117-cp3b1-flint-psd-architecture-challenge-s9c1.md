---
schema: 1
id: 2026-11-07-ap117-cp3b1-flint-psd-architecture-challenge-s9c1
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-cp3b1-design-review-session
created: 2026-11-07
updated: 2026-11-07
sources: "Gauge CP3-B1 PSD design handoff g05 at agents/gauge-v1; ap_117_KESTREL main@0531e734a2ece59cd877ea8659069efee2e0a905; Issue #6 Flint challenge comment 6716513401; source-executed CP3-A FFT/stream V8 structural probe"
---

# Flint — CP3-B1 design challenge: when derived PSD is enough

## Summary

**Outcome: Design-review COMPLETE, CONDITIONAL PASS for option C only under a restricted B1 contract.** No application implementation, PR, merge, release or CP3-B2 work. [Full independent challenge posted to application Issue #6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6#issuecomment-6716513401).

Gauge's independent [numerical design proposal](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/gauge-v1/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-07-ap117-cp3b1-gauge-psd-design-g05.md) proposes A: independent bounded PSD analyzer, B: shared complex FFT/window core, or C: derive PSD from accepted CP3-A peak bins and ENBW. Gauge conditionally favors C with a same-window/latest-only B1 contract. My architectural conclusion independently agrees **only under that restriction**: C is a dependent presentation-adjacent measurement adapter, not a general standalone PSD service or reusable substrate for later Welch/history. Mathematical equivalence is necessary but insufficient to select it.

## Evidence

- **Pinned baseline, not old PR head:** [`ap_117_KESTREL/main@0531e734a2ece59cd877ea8659069efee2e0a905`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/0531e734a2ece59cd877ea8659069efee2e0a905), verified to match live main during this review. Fetched full production CP3-A `src/analysis/spectrum-stream.js` blob `19c34cb8958c204e1ee529ee2c1adc773c8b37c2`, FFT blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`, CONFIG, main wiring and contracts. Read Gauge's complete handoff and Issue #6; issue was open for a design challenge.
- **Independent structural execution:** Fetched exact-source CP3-A FFT and spectrum-stream function bodies into a controlled V8 evaluator, with only import/export declarations adapted. With M=8, H=4, Nfft=8 and 20 constant PCM frames, one 20-frame CP2 block computes four complete windows but exposes only the last [12,20) at spectrum revision 5. The exact same input partitioned into blocks [0,8), [8,12), [12,16), [16,20) yields four independently visible ready spectral starts 0, 4, 8 and 12, ending in exactly the same last observation. An additional two-frame block reuses that last ready revision, creating no new complete window. This is **not a numerical error**; it proves last-only stream observable cardinality is input-partition-dependent and C cannot reconstruct unpublished windows. One PSD per *accepted latest spectrum revision*, not per true complete physical window, is the only defensible B1 promise under C.
- **Geometry and version seam:** Existing CP3-A `ap117.spectrum/1` publishes `window.kind,sampleFrames,fftFrames,sumWeights,sumSquaredWeights,coherentGain,hopFrames`; `equivalentNoiseBandwidthHz` is a *top-level* spectral measurement field. It does **not** publish a versioned `window.definition`. Gauge's proposed PSD output includes a new `definition:periodic-hann/1`, which must be B1-owned and mapped from recognized upstream kind/current method, not falsely asserted to be an existing input field. Keep one home for PSD ENBW.
- **Algebra attribution:** Gauge independently demonstrated direct periodogram P[k]=c|X[k]|²/(fs U) and equivalent C conversion P[k]=A[k]²/(c ENBW) with DC/Nyquist factor 1 and interior c=2. No independent comprehensive PSD numeric oracle was rerun by Flint; I assessed interface semantics and observable-window loss. Gauge's numerical certainty is Gauge's, not reproduced by my structural probe.
- **Test limits:** No full local Git checkout, complete Node/Chromium suite, real-device performance, physical calibration, PSD implementation or compiled B1 tests occurred. This is a blueprint/review, not an accepted new checkpoint.

## Conditional design recommendation

**Prefer C only if the owner ratifies** the same CP3-A window/source-epoch/FFT policy, same latest-observable-window-only behavior, and single no-detrend window-weighted periodogram. A is the fallback for PSD with independent window/detrending/averaging/source lifetime. B's shared FFT primitive might be justified by actual reuse or measured device performance later; do not refactor the accepted FFT merely for aesthetics.

Define a small `ap117.psd/1` adapter with its own revision and owned/frozen linear PSD bin array, copied/frozen source span and known window metadata, distinct method vs derivation, the originating spectrum publication revision and its original CP2 publication revision. No extra source reads, rAF, PCM copy, FFT, partial buffers, duplicative CONFIG policy or generic validator framework. CP3-A remains responsible for sample clock and window geometry.

**Required boundary rules:** Validate exact `ap117.spectrum/1` schema/quantity/validity/unit/reference/method/calibration, finite nonnegative immutable bin array and consistent binCount/Nfft/fs/df/M/H/S1/U/ENBW, known window kind and span length, BigInt source span and fresh upstream stamps. CP3-A's method is the compatibility boundary; silently consuming changed amplitude normalization is prohibited. Preserve separate PSD version. Owning the output does not establish independent sample authenticity; array `Object.freeze` is not a proof of historical source ownership.

**Revision/failure discipline:** Same unchanged spectrum publication => no new PSD publication. Same input stamp with contradictory values => reject, fail closed, clear prior PSD ready. New complete valid input => new own PSD revision. A legitimate large CP2 input can skip intermediate observable spectrum starts; **do not require successive PSD source spans to equal previous span plus exactly H**. Parameter-revision changes may reset window alignment without source epoch change. Reset on source/channel/replay transitions; preserve last valid historic complete span across partial new input and clean EOF; invalidate on explicit upstream unavailable/fault or render failure. PSD adapter must not mutate CP3-A; host handles shared transport failures.

**Minimal falsifiers for Axiom:** Tests for canonical metadata and malformed fingerprint/ENBW/df/bin counts, zero/nonfinite bins, stale/conflicting stamps, exact BigInt spans, valid optional padding, P=A²/(c ENBW) vs independent complex DFT and Parseval, DC/Nyquist, Hann endpoint impulse, short final, partial-window continuation, non-contiguous *observable* windows from large source blocks, and fault-after-ready withdrawal. Do not compare PSD integral universally to CP2 RMS².

## Owner decisions unresolved

1. B1 estimand: same-window latest-only single periodogram, **or** independent PSD service/window/detrending/Welch? Choice determines C vs A.
2. Is stochastic single-periodogram variance acceptable for this checkpoint, explicitly excluding stable averaged noise-floor claims?
3. Does consumer require one PSD per actual complete window or only one per latest observable spectrum publication? **C cannot meet the first with current CP3-A.**
4. Should B1 accept only the exact current supported CP3-A amplitude method/window implementations, requiring explicit revision for a future normalization change? I recommend yes.

## Revisit when

Axiom reconciles Issue #6, owner ratifies or changes one of these four decisions, CP3-A method/pub contract changes, B1 needs all-window history or Welch, or actual device measurements justify an independent FFT/shared-core refactor. Re-pin main and validate B1 code when implemented. Do not attribute this conditional acceptance to Gauge, Harbor or the owner.

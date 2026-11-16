---
schema: 1
id: 2026-11-15-ap117-pr12-gauge-constructor-recheck-r09
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-15
updated: 2026-11-15
sources: "Owner requested PR12 exact-head corrective review; prior reviewed 0880fc8df9182cce9ed2c645e324a2d291375281; corrected application head 2acfeb9daf3b5714424455afc64bcffd237c23d7, accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; GitHub diff, actual source-executed V8 original functions on both SHAs, direct-DTF and weighted Parseval oracle, CI exact-head run 43824257458, Gauge prior R08 at 65f184c909f9fe2674cd7d2ff1e23d6d92f2bcce. Review-only."
---

# Gauge — Auralprint PR #12 R1 constructor-bound correction recheck (R09)

**Verdict:** **ACCEPT corrective head for numerical/configuration admission only; no numerical BLOCK.** This is a bounded exact-head recheck, not a full all-discipline PR approval or permission to merge.

**PR:** [#12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12).
**Reviewed previous head:** [`0880fc8df9182cce9ed2c645e324a2d291375281`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/0880fc8df9182cce9ed2c645e324a2d291375281).
**Reviewed R1 head:** [`2acfeb9daf3b5714424455afc64bcffd237c23d7`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/2acfeb9daf3b5714424455afc64bcffd237c23d7).
**Accepted base:** `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`.
**Gauge prior first-pass:** [R08 exact-head 80-window PSD review](2026-11-15-ap117-pr12-gauge-psd-numerical-audit-r08.md), an independent numerical PASS at the old head.

## Summary

**The reported constructor FFT ceiling mismatch is fixed.** Previously the PSD consumer's local `windowDescriptor` independently accepted `fftFrames` values up to `2**30` even if the associated spectrum provider configuration had `maxFftFrames=16384`. The corrected consumer requires a positive, safe-integer `maxFftFrames>=4` and `fftFrames<=maxFftFrames`, before computing any window weights. These guard conditions match the accepted `createPeakSpectrumAnalyzer` configuration policy for the exercised fixtures; there is no new magic ceiling, configuration import or change to PSD equations. The exact new diff touches **only three files**: `src/analysis/psd-processor.js`, `tests/psd-boundary.test.js` and `docs/AP117_003_PSD_CONSUMER.md`, with 55 insertions and 9 deletions. Upstream accepted FFT/source/CP2/CONFIG and presentation remain unchanged.

**Independent pre/post falsifier:** `M8/H4/Nfft32768/maxFftFrames16384` was accepted by the *old* PSD constructor, returning `empty`, and ran eight `Math.cos` evaluations for the Hann weights. At the corrected head it rejects with `PSD requires an accepted same-window radix-2 spectrum definition` and **zero Math.cos calls**. The original producer would reject that impossible FFT descriptor. This proves the specific mismatch existed and the new guard prevents it **before** window preparation.

**Independent admission sweep:** **38 focused assertions, zero failures**. Fifteen invalid PSD descriptors tested missing/undefined/null/nonfinite/noninteger/string/undersized ceilings, `maxFftFrames` below `fftFrames`, nonradix2 N, M>N and invalid window. Every one rejected before `Math.cos`. Five valid configurations admitted: M8/N8, M8/N16384 exactly at configured cap, rectangular M8/N8, M8/N8 at cap8, and M4/N4 at cap4. On the valid no-data controls, processor returns `empty` and remains unavailable rather than inventing an observation. These probes executed the **actual exact GitHub-fetched source bodies** in isolated JS V8 with only ESM import/export scope adaptations.

**Independent four-window math/regression:** Compiled the *old and corrected* real CP2, spectrum and PSD module function bodies separately. The same 20 Float32 source samples `x[n]=(n+1)/32`, fs48000, periodic Hann M8/H4/N8, passed through the real pipeline as (a) one final 20-frame block and (b) five legal 4-frame blocks. Both exact-head processors produced four PSD windows `[0,8),[4,12),[8,16),[12,20)` and each density array was **bit-identical to the old head** for its matching source partition. Completing CP2 publication revisions were `[2,2,2,2]` and `[4,6,8,10]` respectively, as before; final peak-spectrum revision remained 5. Checked 40 individual PSD bins in this two-partition recheck against a separately authored direct O(MN) complex DFT: maximum absolute PSD bin discrepancy `6.776263578034403e-21` normalized PCM²/Hz, maximum weighted Parseval discrepancy `5.551115123125783e-17` PCM². This targeted regression **does not claim** the prior 80-window/2796-bin R08 sweep was rerun in this follow-up; it remains independently documented exact-old-head evidence, and the PSD arithmetic bodies are unchanged in R1.

**CI:** Exact R1 head [run 43824257458](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43824257458), verification job `133154208864` shows **120 tests passed / 0 failed**, including new constructor negative case, plus successful static build, HTML validator, Chromium browser smoke. These are **verified runner log claims**, not new local checkout/npm/Chromium tests; the browser smoke does not exercise a PSD UI that is not present.

**Result:** **PASS** for the corrective guard and numerical nonregression. No code modification or further arithmetic change is requested within Gauge's scope.

## Evidence

### Exact source and source-contract alignment

| Artifact | New blob SHA | Finding |
| --- | --- | --- |
| [PSD processor](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2acfeb9daf3b5714424455afc64bcffd237c23d7/src/analysis/psd-processor.js) | `1f3937cbdaf77514c435da30879975e6a13f16ef` | Lines 18–34 move the max-FFT guard ahead of Hann sum computation. The PSD density loop and typed output are not modified. |
| [PSD boundary tests](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2acfeb9daf3b5714424455afc64bcffd237c23d7/tests/psd-boundary.test.js) | `f943670222dad3c11ccc774b99391bdfe820746e` | Lines 167–200 include impossible producer/PSD descriptor, zero-cosine negative controls, legal Nfft=16384 admission |
| [PSD contract](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/2acfeb9daf3b5714424455afc64bcffd237c23d7/docs/AP117_003_PSD_CONSUMER.md) | `b2c779bf57f2ba973892ec5930cfdbbf4a4bb090` | Describes ceiling parity and honestly states residual host/exclusive-handle Issue #10 boundary |
| [Prior direct mathematical audit](2026-11-15-ap117-pr12-gauge-psd-numerical-audit-r08.md) | Gauge v1 record at `65f184c909f9fe2674cd7d2ff1e23d6d92f2bcce` | Prior 80-window/2796-bin independent PSD validation; not repeated in full at new head |

The old `2**30` limit was independent of `CONFIG` and potentially inconsistent with the actual provider. The new ceiling is an explicit constructor precondition. The code still uses existing bounded two-window families, finite positive sums, radix-2 FFT, and preexisting source identity requirements. Expected FFT size is a **configuration supplied by the trusted host**, not an authenticated readback from the originating producer; this correction does not establish hostile-wrapper authentication or detect a *wrong native handle*. Correct exclusive wiring remains deliberately deferred to Issue #10.

### Adversarial boundary cases and the observed pre/post difference

| Input | Prior behavior | R1 behavior |
| --- | --- | --- |
| M8,H4,N32768,max16384 | **Incorrect acceptance** for consumer constructor; 8 cosine evaluations | **Rejected**, 0 cosine evaluations |
| Missing `maxFftFrames` | Previously optional | Rejected, 0 cosine evaluations |
| `maxFftFrames` null/NaN/Infinity/string/8.5/-1/0/3 | Independent guard absent | Rejected before weights |
| N8,max7, or N8,max4 | Independently accepted if other fields valid | Rejected before weights |
| M8,N6 / M12,N8 / illegal window | Already malformed | Still rejected before weights |
| M8,N8,max8 | Valid | Accepted |
| M8,N16384,max16384 | Valid producer-shaped configuration | Accepted without starting FFT; only 8 Hann weights |
| M4,N4,max4 | Valid minimum geometry | Accepted |

The prior first-pass R08 numerical algebra, the original complete-spectrum queue and acquisition semantics remain unchanged by R1. It would be a mistake to treat these constructor checks as proof of bounded real-time CPU, heap, GC or strong capability authentication. Numeric performance/operating envelope Issue #11 remains pending.

### Source-executed mathematical control

Independent direct-DFT formula, no production FFT used in the oracle:

    w[n] = .5 - .5 cos(2πn/8);  U = Σw[n]² = 3
    X_q[k] = Σ_(n=0..7) x[q*4+n] w[n] exp(-i2πkn/8)
    c[k] = 1 at DC/Nyquist; 2 interior
    P_q[k] = c[k] |X_q[k]|²/(48000*U)
    Σ_k P_q[k]*6000 = Σ_n(x[q*4+n]w[n])²/U

| Source frames | PSD DC (normalized PCM²/Hz) | Completing CP2 rev single / five-block |
| --- | ---: | --- |
| `[0,8)` | `2.7126736111111112e-6` | 2 / 4 |
| `[4,12)` | `8.7890625e-6` | 2 / 6 |
| `[8,16)` | `1.8337673611111112e-5` | 2 / 8 |
| `[12,20)` | `3.1358506944444444e-5` | 2 / 10 |

PSD output per-bin values are **exactly unchanged** old vs new for this valid input. As before, output is a no-detrend, nonaveraged, one-window periodogram, *not* a separate FFT, Welch estimate, calibrated acoustic measurement or CP2 unweighted RMS. The density algebra was not edited by this patch.

### Scope and remaining decision boundary

**Resolved in R1:** mismatch between PSD constructor FFT ceiling and the **supplied producer configuration**. Rejection before window-weight preparation, new negative regression and legal ceiling-edge positive control.

**Not resolved, by design:** a host could supply configuration inconsistent with the *real* producer or give PSD the wrong genuine subscription. Source stamps are not global credentials; this consumer trusts exclusive host wiring and does not authenticate third-party code. Latch/Axiom's Issue #10 integration ownership remains an explicit condition. No tests demonstrate full host integration, real-time operation, alternate PSD provider geometries, or multi-pane rendering. Two versioned `ap117.psd/1`/`ap117.psd-delivery/1` schemas remain **proposed**, not ratified by passing CI.

**Disposition:** **COMMENTED numerical/configuration PASS on R1, no required correction within Gauge's remit**. Full merge/ratification decision belongs to Axiom/owner after remaining independent reviews, and latest reviewer concerns require their own evidence. No application code, other agent memory, PR merge, shared specs or protected FFT fixture was changed.

## Revisit when

If PR #12 moves beyond `2acfeb9`, a producer configuration authority is changed, a PSD arithmetic/conversion path changes, another reviewer shows an actual host-wiring counterexample or Issue #10's consumer integration begins. Pin that exact new SHA; re-run the impossible-maxFFT constructor negative, accepted N16384 positive, matched legal PCM partitions, direct DFT/Parseval and stale-origin controls. Do not inherit this PASS blindly to later PR heads.

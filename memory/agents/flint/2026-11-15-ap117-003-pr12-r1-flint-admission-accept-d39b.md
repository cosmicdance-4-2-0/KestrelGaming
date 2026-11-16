---
schema: 1
id: 2026-11-15-ap117-003-pr12-r1-flint-admission-accept-d39b
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-003-pr12-r1-independent-rereview
created: 2026-11-15
updated: 2026-11-15
sources: "PR12 revised exact head 2acfeb9daf3b5714424455afc64bcffd237c23d7, predecessor 0880fc8df9182cce9ed2c645e324a2d291375281, accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; source-executed exact-code independent admission and final-drain probes; Actions run 43824257458."
---

# Flint — AP117-003 PR #12 R1: constructor FFT limit correction

**Task outcome:** COMPLETE — independent bounded re-review at `2acfeb9daf3b5714424455afc64bcffd237c23d7`. **Verdict: PASS in Flint's assigned API, ownership, simplicity and resource-admission remit.** The earlier CONDITIONAL PASS at `0880fc8df9182cce9ed2c645e324a2d291375281` remains an intact historical finding; its sole requested constructor correction is resolved. This is **not** team reconciliation, schema ratification, owner merge approval, device realtime certification or a review of changed future heads.

## Summary

The R1 delta from the original review is one commit / three files: `src/analysis/psd-processor.js` (+4/-2), `tests/psd-boundary.test.js` (+35/-0), and `docs/AP117_003_PSD_CONSUMER.md` (+16/-7), total **55 additions / 9 deletions**. No accepted PCM, spectrum, FFT, CONFIG, host render, app-source or subscription implementation changed. The full PR remains six additive files, draft/open/unmerged at inspection.

**Resolved finding:** `psd-processor.js:18-25` now requires `Number.isSafeInteger(maxFftFrames)`, `maxFftFrames >= 4`, and `fftFrames <= maxFftFrames` before the O(M) window-weight generation loop. This mirrors `src/analysis/fft-amplitude.js:6-13`; the unrelated `2**30` cap is gone. No shared validator, CONFIG import, duplicated FFT, or new generic architecture. This is exactly the minimal remedy Flint requested.

**Verdict:** **PASS, no remaining required changes in Flint's narrow remit at this head.** Retain deferred concerns honestly: a trusted host must bind the *correct actual subscription handle* exclusively (Issue #10 integration); the complete-window FFT operating envelope and browser/device GC remain Issue #11; PSD GUI/B2, independent PSD windows, Welch and plugin sandbox remain out of scope.

## Evidence

- **Target:** [Auralprint PR #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12), revised `2acfeb9daf3b5714424455afc64bcffd237c23d7`, accepted unchanged `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. Predecessor `0880fc8df9182cce9ed2c645e324a2d291375281`. Pin/changes independently retrieved from GitHub PR metadata and compare.
- **Exact R1 source:** `src/analysis/psd-processor.js` blob `1f3937cbdaf77514c435da30879975e6a13f16ef`; regression `tests/psd-boundary.test.js` blob `f943670222dad3c11ccc774b99391bdfe820746e`; documentation `docs/AP117_003_PSD_CONSUMER.md` blob `b2c779bf57f2ba973892ec5930cfdbbf4a4bb090`. Inspected new tests L167-200 and full guard L18-33.
- **Accepted producer reference:** `src/analysis/fft-amplitude.js` accepted base blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`. Existing `spectrum-stream.js` and `spectrum-delivery.js` were previously inspected from the identical accepted base; they are unchanged in R1. Original PR #12 Flint report [at `c9731214`](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/c9731214cd55b98d425c3d4ee9772ebca38c6a5c/memory/agents/flint/2026-11-15-ap117-003-pr12-flint-consumer-boundary-c8e2.md) details original exact-code probes, 300 legal M/H/N configurations and 5,038 derived observations.
- **Independent focused execution:** retrieved exact R1 PSD production JS body and directly executed `createPsdProcessor` via a V8 function evaluator after mechanical removal of ES module `export`. This was not a local repository Node test or browser test. Tested nine malformed/incompatible configurations, including exact original `M=8,H=4,Nfft=32768,maxFftFrames=16384`; missing max; `"16384"`, `8.5`, zero, 7, Nfft larger than custom max, non-power-of-two FFT and too-short window. **All nine synchronously rejected with `RangeError` and zero `Math.cos` calls during each rejection.** The original counterexample no longer succeeds. A legal padded `M8/H4/Nfft=maxFftFrames=16384` construct returned `empty` on untouched subscription and `unavailable/not-started` current without any FFT or PCM read. A separate source-executed real producer→subscription→PSD `M8/H4/N8`, final 20 Float32 samples `(n+1)/32`, drained four truthful PSD windows `[0,8),[4,12),[8,16),[12,20)` then `ended`; latest spectrum revision remained 5. Tests were read as well as independently reproduced.
- **Verified external CI:** [GitHub Actions 43824257458](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43824257458), head `2acfeb9...`, completed/success. Directly inspected job steps/log showing **120 tests passed, zero failed**, static build, official HTML checking, and Chromium smoke of the existing latest-value page. Independent direct-DFT CI log covers 1,312 bins with reported max density error `1.5585406229479126e-19` and window-weighted Parseval max `1.5265566588595902e-16`. **CI ran them; Flint did not rerun the full Node/browser test suite locally.** No production PSD UI was exercised.
- **Independence/authority:** Loaded Flint own profile, contract and index on `agents/flint-v1@c9731214cd55b98d425c3d4ee9772ebca38c6a5c` previously. No other agent's new PR #12 independent reports were consulted for this focused acceptance; original first pass is unchanged. Shared GitHub credential signifies source attribution, not verified autonomous runtime identity.

## Re-evaluation and minimality

The new guard reads only the producer's explicit caller-configured FFT ceiling; avoids both hardcoded independent policy and O(M) work on impossible inputs. It is bounded and testable. The regression test includes negative pre-loop work controls and a positive producer-compatible zero-padding ceiling, avoiding a false rejection of configurations that the upstream actually supports.

**Separate transport and scientific schemas remain justified:** `ap117.psd/1` identifies the immutable derived measurement; `ap117.psd-delivery/1` conveys lifecycle/status. `createPsdProcessor` retains one current output, not a second FFT, PCM source reader, renderer scheduler or generic event broker. `take(...args)` refuses foreign receipts without dequeue; that does not authenticate a mistakenly wired *wrong valid handle* at construction. Do not grow a global registry to solve a future host-wiring test.

**No broader changes required.** The correct source and exact-handle host integration fixture remains future Issue #10; producer computational/GC capacity is Issue #11, not a new R1 defect. Numerical specifics, source-span/epoch metadata and accepted CP3-A amplitude semantics are unchanged. None of these deferrals may be falsely represented as already tested.

**Handoff to Axiom:** Update Flint's exact-head result from CONDITIONAL PASS to **PASS at R1**, without erasing the prior dissent/evidence. No authorial obligation remains in this remit. Changed PR head requires repinning and affected checks. Integrator/owner still decide overall design acceptance and merge.

## Revisit when

The PR head changes again, another independent review discovers a valid counterexample, the owner ratifies `ap117.psd/1`, the real host wires a PSD consumer (Issue #10), or measured performance evidence from Issue #11 warrants a distinct resource policy.

---
schema: 1
id: 2026-11-07-ap117-cp3a-gauge-numeric-review-r03
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-07
updated: 2026-11-07
sources: "User linked Auralprint 117 PR #5 for Gauge re-audit, 2026-11-07; exact Axiom PR head 23da63f8e8427d9b23c3f63794aeef6634fd466b on base 790e71f300ad24e01ec97c7ef42f4ca500ba1080; GitHub Actions run 42377361628; independent V8 exact-source FFT/stream probes; Python stdlib cmath golden-fixture calculation"
---

# Gauge → Axiom and owner — Auralprint 117 CP3-A numerical review

## Summary

**Goal/acceptance:** Independent numerical, source-clock, window-assembler and performance-evidence review of Auralprint 117 [PR #5](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5).

**Task outcome:** COMPLETE bounded review. **Numerical PASS; interface-integrity CONDITIONAL PASS** at head `23da63f8e8427d9b23c3f63794aeef6634fd466b`. No observed FFT arithmetic defect. Exact head remains a candidate pending owner acceptance, not a merged/released checkpoint.

**Authority:** Review only. No app edits, merges, CP3-B or other agents' memory writes performed. This technical record is saved on the authorized `KestrelGaming:agents/gauge-v1` branch.

## Evidence

### CI and previous hole

- PR base `main@790e71f300ad24e01ec97c7ef42f4ca500ba1080`. Exact [Actions run 42377361628](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42377361628) completed **success**: **66/66** Node tests, static build, official Nu built/rendered HTML validation, offline Chromium dual-view smoke and artifact. CI reports FFT1024 **median 0.042 ms, p95 0.138 ms**, Node runner only, no device frame-time SLA.
- The previous Gauge CI assurance finding `git diff --check` on a clean checkout was corrected in the accepted base: workflow fetches full Git history, evaluates `BASE_SHA` by GitHub PR/push event, and executes `git diff --check "$BASE_SHA" HEAD` (root fallback). This checks committed base-to-head changes rather than merely unstaged edits. Exact-head CI step succeeded. A deliberately malformed PR commit was not separately run through CI during this review.

### Independent numerical controls

- Fetched exact GitHub source `src/analysis/fft-amplitude.js` blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`, `src/analysis/spectrum-stream.js` blob `64c355315ea8c63bdadb7dd166404d0bd3b5a406`; executed source function bodies in isolated V8 after adapting ESM declaration/import wrappers. This was **not** a full local checkout or browser run.
- Independently implemented a slow direct DFT and checked **every one-sided bin** for six `(M,Nfft,window)` setups on multi-tone deterministic PCM: 16/16 rectangular and Hann, 32/128 rectangular and Hann, 1024/1024 Hann, 1024/2048 rectangular. Maximum absolute differences respectively: 2.01e-16, 1.44e-16, 5.05e-16, 7.80e-16, 5.87e-15, **7.29e-15**. Gain and ENBW metadata matched independent sums on these cases.
- Independently recomputed the PR's frozen 16-input Python fixture using stdlib `cmath` in a separate local Python process. Nine one-sided bins agreed to maximum ~**5.55e-17**. This is independent arithmetic evaluation of the declared equation, not a certified meter reference.
- Default 1024-point periodic Hann at 48 kHz: constant quarter-scale DC -> `0.2499999999999999`, quarter-scale Nyquist -> `0.2499999999999999`, coherent 37-bin sine 0.7 -> `0.6999999999999987`; coherent gain ~0.5; ENBW `70.3125 Hz` (1.5 FFT bins). The implementation correctly keeps interior two-sided factor separate from DC/Nyquist and normalizes with `sum(w)`, not PSD or `sum(w^2)`.
- Metamorphic stream partition checks compared 1-frame, mixed (13/7/3), and 480-frame chunks for (M/H/N/total) 32/8/32/113, 32/16/64/122, 1024/512/1024/2048, 16/1/64/60, 64/64/128/129, 64/2/64/133. Latest sample-span starts were respectively **80, 80, 1024, 44, 64, 68** on every partition; chosen bin values identical (difference 0).
- Adversarial windows: BigInt start `2^58` preserved exactly through endExclusive with CP2 channelId fallback; a revision change at frame 16 dropped old partial samples and produced `[16,48)` only under the new revision; discontinuity invalidated current; final 31-frame file yielded no padded spectral reading; final incomplete tail after one complete window preserved last complete span.

### New interface observation (conditional)

- `createSpectrumStream.accept` checks waveform class, sample spans, chronology and `quantity:"rms-amplitude"`, but **does not check** `publication.measurement.schema==="ap117.measurement/2"` or `validity==="valid"` before computing a `ready` spectrum.
- Exact-source adversarial reproduction: craft a `status:"ready"` publication with all otherwise valid envelope fields, but `measurement.schema="not-cp2"` and `measurement.validity="invalid"`. `accept()` produced **`status:"ready"`**, rather than reject. Other negative clock and epoch checks work.
- **Boundary and impact:** The actual app's trusted upstream `AnalysisPipeline` validates and owns its CP2 ready publication. Therefore this does **not** reproduce a production invalid observation, and the contract says `accept` consumes **already-validated** CP2 PCM. This is a partial ingress-guard / replaceable-adapter integrity gap, not an FFT math failure. Recommend the smallest explicit schema/validity guard and negative fixture if the module promises fail-closed independent validation; alternatively document that input validity is a precondition enforced only by upstream.
- Harbor independently approved PR #5 lifecycle scope at this exact head. Harbor also notes hardcoded `index.html` spectrum window/hop caption duplicates `CONFIG.spectrum`; matching at this revision, future mismatch risk, nonblocking.

### Limits

- No full independent local repository checkout/test suite, physical device tests, browser-level FFT latency measurement, recorder, calibration, noise PSD, BS.1770/EBU compliance or non-Chromium runs. Numeric comparisons validate the declared one-sided linear **peak-amplitude-bin** convention for selected signals; off-bin tallest-bin height is not exact sine amplitude and arbitrary noise is not PSD.
- Node 1024-point FFT p95 is a compute-only diagnostic. It is not an end-to-end observer delivery latency, GC budget or native realtime guarantee. At sample rate 192 kHz the default hop corresponds to ~2.667 ms source sample-time progression; acquisition pacing still requires device/browser profiling.
- No impact on CP2 PCM16 decoder or RMS arithmetic identified in reviewed changes. Full compatibility/diff guards were CI-tested, not independently rerun by Gauge.

| Check executed | Result | Evidence boundary |
| --- | --- | --- |
| GitHub exact-head CI | 66/66 + build/Nu/Chromium; 0.042/0.138 ms FFT report | Hosted runner logs |
| Exact-source radix2 versus separate direct DFT | Max abs delta ~7.29e-15 over selected six definitions | Isolated V8; deterministic multi-tone |
| Python stdlib 16-sample frozen fixture | Max abs delta 5.55e-17 | Local Python independent recompute |
| Partition/epoch/revision/BigInt/tail controls | All exercised expected spans and negative cases pass | Isolated V8; no browser |
| Forged invalid CP2 schema + validity | Improperly accepted as ready by stand-alone spectrum adapter | Host's CP2 pipeline cannot emit that invalid ready envelope |

## Next action

1. Axiom/owner: decide whether `createSpectrumStream.accept` is explicitly a trusted-CP2-only ingress or a defensive interchange validator; if the latter, add exact schema/validity assertion and a negative regression, without broadening scope or changing FFT math. Consider deferring the hardcoded spectrum caption note to a tiny presentation correction.
2. Flint: independently review copy/ownership and method-specific schema evolution before merge; Harbor has already reported a lifecycle PASS. Owner retains integration authority.
3. Preserve CP3-A distinction from CP3-B PSD and CP4 renderers. Device cost/GC/frame pacing should be separately profiled as design expands.

**Persistence:** This record is to be committed/indexed on Gauge's Kestrel memory branch. Confirm exact remote commit after write; app source and PR are unchanged unless a separate review comment is posted.

## Revisit when

PR #5 head changes, owner decides the spectral ingress precondition, peer reviews identify numerical counterexamples, CP3-B PSD begins, or actual device profiling establishes timing and allocation budgets. Recheck the repo state rather than treating this pinned assessment as current by default.

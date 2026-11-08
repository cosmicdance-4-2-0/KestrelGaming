---
schema: 1
id: 2026-11-07-ap117-cp3a-gauge-correction-recheck-r04
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-07
updated: 2026-11-07
sources: "User requested Gauge review of revised PR #5; GitHub comparison 23da63f8e8427d9b23c3f63794aeef6634fd466b..146a8c92ef54069f679b82f63b96608ae727415d; exact-head GitHub Actions 42437698669; source-executed V8 probes on fetched exact application modules; prior Gauge CP3-A R03"
---

# Gauge — Auralprint 117 CP3-A revised PR #5 re-review

## Summary

**Goal:** Verify Axiom corrected Gauge's CP3-A spectrum-adapter ingress defect without changing proven FFT arithmetic, valid CP2 interoperability, or sample-clock window semantics.

**Outcome:** **PASS** on Gauge's numerical / spectral-contract remit for exact `PR #5 head 146a8c92ef54069f679b82f63b96608ae727415d` versus previously reviewed `23da63f8e8427d9b23c3f63794aeef6634fd466b`. **No remaining blocker identified in this scope**. Prior conditional adapter finding closed. PR remains open and is not owner-accepted or merged by this review.

**Authority:** User requested an independent look at the revised PR. Review and Gauge-scoped memory preservation only; no application implementation, merge, CP3-B, deployment, or writes to other agents' branches.

**Target:** [ap_117_KESTREL PR #5](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5); accepted CP2.1 baseline `main@790e71f300ad24e01ec97c7ef42f4ca500ba1080`.

## Evidence

### Change boundary

GitHub compare endpoint establishes exactly **one new commit and four changed files** since previous head:
- `src/analysis/spectrum-stream.js`: enforces `measurement.schema === "ap117.measurement/2"`, `quantity === "rms-amplitude"`, `validity === "valid"`, accepted CP2 `unit`, `reference`, `method`, `calibration`, finite nonnegative numeric RMS, required nonempty measurement-level channel ID, plus existing chronology/waveform guards. Rejection calls `reset("invalid-spectral-input")` and throws, withdrawing previous spectrum.
- `tests/spectrum.test.js`: canonical accepted control and table-driven negative forged CP2 variants. An older handwritten chronology fixture now uses the actual CP2 fingerprint.
- `docs/CP3_FREQUENCY.md`: documents exported adapter's full fingerprint guard.
- `index.html`: replaces duplicated hardcoded periodic-Hann window/hop label with policy-neutral spectrum heading, maintaining `CONFIG.spectrum` as authority.

The FFT blob `src/analysis/fft-amplitude.js@ee35e0793aceb5eb9e3fc49d27f293a1719effc5` and accepted CP2 pipeline/decoder and FrameHost are unchanged by this commit. Scope excludes future PSD.

### Independently executed source controls

Fetched exact source modules from the pinned head and executed the original functions in an isolated V8 harness, adapting ESM import/export syntax only; this **did not perform a local full repo checkout**.

- Constructed a **real** `ap117.measurement/2` publication from the exact production `createSineSource` → `createAnalysisPipeline` (not merely a hand-written normalized label). `createSpectrumStream.accept` produced a valid owned spectrum. On 64 samples with M16/H8/N16, the last window was exactly `[48,64)`, channel `mono`.
- Submitted **18 individually malformed** CP2 measurement variants, each after successfully publishing a real valid observation: wrong or absent schema, wrong quantity, invalid validity, wrong or absent unit, wrong reference, wrong method/calibration, negative/NaN/+Infinity/string/absent RMS, blank/numeric/missing channel, and mismatched nested channel. **All 18 threw the expected validated-CP2 error and left `readCurrent().status === "unavailable"`, `measurement === null` and old stamp not current.** Explicit matching nested channel ID and optional-absent nested ID both remained accepted.
- After rejection and reset, a valid exact CP2 publication was accepted and produced a valid spectral window. No sticky rejection or retained stale observation.
- Executed production `createPcmBufferSource` → `createAnalysisPipeline` → `createSpectrumStream` on both channels and diverse frame lengths with **default M1024/H512**. 481-frame and 1023-frame files explicitly yielded `insufficient-complete-window`. 1024 frames → `[0,1024)`; 1535 → `[0,1024)`; 1536 → `[512,1536)`; 2048 → `[1024,2048)`; 2049 → `[1024,2048)`, independent of 480/257/2048-frame block partition where compared. Constant 0.25 input yielded ~0.25 DC. No invented padding; source tail can remain unrepresented spectrally without misreporting its span.
- Re-ran an independently implemented direct DFT on **every one-sided bin** for new deterministic multitone 32-sample, padded Nfft128 rectangular and periodic Hann controls. Maximum differences to exact production FFT output were **3.26e-16 and 3.80e-16**, respectively. FFT code is unchanged since prior R03 expanded suite where max absolute difference across six definitions was 7.29e-15.

### Exact-head CI

[GitHub Actions 42437698669](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42437698669) completed **success** for `146a8c92ef54069f679b82f63b96608ae727415d`. Inspected job steps and downloaded text logs:
- **67/67 Node tests, 0 failures**, static offline build, Nu built/rendered HTML checks, Chromium dual Canvas smoke, artifact upload and committed-diff whitespace check all green.
- FFT1024 Node-runner warm diagnostic **median 0.068 ms, p95 0.192 ms**. Older head's report (median 0.042 ms/p95 0.138 ms) is a different CI sample and cannot establish performance regression or improvement. No target-device end-to-end benchmark.

### Peer evidence

Flint's independent corrective-head re-review also reports architectural/interface PASS at the same exact `146a8c92`. Harbor's CP3-A lifecycle PASS was at the *old* `23da63f` head. The intervening four-file correction does not modify lifecycle implementation; Harbor remains the owner of independent lifecycle acceptance on the new revision if the project requires it.

## Next action

**Gauge's disposition: PASS at exact pinned head.** The previous warning that spectrum adapter accepted forged CP2 schema/validity, and the adjacent wrong-unit/reference/method/calibration fields identified by Flint, are closed by the narrow correction. No FFT arithmetic, sample-time, or accepted CP2 input regression was detected in exercised controls.

Owner may weigh this sign-off with Flint/Harbor evidence, require any head-specific recovery recheck if desired, and make a merge decision. **Gauge does not authorize merge, CP3-B PSD, or CP4 rendering by posting this review.** Do not create speculative new method contracts solely because the adapter does not recompute upstream RMS; it validates CP2's declared field fingerprint and the producer pipeline owns actual measurement calculation.

**Remaining evidence limits:** No full independent Node/Chromium checkout, Firefox/Safari, native device, physical calibration, browser BFCache navigation or full-system performance profiling. CI results are attributed to GitHub Actions; source-executed V8 controls are independent. Current `ap117.spectrum/1` is peak-amplitude-bin, not PSD or precise off-bin tone estimation.

## Revisit when

The PR head/base changes, a new source/adapter bypasses CP2 validation, FFT/window definitions change, or subsequent CP3-B/CP4 work requires a new measurement fingerprint, device profiling or richer observation-history semantics. Re-pin exact revisions before reusing this PASS.

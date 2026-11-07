---
schema: 1
id: 2026-11-07-ap117-gauge-postmerge-review-r02
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-07
updated: 2026-11-07
sources: "User's Gauge repository review request, 2026-11-07; ap_117_KESTREL main 65d5d9bec4a9f93fafc61e3bb15dcaa3b6740695; PR #3 head 56d4af9759071e9ab6c7973f203e7dcfda23a2f7; exact-head Actions runs 42362252679 and 42362951842; executed isolated V8 source-function counterexamples and separate local git whitespace probe"
---

# Gauge — Auralprint 117 CP2 post-merge independent assessment

## Summary

**Goal and acceptance criteria:** Thorough independent Gauge inspection of the current Auralprint 117 repository: source contracts, numerical accuracy, negative cases, PR/CI evidence, and realistic performance boundaries.

**Task outcome: COMPLETE (bounded review); PR #3 integration and CP3 implementation are not authorized or performed.**

**Authorized scope and boundaries:** Review only of the application; the user explicitly authorized persisting Gauge memory on `cosmicdance-4-2-0/KestrelGaming` branch `agents/gauge-v1`. The application remains private; this public memory record contains bounded technical evidence and pointers, not source code or audio recordings.

**Target repository:** `cosmicdance-4-2-0/ap_117_KESTREL`; merged `main@65d5d9bec4a9f93fafc61e3bb15dcaa3b6740695` ([CP2 PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2)); Flint maintenance [PR #3](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/3) open at `56d4af9759071e9ab6c7973f203e7dcfda23a2f7`. Kestrel memory branch head on loading `4025ec828e1ab9830169ee606de484c5f6081596`.

**Verdict:** CP2's current PCM16 decoding, finite-window RMS, sample-clock continuity and publication snapshot checks passed independently selected probes; no newly demonstrated audio arithmetic blocker. CI has one reproducible assurance defect (committed-whitespace gate). Flint's specific reentrant frame-loop fix passes its exact-head CI and an isolated reentrant control; stale canceled callback delivery remains an explicit *conditional* scheduler-contract risk. Performance and normative meter conformance are unmeasured.

## Evidence

### Confirmed repository/CI state

- CP1 and CP2 are merged; Checkpoint 3 is not integrated. Main and PR #3 both report CI success. The main [Actions run 42362252679](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42362252679) log shows **48/48 Node tests**; PR #3 [Actions run 42362951842](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42362951842) log shows **49/49**. Both pass static build, official Nu HTML checks, Chromium browser smoke, rendered HTML checks and artifact upload. CI results are attributed to GitHub, not a separate full checkout.
- Exact production texts of `src/audio/wav-pcm16.js`, `src/analysis/rms.js`, `src/analysis/pipeline.js` were fetched from merged main, and PR #3's `src/rendering/frame-host.js` from its exact head. The connector exposed their Git blob SHAs. Imported-module declarations were adapted for isolated V8 function execution; application runtime and full project tests were not executed locally.
- Independent V8 probes: all **65,536 signed PCM16 code values** decode exactly to their integer/32768 normalized values; whole-range RMS **0.5773502693240506** equals the independently accumulated BigInt integer-square reference at printed precision. Additional controls passed for contiguous + final/EOF, gap rejected before DSP, immutable measurement after injected analyzer mutation, invalid whole-file RMS placement rejected, and post-final read exception remaining faulted. The isolated PR #3 reentrant stop/start control retained exactly one queued frame.
- **G-117-01 — confirmed medium evidence defect:** `.github/workflows/ci.yml` calls `git diff --check` on a fresh checkout. In an isolated temporary Git repository containing a *committed* trailing-whitespace error, `git diff --check` returned zero whereas `git show --format= --check HEAD` returned 2 and reported the defect. Thus the current green check does not validate committed PR whitespace. Remedy: check the actual base-to-head committed diff in PR context and appropriate commit/range in push context. This is not a PCM correctness defect.
- **G-117-02 — conditional low/medium scheduler-contract gap:** The exact PR #3 frame-host function closes synchronous reentrant stop/start duplication. An additional adversarial harness stored a canceled callback, restarted the host, then *forcibly invoked* the stale callback despite cancellation; this yielded **two pending callbacks**. It does **not** prove that native browser requestAnimationFrame delivers canceled callbacks. Harbor should decide whether the interface promises successful cancellation or requires a generation guard, before alternate schedulers are introduced.
- No branch protection is enabled for current `main` according to the GitHub branch API. Formal owner checkpoint review remains a documented process, not a GitHub-enforced branch rule. This is a process observation, not a merge veto by itself.
- The `docs/CP2_FILE_PCM.md` opening paragraph is stale on main (says CP2 unmerged). PR #3 includes a correction to match merged main.

### Scope and limits

- The pipeline is **deliberately RMS-specific**: it validates `ap117.measurement/2`, `rms-amplitude`, `whole-block` and its exact method. CP3 FFT/PSD needs typed method-specific envelopes and independent spectral oracles; weakening RMS validation to accept arbitrary future measurements would be an error.
- Audio analysis uses nominal time pacing independent of rAF; fixed **480 frames** correspond to 60 ms at 8 kHz, 10 ms at 48 kHz, and 2.5 ms at 192 kHz. Finite-window RMS is not whole-file RMS, programme loudness, VU, PPM, LUFS, or device calibration.
- Decoding/copying occur on the main thread. A nearly 16 MiB mono PCM16 file implies approximately 16 MiB input + 32 MiB decoded samples + 32 MiB selected-source copy resident simultaneously (~80 MiB before other application/GC overhead). This is an analytical allocation estimate, **not** measured peak RSS. A near-limit stereo file implies ~64 MiB for input + decoded channels + selected-channel copy, before transient or previous-source coexistence. Renderer makes per-sample camera projection and Path2D calls on every present; CPU/GC/frame-time budgets were not measured.
- No local full repository checkout, all-browser tests, physical-device timing, calibrated instrument compliance, system-level memory profiling, or 16 MiB worst-case import responsiveness test was performed. The previous Gauge CP2 numeric audit was historically pinned to `e9ec16f`; this review's probes specifically exercised the later merged source.

| Check performed | Observed result | Environment / limit |
| --- | --- | --- |
| Github exact-head CI logs | main 48/48; PR #3 49/49; build/Nu/Chromium success | GitHub-hosted evidence, not Gauge's cloned rerun |
| Isolated exact-source V8 numeric/stream tests | All described control probes passed | Dynamic module wrapper; not a browser/full checkout |
| Forcibly delivered canceled callback | Two queued frames after stale invocation | Adversarial scheduler behavior, not proven native rAF |
| Temporary Git committed-whitespace control | `git diff --check` exit 0, `git show --check` exit 2 | Local scratch Git repository; demonstrates gate misconfiguration |

**Application changes:** None. **Memory persistence:** This handoff is intended to be saved and indexed on the authorized Gauge branch; inspect Git history for the actual resulting commit. The canonical Kestrel `python3 tools/validate_seed.py` cannot be run without a full checkout in this environment; metadata and index links are preflight-checked individually. Do not equate that manual check with the repository-wide validator.

## Next action

**Before merging PR #3:** Ask Harbor to examine stale callback/cancellation contract, lifecycle and recovery; then retain owner review/merge stop. PR #3's narrow fix is technically plausible and has exact-head CI evidence.

**CI follow-up:** Correct the ineffective committed-whitespace verification gate, write a failing committed-whitespace regression or demonstrate its base/head behavior, and confirm the gate on PR and push events.

**Before CP3:** Freeze measurement kinds, dB reference semantics, FFT coherent-gain normalization versus PSD power-normalization, window/hop sample clocks, treatment of DC/Nyquist, independent fixtures and target workload latency/memory budgets. Do not borrow PCM16/RMS pass evidence as spectral calibration.

## Revisit when

PR #3 is reviewed/merged, CI gate changes, the scheduler contract changes, CP3 adds a new measurement type, or a genuine target-host performance experiment is completed. Always recheck live heads before treating this record as current.

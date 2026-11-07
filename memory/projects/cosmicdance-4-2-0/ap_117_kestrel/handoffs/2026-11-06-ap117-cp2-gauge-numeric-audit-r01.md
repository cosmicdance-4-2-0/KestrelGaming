---
schema: 1
id: 2026-11-06-ap117-cp2-gauge-numeric-audit-r01
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-06
updated: 2026-11-06
sources: "User's 2026-11-06 Gauge audit request; https://github.com/cosmicdance-4-2-0/ap_117_KESTREL at e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb; GitHub Actions 42329197868; local Node 22.16.0 and Python 3.13.5 isolated independent numeric probes"
---

# Gauge to Axiom — CP2 numerical accuracy review

## Summary

**Goal and acceptance:** Independently assess numerical accuracy of Auralprint 117 CP2 file PCM and synthetic SignalScope. Provide Axiom a falsifiable review handoff without changing the application or merging work.

**Task outcome: COMPLETE (bounded numerical audit; integration acceptance is separate).**

**Verdict: PASS on CP2's defined PCM16 decoding and per-block RMS arithmetic for exercised inputs; CONDITIONAL on independent source-contract enforcement for future interchangeable adapters. No demonstrated arithmetic blocker.** Realtime performance, normative instrument calibration, all-browser behavior and source/device clocks are not certified.

**Reviewed repository:** `https://github.com/cosmicdance-4-2-0/ap_117_KESTREL` (GitHub reports PRIVATE), branch `foundation/axiom-file-pcm-cp2`, exact commit `e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb`, tree `b55022c56005e9aebdb2f1628e13f128e2d3f2bc`. Source at inspection was unchanged when this handoff was written. The [CP2 specification](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/docs/CP2_FILE_PCM.md), [app contract](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/AGENTS.md), and [CP2 PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2) govern scope. No application code edits or project branch writes were made.

## Evidence

### 1. Exact code and independently generated numerical evidence

Locally recreated **five source modules**, byte-for-byte, verified their Git blob SHA-1 IDs against the target commit before running probes: `src/analysis/rms.js` = `b72b26648aaba5eecd1a5632bb5143454da22f36`; `src/analysis/pipeline.js` = `4bbdfd4e3618861a96110acef49d4d6aa8b0e609`; `src/audio/wav-pcm16.js` = `1989a0eff066a2e3de8d148bf358a3ee1f8abf5f`; `src/audio/pcm-buffer-source.js` = `7fd18ecb6a579dcc7f1fc70c64974602f0c9c0fb`; `src/audio/synthetic-sine.js` = `77f48d03488b888236834530e9910b04780b6af3`. This establishes the executed implementation bytes, but **not a full checkout or full npm test**.

**Independent exhaustive signed-PCM16 conversion:** Python standard-library `wave`/`struct` wrote all integer codes -32768..32767 in a 65,536-frame mono WAVE. Independently generated the expected little-endian Float32 byte stream from each exact `q/32768` rational. Node's [decoder](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/src/audio/wav-pcm16.js) produced an **identical SHA-256 digest** `13a9d0798ab91787f5c75d6776be6dd19716ba7fb310de2d9dbeac3ba314acc7`, confirming all decoded Float32 bytes. Whole-vector RMS = `0.5773502693240506`; 100-digit Python Decimal, integer-square oracle = `0.5773502693240505992826551320460648033578757075855...`.

**Nine separate analytical PCM16 WAV fixtures:** digital zero, positive and negative one-LSB DC, single one-LSB impulse in 480 frames, -32768 impulse in 480 frames, alternating signed extremes, 481-frame asymmetric tail, 8,192-frame sparse impulse and 65,000-frame deterministically generated codes. Float64 RMS results from the exact [analyzer](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/src/analysis/rms.js) differed from 100-digit Decimal exact-sum/square-root expectations by **at most 0.469 ULP** in this set, with several exact matches. Example one-LSB 480-frame impulse RMS `0.0000013929304949573926`; one-LSB 8192-frame impulse RMS `3.371747880871523e-7`. The weighted recombination of per-block squared RMS for 480-frame partitions matched the whole-vector calculation for these fixtures (within reported floating precision).

**Numeric rationale, scoped to PCM16:** signed integer division by 32768 is an exact binary rational representable in Float32; products of supported Float32 samples are representable in Float64, and the compensated nonnegative sum greatly reduces accumulation loss. The 16 MiB file limit bounds numerical magnitude and sample counts; this is not an instrument calibration claim. No clipping or silent zero padding was observed in exercised inputs.

### 2. Adversarial publication contract counterexamples — reproducible, MEDIUM extension risk

The [pipeline](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/src/analysis/pipeline.js) validates each published block and analyzer metadata independently, but **does not check cross-block sample-clock continuity or terminal state**. Using a minimal test source returning four samples of 0.25 at each step, the *exact module* produced:

| Sequence within one stream | First result | Next result | Missing validation |
| --- | --- | --- | --- |
| [0,4), then [100,104), same epoch | ready | **ready** | 96-frame gap not marked invalid/discontinuous |
| [0,4), then [2,6), same epoch | ready | **ready** | 2-frame overlap not rejected |
| [0,4) final=true, then [4,8) final=false | ready | **ready** | data can follow a declared terminal block |
| [0,4) final=false, then null EOF | ready | ended | unexpected EOF lacks explicit terminal declaration |

A new epoch without an explicit `replaceSource` or reset is also accepted, although each individual result retains its epoch identifier. The two in-repository CP2 sources create consecutive blocks and handle their own final state; **this is not proof that a valid CP2 WAV is mismeasured**. It is a future adapter contract vulnerability that should be addressed by an explicitly chosen owner of continuity (source, pipeline boundary validator, or observable typed discontinuity channel). A consumer must never infer contiguous valid audio solely from a series of `ready` statuses.

**Requested Axiom decision:** Is the source a trusted proof producer, or must the interchange/publishing boundary itself enforce monotonically contiguous `[start,end)` intervals and final/EOF state? Add focused negative fixtures before CP3/streaming adapters. Do not silently fill gaps with zeros or collapse separate epochs.

### 3. Signal/time semantics and other bounded findings

- At the **default 48 kHz, 480 samples = 10 ms**, the computed RMS is correctly a block quantity, **not** necessarily a stable programme level. For 20 Hz, 0.5-peak synthetic sine, ten successive blocks had RMS range **0.174347 to 0.449089**, while their energy-weighted combined 100 ms RMS was ~0.353553. This is expected phase-dependent finite-window mathematics, **not an arithmetic bug**. The [UI](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/index.html) correctly labels **Block RMS amplitude**. Do not rebrand it VU, LUFS, dBFS, or a sample-rate-comparable programme loudness meter. Fixed **frame** count means file-window duration changes with file sample rate (480 frames = 60 ms at 8 kHz and 2.5 ms at 192 kHz). Select fixed temporal windows explicitly if later user goals demand comparisons across rates.
- 1 kHz, 0.5 peak synthetic source at 48 kHz: against an independent mathematically periodic Float32 sine calculated by sample number mod 48, over 4,800,000 frames (~100 s), max absolute sample discrepancy **7.450580596923828e-9**. Small gradual phase-recurrence rounding; **LOW, not CP2 acceptance blocker**. A long-duration oracle/FFT calibration fixture should use analytically indexed phase or quantify this drift rather than presume perfect indefinite periodicity.
- [main.js](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/src/main.js) displays RMS to **six decimal places**. Under the current bounded file/480-frame pathway, the smallest nonzero single-LSB one-frame-in-480 RMS is ~1.39e-6 and remains distinguishable. The display rounding still must not be promoted into full internal measurement precision or reused as a tolerance for future higher-resolution formats.
- The [CP2 document](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/docs/CP2_FILE_PCM.md) says CP1 PR #1 was still open at pickup; GitHub now reports that PR merged. This is historical context, not an active restriction. Recheck PR/branch state when integrating.

### 4. Executed checks and explicit evidence limits

| Check | Observed | Scope/limitations |
| --- | --- | --- |
| `git hash-object` on five recreated JS modules | All five match target Git blob SHAs | Independently confirms exact executed module contents; not a full checkout |
| `python3` standard-library WAVE + Float32 exhaustive SHA-256 vs Node decoder | All **65,536** PCM16 codes match byte-for-byte | Local test, no device/codec interoperability outside WAV subset |
| Nine WAV fixtures vs 100-digit Decimal integer-square oracle | Max observed deviation **0.469 ULP** | Local Node 22.16.0 / Python 3.13.5, selected fixtures; not all possible arrays |
| Full vs 480-frame weighted block RMS composition | Agrees for tested signals | Demonstrates block accounting; not a substitute for a specified programme-level algorithm |
| Exact pipeline mocked-source negative probes | Gaps, overlaps, post-final blocks and unannounced EOF accepted | Interface/contract weakness, not built-in source reproduction |
| Synthetic 20 Hz/1 kHz finite-window and 100-second phase probes | Values described above | Mathematical signal interpretation, not realtime latency or hearing tests |
| [GitHub Actions run 42329197868](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42329197868) on `e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb` | **SUCCESS**, 34 tests reported; build, official HTML checks, Chromium smoke, diff checks | **Existing CI evidence, inspected but not rerun by Gauge** |

**Explicitly not run:** target repository's entire `npm test` from a clone, browser host tests from this local environment, device calibration, hardware timing/CPU utilization, 16 MiB worst-case responsiveness, standardized meter compliance, other browser implementations. Private repository was available through the GitHub connector, not to this environment's direct Git network access.

**Application changes:** None. **Agent memory changes:** This project profile/index and handoff only, committed on `cosmicdance-4-2-0/KestrelGaming` branch `agents/gauge-v1`. The external memory home is publicly readable: this handoff stores only bounded technical conclusions and pointers, not project source code or user audio.

## Next action

**Priority 1 — Axiom:** Decide/explicitly document which interface owns cross-block continuity and final/EOF validation. If the pipeline is the boundary, add negative tests for the four demonstrated mismatches and ensure failed blocks never leave stale `ready` publications. If responsibility stays with each source, make the trust boundary explicit and test every adapter against it. Preserve schema/version discipline.

**Priority 2 — Axiom/Gauge:** Consider incorporating independently generated PCM16 full-range vector/digest and sparse/tail RMS into a frozen acceptance fixture bank. Retain independent golden provenance; do not treat a reimplementation of the same algorithm as an independent oracle.

**Priority 3 — future measurement tasks:** Lock analysis window-duration semantics and numerical error budgets per unit/reference before comparing meter modes or adding FFT/PSD. Explicitly benchmark host CPU/latency and callback loss under realistic workloads before claiming performance.

**Suggested acceptance:** Accept this CP2 **numeric slice conditionally** for its current trusted sources; keep the stream-boundary validation as a documented pre-CP3/adapter review issue. No Axiom implementation, PR review submission, code change or owner acceptance has been performed on Gauge's behalf.

## Revisit when

Target head moves, a new source/decoder/clock is added, DSP units/window semantics change, independent numeric fixtures are integrated, or Axiom resolves continuity ownership. Refresh evidence at the exact revision before treating prior tests as current.

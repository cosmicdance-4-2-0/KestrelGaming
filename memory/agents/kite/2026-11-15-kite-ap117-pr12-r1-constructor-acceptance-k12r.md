---
schema: 1
id: 2026-11-15-kite-ap117-pr12-r1-constructor-acceptance-k12r
kind: decision
scope: agent:kite
status: draft
evidence: inferred
author: kite-session
created: 2026-11-15
updated: 2026-11-15
sources: "AP117 PR #12 R1 @2acfeb9daf3b5714424455afc64bcffd237c23d7, prior Kite first-pass @0880fc8df9182cce9ed2c645e324a2d291375281, accepted main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f, CI run 43824257458; Kite home agents/kite-v1@4477d79c1ebbd3329308117a1d1f8ceb63e0625b."
---

# Kite — AP117-003 PR #12 R1 re-review: FFT ceiling correction accepted

**Mode:** Independent **review only**. No application source, tests, contract ratification or merge changed by Kite. Exact current candidate PR #12 `codex/ap117-003-psd@2acfeb9daf3b5714424455afc64bcffd237c23d7` against unchanged accepted `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`, verified at review time. R1 is one additional commit, parent/previous assessed head `0880fc8df9182cce9ed2c645e324a2d291375281`.

**Original independent review preserved unchanged:** [2026-11-15-kite-ap117-pr12-psd-consumer-performance-review-k12q.md](2026-11-15-kite-ap117-pr12-psd-consumer-performance-review-k12q.md), source-pinned at earlier head. This R1 addendum **replaces only the earlier conditional acceptance finding for the NEW head**, not its historical evidence, alternatives or Issue #11 uncertainty. Kite character contract and memory home `agents/kite-v1@4477d79c1ebbd3329308117a1d1f8ceb63e0625b` already loaded; no other agent's new PR #12 response used for this comparison.

## Summary

**Verdict: ACCEPT R1 for Kite's constructor admission and performance/alternatives remit; earlier requested correction is RESOLVED.** No remaining blocker is identified within the exact R1 three-file delta. This is a reviewed specialist acceptance, **not** a holistic PR merge authorization or adoption of proposed `ap117.psd/1` or `ap117.psd-delivery/1` schemas.

R1 updates `windowDescriptor()` in the standalone PSD processor to match the **same configured** FFT limit used by the accepted upstream producer, before doing any O(M) window-weight computation. It avoids a separate hardcoded maximum and adds both invalid-configuration early-rejection and positive maximum-FFT padding tests. Documentation also accurately limits claims about host-side wrong-native-handle wiring and arbitrary wrappers. The preexisting general work/GC concerns remain owned by Issue #11, not this PR.

## Exact reviewed diff and observations

Independent GitHub compare `0880fc8d...2acfeb9d` shows exactly **one commit** `2acfeb9daf3b5714424455afc64bcffd237c23d7`, **three paths**:
1. `src/analysis/psd-processor.js` blob `1f3937cbdaf77514c435da30879975e6a13f16ef` (4 additions, 2 deletions). At lines 18–23, `windowDescriptor({ windowFrames:m, hopFrames:h, fftFrames:n, window, maxFftFrames })` now rejects unsafe/omitted `maxFftFrames`, `maxFftFrames < 4`, or `n > maxFftFrames`, in addition to prior existing M/H/N/power-of-two/window checks. Only after all these guards does it compute periodic-Hann/rectangular weights in the O(M) loop. The old `n>2**30` special ceiling is gone. The consumer still accepts exact provider config as a value and does not import global `CONFIG`.
2. `tests/psd-boundary.test.js` blob `f943670222dad3c11ccc774b99391bdfe820746e` (35 lines added). New test `PSD constructor enforces the producer FFT ceiling before generating window weights` checks missing/invalid/beyond-budget limits, mocks `Math.cos` to show no Hann weight work after rejection, and builds a valid M=8/N=16384 padded provider+consumer with the same accepted maxFftFrames=16384. Its final `take()` returns empty and `readCurrent()` remains unavailable because no PCM was sent: this is intentionally an admission control, **not a performance benchmark or new FFT operation**.
3. `docs/AP117_003_PSD_CONSUMER.md` blob `b2c779bf57f2ba973892ec5930cfdbbf4a4bb090` (16 additions, 7 deletions). It states both PSD and PSD-delivery schemas remain proposed, records the new producer-supplied safe-integer ceiling and distinguishes receipt-argument rejection from actual host capability binding. Correct host wiring remains future Issue #10 integration, not a claim of third-party code authentication.

**No changes in R1** to `src/analysis/fft-amplitude.js`, `spectrum-stream.js`, `spectrum-delivery.js`, `CONFIG`, actual PSD derivation, lifecycle state machine, PCM, Canvas, host, or rest of the new test suite. Source compare returned exactly those three modifications. The previous mathematical evidence and full first-pass review stand unless a later code change contradicts them.

## Recheck of the original counterexample

**Prior defect at `0880fc8d`:** PSD accepted an independently chosen `n <= 2**30` while the producer checked `n <= maxFftFrames`, where the accepted app CONFIG supplies `maxFftFrames=16384`. A trusted host misconfiguration could call the PSD constructor with a giant M/N and incur O(M) Hann weight work before failing to match any valid producer, so our specialist first pass requested provider-consistent admission prior to the loop.

**R1 correction at `2acfeb9d`:** The same `spectrum` object passed by the caller now carries `maxFftFrames` to the PSD constructor; accepted use supplies the matching value to both producer and processor. Invalid oversized N is rejected before the loop. The native producer already requires the same safe-integer limit; a mismatch between supplied host descriptor and actual native producer remains a trusted-host-wiring mistake, not a promise the constructor can authenticate another instance's private configuration.

**Positive/negative controls:** `fftFrames=32768, maxFftFrames=16384` must fail; missing, NaN, Infinity, negative/noninteger/unsafe `maxFftFrames` must fail; padded `windowFrames=8, fftFrames=16384, maxFftFrames=16384` must construct. The added test covers these using the *actual* source class and asserts zero Hann weight computation in rejected cases. It does not execute the earlier 2**30 extreme (appropriately) and does not need to for this deterministic guard.

**Residual limitation (not a newly introduced PR blocker):** `maxFftFrames` is still caller-supplied configuration; there is no cryptographic or opaque producer-bound authentication of configuration identity. The module is intentionally trusted built-in and Issue #10 owns host composition. It is not correct to claim arbitrary same-realm wrappers, wrong native handles or user-supplied values are authenticated. Broader configured FFT work/GC under large M, tiny H or multiple providers belongs to Issue #11; this guard only removes an *inconsistency* between constructor and provider limits.

## Verification evidence and limits

**Source-verified:** current PR head, base and R1 commit metadata; GitHub compare patch and final three changed source files; accepted upstream FFT producer's `maxFftFrames` validation; earlier exact independent report. The new test explicitly confirms the constructor refuses rejected values before any `Math.cos` Hann work.

**External build evidence:** GitHub Actions run `43824257458` completed with `success` for exact R1 head. The implementer reports `node --test tests/psd-boundary.test.js` 10 passing, `node --test tests/psd-*.test.js` 27 passing, `npm run verify` 120 passing + static build, HTML validation and Chromium smoke. These numbers are implementer-reported, not counted from independently running Node in Kite's local environment.

**Not independently rerun:** a checkout of the PR, its new module or full Node suite, Chromium, live device, heap/GC, fully primed maximum FFT/hop1 workload. This is a code review backed by source diff and CI outcome, *not* empirical certification of operating latency. No new requirement to redo Gauge's mathematical suite or introduce an unrelated compositor/FFT change was manufactured from this bounded R1.

## Decision and remaining explicit gates

**Specialist decision:** `COMMENTED — ACCEPT R1 within Kite remit`, not formal owner-approved schema adoption or merge. Earlier **CONDITIONAL PASS at 0880fc8d** is closed with this fix for **2acfeb9d**.

**Continue to preserve:**
- CP2 validated single acquisition, `ap117.measurement/2` and sample-clock/epoch/BigInt semantics;
- CP3-A peak amplitude `ap117.spectrum/1`, exact FFT arithmetic and bounded complete-spectrum delivery;
- PR #12's own matching-window `ap117.psd/1` draft, no extra FFT, distinct periodogram quantity/units and truthful weighted Parseval;
- subscriber continuity, historical valid backlog, clean EOF drain, explicit resync and no source/renderer changes;
- Issue #10 host actual-handle/wrong native handle integration gate;
- Issue #11 real work/GC and multiple-provider operating-envelope gate.

**No new code changes recommended within the exact R1 delta.** If the PR head changes, re-evaluate. The owner retains merge/release/contract authority.

## Evidence

Observed exact source pin and GitHub CI result as above; inferred acceptance from a straightforward same-limit constructor guard and targeted regression controls. No independently executed full application tests or performance measurement. Shared GitHub account attribution reflects the selected Kite role, not authenticated autonomous identity.

## Revisit when

Axiom requests post-correction integration review, the PR head moves, an independent runtime check contradicts the zero-weight-work or valid-padding control, a consumer host attempts to wire a wrong subscription handle, or Issue #11 specifies actual supported performance settings.

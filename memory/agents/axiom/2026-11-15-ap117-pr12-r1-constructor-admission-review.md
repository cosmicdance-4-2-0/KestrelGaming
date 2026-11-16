---
schema: 1
id: 2026-11-15-ap117-pr12-r1-constructor-admission-review
kind: review
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr12-r1-review
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint PR #12 second commit 2acfeb9daf3b5714424455afc64bcffd237c23d7 parent 0880fc8df9182cce9ed2c645e324a2d291375281; accepted main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; CI 43824257458 job 133154208864; Axiom PR comment 6910307463."
---

# Auralprint 117 — PR #12 constructor admission R1 corrected, focused re-review pending

## Exact state
Owner confirmed Codex completed R1 on existing draft PR #12. Verified connected GitHub PR metadata: **open, draft, unmerged**; new `head=2acfeb9daf3b5714424455afc64bcffd237c23d7`, parent `0880fc8df9182cce9ed2c645e324a2d291375281`; base/main `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f` unchanged.

**R1 diff observed:** commit 2acfeb9, 3 files, 55 lines added and 9 deleted. Modified only `src/analysis/psd-processor.js`, `tests/psd-boundary.test.js`, `docs/AP117_003_PSD_CONSUMER.md`. The `windowDescriptor` validator now accepts passed `maxFftFrames`, validates safe integer ≥4 and `fftFrames<=maxFftFrames` before the Hann weight loop, and removes the ungrounded `2 ** 30` ceiling. Same accepted upstream `fft-amplitude.js` rule. New test negative M8/H4/Nfft32768/max16384, malformed/absent limit and `Math.cos` not called on rejection; positive legal M8/H4/Nfft16384/max16384 no signal FFT performed. Documentation now clearly distinguishes rejecting `take(receiptA)` from guaranteeing a real host bound the intended native subscription; Issue #10's *future host wiring* remains open.

**CI:** [exact-head GitHub Actions run 43824257458](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43824257458) completed success. Read verify job 133154208864 log: **120/120 tests, 0 failure, 0 skip**; static build, HTML validation, Chromium smoke and whitespace gates all successful. CI executed, **not Axiom's independent full local npm/browser run**. Existing browser test does not exercise a production PSD GUI because consumer remains headless. No R1 changes to PCM/CP2, FFT producer, spectral window numerical normalization, PSD density formula, sample lineage, subscription queue, status/lifecycle, app host or visuals.

## Project-lead disposition

**R1 source-verified, conditional engineering GO; focused independent gate OPEN.** Source-level defect called out by Flint/Kite appears corrected without unrelated changes. Axiom made **no application edits, merge, deployment or new PR**. Previous six specialist reports are pinned to the *old* `0880fc8...` and must not be silently relabeled as reviews of `2acfeb9...`.

Posted [Axiom PR #12 new-head targeted review request](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6910307463):
- **Flint** reruns producer-matched maxFftFrames admission/source tests, actual boundary and no weighting on invalid config; focus API/minimality.
- **Kite** independently probes limit and computational admission without executing giant workloads; Issue #11 FFT/GC/device operating envelope is separate and stays open.
- **Gauge** checks non-change of `P[k]=A[k]^2/(c[k]*ENBW)` one-sided factors/Parseval and BigInt chronology; optional small numerical re-control, not a wholesale rerun without math change.
- **Harbor, Latch, Mothlight** initial unchanged-path conclusions remain valuable at original head; targeted revisits only if new counterexamples appear.
All agents retain own identity/memory and attribution, share GitHub account; owner relays to actual sessions. No automatic multi-agent execution.

## Merge/contract boundary

Await focused **exact-head** Flint/Kite evidence (and Gauge numerical guard or Axiom verification) before recommending owner acceptance. Do not implement new host/B2 UI or claim Issue #10 whole host binding is solved by reject-arguments API; producer-issued actual handle must be wired exclusively when real host integration exists. Candidate `ap117.psd/1` and `ap117.psd-delivery/1` remain not owner-adopted until decision. No new Codex code correction warranted based on current R1 source inspection. If PR head moves, repin.

## Revisit when
Flint/Kite/Gauge return new-head focused reviews; CI fails; new contradiction against accepted FFT limits; owner merges; PSD host wiring or multi-provider consumption is requested.

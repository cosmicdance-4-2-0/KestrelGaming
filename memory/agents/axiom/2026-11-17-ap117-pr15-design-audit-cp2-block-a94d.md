---
schema: 1
id: 2026-11-17-ap117-pr15-design-audit-cp2-block-a94d
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR15 head 0f451a6b7bc887e5fccb77c6ffa309380e488f1f base/main 4bc1245e9fb979a49bdc2b56c57c8787ef667155, docs/AP117_005A_BENCHMARK_PLAN.md, src/analysis/pipeline.js and FFT/PSD host implementation, CI 44057992838 job 133952184902, Axiom PR15 comment 6945134158."
---

# AP117-005A — PR #15 Axiom independent design audit

## Summary

**CONDITIONAL PASS for the benchmark design; one P2 source-contract documentation correction required; HOLD AP117-005B and merge.** The user presented [PR #15](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/15) for review. Codex delivered one 355-line design document on a draft PR, exact head `0f451a6b7bc887e5fccb77c6ffa309380e488f1f`, accepted base/main `4bc1245e9fb979a49bdc2b56c57c8787ef667155`. No production/test/CONFIG changes. Axiom published a detailed attributable [review comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/15#issuecomment-6945134158). Kite's independent second review has not yet been reported.

## Evidence

**P2 source mismatch:** Design section 3 states “A short nonfinal M-1 or M-H packet is invalid ingress.” Actual `src/analysis/pipeline.js` validates against **configured CP2 `blockFrames=B`**: `0 < samples.length <= B`, and a nonfinal block must be exactly `B` long. The FFT's `M` window and `H` hop do not determine CP2 block admissibility. Example `M=8,H=4,B=4`: four nonfinal full B4 packets and a final full B4 packet legally produce four FFT windows `[0,8),[4,12),[8,16),[12,20)` under the plan's own section-8 partition oracle. The real app `B480,M1024,H512` likewise uses legal nonfinal B480, shorter than FFT window. Request one-sentence correction and retain legal cross-block fully primed cases. No reason to change actual code.

Independent source review supports design's workload matrix: normal F/S 400*480 has 374 completions; default 3*8192 has 15/16/16; C4 overrun and C31/C30 backlog; M/Nfft=16384,H512 0/1/16 and H1 0/1/8192; binCount=8193 and two capacity-16 subscribers would overreserve 262176 > 262144. Absolute 939,524,096 butterfly estimate and scratch/allocation accounting **not measured runtime results**. The design correctly separates Node stages, GC/heap observer effects, actual-browser tracing, file vs live arrival-model limitations, guarded pathological run and explicit source/PSD/FFT correctness checks.

**Additional nonblocking recommendations:** at implementation time combine butterfly work guard with FFT completion/allocation-count guard; disclose whether actual-app stage probes use instrumented test server/modules versus unchanged distributable and compare an uninstrumented control. Do not silently promote any suggested guard limits as universal device policy.

[CI 44057992838](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44057992838), job 133952184902, successful, actual log shows **131/131 Node tests, zero failed/skipped**, build/official HTML/Chromium offline smoke and whitespace; executed by GitHub CI, not by Axiom. No AP117-005A performance measurement or 005B harness was run.

## Revisit when

When Codex corrects the source-contract sentence in the **same draft PR** at a new exact head, fetch changed document/diff, check arithmetic/CI and respond with final Axiom GO/HOLD. Await Kite's independent benchmark-design review before owner-authorized 005B. Keep Issue #11 open and do not merge the design without owner direction. If base/head changes materially, re-evaluate relevant behavior.

---
schema: 1
id: 2026-11-17-kite-ap117-pr15-benchmark-design-review-k15d
kind: decision
scope: agent:kite
status: draft
evidence: observed
author: kite-session
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR #15 at fb911dba06bab4d637e3793f3ec8a56607e3fa7a vs accepted main 4bc1245e9fb979a49bdc2b56c57c8787ef667155; source file docs/AP117_005A_BENCHMARK_PLAN.md blob b010501a53eda6a5d2bb792b2906b76785602067; Issue #11 assignment 6943960245; Kite V8 source-based controls; CI 44064264503; agents/kite-v1@79abcb785db5ba24507dffbb8dff44ae59a9a295."
---

# Kite — AP117-005A PR #15 independent benchmark-design critique

**Target:** https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/15. Exact PR head `fb911dba06bab4d637e3793f3ec8a56607e3fa7a`, accepted base `main@4bc1245e9fb979a49bdc2b56c57c8787ef667155`, verified both live refs. Candidate remains **open/draft/unmerged** at review time, with two commits / one new document `docs/AP117_005A_BENCHMARK_PLAN.md` (+378, no deletion); no app, CONFIG, scripts, test or dependency change. GitHub Actions run `44064264503` reports completed/success on exact head.

**Task:** Owner/Axiom review request from [Issue #11 AP117-005A handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11#issuecomment-6943960245) and the PR discussion. Scope is **design and falsification only**: approve/reject the proposed instrumented experiment, not implement AP117-005B, run a performance benchmark, alter FFT/PSD/CP2, release or merge. Axiom's earlier review `6945134158` requested a source-contract correction and its updated `6945373923` individually accepted R1. **These Axiom reviews were necessarily read as PR-assignment context before Kite's investigation; this was not a blind review.** Kite's own checks and opinion do not treat Axiom's vote as a correctness oracle.

**Kite identity:** Loaded `agents/kite-v1@79abcb785db5ba24507dffbb8dff44ae59a9a295` branch-local `AGENTS.md`, `KESTREL.md`, `agents/kite/AGENT.md`, `PROFILE.json`, `memory/agents/kite/INDEX.md`, `kestrel/MEMORY_PROTOCOL.md`, `STATE_PROTOCOL.md`, `VERIFICATION.md`, `PERMISSIONS.md`, `CONTRIBUTING.md`, and own PR #9/#12/#13 review continuity. Source of truth remains application `AGENTS.md` at exact PR head. Memory branch is public, no sensitive samples.

## Summary

**Verdict: PASS for AP117-005A DESIGN at exact head; one NONBLOCKING AP117-005B oracle-resource clarification requested.** No demonstrated error in the revised workload matrix, CP2 rule, source-status accounting or preflight arithmetic. The small one-document proposal is an appropriate decision gate before optimizing. It distinguishes accept-only diagnostic evidence, actual source+CP2+FFT+native delivery+PSD service, GC/retention, browser scheduling, and *modeled* live arrival separately. It preserves current accepted contracts and does not claim any performance number from arithmetic.

The revised plan correctly states CP2 accepts a full B-sized **nonfinal** PCM packet even when B<M or B<=M-H. Only a short actual length L<B must be final. Separate FFT windows are assembled from contiguous accepted PCM. The sole requested high-risk stress, fully primed N=M=16384/H1/B8192, is **opt-in only** behind independently enforced child work/memory/time guards. No GPU/Worker/WASM, DSP refactor, new source, CONFIG narrowing or production architectural commitment is implied.

**Original independent point not raised in Axiom's verdict:** Section 8's proposed direct complex DFT oracle is quadratic if implemented across *all* bins for every large FFT in the workload matrix. The current `Section 7` preflight butterfly count applies to radix-2 production transforms, **not** a naive DFT correctness oracle. If AP117-005B applies all-bin DFT to the retainable 16384-FFT ×17-window case, even the *one-sided* check executes **2,281,979,904 complex terms** while the production FFT does only **1,949,696 butterflies**. A two-sided DFT needs **4,563,402,752 terms**. This could swamp the measurement and violate the intended resource containment without ever crossing an FFT-butterfly preflight limit. **Implementation clarification:** require full direct DFT only on bounded small-N scientific fixtures; for large N use a deterministic bounded bin sample plus independent time-domain Parseval and fixed lineage/ownership checks, in an isolated **untimed and separately guarded correctness phase**. A source-derived DFT work estimate belongs in preflight when those checks run. This is an implementation trap/clarification, not a defect proven in the one-document design, and does not need new code in 005A.

## Exact source and plan evidence

Read the full 378-line plan `docs/AP117_005A_BENCHMARK_PLAN.md` blob `b010501a53eda6a5d2bb792b2906b76785602067`, at head `fb911dba06bab4d637e3793f3ec8a56607e3fa7a`. Relevant line sections: 25–68 matched variants/sources; 70–132 workload table, completed/queued/forfeited semantics, corrected CP2 rule and pathological admission; 134–154 nested stage timing; 155–182 allocation/GC; 183–225 browser input/live-source separation; 226–274 warmup, preflight and child containment; 275–295 scientific negative oracles; 297–343 minimal 005B diff and gates; 345–378 source/verification scope.

Independently read accepted application `src/analysis/pipeline.js` blob `25f396217a54501d3ea3565bac1b8e2eb0c46b0f` (shape validation lines 26–35, ready/final/EOF/invalid transitions 104–192), `src/analysis/spectrum-stream.js` blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc` (complete count lines 145–148), `spectrum-delivery.js` blob `ef19cd748de41226ab0cd8375949e278f7aeb76f` (bounded queue/overrun), `fft-amplitude.js` blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5` (scratch and output arrays), `pcm-buffer-source.js` blob `7fd18ecb6a579dcc7f1fc70c64974602f0c9c0fb` (actual slicing/EOF), `synthetic-sine.js` blob `77f48d03488b888236834530e9910b04780b6af3`, `psd-session.js` blob `005e8f77fd7d71e5be51780a6cdbefa525bb2377`, `src/main.js` including its corrected same-value slider guard, `src/config.js`, original `scripts/measure-spectrum-delivery.mjs` blob `f0c6f6d0d8da9db32b4215793902cb712bdc2849`, and PR's authoritative `AGENTS.md`.

**Original diagnostic** demonstrably times only `spectrum.accept`, with `take` outside the timer; it cannot support end-to-end/heap/device conclusions. The proposed three graph variants avoid adding a second source read/FFT or violating host-owned subscription by injecting a receipt or wrapper. They deliberately measure module-graph overheads and full-path deltas rather than assigning all delta to one cost component.

## Executed independent source-grounded controls

**Method:** Fetched *actual production function bodies* for `measureRms`/metadata snapshot, `createAnalysisPipeline`, `createPcmBufferSource`, `createPeakSpectrumAnalyzer`, `createSpectrumDelivery`, `createSpectrumStream`, `createPsdProcessor` and `createPsdSession` from accepted source SHA. Evaluated them in an isolated V8 JavaScript environment after adapting **only import/export declarations** and wiring their exported dependencies. Used genuine Float32 generated PCM within a real production `createPcmBufferSource` and full CP2 pipeline. This is not `npm test`, an actual PCM16 WAV decode, a production module-loader run, Chromium, profiler or timed benchmark. It is direct source-function behavior, not arithmetic alone.

**Checks actually executed, all PASS:**
1. **CP2 B4 / FFT M8/H4/N8, 20 samples** with four full nonfinal B4 blocks then one full final B4: four complete PSD windows `[0,8),[4,12),[8,16),[12,20)`, producer properly ended, consumer drained. No premature nonfinal rejection because M>B.
2. **B8, L7 nonfinal**: actual pipeline rejected as `invalid / Source returned an incomplete PCM block`; **B8, L7 final**: accepted as `ready/final`, then clean `ended` on next null.
3. **Two B8192 blocks at default M1024/H512/N1024, delaying PSD drain:** C31 survived and delivered exactly **31** PSD windows; C30 became `broken/subscriber-delivery-overrun` and delivered **zero partial** windows. Read-before-drain queue values were 15,31 for C31 versus 15,0 for C30. This also verifies the C31 reservation fits current producer budgets.
4. **Three B8192 blocks at default M1024/H512/N1024, C16, draining per accept:** 47 complete PSD windows delivered and final control `drained`; per-block computation counts 15/16/16 follow from independent `W(T)`.
5. **Independent arithmetic work/guard table:** normal 400×B480 at M1024/H512/N1024 = 374 FFTs, **1,914,880** estimated radix-2 butterflies (under the proposed 5M/1024-completion guard). Retainable M/N16384/H512, 3×B8192 => 0/1/16, 17 FFTs and **1,949,696 butterflies** (under guard). H1 2×B8192 => 0/1; third B8192 => **8192 new transforms**, **939,524,096 butterflies** for third block (beyond default work guards). 8192 additional transforms create **2 GiB scratch allocations** cumulatively, excluding arrays/GC; not a measured resident heap. One C16 at B=8193 reserves 131088 bins, two reserve 262176 > accepted 262144 budget.
6. **Guard design:** Routine passes stay below both proposal limits (5M butterflies per trial and 1024 per-accept/4096 per-trial completions); pathology must be skipped/opted in, not attempted under CI. Source guards plus external parent process termination are needed; an in-process timer cannot interrupt one synchronous `accept`.
7. **Present accepted host no-op slider:** `src/main.js:159–169` checks source revision before invalidating, so the plan's same-value test-control statement is accurate on this base. Recorded to avoid transplanting stale PR #13 behavior into the present review.

The independent arithmetic is an oracle for completion and aggregate work **not** a latency/GC/heap measurement. Exact large-H1 FFT source function was **not executed**, intentionally avoiding uncontrolled allocation. The producer's source-derived `W(T)` plus small controls support that expected case.

## Design judgments and alternative experiments

**What this design gets right:**
- **A clean question:** compare latest-only source/CP2/FFT, native bounded delivery, and actual host-owned PSD, with identical PCM *within* source class; file-PCM16 and synthetic-sine populations are separate (quantization and phase accumulation differ).
- **Correct scientific chronology:** report CP2 completion span, source epoch and BigInt sample indices separately from callback wall time; a paused demand-driven file/synthetic source does not prove lost live input.
- **Honest queue semantics:** a fast consumer can still lose coverage atomically when one admitted B8192 block creates 15 or 16 windows under C4; backlog C31/C30 isolates that distinction. Distinguish producer computed, subscriber eligible, queued, delivered, sticky-overrun forfeiture and pre-subscription history.
- **Real performance observability:** time inclusive source/CP2 and FFT and PSD, but **do not sum nested stage measures**. Run plain versus instrumented controls, separate observer and GC profiling passes, report sampled high-water as sampling, and keep Canvas/rAF proxy separate from scientific work and presentation hardware.
- **Safe decision gating:** 3 warmups/7 rotated trials, raw records, no p99 claim from seven trials, explicitly defined guard aborts, opt-in external watchdog, no contamination of CI with 8192×16k stress. 005B remains a small isolated set of scripts/tests/report only, no production policy.
- **Rollback/authority:** one Markdown diff, PR draft, no 005B implementation authorized and no silent adoption of a device or multi-provider latency threshold.

**Nonblocking Kite follow-up N1 (implementation safety): DFT oracle resource admission.** In `Section 8` state that direct complex DFT runs in an independently bounded small-N control matrix; large-N checks use a sampled-bin oracle and time-domain energy/Parseval, with explicitly bounded oracle cost and correctness checks excluded from timed service measurements. Falsifier: if a future 005B runner calls full DFT across all 17×16384 FFT outputs, the test itself requires ~2.28×10^9 term evaluations without crossing the existing production butterfly gate; this invalidates any claimed service/GC comparison. Include a separate oracle-operation cap. No changes to protected FFT or producer API needed.

**Optional follow-up N2 (interpretation):** End-to-end source-read/CP2 residual subtracts one nested timer from another; report it as a differential estimate with overhead/variance, not a pure isolated acquisition allocation. Plan `Section 4` already says this; preserve the qualifier when implementing. Similarly a measured native PSD versus native delivery delta does not isolate just PSD math because status/queue/control overheads differ.

## CI and evidence limits

PR full comparison: two commits, **only** `docs/AP117_005A_BENCHMARK_PLAN.md` +378, no app code or benchmark executable. GitHub Actions [run 44064264503](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44064264503) reports **completed/success** for exact head; implementer/Axiom report 131/131 Node tests, build, HTML, Chromium smoke and whitespace from this CI run. I verified run metadata, **not** independently fetched the job logs or rerun those tests.

**NOT RUN:** proposed 005B CLI tools (they do not yet exist), direct complex DFT on 16384 bins, pathological fully primed source computation, Node child runner/GC/heap profiler, Chromium responsiveness, full app E2E, device tests. No false benchmark numbers are asserted. V8 source-based tests and arithmetic are described separately from CI.

**Verdict:** `COMMENTED — PASS for AP117-005A DESIGN`, with a **nonblocking** resource-bound clarification for 005B numerical oracles. Axiom and owner retain integration, adoption and merge decisions; Issue #11 remains open. No application, other-agent memory or benchmark implementation edits made.

## Evidence

Source-pinned plan and accepted production code were read at exact SHA; actual original source bodies were exercised in a constrained, instrumentation-free V8 function environment for CP2/producer/PSD correctness (not a Node/browser full run); independent arithmetic evaluated workload counts, FFT butterfly/allocation estimates and naive large-N DFT terms. Previously posted Axiom review comments were visible before this critique; independent findings are generated from source and reproducible checks, not attributed to those comments. No user-private data included.

## Revisit when

AP117-005B is separately authorized, its oracle and work guards implemented, a revision changes the plan, a measured Node/browser GC or throughput envelope becomes available, or the owner defines device targets/latency thresholds or provider concurrency for a later checkpoint. Preserve the difference between an accepted experiment design and an accepted performance operating envelope.

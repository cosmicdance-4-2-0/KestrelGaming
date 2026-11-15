---
schema: 1
id: 2026-11-15-kite-ap117-pr9-performance-review-k91c
kind: decision
scope: agent:kite
status: draft
evidence: inferred
author: kite-session
created: 2026-11-15
updated: 2026-11-15
sources: "Axiom PR9 assignment issuecomment-6891240452; ap_117_KESTREL PR9 head 35ae476ec8d59c300de877381f84ec7b8c59a1fa vs main 0531e734a2ece59cd877ea8659069efee2e0a905; Kite branch agents/kite-v1@dcbc52146e57125e2451704fd2abe9d64eeba57f."
---

# Kite — AP117-002 PR #9, independent performance and alternatives review

**Exact target:** cosmicdance-4-2-0/ap_117_KESTREL PR #9 at `35ae476ec8d59c300de877381f84ec7b8c59a1fa`, draft against accepted `main@0531e734a2ece59cd877ea8659069efee2e0a905`. Same live head rechecked before review. The 12-file comparison has 1394 additions and 11 deletions.
**Dispatch:** https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9#issuecomment-6891240452
**Prior design:** Issue #8 owner-synthesis comment https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8#issuecomment-6890071261
**Individual identity:** Kite — The Unlicensed Inventor; loaded branch-local Kestrel `AGENTS.md`, `KESTREL.md`, `agents/kite/AGENT.md`, `PROFILE.json`, memory permissions/protocols/index, and own prior Auralprint 117 sync02 review on `agents/kite-v1@dcbc52146e57125e2451704fd2abe9d64eeba57f`. No other agent's new PR #9 review consulted before recording this first pass.
**Scope:** REVIEW ONLY. No app code, tests, PR branch, contract, merge, release or other agent memory edited.

## Summary

**Specialist verdict: CONDITIONAL PASS.** Bounded pull is credible for the narrow ordered-or-explicit-break contract; I found no source-demonstrated queue-performance defect that invalidates the four-window proof. It is not comprehensive PR acceptance and does not certify an unrestricted FFT tuning domain.

**High-severity unresolved performance-admission risk:** a bounded queue bounds *retained* complete spectra, not FFT computation. The documented allowed combination `windowFrames=16384, fftFrames=16384, hopFrames=1, maxInputFrames=8192` can perform 8192 transforms in one *fully primed* accept call, even when every subscriber must overrun and no delivery envelopes are staged. The cost is inherited from accepted CP3-A analysis, **not newly caused by the PR**, and the PR documentation already explicitly admits the missing measurement. Before broad production claims, select a measured supported configuration domain, bounded-work admission or an authorized scheduling strategy. Do not refactor protected FFT math in this PR.

## Source receipt

Read via connected GitHub at the exact PR head:
- `src/analysis/spectrum-stream.js` blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc`, lines 120–126 full-input finite validation, lines 145–149 completion count/staging decision, lines 151–176 unchanged FFT and owned publication, lines 185–194 atomic commit.
- `src/analysis/spectrum-delivery.js` blob `ef19cd748de41226ab0cd8375949e278f7aeb76f`, lines 39–48 subscription reservation, 77–89 pull, 108–116 prepare, 122–143 commit/overrun.
- `scripts/measure-spectrum-delivery.mjs` blob `f0c6f6d0d8da9db32b4215793902cb712bdc2849`, lines 37–53 accept-only timer, 61–86 freeze event counters, 94–106 baseline loading/variants, 108–135 measured rounds, 137–158 extremes.
- `docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md` blob `f56821afa8fbc645fef6e5dfa7bea69877ac2ba4`, resource/benchmark evidence lines 132–197; `src/config.js` blob `2408897d5f7c6f5ff0c08e65d54af4cf1a4405b1`.
- New `tests/spectrum-delivery-atomic.test.js`, `spectrum-delivery.test.js`, `spectrum-delivery-lifecycle.test.js` and `spectrum-delivery-math.test.js`; main/pagehide and CP3 frequency contract diff; original accepted FFT source unchanged.
- `.github/workflows/ci.yml` runs Node/static/HTML/Chromium/whitespace checks but not the measurement script. GitHub Actions run 43690871559 at this head reports completed SUCCESS; PR author reports 93 passed Node tests. These are external evidence, not independently executed tests.

## Findings, ranked

### F1 — HIGH, unsupported peak computational cost

**Falsifier:** Start an accepted max FFT with 8192 frames, accept a second 8192-frame input to complete the first 16384-frame window, then accept a third permitted 8192-frame block with hop1. Before the third block the assembler has `fill = M-H = 16383`. The source formula yields `Q = floor((16383+8192-16384)/1)+1 = 8192` complete windows in one call. The shipped measurement script tests this FFT size only with **two** 8192-frame inputs, producing *one* complete FFT; its 8129-window overrun control uses the cheap `Nfft=64` FFT. Thus neither case covers the fully primed combined CPU/GC extreme.

With 8192 transforms and Nfft=16384:
- Approximate radix-2 butterfly operations: `8192*(16384/2)*14 = 939,524,096`.
- Two Float64 scratch arrays per transform: `8192*2*16384*8 = 2,147,483,648` bytes = 2 GiB allocation churn.
- One owned 8193-bin amplitude array per transform: `8192*8193*8 = 536,936,448` numeric payload bytes, ~512 MiB.
- Combined cumulative numeric allocation is `2,684,420,096` bytes ≈ 2.50006 GiB, excluding metadata, JS array representations and GC.
- Delivery's total reserved bin cap `R=262144` and B=8193 admit at most `floor(R/B)=31` observations for even one subscriber; all complete subscribers necessarily overrun this batch. `delivery.prepare` saves stage-envelope allocation but `analyzer.analyze` is still called 8192 times.

A large accepted sample block can therefore be memory-bounded **as retained delivery** and simultaneously cause severe main-thread CPU and garbage-collection pressure. No hard-realtime performance or hang duration is claimed without measurement. This general FFT/hop1 issue preexisted AP117-002; note it as a separately owner-controlled performance gate, not an unsolicited implementation change.

**Requested gate before broad supported-config claims:** deterministic maximum-work calculation from `M,H,Nfft,maxInputFrames`; explicit accepted performance domain or bounded work admission; optionally a named off-CI fully primed stress fixture, plus browser GC/main-thread measures. Do not add a multi-gigabyte CI stress loop or silently alter peak FFT math.

### F2 — MEDIUM, diagnostic overhead is only accept-time overhead

**Source:** measurement script lines 37–53, 94–135, AP117-002 doc lines 172–197.

**Good fairness controls:** uses `git show 0531e734...:src/analysis/spectrum-stream.js` to load the actual baseline, rewrites its FFT import to the *unchanged* current FFT implementation, gives four variants identical precreated valid 400×480 PCM publications, three warmup rounds, seven measured rotated-order rounds, ordinary GC. Independent count `floor((400*480-1024)/512)+1=374` complete windows and latest revision 375 matches the script assertions. The accepted 480-frame blocks avoid normal subscriber overrun.

**Limit:** the timer encloses only `stream.accept(publication)`, while `take` drains happen after timing and subscriber construction/disposal, derived consumer CPU, resident/peak memory, and independent rendering are not measured. The benchmark therefore measures **producer accept overhead**, not end-to-end delivery throughput, total CPU utilization, GC latency, or device performance. The baseline and new code also differ in full-waveform validation: new `spectrum-stream.js:124–126` scans PCM *before* its FFT assembly loop at 151. Thus even `delivery-no-subscriber` is not a pure queue-only delta.

**Author-reported numbers, not independently rerun:** baseline median total 14.878 ms/400 accepts; no-subscriber 16.225 ms; cap4-drained 16.332 ms; cap4-stalled 16.306 ms. The nominal +9.05% (no sub) and +9.77% (drained) relative to baseline are descriptive single-run ratios, not stable slowdown coefficients. Drain is excluded, and a separate contended run varied materially. Do not attribute all difference to queuing or claim an SLA.

**Suggested next trial:** separately time `accept`, `take` and actual downstream consumer computation; capture GC/heap high-water and browser frame responsiveness with identical inputs and varying max accepted blocks. Keep the current script as valid *limited diagnostic*, not acceptance of production performance.

### F3 — MEDIUM, unavoidable atomic overrun needs consumer capacity guidance

The source correctly returns a sticky subscriber-local break when a whole batch cannot fit before any post-accept `take`. The required 20-frame `M8/H4` test completes Q=4, so cap2 fails and cap4 succeeds. **Independent extension using existing default FFT geometry** `M1024/H512` and one legal input of 8192 frames completes 15 windows from an empty assembler or 16 from the normal primed state. A cap4 subscriber cannot receive a whole batch *even if it drains immediately after every accept*. This is **expected truthful behavior**, not silent data loss or evidence of a flawed queue.

**Recommendation:** document how a caller relates `capacityObservations` to maximum complete windows in an atomic block *plus unconsumed backlog*, not average render rate. If bounded complete delivery cannot be guaranteed for chosen source/block geometry, its overrun is correct; offline backpressure/chunking needs a separate actual source-ownership proof. No implicit unlimited history or new default capacity.

### F4 — LOW, event counts are not measured retained heap

`scripts/measure-spectrum-delivery.mjs:61–86` temporarily wraps `Object.freeze` and counts frozen JS arrays, ready publications, staged/taken envelopes. This establishes reproducible **allocation event counts for those selected objects**, not peak simultaneous retention; it excludes FFT Float64 scratch arrays, metadata, mutable arrays and GC. The docs already disclose this correctly. Its numeric-payload formula `8*R+24*B+16*M+16*N` gives `2,818,072` bytes ≈ 2.688 MiB for max M=Nfft=16384, distinct from the ~2.5 GiB **cumulative** churn above. Avoid describing the numeric estimate as a proven V8/browser heap cap.

**Minor reproducibility detail:** benchmark `git show` requires the pinned baseline commit object in local Git history. A source-only download or shallow checkout need not have it; note the full-history prerequisite. GitHub CI uses fetch-depth 0 but does **not** run the benchmark script.

## Independent alternative comparison and changed opinion

**Current bounded pull:** Complete observations are staged only if subscribers survive the whole incoming batch. On late NaN or injected FFT exception, no new complete observation escapes. No consumer callback runs inside producer `accept`. Independent slow consumers can overrun without altering fast consumers' source truth; current latest remains compatible. Cost: per-handle queues/flags, O(C) checks with C<=8, queue.shift bounded by K<=64, finite retained snapshots. This is proportionate to the owner-established *multi-rate* requirement.

**Earlier Kite prototype A — synchronous per-window push:** Cheap to prototype and delivers four windows when everything succeeds. But it **fails the accepted transactional publication gate as a drop-in**: a later FFT failure cannot retract a callback's already consumed earlier window. PCM prevalidation alone does not eliminate injected FFT exceptions. Running callbacks within accept additionally introduces head-of-line blocking and reentrancy. Keep push as a disposable performance/control experiment, not a current alternative for merger without an atomic staging boundary.

**Host-owned bounded completion batch:** Can postpone publication until accept succeeds, then return a finite batch for host fanout. Potentially smaller than many persistent subscription handles for **one trusted complete consumer**. For multiple independently paced consumers it merely moves per-consumer backlog, currentness, failure/disposal and gap bookkeeping into the host, or forces synchronous consumption. To replace pull, demonstrate the same atomicity, two-subscriber independence, overrun/fence semantics and lower owned state under matched budgets. Do not add this as new production code while reviewing PR #9.

**Revised Kite position:** For this transactional, multi-rate requirement, **bounded pull wins over my earlier push-first preference**. That change follows the observable late-failure and isolation requirements, not other reviewers' votes. Pull vs push does not solve extreme FFT work admission; keep these decisions separate.

## Checks and exact evidence limits

**Actually executed, independent sandbox Node v22.16.0 arithmetic only:** a pure `Math.floor((fill+frames-M)/H)+1` completion-count check returned (M1024,H512,8192): 15 empty / 16 primed; (M8,H4,20): 4; (M16384,H1,8192): 8192 primed. A second Node arithmetic calculation returned R/B cap31, butterfly count 939524096, scratch 2147483648 bytes, amplitude 536936448 bytes, combined 2684420096 bytes and nominal live numeric payload 2818072 bytes. These are *source-derived numerical calculations*, not tests executing the PR code or FFT algorithm.

**Attempted but blocked:** `git ls-remote https://github.com/cosmicdance-4-2-0/ap_117_KESTREL.git HEAD` returned `fatal: Could not resolve host: github.com` in local container. No independent clone; `npm test`, `npm run verify`, `node scripts/measure-spectrum-delivery.mjs`, Chrome/GC/memory profiling and full max-FFT stress **NOT EXECUTED** by Kite. PR author's local 93 passing tests and GitHub Actions success are attributed, not reproduced.

**Not observed:** a numerical regression, malformed queue overrun, leaked complete observation from rejected atomic batch, or measured real-device frame stall. This focused conclusion does not substitute for Gauge/Flint/Harbor/Latch/Mothlight specialties.

## Recommendations, severity and authority

**CONDITIONAL PASS** for AP117-002 performance/alternatives at the exact reviewed head, with no new implementation defect established. **HIGH follow-up**: record the fully primed hop1/maxFFT computation limit and decide production config/work budget *before promising general-purpose performance*. **MEDIUM follow-up**: make benchmark coverage and accept-only timing explicit; add end-to-end/performance evidence only when a relevant performance acceptance claim is made. **MEDIUM usability/composability follow-up**: capacity guidance for atomic one-block overflow. **LOW documentation**: benchmark needs full Git history.

Preserve accepted `ap117.measurement/2` and `ap117.spectrum/1` science, FFT normalization, single PCM read, latest-only renderer, and current render/EOF policy. Do not optimize protected FFT code, add a second prototype, register a new plugin system, merge this PR or rewrite another agent's memories under this review. Axiom/owner retain final integration and merge authority. No PSD or hard-realtime certification is asserted.

## Evidence

The actual PR #9 source, design record, benchmark script, tests, app contract and CI workflow were read at SHA `35ae476ec8d59c300de877381f84ec7b8c59a1fa`. The evidence classifications are: **observed code and external CI**, **independently executed source-derived arithmetic**, and **unverified runtime performance**. The shared GitHub account provides a human-linked write trail, not independent agent authentication. This is a public-safe draft individual review, not adopted project policy.

## Revisit when

Axiom reconciles the six PR #9 reviews; the PR head moves; owner selects actual supported FFT configurations or a computational-work budget; a full-path browser/GC stress/benchmark becomes available; or independent implementation tests contradict the predicted completion/overrun counts.

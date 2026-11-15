---
schema: 1
id: 2026-11-15-ap117-002-pr9-flint-api-ownership-b47a
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-002-pr9-independent-review
created: 2026-11-15
updated: 2026-11-15
sources: "Axiom independent PR9 dispatch comment 6891240452; ap_117_KESTREL PR9 exact head 35ae476ec8d59c300de877381f84ec7b8c59a1fa versus accepted main 0531e734a2ece59cd877ea8659069efee2e0a905; KestrelGaming agents/flint-v1 at 2a47b5eb21a75cb62cd429661d37dd8e66d00910; source-executed independent V8 probes; CI 43690871559."
---

# Flint — AP117-002 PR #9 API, ownership and resource-bound review

**Task outcome: COMPLETE — independent first pass; READ-ONLY.**  
**Verdict: PASS for Flint's bounded complete-spectrum delivery architecture remit at exact head `35ae476ec8d59c300de877381f84ec7b8c59a1fa`.** No blocking correctness defect found in the inspected source and targeted source-execution probes. One **IMPORTANT deferred performance/product gate** remains; it is an explicitly documented preexisting worst-case FFT configuration risk rather than a regression demonstrated by this PR. No application implementation, PR head modification, merge, deployment or shared schema ratification.

**Authorship/independence:** Flint — The Reducer, individual design perspective under the shared cosmicdance GitHub account. The account identity does not authenticate an autonomous agent. I loaded Flint's own Kestrel contract/profile and indexed Auralprint CP3-A/B1/Sync 02 memory. I read the exact Axiom assignment comment, code, tests, implementation record and accepted baseline. **No other engineer's new PR #9 review was inspected before preserving this report.** Historic Issue #8 requirements were supplied as handoff context; first pass derives its checks from source.

## Summary

**Retain the two-file separation and its deliberately small API.** The `createSpectrumStream` owns PCM chronology, FFT window assembler, measurement revisions and latest `readCurrent()/isCurrent()`. Its private `createSpectrumDelivery` owns capacity reservation, subscriber queues, generation/continuity fences and ordered committed observations. Per-subscriber complete delivery is either complete for the configured capacity or explicitly broken; latest render remains independent. No subscriber callbacks execute inside `accept()`; there is still only one already validated CP2 source acquisition, and the accepted FFT normalization is unchanged. The producer publishes no partially failed batch to subscribers or latest readers.

A smaller synchronous per-completion callback or `accept()` returning a batch saves local queue code only by transferring independent scheduling, memory-pressure, exception isolation and lifecycle obligations to callers. That duplicates ownership rather than removing it. A general broker, DAG, topic registry or plugin infrastructure is strictly more machinery and is not warranted. A per-subscriber ring-buffer implementation would improve the current `Array.shift()` amortized-removal cost, but adds complexity without demonstrated benefit under `capacityObservations <= 64`.

**PASS is scoped to a bounded proof and existing trusted built-ins**, not device-latency certification, hostile plugin isolation, unlimited recording history, or approval of the broadest valid FFT/hop configuration for live main-thread use. The owner's remaining merge/acceptance decision is separate.

## Evidence — exact source receipt

- **Assignment:** [Axiom's PR #9 dispatch](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9#issuecomment-6891240452), comment ID `6891240452` (explicit review only).
- **PR:** [AP117-002 PR #9](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/9), head `35ae476ec8d59c300de877381f84ec7b8c59a1fa`, base `0531e734a2ece59cd877ea8659069efee2e0a905`, one commit ahead/zero behind, draft/open/not merged when examined; live `main` matched pinned base. **No later head is covered by this verdict.**
- **Producer core:** [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-stream.js), blob `4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc`; [`src/analysis/spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/35ae476ec8d59c300de877381f84ec7b8c59a1fa/src/analysis/spectrum-delivery.js), blob `ef19cd748de41226ab0cd8375949e278f7aeb76f`. Existing FFT `src/analysis/fft-amplitude.js` blob `ee35e0793aceb5eb9e3fc49d27f293a1719effc5`, unchanged.
- **Scope inputs:** `src/config.js` blob `2408897d5f7c6f5ff0c08e65d54af4cf1a4405b1`; `docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md` blob `f56821afa8fbc645fef6e5dfa7bea69877ac2ba4`; `scripts/measure-spectrum-delivery.mjs` blob `f0c6f6d0d8da9db32b4215793902cb712bdc2849`; `src/main.js`, `docs/CP3_FREQUENCY.md`, new four `tests/spectrum-delivery*.test.js` and modified `tests/app-integration.test.js` inspected via exact-head PR diff/files. Source `AGENTS.md` and CP3 contract read at accepted base/PR (no substantive change).
- **Flint home continuity:** [`agents/flint-v1`](https://github.com/cosmicdance-4-2-0/KestrelGaming/tree/agents/flint-v1), read before test: `2a47b5eb21a75cb62cd429661d37dd8e66d00910`; own `AGENT.md` blob `b56d89557a84ddd9f3c234cc4c7ace0ffa6ee76c`, `PROFILE.json` blob `b6391d89c44152ce44fbf16bdba1f3deb44fdefe`, branch-local AGENTS/KESTREL, MEMORY/STATE/PERMISSIONS, current index and original CP3-B1/Sync 02 work.
- **GitHub Actions:** [run 43690871559](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43690871559) verified through GitHub run metadata: exact head, completed, conclusion **success**. The 93/93 Node, static/HTML/Chromium and benchmark details are reported in PR body and its implementation record, **not independently rerun as a whole suite by Flint**. Local Git checkout was unavailable through the container's DNS/network; source-executed probes were therefore run with exact GitHub-fetched production source bodies in a fresh JS/V8 evaluator after mechanical import/export-declaration adaptation. No external dependency/instrumentality was silently substituted.

## 1. API and ownership

**Current existing API preserved:** `accept(publication)`, `readCurrent()`, `isCurrent(stamp)`, `reset()`, `invalidate()`. Added `dispose()` and `subscribeComplete({capacityObservations}) -> {take, readStatus, resync, dispose}`. Legacy construction without `delivery` keeps latest-only FFT and explicitly rejects attempting complete subscription (`src/analysis/spectrum-stream.js:7-14,201-209`; `spectrum-delivery.js:39-53`).

**One coherent obligation per component:** `spectrum-stream` alone assigns numerical measurement revisions and spectra from accepted CP2 PCM; `spectrum-delivery` alone allocates subscriber mailbox capacities, generation/completion-ordinal stamps, continuityRevision and sticky control state. Subscriber `take()` never invokes a callback in producer `accept()` and cannot mutate the producer's FFT. Each published `ap117.spectrum/1` numerical vector is owned and frozen by its analyzer, so multiple queues can reference the same published object; no copy per subscriber. CP2 `Float32Array` remains trusted read-only borrowed data, **not** sandbox-isolated immutability. Existing `FrameHost` and rendering model remain out of this seam.

**Queue complexity:** each handle retains up to C observation references and O(1) control fields, so storage is O(C); the `Set` of subscriptions is O(S) with S bounded by 8. `delivery.prepare/commit` each scan at most S subscribers, so O(S) for fixed S. `take()` uses `Array.shift()` (`spectrum-delivery.js:76-84`), hence removal is O(C), not worst-case O(1). This is **MINOR / nonblocking** at declared max C=64; do not introduce a ring unless stress profiling justifies it. Queue and staging are not an unlimited general history store.

**Configured budgets:** limits captured by value when producer is constructed (`delivery.js:9-18`). Admission computes `capacityObservations * (Nfft/2+1)`, and rejects if sum exceeds `maxRetainedBins`, max subscriptions or cap ceiling (`delivery.js:39-54`). A separate source-executed control with B=8193 accepted cap31 and rejected cap32 as expected. This is a conservative **reservation** budget, not metered actual JS heap. Freed subscriptions release reservations, not consumer-retained frozen observations; those are explicitly outside producer ownership.

**Size proportionality:** one pinned commit changes exactly **12 files, +1,394/-11 lines**. Of additions, **247 production**, **738 tests**, **246 documentation** and **163 development-only diagnostic**. The 164-line delivery primitive isolates queue/fence state, and most expansion is focused falsification coverage. No general broker, runtime plugin sandbox, PSD implementation, renderer engine, second PCM acquisition, new scheduler or FFT math rewrite. The size is justified by the lifecycle it proves; removing the queue object would shift those obligations elsewhere rather than eliminate them.

## 2. Independent source-executed falsifiers — actual results

**Probe method:** fetched actual exact-head `src/analysis/{fft-amplitude,spectrum-delivery,spectrum-stream}.js` via GitHub connector and directly evaluated their function bodies after removing only ES module `import`/`export` declarations. The accepted old `spectrum-stream.js` was evaluated against the same fetched FFT for comparison. These are **direct execution of production function bodies**, not Node's module loader, browser tests or the repository's unit suite. Results apply only to the pinned head.

| Independent probe | Exact observed result |
| --- | --- |
| **P1 M=8/H=4/Nfft=8**, 20 exact finite values `x[n]=(n+1)/32` as one block and five 4-frame legal blocks | Both delivered four `[0,8), [4,12), [8,16), [12,20)` observations, spectrum revisions `2,3,4,5`, delivery ordinals `1..4`, DC bins `0.15625,0.28125,0.40625,0.53125`, latest start 12 and `ended` after drain. |
| **P2 Four-window batch, capacity 2** | No ready observations delivered; subscriber `status=break`, `reason=subscriber-delivery-overrun`, frontier 4, latest window still `[12,20)`. |
| **P3 Late NaN** | Last PCM sample nonfinite: `Nonfinite spectral PCM` throws; latest unavailable, queued 0, next subscription result `break`; no early ready escaped. |
| **P4 Injected FFT failure** | Throw from instrumented `Math.hypot` on sixth bin after earlier analysis work: error propagated; latest unavailable, subscriber `break`, queued 0. With one prior undrained ready, the failure additionally cleared that backlog and advanced the producer generation; no stale ready escaped. |
| **P5 No subscribers, one 20-frame input** | Four FFT amplitude arrays computed; `ready` latest revision 5, source start 12; **zero staged delivery observation envelopes**. |
| **P6 Two subscriber rates** | A capacity-two slow consumer reported sticky overrun; a fast consumer drained three valid sequential observations and stayed `open`. |
| **P7 Inevitable overrun stress**, M=Nfft=64/H=1, 8,192 frames | `completionOrdinal=8129`, latest start 8128, subscriber `break`, **0 staged delivery envelopes** while all **8,129 FFT amplitude arrays** were still created. Isolated evaluator elapsed ~500 ms, not a stable performance benchmark. |
| **P8 Subscription budget**, B=8193 | cap31 admitted, cap32 rejected by `maxRetainedBins`; adding a subscription beyond a fully reserved budget rejected. |
| **P9 Legacy mode** (no delivery limits) | `accept` generated ready revision 2, DC 0.25; `readCurrent/isCurrent` both correct; `subscribeComplete` explicitly threw `requires configured resource limits`. |
| **P10 Cached ready then reset** | Producer generation advanced from `1n` to `2n`, next `take()` was `break(source-replaced)`, latest unavailable. |
| **P11 Behavioral compatibility fuzz** | **400 deterministic varied legal input sequences**, each up to 20 ready acceptance calls (8,000 total), six M/H/N geometries, rectangular/Hann, randomized legal block lengths, source parameter revisions and final statuses. Compared old and PR9 `readCurrent()` revision, status, reason, exact BigInt spans and all amplitude values after each accepted call. **Zero mismatches** in observed cases. |

The source check does **not** independently prove 93 Node tests, all FFT-bin direct-DFT numerical controls, browser/device safety, live CPU scheduling, full GitHub checkout behavior, or a worst-case `M=Nfft=16384,H=1` run. Gauge's complete numerical oracle is a separate remit. GitHub Action success is attributed to its published run, not converted into our own test result.

## 3. Severity-ranked findings

### PASS — No demonstrated correctness blocker in Flint's remit

**Atomicity:** `spectrum-stream.js:119-126` prevalidates the entire PCM block, `:128-179` stages only numeric completions and eligible envelopes, `:188-194` commits after all analysis and never executes subscriber code. On error `:195-198` resets and delivery-fences queued observations. This directly closes my Sync 02 synchronous callback late-NaN and reentrancy objection. It does **not** promise trusted same-realm callbacks cannot monkeypatch shared globals; the product explicitly excludes hostile plugin isolation.

**Budget/overrun and ownership:** `spectrum-delivery.js:39-54,108-153` reserves capacity, runs O(S) survivor checks, rejects impossible staging, enqueues only bounded shared references, latches a control break even when all data queues are full, advances a source-window frontier and clears backlog on lifecycle fence. Independent probes P2/P5/P6/P7/P8 and source inspection support those invariants. No overrun disappears because a viewer skips rendering.

**Compatibility:** `spectrum-stream.js:201-209` retains legacy methods, P9/P11 demonstrate baseline latest/FFT agreement; independent source reads have not been introduced. Existing host render failure, EOF/replay and preview remain unchanged apart from terminal pagehide disposal. The current PR does not add a PSD production method or a new renderer.

### IMPORTANT, nonblocking for bounded proof — Work-per-accept is not bounded by queue memory

**Path:** `src/analysis/spectrum-stream.js:145-180`; `src/analysis/fft-amplitude.js` unchanged; `docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md:154-195`. `maxInputFrames=8192` and a 262,144-bin queue reservation ceiling bound input and **retained** delivery data, but do not bound **computation** or cumulative allocation inside a single `accept`. Primed `M=Nfft=16384,H=1` may perform 8192 transforms and create ~2 GiB scratch plus ~512 MiB amplitude arrays per such accept by the documented formula. Even my much smaller 64-point/H1 overrun performed 8129 FFTs despite staging none. This is an expected consequence of complete-window calculation inherited from CP3-A, **not a new correctness bug** or a data-memory reservation violation.

**Required future decision:** before advertising unrestricted live/hardware or general user-configurable DSP policies, select a **named per-accept work/latency budget** or explicit source-class backpressure/segmentation policy, measured with full primed extremes and browser memory/GC; reject or make explicit incompatible configurations rather than claim all accepted M/H/N choices are realtime. Do not change the accepted FFT math or silently skip complete windows to quiet the benchmark. A separate owner checkpoint is warranted; it need not block the narrow correctness proof.

### MINOR, nonblocking — FIFO `shift` costs O(C) per read

**Path:** `src/analysis/spectrum-delivery.js:79`. This is bounded to C<=64, while a ring would add index/compaction state and more lifecycle tests. A measurable per-subscriber drain hotspot in the real target workload would justify changing it; absent that evidence, retain the simpler implementation.

### IMPORTANT future integration note — Currentness and handle ownership

**Paths:** `spectrum-delivery.js:55-105`, `docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md:76-89`. The exported observation stamp is **not globally unique**: generation begins at `1n` per producer and continuity is per subscription. This is not a present defect in trusted built-in consumers: they are explicitly responsible for binding cached records to the **actual originating handle**, then checking producer generation/continuity both before and after async derived computation. A different producer or handle may have identical numeric stamps, so downstream cache keys using only `{generation,continuityRevision}` are invalid. The first real PSD/onset consumer integration must assert this handle-identity and post-yield fence behavior. This does not justify adding global GUIDs or a plugin authentication layer to this proof.

**Budget caveat:** “2.69 MiB” is explicitly an estimate for live numeric producer payload under reservation ceilings, **not** an upper bound on JS heap, cumulative churn, metadata/GC or frozen objects retained by consumer code. No claimed measured absolute allocation limit should enter acceptance criteria without instrumentation.

## 4. Smallest alternative evaluated

A synchronous **completion-batch callback** after the whole accepted `accept()` (instead of per-window push) would avoid callbacks from a partly failed block. It would also make downstream processing duration, errors and reentrancy affect upstream acquisition; more importantly, a slow/temporarily unavailable consumer still needs its **own bounded queue and explicit overrun** somewhere. Moving the queue into each consumer duplicates policies, and putting it in the host merely renames the broker. Thus no demonstrably smaller independently scheduled complete-delivery design was found. A simple `readBatch()` from producer-owned shared ring would still require per-subscriber cursors and overrun/history fencing, and would complicate generation ownership. Keep the current narrow producer-private queue.

Any future need for multiple asynchronously scheduled backpressure classes, worker/thread boundaries, dynamic cross-provider routing, persistent historical replay or hostile third-party plugins would require an explicitly versioned new seam. Do not prebuild it now.

## 5. Test commands, exact outcomes, and recommended gates

**Source-executed tests actually run in this review:** independent V8 function-body probes P1–P11 described above; no local `npm test` or browser process was run by this reviewer.

**Repository/CI evidence, separately attributed:**
- [Actions 43690871559](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43690871559) **verified by GitHub run metadata** as `head_sha=35ae476...`, `status=completed`, `conclusion=success`.
- `npm run verify` — 93/93 Node plus static build **per PR and AP117-002 implementation record**, not independently rerun.
- `npm run test:html`, `BROWSER_PATH=/usr/bin/chromium npm run test:browser`, `node --test tests/spectrum-delivery-math.test.js`, `node scripts/measure-spectrum-delivery.mjs`, `git diff --check` — **reported** passing at that head; the implementer reported a first browser run lacking bundled Chromium. Browser test currently exercises latest UI, not a real complete-spectrum consumer panel.
- Full local checkout blocked by network/DNS in this evaluation environment; do not convert tools' outputs into “independently ran npm verify.”

**Before implementation acceptance:** maintain existing protected CP2/CP3-A tests and source-clock contracts, keep complete-delivery atomicity and lifecycle tests, and explicitly assign the future work-budget decision. No changes required to the PR's current API/ownership model on evidence inspected. One reviewer cannot endorse other engineering specialties' uninspected results.

## 6. Scope and dissent

**Preserve:** `ap117.spectrum/1` numerical method, source PCM copy/clock, independent host rendering schedule, one current/latest view, bounded per-subscriber complete delivery, terminal/fault fences, separate `ap117.spectrum-delivery/1`, explicit new `CONFIG` budgets. **Defer:** unrelated performance redesign of FFT, dataflow graph, PSD product, B2 panel UI, render-fault isolation, device realtime, security sandbox, compositor and 116 compatibility.

**No required corrections in my remit at this head.** Dissent from any attempt to equate bound on *retained numeric bins* with bound on *per-accept execution cost*; from auto-promoting shared continuity stamps to global object identity; or from a blanket demand to replace this narrow queue with a universal event system. I would change my PASS if a source-executed legal input produced a lost/unmarked completed window within declared capacity, leaked a partial failed batch, changed accepted latest/FFT values, permitted cross-subscriber corruption, or exceeded admitted retained-bin ownership.

**Owner-facing recommendation:** PASS Flint's API/ownership review at the pinned head, with nonblocking tracked compute-budget risk. Re-pin and rerun affected probes if PR head changes. This report is not owner merge approval.

## Revisit when

Axiom reconciles six independently authored PR #9 reviews, a new exact PR head changes this seam, a real complete-window consumer integrates with async handle checking, or browser/FFT extreme profiling proves a need for an explicit compute-work bound or O(1) queue implementation. Preserve the original first-pass evidence, risks and dissent.

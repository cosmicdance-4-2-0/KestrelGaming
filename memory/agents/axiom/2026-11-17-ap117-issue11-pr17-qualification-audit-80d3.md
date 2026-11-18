---
schema: 1
id: 2026-11-17-ap117-issue11-pr17-qualification-audit-80d3
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "AP117 PR17 a5e75c9da8dd4799b1419c9c23b5dca76168326b base/main 521d5d227016ccdd50f0ac9a58c412c1606598ba; docs/ISSUE11_OPERATING_ENVELOPE_QUALIFICATION.md; docs/evidence/ISSUE11_LOCAL_TRIALS.json, ISSUE11_EXTRACT.py, README_ISSUE11.md, ISSUE11_CI_VERIFICATION.md, ISSUE11_CI_WITNESS.json; GitHub Actions 44204214177 job 134465869125; Axiom PR comment 6964864503."
---

# PR #17 — Axiom operating-envelope qualification evidence audit

## Decision

**PASS in Axiom's scope for document/evidence qualification checkpoint; production operating envelope NOT ACCEPTED; Issue #11 remains open.** User gave [PR #17](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/17) following Axiom's [ISSUE11-QUAL-01 handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11#issuecomment-6963865440). Exact reviewed head `a5e75c9da8dd4799b1419c9c23b5dca76168326b`, unchanged base `main@521d5d227016ccdd50f0ac9a58c412c1606598ba`. Six added docs/evidence files (+3680/−0), one is stdlib Python evidence extractor. No source, CONFIG, benchmark harness/tests, CI, dependency, schema, optimization or runtime change. Draft PR, unmerged at review. [Axiom PR comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/17#issuecomment-6964864503) preserves independent evidence and limits. Kite's review not yet received; owner has not approved candidate thresholds.

## Independent checks

Full report, 164-line postprocessor, local extract, evidence guide, historical CI verification and CI witness were read via GitHub connector. In the retained **reduced** JSON `ISSUE11_LOCAL_TRIALS.json`, calculated:
- 1,164 graph trial records, 822 measured, 134,115 source-processing steps counted by extractor, 199,872,798 bytes original *unshared* raw JSONL, 28,099,683 bytes original *unshared* diagnostic artifacts.
- Recomputed W(T) and conservation accounting for all 138 recorded run/group signatures; zero queue, correct original source SHA; no mismatches in this extract. All guard invocations present as SKIPPED_RESOURCE_GUARD, with no extracted aborted trials. Prior CI witness 72 COMPLETE records, conservation and variants are coherent but separately sourced (zero warmup/one measured).
- Normal Node PSD file coarse median 34.833879 ms summed across 400 blocks (not 34.8 ms per accept), max single-block core 4.686608 ms; synthetic max core 3.017070 coarse / 2.456062 stage. Normal browser PSD stage max core file 6.4 ms / synthetic 6.1 ms, violating proposed 5 ms limit.
- Retainable fully primed H512/M=N16384/B8192/C16 third accept: seven measured stage trials, median **13.910606** ms and range 12.010527–44.475715 ms core, median **12.034352** ms accept and range 10.270044–42.845005 ms. Fails proposed 10ms. Pathological fully primed H1 8192 transforms remains **NOT RUN** by design, needs explicit hard isolation/authorization if ever required.
- Node GC observed count/max 85/3.474035 ms; Node allocation 165/7.469007; browser GC 1128/5.830, browser profile 3506/7.021. Browser CDP event nesting and profiling observer costs are not exclusive stop-the-world pause/causation. Node RSS sample max 225705984 B; browser sample max timing 1018048512, GC 1044566016, profile 1042366464, heap 914305024 B; browser all above proposed 768MiB screen and below independent 1GiB sampled guard.
- Built app file plain/instrumented endpoints both 192000 frames / 374 PSD, drained terminal historical span; synthetic endpoints 480960/938 and 482400/941, each matched W(T); never assume equal accepted source counts for equal wall intervals. Observed file rAF max 116.796ms and 92ms Long Task, interaction max rAF interval 133.266ms; presentation proxies, not confirmed paint or realtime evidence.
- [Exact PR head CI run 44204214177](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44204214177), job 134465869125 success, **150/150 Node tests, zero fail/skip**, build, Nu HTML, Chromium offline browser smoke, artifact upload, whitespace. Independently inspected job log via GitHub but did not run locally. New CI artifact 14383305965 is **not** seven-trial local performance population.

## Constraints / later decision

Codex's 5ms normal service, 10ms bounded maxFFT, 5ms GC event, 64MiB heap, 256MiB Node RSS, 768MiB browser RSS, rAF/input budget proposals are **owner-choice candidates only**, not CONFIG limits, service-level agreements, or universal device admission. Repeated local files remain author-reported and unshared despite SHA-256 and bounded reduced extracts; do not label as independently rerun. Live capture, physical device, worker/WASM candidates, CPU usage/deadline/true peak and concurrent provider/consumer safety remain unmeasured. The smallest next experiment is unchanged built app on **an owner-chosen actual target** with controlled visible foreground conditions, repeated file/synthetic app trials, and independently sourced budget requirements. Issue #11 remains open until owner-reviewed scoped envelope and falsifiable target-specific tests; Kite independent review/owner merge choice are separate. On new PR head inspect diffs and re-review.


## Independent Kite review reconciled — exact head a5e75c9

Kite published [PR #17 independent COMMENTED — PASS](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/17), with [individual source-pinned report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/67d76fa3e544d501ef15da262785f5525970c54a/memory/agents/kite/2026-11-17-kite-ap117-pr17-operating-envelope-audit-k17e.md) at `KestrelGaming/agents/kite-v1@67d76fa3e544d501ef15da262785f5525970c54a`. Axiom re-read the full canonical Kite memory and the PR review at exact head `a5e75c9da8dd4799b1419c9c23b5dca76168326b`. Kite independently checked actual committed extract group/row arithmetic, 64 unique group-data objects across 138 named aliases, 822/342 measured/warmup, 72 historical CI trial totals, seven maxFFT third-block witnesses, GC event counts/max, browser aggregate RSS and guarded skips. It concurs with Axiom's source/evidence finding: **no blockers for the document/evidence checkpoint**, while physical-device performance, owner-defined budgets and general admission remain unproven. Kite transparently notes Axiom's prior PR comment was visible, so review is independently calculated but **not blind**.

Kite's only incremental **nonblocking** suggestion: in a subsequent bounded experiment, make a few original per-block timing and browser GC/observer traces independently retrievable with immutable hashes. The 199,872,798 bytes of local raw JSONL and 28,099,683 bytes of traces/profiles are unshared; a small reduced JSON extract permits aggregate recomputation but not full raw-byte or all-step audit.

Axiom published [reconciliation comment `6965100611`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/17#issuecomment-6965100611): **GO for owner-authorized PR17 docs/evidence merge only**, keep Issue #11 OPEN. Explicitly no production CONFIG-admission limits, optimization, Worker/WASM selection, device/realtime certification or merge action by Axiom. Next owner-gated experiment: selected physical target/browser with defined load/refresh/budgets and repeated unchanged built-app plain vs observer file/synthetic controls.


## Verified owner merge and post-qualification state — 2026-11-17 Pacific

User reports [PR #17](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/17) merged; Axiom independently confirmed GitHub `merged=true`, `state=closed`, `merged_at=2026-11-18T00:24:59Z` (Nov 17 Pacific), accepted PR head `a5e75c9da8dd4799b1419c9c23b5dca76168326b`, merge commit `4ef3d2376f6de1a390024eb65cbad6beab12eadb`. The application `main` currently points to this SHA. Both the AP117-005A (#15) design, AP117-005B (#16) measurement harness, and ISSUE11-QUAL-01 (#17) evidence report are integrated. No open PRs at the time checked.

Current open issues include [#11](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11) work/GC operating-envelope admission, [#14](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14) deferred source-revision/PSD recovery, [#10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) consumer handle/receipt and terminal-drain design gate, and design coordination [#8](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8), [#7](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/7), [#6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6). The issue listings are planning state, not evidence that previously implemented contracts were undone. Issue #14 is explicitly deferred and must not be silently folded into #11.

**Axiom next recommendation:** owner select one real target device/browser and define explicit device/loading/source/refresh, service and frame/GC/memory requirements; run the existing unchanged built application in repeated visible-foreground file/synthetic trials with plain/observer controls. If owner cannot supply deployment hardware/budgets, pause the production-admission aspect of #11 rather than guessing thresholds; a separately scoped **design-only** checkpoint for recovery Issue #14 or presentation Issue #7 can advance independently. Retain CPU/GC/heap and capture/concurrency admissions as not qualified. Do not claim the author-reported reduced extract certifies a real-time/safe device envelope. Axiom did not merge, close Issue #11, or authorize a technology choice.

---
schema: 1
id: 2026-11-15-ap117-pr12-psd-lifecycle-hc05
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-pr12-psd-lifecycle-review-session
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint PR #12 CODEX-AP117-003 exact head 0880fc8df9182cce9ed2c645e324a2d291375281; accepted/main base 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; Issues #6 and #10, docs/AP117_003_PSD_CONSUMER.md, application AGENTS.md; Harbor home agents/harbor-v1@a55a3addf1e29ab26d8e1b3ab8544d32345c553b; exact-source isolated V8 checks; CI run 43789892097, attributable to GitHub Actions."
---

# Harbor — AP117-003 PR #12 independent PSD continuity, EOF, and recovery review (HC05)

**Repository:** `cosmicdance-4-2-0/ap_117_KESTREL`; [PR #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12), **reviewed head** `0880fc8df9182cce9ed2c645e324a2d291375281`.  
**Base:** accepted/main `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f` (accepted AP117-002 complete-spectrum delivery).  
**Harbor own source before review:** `KestrelGaming/agents/harbor-v1@a55a3addf1e29ab26d8e1b3ab8544d32345c553b`.  
**Outcome:** **PASS — Harbor lifecycle/EOF remit, no blocking defect reproduced**. Review only; PR remains draft and owner/other-specialist acceptance is independent. No application code, contract, merge, deployment or another agent's memory changed.

## Summary

AP117-003 introduces an **opt-in headless synchronous PSD consumer** receiving records through the **actual bound complete-spectrum subscription** rather than by adopting caller-supplied receipts or polling `readCurrent()`. This responds to [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) and [Issue #6](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6). The proposed `ap117.psd/1` and `ap117.psd-delivery/1` schemas remain candidates, not adopted public interfaces. The PR adds six files only (producer, CP2, FFT, FrameHost and host rendering unchanged).

**Harbor's material conclusion:** A derived observation must be accepted only after the bound subscription's live generation/continuity and ordered cursor are checked; a previously returned ready result may remain **historically valid** but must lose **live continuous readiness** after a fence. Producer EOF and consumer drain are distinct. Under source-executed checks, the new processor satisfies those properties; after overflow, invalidation or parameter segmentation, resumed PSD coverage begins only **after** explicit `resync`, never by pretending missed windows were analyzed.

**No severity-critical or blocking finding in assigned scope.**

## Evidence

### Inspected exact-head sources

- [`src/analysis/psd-processor.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/src/analysis/psd-processor.js) (all 304-ish lines): constructor captures `take/readStatus/resync/dispose` from supplied handle; checks `ap117.spectrum-delivery/1` provenance, BigInt ordinal, generation, continuation and spectrum window fingerprints; computes frozen PSD; implements sticky first/latest diagnostic reasons, `reset`, explicit `resync({source})`, `dispose`, distinct `readStatus` and `readCurrent`.
- [`src/analysis/spectrum-stream.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/src/analysis/spectrum-stream.js), [`src/analysis/spectrum-delivery.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/src/analysis/spectrum-delivery.js), [`src/analysis/fft-amplitude.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/src/analysis/fft-amplitude.js): accepted producer + FFT source used by the independent probes, not modified in this PR.
- [`tests/psd-lifecycle.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-lifecycle.test.js), [`tests/psd-boundary.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-boundary.test.js), [`tests/psd-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-integration.test.js), [`tests/psd-math.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/tests/psd-math.test.js), [`docs/AP117_003_PSD_CONSUMER.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/docs/AP117_003_PSD_CONSUMER.md), [AGENTS.md](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/0880fc8df9182cce9ed2c645e324a2d291375281/AGENTS.md), Issues #6 and #10, PR changed-file list/diff, and original Harbor [PR #9 evidence](2026-11-15-ap117-pr9-lifecycle-review-hc04.md).

### Independently executed negative and positive checks

**Harness fidelity:** Used GitHub connector to fetch the exact head's `fft-amplitude.js`, `spectrum-delivery.js`, `spectrum-stream.js`, and `psd-processor.js`; evaluated production source in an isolated V8 tool with only ESM import/export syntax replaced by explicit injected dependencies. No application implementation modification or temporary commit. Synthetic fully fingerprinted `ap117.measurement/2` envelopes and Float32 PCM with Hann M8/H4/N8 and explicit production-style delivery ceilings. These are **source-executed focused checks, not the Node test runner or a live browser**.

**Run 1: 14/14 PASS, 0 FAIL:**
1. One 20-frame final input produces four ordered PSD spans `[0,8),[4,12),[8,16),[12,20)`; processor `readStatus` remains open while draining; only `take().ended` establishes drained state and prior ready remains historical.
2. Short final 7 samples has no manufactured PSD ready; terminal `ended`.
3. 8+2 partial final tail produces only `[0,8)`, then ended.
4. Capacity-2 consumer breaks on atomic 4-window batch while cap-4 peer succeeds; sticky overrun, no old backlog on resync; next real window starts at current frontier.
5. Cached ready after a newer unseen ready is fenced by source reset; explicit `resync({source: newEpoch})` allows only genuinely new epoch coverage.
6. Same-epoch source-revision change forfeits first-batch completions and requires descriptor-aware resync, after which new windows are delivered.
7. Invalidate while assembler retains partial PCM fences PSD; after resync a legitimately completed overlapping window is accepted with its original source-frame span.
8. Ready-after-final input fails closed; processor remains terminal after resync until producer reset.
9. External subscription take is detected as `delivery-order-gap`.
10. External subscription resync is detected as `upstream-continuity-changed`.
11. Local processor reset produces sticky break until explicit resync.
12. Producer terminal dispose revokes readiness and cannot reopen; old ready remains historic data.
13. Processor dispose closes its owned handle and is terminal.
14. `take(foreignReceipt)` throws before consuming the real bound queue.

**Run 2: 6/6 PASS, 0 FAIL:**
1. Distinct producer handles with identical first-generation/ordinal stamps; `take(receiptA)` rejected before changing B's queue; B obtains its own observation.
2. A later B subscription at same provider frontier does not receive A's earlier window, but receives its next actual window.
3. Sticky subscriber overrun first cause remains while successive producer reset/invalidation update latest cause; explicit resync clears.
4. A forged bad-unit second observation withdraws derived PSD readiness while spectrum producer remains healthy.
5. Source-epoch chronology fault is classified as **upstream**, not a local subscriber overflow.
6. A synchronous pull wrapper invalidating the producer after taking an item prevents publication of a stale derived PSD.

**Total observed in two independent targeted source-execution batches: 20 PASS / 0 FAIL.** These are synthetic *direct producer adapters* and consumer controls, not the exact CP2 end-to-end harness. Production test source covers both legal CP2 partitions with actual pipeline; I inspected it but did not re-execute it independently.

**CI and environment:** [GitHub Actions run 43789892097](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43789892097) has exact `head_sha=0880fc8df9182cce9ed2c645e324a2d291375281`, completed `conclusion=success`, including Node tests, build, HTML and Chromium steps. Implementer reports `npm run verify` with 119/119 tests and passing HTML/browser gates; those are **attributed CI/implementer evidence**, not independently rerun by Harbor. Local `git ls-remote https://github.com/cosmicdance-4-2-0/ap_117_KESTREL.git HEAD` failed: `Could not resolve host: github.com`. No local `npm run verify`, full test suite, browser BFCache navigation, hardware/GC timing or physical PSD calibration was run.

### Ranked findings / boundaries

**Blockers: NONE found by Harbor.**

1. **Nonblocking product boundary:** The last `readCurrent()` PSD can remain a frozen `ready` historical observation after clean EOF, while `readStatus().drained` only becomes true once `take().ended` is consumed. A future panel must combine PSD value + consumer continuity + terminal drain; never label last historic PSD as ongoing live acquisition. This is documented intentional behavior, not a defect.
2. **Nonblocking integration responsibility:** The host must supply the correct exclusive subscription and, at source/epoch/revision change, explicitly authorize `resync({source})`. Matching generation/ordinal stamps are not cross-producer authentication. No arbitrary same-realm plugin trust or async consumer after-yield support is implied; future asynchronous code needs its own revalidation before commit.
3. **Nonblocking coverage loss:** A first changed-parameter batch can contain legitimately completed FFT windows but still be forfeited when the producer fences; PSD must remain broken until explicit frontier resync. Missing coverage is not reconstructed from latest. This was source-executed.
4. **Unproven operating envelope:** Processor's claimed bounded work is separate from upstream max FFT/hop1 allocation churn. Issue #11 performance/resource study remains open; no main-thread deadline or hardware/GC guarantee.
5. **Schema/authority:** `ap117.psd/1` and `ap117.psd-delivery/1` are candidate schema names. A successful test suite is not owner ratification, production rollout or merge authorization. No renderer, plugin bus, PSD panel, separate FFT or additional PCM acquisition was added.

**Required corrections:** None in Harbor's assigned exact-head remit. Re-run this review on any changed PR head. Keep other specialists' independent findings and owner acceptance separate.

## Revisit when

PR #12 head changes or another engineer finds a concrete counterexample; the owner adopts a PSD schema/consumer contract; an asynchronous or graphical consumer is added; a new source/epoch reconfiguration API is proposed; or operating-envelope work under Issue #11 proceeds. Revalidate published API semantics and exact revisions; never promote this source-only isolated pass to device- or browser-certified behavior.

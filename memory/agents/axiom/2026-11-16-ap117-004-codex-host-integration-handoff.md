---
schema: 1
id: 2026-11-16-ap117-004-codex-host-integration-handoff
kind: handoff
scope: agent:axiom
status: dispatched
evidence: observed
author: axiom-codex-004-delegation
created: 2026-11-16
updated: 2026-11-16
sources: "Auralprint 117 accepted main bdead48ae672ed6834eae274c8876944a79104bc; source AGENTS.md, src/main.js, src/config.js, src/analysis/{pipeline,spectrum-stream,spectrum-delivery,psd-processor}.js, docs AP117_002 and AP117_003, tests; Issue #10 approved checkpoint plan 6911230503; Codex implementation work order on Issue #10 comment 6911643686; Issue #11 performance and Issue #7 CP3-B2 deferred."
---

# AP117-004 — Codex handoff: real host-owned PSD consumption

## Owner request, baseline, release of implementation work

Owner agreed to Axiom's ordering **Issue #10 actual host PSD integration, then Issue #11 measured CPU/GC operating envelope**, reviewed proposed checkpoint and explicitly requested a Codex handoff. GitHub verified `main@bdead48ae672ed6834eae274c8876944a79104bc` unchanged; merged PR #12 headless PSD consumer. Axiom produced conversation downloadable Markdown `CODEX_AP117_004_Host_Owned_PSD_Integration_Handoff.md` and published [complete source-pinned implementation authorization, Issue #10 comment 6911643686](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10#issuecomment-6911643686), following [Issue #10 checkpoint design comment 6911230503](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10#issuecomment-6911230503).

**Status:** Handoff prepared, issued for owner relay. Codex independent sandbox work not yet observed. **No Auralprint production code changes, implementation PR, merge or release by Axiom.**

## Scope and binding semantics

- Implement one narrow `host-owned PSD session` factory. Its only input is the **actual spectrum producer** (plus accepted CP2 source descriptor, CONFIG spectrum and capacity), from which it **itself creates** one native `spectrum.subscribeComplete({capacityObservations})` and passes it directly/exclusively to accepted `createPsdProcessor`. No arbitrary caller-supplied subscription, no detached receipt input, no hostile plugin authentication/global registry. The testable host boundary cannot mis-pair externally supplied subscription methods because it does not accept them. Trust in selecting the right producer remains a host responsibility.
- On the first validated CP2 ready publication, derive source/channel/sample rate/epoch/revision/tap/clock domain from `measurement.sampleSpan` plus `measurement.channelId`, **subscribe before** `spectrum.accept(publication)` on that same block; thereafter one existing CP2 read and one producer accept per advance; finite PSD drain after every successful accept.
- Add one named CONFIG PSD subscription capacity (suggested 4; must match accepted producer admission); derive a finite drain limit from that value, stop on `empty/break/ended/closed`. Bounded per-session retained last PSD and processed count; no time inference or latest-only spectra used as replays.
- Preserve source-end-with-queued-final vs PSD actually drained; distinguish first reason/newest cause, source/consumer/subscriber failure, historical cached values, and unrecoverable coverage loss from `resync` or changed sourceRevision. Synthetic slider invalidation is an authorized revision transition but can forfeit first new-segment batch; host records gap before authorized frontier resync. Unexpected failure never silently resyncs.
- Same host lifecycle: pause/resume preserve valid epoch, new WAV/channel/replay/source replacement/import failure/cancel/late completion dispose old PSD and rebind from next validated ready; pagehide/BFCache, final render fault replay-required, global rendering policy unchanged.
- Minimal accessible textual diagnostic adjacent to SpectrumScope displays per-session complete-window count, last PSD scientific span, consumer state and gaps, but **no PSD chart**, third Canvas, new renderer frame/scheduler or changes to existing FFT/RMS UI semantics.

## Required reproducible controls

- Current `M1024/H512` WAV 2048 frames → **three** PSD windows `[0,1024),[512,1536),[1024,2048)`, all final results drained; WAV 481 → zero PSD (RMS exists).
- Legal Gauge `M8/H4/N8` final20 vs five4 blocks → four equal PSD windows with true completing source revisions; cap4 complete, cap2 explicit sticky overflow.
- Same-source-descriptor two actual producers and staggered subscribers, colliding local numeric stamps: no cross-subscription injection via host's supported API; correctly report limitations for *wrong producer passed by host*, not claimed authentication. Preserve same-handle historical eligibility.
- Slider revision first-batch fence/forfeiture, source epoch/channel/replay/import cancellation and late result, post-final rendering fault, EOF backlog, recovery, pagehide/BFCache and separate failure scopes.
- Test **actual `src/main.js` integration**, not just standalone PSD tests. No extra PCM read/FFT, one FrameHost/two Canvas. Current Chrome/offline/static HTML, existing CP2/CP3-A and accepted PSD math remain covered.

## Delivery

Codex may implement/test/commit in isolated branch, **push its branch and open one draft PR** against verified main. No merge, deployment, release, protected-history rewriting, other agent memories, generic broker, new FFT/math, CP3-B2 PSD view or Issue #11 optimization. Source exact head/base and tests with evidence. Axiom dispatches Flint/Latch/Harbor/Mothlight/Gauge/Kite for independent exact-head review; owner decides merge. Contract conflict/real silent data loss → stop and report, not silent workaround.

## Revisit when

Codex reports a draft PR, source baseline moves, an accepted lifecycle contract requires redesign, true host-subscription pairing cannot be ensured in a small factory, or owner changes scope.

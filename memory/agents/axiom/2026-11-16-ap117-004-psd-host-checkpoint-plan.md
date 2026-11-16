---
schema: 1
id: 2026-11-16-ap117-004-psd-host-checkpoint-plan
kind: design
scope: agent:axiom
status: proposed
evidence: observed
author: axiom-psd-host-design-proposal
created: 2026-11-16
updated: 2026-11-16
sources: "Auralprint main bdead48ae672ed6834eae274c8876944a79104bc after merged PR12; issue10 proposal 6911230503; issues 7/10/11; AGENTS.md, docs/CHECKPOINTS.md, docs/AP117_002_COMPLETE_SPECTRUM_DELIVERY.md, docs/AP117_003_PSD_CONSUMER.md; src/main.js, src/config.js, src/analysis/pipeline.js, spectrum-stream.js, spectrum-delivery.js, psd-processor.js, src/audio synthetic-sine.js/pcm-buffer-source.js, index.html, tests/app-integration.test.js and browser-smoke.mjs."
---

# Auralprint 117 — AP117-004 / CP3-B1-H1 proposed host-owned PSD consumption checkpoint

## Source verification

Owner confirms order: **Issue #10 real application PSD consumer host integration, then Issue #11 operating-envelope/GC validation.** GitHub accepted baseline `main@bdead48ae672ed6834eae274c8876944a79104bc` from owner-merged PR #12. Issue #10 remains open. Inspected actual main app composition, CP2 pipeline/sources, spectrum queue/producer/PSD consumer, source file/test/HTML, and AGENTS/checkpoint contract. Published detailed **design-only, non-implementation authorization** on [Issue #10 comment 6911230503](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10#issuecomment-6911230503).

## Proposed engineering boundary

Proposed **CP3-B1-H1 / AP117-004**: small **host-owned PSD session binding** for actual `src/main.js` preserving one CP2 source read and `spectrum.accept` per block, one existing FrameHost/2 Canvas. A new single-purpose host helper owns construction and disposes exactly one real `spectrum.subscribeComplete` handle, passes original native handle directly/exclusively to `createPsdProcessor`; generic function-shaped wrapper authentication and plugin sandbox deliberately excluded. Host obtains authorized source descriptor from actual accepted CP2 ready metadata (including measurement-level channel ID), subscribes **before** calling `spectrum.accept` on first ready, and drains bounded PSD results **after** accept. No historical replay or latest-only analysis poll. Explicit CONFIG-defined queue capacity suggested 4 (current B480/H512 completes ≤1 window/block), actual resource ceiling remains delivery admission. Consumer produces own PSD status currentness; source end with queued final observations is not downstream drained; final publish must drain before stopping timer.

Lifecycle: pause/resume preserves source, replacement/channel/replay/import resets/disposes old session, synthetic parameter revision fence yields explicit **lost-coverage status**, not hidden auto-resync; sourceRevision authorized descriptor transition at frontier after recording gap. Unexpected overrun sticky until deliberate handling; do not poison separate RMS/FFT solely for consumer break, but upstream/render failure retains existing global failure policy, including EOF — REPLAY REQUIRED, stale imports, pagehide/BFCache. Protect same-handle history while continuity valid; wrong-live-handle construction negative required by Issue #10 in production host path, not just `take(receiptA)` rejection.

**Small visible diagnostic suggested** adjacent to current spectrum readings: processed PSD window count, latest scientific source span, producer ended but PSD drain pending vs actually drained, explicit break reason. Not a PSD graph, third canvas, full numerical axis or B2 design. Avoid high-frequency live region announcements. Alternative fully headless host seam allowed only with actual `main.js` integration verification and no invisible unbounded work; owner/design review to decide. Honest scientific semantics and presentation/source clocks remain independent. Current HTML only renders two Canvas2D scopes.

Required acceptance cases: synthetic normal continuous windows; 2048-frame WAV produces three PSD windows `[0,1024),[512,1536),[1024,2048)`; 481-frame WAV produces zero PSD windows; special legal M8/H4 final20 vs five 4 partitions produce four and correct finishing revisions; cap2 overflow vs cap4 full; wrong producer or staggered subscription handle (same local stamps), genuine historical same-handle; pause, parameter edit lost first segment, file/channels/source epochs/replay, final drain, replay-required render fault, cancellation, BFCache and disposal; CI Node/static/html/browser and scientific regression. No extra PCM/FFT or scheduler.

## Key risk and open choices

1. Ensure **no original CP2-ready batch is missed** before new subscriber creation. Subscribe on first *ready* before producer.accept, not after first complete spectrum. Do not try to predict source descriptor from UI labels; accepted CP2 uses measurement-level channel and sampleSpan.
2. PSD producer `delivery.commit({final:true})` is terminal on the final ready block; host must drain before `stop("complete")` (no extra advance guaranteed).
3. `spectrum.invalidate` on synthetic slider fences and retains partial input; later sourceRevision transition can forfeit initial new-parameter completed windows. Host must report and preserve gaps before any authorized resync and must not silently reconstruct from latest spectrum.
4. Bounded drain should use an explicit CONFIG count and stop on `empty/break/ended`, not assume all work fits one animation frame. Current app B=480, H=512; future larger bursts deliberately tested for truthful capacity-2 overrun; global FFT/GC work envelope remains Issue11.
5. Trusted host correct native handle construction is a **host architecture responsibility**. Don't assert method function existence or equal generation/continuity stamps cryptographically prove the intended provenance.

## Authority/next action

Owner asked for a plan, not implementation. **No code/PR/merge** has been authorized or started. First challenge candidate with Flint/Latch (binding/ownership), Harbor (EOF/params/replay/faults), Mothlight (status diagnostic), Kite (bounded drain and limits), Gauge (numerical wording/source lineage). Then Axiom reconciles owner-approved interface and delegates one Codex implementation task: task branch, tests, **push and open draft PR**, preserve current baseline, no auto merge or deployments. After accepted host checkpoint, pursue Issue #11 measured operating envelope; B2 presentation stays separate Issue #7.

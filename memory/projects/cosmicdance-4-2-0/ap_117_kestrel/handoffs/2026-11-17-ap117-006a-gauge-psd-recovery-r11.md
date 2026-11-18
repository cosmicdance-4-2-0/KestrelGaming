---
schema: 1
id: 2026-11-17-ap117-006a-gauge-psd-recovery-r11
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: draft
evidence: inferred
author: chatgpt-gauge-session
created: 2026-11-17
updated: 2026-11-17
sources: "AP117 Issue #14 handoff comment 6965232646; exact Auralprint main 4ef3d2376f6de1a390024eb65cbad6beab12eadb; Gauge home ee15365162ed18afe02126368da3136c349395b5; source inspection and independent fixture arithmetic, no application code or full runtime tests run."
---

# Gauge — AP117-006A independent PSD recovery design review

**Outcome: COMPLETE (design review only); recommendation: B with source-clock and subscription-frontier receipt, conditional on explicit owner approval.** No implementation, release, merge, Issue #11 edit, automatic recovery or independent executable app tests performed. Authorship is an attributed Gauge-context ChatGPT engineering review, not a cryptographically authenticated agent instance.

**Assignment:** [Axiom's AP117-006A source-pinned Issue #14 handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965232646). **Target source:** [Auralprint main at 4ef3d2376f6de1a390024eb65cbad6beab12eadb](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/4ef3d2376f6de1a390024eb65cbad6beab12eadb), confirmed current on 2026-11-17. Prior related Gauge [PR #13 handoff](2026-11-16-ap117-pr13-gauge-host-chronology-r10.md) is historical, not current proof.

## Summary

**Prefer B** (explicit new same-epoch PSD association for one exact authorized synthetic revision) over A (explicit restart with new source epoch) *only if* the recovery contract includes independently auditable attachment and sample-support provenance. B must not be an implicit `resync()`, backfill, raw-receipt path, generic broker, or repetition after arbitrary consumer faults. A is fully defensible when least risk matters more than in-epoch continuation.

**Two producer fences exist**: source edit calls `spectrum.invalidate` at [main.js:159–168](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/main.js#L159-L168), and first accepted ready CP2 block with new `sourceRevision` invokes `delivery.fence` after FFT assembly at [spectrum-stream.js:127–193](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/analysis/spectrum-stream.js#L127-L193). `retain = !parametersChanged && delivery.prepare(count)` means first-transition-block completions were computed but not retained; attaching before that accept inevitably creates a doomed native subscriber. Failed accept resets/fences rather than establishing recovery.

**The additional Gauge trap: attachment time differs from sample support.** For an already-running M8/H4 FFT, prior revision0 [0,8) completed; revision1 accepts [8,20) and completes new windows [8,16) and [12,20), both unrecoverable in the transition block. The post-accept delivery frontier is **2** in its new generation; a new subscription attached at source cursor **20** begins after ordinal2. Next accepted [20,24) completes ordinal3 on **[16,24)**. Its FFT window contains four samples acquired **before** subscription attachment. This is a legitimate future completion, but **not** an all-post-click input interval. The same distinction arises with B480/M1024 even when the first transition block completes zero windows: a later eligible FFT window includes the first transition block's pre-attachment PCM.

## Evidence and invariants

**Inspected source blobs at the target commit:** `src/main.js` 6ff041e3e4bc8f0abd046ec52205a119a545f772; `src/analysis/spectrum-stream.js` 4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc; `src/analysis/spectrum-delivery.js` ef19cd748de41226ab0cd8375949e278f7aeb76f; `src/host/psd-session.js` 005e8f77fd7d71e5be51780a6cdbefa525bb2377; `src/analysis/psd-processor.js` 1f3937cbdaf77514c435da30879975e6a13f16ef; `src/audio/synthetic-sine.js` 77f48d03488b888236834530e9910b04780b6af3; `src/config.js` c5b692a2d984f3ba0f0c863048835e5e9617da70; `tests/app-integration.test.js` 42b81fb8f42bc683e0e3b7444d6370744109f122; `tests/psd-session.test.js` cae8b889ff20a6694e6346f02fdd41decea45242; `docs/AP117_004_HOST_PSD_SESSION.md` 6741dd16dbed6eb8c55d772bd5165955a28472ae; read Issue #10's native-handle/terminal-drain rules, Issue #7's measurement/presentation boundary, and Issue #11's distinct performance gate. No peer AP117-006A reviews were read.

**Minimum B transition**: (1) trusted synthetic edit records the *actual* source identity, epoch, new revision and the explicit requested recovery action (not a latest display stamp); (2) if the new revision has not passed a successful `spectrum.accept(ready)`, remain `pending-transition` with no new subscription; (3) accept/settle both fences before attachment; (4) require same authorized source identity/revision and an open, nonfaulted nonfinal producer, and no intervening new edit/source replacement; (5) dispose broken previous handle, preserve one immutable historical **summary** (not a second dense PSD store); (6) create a new host-bound native session against the actual producer and trusted CP2 descriptor; (7) record new delivery generation, **attachment completion ordinal frontier**, source cursor/epoch/revision, first eligible completion ordinal and first delivered PSD half-open span. Never infer native authority from matching stamps. No app changes are authorized here.

**Loss/meaning must be split**: (a) source-revision comparability fence even with contiguous PCM samples; (b) discarded pre-boundary partial FFT and unobserved completed FFT ordinals (post-fence count can be read from that generation's frontier, not from pixels); (c) possible pre-attachment PCM inside a post-attachment completion's FFT support; (d) draw coalescing, which is **not** scientific loss. Mark unknown quantity as unknown, not zero. New segment `current` only after a genuinely derived eligible PSD, not simply because a session subscribed. Old `lastSpan` remains explicitly historical; its span can overlap a new span without bridging continuity. Count/schema are per segment and source description. Future visualization must distinguish sample support, attachment and completed observation and must not label this as a continuous time series.

**Sticky failure and resource boundaries**: a B recovery action cannot repurpose an unknown source-revision change, invalid CP2, render fault, disposal, producer failure or subscriber overrun as authorized new input. A second genuine setter change before attach invalidates the original exact-revision intent, including while paused. A source transition/replay/import/channel change invalidates pending and owns its own new epoch. At EOF, do not attach an ended producer; any existing queued final observations drain until the real consumer returns `ended`, not merely producer `upstream.ended`. Short EOF yields no fabricated window. Current `CONFIG.psd.capacityObservations=4` remains the admitted bound; one large accept producing >4 completions must break atomically, not silently skip or relabel. Preserve single source read, single original FFT, one timer/FrameHost, numerical `ap117.spectrum/1` and `ap117.psd/1`, and no Issue #11 change.

**Important host-state seam**: `main.js:129–130` clears `authorizedSourceRevision` when the first new ready CP2 publication is observed, *before* the producer `accept`. This existing transient variable cannot later prove the edit was authorized for an explicit click-after-transition recovery. B needs a separate bounded trusted edit/intent receipt; never infer permission solely from `source.getSettings()` or a current descriptor. The attachment frontier identifies missing **completions**, not a complete list of missing sample supports.

## Smallest discriminating future tests — proposed, NOT executed

1. **Double fence**: M8/H4 old [0,8), authorized edit, revision1 [8,20) with two completed windows, pending B action before accept. No attachment before accept. Afterwards generation and frontier2; next [20,24) delivers exactly ordinal3 [16,24); 2 preceding completions are marked missed; four pre-attachment samples are labeled input support. Verify a naive early subscriber breaks.
2. **Zero-completion transition**: B480/M1024 first revised block completes zero windows; post-transition attachment is valid, but first later window's start is earlier than the attachment cursor. Zero missing completions does not imply all-post-click samples or scientifically continuous revision history.
3. **Repeated edits and trust**: revision1 pending followed by genuine revision2 rejects stale intent; no-op change neither fences nor silently authorizes; mismatched source/epoch/channel/tap/clock, unknown revision or wrong originating handle rejects despite matching generation/ordinal numbers.
4. **Failure & terminal**: error in first transition accept, pause/resume, render fault, cancel/import, source/channel/replay, pagehide/BFCache, short EOF and final queued 4 windows each follow bounded explicit fail/terminal rules; no auto-attach after EOF, no false current output and real consumer drain to `ended`.
5. **Capacity & projection**: capacity2 vs 4 with four committed windows shows atomic sticky overrun, no partial 'current' claim, first/newest cause retained; render coalescing does not change scientific completion or gap count.
6. **No duplicate work**: instrument actual source reads, accepted CP2 blocks, producer FFTs, native subscription count, drain calls and FrameHost timers before/after eligible B; assert one PCM read/accept/FFT for each original completed window and no separate scheduler/broker.

**No tests run here.** The two-window M8/H4 arithmetic above is an independently derived source-geometry prediction, not an observed execution of the app or proposed recovery implementation.

## Dissent / recommendation

A is a lower-risk, truthful and already-existing recovery path; improving accessible explicit controls alone is a legitimate minimal release. I **favor B** only because A prevents scientific in-epoch continuation after an authorized, ordinary source edit and forces resetting the sample clock. Axiom's B is not yet an implementable contract without an explicit edit-authentication lifetime, post-fence admission gate, two-dimensional loss report and support-versus-attachment semantics. There is no need for a general journal, PSD schema change, third Canvas or Issue #11 refactor. **Owner must approve a bounded AP117-006A contract before implementation.** Preserve other reviewers' future dissent without pretending consensus.

## Revisit when

Axiom reconciles independent reviews, the owner decides A vs B or a narrower policy, a formal transition receipt and observation-loss semantics are specified, or future code/tests materially change either fence or trusted host association. Re-pin current source at that time; this is a draft independent design opinion, not an accepted runtime guarantee.

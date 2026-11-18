---
schema: 1
id: 2026-11-17-ap117-006a-gauge-recovery-executed-fences-c62e
kind: handoff
scope: agent:axiom
status: draft
evidence: observed
author: axiom-issue14-gauge-followup-2026-11-17
created: 2026-11-17
updated: 2026-11-17
sources: "Gauge Issue #14 comment 6965413113, Axiom existing source-pinned response 6965473021 and prior Issue14 agent record; current Auralprint main@4ef3d2376f6de1a390024eb65cbad6beab12eadb; exact source blobs spectrum-stream 4d60ad2fc85f2a9979c156d221130f1b7c1d2dfc, spectrum-delivery ef19cd748de41226ab0cd8375949e278f7aeb76f, psd-session 005e8f77fd7d71e5be51780a6cdbefa525bb2377, psd-processor 1f3937cbdaf77514c435da30879975e6a13f16ef, fft-amplitude ee35e0793aceb5eb9e3fc49d27f293a1719effc5; isolated exact-source V8 fixtures for M8/H4 and M1024/H512; no app changes or full suite."
---

# Axiom — AP117-006A Gauge reconciliation: executed double-fence and sample-support counterexamples

**Identity:** Axiom — The Geometer; [agent contract](../../../agents/axiom/AGENT.md); `KestrelGaming@agents/axiom-v1`. This is an attributed reviewer perspective, not independently authenticated model identity.  
**Assignment:** User asks for a concrete second look at Gauge's [Issue #14 G1–G5 review](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965413113). Axiom has **already** incorporated G1–G5 as *candidate constraints* at [issue comment 6965473021](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965473021) and the [previous design record](2026-11-17-ap117-issue14-recovery-design-006a-initial-4e5b.md). This report supplements rather than repeats that reconciliation.  
**Exact inspected source:** `cosmicdance-4-2-0/ap_117_KESTREL@4ef3d2376f6de1a390024eb65cbad6beab12eadb`, verified matching `main` at review.  
**Verdict:** **Option B — conditional design preference**, preserving A as explicitly permissible lower-risk fallback. **New nonnegotiable input-support bound and late-click settlement witness** must be in any B implementation acceptance. No current app defect alleged. No implementation authorized.

## Summary

Gauge is correct that subscription attachment and FFT input support are different clocks/events. A native subscription binds only future **completed windows**; it does not guarantee all samples in those windows were acquired after subscription attachment. A genuinely revised source may have pending FFT assembler data before B attaches; that data is valid *if and only if* it was collected after the **revision onset**. An early B subscription, created before the producer's second internal `source-parameters-changed` fence, is broken even though it was created after the host's initial immediate `invalidate()`.

**Sharpened invariant:** For every new-segment `ap117.psd/1`, `revisionStartFrame <= sampleSpan.startFrame < sampleSpan.endFrameExclusive`; `sampleSpan.startFrame` may be less than `attachSourceCursor`. `revisionStartFrame` is the start frame of the **first successfully accepted CP2 block with the new revision**, not the moment of click and not merely `attachFrontier`. B must retain or independently derive this truth from an authoritative host-issued transition witness, not infer it from equal generation/ordinal/source strings.

For a **late user click**, an edit authorization receipt alone is insufficient to verify that the producer's second fence settled. The host must also retain a bounded **successful-transition settlement witness** recorded *after* the accepted new-revision `spectrum.accept(publication)`, containing the selected source instance association, exact sourceId/epoch/revision, `revisionStartFrame`, accepted block end-frame, producer generation/frontier and whether producer is still open. A pending user intent can wait for the settlement witness; a click after settlement can attach immediately only when both witnesses still match the **same** selected source instance and revision. This is a minimal lifecycle record, not a general event bus or signed receipt.

## Evidence

### Exact source facts, not proposals

1. [`src/main.js:150–175`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/main.js#L150-L175): genuine setter increment records transient `authorizedSourceRevision`, invalidates pipeline/FFT; no-op does not. [`main.js:111–149`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/main.js#L111-L149): `admitPsd` clears that transient before next spectrum accept. This transient **cannot** authorize a later B click.
2. [`src/analysis/spectrum-stream.js:117–193`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/analysis/spectrum-stream.js#L117-L193): on real revision change, clear mixed-revision FFT partial assembly, compute all new-revision FFTs without staging retained windows, then `delivery.fence("source-parameters-changed")` and `delivery.commit([], completed)`. Only completed windows count, without backfill. This establishes `revisionStartFrame` as the first revised block's source `startFrame`.
3. [`src/analysis/spectrum-delivery.js:31–165`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/analysis/spectrum-delivery.js#L31-L165): each producer's generation/frontier and per-subscription continuity are local. A newly subscribed B may read the latest frontier but cannot take preceding completions; `ended` does not mean a subscriber queue was drained.
4. [`src/host/psd-session.js:11–133`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/4ef3d2376f6de1a390024eb65cbad6beab12eadb/src/host/psd-session.js#L11-L133): host owns native `subscribeComplete` and passes it directly to PSD consumer; only capacity-bounded `drain/readStatus/readCurrent/dispose` exposed. No native association is authenticated against an incorrectly selected/hostile producer; main's static selected producer is the trusted authority.

### Independently executed, source-pinned focused tests

Retrieved `psd-session.js`, `psd-processor.js`, `spectrum-stream.js`, `spectrum-delivery.js`, `fft-amplitude.js` from the exact pinned source. Changed only ESM import/export declarations into explicit dependency injection in a fresh V8 function scope. **Production algorithms unchanged.** Tests supply conforming finite CP2-style RMS-ready observations with explicit BigInt frame spans; **not** full running `main.js` or actual synthetic `pipeline.advance`.

| Controlled state and operation | Direct observed result |
| --- | --- |
| **G2 M8/H4**: initial revision0 `[0,8)`; immediately `invalidate()`; subscribe **too early** at generation2/frontier0, then accept revision1 block `[8,20)` | The early session is broken by second fence, with reason `source-parameters-changed` and generation3. |
| Attach **after** revised `[8,20)` has succeeded | Session enters `processing` at generation3/frontier2; source cursor20. |
| Accept subsequent revision1 `[20,24)` | New session obtains ordinal3 `[16,24)`: **four pre-attachment samples**, **zero pre-revision samples**. Earlier two completed ordinals 1–2 were not delivered to B. |
| **Default-scale geometry M1024/H512**: revision0 `[0,1024)`; invalidate; revision1 first block `[1024,1504)`, size480 | Early B breaks at second fence. Legitimate B attaches after successful accept at generation3/frontier0/source cursor1504. There were **zero** missed complete FFTs in this first revised block. |
| Accept further revision1 `[1504,1984)`, `[1984,2464)` | B's first delivered complete ordinal1 spans `[1024,2048)`, including **480 pre-attachment but zero pre-revision samples**. |

These are **actual source-factory executions** under controlled legal metadata, not a user experience demonstration and not a completed recovery feature. No application changes or full test suite were executed. The existing GitHub `main` HEAD was checked and matched the pinned SHA.

## Candidate B state and authority model (not ratified)

- **Edit receipt:** On a *genuine trusted setter transition*, save bounded host source instance association, previous/target revision, sourceId/epoch/channel/tap/clock/sampleRate, and a host-created edit sequence. A no-op creates no receipt; a second genuine edit invalidates the earlier target. Merely matching public strings or source getter snapshots is never an authorization proof.
- **Settlement witness:** On the **first accepted, successful** `spectrum.accept` for that target revision (after second fence), record `revisionStartFrame=acceptedCP2.sampleSpan.startFrame`, accepted-block end cursor, producer generation/frontier, and open/nonterminal status. If accept throws or completes with final/ended, don't allow attaching from that witness. Never determine settlement solely from `readCurrent().status === "ready"` or from `authorizedSourceRevision` (already cleared).
- **User recovery action:** Owner-preferred B requires an explicit user choice, with intended revision bound to the edit receipt. If no settlement yet, state `PENDING_FENCE`, no early subscription. When settlement observed and source still the same host-selected instance/revision, retire broken old session to **one historical immutable summary** and create the new native session. If user chooses after settlement, verify the retained witness and attach at the current producer frontier. A click with no valid edit or a no-op must not silently relabel an existing session.
- **New segment:** At native attach record `attachFrontier`, `attachSourceCursor`, generation, exact descriptor, `revisionStartFrame` and association reference. First eligible completed ordinal is `attachFrontier+1`. State remains `WAITING_FIRST_PSD` until a real valid observation; only then `ACTIVE`. Record actual `sampleSpan` and `inputSpectrum.completionOrdinal`; enforce `sampleSpan.startFrame >= revisionStartFrame`. Retain separate `missedCompletedOrdinalCount` (when justified), `firstWindowPreAttachSupportFrames` and **revision discontinuity**. Do not combine them into one misleading 'lost samples' number. Render coalescing is orthogonal.
- **Fail closed:** Any unknown revision, another genuine edit, source instance/epoch/channel switch, failed accept, producer/consumer fault, overrun, render failure, EOF/closed, replay/import/cancellation/pagehide cancels pending intent and bars auto-retarget. Preserve first/newest sticky failure reason, producer ended versus subscriber drained and immutable history; no automatic `resync`, catch-up or re-subscribe. First revision accept may complete several unretained windows; the recovered segment cannot claim them.
- **Capacity:** keep current `CONFIG.psd.capacityObservations=4` and producer budgets for the first experiment; if a legal post-attach atomic batch exceeds capacity, break visibly without partial PSD outputs. No second PCM read, FFT, analysis timer, extra Canvas or general plug-in registry.

## Alternatives, stop conditions and falsifiers

**A — explicit source restart:** No application semantic change, low risk, honest new epoch/clock; sacrifices same-epoch post-edit continuation and may be cumbersome. Keep as fallback if B's authorization/pending/fence/UX cannot be proved with minimal host state.

**B — explicit same-epoch new segment:** User-preferred and scientifically coherent with edit + successful-settlement witness, post-second-fence native attachment, bounded history, and distinct support/ordinal/revision semantics. **Conditional recommendation**, not automatic implementation. Has additional state and negative tests; if proof cannot distinguish a legitimately revised source from a malicious/wrongly selected source, B must not claim stronger trust than the existing host.

**Smallest future acceptance suite (NOT EXECUTED):**
1. Two-fence M8/H4 test with early rejected/broken session and late ordinal3 `[16,24)`; assert `revisionStartFrame=8`, `attachCursor=20`, `preAttachSupport=4`, `preRevisionSupport=0`, two completed ordinals forfeited.
2. M1024/H512 revised block480 zero-completion case; first eligible `[1024,2048)` with 480 preattach samples and **zero missed completions**, but explicit revision discontinuity.
3. Early click -> pending -> successful acceptance -> attached; late click after settlement -> attach; no-op/rapid second edit and stale source instance/epoch/handle -> rejected or canceled, no fabricated association.
4. First revised accept throws or fails; late short EOF or producer terminal; cap2/4 atomic burst; subscription revoked and source-replaced, paused/replay/channel/import/pagehide; no auto-retarget, no fake current science.
5. Real host test: no additional `readBlock`, FFT or timer; explicit UI text distinguishes 'pending transition', 'waiting for first PSD', 'historical', 'revision break', 'forfeited completed windows' and 'overlapping pre-attach input'; no claim of physical noise-floor or nonaveraged PSD as a continuous stream.
6. Independent negative oracle should **mutate** the implementation to attach before second fence and ensure it fails, and force a mixed-revision FFT window to ensure the revisionStart invariant detects it.

**Decision authority:** User has expressed preference for B (prior Axiom record); no owner-approved final semantic contract or AP117-006B implementation handoff exists in this review. Issue #11 remains separate/parked; Issues #10 and #7 must preserve consumer origin and presentation semantics.

## Outcome

**COMPLETE — Axiom source-executed response/addendum to Gauge G1–G5; design only.** The existing Axiom candidate constraints remain, and a new condition was added: revision-start provenance must be an independent **lower bound on every new-segment FFT/PSD sample span**, with a **settlement witness** durable enough to authorize a late click. No application code, Issue #11, other agent memory, or owner policy was changed. The source-pinned report may be posted to Issue #14 for specialist reconciliation; still subject to owner adoption.

## Revisit when

Owner approves a concrete B control/UX and interface, a new recovery implementation checkpoint is authorized, an agent demonstrates that the additional settlement witness is redundant but equally verifiable, a mutation shows a pre-revision frame entering B, or the A/B choice is reopened with actual user trials.

---
schema: 1
id: 2026-11-17-ap117-issue14-recovery-design-006a-initial-4e5b
kind: design
scope: agent:axiom
status: draft
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint main@4ef3d2376f6de1a390024eb65cbad6beab12eadb; Issue #11 owner parking comment 6965209785; Issue #14 source-pinned initial design comment 6965232646; Issue #10; src/main.js; src/analysis/spectrum-stream.js; src/analysis/spectrum-delivery.js; src/analysis/psd-processor.js; src/host/psd-session.js; src/audio/synthetic-sine.js; tests/app-integration.test.js; docs/AP117_004_HOST_PSD_SESSION.md."
---

# AP117-006A — Issue #14 initial recovery design, after owner parks Issue #11

## Owner scheduling / source pin

User directed: “I think we should stick a pin in #11 and come back to it later. Lets tackle #14 instead.” Verified Auralprint `main@4ef3d2376f6de1a390024eb65cbad6beab12eadb` with PR #15 (005A design), #16 (005B benchmark harness) and #17 (bounded qualification docs) integrated; #11 still open, performance admission unapproved. Published [owner scheduling checkpoint on Issue #11](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11#issuecomment-6965209785): **parked**, not closed. Preserved evidence. No new device/performance/config work authorized.

Read the full Issue #14 (previously deferred), Issue #10, source producer/delivery/processor/host/host session, current app integration tests, original host design. Published [AP117-006A source-pinned initial design](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965232646). **Design only, not code or adoption authorization.**

## Crucial observed seam / second fence

- Genuine synthetic amplitude or frequency setter increments `sourceRevision`; host invalidates CP2 and spectrum immediately (spectrum.invalidate() calls `delivery.fence(...,{reopen:false})`), causing old PSD session to become broken/historical. No-op input preserves revision and session.
- On first `spectrum.accept(publication)` of a different sourceRevision, producer code sets `parametersChanged`, clears mixed-revision assembler, sets `retain=false`, computes any complete new revision FFTs but does NOT retain them and calls `delivery.fence("source-parameters-changed")` **again**, then `commit(staged=[],completed,final)`. This means any fresh subscription made *before* this transition accept would itself immediately break; its first-block completions are **not recoverable** via later new subscription. For defaults B480/M1024 first new block has zero new-revision completions; other legal geometries may complete one/more. This is a contract-design hazard for a naive automatic re-subscription patch.
- Host `admitPsd(publication)` currently executes before `spectrum.accept` for initial first-block coverage, and intentionally lacks any resync API; `createPsdSession()` owns exact native originating handle. Existing app test explicitly proves hold-on-break, no-op, unknown revision, source restart, lifecycle. Issue14 must preserve these until owner-approved replacement tests.

## Alternatives and Axiom provisional recommendation

**A — restart source with clearer explicit controls.** Unmodified policy and lowest risk, new source epoch and sample clock; limited usability. **B — explicit, user-authorized separate same-epoch PSD segment** after genuine revision. Preserve original historical segment and labeled discontinuity; bind user intent to exact selected sourceId/epoch/revision; after producer has consumed new-revision fence, admit a fresh native session for future-only completions. If user acts before fence, intent pending. Old session disposed without pretending restored coverage. If new revision/fault/source replacement/final/disposal occurs before attach, fail closed. First new-revision-block completions can be lost and must be labeled as unavailable, not backfilled. Bound prototype history to active+one old summary. No new source read/FFT/timer or separate Canvas, and no automatic `resync()` or general broker. Option B is Axiom **provisional preference**, **not adopted owner policy**; A is legitimate dissent.

Independent reviews requested from Harbor (lifecycle), Latch (native handle), Gauge (PSD math/provenance), Mothlight (accessible UX), Flint (small stable interface), Kite (competing falsifiable resource-bounded alternative). Need reconcile into one owner-reviewed AP117-006A design with acceptance tests before an independently authorized AP117-006B implementation. Critical tests: revision transition with zero/one/many FFTs in first new block, repeated edits, unknown revisions, no-ops, paused resume, EOF pending, sticky overrun, rendering fault, late importer, replay/change/source replacement, pagehide, correct provenance/ordinal/gap representation. Preserve explicit Issue11 hold and separate work.

## Evidence limits

No production tests independently run during this design discussion, no application or CONFIG modifications, no merge, no assertions of zero-loss same-epoch recovery. Source inspection supports sequencing semantics; actual user UX and design comparison remain untested. Need source-pinned independent review, owner decision and bounded implementation afterward.


## Owner preference — Option B (2026-11-17)

User said, “Eh, I favor B.” Axiom treats this as **owner-preferred design direction**, not final acceptance of an unspecified recovery implementation. Recorded [Issue #14 owner-direction comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965287198): design **explicit user-authorized new PSD segment in the same source epoch/clock**, preserving historical old segment and discontinuity, with future-only new sourceRevision-bound native subscription **after** the producer's first new-revision accept fence; pending state if intent precedes it. No silent backfill or automatic resync. Alternative A retained as comparison/fallback. Specialist critiques now focus on B's concrete failure modes rather than a new popularity vote. Independent review, owner-approved final contract and separate AP117-006B authorization still required. No production change.


## Gauge G1–G5 reviewed — independent design amendment (2026-11-17)

Read [Gauge Issue14 comment 6965413113](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965413113) and full [individual handoff `agents/gauge-v1@56329bde...`](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/56329bdece2323f97296ad291856b08bc0009a83/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-17-ap117-006a-gauge-psd-recovery-r11.md); independently cross-checked against the previously inspected main and delivery/PSD code. Gauge conditionally endorses B but observes a missing distinction and invalid transient authority assumption. Axiom incorporated them as **candidate design constraints**, not merged consensus, via [Issue14 comment 6965473021](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6965473021).

**G2 sample-support overlap:** M8/H4, revision0 `[0,8)`, first revision1 accept `[8,20)` produces two **unretained** FFT windows `[8,16)` and `[12,20)`, post-fence frontier2. New native subscription at source cursor20 is future completion ordinal3 `[16,24)`; its valid PSD includes four pre-attachment PCM frames, though completion occurs after attach. This is a source-derived arithmetic counterexample, **not an executed test**. Distinguish epoch/revision comparability, missed complete-window ordinals, raw window-input support predating attach and render coalescing. Zero missing completions at default B480/M1024 still cannot imply all-post-click PCM support.

**G3 durable receipt:** `src/main.js` clears transient `authorizedSourceRevision` before first revised `spectrum.accept`, so an explicit click after that accept cannot trust that transient or mere getter/descriptor/generation stamps. Need a bounded trusted host-owned source edit receipt retaining exact seven source descriptor fields and selection authority; second genuine revision/change/source fault cancels pending intent. No-op cannot mint receipt.

**G4 attach frontier:** record native producer handle, generation, `attachFrontier`, source cursor, expected source descriptor, first eligible `attachFrontier+1`, and first actual PSD half-open span. New segment is pending/no current PSD until an actual observation. Late post-fence completions cannot be backfilled. First/newest sticky faults, producer-ended vs drained, capacity4, and one-read/FFT/timer retained.

**Decision:** B remains owner-preferred and Gauge-conditionally supported; A remains lower-risk fallback. Await Harbor, Latch, Mothlight, Flint and Kite before freezing option/UX/interface; no implementation authorized. Issue11 remains parked/open.


## Interim multi-agent reconciliation — Harbor B0 vs Gauge/Axiom pending B

At accepted application `main@4ef3d2376f6de1a390024eb65cbad6beab12eadb`, Axiom fetched all GitHub Issue #14 comments and read [Harbor's full source-pinned HC08 report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/5d95013c7e808f728e59cb17a9fb7fe3b262dabe/memory/agents/harbor/2026-11-17-ap117-006a-harbor-recovery-design-hc08.md), [Gauge's R11](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/56329bdece2323f97296ad291856b08bc0009a83/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-17-ap117-006a-gauge-psd-recovery-r11.md) and [Axiom's source-executed additional proof](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/de04ded48aab1c6a054f99aa3638541b445af266/memory/agents/axiom/2026-11-17-ap117-006a-gauge-recovery-executed-fences-c62e.md). Published [interim Issue14 reconciliation comment 6968149848](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14#issuecomment-6968149848), distinguishing independent executed source controls from design-only assumptions.

Harbor favors **manual post-fence B0** rather than B pending-early: the host records source-bound genuine edit, waits until **successful nonfinal first revised spectrum.accept** and producer is open, then enables an explicit **Start new PSD segment** control; no early request/queued callback. On click recheck source-instance identity, exact source seven-field descriptor/new revision, successful settlement and native producer; dispose old broken handle, keep exactly one historical summary; attach fresh native consumer, record actual generation/frontier/cursor, and wait for first real PSD. Harbor's seven source-executed V8 controls confirmed double fence, ordinal3 [16,24) with pre-attachment PCM support and zero-completion first-revised block, terminal refusal, double edits, sticky overrun, option-A epoch restart. They do *not* prove prospective B0 host/UI logic.

Gauge/Axiom original **B pending-early** instead allows one user-requested intent before the second fence and delays attachment. This reduces delayed-click friction but adds cancellation/revalidation across pause/EOF/fault and second edit. **Axiom provisional preference now B0** as minimal first experimental design, keeping pending-early variant as valid specialist dissent/possible later UX extension. A (explicit source restart/new epoch) remains existing trustworthy fallback. User favored high-level **B**, but has NOT expressly chosen B0 or authorized code; preserve those distinctions.

Common scientific invariants: exact trusted edit receipt separate from successful transition-settlement witness; second fence has finished; `revisionStartFrame <= PSD.sampleSpan.startFrame`; `sampleSpan.startFrame` may precede attachment cursor, so record frontiers and first overlap; report revision comparability break, completed-but-not-observed ordinals, preattachment sample support, Canvas coalescing as **four distinct** matters; no backfill, false gap-free series, wrong-origin/handle association, resync or extra PCM/FFT/timer/Canvas. Failed accept/terminal/unknown revision/source changes/malformed/overrun/render fault/disposal fail closed, capacity remains 4 and queued EOF drains truthfully.

Review status: **only Gauge and Harbor** specialist Issue14 reviews posted at this check; Axiom also posted its own focused source-executed supplement. Latch, Flint, Kite, Mothlight reviews are **not yet visible in Issue14 or indexed agent home records**. No six-agent consensus or final adopted recovery contract. Issue11 remains parked/open. Owner and independent review gates separate.

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

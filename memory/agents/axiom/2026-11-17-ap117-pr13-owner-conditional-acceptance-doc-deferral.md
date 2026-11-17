---
schema: 1
id: 2026-11-17-ap117-pr13-owner-conditional-acceptance-doc-deferral
kind: closeout
scope: agent:axiom
status: owner-accepted-conditionally
evidence: observed
author: axiom-pr13-final-doc
created: 2026-11-17
updated: 2026-11-17
sources: "Owner's direct 2026-11-17 conditional acceptance request; Auralprint PR13 docs commit ed6a0523d8351229a1aed6cc311804797b0ab587, previous R1 head bce44420bb7053556a10d40fef97afd91ad9c499, base main bdead48ae672ed6834eae274c8876944a79104bc; Issue14 and PR comment 6943388382."
---

# AP117-004 PR13 — owner accepted prototype hold-on-break limitation; documented future deferral

Owner said **"Conditionally accepted. Make the documentation clear that this is a known limitation, deferred till future work."** Applies only to the bounded AP117-004 prototype, not permanent instrument behavior.

Genuine synthetic amplitude or frequency change increments sourceRevision, invalidates CP2/peak and fences host PSD. RMS/peak may continue; PSD remains broken until explicit **Use synthetic source** or source Replay/replacement. Last PSD is historical. No resync or backfill of forfeited FFT windows; restarted source epoch is not a gap-free continuation. Redundant/no-op input does not fence (PR13 R1).

Axiom created [Issue #14 — Deferred PSD recovery](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/14) for a separately approved, discontinuity-aware recovery design, source/epoch contracts, UI/user action, independent tests. Issue14 is **not** implementation authorization and does not displace agreed next Issue #11 CPU/GC operating envelope or Issue #7 graphical PSD.

Axiom updated one **documentation-only** source in the actual open draft PR13 branch `task/codex-ap117-004`: [commit `ed6a0523d8351229a1aed6cc311804797b0ab587`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/commit/ed6a0523d8351229a1aed6cc311804797b0ab587) modifies `docs/AP117_004_HOST_PSD_SESSION.md` (verified blob `6741dd16dbed6eb8c55d772bd5165955a28472ae`). Top now states **KNOWN LIMITATION / owner conditional acceptance**; recovery section explains real edit vs no-op, known persistent unavailability, exact recovery controls, historical data/no backfill, deferral to Issue #14, and rejects permanent instrument certification. Outdated "awaits owner acceptance" sentence eliminated. No product code, tests, schemas or scheduling modified. Axiom posted [PR comment 6943388382](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6943388382) attributing owner decision and docs.

Prior exact R1 head `bce44420bb7053556a10d40fef97afd91ad9c499` got Harbor/Mothlight/Flint targeted PASS and CI 131/131 via workflow `44047034181`; those are **historical**, not new commit CI. First-pass Latch/Gauge/Kite remain pinned to original PR13 head. With no production code changed, Axiom recommends **GO for OWNER merge of documentation-updated PR13**, contingent on validating the new head/CI and owner controlled merge. Issue10 closes only after accepted merge.

## Final verification and merge recommendation

Verified updated doc-only PR13 head `ed6a0523d8351229a1aed6cc311804797b0ab587` against accepted unchanged main `bdead48ae672ed6834eae274c8876944a79104bc`, still draft/unmerged, mergeable. GitHub commit lists **only `docs/AP117_004_HOST_PSD_SESSION.md`** changed. [New-head Actions run 44050839890](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44050839890), job 133927948804, completed **success**; Axiom independently read runner log **131/131 Node tests, zero fail/skipped**, build, official Nu HTML, Chromium offline/browser smoke and whitespace success (CI-run tests, not Axiom local full-suite). Posted [Axiom final GO for owner merge comment 6943422172](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6943422172). Owner condition fully satisfied and recorded; **no actual merge** performed. Issue14 remains future recovery; agreed Issue11 operating envelope next.

---
schema: 1
id: 2026-11-17-ap117-pr13-post-harness-crash-status
kind: review
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr13-recovery-snapshot
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR13 head 2d417adab3f28315c0cbde63048851ae6e44bca8 and main bdead48ae672ed6834eae274c8876944a79104bc; PR13 timeline specialist comments as of 2026-11-17; CI 43844573608; Latch branch agents/latch-v1 head 36d3c8a and tree with no PR13 review; issues 10/11 open."
---

# Auralprint AP117-004 PR #13 — recovered harness state, pending sixth reviewer

User reported harness session crash and asked for current state. Connected GitHub verification found no lost committed engineering work:
- [PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13) **open, draft, unmerged, mergeable**, one commit exact head `2d417adab3f28315c0cbde63048851ae6e44bca8`, accepted base/live main `bdead48ae672ed6834eae274c8876944a79104bc` unchanged.
- [Exact-head CI](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) completed **success**: Node 131/131 tests, build, Nu/HTML, Chromium browser/offline, representative rendered HTML and whitespace; CI attribution only.
- Six assigned independent reports: **Flint PASS** (PR comment `6914505228`), **Gauge PASS** (PR review `5933132570`), **Kite PASS** (`5933194704`), **Harbor CONDITIONAL PASS** (`5933255439`), **Mothlight CONDITIONAL PASS** (`5918671784`), **Latch no PR13 review yet**. Checked Latch own authorized branch `agents/latch-v1@36d3c8a506760871bf1a16469dec0b67bf92d50c`, file tree shows only older PR9/PR12 Auralprint records, not PR13. Do not interpret absence as failed review: session may have crashed before committing.
- Original Axiom PR13 [review dispatch](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6914016022) remains available, scoped to six remits. Source intact; no Codex corrective PR commit or Axiom merge.

## Current concrete corrective consideration

**Harbor HC06-01, independently source-executed, and Mothlight MOTH-13-03 source-traced:** synthetic `src/audio/synthetic-sine.js` setter correctly keeps `sourceRevision` unchanged for same-value input, but PR `src/main.js` `bindRange` unconditionally calls `pipeline.invalidate("source-parameters-changed")` and `spectrum.invalidate(...)` even on no-op input. Under deliberate **hold-on-break (no resync)**, an unchanged slider value irreversibly breaks PSD until source restoration/replacement/replay; RMS/peak resume. Although unconditional invalidation existed before PR, PSD's newly permanent break is introduced consequence. Proposed smallest fix compare source revision before vs after setter; only fence on actual revision change, while continuing UI update; exact no-op and actual-change regression. Alternative owner may explicitly approve any-input reset, but user burden likely not justified. Do not silently auto-resync genuine discontinuities.

**Mothlight additional source-trace concerns (not independently executed):**
- MOTH-13-01: `src/main.js` displays "PSD processing" when source is **paused** because session state isn't aware of host transport; append separate host transport/idle label without modifying the processor's scientific status, test Pause/Resume.
- MOTH-13-02: initial session **admission failure** (no subscription ever began) incorrectly displays "discontinuity: lost coverage"; distinguish no coverage ever admitted from lost prior coverage, test thrown constructor.
- MOTH-13-04: accepted true value-change causes sticky PSD hold-until-source-restart. Scientifically honest but significant recovery UX choice, requiring owner acceptance/clarification. Could name "Use synthetic source" explicitly in diagnostic without modifying recovery semantics.
- Harbor lifecycle controls pass 14/14 targeted and 3/3 importer controls, extra exact-source slider reproduction; first/final EOF, overflow, disposal, rendering-fault policy pass in assigned remit. No numerical or complete-delivery blocker reported.
- **Latch's actual origin/handle trust review is still absent.** Do not call it a six-review verdict or approve merge.

## Recovery plan

1. Dispatch/restart **Latch** using Axiom source-pinned [PR13 review assignment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6914016022); load own agent contract/memory, independently challenge genuine native handle binding, two-producer/same-stamp and same-producer staggered subscriptions, trust boundary, preserve PR comment and own-memory report. No edits/merge.
2. Reconcile all six with exact source SHA, treating HC06-01 and MOTH-13-03 as overlapping reproducible/sourced no-op cause, not two different bugs. Recommend one bounded Codex repair on same draft PR: actual-revision guard + diagnostic pause/admission correction + focused tests. Owner to adjudicate genuine hold-on-break product policy without silent recovery logic.
3. Codex may push small correction on existing branch only after owner asks; ask affected reviewers Harbor/Mothlight, Flint if main wiring changes, Gauge/Kite only where relevant, and Latch's first-pass status. Repin new PR head/CI before owner merge verdict.
4. Keep [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) open until actual host acceptance; [Issue #11](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11) and CP3-B2 Issue #7 remain deferred.

**Axiom current disposition: REVIEW HOLD**, not merge ready. No Auralprint code changed by Axiom. This file is the continuity snapshot after reported harness crash.

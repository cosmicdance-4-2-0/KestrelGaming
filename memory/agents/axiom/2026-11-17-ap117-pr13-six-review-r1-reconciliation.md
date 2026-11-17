---
schema: 1
id: 2026-11-17-ap117-pr13-six-review-r1-reconciliation
kind: review
scope: agent:axiom
status: active
evidence: observed
author: axiom-pr13-six-review-reconciliation
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR13 exact head 2d417adab3f28315c0cbde63048851ae6e44bca8 vs accepted main bdead48ae672ed6834eae274c8876944a79104bc; six specialist reviews (Flint 6914505228; Latch 5935026014; Gauge 5933132570; Kite 5933194704; Harbor 5933255439; Mothlight 5918671784), Actions run 43844573608, Axiom PR13 reconciliation/correction comment 6942610980; original source src/main.js and synthetic-sine.js."
---

# AP117-004 PR #13 — six independent reports reconciled; R1 requested, merge held

## Evidence

As of 2026-11-17, [PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13) is open/draft/unmerged/mergeable, exact head `2d417adab3f28315c0cbde63048851ae6e44bca8`, accepted base/main `bdead48ae672ed6834eae274c8876944a79104bc`. Exact-head GitHub Actions [run 43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) completed success, 131/131 Node tests plus build, official Nu HTML and Chromium offline browser smoke. CI-executed evidence, not Axiom local full-suite run.

**All six engineering first passes now documented and source-pinned**:
- **Flint PASS** (PR issuecomment `6914505228`): native producer-owned handle, host first-ready-before-accept, finite drain, Node engine >=22.15 test hook support, no corrective scope.
- **Latch PASS** (PR review `5935026014` and permanent [LK30](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/8f2250bfc717cb66b1bccdad99db52523e663dc1/memory/agents/latch/2026-11-17-ap117-pr13-host-psd-session-trust-lk30.md)): independently source-executed both equal-stamp genuine producers with correct distinct PSD, staggered later subscriber and historic A, no external receipt/caller-built wrapper ingress, four queued terminal observations and overflow. Trusted selection of the correct producer remains a host prerequisite, not hostile JS authentication. This closes Latch's old native-host-bound subgate within this bounded single app.
- **Gauge PASS** (PR review `5933132570`): PSD numerical formula/lineage and full-window integration without another FFT or PCM read.
- **Kite PASS** (PR review `5933194704`): capacity-bounded work, explicit overflow, no measured full device performance/GC.
- **Harbor CONDITIONAL PASS** (review `5933255439`, independent 14+3 focused source-executed checks): **HC06-01 reproduced**: actual `createSineSource` no-op setter leaves revision unchanged, but `main.js` unconditionally invalidates pipeline/spectrum, generating a permanent false PSD break under new hold-on-break policy. Genuine hold-on-break HC06-02 is truthful and significant owner recovery UX tradeoff.
- **Mothlight CONDITIONAL PASS** (review `5918671784`, source inspection only): MOTH-13-03 same false-break root as Harbor HC06-01, not independent bug; MOTH-13-01 paused host still labels PSD "processing", though no frames acquired; MOTH-13-02 failed first admission says "lost coverage" despite no subscription, MOTH-13-04 hold-on-break recovery cue needs clear instruction/owner policy affirmation.

## Reconciliation and correction authorization

Posted detailed owner-relay **[Axiom six-review reconciliation and CODEX-AP117-004-R1](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6942610980)** on existing draft PR #13. **Integrator decision:** **CONDITIONAL GO for one bounded correction, HOLD MERGE**.

Changes authorized for Codex **on existing task branch**:
1. Compare real synthetic sourceRevision **before and after** range setter; preserve accepted UI output updates but only invalidate pipeline/spectrum and set authorized revision when genuinely changed. Preserve honest sticky break for actual change. **Important protected accepted CP3-A behavior change**: old no-op input *did* fence producer because existing host code unconditionally invalidated; request explicit compatibility review and test rather than hiding this semantics change. STOP if canonical no-op invalidation requirement exists. No numerical/spectrum-source refactor.
2. Add host transport to `#psd-status` truth so when source is paused it doesn't imply actively acquiring PSD; keep scientific session state/schema untouched.
3. Distinguish never-admitted PSD session constructor failure from actual lost continuous coverage; add actual `main.js` harness test.
4. Name existing recovery control ("Use synthetic source"/file source replay) explicitly for true hold-on-break while **not** silently implementing resync or a new UI control.
5. Focused actual integration tests plus full Node/static/Nu/Chromium, show exact new head and attributable evidence; push minimal commit onto existing draft PR, never create second PR/merge/release.

Request targeted new-head re-reviews: **Harbor** on invalidation/recovery, **Mothlight** on diagnostic/UX, **Flint** on accepted old CP3-A no-op input semantics and minimality. Latch/Gauge/Kite historical reports remain at old SHA, diff-inspect for unaffected areas; repeat only when corresponding logic changes. User/owner ultimately decides whether genuine edited-value PSD hold until restart is acceptable temporary prototype policy. Nothing in six reviews warrants new source/FFT/PSD math, plugin framework, general compositor or Issue #11 optimization.

## Status

Application PR still draft and unmerged. Axiom only posted source-pinned PR review/correction instructions and this authorized memory; **no application implementation, Codex execution, app code commit or merge performed by Axiom**. Issue #10 host integration remains open until corrected owner acceptance; Issue #11 measurement and Issue #7 visualization separate.

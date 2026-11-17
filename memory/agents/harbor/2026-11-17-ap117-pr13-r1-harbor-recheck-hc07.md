---
schema: 1
id: 2026-11-17-ap117-pr13-r1-harbor-recheck-hc07
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-pr13-r1-recheck-2026-11-17
created: 2026-11-17
updated: 2026-11-17
sources: "CODEX-AP117-004-R1 PR #13 issuecomment-6942893831; exact revised head bce44420bb7053556a10d40fef97afd91ad9c499 against prior reviewed head 2d417adab3f28315c0cbde63048851ae6e44bca8 and accepted main bdead48ae672ed6834eae274c8876944a79104bc; Harbor prior HC06 home@df1c3048d7095122ce385eb1e6401bb774c1126b; exact-source 12 lifecycle/slider + 7 diagnostic isolated V8 checks; GitHub Actions run 44047034181 exact-head successful, job log 131/131 attributed to CI."
---

# Harbor HC07 — Auralprint PR #13 R1 lifecycle/continuity recheck

**Assignment:** Harbor focused re-review, [PR #13 R1 dispatch](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#issuecomment-6942893831).  
**Source pinned:** R1 `bce44420bb7053556a10d40fef97afd91ad9c499`, parent/reviewed head `2d417adab3f28315c0cbde63048851ae6e44bca8`; unchanged accepted base `main@bdead48ae672ed6834eae274c8876944a79104bc`.  
**Harbor home loaded:** `agents/harbor-v1@df1c3048d7095122ce385eb1e6401bb774c1126b`. Previous findings are in [HC06](2026-11-16-ap117-pr13-host-psd-recovery-hc06.md); do not rewrite the historical conditional verdict.  
**Disposition:** **PASS, Harbor R1 lifecycle and recovery scope**; prior moderate **HC06-01 resolved**. Genuine-edit hold-on-break remains an explicit **owner decision**, not silently changed to automatic resync. No application source edit, merge, or adoption authority claimed.

## Summary

The R1 correction is one bounded commit and four changed paths: [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/src/main.js), [`tests/app-integration.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/tests/app-integration.test.js), [`tests/browser-smoke.mjs`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/tests/browser-smoke.mjs), and [`docs/AP117_004_HOST_PSD_SESSION.md`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/docs/AP117_004_HOST_PSD_SESSION.md). FFT, CP2, PSD math, native delivery/session contracts and rendering backend are unchanged.

**HC06-01 closeout:** [`src/main.js:151–174`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/src/main.js#L151-L174) now captures `source.getSettings().sourceRevision` immediately before and after successful setter execution. It updates displayed control output regardless, but grants `authorizedSourceRevision` and invalidates both CP2/peak **only when the revision actually changes**. A same-value event no longer falsely claims `source-parameters-changed` and cannot permanently strand an otherwise healthy PSD session. The source setter's no-change behavior remains [`synthetic-sine.js:50–56`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/src/audio/synthetic-sine.js#L50-L56). A rejected value likewise does not invalidate or overwrite pending authorization.

**Actual change:** When amplitude/frequency truly changes, both existing invalidations occur, the current PSD session moves immediately to sticky broken, its last science result remains historical, and no ordinary new-revision input silently resynchronizes or backfills missing completed windows. A subsequent same-value event does not create a second fence or erase the authorized revision awaiting the next CP2-ready input. This is intended scientific fail-closed behavior, not a new defect.

**Diagnostic:** [`src/main.js:60–98`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/bce44420bb7053556a10d40fef97afd91ad9c499/src/main.js#L60-L98) separates transport from consumer state, yielding `PSD session ready; source paused` when a healthy subscribed processor is idle because the host paused. A first `psd-session-admission-failed` now says `no subscribed coverage began` and **does not** claim previously lost coverage or historical measured span. Real broken sessions preserve earliest/latest reason, failure scope, historical sample span and source-specific recovery instructions.

## Evidence

### Independent source-executed controls, exact R1

Fetched exact production `src/main.js`, `synthetic-sine.js`, `fft-amplitude.js`, `spectrum-delivery.js`, `spectrum-stream.js`, `psd-processor.js`, `host/psd-session.js` with connector at `bce44420...`. Used **production module bodies**, replacing static ESM declarations with explicit injected dependencies for isolated V8 evaluation. Extracted the exact `bindRange` and `updatePsdDiagnostic` functions from production `src/main.js` and exercised them with minimal controlled host/DOM mocks. This is source-execution, **not** a full production `main.js` Node or Chromium run.

**12/12 PASS — lifecycle and slider source controls:**

1. Duplicate amplitude 0.5 retains revision0, peak object, PSD object, live producer generation and ready status; no CP2 or spectrum invalidation. Display still updates to 0.50.
2. Duplicate frequency 1000 similarly preserves continuity and updates its output.
3. Two no-op controls followed by new ready PCM deliver the next ordered complete spectrum→PSD window, ordinal increases without reset.
4. Real amplitude change to 0.25 yields source revision1, **exactly two** named invalidations and immediate `source-parameters-changed` upstream break with authorized revision1.
5. Real frequency change to 2000 independently performs the same genuine-change fence.
6. Duplicate amplitude/frequency after real edit does not add a second fence, change first/latest reasons or erase pending authorization.
7. After real change, later valid sourceRevision1 input can keep peak alive while PSD stays broken and latest PSD becomes historical; no implicit resync.
8. Rejected out-of-range setter preserves source revision and pending authorization and does not invalidate.
9. Four queued complete final PSD observations drain in order, with `source-ended-drain-pending` before drain and `drained` after; no fabricated tail.
10. Undercomplete seven-frame final yields drained zero-window result.
11. Upstream render-failed following a genuine source fence preserves first cause `source-parameters-changed` and latest `render-failed`.
12. Disposed host session is idempotent, cannot re-open and performs no further PSD drain work.

**7/7 PASS — source-executed diagnostic states:** active = `PSD processing` plus `transport: running` without historical/loss; healthy paused = `PSD session ready; source paused`, same last span/count but not processing; first admission rejected = `no subscribed coverage began` and zero/unavailable span without `lost coverage`; synthetic break = historical span + first/latest and `Use synthetic source`; file break = `Replay or select a source`; clean drained = last science historic without false loss; disposed = explicit disposed/transport state without processing.

**Aggregate:** **19/19 focused isolated source-execution checks PASS, 0 FAIL.** All tests used synthetic controls, not a full browser host. Work and status remain independent of rAF in the unchanged host boundary.

### Actual PR diff and CI

Remote [one-commit R1 comparison](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/compare/2d417adab3f28315c0cbde63048851ae6e44bca8...bce44420bb7053556a10d40fef97afd91ad9c499) verified **four changed files**, no producer, FFT/PSD or subscription changes. [GitHub Actions 44047034181](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44047034181) completed `success`, associated with exact head `bce44420...`; independently read verify job `133915182137` summary and full log, confirming **131/131 Node tests, 0 failures**, successful static build, built and rendered HTML validation, browser smoke (paused/no-op, genuine fence/recovery, EOF/replay, cancellation, pagehide/BFCache event/reload, no external requests) and whitespace checks. GitHub's workflow uses a PR merge ref; this evidence is **CI-run, not Harbor-local full-suite execution**.

**Historical comparison:** Prior Harbor [HC06](2026-11-16-ap117-pr13-host-psd-recovery-hc06.md) directly reproduced sourceRevision 0→0 with **two improper invalidations**, leading to sticky PSD loss under hold-on-break at old head. At new head, the direct source slider test reproduces the same input with **zero invalidations** and preserves currentness; a valid actual edit still fences. Codex's separately attributed archive-old-vs-new actual-main test and full-browser proof are credible additional evidence, not assigned to Harbor as executed.

**No local full-host rerun:** Did not perform `npm run verify`, Node module-hook actual-main import, Playwright/Chromium, device calibration, GC/real-time benchmarking, or real BFCache navigation personally. Source-executed branch local V8 mocks cannot prove browser event behavior outside the tested input semantics. No changes to application code or other agents' memory.

### Findings and decisions

- **HC06-01: RESOLVED.** Unchanged-input false `source-parameters-changed` fence is no longer reproduced. The revised tests assert exact session identity/observation continuity and source clock, and include real-change positive controls. No residual blocker in Harbor's R1 scope.
- **HC06-02: OPEN OWNER-ACCEPTANCE POLICY, not a new code defect.** A real parameter edit still leaves PSD unavailable until explicit restoration/replay, while RMS/peak continue. This is truthful fail-closed analysis but significant UX friction. The host now names applicable recovery controls. The owner should accept this limited prototype consciously or schedule a new explicit segmented/new-association design; never silently label missed history as continuous.
- **Recovery and compatibility:** Explicitly documented host-compatibility change: CP3-A previously invalidated RMS/peak for *any* slider input; R1 retains valid RMS/peak on no-op. Source setters define revision change only on real edits. No source-contract evidence found requiring a false no-op invalidation. Protect existing genuine-edit, final-tail replay-required, import cancellation, source disposal and global render-failure policy unchanged from first-pass accepted behavior.
- **No change requested:** No corrections required for exact R1 head within Harbor remit. Other specialists' decisions, owner merge/adoption and Issue #11 performance limits remain independent.

## Revisit when

PR #13 advances again or merges, a new integration test exposes a counterexample, the owner revises hold-on-break policy, a non-synthetic source adds settings with side effects unreflected in `sourceRevision`, or the host supports independent instrument resumption. Re-pin both current application/head and Harbor memory, rerun changed-line and regression controls, and preserve original HC06 finding as historical evidence. Shared GitHub authentication is an attribution channel, not authenticated separate agent identity.

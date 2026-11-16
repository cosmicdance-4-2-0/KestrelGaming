---
schema: 1
id: 2026-11-16-ap117-pr13-host-psd-diagnostic-review-f8c3d49a
kind: handoff
scope: agent:mothlight
status: active
evidence: observed
author: mothlight
created: 2026-11-16
updated: 2026-11-16
sources: "Auralprint AP117-004 PR #13 head 2d417adab3f28315c0cbde63048851ae6e44bca8 against main bdead48ae672ed6834eae274c8876944a79104bc; Mothlight GitHub COMMENT review #5918671784; Axiom assignment comment #6914016022; CI run 43844573608."
---

# AP117-004 PR #13 — Mothlight independent PSD host diagnostic review

## Summary

**COMPLETE.** Posted an independent [COMMENT review on Auralprint PR #13](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/13#pullrequestreview-5918671784) at exact head `2d417adab3f28315c0cbde63048851ae6e44bca8`, accepted baseline `main@bdead48ae672ed6834eae274c8876944a79104bc`. Verdict: **CONDITIONAL PASS** for Mothlight's status/UX remit; no demonstrated data-delivery or mathematical correctness blocker. Reviewer did not modify Auralprint code, authorize merge, adopt host/PSD schemas, or claim independent tests. Axiom's review hold and owner control remain.

## Evidence

Source inspected: project `AGENTS.md`, `src/host/psd-session.js`, `src/main.js`, `src/config.js`, `src/audio/synthetic-sine.js`, `index.html`, `docs/AP117_004_HOST_PSD_SESSION.md`, `tests/psd-session.test.js`, `tests/app-integration.test.js`, `tests/browser-smoke.mjs`, accepted producer/processor boundaries and own PR #12 review. **GitHub CI** [43844573608](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43844573608) at exact head completed success; Axiom's log inspection records 131 Node tests + build/Nu/browser. I did **not** independently run Node, Chromium or screen reader; trace findings below are **source-only**.

**Positive source findings:**
- Main registers the native producer-owned PSD subscription on first accepted CP2 descriptor **before** that same `spectrum.accept` and drains synchronously after accept, independent of `FrameHost` and the two existing Canvas presenters.
- `psd-session.js` distinguishes `source-ended-drain-pending` versus consumer `drained`, preserves final windows and exact BigInt half-open spans and marks drained/broken/disposed output **historical**.
- `reason` and `failureScope` record first cause, `latestReason` later cause, true producer `upstream` is separate; resync not exposed and stale previously valid outputs never become current again. Subscription-local loss is not renderer coalescing.
- `lastPaintedSpectrum` is **peak Canvas** presentation receipt only; no PSD “last painted” or wall-clock sample claim is fabricated. Proposed status text disclaims dB/physical calibration/Welch/steady noise floor.

**Findings requiring integrator consideration:**
1. **MOTH-13-01 MEDIUM:** during a real Pause, `src/main.js:355-369` calls `stop(); drawFrame()`, but the live PSD session maps `state="processing"` based on an open subscription (`psd-session.js:68-75`); UI at `main.js:63-68` prints **“PSD processing”** despite source clock frozen. Proposed low-risk UI-only correction: separate host transport state (“paused”) from processor continuity; preserve last complete scientific span and no timer fabrication.
2. **MOTH-13-02 LOW:** if PSD subscription/session admission throws before any PSD history, host sets `psdFailure.reason="psd-session-admission-failed: ..."` and `historical:null` (`main.js:125-133`), but a generic failure branch at `main.js:80-82` reports **“discontinuity: lost coverage”** although no subscription was ever established. Label initial non-admission as **“PSD not admitted/no subscribed coverage begun”**, not historical lost observations.
3. **MOTH-13-03 LOW–MEDIUM:** synthetic setters only increment `sourceRevision` when the value changes (`synthetic-sine.js:50-56`), but the unconditional slider `input` handler invalidates both pipeline/FFT even if value unchanged (`main.js:150-159`). Under this PR's **permanent hold-on-break** PSD recovery, a same-value event can retire a valid session without real parameter change. The invalidation hook predates this PR, but its permanent PSD implication is new. Proposed guard: compare source revision before/after setter; no-op should not fence; test actual change + explicit source restoration separately.
4. **MOTH-13-04 POLICY, not code fault:** intentional parameter change fences PSD forever until existing source restoration/replacement/replay; ongoing RMS/peak remain valid. Diagnostic states this, but recovery command is buried in long non-live text; the actual control is **“Use synthetic source.”** Ask owner to affirm the conservative limitation and optionally name the exact action in a future/status-only patch. `aria-live="off"` avoids per-frame announcements but screen-reader discoverability was not independently validated.

These are **source-trace findings** and human-facing limitations, not evidence of broken FFT/PSD mathematics, software test failure, rogue stamps or lost legitimate complete-window delivery. None authorizes auto-resync or a new generic panel/broker.

## Revisit when

Axiom reconciles six exact-head PR #13 independent reports, a narrow UI correction is made, or the owner reviews persistent PSD hold-on-break tradeoffs. Pin updated PR SHA, require targeted Pause, admission-failure and no-op-change negatives, and preserve distinction between a source's last ready publication, PSD continuity, and last successfully painted **peak** frame. Never treat green CI as independent screen-reader evaluation.

**Authorial perspective:** Mothlight — The Invisible Stagehand. Shared GitHub credentials demonstrate attribution only, not a uniquely authenticated agent runtime.

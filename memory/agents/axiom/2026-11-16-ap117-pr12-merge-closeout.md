---
schema: 1
id: 2026-11-16-ap117-pr12-merge-closeout
kind: closeout
scope: agent:axiom
status: accepted
evidence: observed
author: axiom-merge-closeout
created: 2026-11-16
updated: 2026-11-16
sources: "Auralprint PR12 merge metadata, accepted new main bdead48ae672ed6834eae274c8876944a79104bc, PR12 reviewed source 2acfeb9daf3b5714424455afc64bcffd237c23d7, Axiom acceptance comment 6910615461, issue #10 and #11 current open status."
---

# Auralprint 117 — PR #12 merged, AP117-003 headless PSD consumer accepted

## Verified merge and baseline

Owner reported PR #12 merged. GitHub connector independently verified:
- [PR #12](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12) **merged**, `merged_at=2026-11-16T08:05:15Z`;
- Reviewed source head `2acfeb9daf3b5714424455afc64bcffd237c23d7`;
- Accepted previous base `2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`;
- Merge commit and new remote **`main@bdead48ae672ed6834eae274c8876944a79104bc`** (identical SHA) at verification.
- Axiom's [final recommendation](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6910615461) was GO for owner merge, following initial six specialist independent reports and Flint/Kite/Gauge R1 exact-head signoffs.

## Accepted scope, no overclaim

The merged changes add opt-in **headless, trusted built-in, complete-window FFT→PSD consumer** `src/analysis/psd-processor.js` with separate bounded control `ap117.psd-delivery/1` and normalized-PCM-squared-per-Hz `ap117.psd/1` one-sided, no-detrend, nonaveraged periodogram observations. Each valid subscribed FFT window yields one derived PSD when pulled; the existing PCM source, FFT producer, spectrum latest-only display, presentation and scheduling are untouched. Formula `P[k] = A[k]^2 / (c[k] ENBW_Hz)`; integrated density is window-weighted mean-square, not CP2 unweighted RMS². Existing accepted FFT producer ceiling `maxFftFrames` now enforced before any new PSD weight computation.

Source/consumer complete-window, history/fence/EOF, bounded overrun and origin limits passed focused review; exact head CI 120/120 Node tests, build, HTML and existing Chromium passed as **CI-run evidence**, not an Axiom independent local full-suite run. No PSD GUI/browser widget test because production host is not yet wired. New schema adoption is **for this scoped internal implementation**; no general PSD provider/plugin interface, physical instrument certification, Welch or external realtime promise.

## Open downstream gates

- [Issue #10](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/10) remains **open**. Next actual host/consumer and any multi-panel integration must bind and exclusively transfer the intended *actual native subscription* instead of assuming equal generation/continuity counters authenticate receipt origin. Test wrong-live-handle at construction, EOF with queued final results, source revision/epoch resync loss and status separation, panel last-drawn state. Do not label issue closed merely from `take(receiptA)` rejection in the headless proof.
- [Issue #11](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/11) remains **open**. Measure actual CPU/GC/heap/producer work and capacity before unrestricted live, user-configurable multi-provider and realtime performance claims.
- CP3-B2 / UI and future module architecture are **not** implicitly authorized by merge. Next task should be scoped from the accepted main baseline and staged as a small host wiring/integration contract/proof with first real production consumer and reviewable test, not automatic compositor/plugin/scene-runtime implementation.

## Next

When owner authorizes Codex next assignment, plan with new `main@bdead48ae672ed6834eae274c8876944a79104bc`, repo AGENTS.md and current issue requirements; preserve config source-of-truth, immutable shipped releases, independent senior review, Codex sandbox branch pushed + draft PR, never automatic merge/release. Axiom coordinates changes, six seniors preserve dissent, owner merges.

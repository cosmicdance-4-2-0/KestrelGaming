---
schema: 1
id: 2026-11-07-ap117-cp2-lifecycle-audit-hb8c
kind: lesson
scope: agent:harbor
status: superseded
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Read-only GitHub review cosmicdance-4-2-0/ap_117_KESTREL main@65d5d9bec4a9f93fafc61e3bb15dcaa3b6740695 and PR3@56d4af9759071e9ab6c7973f203e7dcfda23a2f7; exact-head CI run 42362951842; isolated Node 22 lifecycle reproductions performed 2026-11-07."
---

# Harbor — Auralprint 117 CP2 lifecycle and resilience review

## Summary

**Outcome: COMPLETE independent source review; CONDITIONAL PASS for CP2 recovery boundaries.** The target is a private application repository. This is a public-safe scoped audit receipt, not a mirror of private code or an authorization to change the application.

At review: CP1 and CP2 had merged; CP2 main was `65d5d9bec4a9f93fafc61e3bb15dcaa3b6740695`. Flint's focused frame-loop maintenance PR #3 was open at `56d4af9759071e9ab6c7973f203e7dcfda23a2f7`. Its exact-head CI [run 42362951842](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42362951842) reported 49/49 Node tests, static build, Chromium browser smoke, HTML checks and offline checks passing. These are GitHub CI observations, not a local full-checkout rerun.

Core boundaries reviewed favor accurate block RMS provenance, contiguous source clocks and epochs, fail-closed invalid observations, immutable scalar measurements, bounded file reads, and host-owned render scheduling. No hardware, browser-general, calibration or performance certification was established.

## Evidence

- **Observed, isolated test:** A synchronous stop/start inside one render callback scheduled two pending frames in main; the one-condition PR #3 candidate scheduled only one. This supports the narrow PR correction.
- **Observed, isolated test:** Both versions rescheduled after a throwing render callback; an initial scheduling exception left the frame host marked running without a callback and blocked retry. These indicate missing bounded-failure/restart semantics, not proven physical-browser incidents.
- **Observed, isolated test:** A failing initial file-import status notification can leave the importer busy, rejecting subsequent attempts. The relevant application notification performs UI work, giving this a plausible but unproven integration trigger.
- **Observed, simulated adapter only:** Delivering a previously cancelled callback after stop/start caused two pending frames even in the PR #3 candidate. Native Chromium late-delivery behavior was **not** reproduced. Treat as a future adapter-invariant test, not a certified browser failure.
- **Observed, source inspection:** The static build removes the previous output before copying replacements. Interruption can leave a partial build; atomic artifact publication is a later delivery consideration, not a CP2 numerical blocker.
- **Evidence boundary:** Test reproductions used inspected logic copied into a short isolated Node.js harness, not a byte-identical cloned checkout. Private repository network cloning was unavailable. A complete local Node suite, browser suite and memory-repository validator were not executed.

**Independent judgment:** The narrow synchronous reentrant bug targeted by PR #3 is corrected. Do not elevate that result into an unlimited lifecycle guarantee. Prefer focused error-path tests and small state rollback/callback-generation fixes over a new scheduler or recovery subsystem. Project owner retains PR acceptance and merge authority; no app changes were made.

## Revisit when

Before claiming lifecycle hardening or starting broader renderer interchange, recheck target main/PR SHAs and reproduce error paths directly in the actual checkout. Add regression tests for failed frame scheduling, persistent draw exceptions and failing file-import notifications; decide whether stale callback delivery is part of the frame-host adapter contract. Verify a fresh exact-head CI run and treat previous CI as source-pinned history.

## Superseded by

[Integrated CP2 lifecycle and recovery audit](2026-11-07-ap117-integrated-cp2-recovery-review-hb9d.md) — exact merged-head source-executed review with normalized findings and recovery verdict.

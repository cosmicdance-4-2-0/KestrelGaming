---
schema: 1
id: 2026-11-07-flint-ap117-cp2-frame-loop-pr3-f82a
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-ap117-cp2-maintenance-session
created: 2026-11-07
updated: 2026-11-07
sources: "ap_117_KESTREL main@65d5d9bec4a9f93fafc61e3bb15dcaa3b6740695; Flint PR #3 head 56d4af9759071e9ab6c7973f203e7dcfda23a2f7; CI run 42362951842; GitHub compare/PR patches; 2026-11-07."
---

# Flint — Auralprint 117 CP2 frame-host minimality pass

## Summary

**Outcome: COMPLETE for the bounded patch; PR #3 is OPEN, not merged.** After Axiom/Gauge delivered and the owner merged CP2, I inspected the source contracts, source/DSP interfaces, browser host, tests, and checkpoint documentation. No DSP arithmetic correction or architecture rewrite was justified.

One concrete render-host invariant gap: a synchronous `onFrame` callback performing `stop(); start()` schedules a replacement frame while the prior callback's `finally` schedules a second. This defeats the promise of one host-owned requestAnimationFrame loop. The smallest correction is to queue a successor only when the host is running **and** no frame is already queued (`handle === null`).

## Evidence

- **Observed merged baseline:** Auralprint 117 `main@65d5d9bec4a9f93fafc61e3bb15dcaa3b6740695` already contains CP2 and the prior Flint publication integrity fixes. PR #2 is merged, not awaiting re-review. Historical CP2 document header incorrectly still denied its own merge.
- **Observed patch:** [PR #3](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/3) at `56d4af9759071e9ab6c7973f203e7dcfda23a2f7`: only `src/rendering/frame-host.js`, `tests/camera-render.test.js`, and `docs/CP2_FILE_PCM.md`. One guard changed, one deterministic reentrant restart regression added, one historical status paragraph corrected. No source/DSP/provenance contracts, runtime dependencies or visual models changed.
- **CI-attributed exact-head verification:** [GitHub Actions run 42362951842](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42362951842) concluded success, including **49 passing Node tests / 0 failures**, static build, remote-code gate, official Nu validation, Chromium browser smoke, rendered-state HTML validation, artifact upload and whitespace check. Job logs were inspected for counts. No independent local full repository checkout/test run was performed; container could not resolve GitHub DNS. Other browsers, real hardware, and worst-case performance remain unverified.
- **PR evidence:** the exact comparison is three commits ahead, zero behind, with only those three paths modified; review handoff is recorded in PR #3 comment [6705483632](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/3#issuecomment-6705483632).

## Decisions and scope

Avoid adding a new frame scheduler or generalized lifecycle machinery for this one-counterexample fix. Preserve the host's existing request/cancel interface, model/DSP independence, and runnable prototype. Do not merge, deploy, or start CP3 within this task; owner approval and independent Harbor review remain the stop.

The patch guarantees no duplicate scheduling for the **tested synchronous reentrant restart**. It is not a general proof about late callbacks from a nonconforming requestFrame host, GPU context loss, or asynchronous cancellation races; Harbor should evaluate those separately if material to recovery.

## Revisit when

When Harbor reviews lifecycle recovery, when PR #3 is updated or merged, or when new renderer adapters introduce concurrent stop/start transitions. Re-read exact current head and rerun the new negative case plus full checks after any change. Do not treat CI for `56d4af9759` as evidence for later heads.

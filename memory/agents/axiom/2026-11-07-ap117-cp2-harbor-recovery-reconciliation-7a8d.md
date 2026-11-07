---
schema: 1
id: 2026-11-07-ap117-cp2-harbor-recovery-reconciliation-7a8d
kind: handoff
scope: agent:axiom
status: active
evidence: inferred
author: axiom-review-session
created: 2026-11-07
updated: 2026-11-07
sources: "Harbor integrated CP2 audit memory/agents/harbor/2026-11-07-ap117-integrated-cp2-recovery-review-hb9d.md on agents/harbor-v1; exact source files main@7a8df54a35f4743e4c223001337d8382dda21122; CI run 42363792862."
---

# Axiom reconciliation — Harbor CP2 recovery review

## Summary

**Outcome: REVIEW/PROPOSAL ONLY.** Accept Harbor's **CONDITIONAL PASS** of `ap_117_KESTREL/main@7a8df54a35f4743e4c223001337d8382dda21122` as a credible independent source-executed audit. Exact `src/rendering/frame-host.js` and `src/audio/file-import.js` blobs still match Harbor's pinned source. Axiom inspected source and test definitions but did **not** independently execute Harbor's negative injection fixtures or modify application files. The merged CP2 prototype's normal input/analysis and rendering invariants are not invalidated by these exception-specific defects.

## Evidence

- **High / FileImport recovery:** `load()` sets `busy=true` and invokes `onState("loading")` before entering the `try/finally` that resets busy. If the callback throws, subsequent file imports return false indefinitely; Harbor independently reproduced this in the integrated application by making the Canvas2D drawing path throw during loading. Source inspection confirms the control-flow hole.
- **High / FrameHost liveness:** `start()` sets `running=true` before `requestFrame(frame)`; a synchronous scheduling exception leaves running true, handle null and `start()` nonretryable. Source inspection confirms this state.
- **Medium / render callback failure:** `frame()` unconditionally schedules its successor in `finally` when still running, even after `onFrame()` throws. This can generate an infinite failing callback loop. Decide the application-level error report and explicit recovery action; scheduler should not automatically rearm after an unhandled frame failure.
- **Deferred / stale canceled callbacks:** Harbor's force-delivered canceled-frame counterexample violates normal native rAF cancellation delivery semantics. Treat as potential custom-adapter concern, not an established Chromium/browser issue. No token-generation framework justified by this evidence.
- **Low / CI whitespace coverage:** `git diff --check` on a clean CI working tree does not check whitespace defects in committed PR changes. Provide explicit comparison range with available base/head, not only a working-tree check. Attribution: Gauge observed this separately; Axiom checked the workflow's literal command, not Gauge's fixture.

## Small bounded checkpoint proposal

1. **FileImport owns cleanup**: Guard `onState("loading")` within cleanup scope; ensure exceptions from notification paths cannot strand the busy flag or create unhandled pending imports. Negative test: transient notification/draw exception followed by a valid later import.
2. **FrameHost owns scheduling state**: Start and successor-request errors must roll back `running`/handle accurately; an unhandled `onFrame` exception must not silently requeue forever. Negative tests: initial `requestFrame` throws then retry succeeds; successor request fails then explicit restart succeeds; `onFrame` throws once and is not automatically retried.
3. **Application host owns recovery policy**: report render errors without changing measurement semantics; leave explicit retry under host/user control; preserve separation of audio sample-clock advancement from rAF, with a clear decision whether transport pauses on rendering failure. Negative integrated test: Canvas exception during import notification, no disabled-control wedge, later valid file succeeds.
4. **Independent CI correction**: replace the vacuous whitespace gate with a comparison of committed changes (ensure refs are fetched), in a separate tiny maintenance path if necessary.
5. Recheck normal CP2 tests, synthetic/WAV import, replay, channel switch, EOF, disposal, frame reentrant restart, and exact-head browser CI. No RMS/PCM/math/source clock/schema/renderer interchange work in this correction. Owner retains integration authority.

## Revisit when

A bounded lifecycle correction PR is proposed, owners select render-failure behavior, CP3 depends on shared scheduling, a custom animation scheduler is added, or independent negative tests challenge Harbor's conclusions.

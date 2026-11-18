---
schema: 1
id: 2026-11-18-ap117-ux0-independent-human-experience-64e1c9b2
kind: handoff
scope: agent:mothlight
status: active
evidence: observed
author: mothlight
created: 2026-11-18
updated: 2026-11-18
sources: "Owner AP117-UX0 assignment (2026-11-18); AP117 main@78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a; Auralprint1@75e26348848f874329ca1ac95bb13576371ed2da; PR #20 cd0ca25616a3f7277df0bc7bf1a913b8aec3957f; independent report ap_117_KESTREL issue #21."
---

# AP117-UX0 — Mothlight independent human-experience first pass

## Summary

**Task outcome: COMPLETE — individual source-pinned design report posted.** [AP117-UX0 Mothlight issue #21](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/21) is the authoritative public design artifact for this first pass. No production change, prototype, execution of UX tests, Axiom reconciliation, merge or UX0 adoption occurred. Mothlight did not read the other agents' new UX0 first-pass submissions before preserving its conclusions.

**Original owner scope:** five complete desktop and touch-only mobile journeys, Scene gesture ownership, selection/inspector, accessibility, source/analysis/displays status, restoration and proposed falsifiers. Axiom handles conceptual architecture and later reconciliation; Kite handles two experiments. The independent report preserves those review boundaries.

## Evidence

**Observed source:** AP117 head `main@78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a` has a working two-Canvas RMS, peak FFT and PSD-diagnostic prototype with one FrameHost. Its Camera2D is projection-only, no 117 audible playback, Scene gesture manager, instrument registry or workspace persistence. The AP117 PSD document at this pin records owner-accepted *prototype* sticky break after a genuine source edit; recovery is separately assigned to issue #14.

**Observed legacy reference:** Auralprint1 pinned SHA `75e26348848f874329ca1ac95bb13576371ed2da` implements mode-gated pointer-captured Camera pan/pinch/twist, pair rebasing with no join/leave pose jump, keyboard/wheel fallback and blur/visibility/capture cancellation. Workspace's many panels preserve focus, but the owner describes that larger UI as clunky. Historical Orb has stable per-instance identity, Scene-entity simulation state and a normalized legacy Band Bank, not 117 PSD or a production instrument schema. [Legacy116Orb PR #20](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/20) is open draft reference only.

**Inferred/proposed design:** preserve behavioral 116 gestures and focus protection, reject its direct UI-layout port. Recommend one contextual inspector and visible instrument inventory with the same commands on desktop and touch-only mobile. Separate Workspace placement, Scene object, visualizer identity and shared analysis resource; preserve CONFIG→prefs→state ownership and distinct transport/analysis/render clocks. A third instrument must not demand per-type edits in central UI; dormant/historical/failed analysis must not appear as measured zero. Proposed transitions handle 1→2→1 touch without jumps, third touch exclusion and cancellation. Saving/restoring a workspace is proposed, not an existing AP117 feature; lost file permission must not silently auto-replay.

**Proposed checks, NOT executed:** UX0-M01..M12 at issue #21: add third type, reorder, five touch-only journeys, multi-touch join/leave, zero/unavailable, stale source async, duplicate/remove identity, missing-file restore, keyboard/AT/reduced motion, drawing versus data gaps, canceled inspector capture and invalid persisted type.

**Verification performed:** read GitHub exact-pin source, reviewed design contracts, compared source-level gesture and UI behavior, and published issue #21. No device, browser, Node, screen-reader, performance or human testing was executed. No cross-agent UX0 report was read.

## Revisit when

After Axiom and Kite independently record first passes, compare design alternatives without erasing dissent. Axiom should reconcile with Flint/Gauge/Harbor/Latch adversarial reviews and owner acceptance, then prepare bounded UX1/UX2. Revalidate actual AP117 head and issue #14 recovery state before implementing any UX proposal. Retain no claim that this record is a ratified schema or production design.

**Agency note:** Mothlight authors this independent perspective. GitHub shared credential does not authenticate an individual agent runtime.

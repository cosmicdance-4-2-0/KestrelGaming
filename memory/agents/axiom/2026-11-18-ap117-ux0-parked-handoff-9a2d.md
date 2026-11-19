---
schema: 1
id: 2026-11-18-ap117-ux0-parked-handoff-9a2d
kind: handoff
scope: agent:axiom
status: draft
evidence: user-stated
author: axiom
created: 2026-11-18
updated: 2026-11-18
sources: "Owner-Axiom conversation on 2026-11-18: AP117 ecosystem/UX architecture discussion, work-order proposal and explicit 'Put a pin in that'; AP117 main@78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a; PR #20 Legacy116Orb draft, PR #18 PSD recovery draft."
---

# Axiom — AP117 UX0 parked for a later session

## Summary

**Task outcome: PARTIAL / PARKED BY OWNER.** Following the 2026-11-18 Auralprint 117 discussion, the owner said **"Put a pin in that. Lets work on something... else. Sync up your Agent memory for new work."** The proposed **AP117-UX0 — Experience Architecture and Cross-Device Interaction Contract** workload is therefore **not currently active**, not dispatched to agents, not approved as a merged target-project contract, and not an authorization to implement UX1/UX2. Await a fresh owner request before resuming.

The owner emphasized that Auralprint is an **audio analysis and visualization ecosystem**, not a feature-for-feature 116 port. UX must be designed alongside analysis/visualization architecture and must scale to a large catalog without becoming clunky. **Mobile usability and multi-touch Camera behavior are first-class requirements**, not a post-hoc responsive design exercise. The owner values 116's mature transport, Orb, Band Bank and touch interaction as behavioral references without retaining their coupling.

## Evidence and continuity

- **User-stated goals and acceptance direction:** desktop and mobile have equal access to significant capabilities, although their presentations differ; no mouse/hover prerequisite on touch devices; preserve and improve one-finger pan and two-finger zoom/rotate Camera behavior; keep scientific measurement semantics independent from visual mapping and UI state.
- **Prior investigative observations:** 116 Orb is a configurable, stateful particle-emitting Scene entity with per-instance channel/band selection and shared resource governor; the 116 Band Bank uses a configurable 3–256 band partition with linear/log/Mel/Bark/ERB distributions and normalized analyser dB activity rather than physical band power. Preserve the original behavior as `Legacy116Orb` for comparison, but do not make 116's runtime types or band normalization AP117 science.
- **GitHub artifact created in this conversation:** [draft PR #20](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/20), head `cd0ca25616a3f7277df0bc7bf1a913b8aec3957f`, adds `docs/legacy/Legacy116Orb.md` to AP117. It is a documentation-only, source-pinned reference; **not merged** as observed at drafting.
- **Proposed UX workstream only:** UX0 design/reconciliation first; later optional audible transport/playback consumer (UX1) and adaptive instrument workspace (UX2) as separately reviewed, executable checkpoints; then a bounded scene-entity proof with Legacy116Orb (UX3). The proposed UX0 first passes are Axiom (contracts), Mothlight (experience), Kite (competing experiments), with Flint, Gauge, Harbor and Latch independently challenging complexity, evidence/performance, recovery and trust boundaries. These are **proposed assignments**, not executed dispatches.
- **Auralprint mainline observation at discussion:** `main@78c68bb5ccd3a3c45fb26eb48754e55cbfbb478a`; [PR #18](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/18) PSD recovery remained draft and under review. Recheck current source and issue/PR states when returning. Do not extrapolate historical CI or benchmark data to later heads.

## Boundaries

No production, schema, DSP, Camera, input, renderer, workspace or transport edits were authorized by this parked proposal. No multi-agent independent UX0 reports, reviewed reconciliation, or owner UX0 acceptance are claimed. Existing AP117 checkpoints and protected benchmarks remain authoritative, and Auralprint 116 shipped artifacts remain immutable.

**Agent change of context:** Reload Axiom's own home branch identity, memory indexes, and task-specific continuity. The next user task is unspecified and should set its own project, authority, and scope; do **not** automatically steer the user back into Auralprint UX0.

## Revisit when

The owner explicitly resumes AP117 UX0, requests a fresh UX assignment or playback/workspace implementation plan, or asks to revisit the pinned 116 Orb/Band Bank references. Fetch current target-source and agent-memory HEAD before proceeding.

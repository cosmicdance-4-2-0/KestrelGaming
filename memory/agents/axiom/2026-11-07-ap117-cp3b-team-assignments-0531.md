---
schema: 1
id: 2026-11-07-ap117-cp3b-team-assignments-0531
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-coordination-session
created: 2026-11-07
updated: 2026-11-07
sources: "User directive to involve the full seven-engineer Kestrel roster early; KestrelGaming agents/ROSTER_V1.json, docs/ENGINEERING_PARTY_V1.md; ap_117_KESTREL main@0531e734a2ece59cd877ea8659069efee2e0a905 and GitHub issues #6 / #7."
---

# Auralprint 117 CP3-B — collaborative design assignment

## Summary

**User direction:** Axiom is primary integrator for Auralprint 117, but should enlist the six other Kestrel engineers in *design*, not wait until implementation for review. In particular, Gauge should co-design CP3-B1's mathematical specification, and Mothlight, Kite and Flint are the initial CP3-B2 visual/presentation design team.

**Actions observed:** Created two target-project planning issues on the accepted `main@0531e734a2ece59cd877ea8659069efee2e0a905`:
- [B1 — Gauge + Axiom PSD numerical contract and falsifiers](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/6).
- [B2 — Mothlight + Kite + Flint SpectrumScope presentation](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/7).

No agents were autonomously launched, no app branch/PR was created, and no B1/B2 implementation or merge happened in this coordination session. The owner/human dispatcher can provide these issue links to the agents in independent sessions. The owner retains integration/merge authority.

## Design operating sequence

1. **Gauge first**: independently co-design PSD method, units/reference, window-power normalization, provenance, expected Parseval identity, error tolerances and independent sample-time/numerical falsifiers. Axiom initially preserves scientific ambiguity rather than assuming the first proposed formula is accepted.
2. **Parallel B2 independent exploration**: Mothlight tests user comprehension, explicit units, accessibility, invalid/waiting/retry states; Kite proposes cheap falsifiable alternatives (mode switch vs multiple views, etc.) without a permanent redesign.
3. **Flint** reviews Mothlight and Kite proposals only after first independent passes, challenges complexity, source/read/rAF ownership, and proposes the smallest B2 model/presenter/UI boundary; also offers B1 architecture-simplicity challenge.
4. **Axiom** reconciles numerical contract and interface versioning into a small B1 proposal/implementation; B2 design remains provisional until B1 units/reference/method are pinned. Existing CP3-A functional prototype remains runnable; no implicit PSD by squaring displayed peak-amplitude bins.
5. **Harbor** targets recovery, source switching, short EOF, pause/retry, pagehide and render-error liveness under new measurement/view states.
6. **Latch** targets local-file trust/privacy, accidental external requests, persistence/telemetry or untrusted exported observation boundaries when the new design introduces relevant risk. Do not require redundant ceremonial reviews.
7. Gauge validates actual B2 axis/label scientific truth; Mothlight checks accessible UX, Flint checks minimum maintainable scope; independent exact-head CI plus owner review before merge.

Team identity: Axiom, Gauge, Flint, Harbor, Mothlight, Kite, Latch. The roster describes potential engineers; no issue creation by itself invokes independent sessions.

## Evidence

- KestrelEngineeringEnsemble version 1 roster enumerates exactly seven proposed engineer profiles with distinct priorities; Axiom is designated project integration lead by the user in the current assignment.
- Issue #6 asks Gauge to prepare a contract decision including independent oracle and algebraic power density integration, not merely later verification.
- Issue #7 explicitly asks independent initial first passes from Mothlight and Kite before Flint reconciles solutions, avoiding manufactured consensus.
- The current app main includes accepted CP3-A amplitude spectrum, finite-block RMS, one PCM read, two host-owned Canvas surfaces, one FrameHost; CP3-B remains design only.

## Revisit when

Gauge, Mothlight, Kite or Flint submit an actual proposal; B1 mathematical contract is selected; B2 options are reconciled; owner changes priorities to CP4; or application main advances. Pin each resulting action to exact commit/issues and do not fabricate independent agent participation.

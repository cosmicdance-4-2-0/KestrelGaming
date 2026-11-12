---
schema: 1
id: 2026-11-11-stage-fright-ven-g3-masking-followup-cd296f45
kind: handoff
scope: agent:mothlight
status: active
evidence: observed
author: mothlight
created: 2026-11-11
updated: 2026-11-11
sources: "Owner-relayed Ven G3-V01..V04 review references Stage Fright PR23 draft f04a49f98ca6cd1db8c5282b5e9df8923e1965a7. Four owner-requested fixes already recorded by Mothlight at later draft 70c47cec17404288fe1e3409334d380c41e57044. New PR23 head 8217d661c9f7e1a5d65e3040ed037057ef826d12 and SF-0007 record. Main 16414b1d59a04b9f14164dc9ba05956dbf0db5f9."
---

# Stage Fright — Ven's older Gate 3 audit and investigator-mask correction

## Verified chronology

The owner supplied another independently attributed Ven audit of **Gate 3**. Ven's four findings G3-V01–G3-V04 were written against PR #23 at **old head `f04a49f`**, concerning retrospective cognition, deliberate restraint, first-pair inference, and one-direction transfer. **All four were already resolved in the later `70c47ce` draft** by prior direct owner request. The newer protocol distinguishes post-run stories from predecision behavior, `REFRAIN_DECLARED` from `NO_HOLD_UNCLASSIFIED`, H3-02's fixed A/B inference from a Cue-board heuristic, and complementary C/D candidate crossed cases for only *within-mechanism* H3-04. Do not misattribute Mothlight's owner-requested corrections to a fresh Ven endorsement or claim Ven audited the newer head.

Ven additionally highlighted an **actually unresolved issue**: investigator condition masking distinct from participant masking. Ven also suggested an optional pre-consequence comprehension probe, which would cause possible reactivity and timing/attention changes.

## Follow-up actually committed

**Draft [Stage Fright PR #23](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/23)** now has follow-up head `8217d661c9f7e1a5d65e3040ed037057ef826d12`; still proposed `0.0.2.7/SF-0007` and not merged at last check. Four files remain changed: Gate 3 protocol, `docs/changes/SF-0007.md`, `CHANGELOG.md`, `version.json`. No Gate 1, Gate 2, roadmap or runtime change.

The targeted refinements:
- Differentiate **participant masking** (no true case label) from **interacting-investigator masking** (no access to assignment, causes, debug outcomes) and do not call a merely participant-masked study double-blind. Preferred confirmatory design hides source truth from interacting investigator through automated allocation; noninteracting technical custodian can handle failures. If impossible, preregister/disclose investigator-unmasked bias, use neutral scripts, record unmaskings/assistance and apply fixed sensitivity/handling rules.
- Preserve **uninterrupted first-exposure primary trials**. A pre-consequence comprehension question would be in a **separate exploratory probe arm**, assigned in advance with pause/interruption equivalence and pilot of reactivity; it cannot turn the main first-contact run into proof of cognition.
- Add two unexecuted negative paper cases `T3-21` investigator hidden-condition leak and `T3-22` probe-altered decision. Current paper matrix is `T3-01..T3-22`, **not executed**.
- Update SF-0007 change record and changelog, preserving older-head Ven provenance and unratified contract status.

**Gate status:** Stage 0 Gate 3 design draft awaiting explicit human owner approval. No human subject or experiment recruited/performed, no H3 result validated, no numeric parameter adopted. Run tests/CI still distinct from gameplay trials. Check fresh GitHub Actions before claiming final PR CI.

**Source:** [Gate 3 protocol at revised PR head](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/8217d661c9f7e1a5d65e3040ed037057ef826d12/docs/design/STAGE0_GATE3_JUDGMENT_TRIAL_PROTOCOL.md); [SF-0007 ledger](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/8217d661c9f7e1a5d65e3040ed037057ef826d12/docs/changes/SF-0007.md).

**Authorial perspective:** Mothlight — The Invisible Stagehand. KestrelGaming shared-main sync remains a separate postponed task.

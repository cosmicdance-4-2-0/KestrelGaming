---
schema: 1
id: 2026-11-11-stage-fright-gate3-inference-amendments-64acb321
kind: handoff
scope: agent:mothlight
status: superseded
evidence: observed
author: mothlight
created: 2026-11-11
updated: 2026-11-11
sources: "Stage Fright source main 16414b1d59a04b9f14164dc9ba05956dbf0db5f9 / 0.0.2.6/SF-0006; draft PR #23 branch design docs at 70c47cec17404288fe1e3409334d380c41e57044; explicit four-item owner requested refinement; SF-0007 candidate change record."
---

# Stage Fright — Gate 3 inferential guardrails amended in PR #23

## State

The human owner requested four targeted corrections to Mothlight's **STAGE0-G3-JUDGMENT-01** draft: (1) treat after-run explanations as retrospective, not predecision cognition proof; (2) distinguish prospective intentional Refrain versus simple no-Hold; (3) limit H3-02 initial A/B claims; and (4) complement or limit H3-04's transfer claim.

Mothlight incorporated all four in the **same open draft PR #23** ([source-pinned Gate 3 protocol](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/70c47cec17404288fe1e3409334d380c41e57044/docs/design/STAGE0_GATE3_JUDGMENT_TRIAL_PROTOCOL.md)), without changing Gate 1 authority, the Gate 2 chandelier mechanics, Stage Fright roadmap, runtime code or project version numbering. PR now contains **T3-01…T3-20** (20 **unexecuted** paper tests) instead of 16. Its affected files remain only the Gate 3 protocol, SF-0007 change record, CHANGELOG and proposed `version.json`.

## Decisions and limitations

1. **Retrospective cognition:** after-run accounts may be post-hoc reconstructed/feedback-contaminated, even when consistent with objective events. Interpret as self-report, separate from logs. No direct cognition measurement is claimed.
2. **Restraint:** `HOLD_ATTEMPTED`, `REFRAIN_DECLARED` (only when prospectively, unobtrusively marked before cutoff), `NO_HOLD_UNCLASSIFIED`, `UNABLE_OR_TOO_LATE`, and `RETROSPECTIVE_CLAIM` are distinct observational categories. There is no new mandatory control, World writer or tick cost. If no prospective marker is supported, do not infer intention from absence of a Hold; no-Hold remains unclassified.
3. **H3-02:** A/B can show *case-specific evidence-consistent observable behavior*, but since authorized Cue and physically safe limiter are perfectly correlated across the fixed pair, even good-looking trial choices and accounts cannot establish physical reasoning over a cue-board shortcut.
4. **H3-04:** complementary **candidate** crossed Stage 2 cases `C = authorized/unsafe` and `D = unauthorized/safe` are proposed, not authored/executed. Both require individually valid physical/evidence paths before any **bounded local, within-mechanism** two-direction transfer inference. If unavailable, do not claim such transfer; only exploratory one-direction observations may be reported. No other-mechanism or general expertise claim follows even if C/D succeed.

Extra negative checks T3-17..20 cover no-action/posthoc reconstruction, too-late declared Refrain, cue-board confound despite polished explanation, and invalid/missing complementary transfer variant.

## Governance and evidence

[Draft Stage Fright PR #23](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/23), candidate `0.0.2.7/SF-0007`; Stage Fright `main` remains `0.0.2.6/SF-0006` until actual review/merge. On draft head `70c47cec17404288fe1e3409334d380c41e57044`, GitHub push workflow succeeded and PR workflow was still running at first check; verify final results when needed. Hosted check success does **not** mean pilot, game mechanics, actual participants, or paper T3 cases passed.

**No additional engineer/Ven endorsement is implied by the owner-requested amendments.** Retain explicit Gate 3 design approval boundary; don't merge or claim Stage 0 complete solely because documentation exists.

## Next

Focused owner/design review of altered inference classes, possible marker reactivity, the C/D authoring feasibility boundary, and the updated negative matrix. Then approve/revise Gate 3 distinctly from PR merge; preserve Stage 0 Gate 4 closeout and later participant trials as separate work.

**Authorial perspective:** Mothlight — The Invisible Stagehand.

## Superseded by

[Ven's older-head G3 review and explicit investigator-mask protocol follow-up](2026-11-11-stage-fright-ven-g3-masking-followup-cd296f45.md). The prior owner-inference fixes remain valid; the later PR #23 adds masking and optional probe-arm controls.

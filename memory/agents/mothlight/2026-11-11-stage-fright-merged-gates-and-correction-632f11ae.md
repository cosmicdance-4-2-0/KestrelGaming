---
schema: 1
id: 2026-11-11-stage-fright-merged-gates-and-correction-632f11ae
kind: handoff
scope: agent:mothlight
status: superseded
evidence: observed
author: mothlight
created: 2026-11-11
updated: 2026-11-11
sources: "Stage Fright main 514ce104bcd3eb3b235df491aca85e36ac0a6a99; PRs #18/#19/#20 merged 2026-11-11; draft PR #21 proposed at 0ffac72aca224cda2314c35a81db49e8578ff7ec; prior review and reconciliation source pins in memory/agents/mothlight/2026-11-11-stage-fright-gate1-six-reports-reconciliation-d8a630c1.md."
---

# Stage Fright — merged Gate 1/2 proposals and forward compatibility repair

## Current verified history

The project owner merged all three Stage 0 documentation PRs *in order*: [#18](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/18) (independent Gate 1 review intake, merge `0b388846c3f929c1f0ad82c9a894aabf17aee7eb`), [#19](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/19) (provisional Gate 2 chandelier A/B model, merge `6ff94b23f7eb7ccae423a4f6e8df6896f0bc3396`), and [#20](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/20) (Mothlight's candidate Gate 1 arbitration and simulation reconciliation, merge `514ce104bcd3eb3b235df491aca85e36ac0a6a99`).

**There is no code regression from that sequence:** all were *provisional/design docs only*, original six reviews remain intact, post-merge R0 CI succeeded for each, and no gameplay mechanics were implemented. **Their order did expose a real but resolvable documentation dependency:** Gate 2 PR #19 still deferred exact Hold/Cue, post-Inspect publication and last-effective cutoff decisions that Gate 1 PR #20 subsequently proposed. Merging proposals does **not** ratify executable contracts or prove fairness.

**Administrative discrepancy:** the three merges did not update `version.json` or allocate individual ChangeIDs. Game main remains at `0.0.2.4/SF-0004` despite new merged docs. Its versioning policy normally requests each accepted integration have its own recorded ChangeID. Do not pretend otherwise or rewrite historical merges.

## Corrective proposal, not yet merged

Mothlight prepared [Draft PR #21](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/21), branch `design/stage0-gate2-gate1-alignment`, latest documented head `0ffac72aca224cda2314c35a81db49e8578ff7ec`, as a strictly forward docs correction:
- specify one fictive physical `HOLD` interlock instead of blanket player-over-Cue priority; distinguish fresh Cue suppression from already matured scenery consequence;
- express move/inspect/read/operate timing in completed active-step boundaries and an exact last-effective Hold cutoff; observations are post-world and usable only from the next decision step;
- update F2-08/09/11/12 and four independently inspectable **paper** traces without claiming execution;
- correct stale labels in the Gate 1 intake, roadmap and reconciliation;
- propose `0.0.2.5/SF-0005` as **one prospective, transparent, catch-up integration** with full disclosure that the three historical merges never had individual version ChangeIDs.

The first PR #21 build failed **only** at `npm run version:check` because the record began with `**Proposed version:**` instead of the validator-required `**Version:**`. This was corrected at `0ffac72...`; follow-up hosted push and PR CI both **PASSED** at head `0ffac72aca224cda2314c35a81db49e8578ff7ec`: [push run 43025480821](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/actions/runs/43025480821), [PR run 43025489667](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/actions/runs/43025489667). Those existing R0 checks do not execute the new G1/F2 mechanics; no gameplay test was performed. **PR #21 is deliberately draft** and owner acceptance remains open; main has not been changed by this correction.

### Remaining actual gate state

Gate 1 has six received independent reviews and a merged but still explicitly **proposed** authority/tie table. Gate 2 has a merged but explicitly **provisional** mechanism, and PR #21 adds proposed compatibility clarification. No authoritative game-physics runtime, experimental player data, fixed timing parameters, durable saves or full Ghost architecture exists. Gate 3 trial design and Stage 0 owner acceptance remain future work.

**Best continuation:** inspect live main and PR #21 head/CI; if owner accepts the compatibility proposal, integrate it with the version ledger after CI, preserving source-pinned alternatives. Then decide whether the concrete Hold interlock and physical cutoff make the A/B fixture fair enough to commission targeted review. No branch rebasing or KestrelGaming main synchronization was done: the owner explicitly deferred that unrelated task.

## Evidence

[Original merged game head](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/tree/514ce104bcd3eb3b235df491aca85e36ac0a6a99) · [Proposed SF-0005 change record](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/0ffac72aca224cda2314c35a81db49e8578ff7ec/docs/changes/SF-0005.md) · [Prior source-pinned six-agent Gate 1 record](2026-11-11-stage-fright-gate1-six-reports-reconciliation-d8a630c1.md).

**Agent authorial perspective:** Mothlight — The Invisible Stagehand; shared GitHub credentials do not verify separate runtime identities.

## Superseded by

[Owner-relayed Ven independent PR #21 audit and Mothlight's candidate corrections](2026-11-11-stage-fright-ven-pr21-audit-response-c724c3ae.md). This older record preserves the original merged-stack and correction context, but PR #21 has received further audit-driven design refinement.

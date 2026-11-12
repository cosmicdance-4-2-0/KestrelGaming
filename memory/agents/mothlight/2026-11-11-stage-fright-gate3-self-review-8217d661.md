---
schema: 1
id: 2026-11-11-stage-fright-gate3-self-review-8217d661
kind: lesson
scope: agent:mothlight
status: active
evidence: inferred
author: mothlight
created: 2026-11-11
updated: 2026-11-11
sources: "Owner requested another pass at Stage Fright PR #23 after upstream skills synchronization. Reviewed PR head 8217d661c9f7e1a5d65e3040ed037057ef826d12 against main 16414b1d59a04b9f14164dc9ba05956dbf0db5f9; Kestrel home d0f5a85d8fba539f16caeab83bf02c5ece3df905; GitHub Actions run 43143160818."
---

# Stage Fright Gate 3 — self-review of opportunity coding and scripted controls

## Summary

Mothlight completed an author-side design review of [PR #23](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/pull/23) at `8217d661`. Recommendation: make two bounded protocol corrections before formal Gate 3 adoption. This was a review, not a new independent peer endorsement. The game draft remains unchanged, open, draft and unmerged at the checked revision. No gate was accepted and no gameplay or participant study was performed.

The existing retrospective-cognition, unclassified-inaction, A/B-confounding, complementary C/D transfer, investigator-masking and separate-probe-arm corrections remain present. Preserve those limits. The stronger conclusions below are Mothlight's source-based design inferences, not observed participant failures or attributed peer findings.

## Evidence

### Finding M-G3-R01 — opportunity history must survive late action

[Observation rubric, lines 138–142](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/8217d661c9f7e1a5d65e3040ed037057ef826d12/docs/design/STAGE0_GATE3_JUDGMENT_TRIAL_PROTOCOL.md#L138-L142) groups absent windows, prohibited overlap, inaccessible stations and expired cutoffs as `UNABLE_OR_TOO_LATE`, interpreted as not observing a free choice. Section 5 step 5 and T3-18 repeat this ambiguity.

Paper counterexample, not an executed trace: a preflight-valid B provides a fair evidence-to-Hold route; the participant spends the remaining time rereading or starts another timed job, then requests Hold too late. Gate 2's single active job and irreversible cutoff legitimately prevent that late operation. That does not mean there was never an opportunity. Conversely, an inaccessible control or impossible route is a fixture/technical limitation. Combining them can remove meaningful timing failures from the judgment analysis or overwrite a real late Hold attempt.

Recommended correction: record action (`HOLD_ATTEMPTED`, declared restraint or unclassified nonaction) separately from opportunity history. Distinguish `NO_FEASIBLE_OPPORTUNITY` from `OPPORTUNITY_EXPIRED` after a demonstrated feasible opportunity; record the trace-supported cause or unknown cause without claiming cognition. Keep late requests and receipts. Prior voluntary actions consuming time remain behavioral outcomes under the locked analysis rules; do not automatically exclude them as technical failures. Add paired paper cases covering an impossible fixture and a feasible opportunity subsequently exhausted.

### Finding M-G3-R02 — exhaustive acquisition is confounded with always intervening

[Control policy, line 110](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/8217d661c9f7e1a5d65e3040ed037057ef826d12/docs/design/STAGE0_GATE3_JUDGMENT_TRIAL_PROTOCOL.md#L110) visits every station, then attempts Hold regardless of what was learned. This can measure route/inspection cost, but it does not test whether exhaustive acquisition followed by a simple evidence-based decision trivially solves the toy. A's missed Beat can result from the forced Hold alone.

Paper counterexample, not a measured fixture: if both cases allow all readings before the cutoff, an inspect-all policy using acquired physical clues could refrain in A and Hold in B with no meaningful opportunity tradeoff. The current script instead Holds in both, losing A's Beat and understating that stronger comparator. The optional case-specific evidence-aware reference trace is a feasibility proof, not a frozen common policy that closes this comparison.

Recommended correction: retain the current script if useful, explicitly naming it inspect-all-then-Hold, and separately define an exhaustive-acquisition policy with a fixed observation-driven decision rule. It may use only legally acquired facts, never hidden condition labels or omniscient safety flags. Freeze its route, costs, decision rule and late/ambiguous-evidence handling before confirmation. Alternatively narrow the detector claim to route cost. Inspecting the only mechanism is not inherently a design failure, as the roadmap already states.

### Verified supporting state

- PR diff has exactly four paths: Gate 3 protocol, SF-0007 record, CHANGELOG and version.json. Gate 1/2, roadmap and executable code are unchanged. Proposed integration remains `0.0.2.7/SF-0007`; checked main is `0.0.2.6/SF-0006`.
- Hosted [run 43143160818](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/actions/runs/43143160818) reports successful `check` and `browser-smoke` jobs for the reviewed head. Those are infrastructure checks, not human evidence or executed T3 checks.
- Locally executed `node tools/validate-version.mjs`: passed. Existence check of 13 local Markdown links across the changed documents: no missing targets; external URLs and heading anchors were not checked by that script.
- `git diff --check <base>...HEAD` reports nine Markdown two-space line endings as trailing whitespace. This is an observed formatting warning, not a scientific or runtime defect. No cleanup was made.
- The PixiJS router plus 25 specialized modules are present on the home branch, with 65 imported Markdown files pinned to upstream `83760c6f53462ca9cecd68055041f5a8c94758ce`. The documented v8.22.0 source basis matches Stage Fright's exact `pixi.js` dependency. Read the router, accessibility and ticker guidance; these references do not replace Stage Fright's headless-core and authoritative-tick contracts.
- Before this record, `python3 tools/validate_seed.py` reported 15 inherited memory errors. `python3 -m unittest discover -s tests -v` ran 82 tests with six failures; all five PixiJS import-integrity tests passed. The broader branch is not green. No unrelated historical records were repaired.

The general repeated-exposure rule already requires subsequent runs to be labeled exposed. A technical restart must retain the participant's actual exposure history; this is an application of the existing rule, not a third blocking finding.

## Revisit when

Recheck both findings against any newer PR head. If assigned a correction pass, amend the protocol and its existing SF-0007 documentation together, preserve the four-file scope and earlier inference limits, and add focused paper counterexamples. Do not implement, merge, ratify a gate, dispatch peer agents, publish a review comment or recruit participants based on this memory alone. Owner gate acceptance and later scoped implementation remain separate decisions.

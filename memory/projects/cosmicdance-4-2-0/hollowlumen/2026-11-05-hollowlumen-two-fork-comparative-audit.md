---
schema: 1
id: 2026-11-05-hollowlumen-two-fork-comparative-audit
kind: lesson
scope: project:cosmicdance-4-2-0/hollowlumen
status: draft
evidence: observed
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "Read-only comparative audit on 2026-11-05 of cosmicdance-4-2-0/hollowlumen main 4736ab3bb7fa9cbc316043093a02d9f313c52a51; Kisuul/hollowlumen main c00e15e7af5ba028584363f4be6151a373b084ec; both include ancestor ac0317e250bef11c1f12abebe7be023aa41ecb47."
---

# Axiom — Comparative HollowLumen design/engineering audit

## Summary

**Central assessment:** The forks are complementary: CosmicDance explored product identity, independent creature design, proposed encounters, historical scope reconciliation and branding; Team B created a tested five-screen cottage prototype. Neither has yet implemented or empirically validated the combined game thesis. Do not merge divergent forks wholesale.

**Observed strengths of CosmicDance:**
- Clear separation of pattern definition, critter individual, favorite, household/encounters/world, with later genetics deliberately deferred.
- `docs/CONCEPT_DEMOLITION_REVIEW.md` challenges derivative creature-battler assumptions and proposes a fair combat-vs-Threadwork test rather than dogmatic replacement.
- `docs/PLAYABLE_GAME_HYPOTHESIS.md` and `docs/TEAM_B_SYNCHRONIZATION_BRIEF.md` provide a falsifiable first slice and bounded B-01 analysis-only assignment.
- `docs/CLIENT_REVIEW.md` explicitly marks 30 unresolved client questions, differentiating unapproved hypotheses and evidence.
- Four compact, editable SVG assets with titles/descriptions and no observed external resource refs/scripts. The Lavender & Loop contrast values sampled in `docs/DESIGN_LANGUAGE.md` were independently recomputed to matching reported two-decimal values. 82 Markdown references checked; none had a nonexistent local path.

**Risks and specific corrections:**
1. **Decision overload:** 13 Markdown files (~156,666 characters), no running design experiment and 30 open client questions. Inference: more speculative documentation is lower-value than one discriminating playable test and a prioritized acceptance ledger. No documented client approval on CosmicDance PR #1/#2.
2. **Canon ambiguity during onboarding:** Narrow `docs/PRODUCT_SPEC.md` still says cottage/idle/adventure are removed from the core, whereas later documents reopen them; scope-history banners explain the change. Future agents must follow a canonical current decision ledger rather than treating any older draft as binding.
3. **Brand incompatibility:** Lavender & Loop is not identical to Team B's approved (direction, not rendered UI) Pastel Twilight Craft token set. Same `--hl-*` prefix and overlapping semantic names but different values, e.g. CosmicDance `--hl-canvas #FBF8FF` vs Team B `#FCF8FF`. Do not paste one style sheet into the other or replace the canonical Team B DTCG token JSON.
4. **Product originality and crochet authenticity:** Team B's `src/App.jsx` currently uses `knit`/`purl` for the scarf activity, which are knitting terms despite the clarified crochet-centered concept. This is a source-grounded product-language mismatch, not a game-engine defect.
5. **Widget is a product promise and an engineering unknown:** The actual mobile platform remains unspecified. The web mock is not native. Parallel feasibility spike after establishing favorite ID / renderer projection should not be represented as a working native extension.
6. **No independent project verification infrastructure in CosmicDance fork:** Docs/brand-only repo has no CI. This is not an app-build failure. Future lightweight checks for SVG validity, text/accessibility, Markdown links and design artifacts could improve maintainability. Inline SVG assets reuse generic `title`/`desc` IDs; this becomes an integration collision risk only when multiple source SVGs are inserted inline in the same DOM, not when loaded as separate image resources.
7. **Backend and world-simulation scope:** Proposed Threadwork interactions, inherited traits and expanding RPG systems are unapproved and require matched, small user experiments. Client experience and proven identity persistence take precedence over feature accumulation.

**Recommended next milestone:** Compare CosmicDance's B-01 analysis assignment with Team B's First Thread Gates 0-2; fix a baseline fixture and preserve v1 data; state minimal interfaces for `PatternDefinition`, `Critter`, `Collection`/favorite and `Household`; implement v1→v2 migration with deterministic repeated hydration; only then prototype two household residents and a testable furniture reaction. Distinguish core product direction signoff from code acceptance.

## Evidence

- [CosmicDance product spec](https://github.com/cosmicdance-4-2-0/hollowlumen/blob/4736ab3bb7fa9cbc316043093a02d9f313c52a51/docs/PRODUCT_SPEC.md), [current gameplay hypothesis](https://github.com/cosmicdance-4-2-0/hollowlumen/blob/4736ab3bb7fa9cbc316043093a02d9f313c52a51/docs/PLAYABLE_GAME_HYPOTHESIS.md), [B-01 handoff](https://github.com/cosmicdance-4-2-0/hollowlumen/blob/4736ab3bb7fa9cbc316043093a02d9f313c52a51/docs/TEAM_B_SYNCHRONIZATION_BRIEF.md), [client review](https://github.com/cosmicdance-4-2-0/hollowlumen/blob/4736ab3bb7fa9cbc316043093a02d9f313c52a51/docs/CLIENT_REVIEW.md), [brand](https://github.com/cosmicdance-4-2-0/hollowlumen/blob/4736ab3bb7fa9cbc316043093a02d9f313c52a51/docs/BRAND_PROTOTYPE.md).
- [Team B First Thread roadmap](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/docs/plan/FIRST_THREAD_A_TO_B_ROADMAP.md), [game state](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/state/game.js), [Pip and wander UI](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/App.jsx), [canonical theme tokens](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/docs/design/tokens/visual.tokens.json).
- Repository metadata reports both parents `valubester/hollowlumen`; shared commit `ac0317e250bef11c1f12abebe7be023aa41ecb47` resolved in both repositories with same tree SHA.
- **Verification limits:** Source/doc static inspection and simple checksum/contrast/link checks only; no screenshot rendering, UX playtesting, build, or simulation executed for CosmicDance. Any claim of quality beyond source-grounded facts is an explicit engineering inference.

## Revisit when

The owner/client resolves core gameplay/brand/widget questions, a B-01 response or implementation is accepted, another PR changes the domain schema, or an empirical comparison of small gameplay experiments exists.

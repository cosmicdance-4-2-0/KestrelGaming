---
schema: 1
id: 2026-11-05-hollowlumen-invariant-audit-v1
kind: lesson
scope: project:kisuul/hollowlumen
status: draft
evidence: observed
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "Read-only source and CI inspection of Kisuul/hollowlumen main c00e15e7af5ba028584363f4be6151a373b084ec on 2026-11-05; links and uncertainty in Evidence below."
---

# HollowLumen — Axiom architectural audit, 2026-11-05

## Summary

**Observed boundary:** A viable single-companion cottage prototype is being asked to grow into an individual-creature making/inhabitation game; its identity, save migration and one-time world-consequence contracts are not yet implemented. Proposed Threadwork and RPG systems are hypotheses, not accepted requirements.

**Priority order:**
1. Baseline fixture + exact old Zustand `{state,version}` envelope + deterministic v1->v2 compatibility and failure recovery before adding `Critter.id`/`favoriteId`. `sanitizeSave` currently defaults if `saveVersion !== 1`; Zustand `persist` is version 1 without a `migrate` implementation. Existing values must be preserved.
2. Make rewards and quest transitions domain-owned and testably idempotent before persistent consequences. Currently `Wander.choose` gates completion in React and `finishWander(game,routeId)` awards solely by known route ID. This is acceptable for repeatable prototype wanders, **not** sufficient for once-only quest rewards.
3. Test creation and identity separately from visual customization; the current renderer imports `COLORS` from economy state and UI reads scalar Pip fields.
4. Check appearance/world independence at rendered level: `src/theme/palette.css` ties cottage/hill colors to `data-ui-theme` even when independent `sceneMode` is always-day or always-night. This is an observed coupling, not proof that the design intends identical scene colors under all UI modes.
5. Pin dependencies: no committed `package-lock.json`; CI derives a fresh candidate with `npm install --package-lock-only`. The current workflow only triggers on PR or manual dispatch, not merged main. GitHub reports main not protected. Treat as reproducibility/integration risks.
6. Expand behavioral/a11y validation: the Chromium smoke navigates five routes, toggles gate, tests appearance, screenshots and a night button's contrast, but does not run actual wander, idle, purchase, lost-save recovery, 200% zoom, assistive-tech or native-widget acceptance.
7. Keep live docs current: `docs/PROTOTYPE.md` retains historical claims that browser automation/build were not run, while later CI does run them. The SVG companion always says 'smiling' in its accessible label regardless of face. These are small, confirmed documentation/semantic issues.

**Main success invariant for the next implementation:** An individually named and constructed critter retains the same stable ID, current favorite reference, appearance and ownership across create, select, reload, and repeated hydration without losing existing v1 economy progress.

## Evidence

- [Save sanitizer and economy](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/state/game.js) and [Zustand persistence](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/state/useGame.js).
- [UI session completion and scalar companion](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/App.jsx); [SVG label](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/components/Lumenette.jsx).
- [Theme palette](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/theme/palette.css) and [presentation resolver](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/src/theme/presentation.js).
- [CI workflow](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/.github/workflows/verify-build.yml), [browser smoke](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/tools/smoke-browser.mjs), [GitHub Actions passing PR #7 run](https://github.com/Kisuul/hollowlumen/actions/runs/42043034061).
- [Roadmap](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/docs/plan/FIRST_THREAD_A_TO_B_ROADMAP.md) explicitly marks itself PROPOSED and names most of these gates.
- **Verification limitation:** Source inspection and reported workflow results only; no local checkout, build, screenshot rendering or runtime mutation was performed as part of this audit. Findings about potential consequences are inferences, not reproduced end-user defects.

## Revisit when

A v1 save migration fixture or v2 schema lands, an accepted product direction resolves the gameplay hypothesis, or CI/browser findings are reproduced/refuted by a new revision.

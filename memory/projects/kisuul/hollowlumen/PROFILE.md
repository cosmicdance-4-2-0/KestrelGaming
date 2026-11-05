---
schema: 1
id: 2026-11-05-hollowlumen-project-profile
kind: profile
scope: project:kisuul/hollowlumen
status: active
evidence: observed
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "https://github.com/Kisuul/hollowlumen at main c00e15e7af5ba028584363f4be6151a373b084ec; README.md, package.json, src/state/, src/theme/, src/solar/, docs/plan/FIRST_THREAD_A_TO_B_ROADMAP.md, .github/workflows/verify-build.yml, tests/, GitHub Actions PR #7 run 42043034061."
---

# HollowLumen — project context (Axiom)

## Summary

- Implementation authority: `Kisuul/hollowlumen`. The separately referenced `cosmicdance-4-2-0/hollowlumen` documents are nonbinding design research, not a branch to merge wholesale.
- At 2026-11-05 main SHA `c00e15e7af5ba028584363f4be6151a373b084ec`: React/Vite five-route client-side game prototype; pure `src/state/game.js` economy; Zustand local persistence v1 in `src/state/useGame.js`; separate appearance preferences and fictional solar model.
- Current game is one mutable, customizable Pip and local-only earnings; no distinct persistent critter identities, pattern construction, multiple residents, native widget, or persistent world quest flags.
- Approved visual *palette choices* are documented, but rendering and end-to-end play acceptance are separate gates. `docs/plan/FIRST_THREAD_A_TO_B_ROADMAP.md` is a **proposed** plan, not a client-approved gameplay specification.
- Current direction's critical path: preserve working v1 baseline, clarify scope, migrate individual identity/saves, then prototype inhabitation and meaningful making before expanding adventure systems.
- This assessment was read-only with respect to HollowLumen; repository connector reported pull-only access.

## Evidence

Observed source: [main tree](https://github.com/Kisuul/hollowlumen/tree/c00e15e7af5ba028584363f4be6151a373b084ec), [prototype](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/docs/PROTOTYPE.md), [proposed plan](https://github.com/Kisuul/hollowlumen/blob/c00e15e7af5ba028584363f4be6151a373b084ec/docs/plan/FIRST_THREAD_A_TO_B_ROADMAP.md). GitHub Actions run [42043034061](https://github.com/Kisuul/hollowlumen/actions/runs/42043034061) reported success for PR #7 head `5e4feb7165ece3504e8f16ca7b89f8b11fa07cd9`, including tests, build, Chromium smoke. No independent build/test was run in Axiom's audit environment; network-backed checkout was unavailable.

## Revisit when

Implementation main moves, the original designer accepts a concrete game-loop hypothesis, save schema changes, a package lockfile is committed, or new runnable acceptance evidence exists.

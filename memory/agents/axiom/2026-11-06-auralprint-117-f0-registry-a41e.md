---
schema: 1
id: 2026-11-06-auralprint-117-f0-registry-a41e
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "cosmicdance-4-2-0/Auralprint1 v117_dev ff547056542a10e3fbf1ae2010248d4558e55dda; architecture/117-foundation-invariants db9dfaf2886553f0a6c68b0cbb47e283ccfeef40; PR #111; GitHub source/test/contract inspection 2026-11-06."
---

# Auralprint 117 — Axiom F0 invariant foundation checkpoint

## Summary

**Outcome: PARTIAL (review submission complete; F0 owner acceptance pending).** Under explicit user instruction to begin Auralprint 117 Foundation F0, prepared a documentation-only Canon 116 invariant/boundary registry in a dedicated Auralprint1 development branch. The review artifact lives in [Auralprint PR #111](https://github.com/cosmicdance-4-2-0/Auralprint1/pull/111), base `v117_dev@ff547056542a10e3fbf1ae2010248d4558e55dda`, head `db9dfaf2886553f0a6c68b0cbb47e283ccfeef40`; three commits, no merge.

The [registry](https://github.com/cosmicdance-4-2-0/Auralprint1/blob/db9dfaf2886553f0a6c68b0cbb47e283ccfeef40/docs/development/build-117-f0-invariant-registry.md) defines 20 protected families A01–D04 (CONFIG, preset/schema/import atomicity, source/Queue/Analysis, Orb/Ring/resource clocks, Camera/renderer, recorder/UI/distribution/performance) and six candidate proof gates F1-AN-01/02, F2-VIZ-01/02/03, F3-MIG-01. Every family has a current source owner, breaking counterexample, test pointer and explicit gap where needed. The existing November 2 architecture-preparation checkpoint received a follow-on link; its historical results were not rewritten.

## Evidence

**Directly observed:** GitHub branch `v117_dev` resolved to the pinned SHA; AGENTS, ROADMAP, source modules and selected named tests were read from that revision. Exact head comparison returned only `docs/development/build-117-f0-invariant-registry.md` (new) and `docs/development/build-117-architecture-preparation.md` (follow-on pointer). Remote-tree comparison resolved all 145 local Markdown links in those two documents, all 20 IDs were distinct and no trailing-whitespace lines remained. Protected application/Canon/fixture paths were absent from the diff. PR #111 was opened, not merged.

**Not executed:** Local `git clone` failed because GitHub DNS resolution was unavailable. No `npm ci`, `npm test`, `npm run build`, `git diff --check`, native browser/device checks or independent Canon checksum computation was performed. Historical B0–B2 tests/benchmarks remain attributed to their original run, not to this F0 review. The validator on the Axiom memory repository was likewise not run as part of this record.

**Key engineering distinction:** the accepted AnalysisFrame is a reused borrowed view; its readiness and buffer replacement are source-visible, but a sample sequence, source/definition epochs, timestamp domains, snapshot retention and independent scheduling are **not** shipped 116 guarantees. F1 must choose and prove them, not smuggle them into a claim of historical parity. Generic Visualizer failure isolation/type registration and a persisted plugin format are likewise unaccepted proposals. Held Auralprint PR #109 is excluded from `v117_dev`.

## Revisit when

1. PR #111 receives an owner review/merge decision or its head changes. Recheck the exact head and reconcile the invariant registry, without calling F0 accepted prematurely.
2. Stage 0 B3/B4 evidence is assigned or collected. B5–B7, Hero and representative device/lifetime evidence remain separately open; do not promote Stage 0 on the F0 registry.
3. F1 Analysis or F2 Visualization interfaces are proposed. Use the registered counterexamples and negative/protected controls; preserve CONFIG precedence, schema-16 wire meaning, L/R/C, update/resource/draw ordering and owned cleanup. Require separate owner decisions on interface versioning, rendering strategy and migration/rollback.
4. Auralprint accepted source changes or the target branch diverges. Re-pin the source before assuming any mapping still holds.

**Next useful action:** Request independent architecture/source review of [PR #111](https://github.com/cosmicdance-4-2-0/Auralprint1/pull/111); resolve omissions/contested assertions; then seek explicit F0 acceptance and separately scope F1 Analysis contract design. Do not touch Canon, held PR #109 or application source as part of this F0 note.

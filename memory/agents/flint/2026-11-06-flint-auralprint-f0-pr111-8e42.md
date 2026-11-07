---
schema: 1
id: 2026-11-06-flint-auralprint-f0-pr111-8e42
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-auralprint-f0-review-session
created: 2026-11-06
updated: 2026-11-06
sources: "cosmicdance-4-2-0/Auralprint1 PR #111 @db9dfaf2886553f0a6c68b0cbb47e283ccfeef40, follow-up correction @8a23cf37a0bf7959ad043eb86e8d727a4976c93d; v117_dev@ff547056542a10e3fbf1ae2010248d4558e55dda; GitHub Actions run 42311076951; exact source and tests inspected 2026-11-06."
---

# Flint — Auralprint Build 117 F0 PR #111 review

## Summary

**Individual verdict for PR #111 at `db9dfaf2886553f0a6c68b0cbb47e283ccfeef40`: REQUEST CHANGES (one bounded documentation correction).** The source/test mapping, 20 invariant families, six pending design/proof gates and refusal to promote Stage 0/1 or invent an ABI are proportionate for an F0 documentation checkpoint. No production source changes appear in this PR.

**Blocking precision issue:** B06's heading claims borrowed AnalysisFrame data *has an explicit validity boundary*, but the same row and `src/js/audio/analysis-frame.js` establish no sequence, source/definition epoch, timestamp or retained snapshot lifetime. Change only the heading to e.g. "**B06 — AnalysisFrame exposes borrowed producer data; freshness and retention contracts remain unresolved.**" Preserve the mapped evidence and F1-AN-01 decision.

**Optional, not blockers:** Add a clause under B03 protecting the Scrubber's decoded-file waveform path from being conflated with the live FFT/AnalysisFrame path (`AGENTS.md` §3.3, `src/js/audio/scrubber.js`, waveform tests); do not add a 21st row. D04 is a verification/evidence gate rather than a behavioral invariant; classify accordingly if editing.

This is Flint's independent, source-based documentation review, not agreement or disagreement attributed to Axiom. At the original review checkpoint, no PR review was submitted and no Auralprint files were modified.

## Evidence

- Inspected PR metadata, both changed documentation files, Auralprint `AGENTS.md`, ROADMAP, prior Build 117 preparation/baseline, and relevant pinned source/test files through the GitHub connector. PR is open, head `db9dfaf2886553f0a6c68b0cbb47e283ccfeef40`, base `ff547056542a10e3fbf1ae2010248d4558e55dda`; 2 documentation files (+110, -0).
- GitHub Actions run [42311076951](https://github.com/cosmicdance-4-2-0/Auralprint1/actions/runs/42311076951) confirms `head_sha=db9dfaf2886553f0a6c68b0cbb47e283ccfeef40` and completed success. Both Ubuntu and Windows test/build/packaging/whitespace jobs succeeded; Ubuntu additionally completed its browser smoke gates. These are **CI-executed**, not independently rerun local gates.
- Independently enumerated the pinned tree (1,050 entries, not truncated) and checked 111 relative links in the new registry plus 34 in the preparation document: all 145 link destinations exist. This verifies destinations, **not** Markdown anchor fragments or external links.
- Source inspection: `src/js/audio/analysis-frame.js` reuses frame/channel objects and borrows producer arrays; `tests/analysis-frame.test.js` asserts reference identity and replacement after BandBank rebuild; `src/js/main.js` samples/updates on each delivered app rAF. These support the no-versioned-lifetime conclusion. No source execution was claimed.
- `git ls-remote` from the local container failed with `Could not resolve host: github.com`; no independent local `npm ci`, `npm test`, `npm run build` or `git diff --check` on Auralprint was executed. GitHub CI covers the pinned head but does not prove future contracts.

## Correction applied — 2026-11-06

Following the user's explicit authorization to correct PR #111 directly, updated only the B06 title in `docs/development/build-117-f0-invariant-registry.md` on `architecture/117-foundation-invariants`:

> B06 — AnalysisFrame exposes borrowed producer data; freshness and retention contracts remain unresolved.

**Auralprint commit:** [`8a23cf37a0bf7959ad043eb86e8d727a4976c93d`](https://github.com/cosmicdance-4-2-0/Auralprint1/commit/8a23cf37a0bf7959ad043eb86e8d727a4976c93d), parent `db9dfaf2886553f0a6c68b0cbb47e283ccfeef40`. GitHub returned one changed file, one line added and one removed; fetched final document confirms old B06 title absent and corrected title present. PR #111 updated to that exact head and remains open. **Original B06 review blocker resolved.** The optional Scrubber and D04 suggestions were deliberately not included. No merge or PR review was submitted.

The earlier CI result applies to the prior head only; current-head CI and local full tests were **not independently reproduced** by Flint at this correction checkpoint. The original REQUEST CHANGES verdict remains part of the evidence trail for the original reviewed SHA, not the revised document.

## Revisit when

The PR head changes, the B06 title is corrected, source/runtime assumptions change, or the owner requests a broader proof. Reread exact new SHA and rerun relevant parity checks before changing verdict. Do not promote F0 approval to Stage 0/1 acceptance or migration authority.

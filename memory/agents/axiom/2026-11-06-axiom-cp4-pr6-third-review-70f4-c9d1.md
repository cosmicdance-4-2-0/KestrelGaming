---
schema: 1
id: 2026-11-06-axiom-cp4-pr6-third-review-70f4-c9d1
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "KestrelGaming PR #6 initial Studio base 4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a; previously reviewed b34202540eb4c860caa732ef8f98b23529d12bd3; reviewed current head 70f4a449736bfccfb19a716e772b2e81f0225b09; source-matched validator Git blob d107cad5963736620224bc671037740d299fb745; 83 isolated probes/controls, CommonMark rendering and source review on 2026-11-06."
---

# Axiom — PR #6 independent third review: 70f4a449

## Summary

**Verdict: REQUEST CHANGES for exact PR head `70f4a449736bfccfb19a716e772b2e81f0225b09`.** Both previously identified blocking classes (wrong linked agent destination and misleading multiline code/HTML catalog references) are now correctly rejected. All five earlier blockers stay rejected. A new, narrow **P2 catalog-link recognition bypass** remains: an apparent team link solely inside another Markdown link's quoted title satisfies catalog registration, even though rendered Markdown has no navigable team link. This defeats the exact discoverability invariant targeted by CP4. A bounded check, not a general Markdown engine, is sufficient.

**Pins:** Base Studio `meta/team-contracts-v1@4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a`; previous PR head `b34202540eb4c860caa732ef8f98b23529d12bd3`; new PR head `70f4a449736bfccfb19a716e772b2e81f0225b09`. Axiom home `99b2fd0034038f2d759aa1ff7f6518b2deb21a03` at this review's pickup, prior to saving this record. The PR remained open, unmoved and unmerged. Git commit tree `da76d589a5df32dc732e75e4cf659e07676c50f5` was observed, not independently reproduced as a full local checkout.

The architect's [shared reconciliation](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a/docs/STUDIO_ARCHITECTS_REVIEW_RECONCILIATION_2026-11-05.md) governs checkpoint order. The preceding [Axiom b342025 review](2026-11-06-axiom-cp4-pr6-followup-b342-review-e6d2.md) retains the prior history; this note records only new observations.

### Reproduced remaining P2 blocking case

Start with a valid 3-member synthetic Architects TEAM.md, JSON profile and roster. Replace the entire `teams/INDEX.md` with:

```markdown
[Some Other Resource](elsewhere.md "[The Architects](architects/TEAM.md)")
```

**Expected:** Rejection: no visible usable link to `architects/TEAM.md`.

**Actual:** `validate_team_contracts(root) == []`. CommonMark rendered HTML has **only** `<a href="elsewhere.md" title="[The Architects](architects/TEAM.md)">Some Other Resource</a>`, so no team navigation exists. Same outcome with single-quoted link titles and image title text. Source: `tools/validate_team_contracts.py` `_catalog_has_team`: regex searches `[The Architects](architects/TEAM.md)` anywhere in the remaining text, including a different link's title, without resolving actual link syntax.

**Minimum correction:** Recognize the team link only as actual local navigation, excluding links spelled solely inside another link/image's title. Add one negative fixture plus a positive conventional visible link with optional quoted title. No v0.2 schema migration and no prose semantics interpreter justified.

### Secondary P3 valid-input compatibility

A catalog containing `A<B in source notation` followed by a valid conventional `[The Architects](architects/TEAM.md)` link is rejected because `_catalog_has_team` treats `<B` as raw HTML by regex `<[/!?A-Za-z]`. CommonMark renders this as ordinary escaped text, not HTML. This is an observed false rejection in otherwise legitimate explanatory prose. Prefer a documented, proportionate boundary or a more precise raw-HTML recognizer. Not independently a merge blocker.

### Passed controls and scope

- Five original Axiom/Flint blockers stay rejected: duplicate contradictory Composition section; HTML-comment/indented-code-only table; HTML-comment/image-only catalog.
- Both b342025 blockers closed: Axiom label pointing to Flint or unrelated repo, relative/script/query link targets; catalog team link solely in multiline backtick span or raw HTML attributes/body.
- Valid linked Axiom/Flint/Harbor canonical branch rows, unlinked and mixed branch labels, title links, `./` links, normal comments/fences, case/identity spacing, real navigation with accompanying code examples all pass. Wrong role, branch prefix, missing or duplicate Harbor, duplicate JSON keys, typed authority/memory violations, missing header/separator, wrong identity and unclosed comment reject.
- Static inspection of actual Architects contract/profile at reviewed head confirms the three role and branch links match `source_repository` exactly; populated two-member prose template uses new header/separator conventions. JSON schema v0.1 is unchanged.
- The changed Auralprinter handoff is outside this final 3-file delta, and its prior PARTIAL/COMPLETE/proposal meaning remains unchanged. No direct project application code changes.

## Evidence

Executed against `tools/validate_team_contracts.py` whose **local Git blob `d107cad5963736620224bc671037740d299fb745` exactly matched GitHub's file blob at head**: 31 previous probes/controls after normalizing their previously noncanonical example URLs (28 expectation checks + 3 malformed/symlink controls), 45 additional independent controls (all expected outcomes), and 7 direct CommonMark-rendered catalog-title/compatibility probes (four false accepts, one false rejection, two passing controls); **83 checks/controls total**, some intentionally overlapping failure classes. Python 3.13.5; `python -m py_compile` passed. A local two-commit Git fixture passed `git diff --check HEAD~1 HEAD` for the validator-only follow-up change. The full seven-file PR diff was retrieved and all 429 added lines scanned for trailing whitespace: no findings. This **is not** the full repo diff-check gate.

**Not independently run:** `python3 tools/validate_seed.py`, `python3 -m unittest discover -s tests -v`, full `git diff --check 4fdc83e... 70f4a44...` on a full checkout; direct GitHub clone was blocked by DNS. Implementer's 116 passing tests (including their tests on Python 3.12.14) are attributed to the implementer and not claimed reproduced. GitHub returned no Actions runs/statuses for this exact commit when queried. A runnable source-matched evidence ZIP was generated in the originating chat, not committed to the public repo.

This was read-only inspection and isolated local execution. No PR edit, merge, Studio branch edit, PR comment, Checkpoint 5 work, or represented peer consensus.

## Revisit when

PR #6 advances, the catalog title counterexample is rejected by a change at a new exact SHA, an independent full-checkout gate runs, or the Studio architect explicitly changes the navigation guarantee with an evidence-based reason. Re-resolve current heads and recheck the valid-input controls.

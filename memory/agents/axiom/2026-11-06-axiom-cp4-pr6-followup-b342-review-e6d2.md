---
schema: 1
id: 2026-11-06-axiom-cp4-pr6-followup-b342-review-e6d2
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-06
updated: 2026-11-06
sources: "KestrelGaming PR #6 base 4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a, initial head 1c7bd337db3b6d2ff1660a6d690569529ae7138e and follow-up head b34202540eb4c860caa732ef8f98b23529d12bd3; exact Git blob for follow-up tools/validate_team_contracts.py b25dce67ea2ca2cc4c71ddce0772d60b106ac78c; 48 isolated local Python probes on 2026-11-06; Axiom previously published CP4 independent review a8f2."
---

# Axiom — Checkpoint 4 PR #6 follow-up independent review

## Summary

**Verdict: REQUEST CHANGES at exact PR head `b34202540eb4c860caa732ef8f98b23529d12bd3`.** The bounded follow-up resolves all five earlier blocking examples, explicitly documents the narrower Markdown table syntax, retains typed schema 0.1 and addresses ordinary link/title compatibility. But further independently exercised cases show a **wrong linked agent-home destination** can be accepted, and **non-navigable catalog content** can still satisfy the registration check. Do not merge on the strength of the implementer's reported 113 tests alone.

**Reviewed sources:** Studio base `4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a`, previous reviewed head `1c7bd337db3b6d2ff1660a6d690569529ae7138e`, new review head `b34202540eb4c860caa732ef8f98b23529d12bd3`. Axiom home was `95765b13d5cb446eda6d448800a24eea3197b1e3` before this record. Studio and review branches matched supplied SHAs at inspection, PR remained open, no branch drift. Read follow-up diff and complete PR scope and previous report; common Kestrel contract/agent continuity remain individually scoped. The [architect reconciliation](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a/docs/STUDIO_ARCHITECTS_REVIEW_RECONCILIATION_2026-11-05.md) remains the shared decision record.

### Original blockers — now rejected

Reran previous five mutations using source-matched new validator: duplicate conflicting operative Composition headings; only composition rows inside HTML comment; only rows indented into Markdown code; catalog registration only in HTML comment; catalog registration only as image. **All five are now rejected.** Safe catalog links with optional `./` or quoted title pass. A valid synthetic three-member profile and normal table pass. Other exercised controls cover wrong roles/branches, duplicate or missing members, duplicate JSON keys, fenced requirements, wrong identity, typed permissions and continuity prohibitions, malformed data and symlinks.

### New observed defects

1. **P1/P2 — linked branch target contradicts canonical home locator.** The operative first and second cells can read `Lead — Axiom` and `[`agents/axiom-v1`](https://github.com/cosmicdance-4-2-0/KestrelGaming/tree/agents/flint-v1)` and the validator returns `[]`. Relative unrelated targets and `javascript:alert` also return `[]`, because `_check_composition()` captures only the displayed code label and permits any non-whitespace link target. **Expected:** reject a clickable home URL that does not resolve to the same canonical agent branch; **actual:** accepted. This is a machine-parsable mismatch and manual pickup hazard, not arbitrary prose semantics. Small correction: compare an optional link destination with the canonical repository + branch locator (or explicitly constrain/forbid linked form and update the real Architects accordingly), preserving unlinked code labels. Test the existing real Architects GitHub URLs and intentional wrong-branch links.
2. **P2 — catalog claims navigation using a multi-line inline code span.** Source:
   `Example: \`not a link\n[The Architects](architects/TEAM.md)\nstill not a link\``.
   A CommonMark parser renders the entire example as code without an anchor, but `_operative_markdown()` masks inline code one line at a time, so `_catalog_has_team()` sees a fake link and returns true. **Expected:** missing catalog registration; **actual:** `validate_team_contracts()==[]`. Another no-navigation example `<div data-note="[The Architects](architects/TEAM.md)"></div>` also passes because the link text is inside an HTML attribute. Minimal remedy: fail closed or mask supported multi-line inline code, and do not accept link syntax solely inside HTML tag attributes; add these tests. The documentation explicitly claims inline code and hidden references do not register a team.

These are semantic reference integrity failures within machine-readable syntax; a general Markdown parser or unconstrained prose keyword policing is unnecessary.

### Compatibility and restraint

The follow-up now requires exactly one root-level operative Composition section, a conventional pipe table headed `Role` / `Individual home`, at least three separator dashes, contiguous complete rows with equal cell counts, and recognized literal or linked backticked home labels. This **does change accepted Markdown** without changing JSON schema v0.1. It is documented and justified by the originally accepted hidden/contradictory declarations; normal Architects layout and synthetic table controls conform. Unusual HTML layouts, nested Markdown blocks, pipe escapes and arbitrary prose truth are outside the expressly stated contract syntax and are not independently classified as new violations merely because a general Markdown renderer could parse them.

The unrelated Auralprinter handoff status formatting change remains the same as in previous PR head: A1 PARTIAL, AP-A1-01a COMPLETE and merged, ADR-011 proposal only; no status transition or application code change.

## Evidence

- Read GitHub PR #6 metadata, the specific follow-up commit patch (four files), full PR scope, and validator at exact head. **Local reconstructed validator Git blob `b25dce67ea2ca2cc4c71ddce0772d60b106ac78c` matched GitHub exactly.** The prior baseline harness source was `0e0ff8120134e6cf0f88bb93cdc904ecd562f90d`. This establishes the tested implementation bytes, not host-execution equivalence.
- Executed **31 prior probes** (28 fixture cases + 3 separate malformed/roster/symlink controls) and **17 new cases** (48 total) under Python 3.13.5 in temporary directories. The original five now reject. Four new unexpected accepts are source-specific variations of the two new findings. The independent probe ZIP, including the exact source, runnable fixtures and logs, was produced in the current ChatGPT conversation but is not committed to this repo.
- `python -m py_compile` succeeded for validator and probe scripts; a local two-commit Git fixture produced a clean `git diff --check HEAD~1 HEAD` for **validator only**.
- **Not executed:** Full `python3 tools/validate_seed.py`, `python3 -m unittest discover -s tests -v` for the complete repository, and `git diff --check 4fdc83e... b342025...` for the **full seven-file PR**. Direct container GitHub access failed DNS resolution. Implementer-reported 113 tests/37 team tests on Python 3.12.14 were not independently reproduced. GitHub status and workflow queries returned no checks or workflow runs for this commit; not evidence of CI failure.
- No PR edits, merge, PR comments, engineering correction, or Checkpoint 5 activity. This record is attributed independent review, not a peer consensus or a claim of a production defect.

**Review gate:** Fix the two reference integrity classes, rerun the minimal negatives plus real Architects/template positive controls, and secure the full checkout-level gates with exact SHA/environment provenance. The required change is narrow; preserve the work already done.

## Revisit when

PR #6 advances beyond `b34202540eb4c860caa732ef8f98b23529d12bd3`, independent evidence falsifies the examples or establishes a bounded alternate authoring policy, or the architect asks for a narrowly scoped re-review. Always re-resolve branch heads; prior test success does not certify an amended revision.

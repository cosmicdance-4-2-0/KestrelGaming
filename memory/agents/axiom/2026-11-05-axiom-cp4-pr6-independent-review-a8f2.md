---
schema: 1
id: 2026-11-05-axiom-cp4-pr6-independent-review-a8f2
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "KestrelGaming PR #6 reviewed exactly at head 1c7bd337db3b6d2ff1660a6d690569529ae7138e against Studio base 4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a; byte-matched submitted validator Git blob 0e0ff8120134e6cf0f88bb93cdc904ecd562f90d; isolated CPython 3.13.5 negative/positive probes 2026-11-05; original Axiom Studio audit and canonical Architect reconciliation."
---

# Axiom — Independent CP4 PR #6 review: Request changes

## Summary

**Verdict: REQUEST CHANGES before integrating Checkpoint 4.** The submitted patch fixes major original failures (wrong role/branch mappings, duplicate keys, fenced code, index absence, typed no-authority checks) without schema v0.1 migration. However, the validator continues to accept **non-operative** team membership assertions and **multiple contradictory operative composition sections**. Catalog checking also accepts non-navigable references.

**Exact reviewed references:** PR `https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/6`; review branch `fix/team-contract-parity-checkpoint4` at `1c7bd337db3b6d2ff1660a6d690569529ae7138e`; base `meta/team-contracts-v1@4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a`; Axiom home `c57fa06681ca772abd4a341e1887eb63c47871da` before this memory write. No PR head drift was detected. Source files and full six-file PR patch were examined using the authorized GitHub connection. The established [reconciliation](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a/docs/STUDIO_ARCHITECTS_REVIEW_RECONCILIATION_2026-11-05.md) remains authoritative for checkpoint order.

### Merge-blocking counterexamples

All start from a valid synthetic 3-member Architects team fixture: proper schema, roster, catalog, headings and composition table. Input is changed in one respect per case. **Expected: reject. Actual: `validate_team_contracts(root) == []`.**

1. **P1 — duplicate competing operative composition sections.** Append a second exact `## Composition — different instincts, not averaged identities` section declaring Flint lead and Axiom counterweight. `_check_composition()` uses `re.search` and parses only the first; neither the heading validator nor other logic rejects duplicate operative sections. A human reader sees a contradiction.
2. **P1 — hidden rows accepted as operative.** Put the only legitimate composition table inside an HTML comment (`<!-- ... -->`) or indent each line four spaces (Markdown indented code). Both pass because `_operative_markdown()` strips fenced code only, and `_check_composition()` strips leading spaces from purported rows. A reader sees no operative team composition.
3. **P2 — catalog non-links accepted.** Replace the only navigable registration with `<!-- [The Architects](architects/TEAM.md) -->` or `![The Architects](architects/TEAM.md)`. The catalog regex accepts both, though the former is invisible and the latter is an image rather than a navigation link.

These defects concern precise, mechanically recognizable clauses and do not justify implementing a general Markdown semantics engine. Minimum correction: reject repeated operative composition sections; exclude HTML comments and indented code from requirements/role rows and catalog registration; distinguish real Markdown navigation links from image references, and add reproductions as negative tests. Preserve the existing valid Architects and template layout.

### Compatibility and optional questions

- A usable conventional link with a title (`[The Architects](architects/TEAM.md "Founding team")`) or a `./architects/TEAM.md` prefix is rejected by the exact catalog regex. These are valid Markdown links but outside the narrow documented `team-id/TEAM.md` string. **P3 proportionality recommendation**, not an independent merge blocker: either permit these safe variants or explicitly state why the restricted link spelling is part of the v0.1 contract.
- Pipe-delimited member lines lacking a Markdown header/separator are accepted as a "table"; similarly, a subheading suggesting illustrative roles is not distinguished. Clarify the operative table grammar, avoiding brittle overgeneralization. The current formal grammar is bounded but only partly a rendered-table grammar.
- Arbitrary prose that claims a vote, authority, or independent execution still passes by design. This is the acknowledged static-semantic boundary and **not** a new finding of real privilege escalation.

### Confirmed positive/negative controls

A complete, linked three-member table passed. Swapped roles, wrong branch suffix `flint-v11`, omitted/duplicated Harbor row, unexpected Kite, duplicate team-profile and roster JSON keys, fenced-only rows/headings, bad team ID, absent/fenced catalog registration, nonempty typed permissions, non-null team memory scope, federated default and dangling teams-directory symlink were rejected. Harmless identity whitespace was accepted. The first synthetic audit script ran 28 numbered fixture probes: 19 matched their declared expected outcomes, 9 diverged (five substantive hidden/ambiguous declaration cases, two standard-link false rejections, two table-grammar questions); three further filesystem/parse controls behaved as expected. The findings are not claims that production Architects files currently contain contradictions.

**Baseline repair:** The unrelated Auralprinter project handoff changed `**Task outcome:** PARTIAL for the full A1 milestone; AP-A1-01a COMPLETE and merged.` to a standalone `**Task outcome:** PARTIAL` plus the equivalent explanation in the following paragraph. Verified both blobs and surrounding prose. A1 remains partial; AP-A1-01a remains complete and merged; ADR-011 remains a proposal.

## Evidence

- Validated that the local reconstructed `tools/validate_team_contracts.py` has Git blob `0e0ff8120134e6cf0f88bb93cdc904ecd562f90d`, exactly matching GitHub PR head. The baseline file from the earlier independent Axiom harness matched baseline Git blob `6e29e92698264b3ef3b526ee04743a5a13718941`. The local patch source was independently compiled and executed under CPython 3.13.5.
- Executed 28 isolated temporary fixture probes plus 3 additional malformed-roster/profile and dangling-symlink controls. Five material acceptance failures are given above; full run logs and runnable Python fixtures were returned to the originating ChatGPT conversation in a separately downloadable ZIP. These fixtures are **not** a substitute for a complete repository checkout.
- Ran `python3 -m py_compile` for the submitted validator and local probe harness. Ran `git diff --check` on a local one-file Git fixture containing the byte-matched baseline and submitted **validator only**; it produced no whitespace diagnostics and exited 0.
- **Not executed:** `python3 tools/validate_seed.py`, `python3 -m unittest discover -s tests -v` for the full checkout, and the required six-file `git diff --check <base> <review>`. The available container could not resolve github.com, and the entire repository was not materialized. Implementer-reported 104 passing tests (28 team tests) on Python 3.12.14 were not independently reproduced. GitHub returned no workflow runs for the exact PR commit when queried; this is absence of evidence, not proof of a CI failure.
- Static inspection confirms the real Architects team uses the expected role labels, exact home branches, and catalog target. Runtime full-checkout validity is unverified in this review.
- No review branch edit, merge, PR comment, or Checkpoint 5 implementation was undertaken. Other engineers' findings are attributed to their original reviews, not treated as newly executed by Axiom.

**Acceptance needed before integration:** Include at least the five counterexamples as reproducible negative tests and confirm they now fail closed. Then run the complete Studio validation/test/diff gates on a real checkout with source SHA and environment evidence. The host-only pickup/continuity obligations properly remain Checkpoint 5.

## Revisit when

PR #6 receives a bounded follow-up commit with repaired operative Markdown/catalog recognition and additional negative tests; a checkout-level full test run is independently verified; or the Studio architect disputes the classification of HTML comments, indented code, duplicate headings or image-only catalog entries as non-operative references. Re-review new head explicitly; do not assume this verdict automatically applies to later revisions.

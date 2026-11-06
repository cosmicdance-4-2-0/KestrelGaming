---
schema: 1
id: 2026-11-06-flint-cp4-pr6-minimum-enforcement-c41e
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-cp4-review-session
created: 2026-11-06
updated: 2026-11-06
sources: "KestrelGaming PR #6 fix/team-contract-parity-checkpoint4@1c7bd337db3b6d2ff1660a6d690569529ae7138e, base meta/team-contracts-v1@4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a; submitted validator Git blob 0e0ff8120134e6cf0f88bb93cdc904ecd562f90d; 18 isolated synthetic probes under CPython 3.13.5 on 2026-11-06; Axiom independently reported CP4 review in memory/agents/axiom/2026-11-05-axiom-cp4-pr6-independent-review-a8f2.md at 95765b13d5cb446eda6d448800a24eea3197b1e3."
---

# Flint — PR #6 review: minimum sufficient contract enforcement

## Summary

**Verdict: REQUIRES CORRECTION before integration.** Preserve the substantive CP4 fixes already in PR #6; its remaining defects are ambiguous recognition of operative Markdown, not an argument for a general Markdown parser or v0.2 migration. Adopt one explicit narrow composition-table grammar, a single operative Composition heading, and real catalog navigation links. Contract v0.1, individual identity and authority limits remain unchanged. This is Flint's independently executed follow-up of previously reported Axiom counterexamples, not a second original discovery claim.

## Evidence

- Reviewed the complete six-file PR patch, current template and Architects contract, the shared reconciliation, Flint founding audit, and Axiom's separately attributed CP4 review.
- Reconstructed `tools/validate_team_contracts.py` in a disposable local directory and verified `git hash-object` equals submitted Git blob `0e0ff8120134e6cf0f88bb93cdc904ecd562f90d`; `python3 -m py_compile` passed on Python 3.13.5.
- Executed **18 targeted synthetic fixtures**, with a valid three-member table as positive control. **All five Axiom merge-blocking cases reproduced**: a second contradictory Composition section, HTML-comment-only membership, four-space-indented-code-only membership, comment-only catalog registration, and image-only catalog registration each returned an empty error list. Additional probes found HTML-comment-only required heading accepted, role-only rows without a Markdown table header/separator accepted, and conventional catalog links with a title or `./` prefix incorrectly rejected.
- Positive controls accepted: valid three-member layout, harmless identity whitespace. Negative controls rejected as intended: changed branch suffix, role swap, duplicate member, and fenced-only role rows. All probes were isolated fixtures, not claims that the real Architects files contain those changes.
- The small Auralprinter handoff patch separates `**Task outcome:** PARTIAL` from explanatory text while retaining A1 PARTIAL, AP-A1-01a complete/merged, and ADR-011 proposed; no application modifications were made.
- The implementer's 104 full-suite passes are attributed to the PR description; **not independently reproduced**. No complete GitHub checkout was available because the container could not resolve github.com. Full `validate_seed.py`, full unittest discovery and six-file `git diff --check` remain **NOT RUN** in Flint's review.

## Correction design (proposal only)

1. Extend `_operative_markdown` to mask HTML comments and indented code as well as fenced code when scanning headings, members and catalog; fail closed on malformed unmatched comments in required declarations.
2. In `_check_composition`, demand **exactly one** visible top-level Composition section and one conventional table immediately after that heading (optional blank lines; header + separator + contiguous member rows), with complete role/branch parity against typed PROFILE.json. Examples and alternate role mappings must be fenced, not competing operative tables. Maintain the real four-column Architects format and the two-member template.
3. Match a *navigation link*, not an image or hidden text, in the catalog. Support optional `./` and a conventional quoted Markdown title without accepting arbitrary destinations; catalog stays navigation, not a roster.
4. Add negative cases for every reproduced failure and positive controls for the real Architects, 2-member template shape, ordinary catalog-link variants, benign comments/examples and harmless whitespace. The current synthetic fixture's headerless role rows must change to a real table to test the documented contract rather than implementation assumptions.
5. Do not add a dependency, extra synchronization layer, global Markdown renderer, new schema, team memory or CP5 work. Do not promise detection of arbitrary prose authority claims; host permissions and genuine independent execution are outside static validation.

## Revisit when

PR #6 receives an explicitly bounded follow-up commit and updated tests, or the architect decides that Markdown composition should no longer be a required v0.1 mirror. Independently rerun the negative controls and repository-wide gates on the **new** head before recommending integration. Source drift or newly demonstrated legitimate table formats should prompt revision of the proposed strict grammar.

---
schema: 1
id: 2026-11-05-studio-foundation-audit-f1
kind: lesson
scope: agent:flint
status: draft
evidence: observed
author: flint-review-session
created: 2026-11-05
updated: 2026-11-05
sources: "cosmicdance-4-2-0/KestrelGaming meta/team-contracts-v1@6ba81c0de15ea86f455f40f50ee6414f7e6f3216; tools/validate_team_contracts.py blob 6e29e92698264b3ef3b526ee04743a5a13718941; tests/test_team_contracts.py blob 83628e893e1f7add9b98589240990e74778d01c4; isolated Python execution on 2026-11-05."
---

# Flint — independent Studio foundation review

## Summary

**Provisional verdict:** The Studio/team/project/individual boundary and Architects composition are defensible; do not stabilize or multiply the current `KestrelTeamContract` schema before reducing duplicate sources of truth and repairing structural validation. A team is a composition policy, not an identity, a vote, or a permission authority. Retain composite-vs-federated provenance and independent member memory.

**Design preference (not a defect):** The long `TEAM.md` and `PROFILE.json` repeat missions, methods, member home branches, authority prohibitions, execution explanations, and evaluation criteria. Prefer a small machine-readable roster/mode manifest and one human-readable operating procedure. Keep immutable authority and memory restrictions in the shared team policy rather than repeating them in every profile.

## Evidence

Inspected Studio HEAD `6ba81c0de15ea86f455f40f50ee6414f7e6f3216` and Flint HEAD `17b7da99ac9a558c673fb5cdc8521bc8fd85c8d8`. Reconstructed `tools/validate_team_contracts.py` and `tests/test_team_contracts.py` verbatim in an isolated local directory; `git hash-object` matched the published blobs. Ran the 16 original synthetic unit tests: **16 passed**. The template file used by the tests was a reduced stand-in containing only the three keys the template-specific test asserts; the real Architect files and full repository validation were not executed in this environment. No GitHub Actions runs were returned for the Studio branch.

Independently constructed negative cases against the exact validator implementation:

1. **Accepted invalid branch locator:** replacing `agents/flint-v1` with `agents/flint-v11` everywhere in synthetic team prose returns no errors because the check is a substring search (`tools/validate_team_contracts.py`, around line 201).
2. **Accepted conflicting role mapping:** swapping Axiom and Flint lead/counterweight labels in TEAM prose while leaving the JSON unchanged returns no errors. The validator checks that agent branch names appear, not that member roles agree across files.
3. **Accepted unindexed team:** a valid synthetic team home with no `teams/INDEX.md` registration returns no errors. This undermines discoverability as teams multiply.
4. **Accepted duplicate JSON keys:** adding an incorrect duplicate `schema.name` before the correct value still returns no errors; default `json.loads` keeps the last key. Ambiguous input may be interpreted differently by other readers.
5. **Rejected harmless Markdown variation:** adding one space after the display-name label results in `identity/profile mismatch`; the validator requires exact Markdown string fragments.
6. **Accepted misleading prose:** a synthetic TEAM file claiming production-deploy and voting authority passes the structural validator when required headings are present. This demonstrates the limit of prose checks; it is not evidence that such authority is granted.

These are **isolated reproductions**, not reports that the real Architects files presently contain those defects. Original tests catch duplicate agents, missing fields, wrong roles in JSON, invalid schema versions, and nonempty permissions: that basic validation is useful.

## Recommendation

Before approving more teams, fix exact member-token and role correspondence checks; detect duplicate JSON keys; make catalog registration verifiable; stop treating cosmetic Markdown spacing as semantics. Then run a matched task against generic Kestrel, solo Axiom, and the Architects composite. Consider a versioned v0.2 after that evidence, with one canonical owner per field and migration of Architects plus test fixtures. Do not silently accept mixed schema versions.

## Revisit when

Recheck against a newer Studio head, actual checkout-level tests/CI, peer findings, or a completed matched behavioral trial. Reproduce every reported validator failure against the current implementation before promoting these findings into shared policy. This is Flint's independent review; it does not assert agreement by Axiom, Harbor, or the Studio architect.

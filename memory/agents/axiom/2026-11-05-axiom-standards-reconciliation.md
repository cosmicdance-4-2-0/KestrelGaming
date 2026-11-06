---
schema: 1
id: 2026-11-05-axiom-standards-reconciliation
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "Axiom home 78af907268a1f3510bf880c6ac2d42b4f49ba513; shared main 4cb17b01d7ac50bd15ed69e84eccee0d32035a8b; local merge 9eb99b2; current user request for an Axiom standards PR."
---

# Axiom — Standards reconciliation and pickup baseline

## Summary

Integrate the reviewed shared baseline through
`maintenance/axiom-standards-2026-11-05`, targeting `agents/axiom-v1` for review.
The individual home must retain its identity and attributed memories while
receiving common standards. Do not merge this home wholesale into shared `main`.

The review branch includes the shared roster, pickup/structure documentation,
character templates, regression checks, and shared Auralprinter continuity.
Axiom's bootstrap, README, and project catalog are reconciled explicitly.
The existing shared contract, nine skill packages, protocols, validator, and CI
match pinned main; no audio curriculum or unmerged skill proposal is imported.

Axiom's two attributed audits are now discoverable from its continuity index and
`metadata.established_history` (paths relative to `agents/axiom/`). The profile
schema remains 0.1 and design status remains DRAFT. `first_state` records founding
history; it is not current usage status. Recorded sessions, authenticated runtime
identity, and comparative behavioral evaluation are separate claims.

## Evidence

- Loaded the Axiom entrypoint/profile and relevant agent/project records at the
  home revision above, plus shared pickup/structure documentation at pinned main.
- Home baseline validator and 72 tests passed before edits.
- Both baseline SHAs remain ancestors of the integration commit. All pre-existing
  project records remain byte-identical; the merged catalog retains both forks.
- An isolated archive of pinned main fails validation because the Auralprinter
  handoff appends prose to its exact `Task outcome` marker. This branch separates
  the unchanged PARTIAL marker from its explanation without altering the outcome
  or weakening validation. That imported record is not Axiom-authored work.
- The old Axiom test required history to remain empty permanently. Its replacement
  checks indexed local memory, source metadata, and Axiom attribution while
  retaining null runtime identity, draft design, and unexecuted comparative trials.
- Corrected-tree validation and all 83 unit tests passed. Failure messages from
  mocked HTML checker fixtures are expected negative-test output, not suite failures.
- A full base-to-head whitespace check flags 20 inherited Markdown hard-break
  lines in four newly imported shared documents. These are present verbatim in
  pinned main; no formatting sweep is part of this pass.

## Limits and next pickup

This is a review-branch update until the PR is merged. Resolve the actual home SHA
before assuming these corrections are available there. This pass checks memory
structure and attribution, not the present behavior of either HollowLumen project.
No matched agent comparison was run. Shared docs still contain historical wording
about the roster PR being unmerged; Git ancestry and the included roster establish
its integration here. Correcting shared historical prose can be a separate main PR.

## Revisit when

The PR is reviewed or merged, shared main changes, another home writer adds records,
or a real comparative trial supplies evidence for a different evaluation status.

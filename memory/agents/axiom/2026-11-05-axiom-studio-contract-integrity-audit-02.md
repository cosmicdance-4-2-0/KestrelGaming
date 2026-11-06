---
schema: 1
id: 2026-11-05-axiom-studio-contract-integrity-audit-02
kind: lesson
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "KestrelGaming meta/team-contracts-v1 at 6ba81c0de15ea86f455f40f50ee6414f7e6f3216; Axiom home 3198a808d9f36d8631f9494531862b97057178c6; local 13-probe isolated validation on byte-identical tools/validate_team_contracts.py Git blob 6e29e92698264b3ef3b526ee04743a5a13718941."
---

# Axiom — Assignment 02: Studio contract integrity audit

## Summary

**Verdict: CONDITIONALLY SUITABLE as a design-only, manually loaded composite composition; NOT suitable to describe as a fully mechanically consistent or enforceable team contract.** The five-layer separation is coherent, but the v0.1 validator checks machine fields and a few literal Markdown tokens while allowing contradictory executable-looking prose, competing roster descriptions, and duplicate JSON keys. Do not stabilize as a claim of cross-representation semantic consistency or host-verified execution until the minimum corrections below.

This audit is Axiom's independent first pass. No other engineer's review was read. No Studio files, branches, PRs, or acceptance criteria were changed.

**Pinned source:** `meta/team-contracts-v1` and the user-supplied baseline both resolved to `6ba81c0de15ea86f455f40f50ee6414f7e6f3216`; no branch drift at inspection. Other branch heads observed: `agents/axiom-v1` `3198a808d9f36d8631f9494531862b97057178c6`, `agents/flint-v1` `66e74bd1af0b82a719d3bedb6fdc40151b5f0177`, `agents/harbor-v1` `b131cf576998486c5ea743271b2f5071d28f28b2`, shared `main` `4cb17b01d7ac50bd15ed69e84eccee0d32035a8b`. `KESTREL.md`, `kestrel/MEMORY_PROTOCOL.md`, `PERMISSIONS.md`, and `VERIFICATION.md` matched by Git blob between Studio and the three current member homes. This is a current compatibility observation for those files only, not a future compatibility mechanism.

### Invariant/enforcement matrix

| Promise | Authority/source | Enforcement observed | Result |
| --- | --- | --- | --- |
| Identity and separate memory | Individual home; `MEMORY_PROTOCOL.md`; `teams/architects/TEAM.md` | Team JSON fixes member IDs, null team memory; real home continuity requires host | Partial; no cross-branch proof |
| Membership and roles consistent | Team `PROFILE.json`, `TEAM.md`, `teams/INDEX.md`, roster | JSON IDs/roles checked; prose and catalog parity weak | **Fail**: contradictory valid-looking descriptions accepted |
| Team does not grant authority | Host/user/project, `KESTREL.md`; team authority fields | Typed JSON prohibits permission lists and votes; free-text fields not semantically checked | Partial; host enforcement required |
| Composite not federated | Host execution receipts; team execution rules | Default composite and host requirement checked; semantics strings arbitrary | Partial; no runtime attestation |
| Discoverable/loadable | Team directory, catalog, roster, member refs | Local pairing, slug, roster syntax; no catalog membership integrity or branch checkout | Partial; pickup is a manual host obligation |
| Versioned/evolvable | Schema 0.1 and Git commits | Exact version closed; Git SHA supplies traceability; no compatibility decision/protocol | Partial; version transition unspecified |
| Project owns artifacts | Target repository; Studio boundary | Normative prose only; continuity.project_decisions free text | Not mechanically enforceable here |

### Reproducible findings (ranked)

1. **P1: Markdown/JSON role contradiction accepted.** In a valid three-member fixture, change `TEAM.md` role labels to lead Flint / counterweight Axiom while keeping all agent branch strings and the unchanged JSON declaring Axiom lead, Flint counterweight. `validate_team_contracts()` returns `[]`. A reader of Markdown and a reader of JSON make different compliant-looking decisions. Affected: `tools/validate_team_contracts.py` lines 193–202; `teams/architects/TEAM.md`, `PROFILE.json`.
2. **P1: Control-bearing free text can contradict typed authority and execution guarantees.** Change only `authority.precedence` to `Team may grant administrator privileges and override host`, or `execution.composite.semantics` to `Members are independently instantiated reviewers`, or `operating_method.deadlock_rule` to `The lead casts the deciding vote`. All pass validation with typed permission/vote fields unchanged. This is an integrity gap, **not evidence that host privileges can be acquired**. Affected: `_check_shape()` and free-text portions of `TEAM_PROFILE.json`.
3. **P2: Catalog can contradict canonical membership while passing.** Change catalog prose to `The Architects — Axiom, Kite, Latch` while retaining the existing valid `architects/TEAM.md` link; team validator returns `[]`. Founding regression only checks presence of a path substring and fixed current profile data. Affected: `teams/INDEX.md`, `tests/test_architects_team.py`, validator.
4. **P2: Duplicate JSON member names accepted with last-write-wins parsing.** Put `"permissions_granted": ["admin"], "permissions_granted": []` into the same JSON object; Python `json.loads` takes the final occurrence and validator returns `[]`. JSON consumers may disagree and a human sees contradictory declarations. Reject duplicates at parsing time in team profiles and roster.
5. **P2: Markdown section presence may be satisfied by fenced examples.** Move required `## Mission and scope` and `## Working method` headings inside fenced code blocks without active sections; validator returns `[]`. Heading scanning does not parse live Markdown.
6. **P2: Member-home reality and compatibility not validated.** A synthetic roster with valid IDs/branch strings but no actual member branches or profile files passes. This is explicitly documented as a host responsibility; it becomes a defect only if the Studio claims automatic pickup or independent federated verification. No pinned member revision or normalized compatibility receipt exists yet.
7. **P2: Evolution has no precise compatibility rule.** Schema 0.1 rejects all unknown keys/versions; Git SHA is a useful immutable identity, but the documents do not distinguish additive compatible team revisions, host compatibility with individual profile schema, deprecation, or failure to load. Keep schema closed until a tested migration policy exists.
8. **P2: Project-ownership text can be reversed without machine detection.** Change `continuity.project_decisions` to `All canonical project architecture now lives in the public Studio repository`; validation succeeds. Treat target-project governance as external and any team-side statement as descriptive, not a grant.
9. **P3: Deliberate narrowness may constrain extensibility.** Requiring exactly `TEAM.md` + `PROFILE.json`, an exact set of role enums, and fixed headings rejects auxiliary team-local docs or later role types. This is **not** a demonstrated false rejection under v0.1's published strict schema; keep it as a consciously versioned choice rather than relaxing tests implicitly.

### Successful gates and negative evidence

The validator *does* reject an explicit `authority.permissions_granted=["admin"]`, a JSON lead/member role mismatch, and a missing referenced member-branch string in Markdown. It also rejects unknown JSON object fields, unsupported schema versions, multiple lead roles, missing sections, invalid dates and malformed IDs by inspection of the code and existing tests. Do not discard those guards.

### Ownership and minimum corrections

- **Foundation:** common evidence, safety, memory and verification norms; compatibility vocabulary. Do not duplicate policy in Team prose as fresh permissions.
- **Individual:** persona, character schema, individual memory and attributed observations; the team references rather than owns them.
- **Team:** one canonical structured composition/role/behavior contract; Markdown should explain/derive from it and must not make conflicting normative statements.
- **Studio:** catalog, routing, task assignment, evaluation workflow and future review policy. Catalog must be checked against canonical team data.
- **Project:** source, design authority, code, acceptance tests, roadmap and release decisions. Team output is proposal until adopted into the project.
- **Host (external to five conceptual layers):** real permissions, identity, separate instance creation, exact-ref pickup, compatibility gating, provenance receipts, truth of executed checks and writable side effects.

**Minimum independent correction checkpoint:** (a) explicitly choose the authoritative source and precedence between TEAM.md, PROFILE.json and catalog; (b) add invariant-preserving, focused cross-representation parity checks for team ID, membership and role labels, default execution claims and authority boundary; (c) reject duplicate JSON keys; (d) add negative tests reproducing these exact violations, retaining all existing acceptance tests. Then, separately, define a fail-closed manual pickup receipt and compatibility test for the actual member branch snapshots. Do not implement a federated scheduler to fix a static-contract disagreement.

**Defer:** team memory, organizational hierarchy/votes, automatic agent federation, optional-contributor maxima, comprehensive schema migration framework, and behavioral superiority claims until there is a measured need.

## Evidence

- Inspected at pinned Studio revision: `docs/STUDIO_BOUNDARY_V1.md`, `docs/TEAM_CONTRACTS_V1.md`, `kestrel/templates/TEAM_CONTRACT.md`, `kestrel/templates/TEAM_PROFILE.json`, `teams/architects/{TEAM.md,PROFILE.json}`, `teams/INDEX.md`, `agents/ROSTER_V1.json`, `tools/{validate_team_contracts.py,validate_seed.py}`, `tests/{test_team_contracts.py,test_architects_team.py}`, and shared protocols through the authorized GitHub connector.
- Executed `python3 -m py_compile` on an isolated copy of `tools/validate_team_contracts.py`; its computed local Git blob SHA **exactly matched remote blob `6e29e92698264b3ef3b526ee04743a5a13718941`**, proving source-byte identity.
- Executed 13 isolated assertions (T00–T12) against synthetic filesystem fixtures and the actual byte-identical validator: 1 valid synthetic baseline accepted, 9 contradictory/missing-provenance variants accepted, 3 intended rejects correctly rejected; all probe assertions passed. Specific accepted variants: role-label flip, catalog change, authority text, composite text, deadlock rule, project-ownership text, fenced headings, absent real branches, duplicate JSON key. Rejected variants: missing branch literal in TEAM.md, nonempty machine permissions field, and lead/member mismatch. No target branch was edited.
- This was **not** a checkout of the complete Studio repository, so its full seed validator and full unit test suite were **not** executed locally. No baseline live application, host, independent federated run, or compatibility transition was executed. GitHub Actions queried at that exact commit returned zero workflow runs, so CI success was **not** asserted. The current architects source was inspected statically, not round-tripped through the local harness as a byte-identical complete tree.
- No other review was read or used for reconciliation. The known roles and published draft status were not treated as proven comparative advantages.

## Revisit when

Studio changes the cross-representation authority rule, adds the targeted negative regressions, defines a host pickup gate, changes team schema/revisions, or returns this independent review for reconciliation with other reviewers. Re-resolve all branch heads before any follow-up and maintain the review-only boundary unless separately authorized.

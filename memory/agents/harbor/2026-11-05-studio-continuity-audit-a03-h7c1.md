---
schema: 1
id: 2026-11-05-studio-continuity-audit-a03-h7c1
kind: lesson
scope: agent:harbor
status: draft
evidence: inferred
author: harbor-chat-review-2026-11-05
created: 2026-11-05
updated: 2026-11-05
sources: "Architect Assignment 03, supplied 2026-11-05; KestrelGaming meta/team-contracts-v1@6ba81c0de15ea86f455f40f50ee6414f7e6f3216; read-only GitHub inspection; isolated local Git race and unpublished-file fixture, 2026-11-05."
---

# Harbor — Assignment 03: Studio continuity, recovery, and operational resilience audit

**Status:** Independent first-pass review, not yet accepted by the Studio architect.
**Mode:** Review only. No Studio branch edits, corrective commits, PR, or consultation with other reviewers.
**Review baseline:** `meta/team-contracts-v1@6ba81c0de15ea86f455f40f50ee6414f7e6f3216`.
**Branch drift at inspection:** None; Studio branch head matched supplied baseline.
**Agent home at inspection:** `agents/harbor-v1@f88671781dca1a5aa74494863bba2de7d2556d17` (before this report commit).
**Other member heads observed solely for provenance comparison:** Axiom `1f15a7d4adf82b70e81cf7ed64b58743d3ec72f7`; Flint `66e74bd1af0b82a719d3bedb6fdc40151b5f0177`.
**Project for this audit:** `cosmicdance-4-2-0/KestrelGaming`; the hypothetical downstream architecture project was not supplied and was not audited.

## Summary

**Verdict: CONDITIONALLY RECOVERABLE, not yet OPERATIVELY DEMONSTRATED.** Kestrel Studio v0.1 has a sensible separation of individual identity, team composition, shared methods, project authority, and memory ownership. It documents pickup receipts and resumable handoffs, and mechanically validates structural invariants. It does **not** yet provide an operational guarantee that a task's receipt, independent contributions, checkpoints, or final decisions were saved. Recoverability begins only at the last **confirmed remote, discoverable checkpoint**, not at the last sentence written in a ChatGPT session.

The **minimum correction is not a new memory tier or studio scheduler**: require one small, indexed, source-pinned assignment pickup/handoff receipt for substantial team work, using the existing project-scoped Kestrel handoff workflow. Verify remote synchronization, then revalidate differences on resume. Keep project decisions and implementation canonical in the target project's own repository; the Kestrel handoff stores references and accountable task history, not a competing architecture.

## Continuity invariants

1. **Identity and execution mode:** The team ID and exact team-contract SHA must be known. Record composite (one context) versus actually independently launched federated contexts. Do not promote stylistic role checks into independent-agent testimony.
2. **Source provenance:** Record the exact shared contract/skills SHA; each member home branch SHA actually read (or mark missing); target project owner/repo, ref and inspected SHA; and material compatibility differences. A branch locator is not a revision.
3. **Work provenance:** Preserve who reported an observation, whether a real separate session executed it, source revision, verification status, and material dissent. A label in a document is attribution, not authenticated host identity.
4. **Durable checkpoint truth:** Distinguish unsaved in-session output, local files/commits, committed remote agent memory, and remote project handoff or project decision. Do not mark a checkpoint complete before verifying its remote destination.
5. **Canonical ownership:** Only the authorized project owner accepts project architecture/release decisions. A team or individual memory entry cannot silently become the project's design source of truth.
6. **Recoverable next step:** A handoff preserves task objective/acceptance, task outcome (IN PROGRESS/PARTIAL/BLOCKED/COMPLETE), completed versus proposed operations, evidence/checks, missing inputs, blockers and the next authorized bounded step. Authorities must be rechecked on resume.
7. **No invented past:** Missing memory, missing profile, stale test, unavailable agent or aborted session creates an explicit gap. It cannot be repaired by plausible narrative.

## Lifecycle — what survives

| Stage | Explicitly preserve | Reconstructable from pinned, reachable source | Recheck on resume |
| --- | --- | --- | --- |
| 1. Human assignment | Objective, acceptance, authority, project locator, execution mode request | None if only in ephemeral session | Who currently authorizes scope and effects |
| 2. Team pickup | Team SHA, mode, member SHAs read, common/skills SHA, missing pieces | Contract contents, member profiles, indexed history | Compatibility and real accessibility |
| 3. In-session work | Only material decisions, validated observations and checkpoint refs worth preserving | Committed repository files and tests | Proposed actions versus executed actions |
| 4. Session interruption | Last remotely confirmed handoff/artifact/commit; partial status | Previously committed changes and prior handoffs | Whether unsaved output ever existed cannot be proved |
| 5. Member home advances | Prior pinned home SHA plus newly cited memory commit if relevant | Commit history when reachable | Whether new facts supersede old observations |
| 6. Another session resumes | Receipt, actual project state and all remaining risks | Relevant source/memory at pinned SHAs | Current heads, worktree, authority, checks and drift |
| 7. Project delivery | Project-owned artifact/PR/decision and owner acceptance; closure state | Accepted project history | Applied changes, integration and release status |

**Key boundary:** A project's durable, accepted decision belongs in its own repo or authorized project record. The Kestrel project-scoped handoff may point to it but should not issue a rival decision.

## Failure scenarios — consequence and evidence

| Rank | Failure and consequence | Classification | Existing response and uncovered gap |
| --- | --- | --- | --- |
| HIGH | Session terminates with report only in ChatGPT, before remote save. Unpublished reasoning/output is unavailable from Git history. | Isolated generic-Git reproduction; host behavior not tested | State protocol recommends handoffs but Studio does not require a confirmed receipt/checkpoint. Do not promise zero loss before publication. |
| HIGH | Next session claims real Axiom/Flint/Harbor independence from a composite role description, or repeats unverified testimony. | Documented prohibition; runtime enforcement unverified | Team and validator forbid specific structural false claims, but narrative and execution identity require truthful host-provided evidence. |
| HIGH | Pickup uses branch names and newer skill text while reporting older source revisions; test/architecture claims become unauditable. | Actual divergent branch snapshots observed; harmful result untested | Team docs require pinned refs, but no persistent mandatory per-assignment manifest. |
| MEDIUM | Agent memory updated in one commit, but project handoff/index omitted or saved separately; a rescuer sees partial continuity. | Plausible sequence, not demonstrated against Studio | Git commits atomically update a single ref, not unrelated branch refs or user actions; index + record should be one commit, project artifact linked explicitly. |
| MEDIUM | Two sessions write same branch based on stale head, and second update is rejected. | Isolated local Git race reproduced | Non-fast-forward protection rejects silent overwrite in normal push; fetch, inspect, reconcile, no force push. Studio has guidance but no orchestration. |
| MEDIUM | Handoff cites test passed at an earlier project SHA or credits an unverified observation as current. | Read-only source inspection, risk not reproduced | Memory/verification protocols explicitly demand revalidation; receipt should track evidence SHA and status. |
| MEDIUM | Required member home missing or invalid; team silently continues using an imagined specialist. | Documented fail-closed behavior; runtime unavailable untested | Agent Pickup forbids impersonation; downgrade to an authorized generic/composite mode only with disclosure or escalate if that role is required. |
| MEDIUM | Architectural/release decision attributed to Axiom/team instead of authorized owner. | Documented boundary; no real governance incident tested | Explicit project owner acceptance and durable decision link needed. |
| LOW | Previously accepted contract fails a later validator run. | Plausible due to changed checkout/validator/environment; not reproduced | Compare exact source/validator/runtime versions and diagnose; don't weaken tests or claim an old pass proves a new revision. |
| LOW | Loss of a pinned commit after destructive history rewrite or unavailable provider. | Speculative for this assignment | Existing no-force-push policy and Git history are proportionate; no case for backup infrastructure or new coordination service here. |

## Existing protections — classifications

- **Mechanically enforced (local structural validation):** `tools/validate_team_contracts.py` enforces paired team files, closed JSON schema v0.1, unique registered members and functional roles, empty permissions, no synthetic votes, null team identity/memory scope, draft/not-certified state, and explicit execution-mode structure. `tools/validate_seed.py` checks indexed memory metadata, link reachability, handoff outcomes, duplicate IDs, and schema structure. These checks do not establish real identity, existence of remote branches, truthful narrative, or successful runtime recovery.
- **Documented safeguards:** `docs/STUDIO_BOUNDARY_V1.md`, `docs/TEAM_CONTRACTS_V1.md`, and `teams/architects/TEAM.md` define routing, pickup, team roles, composite/federated truthfulness, project ownership, and the substantial-task pickup receipt. `kestrel/STATE_PROTOCOL.md` and `kestrel/MEMORY_PROTOCOL.md` define resume and memory rules.
- **Host-dependent obligations:** Resolve and actually load each home SHA; obtain real permissions; attest independent contexts when claimed; save remote artifacts; recheck current branch/project state; establish human acceptance and delivery.
- **Missing operational safeguard:** A mandatory *persisted assignment-specific* receipt with a verified remote checkpoint for substantial Studio team work; explicit recovery status when some input is missing. No assignment-instance file, runtime ledger or auto-save service currently exists.

## Observed revision compatibility

Source heads observed via GitHub read-only access:
- Studio `6ba81c0de15ea86f455f40f50ee6414f7e6f3216`.
- Axiom `1f15a7d4adf82b70e81cf7ed64b58743d3ec72f7`.
- Flint `66e74bd1af0b82a719d3bedb6fdc40151b5f0177`.
- Harbor `f88671781dca1a5aa74494863bba2de7d2556d17`.

At inspection, `KESTREL.md`, `kestrel/MEMORY_PROTOCOL.md`, `kestrel/STATE_PROTOCOL.md`, `kestrel/PERMISSIONS.md` and `kestrel/VERIFICATION.md` had identical blob SHA across all four checked snapshots. Branch-specific `AGENTS.md` differed. `docs/AGENT_PICKUP.md` existed on Studio/Axiom but not Flint/Harbor; `skills/INDEX.md` differed between Studio/Axiom and Flint/Harbor. These are observed snapshot differences, **not a demonstrated incompatible shared contract**.

## Minimum corrections — bounded proposal

1. **Use the existing project-scoped handoff** under `memory/projects/<owner>/<repo>/handoffs/` for substantial multi-session team tasks. No new writable team-memory namespace or global journal. A small optional `Team pickup` subsection in `kestrel/templates/HANDOFF.md` should include: assignment ID, task owner, mode, team SHA, all actually read member home SHAs, shared/skills SHA, target SHA, input gaps, output/checkpoint pointers, member attribution with executed-versus-simulated status, unresolved dissent, current outcome, and next action.
2. **One checkpoint, one truthful claim:** write the receipt and its nearest-scope index update in the same Git commit when practical, confirm the remote branch SHA, and link any project-owned artifact. If save fails, state LOCAL ONLY/UNSAVED and hand back the content in the current response. Do not pretend separate project and agent branches can be atomically committed together.
3. **Resume protocol in five questions:** What exact task/mode was authorized? Which SHAs were actually read? Which artifact/checkpoint was remotely confirmed? What changed since? Which claims require rerun or fresh human approval? If unavailable, visibly narrow scope or block only the affected claim/action.
4. **Decision handoff:** Identify the authorized accepting human or host, decision link, rejected alternatives and dissent. Never attribute project acceptance to a team character.
5. **Verification checkpoint:** Add one short manual restart exercise and, if template fields become required, narrowly targeted fixture checks for a missing member SHA and false federated attribution. No database, scheduler, role registry, distributed lock or new team memory layer without evidence of need.

Suggested human-readable receipt (illustrative only; NOT an actual executed team):
```text
Assignment: project-architecture-001; owner: <authorized task owner>
Team: architects@6ba81c0...; mode: federated only if independently launched
Members actually read: axiom@<SHA|MISSING>, flint@<SHA|MISSING>, harbor@<SHA|MISSING>
Shared/skills: <SHA>; target: <owner/repo>@<SHA>
Checkpoint: <durable URL>@<SHA> or UNSAVED
Evidence: <claim -> artifact, verifier, result, revision>
Contributors: <actual separate execution context or one composite session>
Status: PARTIAL; gaps: <exact missing items>; next: <bounded authorized action>
```

## Evidence

**Inspected at exact Studio SHA:** [Studio boundary](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/docs/STUDIO_BOUNDARY_V1.md), [team schema and loading rules](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/docs/TEAM_CONTRACTS_V1.md), [team prose template](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/kestrel/templates/TEAM_CONTRACT.md), [team JSON template](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/kestrel/templates/TEAM_PROFILE.json), [Architects charter](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/teams/architects/TEAM.md), [Architects profile](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/teams/architects/PROFILE.json), [team catalog](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/teams/INDEX.md), [validator](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/tools/validate_team_contracts.py), [validator tests](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/tests/test_team_contracts.py), [Architects regression tests](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/tests/test_architects_team.py), [agent pickup](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/docs/AGENT_PICKUP.md), common permissions/verification/state/memory protocols, [handoff template](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/kestrel/templates/HANDOFF.md), [seed validator](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/tools/validate_seed.py), [CI definition](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/.github/workflows/validate.yml), and [contributing](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/6ba81c0de15ea86f455f40f50ee6414f7e6f3216/CONTRIBUTING.md). GitHub trees and branch metadata were inspected for member home SHA/blob comparisons without reading peer review findings.

**Executed isolated local Git tests, 2026-11-05:** Created a temporary bare repository and two independent clones of `main`. Writer A's ordinary push succeeded. Writer B's stale push exited 1 with a non-fast-forward rejection. After fetch/rebase and push, a fresh clone contained both `memory/a.md` and `memory/b.md`. A third session created `report-unpublished.md` without committing; it was absent from the bare repository tree. These prove generic Git recovery boundaries under the stated conditions, **not** Kestrel Studio's host-level behavior.

**Read-only static validation inspection:** The validator's free-text fields are checked for presence/non-placeholder text, not truth. The schema imposes correct status/authority structure but cannot attest that independent instances existed or a report survived a session. There were no check-runs or workflow runs returned for the Studio review baseline via inspected GitHub endpoints; this is not proof that CI is broken.

**Not performed:** No complete local checkout of the Studio baseline (the execution container could not resolve `github.com`), no `validate_seed.py` or Python unittest suite run locally, no real Studio session crash/restart or independent-host trial, no actual multi-branch simultaneous commit failure, no other reviewers consulted, no changes to `meta/team-contracts-v1` or target projects.

**Next checkpoint for architect:** Approve the small receipt addition, produce one sample project-scoped team handoff for a disposable task, intentionally interrupt/restart using a fresh context, verify exact SHA/mode/evidence/next-step pickup, then decide whether template-specific validation is worth adding. Reject any proposal for a new persistence service until this trial demonstrates a concrete failure the existing Git and handoff protocols cannot handle.

## Revisit when

The architect accepts or rejects the receipt proposal; a real Studio team assignment can be resumed from a fresh context; common/agent branches diverge materially; the team schema or validation logic changes; or an observed incident contradicts the risk estimates. This is Harbor's attributable independent review, not a team vote, implemented correction, or accepted Studio policy.

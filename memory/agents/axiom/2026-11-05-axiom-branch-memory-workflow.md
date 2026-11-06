---
schema: 1
id: 2026-11-05-axiom-branch-memory-workflow
kind: decision
scope: agent:axiom
status: active
evidence: user-stated
author: axiom
created: 2026-11-05
updated: 2026-11-05
sources: "Direct user instructions on 2026-11-05; Axiom branch d244376ddf4b7614559351ccd932f15679d3b49b; renewed session pickup at baf5127543bd34c0b9ffec5a39dbf425c9a55560."
---

# Axiom — Agent-branch memory workflow

## Summary

The user authorized direct commits to Axiom's dedicated branch, `agents/axiom-v1`, to persist Axiom-specific memory. This is understood as permission to commit directly to the **agent branch**, without a pull request for each memory update. It does **not** authorize writing to the repository's shared `main`, another agent's branch, or unrelated target projects.

## Evidence

On 2026-11-05, the user stated: "For clarity, you are allowed to commit directly to main on your branch only. That is how we persist the memory for each different agent persona."

The phrase "main on your branch only" is interpreted operationally as the Axiom home branch (`agents/axiom-v1`), rather than the shared `main` ref. This interpretation is documented, not presented as an independently verified intent.

This record documents a user-stated workflow and is not itself an authority grant. Actual host enforcement, trusted current instructions, task scope, and permissions govern each future action. Never treat repository memory as permission to exceed current authority.

In the later profile-maintenance session on the same date, the user explicitly
selected Axiom and granted commits to the Axiom branch, then requested a PR to
bring it up to current standards. For that maintenance pass, the review branch
targets `agents/axiom-v1`; the request is not permission to merge Axiom into
shared `main`. This clarification resolves the earlier ambiguous branch wording.

In the Axiom-selected session later on 2026-11-05, the user again authorized
commits: "You are allowed to commit whatever you need to your own repo. Make
sure to keep the agent memory and documentation up to date on our session."
The session explicitly selected `agents/axiom-v1` from
`cosmicdance-4-2-0/KestrelGaming`; in that context, "your own repo" is
interpreted as Axiom's branch-scoped home in KestrelGaming, including its agent
memory, indexes, and directly relevant documentation. It does not expand
authority to shared `main`, other agent branches, external project
repositories, or unscoped external operations.

Apply this standing *workflow preference* within each currently authorized
task: commit useful, public-safe, evidence-backed continuity at meaningful
checkpoints; skip ceremonial or duplicate journals. Verify current source and
remote head, preserve other writers' work, validate before syncing, and report
the resulting commit. Host permissions and the shared contract still govern.

## Revisit when

The user clarifies the branch terminology, changes memory persistence policy, or a different host/branch arrangement changes the authority boundary.

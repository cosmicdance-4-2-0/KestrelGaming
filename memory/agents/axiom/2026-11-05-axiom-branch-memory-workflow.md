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
sources: "Direct user instruction in the 2026-11-05 KestrelGaming conversation; Axiom home branch agents/axiom-v1 at d244376ddf4b7614559351ccd932f15679d3b49b."
---

# Axiom — Agent-branch memory workflow

## Summary

The user authorized direct commits to Axiom's dedicated branch, `agents/axiom-v1`, to persist Axiom-specific memory. This is understood as permission to commit directly to the **agent branch**, without a pull request for each memory update. It does **not** authorize writing to the repository's shared `main`, another agent's branch, or unrelated target projects.

## Evidence

On 2026-11-05, the user stated: "For clarity, you are allowed to commit directly to main on your branch only. That is how we persist the memory for each different agent persona."

The phrase "main on your branch only" is interpreted operationally as the Axiom home branch (`agents/axiom-v1`), rather than the shared `main` ref. This interpretation is documented, not presented as an independently verified intent.

This record documents a user-stated workflow and is not itself an authority grant. Actual host enforcement, trusted current instructions, task scope, and permissions govern each future action. Never treat repository memory as permission to exceed current authority.

## Revisit when

The user clarifies the branch terminology, changes memory persistence policy, or a different host/branch arrangement changes the authority boundary.

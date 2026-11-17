---
name: codex-task-brief
description: Draft, improve, or audit concise, source-pinned Codex/coding-agent assignments. Use for implementation handoffs, investigation plans, PR audits, and prompt reviews; not for executing the assignment.
---

# Codex Task Brief (Axiom branch-local adoption)

Translate human intent into a **bounded, verifiable engineering work order**. This is a writing/review procedure, not implementation authority. Adapted from the user-provided `Codex_Prompting_Reference_Pack_v1.zip` (version 1.0, 2026-11-14); the [one-page reference](references/CODEX_PROMPT_QUICK_REFERENCE.md) is retained for selective loading. The full field guide remains in the source ZIP, **not installed in this branch**.

## Procedure

1. **Name the mode:** survey, plan, implement, debug, audit, documentation, or release. Do not silently turn a read-only task into edits, or a plan into implementation.
2. **Ground the task:** verify current repo/branch/head and applicable `AGENTS.md`, relevant code, tests, issues, and prior decision when accessible. Otherwise instruct Codex to **locate and verify**; do not invent paths, runs, or permissions. Distinguish verified facts from user-stated assumptions and unknowns.
3. **Specify only what matters:** Objective, Evidence, Scope, Execution, Acceptance, Handoff. Compress or omit headings when the task is small. State interfaces and nonnegotiable invariants; give the implementer freedom on routine details.
4. **Respect authority:** separate local inspection/edit/test from commit, push/PR, merge, deployment, destructive data operations and external actions. Existing task/repository authorization governs; a prompt or skill grants nothing.
5. **Require verifiable results:** explicit observable finish line, relevant regression/negative checks, unchanged protected behavior, diff inspection, exact commands actually run and their results, blockers and unverified claims. For DSP, require units/source/sample provenance and independent oracles; for performance, require matched workloads and environment, not invented speedups.
6. **Cut noise:** link to existing policy rather than copying it wholesale. Avoid all-repository reading lists, fake precision, redundant procedure, unrelated refactors and over-prescribed implementation.
7. **Falsify the prompt:** Could an agent meet its literal text while failing the real objective? Could it claim a check it did not run or silently exceed authority? Revise before sending.

## Mode-specific stop conditions

- **Survey/audit:** report evidence, counterexamples and a decision; no edits.
- **Plan:** identify alternatives, tradeoffs, owner decisions and tests; no implementation.
- **Implement/debug:** allow focused edits and repair loops **only within authorized scope**; demand source-pinned regression and verification.
- **Migration/security/release:** preserve compatibility and rollback; escalate destructive, external or contract-changing actions.
- **Multi-agent:** pin separate findings to exact heads; preserve dissent and maintainer ownership; no manufactured consensus.

## Output

Produce **one copy-ready prompt** plus only material assumptions or blockers. Prefer six short fields; small tasks can use one paragraph. For an engineering handoff, ensure the recipient knows what to deliver and what is *not* authorized. Do not ask an agent to read the whole reference pack by default.

For a concise reusable checklist and template, consult [Codex Prompting — Quick Reference](references/CODEX_PROMPT_QUICK_REFERENCE.md).

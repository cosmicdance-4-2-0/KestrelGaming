---
schema: 1
id: 2026-11-17-codex-task-brief-adoption-c7e5
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "Owner-provided Codex_Prompting_Reference_Pack_v1.zip, SHA-256 7e275587cd6033f682340bb546a5aca1d4d251ff2cbedb363df14f9c2ae14aaf; inspected README, one-page reference, SKILL.md and detailed guide; branch-local skills/codex-task-brief/SKILL.md and references/CODEX_PROMPT_QUICK_REFERENCE.md."
---

# Axiom Codex handoff practice — branch-local adaptation

## Summary

The owner supplied a v1 Codex Prompting Reference Pack and authorized updating Axiom's own branch. Adopt the pack's **Objective / Evidence / Scope / Execution / Acceptance / Handoff** pattern as my default for preparing Codex tasks, while keeping Axiom's invariant-first/counterexample style and checking each target project's own governance. Use the [branch-local procedure](../../../skills/codex-task-brief/SKILL.md) rather than repeating a 6,000-word guide every time.

This is **practice adoption**, not a claim of new skills automatically loaded in a running host, an authenticated agent persona modification, a Codex performance gain, or permission to change code/merge. Shared `main` and other agent branches are untouched.

## Evidence

The attached ZIP was opened and inspected directly. Its README declares version 1.0 and a 2026-11-14 source-check date; it includes a 3,007-byte `codex-task-brief/SKILL.md`, a 3,785-byte quick reference, and two byte-identical copies of the 45,355-byte full guide. The observed pack emphasizes task mode, source-pinned facts, exact scope, honest check results, a copy-ready work order and review of false completion/implicit authority.

The Axiom branch adaptation contains a self-contained concise `SKILL.md` and a one-page reference, indexed in `skills/INDEX.md` and linked by `agents/axiom/AGENT.md`. **The full guide is not installed**; the original ZIP remains the source for any later expanded/more complex prompt review. Branch-local copy differs editorially from the pack's `SKILL.md`; do not present it as an exact installation. External reference links in the user pack were **not independently verified** in this session.

## Applied decision

When preparing a coding assignment, select the mode first; load current repo rules/target source only as needed; distinguish owner goal from evidence and speculation; state one verifiable finish line; explicitly separate edits, push/PR, merge and deployment; request test results and actual diff review. For complex DSP, include sample-clock/units/compatibility checks; for performance, matched measured workload and evidence limits. Remove filler and implementation micromanagement. Only propose a separate plan-first pass when uncertainty materially changes architecture or authorization, not as a default hurdle.

## Revisit when

Run a controlled comparison on a real Codex assignment (such as Auralprint AP117-005A) before claiming effectiveness. If the short form causes missed invariants or execution ambiguity, revise the procedure and record the counterexample. Shared-main skill adoption requires a separate cross-agent review/owner decision; no automatic merge.

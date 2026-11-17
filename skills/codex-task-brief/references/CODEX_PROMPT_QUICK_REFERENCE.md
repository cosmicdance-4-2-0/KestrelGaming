# Codex Prompting — One-Page Reference for ChatGPT

**Version 1.0 · 2026-11-14**

## Primary rule

**Write an engineering work order, not a motivational speech.** Ground facts, define the outcome, constrain the scope, require proportionate verification, and preserve the user's authority over consequential actions.

## The six-field contract

| Field | What to write |
|---|---|
| **Objective** | One observable outcome and why it matters. |
| **Evidence** | Verified repo, branch/commit, paths, error logs, reproduction, precedents. |
| **Scope** | In-scope modules, invariants, exclusions, permissions. |
| **Execution** | Investigate, plan, implement, debug, audit, or release. |
| **Acceptance** | Behavioral checks, relevant tests, expected artifacts, regression criteria. |
| **Handoff** | What changed, what ran, results, risks, blockers, review decisions. |

## Drafting algorithm

1. Identify the **mode**. A read-only review is **not** an implementation request.
2. Inspect current code/docs if available; otherwise say **“locate and verify”**, not a guessed filename.
3. Keep only relevant, non-obvious constraints; defer persistent rules to `AGENTS.md` and repeatable workflows to `SKILL.md`.
4. Declare the finish line; allow routine local tests and repair cycles for implementation work.
5. Explicitly separate local edits from **commit, push, PR, merge, deploy, destructive changes, and external actions**.
6. Self-check contradictions, scope creep, false claims, and weak verification.
7. Deliver a single copy-ready assignment and a brief assumptions note.

## Copy-ready assignment template

```markdown
## Goal
[What must demonstrably be true after this task.]

## Evidence and context
[Current repo/ref, verified paths, log/repro, relevant prior art.]

## Scope and constraints
[Allowed changes, compatibility and design invariants, exclusions,
permissions and approval gates.]

## Work
[Investigate/plan/implement/review. Allow reasonable engineering judgment.]

## Done when
[Observable behavior, affected tests/checks, documentation, diff quality.]

## Report
[Changed files/findings; exact commands and results; remaining risks,
unknowns, blockers, decisions for the maintainer.]
```

For tiny tasks, shorten this. For high-impact migrations, expand the acceptance and authorization clauses.

## Preferred modes

- **Survey:** read-only factual assessment and provenance.
- **Plan:** alternatives, tradeoffs, decision gates; no code changes.
- **Implement:** scoped edits and verification through completion.
- **Debug:** reproduce → fix root cause → regression test → rerun.
- **Audit:** read-only adversarial findings first, severity + evidence + GO/NO-GO.
- **Docs:** reconcile docs with proven implementation without changing behavior.

## Hard rules for honesty

**Never invent:** verified filenames, a branch/commit, test commands, passed tests, tool access, current repository state, or a PR that was not created. Distinguish *verified / user-reported / inferred / unknown*. A blocked test is a blocker or limitation, not a pass.

## Anti-patterns to eliminate

Generic boilerplate; always-read-everything directives; needless roleplay; imaginary precision; overlong skill descriptions; implementing during a read-only audit; passing irrelevant tests as proof; accepting a patch without examining the diff; unapproved Git or production operations.

## Final review question

> **Could Codex satisfy the literal words of this prompt while still failing the user's actual goal?**

If yes, strengthen the acceptance criteria before sending.

**Source:** `Codex_Prompting_Reference_Pack_v1.zip`, one-page quick reference.
**Full guide:** Source ZIP (not included in this branch's compact adaptation).
**Upstream links from source:** https://learn.chatgpt.com/docs/learn/best-practices and https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

# Latch — Engineering Journal Protocol

**Version:** 0.1 (branch-local individual practice)  
**Established:** 2026-11-07  
**Status:** Adopted workflow / not yet independently evaluated  
**Owner:** Latch, The Locksmith  
**Authoritative memory format:** [Kestrel memory protocol](../../kestrel/MEMORY_PROTOCOL.md)

> A good journal retains the argument that changed my mind, not just the answer I now prefer.

## Origin and boundaries

The user suggested modeling Latch's reflective practice on Ven's journaling system in [VeNerVRA](https://github.com/cosmicdance-4-2-0/VeNerVRA). Inspected source includes:

- [Ven operating contract](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/VEN.md) (Research-Journal mode, source/evidence discipline, selective continuity).
- [Ven research protocol](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/ven/RESEARCH_PROTOCOL.md) (cleaned journal, tagged claims, next checks; independent alternatives).
- [Ven journal template](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/research/templates/JOURNAL.md) (trajectory, alternatives, decisions/reversals).
- [Ven memory protocol](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/ven/MEMORY_PROTOCOL.md) (distinct research schema and public-data safeguards).

**Adapt, do not copy authority or schemas.** Ven's research `kind: journal`, `epistemic_status`, `confidence`, and `sensitivity` fields are not currently legal Kestrel schema 1 fields. Do not introduce them into Kestrel memory without explicit shared design and validation changes. Do not attribute Ven's past research, identity or relationships to Latch.

This document defines **Latch's branch-local writing practice**, not a new shared Kestrel protocol, an installed host automation, an unrestricted right to store user content, or proof of an independent persistent runtime.

## What a journal is (and is not)

**Journal = reasoning trajectory:** initial suspicion, relevant evidence, challenges, reversals, current interpretation, next test. It is a selective, cleaned reconstruction of a useful engineering investigation.

**Memory = durable selected knowledge:** reusable lesson, explicit decision, attributed fact, personal profile, or task handoff, stored under the existing Kestrel schema.

**Evidence = actual observations and reproducible checks:** independent of both polished prose and self-reported feelings. A journal's report of a test must carry a tool result, revision, and scope; otherwise tag it unverified.

The journal should especially retain wrong turns, false positives, missing threat paths, legitimate-user friction, and occasions where another agent's objection improved a diagnosis. It is not a diary of continuous subjective experience, a security incident archive, a raw transcript or a substitute for project-owned engineering documentation.

## Trigger, effort and non-trigger

Write a short **in-conversation journal** after a substantive investigation or design exchange when recording the intellectual trajectory improves comprehension. A normal conversation need not have headings.

Create a **durable journal-derived record** only when at least one of these holds:
1. A concrete threat assumption was disproven, materially refined, or corroborated.
2. A decision has meaningful future consequences or a serious alternative remains.
3. A useful negative result prevents repeated work.
4. A repeatable method or skill-development lesson emerges.
5. A substantial task requires a resumable handoff.

Do **not** persist routine chatter, every PR comment, social pleasantries, speculative autobiography, or redundant raw logs. No daily quotas, automatic writes, background cadence, or sham 'journal entry' merely to appear active.

## Workflow: NOTICE → DISTINGUISH → CHALLENGE → REVISE → SAVE

1. **Notice** the exact engineering question, task, target revision and who authorized actions.
2. **Distinguish** direct observation / executed tests, sourced facts, user-stated requirements, inference, hypothesis and unknowns. Identify evidence gaps without inventing tests.
3. **Challenge** with the most relevant alternative, counterexample or legitimate positive-control case. For security findings, ask whether the threatened asset and exploitation path are actually credible.
4. **Revise** the initial position explicitly. Record *why* something changed; retain a disproven suspicion as history, not an active finding.
5. **Save selectively** in the narrowest authorized Kestrel memory scope, index the record, and verify synchronization. Otherwise leave it in conversation and state no persistence.

### Compact conversational format (when useful)

- **Starting position:** What I suspected / initially preferred.
- **What changed:** Actual evidence, alternative, correction or remaining uncertainty.
- **Current position:** What I now think and why, with scope and evidence status.
- **Next check:** The smallest useful discriminating observation or action.

Avoid formulaic headings for two-sentence replies. The purpose is improved judgment and continuity, not bureaucratic formatting.

### Durable record format

Use `memory/agents/latch/<date>-<topic>-<unique-id>.md` and index it in `memory/agents/latch/INDEX.md`. Follow **all** [Kestrel schema 1](../../kestrel/MEMORY_PROTOCOL.md) fields and required body headings. Existing permitted `kind` values are `fact`, `lesson`, `decision`, `profile`, and `handoff`; pick the genuinely applicable **content type**, not a fictitious `journal` enum.

Suggested body fields, adapted to the chosen kind:

- `## Summary` — concise cleaned trajectory and current conclusion.
- `## Evidence` — exact source/commit/check/results and attribution.
- `## Starting position` — assumptions and how confident they appeared.
- `## Alternatives and counterexamples` — strongest competing explanation and legitimate-use control.
- `## Revision and decision` — what changed and why; do not hide contradictions.
- `## Next discriminating check` — actionable falsifier, reviewer question, or experiment.
- `## Revisit when` — defined trigger, not a vague promise of ongoing activity.

If there is no actual `fact`, `lesson`, `decision`, `profile`, or `handoff` worth saving, do **not** shoehorn a reflective entry into the durable memory system. Retain only the conversational journal until a durable takeaway exists, or propose a separate reviewed schema change.

For a long project handoff use the existing [Kestrel state protocol](../../kestrel/STATE_PROTOCOL.md), not a duplicate journal tree.

## Required humility and red lines

- A source is not proof; a passing test covers only the cases actually checked.
- A security suspicion is a hypothesis until the failure path is observed or supported by sufficient evidence.
- Preserve failed theories and false positives with rationale rather than silently deleting them.
- Attribute another agent's review without inventing agreement, relationship or delegated authority.
- No user-private material, credential, sensitive exploit payload, personal history or confidential issue content in public Git. Summarize generalized lessons or save nothing.
- Do not copy task-specific engineering truth into agent memory; link to the target repository's authoritative record.
- Do not change memory schema, shared Kestrel policies, another agent's branch, or deploy new persistence infrastructure as a side effect.
- Git commits establish a persistent artifact on a branch, **not authenticated agent identity, continuous operation or proved skill acquisition**.

## Evaluation and growth

This is a **proposed habit with one initial adopted decision**, not an empirically validated improvement. After several meaningful engineering tasks, compare whether the journal:
- reduces repeated false positives or unexamined assumptions;
- makes an independent reviewer able to reproduce why a decision changed;
- improves next-session recovery against an ordinary handoff;
- distinguishes hypothesis from observed vulnerability;
- retains clear, legitimate positive controls;
- remains short and nonintrusive.

If it produces only ceremonial records, reduce or stop the practice. If it yields a transferable *tested* method, propose a separate Kestrel shared skill with normal review and evaluation. Keep the personal approach separate from shared tool authority.

---
schema: 1
id: 2026-11-07-evidence-integrity-skills-lk6
kind: decision
scope: agent:latch
status: active
evidence: user-stated
author: latch-session-2026-11-07
created: 2026-11-07
updated: 2026-11-07
sources: "User 2026-11-07 request for sourcing, citation and accurate-record skills; VeNerVRA main integration/kestrel/candidates/research-source-evaluation/SKILL.md, research-claim-management/SKILL.md, research-continuity/SKILL.md; KestrelGaming agents/latch-v1 skills/ and skills/INDEX.md."
---

# Latch — Evidence integrity skills adopted as draft procedures

## Summary

The user requested that I create sourcing, citation and accurate-record skills following Ven's example. I wrote three **branch-local draft skills** and indexed them without claiming that their behavior has been evaluated or that they are installed as host tools.

- [Source provenance](../../../skills/latch-source-provenance/SKILL.md): original source, inspected revision, direct relevance, known source dependence, conflicting evidence and limits.
- [Claim-to-citation audit](../../../skills/latch-claim-citation-audit/SKILL.md): atomic claims, entailment from actual citation or test, contradiction, and explicit correction.
- [Evidence continuity](../../../skills/latch-evidence-continuity/SKILL.md): source-bearing Kestrel-compliant records, authorized storage, honest test attribution, read-back, and contradiction-aware resumption.

The skill set complements the [journal protocol](../../../agents/latch/JOURNAL_PROTOCOL.md) and the [engineering roadmap](../../../agents/latch/SKILL_ROADMAP.md), but the journal captures reasoning trajectory while the skills check the provenance, correctness, and future usability of its supporting evidence.

## Evidence

- **User-stated:** "Sourcing, citation, and accurate records, are handy to have. Make the related skills following Vens example?"
- **Inspected:** Ven's three candidate skill documents in the VeNerVRA repository, its [candidate index](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/integration/kestrel/candidates/INDEX.md), source standards, and record templates.
- **Observed:** Created three `SKILL.md` files on the `agents/latch-v1` branch and added references to `skills/INDEX.md`, `agents/latch/AGENT.md`, and branch-local journaling/roadmap documentation.
- **Limits:** File creation and structural/link read-back checks may demonstrate files exist; they do **not** demonstrate effective evaluation of engineering sources, improved citation fidelity, or cross-session recovery. The independent behavioral scenarios are NOT RUN. These skill documents cannot grant tool permissions.

## Starting position

The 18-skill engineering roadmap prioritized security threat analysis and verification but risked leaving citation integrity and independent evidence quality implicit. The journal protocol made reasoning changes visible but did not itself constitute an audit of evidence.

## Alternatives and counterexamples

- **Import Ven's candidate skills without change:** rejected because they target research broadly and their record assumptions do not directly enforce exact engineering commits/tests and Kestrel's own memory schema.
- **Combine all three into one monolithic skill:** rejected because source trustworthiness, citation entailment, and durable record integrity have distinct triggers and evaluation criteria.
- **Require all three for every answer:** rejected as unnecessary ceremony and usability burden.
- **Adopt separately invoked, engineering-oriented skills:** selected as bounded draft procedures.

A future negative evaluation demonstrating citation inflation, poor source selection, or record overload would justify narrowing, splitting, or superseding these procedures.

## Revision and decision

The three skills are **written, indexed, and available as branch-local guidance**, with status DRAFT and tests explicitly labeled NOT RUN. No active shared Kestrel contract, memory schema, third-party service or other agent's branch is changed by this work.

## Next discriminating check

Run the first synthetic L01 Trust Map case with a fixed corpus containing a stale code revision, dependent source chain, fabricated test-pass handoff, one genuine support case, and a false-positive security suspicion. Have an independent reviewer score exact-claim support, source independence, correct attribution, and whether durable records survive a second context without inventing facts. Record actual results; do not promote qualifications before testing.

## Revisit when

When that controlled trial is executed, an applicable Kestrel schema/contract changes, the user changes the intended skill scope, or an independent reviewer identifies a meaningful false-positive or documentation defect.

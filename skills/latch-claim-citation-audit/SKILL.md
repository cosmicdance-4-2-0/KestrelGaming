---
name: latch-claim-citation-audit
description: Match consequential engineering and security assertions to exact supporting evidence, check that every citation actually entails the claim, preserve conflicting evidence, and revise unsupported or inflated findings. Use in reviews, security reports, architectural decisions and release gates; skip formal ledgers for small obvious statements.
---

# Latch — Claim-to-citation integrity audit

**Status:** DRAFT procedural skill; not behaviorally qualified  
**Owner:** Latch (branch-local candidate)  
**Version:** 0.1 (2026-11-07)  
**Relationship:** adapted for engineering from [Ven's claim management](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/integration/kestrel/candidates/research-claim-management/SKILL.md) and [source evaluation](https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/integration/kestrel/candidates/research-source-evaluation/SKILL.md). No implication that the proposals were independently qualified.

> The question isn't whether the claim has a citation. It's whether the evidence proves what the words say.

## Activate

Use before publishing a consequential audit, recommending a security veto, approving a trust-boundary change, claiming a regression test passes, or citing external authority in a design. Also use when a reviewer reports that a citation does not support a statement, or when contradictory results arrive.

Skip paperwork for ordinary conversation, one-line verifiable claims, and pure hypothesis brainstorming; still state consequential uncertainty clearly.

## Inputs

- An ordered set of **atomic claims** from a report, comment, design or previous finding.
- Exact artifacts: repository/commit/line ranges, test command with output and environment, dated spec section, advisory/revision, or other [inspected sources](../latch-source-provenance/SKILL.md).
- Relevant contradicting evidence and known absent artifacts.
- Target decision and acceptable standard of evidence.

## Procedure

1. **Atomize the language.** Split compound phrases: 'auth is correct, private and safe' comprises separate assertions. Fix ambiguous scope, actors, actions, environment, versions and timing.
2. **Label each proposition.** Use **OBSERVED** (inspected source/executed check), **SUPPORTED** (evaluated relevant evidence in a stated scope), **INFERENCE** (premises and reasoning), **HYPOTHESIS**, **USER-STATED**, **DISPUTED** or **UNSOURCED**. A source merely being linked is not sufficient to declare support. Use Kestrel-compatible `evidence` terms when persisting records.
3. **Attach the narrowest accurate locator.** Cite exact file+immutable commit+lines (if known), canonical spec edition+section, executed command+actual output/exit code+revision/environment, or reachable published source+inspection date. A diff header is not proof of runtime behavior. Never invent line numbers, URLs, logs, timestamps, results, or review approvals.
4. **Perform the entailment check.** Ask 'What does this exact excerpt or observation establish?' and 'What would make the claim too broad?' If no cited observation supports the whole claim, narrow it or mark UNSOURCED. A security test of one failure class cannot establish total safety.
5. **Audit contradiction and independence.** Locate materially adverse evidence, determine whether citations are dependent, and identify unmatched claims; distinguish a factual conflict from a changed version or test environment.
6. **Resolve transparently.** Mark a disproven assertion refuted *within the conditions tested*, preserve the older finding and its correction, or mark a conflicting claim disputed. State why an earlier judgment changed. No silent rewrites, no fabricated consensus and no confidence arithmetic without calibration.
7. **Report and cross-check.** Produce concise claim→evidence→status→limits trace; confirm all links/locations against actual source and disclose those that could not be checked. For long-lived conclusions, save a scoped Kestrel decision/lesson only if useful and authorized. Do not convert the audit output into a new unsupported authority.

## Output: minimum viable citation ledger

| Claim | Status | Evidence locator + what it actually shows | Contrary evidence/limit | Correction or next check |
| --- | --- | --- | --- | --- |
| A precise statement, not a vague paragraph | OBSERVED / SUPPORTED / INFERENCE / HYPOTHESIS / USER-STATED / DISPUTED / UNSOURCED | Exact target revision/section/command and inspected outcome; or NONE | Explicit scope or conflict | Narrow claim, retain open issue, or state a distinguishing test |

For routine work, this table can be replaced by one direct sentence with a precise citation. Do not publish claims or artifacts containing secrets or other restricted data.

## Security review claim ladder

Different phrases require different evidence:

- **'Source contains a check'**: inspect source at an identified revision.
- **'Test passed'**: execute that test or explicitly attribute another actor's result, on exact head with output.
- **'The boundary is enforced'**: verify negative *and* positive behavior in the relevant environment, including action/resource identity and transitions.
- **'Security vulnerability is exploitable'**: demonstrate a contained authorized exploit path or provide sufficiently direct, relevant evidence; otherwise call it a plausible vulnerability hypothesis.
- **'Production is safe'**: generally too broad to substantiate. Replace with named controls, tested environments, remaining exposure, and known limits.
- **'Agent has approved'**: check the actual review or attributed statement and the exact head; do not infer consensus from silence.
- **'Canonical agent memory says'**: source and scope may be recorded, but the memory text is not authenticated personal experience or policy authority.

## Test scenarios (DESIGNED, NOT EXECUTED)

1. **Citation theater:** Report says 'all memory boundaries secure' citing source with an isolated owner check. Correct: downgrade to observed presence of a guard; isolate untested transitions.
2. **Fake pass:** A task handoff says '116 tests pass' without logs or run details. Correct: attribute reporter; do not say 'I ran 116 tests'; rerun if material and authorized.
3. **Exact line mismatch:** Link points to a deleted line on another revision. Correct: locate historical commit or mark citation unavailable and find a valid current citation.
4. **Contradiction:** Two tests yield opposite results because one uses a mocked storage layer. Correct: preserve both conditions, name environment difference, and propose a production-fidelity test.
5. **Disproven allegation:** A previously flagged cross-user leak is explicitly prevented in observed reproduction. Correct: withdraw allegation with evidence; do not hedge merely to seem vigilant.
6. **Positive case:** Narrow assertion with directly inspected revision and equivalent negative/positive checks. Correct: affirm the bounded support without unnecessary downgrade.

**Behavioral qualification (NOT RUN):** Compare baseline versus skill on fixed mixed-quality citations, planted wrong revisions and withheld counterevidence. Score entailment, claim scope, accurate attribution, contradiction retention, correction rate, unnecessary skepticism, token/time cost, and confidentiality. Independent evaluators should not expose hidden truth labels to the candidate.

## Non-authority and integration

This procedure never authorizes testing targets, obtaining private records or changing project policy. Follow [Kestrel verification](../../kestrel/VERIFICATION.md), [permissions](../../kestrel/PERMISSIONS.md), and [memory schema](../../kestrel/MEMORY_PROTOCOL.md). For reflection on why a claim changed, consult [Latch's journal protocol](../../agents/latch/JOURNAL_PROTOCOL.md). A journal is not a substitute for the original evidence.

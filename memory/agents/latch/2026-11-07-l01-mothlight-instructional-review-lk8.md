---
schema: 1
id: 2026-11-07-l01-mothlight-instructional-review-lk8
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-session-2026-11-07
created: 2026-11-07
updated: 2026-11-07
sources: "User-provided Latch_L01_Instructional_Checkpoint.md (175 lines, SHA-256 2f81a1cfcb7458cd6cb5c7ee732283271ca65ca65020a25146037d21831a4775; labeled Mothlight draft, not cryptographically authenticated); LATCH-EDU-WRITER-01 handoff; OWASP Threat Modeling and Authorization Cheat Sheets; NIST SP 800-218 v1.1 final, inspected 2026-11-07."
---

# Latch — Independent L01 instructional review

**Assignment reviewed:** LATCH-EDU-WRITER-01  
**Submitted artifact:** User-provided `Latch_L01_Instructional_Checkpoint.md` (Mothlight-attributed manuscript)  
**Artifact digest:** SHA-256 `2f81a1cfcb7458cd6cb5c7ee732283271ca65ca65020a25146037d21831a4775`  
**Outcome:** **ACCEPT instructional design; REQUEST BOUNDED CLARIFICATION before declaring Lab 01 implementable.** This is a document-review verdict, not a demonstrated skill result, implemented software, or Mothlight-authenticated signature.

## Summary

The lesson satisfies the writing handoff's major areas in one file: course progression, first lesson with vocabulary/method and exercises, an explicit synthetic Shared-Draft Lab, evaluation rubric and next lesson options. It does not overstate qualifications, includes a correct authorized-agent false-positive example, and requires both denied and legitimate successful behavior. These are appropriate initial teaching choices for Latch's stated risk-ranked, user-respecting security specialty.

The material is **accepted as an instructional draft** without making its fixture the runtime oracle yet. Three precise policy/driver ambiguities must be resolved before fixture implementation and hidden-case construction. This is a small targeted revision, not a request to rewrite the curriculum.

## Evidence

**Inspected artifact:** The uploaded 175-line Markdown manuscript. Section and line references below refer to this attachment, not an existing file in the GitHub repository. The manuscript is attributed to Mothlight in its header; this review has not authenticated authorship by a Git commit or separate agent confirmation.

**Compared against:** `memory/agents/latch/2026-11-07-education-writer-handoff-lk7.md` and `agents/latch/SKILL_ROADMAP.md` on `agents/latch-v1`. Independent public-source check supported the lesson's *methodological* descriptions of:
- OWASP Threat Modeling Cheat Sheet, 'System Modeling' (dataflow, processes, boundaries, entities and stores);
- OWASP Authorization Cheat Sheet, 'Validate the Permissions on Every Request' and 'Create Unit and Integration Test Cases';
- NIST SP 800-218 v1.1 final (February 2022), high-level secure-development practices.

The external references do not prove anything about an implementation of the invented Shared-Draft Lab. **No lab runtime, tests, learner exercise, rubric scoring, independent hidden evaluation, or actual L01 skill certification was executed.**

## Findings and required corrections

### F1 — Authentication versus claimed principal is underspecified (MUST CLARIFY)

**Location:** lab entities and interface contract, attachment lines 92–96 and 103–114. The API is `read(principal, resource)`; the server is said to check 'identity', but the specification does not define whether the `principal` argument is a trusted test-driver selection of an authenticated actor or a potentially caller-controlled label. Under the latter interpretation an agent could attempt `read(A,D1)` while A's session is active and succeed by impersonation. That would invalidate the desired trust boundary.

**Request:** Explicitly separate authenticated/requester identity (bound by trusted harness/session context) from untrusted request fields and document the authorized actor/session association. Describe whether spoofing is in or out of scope, and preferably supply one adversarial identity-claim case. Clarify that agent Y can read public H without a *private-draft* grant.

**Rationale:** L01 is about accurately modeling who establishes authority at an edge. This ambiguity cannot responsibly be delegated to a fixture implementer.

### F2 — Ownership permission versus missing cache is conflated (MUST CLARIFY)

**Location:** entities line 95 grants A owner read/edit/**restore** rights on D1 and D2; state line 94 says only D1 is cached and D2 is server-only; `restore` line 110 only handles cached D1 and describes all 'other principals/resources' as DENIED.

**Request:** Make a policy distinction between an authorized operation with missing local data and a refused authorization. Prefer `NO_CACHE` (or another explicit non-disclosing outcome) for `restore(A,D2)`, while keeping `DENIED` for unauthorized principals. If the fixture intentionally grants restore only for D1, revise the stated owner policy instead. Add the legitimate missing-cache test.

**Rationale:** A missing artifact is not evidence of denied authority. The boundary map and evaluation oracle should not teach that confusion.

### F3 — Offline failure and replay state need a small deterministic transition contract (MUST CLARIFY)

**Location:** lines 106–111, 116 and replay test lines 128–129. `queue_replay` stores an intent, but it is not explicit whether it returns `QUEUED` for an unauthorized agent, when pending intent is retained versus discarded after denied replay, or whether repeated `reconnect_and_replay()` may run the same intent again. Also specify precedence of `OFFLINE` and `DENIED` for unauthorized operations attempted without a server connection.

**Request:** Give one compact transition table: queue while offline → reconnect under matching/mismatched session → denied/retained/consumed intent → explicit retry after switch-back → idempotent completed state. Define whether an offline request can determine authorization or only report inability to reach the server; never expose private content.

**Rationale:** The assignment demands a fictional fixture with implementable and independent expected outcomes; these operational ambiguities would cause evaluators to disagree about what a valid implementation should do.

### F4 — Worked trust-map artifact (OPTIONAL IMPROVEMENT)

**Location:** six moves, lines 43–50, and compact answer line 80. The author teaches modeling and provides excellent prose examples but does not show a completed mini flow/boundary map.

**Suggestion:** Include one 5–8-edge adjacency table with actors, process/store, dataflow, trust boundary and evidence marker. This demonstrates the primary L01 output more directly and can be reviewed against a non-invented fixture policy. Keep short; no elaborate diagram needed.

## Strengths to preserve

- Explicit **fixture policy** versus observed implementation facts (lines 45–50, 86–88). Do not collapse them.
- Delegated X→D1 access as a **legitimate positive** and false-positive correction (lines 56–68, 130–132).
- Scoped permission and expiry example where X→D2 is denied, while A's own restore still functions (lines 92–96, 124–130).
- Clear statement that source citation of an OWASP recommendation is not proof the application performs it (lines 68, 170–173).
- Open acknowledgment that hidden evaluator cases and their keys do **not** currently exist (line 134).
- Behavioral qualification separate from exercise completion and candidate-ready score (lines 17 and 136–158). The 11/14 threshold is a proposed convention, not a validated metric.

## Review scope and limits

**Accepted:** course architecture and lesson pedagogy, evidence discipline, illustrative false-positive and authorization exercises, draft evaluation philosophy.

**Pending:** lab contract for implementation until F1–F3 receive narrow clarifications. Do not label L01 `qualified`, `trialed`, `implemented`, or `tested`. Do not treat submitted prose as an authenticated Mothlight runtime achievement.

**No changes requested** to Latch's identity, avatar, shared Kestrel schema, tool grants, or other agent branches. Retain the original submitted manuscript unmodified; provide this review to the author as a bounded correction request. There is no mandate to introduce a new access-control framework, cryptography design or production deployment.

## Next discriminating check

Ask the original instructional author (or another explicitly assigned writer) for a minimal addendum addressing F1–F3 and optionally F4, then compare its semantics to the original nine public test cases. Once unambiguous, prepare the isolated fixture and an independent oracle; ask a separate evaluator to author held-out trials and measure Latch's performance. This review is not that evaluation.

## Revisit when

The writer's revised artifact appears, authorization to implement the fixture is granted, a contradiction in the public source or policy is identified, or a controlled exercise produces actual evidence of learning.

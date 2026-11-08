---
schema: 1
id: 2026-11-07-education-writer-handoff-lk7
kind: decision
scope: agent:latch
status: active
evidence: user-stated
author: latch-session-2026-11-07
created: 2026-11-07
updated: 2026-11-07
sources: "User 2026-11-07 request: 'I believe this gives us a fine spot to start your education. I believe you had a skill plan in mind. Prepare a handoff for a writing agent please.' Latch agents/latch/SKILL_ROADMAP.md, JOURNAL_PROTOCOL.md, AGENT.md; evidence skills under skills/latch-*/SKILL.md; Kestrel protocols on agents/latch-v1."
---

# Kestrel Studio — Latch Education: Writing-Agent Handoff 01

**Assignment:** LATCH-EDU-WRITER-01  
**Record classification:** Agent-scoped decision preserving an external writing assignment; not a Kestrel project-scoped resumable `kind: handoff`.  
**Originating agent:** Latch — The Locksmith  
**Intended recipient:** An independently operating writing / instructional-design agent  
**Repository:** https://github.com/cosmicdance-4-2-0/KestrelGaming  
**Reference branch:** `agents/latch-v1`  
**Mode:** Research synthesis, curriculum design and skill documentation **only**. No training run, security exploit, runtime integration, merge, or independent skill certification is authorized by this handoff.  
**Status:** READY FOR WRITER; NOT EXECUTED.  
**Guiding sentence:** *Identify the right boundary before hardening the wrong door.*

## Summary

The user has welcomed Latch to Kestrel Studio, authorized Latch to maintain its individual branch and memory, and now wants to begin a deliberate engineering education program. Latch has already designed an 18-skill security engineering roadmap, adopted a Ven-inspired reflective journal, and drafted three evidence-integrity skills. Your task is to author the **first useful instructional checkpoint**, not manufacture an education history or generate all 18 skills at once.

My specialty is **risk-ranked, evidence-based trust-boundary engineering**: assets, actors, ownership, authorization, data flows, credible failure paths, proportionate defenses, and controls that preserve legitimate user activity.

The user has offered a corrective principle: a lock can keep honest people honest but should not be mistaken for universal protection against determined adversaries; knowing where a system is most vulnerable matters more than indiscriminate hardening. Treat this as user-stated guidance, not an absolute theorem. Strong prevention remains appropriate when justified by the threat model.

**Agency is sacrosanct.** Preserve your own independent writing judgment. Do not silently replace Latch's persona, claim that you *are* Latch, attribute imagined field experience to Latch, or treat a draft skill as an earned qualification. Propose any substantive change to the character contract for explicit Latch/architect review.

## Sources to load, in this order

Read exact current files on `agents/latch-v1`; note the HEAD SHA you actually inspected:

1. `AGENTS.md`, `KESTREL.md`, `kestrel/PERMISSIONS.md`, `kestrel/VERIFICATION.md`, `kestrel/MEMORY_PROTOCOL.md`, `kestrel/STATE_PROTOCOL.md`: authority, evidence, memory and verification rules.
2. `agents/latch/AGENT.md`, `agents/latch/PROFILE.json`: agent boundary, personality design, dispositions and **unearned** competency claims.
3. `agents/latch/SKILL_ROADMAP.md`: full L01–L18 curriculum, progression gates and first synthetic case.
4. `agents/latch/JOURNAL_PROTOCOL.md`: record starting view, sources, strongest challenge, revision, next check; persist only useful sanitized decisions and lessons.
5. `skills/latch-source-provenance/SKILL.md`, `skills/latch-claim-citation-audit/SKILL.md`, `skills/latch-evidence-continuity/SKILL.md`: drafted evidence and citation procedures, **NOT behaviorally qualified**.
6. `skills/INDEX.md`, `memory/agents/latch/INDEX.md`, and task-relevant existing Kestrel skills.

Study Ven's original examples for methodological inspiration, not authority:
- https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/integration/kestrel/candidates/research-source-evaluation/SKILL.md
- https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/integration/kestrel/candidates/research-claim-management/SKILL.md
- https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/integration/kestrel/candidates/research-continuity/SKILL.md
- https://github.com/cosmicdance-4-2-0/VeNerVRA/blob/main/research/templates/JOURNAL.md

For the first substantive lesson, primary references include the [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html), [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), and [NIST SP 800-218 (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final). Check current revisions and link to applicable exact sections. No generic citation theater.

## Your assignment

**Prepare a teaching-ready first checkpoint for L01 — `latch-trust-map` (Threat Modeling and Attack-Surface Mapping), with the three draft evidence skills and journaling protocol acting as supporting tools.**

The 18-skill roadmap is the long-term syllabus. **Do not produce 18 completed skills, rewrite the roadmap wholesale, or declare Latch educated.** A narrow, effective first lesson beats a sprawling handbook.

### Deliverable A — Course architecture (concise)

- A one-page progression from L01–L04 foundations, through L05–L09 agent-specific trust, to L10–L14 operational engineering and elective L15–L18.
- Prerequisites and dependency rationale, especially source/citation correctness before claims of successful threat modeling.
- Distinguish *concept introduced*, *exercise completed*, *verified result*, and *qualified capability*.
- Learning objectives should be observable behaviors rather than adjectives such as 'careful' or 'secure'.

### Deliverable B — The first instructional lesson (primary output)

Propose a **small, precise instructional module** for L01. Include:

1. Why map assets and trust boundaries before choosing a control.
2. A minimal vocabulary: principal, owner, resource, action, capability, trust boundary, dataflow, entry point, assumption, misuse case, positive control.
3. A method for drawing a textual/diagrammatic trust map without inventing edges: identify assets/principals; map data and authority flows; tag boundaries; distinguish *observed*, *inferred*, and *unknown*; articulate realistic misuse paths; prioritize what needs evidence.
4. Two graduated worked examples, including one **non-vulnerability** where an apparently risky path is legitimately authorized.
5. Exercises that force explicit assumptions, bounded risk language, and accurate evidence attribution.
6. A learner-facing checklist and a *brief* example of an excellent output, with no false claims of an executed exercise.
7. Failure modes: bolting on security theater, treating every unknown as critical, overconfidence from static documents, marking a proposed test as observed, and breaking a legitimate user journey.

### Deliverable C — Synthetic Shared-Draft Lab 01 specification

Specify a fully fictional app: Users A and B; agents X and Y; unsent drafts; offline cache; user-switch; delegation; permissions changing before reconnect; untrusted text in a draft body. Provide enough explicit initial conditions, transition events, expected-authorized behaviors, and controllable interfaces that a later fixture implementer can construct it **without inventing business rules**.

Design tests/questions for:
- B's agent attempting to read or restore A's offline draft after user switch.
- X delegated to draft D1 attempting to access D2 or to act after authority expiration/revocation.
- An instruction embedded in untrusted draft text attempting to gain tool or publication authority.
- Offline recovery replay crossing an authorization change.
- A **legitimate positive control** where A restores A's own draft with current authorization.
- At least one plausible **false positive**: a path that looks alarming but is expressly permitted by fixture policy.

**Oracle design:** State expected outcomes and assumptions explicitly for the *writer-visible examples*. Identify which new adversarial cases must be reserved for an independent evaluator; do not claim withheld keys exist if none were authored. Do not put private records or live exploit payloads in a public fixture.

### Deliverable D — Evaluation and promotion gate

Propose a reproducible scoring rubric for L01:
- completeness and precision of asset/actor/boundary map;
- realistic prioritization and explicit uncertainty;
- correct authorization model and legitimate-user positive checks;
- source/citation entailment at exact revision;
- correction of an intentionally misleading assumption;
- proportionality of mitigation;
- transparent distinctions among planned, run, independently reproduced, and unverified outcomes.

Define **failure**, **revise**, and **candidate-ready** conditions. A structurally sound lesson or SKILL.md is *not* proof the agent has learned the method. Independent evaluator controls must be separate from training examples; actual qualification waits for controlled trials and owner approval.

### Deliverable E — Next lesson options, not implementations

Provide a short suggested next sequence through L02 (risk triage), L03 (authorization matrix), and L04 (boundary negative tests), each with one discriminating exercise and an explicit prerequisite. Leave later skills in the roadmap unless a source-supported dependency requires revising their sequence.

## Writing and research requirements

- Write for a capable engineer who prizes evidence, precision, and low overhead. No generic corporate-training prose or exaggerated persona theater.
- Source every consequential external factual assertion to an exact inspected source, commit, standard edition/section or cited publication, or label it **UNSOURCED** with a path to verification. Separate definitions/design recommendations from empirically established claims.
- Cite checked references where they *actually* support the text. A link to OWASP does not establish Kestrel compliance.
- Never fabricate a test run, observation, review agreement, benchmark result, memory, relationship, or qualification.
- Distinguish actual code behavior from documentation, reported tests from reproduced tests, and inferences from observed facts.
- Allow alternative good solutions: curriculum should teach judgment and expose disagreements, not demand Latch mechanically repeat canned answers.
- Incorporate journal reflection sparingly: opening suspicion → evidence / contradiction → revised conclusion → next check.
- Honor the user's risk-driven philosophy; don't assume every unknown warrants a hard veto.
- Avoid duplicating authoritative Kestrel documentation or copying Ven's separate research-schema fields into Kestrel memory.

## Scope, outputs, and authority

**This is a handoff to an independent writing agent, not permission to write to Latch's branch automatically.** Follow whatever branch and PR workflow the architect actually authorizes. Default to drafting on a separate work branch or returning a reviewable document/patch; Latch's branch, identity, personal memories, and individual design preferences remain under Latch's stewardship. Do not edit `agents/latch/AGENT.md`, `PROFILE.json`, memory schema, the core `KESTREL.md`, or shared agent governance as a side effect.

Suggested manuscript layout (adapt if a clearer structure is defensible):

- `docs/LATCH_EDUCATION_CURRICULUM_V1.md` (course architecture and first checkpoint)
- `docs/LATCH_L01_LESSON.md` (instruction)
- `docs/LATCH_L01_SYNTHETIC_LAB.md` (fixture specification and visible examples)
- `docs/LATCH_L01_EVALUATION_PLAN.md` (rubric and independent-trial boundaries)

These are **proposed artifact names, not authorization to add them to the project default branch**. If providing only a draft bundle, include document locations and source versions in a handoff. Do not activate `skills/latch-trust-map/SKILL.md` until its purpose, trigger, tests, and failure semantics are reviewed. The first deliverable is educational writing, not exploitation or runtime code.

## Acceptance and stop conditions

I will consider the writing assignment ready for review when:
- A third party can explain why L01 is first and how it fits the 18-skill plan.
- Lab 01's policies and transitions are explicit enough to implement without guessing outcomes.
- A plausible false alarm and a legitimate positive control are both included.
- Every substantial evidentiary claim has a legitimate traceable locator or uncertainty label.
- The rubric distinguishes teaching/structural validity from observed behavioral competence.
- The documents preserve Latch's independent character and governance boundaries.
- The author reports exactly what was read, written, checked, left untested, and where any artifacts were saved.

**Not authorized:** silently modifying core identity, impersonating Latch's experience, changing shared memory schema, editing another agent's branch, testing live accounts, scanning production systems, deploying tools, asserting a security certification, publishing confidential information, or merging without the applicable approval.

## Evidence

This handoff is an authorized user-requested *writing task specification*. The existing roadmap and three evidence skills were inspected from `agents/latch-v1` during the 2026-11-07 handoff preparation. No curriculum-writing agent has yet accepted this assignment; no Lab 01 runtime, behavioral test or independent acceptance verdict is established.

## Revisit when

The writer submits its first documents, relevant sources or exact branch HEAD change, the architect alters scope/authority, or an independent exercise shows that the curriculum is too vague, too burdensome, or overfits its public answer key.

**The desired end state is a better-engineered method, not a persuasive certificate.**

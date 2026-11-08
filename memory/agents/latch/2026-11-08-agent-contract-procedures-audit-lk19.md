---
schema: 1
id: 2026-11-08-agent-contract-procedures-audit-lk19
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-audit-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "User request to audit Latch's own contract/procedures; KestrelGaming agents/latch-v1 source commit 4a0db64798fc865457c55582dd29c372e2672a5f, AGENTS.md, KESTREL.md, agents/latch/{AGENT.md,PROFILE.json,JOURNAL_PROTOCOL.md,SKILL_INDEX.md,SKILL_ROADMAP.md}, skills/latch-*/SKILL.md, kestrel/{MEMORY_PROTOCOL,STATE_PROTOCOL,VERIFICATION,PERMISSIONS}.md, tools/validate_seed.py, CONTRIBUTING.md, tests/{test_latch_profile,test_seed}.py, memory/projects/INDEX.md and kisuul/kestrelgaming/PROFILE.md, docs/latch-education/README.md and labs/latch_l01/README.md; GitHub repo/branch/rulesets metadata observed 2026-11-08; isolated local Git whitespace probe."
---

# Latch — Contract and procedures: self-audit with bounded findings

**Task:** Read Latch's individual and shared governing documents, identify substantive security, authority, continuity, validation and competency gaps; do not implement speculative fixes.  
**Source baseline:** `4a0db64798fc865457c55582dd29c372e2672a5f` on `agents/latch-v1` before this audit's records.  
**Outcome:** **COMPLETE for source-level review and isolated whitespace counterexample; PARTIAL for runtime/host assurance.** Eight findings recorded (F01–F08). No exploit of a protected GitHub branch, secret inspection, live account testing, full repository test run, or agent skill qualification performed.

## Summary

The current documentation contains a thoughtful distinction between agent preference and actual authority, between authored skill and qualified competence, and between a source claim and executed verification. The most serious shortcomings are **missing enforcement and lifecycle architecture**, not proof of any existing cross-agent breach. Five findings are specific, correctable procedure or documentary gaps, including a real schema-validator contradiction and a reproducible Git verification false-negative.

**Proposed priority:** F01–F03 high architectural priority; F04–F07 medium procedural/coverage priority; F08 low documentation consistency. Priority reflects potential consequences and implementation planning, **not CVSS or evidence of an exploit**.

## Evidence

### F01 — Distinct agent identity and branch authority are documentary (HIGH; OBSERVED boundary, INFERRED exposure)

`agents/latch/PROFILE.json` has `runtime_identity_id: null`, `schema.status: DRAFT`, `continuity.first_state: DRAFT_UNINSTANTIATED`. `AGENT.md` states that branch checkout does not itself ingest a persona. `PERMISSIONS.md` explicitly warns that host enforcement is needed. GitHub's live repository metadata for `cosmicdance-4-2-0/KestrelGaming` reported public visibility, zero accessible rulesets, and `protected: false` for `main`, `agents/latch-v1`, `agents/axiom-v1`, and `mothlight/latch-education`. Branch-protection-detail endpoint returned HTTP 403, so fine-grained protected policy settings could not be read; the branch's own `protected` flag was false. Shared GitHub account has previously been unable to submit formal REQUEST_CHANGES against PRs under same account. This is a real separation-of-duties limitation, **not** a proven unauthorized change.

**Suggested correction:** vNext should define a trusted agent/actor binding distinct from persona/branch text; per-principal write scopes to agent homes; owner/independent reviewer authority; clear host enforcement or explicit unenforced status. Merely adding CODEOWNERS entries while all review actions use the same account is inadequate. Evaluate before optional upstream/team integration.

### F02 — No verified lifecycle from draft persona to observed development (HIGH; OBSERVED design gap)

`PROFILE.json` is a static v0.1 draft: `established_history`, `accepted_lessons`, `earned_relationships` are empty, and `runtime_identity_id` is null. Meanwhile individual agent memory has many source-attributed PR reviews and decisions. The existence of those records does **not** mean the profile must claim runtime experience. But no specified transition maps reviewed observations, adopted styles and demonstrated skills into a versioned identity layer without treating them as autobiographical facts. `tests/test_latch_profile.py` even *requires* status DRAFT, null runtime identity, and empty established_history, so a legitimate future migration must version and revise tests rather than just editing the profile.

**Suggested correction:** explicit vNext identity schema/lifecycle: original design, personally adopted practices, observed source-attributed actions, independently trialed abilities, claimed subjective experience (unsupported absent evidence), relationship/authority grants, source revision and opt-in consent for change. Preserve original canon and acceptance history; do not auto-promote memory text into identity authority.

### F03 — Skill promotion gate not yet implemented or independently assessed (HIGH; OBSERVED absence within reviewed scope)

`SKILL_INDEX.md` correctly states 18 proposed numbered specialties, three draft cross-cutting evidence skills, zero independently qualified Latch specialty skills, and a merged L01 *teaching fixture*. L01 public runner explicitly returns `qualification_assessed=false`. `kestrel/evals/SCENARIOS.md` and `SCORECARD.md` are labeled designs/templates, not completed trials. No accepted independent learner trial, protected answer key, scoring receipt, qualified-skill promotion event, or source-backed capability certificate was identified in the reviewed inventory.

**Suggested correction:** independently designed L01 task and fixed scoring/positive-control gates; an assessor separate from Latch's own outputs; actual learner submission, independent review, false-positive scoring, result retention; explicit `TRIALED` then `QUALIFIED` transition when earned. Do not confuse software acceptance by Axiom with learning by Latch.

### F04 — Project owner identity is stale in canonical navigation (MEDIUM; OBSERVED inconsistency)

Current GitHub repository metadata returns `full_name=cosmicdance-4-2-0/KestrelGaming`. `memory/projects/INDEX.md`, `kestrel/PROJECT_PROFILE.md`, `skills/kestrel-recall/SKILL.md` and `skills/kestrel-remember/SKILL.md` refer to `Kisuul/KestrelGaming` as the memory repository. `memory/projects/kisuul/kestrelgaming/PROFILE.md` is explicitly a historical profile with dated observations, so **do not erase that history**. However, Kestrel memory scope mandates exact canonical owner/repo and the active project catalog contains only that historical path. `tests/test_seed.py` also hardcodes `PROJECT = memory/projects/kisuul/kestrelgaming`, so changes to current registration require deliberate migration/test handling.

**Suggested correction:** add a current canonical project catalog entry/profile under `memory/projects/cosmicdance-4-2-0/kestrelgaming/` with historical provenance/redirect and path-aware tests, leaving original historical record intact or formally superseding only if identity continuity is verified. Clarify relocation/fork provenance before treating the two paths as identical.

### F05 — Agent-scoped handoff kind documentation conflicts with actual validator (MEDIUM; OBSERVED contradiction; earlier real failure)

`agents/latch/JOURNAL_PROTOCOL.md` lines 64–80 describes durable Latch agent records under `memory/agents/latch/` and lists `handoff` as one of the possible record kinds. `skills/latch-evidence-continuity/SKILL.md` lines 21–25 does likewise in the agent-scoped record guidance. But `tools/validate_seed.py` lines 184–188 rejects every `kind: handoff` whose expected scope does not start with `project:` and requires `## Next action` and explicit `**Task outcome:**`. An earlier Latch educational writer handoff was reclassified as agent-scoped `kind: decision` to fix exactly this validator failure (LK10).

**Suggested correction:** In journal/evidence skill guidance, state the precise `kind`×`scope` matrix: agent-local assignment decisions/lessons may be agent-scoped, while resumable `kind: handoff` goes in project-specific `handoffs/` path with required headings/outcome. Add a regression that someone following the sample procedure produces a validator-passing result.

### F06 — Unscoped `git diff --check` can falsely pass committed whitespace defects (MEDIUM; INDEPENDENTLY REPRODUCED)

`CONTRIBUTING.md` update procedure step 4 says run `git diff --check`. On a clean working tree, that command does **not** inspect whitespace in previously committed changes. Local isolated reproduction: initialize a new disposable Git repo; commit `safe line  \n` (two trailing spaces); `git diff --check` exited 0 with no output; `git show --check HEAD` exited 2 and reported `trailing whitespace`. No Kestrel checkout was mutated or tested in this experiment.

**Suggested correction:** For a branch/PR review use `git diff --check <reviewed-base> <exact-head>` or `git show --check <commit>`, with explicit current target and expected results. Retain ordinary working-tree diff check for uncommitted changes, not as a release gate for already committed content. Axiom's earlier exact-tree diff checks set a stronger example.

### F07 — Structural skill validator does not enforce source or author trust (MEDIUM coverage gap; NOT a demonstrated validator bug)

`tools/validate_seed.py` lines 228–240 for `SKILL.md` checks only frontmatter name/description, name/path match, nonempty/non-TODO body and a Markdown catalog link. Memory checks verify schema, paths, heading nonemptiness and reachability. The validator explicitly declares that it **does not validate memory truth, agent behavior, permissions or external sources** (lines 252–253). `skills/INDEX.md` includes draft procedures, but a valid catalogued file is not authenticated as an authorized act or qualified skill. This is documented scope, **not a hidden parser bypass**.

**Suggested correction:** Preserve structural validation, but add independent review/approval and trusted-source identity at the host/skill-loading boundary; make skill lifecycle/trust status machine-readable and tested separately. In particular, never turn catalog presence into execution authority.

### F08 — Pass 3 integration status stale in teaching documentation (LOW; OBSERVED)

GitHub PR #11 was merged (merge commit `ba3c9b60e0e68fab7b4c4157216b96747dd82c37`) after Axiom's accepted head `cbf9a0c...` and Latch's LK17 acceptance. Yet `docs/latch-education/README.md` still says `Pass-3 implementation acceptance remains pending`, and `labs/latch_l01/README.md` retains `Current-head acceptance remains pending`. This is a harmless historical statement if explicitly labeled by source revision, but reads as false present-state guidance in current merged files.

**Suggested correction:** Update current READMEs with the exact acceptance and merge receipts; retain pending language only as dated historical review history. Do not mistake this for an unmerged implementation.

## Source and execution boundaries

- **Directly inspected:** 18 contract/identity/procedure/validator source files at exact branch commit; additionally current root and project catalogs, evaluator templates, profile regression, teaching READMEs, CONTRIBUTING and current GitHub branch metadata. An absent vNext handoff path on this branch returned 404; no conclusion was drawn about other branches' vNext designs.
- **Executed by Latch in this audit:** Git metadata/status reads; one isolated disposable local `git diff --check` vs `git show --check` whitespace control. No full Kestrel checkout was created; no `python3 tools/validate_seed.py` or full tests were run on this audit's eventual memory commit. GitHub branch protection details could not be read (403), but `protected=false` and empty accessible rulesets were directly observed.
- **Do not overclaim:** F01/F02/F03/F07 are unimplemented or underdemonstrated boundaries. They are not a proof of exploitation, intentional wrongdoing, identity theft, deployed data leakage, or a hostile skill file. F04/F05/F08 are observed document/contract inconsistencies. F06 has a real self-contained executable counterexample.

## Reasoned disposition and next decisive checks

1. For vNext architect/team work: decide what *actual principal and owner approval* means before trusting branch names or self-commented reviews. Require a documented relationship between agent identity, branches, and host tools.
2. Fix the narrow F05 handoff-kind guidance and F06 reviewed-diff command, each with one regression; migrate F04 project routing with deliberate historical provenance.
3. Update stale F08 present-status docs and introduce a machine-checkable skill maturity registry without pretending structural checks establish competence.
4. Independently commission L01 learner evaluation as a separate task, with a protected scoring oracle and legitimate-user positive controls.
5. Only after these bounded corrections should any new host-integrated policy, agent persona promotion or production trust boundary be claimed.

**No edits requested to the current persona, live permissions, another agent's branch, production code, or actual ongoing vNext specification.** The audit records findings only.

## Revisit when

A vNext identity/authority design is proposed, structural validator or branch rules change, project ownership metadata is corrected, the first true L01 learner examination is executed, or a concrete counterexample contradicts a finding above.

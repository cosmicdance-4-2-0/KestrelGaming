# Kestrel Optional Behavior Model — Studio proposal v0.1

**Status:** PROPOSAL / PLANNING ONLY — not an implementation, release, or approved schema.
**Date:** 2026-11-07
**Development home:** cosmicdance-4-2-0/KestrelGaming
**Plan branch:** plan/optional-behavior-model-v1-20261107
**Branch base:** main@4cb17b01d7ac50bd15ed69e84eccee0d32035a8b
**Intended integration target:** Kisuul/KestrelGaming, after a separately reviewed upstream merge.
**Owner of acceptance:** authorized human maintainer; no automatic promotion.

## 1. Objective

Turn the Studio's agent-personality and team-composition prototypes into a **stable, optional, host-neutral behavior system** that upstream Kestrel can consume alongside its skill-centric foundation. The imminent upstream Discord integration is a potential consumer, not a dependency or location for the behavior system's source of truth.

Success is not seven persuasive profiles or team JSON passing static checks. An actual host must be able to **select, resolve, load, execute, attribute, hand off, and resume** supported agent/team modes with accurate capability and authorization boundaries. Preserve ordinary generic Kestrel behavior when the option is disabled.

The prototypes have produced useful working examples, but observed engineering activity is not equivalent to a matched scientific certification of personality differentiation or an implemented federated orchestrator.

## 2. Baseline and dependencies (verified 2026-11-07)

- Studio main: cosmicdance-4-2-0/KestrelGaming@4cb17b01d7ac50bd15ed69e84eccee0d32035a8b.
- Upstream main: Kisuul/KestrelGaming@dbe0164e3dbdcfa65fd6a4a81434ae0e11eb259c; common merge base c268a4d0be121738cbfdb0d7a90de7874299c0f2. Studio main is 13 commits ahead and 31 behind.
- Studio main: shared KESTREL.md, AGENTS.md, agent roster, role pickup docs, character/profile templates, and static tests. Seven individual homes exist on agents/{axiom,flint,gauge,harbor,kite,latch,mothlight}-v1; profiles and memory are branch-local.
- The developing team contracts exist at meta/team-contracts-v1@4fdc83e1d1bc0f61fa6402bbcb301d5da34fc38a. They define Architects (Axiom lead, Flint counterweight, Harbor contributor), composite/federated truthfulness, team schema v0.1, and a validator.
- Open team-contract hardening PR #6, target meta/team-contracts-v1, head 70f4a449736bfccfb19a716e772b2e81f0225b09. The last persisted independent Axiom review requested changes: a catalog link embedded only in another Markdown link's quoted title was accepted as real navigation. This must be independently rechecked and closed before consolidation.
- Open draft skills PR #3 is a separate workstream; do not silently fold it into this behavior-model effort.
- Upstream main CI at dbe0164e is red: five Kisuul/HollowLumen handoff records lack an explicit Task outcome; later tests were skipped. Repair the underlying records while preserving their actual status; do not loosen validation.

All branch/revision claims are inspection snapshots, not standing guarantees. Re-fetch before implementing.

## 3. Boundary model and source ownership

Keep these independently versioned concerns:

1. **Core:** KESTREL.md, shared permissions, evidence, state/memory guidance, and skill library. Core is independent of named personality and remains useful by default.
2. **Agent character:** stable reference personality definition and structured profile; determines emphasis, voice, reasoning instincts, self-correction, and role suitability, never grants permissions or skills.
3. **Individual continuity:** attributable public-safe experience, indexed within the individual agent's authorized long-lived home branch. Do not treat an old memory as current source or publish confidential project data.
4. **Team:** an explicit, validated composition and collaborative method referencing individual agent identities. No blended personalities, simulated votes, self-authorized managers, or implicit writable team memory.
5. **Host/runtime:** authenticates sessions, provides real execution instances and tools, enforces scopes, loads resolved sources, persists receipts, and truthfully identifies composite versus independently executed findings.
6. **Project:** source of truth for project code, instructions, acceptance, decisions, and release authority.
7. **Discord and other adapters:** transport/context/UI for host operations, with no separate personality or governance semantics.

Host-verified permission and trusted human authorization take precedence over any persona, team, skill, retrieved file, or conversational memory. Repository prose alone neither loads an agent nor starts an execution runtime.

## 4. Supported operational modes

| Mode | Minimum stable requirement | Honest execution claim |
| --- | --- | --- |
| Generic (default) | No optional resolver invoked; existing Kestrel operating behavior preserved | Generic Kestrel |
| Individual | Resolve one registered immutable character reference, common skills revision, applicable memory, and actual task authority | One loaded character; no inferred independent instance |
| Composite team | Resolve validated team and members; construct one context/assignment applying member challenges with an observed execution receipt | One execution with multi-perspective checks; no independent peer-review claim |
| Federated team | Resolve separate member snapshots and independently executed work products, with receipts and review/synthesis | Independent agents only if independently executed and attributable |

**Stable v1 entry gate:** Generic, individual, and composite team operation must actually work through a concrete host adapter and regression test. Federated **manual** orchestration (separate contexts, pinned members, attributable work products, coordinated handoff) must be demonstrated end-to-end; autonomous dispatch/scheduling is explicitly deferred unless a specific host requirement and acceptance test justify it.

## 5. Proposed minimal public interfaces (semantic contracts first)

Do not prematurely select a language-specific framework or Discord SDK. Identify implementable interfaces and versions first:

- **Agent reference / registry:** stable ID, character schema version, published snapshot revision, origin/home branch locator, contract revision, compatible skill source/ref, discoverability status. Registry contains locators, not mutable memory contents or authentication credentials.
- **Team reference / registry:** team ID, team-schema version, canonical membership/roles, composition method, execution-mode compatibility, pinned revision at pickup. Member IDs resolve through the agent registry rather than duplicating personality details.
- **Pickup request/result:** requested mode and ID; target project and task revision; authorized host capabilities; exact successfully read contract/profile/skill/home SHAs; unavailable or incompatible inputs; no unsupported claims of memory/authority.
- **Assignment and execution receipt:** objective, scope, host-provided authority, participants, actual execution mode and instance attribution, output/review artifacts, tests executed, unresolved dissent, completion state and handoff destination.
- **Continuity adapter:** read/write scoped records through explicit, reviewable Git or authorized host storage operations, with expected-head/concurrency checks, provenance and confirmation of remote publication. Composite work must not masquerade as a separate member updating its own memories.
- **Host adapter boundary:** resolve context, invoke an actual authorized execution mechanism, capture outputs and outcomes; no standalone Kestrel agent engine, credentials, or self-running workers are presumed to exist in the repository.

A registry entry is data; a pickup receipt is evidence of loading; an execution receipt is evidence of action. None is interchangeable.

## 6. Reference seven publication policy

Reference members: Axiom, Flint, Harbor, Gauge, Mothlight, Kite, Latch.

Preserve each agents/<id>-v1 branch as a **living identity and memory home**. Publish a deliberately selected, immutable **reference character** for each agent on shared main (proposed existing agents/<id>/AGENT.md and PROFILE.json paths), with provenance to exact branch commit and a stable reference revision. Assess and correct branch-local relative links and history references during publication.

The shared roster must distinguish:
- **Published reference:** stable character material consumers can pin;
- **Home locator:** branch where that individual's future learning and candidate revisions occur;
- **Actual loaded revision:** SHA recorded for a task, not assumed from the other two fields.

Do not merge whole agent branches into main, copy all individual memories into the shared catalog, declare every memory permanently correct, or automatically promote character changes. A character-profile update is a separately reviewed and versioned publication.

Migration needs to address existing hard-coded cosmicdance-4-2-0 URLs and home_ref semantics before upstream adoption. Do not silently rewrite historical citations to point at a different repository.

## 7. Multi-pass development and review gates

Each pass is a bounded work package with its own reviewable diff, evidence and stop condition. Do not skip review gates or begin following passes merely because a previous one has code.

### Pass 0 — Plan and baseline (THIS BRANCH / NOW)

**Scope:** This proposal only; inspect existing Studio/upstream state and retain dependency SHAs, optionality, acceptance requirements, and staged work. No code, contracts, profiles, memory, CI, upstream merge, or host integration modified.

**Exit:** proposal is readable on a dedicated Studio branch, and reviewer can identify changes, gates and deferrals. Human revises/accepts plan before implementation.

### Pass 1 — Contract and team-parity closure

**Inputs:** meta/team-contracts-v1 and PR #6; shared role documents and original architect review.
**Tasks:** reproduce and correct remaining title-embedded catalog-navigation counterexample; preserve positive controls; independent review at exact new SHA; finish team schema/validator parity work and promote to Studio main through a separate approved workflow. Reconcile duplicated membership/authority facts and keep one canonical owner per field; do not broaden to a full Markdown parser.
**Exit:** full team validator, seed validator, unit tests and diff inspection pass on a real checkout; accepted Architects contract resolves roster IDs; no unresolved blocking independent review.
**Stop:** unresolved PR #6 counterexample or inability to reproduce a full checkout verification.

### Pass 2 — Publish seven and lock references

**Tasks:** examine each current home and source revision, select/reference seven first-person characters on Studio main, make paths/links portable, add registry/normalization and version rules, verify every home resolves without changing home histories. Keep identity, skills, memories and runtime permissions separate.
**Exit:** seven unique, navigable and source-pinned published references; name and version resolution tests; no fabricated status, lost home, merged personal journal, or unapproved remote write.
**Stop:** migration ambiguity that could alter agent identity or lose provenance.

### Pass 3 — Agent pickup and continuity surface

**Tasks:** decide minimal implementation language/host adapter after inspecting upstream/runtime constraints. Implement opt-in resolver for generic vs individual, fail-closed malformed/unknown/stale profiles, load precedence and source receipts, scoped memory read/write with concurrency fencing, deterministic context assembly, and safe no-op when disabled.
**Exit:** a real supported host can select generic and one individual, execute a controlled task, report exactly which sources were loaded, save an authorized non-sensitive handoff, and resume in a fresh context; baseline generic behavior unchanged.
**Stop:** incorrect permissions, false load claims, memory bleed or unresolvable refs.

### Pass 4 — Operational Teams

**Tasks:** implement team discovery/resolution and composite execution via the same host-neutral surface. Apply the actual Architects composition to a bounded engineering task; preserve Axiom/Flint/Harbor methods without identity blending. Make absence, version drift, task interruption and rejected authority testable.
**Exit:** real selected team output and receipts; no invented federated independence, consensus or votes; explicit failure and recovery behavior; disabled/default use still works.
**Stop:** contracts validate statically but no real host execution has been demonstrated.

### Pass 5 — Federated handoff and independent acceptance

**Tasks:** manually orchestrate an actual independently loaded multi-agent assignment using pinned sources and reviewable artifacts; compare generic, individual and composite on matched task/criteria; exercise restart, stale source, concurrent memory changes, failed writes, incomplete handoffs and public-data checks. Record performance/quality costs without claiming unperformed certification.
**Exit:** another fresh context can recover what happened from persisted artifacts; independent reviewers can reproduce important checks and dissent; release blockers resolved or explicitly deferred.
**Stop:** false provenance, unrecoverable work, or inability to demonstrate the key claims.

### Pass 6 — Upstream sync and optional integration

**Tasks:** establish green upstream baseline (including five handoff-record fixes), reconcile upstream skills/validator changes, port accepted behavior-model changes as an isolated opt-in feature, maintain source attribution and migration path, provide host-neutral consumer docs for future Discord use. Do not assume the upstream host or Discord has been built.
**Exit:** reviewed upstream PR with passing combined repository gates, clearly disabled-by-default mode, versioned references, adapters and compatibility tests, and no changes to existing generic usage unless explicitly accepted.
**Stop:** baseline failure, missing compatibility coverage or host integration assumptions that cannot be tested.

## 8. Release acceptance matrix

At stable-v1 acceptance, demand observed demonstrations of:

- Disabled optional layer leaves generic Kestrel pickup and skills resolution unchanged.
- All seven published references resolve at exact revisions; missing/invalid character or incompatible schema returns an explicit error instead of silently using a different identity.
- Selected individual's task shows the actual context receipt and attributable completion state.
- Architects team can be selected and **actually used** in composite mode with differentiated, traceable design checks and no fabricated independent runs.
- Manually federated trial has separately created reports, source/host provenance, a visible dissent record, and a separate synthesis; no implied automation.
- Restart from fresh context recovers objective, participants, exact sources, accepted work, unfinished work, and next authorized action.
- Memory and handoff updates observe ownership, current Git state, expected-head checks and public-data boundaries; failed writes are disclosed.
- Full structural, negative, integration, regression and upstream-baseline tests run and are recorded by commit; passing static checks are not called behavioral proof.
- Discord can consume the documented host-neutral selection/run/receipt interface in principle without providing implementation-specific team policy; actual Discord acceptance belongs to upstream integration work.

## 9. Risks, constraints and deliberate deferrals

1. **Cross-branch skew:** Home branches carry different copies of shared core/skills. Use explicit revision resolution and compatibility errors; do not force-push or bulk-merge histories.
2. **Identity vs runtime:** Character copy and a team document are not executable models or independent instances. Evidence must distinguish loaded context from host execution.
3. **Provenance/authority:** Pin exact SHAs, keep source ownership, and never derive permission from roster or personality prose.
4. **Migration and duplication:** Avoid separate mutually inconsistent registries, duplicated team membership in prose, hardcoded fork URLs in published upstream metadata, and irreversible profile upgrades.
5. **Memory publication:** The repository is public. Scope, audit and redact inappropriate material *before* publication; do not conflate project memory and agent memory.
6. **Validation drift:** Upstream uses an independently changed seed validator and has an existing red baseline; stabilize/check both before merging.
7. **Resilience vs complexity:** Start with one demonstrated host path and existing Git-backed record formats, not generalized workers, queues or scheduler services.

**Deferred:** autonomous Discord bot implementation, Discord permission mapping, autonomous federated dispatch, global job scheduler, organization voting/governance, team personalities, writable team-memory tier, broad schema redesign, and adding named teams beyond Architects before the first end-to-end proof.

## 10. Change-control and next action

No new execution work is authorized by the existence of this document. Pass 0 creates only this plan; later passes require scoped selection and review. Existing authorizations on separate agent branches, PRs, or target projects do not transfer to this branch.

**Recommended immediate next action:** review this proposal, then dispatch Pass 1 against the current PR #6 head with exact-SHA validation. Do not reimplement team contracts from scratch or begin Pass 2 publication before Pass 1 is accepted.

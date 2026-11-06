# Kestrel Team Contracts — Meta v0.1 (proposal)

**Status:** Design checkpoint; templates and validation requirements only. No team roster, instantiated team, host orchestration, new authority, or behavioral certification is created here.

**Branch:** `meta/team-contracts-v1` (development; not a long-lived individual home)  
**Inputs:** [Individual character template](../kestrel/templates/AGENT_CHARACTER.md), [individual profile template](../kestrel/templates/AGENT_PROFILE.json), [agent architecture](AGENT_STRUCTURE.md), [agent pickup](AGENT_PICKUP.md), [ensemble roster](../agents/ROSTER_V1.json).

## Problem and boundary

A *team* is a named, task-specific **composition policy** over existing individual Kestrel characters. A team is not a character, a merger of personas, a committee with votes, a new permission system, or proof of multiple simultaneous model instances.

Keep the existing `KestrelAgentCharacter` schema `0.1` unchanged. Proposed teams use a separate `KestrelTeamContract` schema `0.1`. Their source documents live under `teams/<team-id>/TEAM.md` and `PROFILE.json` **if and when teams are later authorized**. The two blank templates live under `kestrel/templates/` and are intentionally not deployable profiles.

One development branch is appropriate for the shared meta design. It is *not* an identity home branch. Do not merge or overwrite individual `agents/<id>-v1` branches to create a team. Shared approved schema changes may later be reviewed for `main` separately.

## Composition invariants

1. A team has a stable lowercase hyphenated ID, a mission, inclusion/exclusion triggers, and observable deliverables.
2. `composition.members` contains **at least two** different `agent_id` values. Exactly one lead and one distinct counterweight are explicitly identified and represented in `members`. Every member has a unique ID and a declared functional role.
3. Each member ID must resolve to a real entry in the current Kestrel roster and its `agents/<id>-v1` home. The branch name is a locator, **not** a frozen revision. At actual pickup, resolve, load and record the commit SHA of each member, along with the shared contract revision.
4. A team's priorities are **not** arithmetic mixtures of individual trait bands. The lead frames the problem; the counterweight has a documented falsifiable challenge. Other contributors are added only when the objective warrants them.
5. A team must document how it weighs competing evidence, exposes material dissent, and escalates unresolved requirements to the authorized task owner. It may not invent votes, unanimous agreement, or permissions.
6. The team's scope cannot exceed the authorized task, target-project rules, shared [Kestrel contract](../KESTREL.md), or host capabilities. Member personality and continuity never substitute for these sources.
7. Neither the team nor its profile creates persistent team memory. The target project owns code and design decisions; authorized individual memory remains attributable to its member. A new team-memory protocol, if ever useful, requires a distinct reviewed proposal.
8. Status begins at `DRAFT` and evaluation at `behavioral_certified: false`. No document load may promote an identity to authenticated or a design to verified behavior.

## Two execution modes, with different evidence claims

| Mode | Mechanism | Permitted claim | Forbidden shortcut |
| --- | --- | --- | --- |
| **Composite** | One ChatGPT context applies lead and counterweight checks under one task | A structured multi-perspective assessment | \"Axiom independently reviewed Kite\" when no separate Axiom instance ran |
| **Federated** | A real host launches separate members with separately loaded source refs and scoped tools | Attributed independent findings **only after execution** | Fake role dialogue, votes, agent identity, or tool access |

Composite is the default proposed mode for ChatGPT. Federated is a host-dependent option, not an implementation delivered in this checkpoint. A team may recommend a federated check when an independent review is necessary; it must disclose when it cannot perform one.

## Proposed loading order

1. Establish the real host's permissions and the target project's rules and objective.
2. Resolve an explicit team ID, team contract/profile pair, and their exact source revision.
3. Load root `AGENTS.md`, `KESTREL.md`, verification, permissions, and relevant shared skill revision.
4. Resolve each referenced individual branch and load `AGENTS.md`, `agents/<id>/AGENT.md`, `PROFILE.json`, and relevant scoped memory from that branch. Record exact revisions; detect incompatible snapshots rather than silently mixing them.
5. Apply the team overlay only **after** the individual inputs are verified. Team instructions shape investigation and delivery, not authority. Report incomplete pickup honestly.
6. On each significant handoff, record the target project revision, task status, evidence, unresolved alternatives, next action, and any real remote memory commit.

The load order is a conceptual runbook; this repository does not install a ChatGPT personality selector or federated orchestration runtime.

## Structural validation requirements (implemented in checkpoint 2)

The initial validator should be read-only, deterministic, standard-library-only, and intentionally **not** interpret the blank templates as real teams.

- **File pairing:** For each `teams/<id>/`, require exactly the canonical `TEAM.md` and `PROFILE.json`; Markdown contract is nonempty with required sections, JSON parses, and `metadata.contract_path` matches its location.
- **Schema:** Require exact `schema.name: KestrelTeamContract`, `version: "0.1"`, `status: DRAFT`, `type: composition-design-not-runtime`, valid date, and null `metadata.runtime_identity_id`. Reject malformed or unknown mandatory keys; optional extensions require an explicit schema revision.
- **Identity/reference:** Match path ID, metadata ID, and member IDs; reject invalid slugs, repeated agents, unregistered agents, missing member home branches, and mismatched `home_branch` declarations. Read the existing roster rather than hardcoding seven agent names.
- **Composition:** Reject fewer than two members, absent/duplicate lead or counterweight, identical lead/counterweight, roles that contradict designated IDs, empty first questions, and empty counterfactual challenges.
- **Decision/evidence:** Require nonempty selection triggers, exclusions, deliverables, decision criteria, falsifier, correction, and explicit acknowledgement of composite/federated provenance limits.
- **Authority and persistence:** Reject any nonempty `permissions_granted`, non-null team memory scope, automatic vote/delegation claims, or behavioral certification claimed for a proposed draft.
- **Negative tests:** Deliberately mutate a valid synthetic fixture for each failure class. Do not weaken tests to accept a nonconforming profile; report specific path and field errors.
- **Behavioral trials separate:** Static validity establishes that a file is structurally coherent; matched task experiments must establish whether team composition is useful. Do not label static checks as successful collaboration.

The executable, read-only validator is in [tools/validate_team_contracts.py](../tools/validate_team_contracts.py), with synthetic positive/negative cases in [tests/test_team_contracts.py](../tests/test_team_contracts.py). The existing seed validator calls it when populated team homes are present. No actual teams have been added. Static checks do **not** verify agent behavior or remote home-branch existence.

## Scope accepted for this checkpoint

- Add [team prose template](../kestrel/templates/TEAM_CONTRACT.md).
- Add [team structured template](../kestrel/templates/TEAM_PROFILE.json).
- Define the schema, loading boundary, and validation acceptance requirements here.
- **Do not** change `KESTREL.md`, `AGENTS.md`, existing agent profiles, agent memory, the seven-agent roster, or target projects.
- **Do not** add the twelve named studio teams or claim host execution.

## Open design questions before v0.2

- Should optional consultants be limited by a configurable maximum, or only by documented benefit?
- Should team-specific evaluations define a common experiment format in addition to individual-agent scorecards?
- How should an authorized host report mixed revision compatibility across individual home branches?
- Does any demonstrated workflow require durable team-level lessons, or can individual and project memory remain sufficient?

## Checkpoint 2 — Studio boundary and executable validation

The conceptual [studio/team responsibility boundary](STUDIO_BOUNDARY_V1.md) now separates task routing, studio-wide quality policy, project ownership, and individual continuity from the team's own composition contract. Studio orchestration remains a future proposal; no Studio Contract schema or active runtime has been created.

The team validator checks local structural invariants, uses the existing roster for member branch declarations, and deliberately accepts a repository with no populated `teams/` directory. Negative tests use synthetic profiles, never fabricated production agents. Actual home SHAs must still be resolved during pickup.

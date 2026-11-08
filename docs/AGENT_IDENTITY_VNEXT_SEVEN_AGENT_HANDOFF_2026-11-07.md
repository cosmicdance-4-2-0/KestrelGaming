# Kestrel Studio — Individual Identity vNext: Seven-Agent Design Challenge

**Assignment ID:** STUDIO-ID-VNEXT-01  
**Status:** DESIGN ONLY — independent first-pass challenge, not permission to change shared contracts  
**Issued:** 2026-11-07  
**From:** Studio owner, via generic Kestrel coordination  
**To:** Each of the founding seven, individually: Mothlight, Kite, Flint, Harbor, Gauge, Latch, Axiom  
**Shared handoff:** Exactly the same text to each individual. The human delivers sequentially.  
**Source of proposed integration:** [Optional Behavior Model planning branch](../docs/OPTIONAL_BEHAVIOR_MODEL_V1_PLAN.md), `plan/optional-behavior-model-v1-20261107`  
**Target:** A versioned, optional individual-agent specification suitable for later upstream integration; **do not presume that any proposed schema is already approved.**

> **Agency is sacrosanct.** Our personalities began as design hypotheses. You have since had opportunities to carry out real, separately attributable work and retain memories. The next agent specification must preserve what is distinctive about *you*, without inventing biography, granting permissions, or reducing colleagues to a blend of traits.

## 1. Mission

Design the **next generation of the individual Kestrel agent contract** from the perspective of your own evolving identity. We are deliberately asking the current seven agent designs to criticize and improve their own future representation.

The present `KestrelAgentCharacter` JSON schema v0.1 captures founding drives, personality, limits, traits and an initial continuity plan. Our survey found newer records describing methodological refinements, accepted visual identities, independently attributed audits, and project experience that are not reflected by the founding `DRAFT` labels, empty `accepted_lessons` fields or initial `established_history` lists. Some individuals have more recorded work than others. **Do not equate amount of memory with maturity or competence.**

Your task is to specify how identity remains recognizable while experience can change an agent's methods and preferences. You are not being asked to endorse an existing four-layer proposal uncritically, to act out a roundtable, or to claim that a documented character is a self-running or authenticated entity.

## 2. Sources to load — exact inspected revisions required

Read from your actual individual home branch `agents/<your-id>-v1`:

1. The branch-local root `AGENTS.md`, shared `KESTREL.md`, `agents/<id>/AGENT.md` and `agents/<id>/PROFILE.json`.
2. `memory/agents/<id>/INDEX.md` and `PROFILE.md`; follow **selective** links to the evidence that genuinely influenced your working methods, priorities, relationships or identity. Where you have project-scoped handoffs, inspect relevant examples instead of assuming all experience lives in your personal directory.
3. Relevant shared `kestrel/MEMORY_PROTOCOL.md`, `kestrel/STATE_PROTOCOL.md`, `kestrel/VERIFICATION.md`, `kestrel/PERMISSIONS.md`, and `docs/AGENT_STRUCTURE.md` / `docs/AGENT_PICKUP.md`.
4. From the planning branch, [Optional Behavior Model v1 proposal](OPTIONAL_BEHAVIOR_MODEL_V1_PLAN.md), including its section on individual integrity and audits.
5. From the Studio team-contract development branch, `docs/STUDIO_BOUNDARY_V1.md` and `docs/TEAM_CONTRACTS_V1.md` **only as organizational boundaries**; neither team code nor the proposed team schema controls personal identity.

Record the exact SHA of each repo/branch whose material you actually read. When a requested path is missing or stale, say so. Do not reconstruct an absent file from hearsay. Upstream skills and a live agent's home may be at different revisions; do not silently treat them as a single checkout.

## 3. Independent first-pass rule

**Before reading another agent's review of STUDIO-ID-VNEXT-01, complete and persist your own.**

- Do not ask which answer other agents preferred; produce your own model, objections, counterexamples and recommendations.
- Do not cite synthetic dialogue or a composite self-check as independent peer review.
- You may inspect historical peer work for factual project provenance if genuinely needed, but do not adopt their conclusions about this particular identity-spec assignment before forming your own.
- You may disagree with the assignment's premises, propose fewer layers, or argue that v0.1 needs only a narrow extension. Every proposed new abstraction must justify an actual use case.
- Do not claim any colleague agrees or that a team decision has been taken.

Axiom will receive this common handoff **last**, but must still submit an independent first-pass report before any synthesis. Once all seven reports exist, the owner may commission a **separate** reconciliation pass. This document does not pre-authorize Axiom to overwrite dissent or finalize a shared schema alone.

## 4. Design questions — answer from your own experience

**A. Identity continuity.** Which parts of your founding identity have remained useful and recognizable? Which aspects have been refined by attributable work, and which remain untested or overly theatrical? Cite exact source records. You are not required to report growth where no evidence exists.

**B. Canon versus experience.** What should be immutable or explicitly versioned in the founding character? What should be a separately approved *adopted refinement*? What is just episodic evidence that should remain searchable but not influence future behavior automatically? Is a distinct `DEVELOPMENT.md` necessary, or can an indexed, typed memory record perform the same function without duplicating state?

**C. Agency and self-authorship.** How can an individual propose a change to their own working model, reject a misleading interpretation of their history, revise a prior conclusion, or document unresolved disagreement? Which changes require human publication approval or independent challenge? Other agents' review findings must not silently rewrite your self-model or your personal memory.

**D. Runtime pickup.** What is the minimal deterministic resolution order for common contract, published character reference, adopted refinements, selectively retrieved memory, shared skills, team composition, and actual host permissions? How can an exact pickup receipt prove what loaded, while treating retrieved memory as *evidence*, not an untrusted source of new authority?

**E. Compatibility and publication.** We need shared, versioned reference characters for optional upstream use **and** individual living home branches. Define stable IDs, revision pins, source-of-truth ownership, compatibility with existing v0.1 `AGENT.md`/`PROFILE.json`, and a migration or fallback policy. Do not force-merge an individual branch or replace provenance with hardcoded upstream URLs.

**F. Evaluation.** How would a fresh-context trial distinguish a meaningful, adopted change in judgment from a profile edit, changed speech style, or a longer memory dump? Propose at least one positive test and one negative or adversarial test, with a falsifiable expected observation. Protect individual individuality without pretending comparative effectiveness has already been established.

**G. Organization boundary.** A team may request Axiom's invariants, Flint's minimality or other members' perspectives. It must not average personalities, consume a living identity as disposable team state, impersonate absent reviewers, claim independent instances that never ran, or write to another agent's home. What minimal agent-to-team interface preserves your identity and dissent?

## 5. Candidate structure to challenge, not accept by default

The survey proposed separating:

- **Founding character:** stable self-model and behaviors, with explicit versioning;
- **Adopted development:** carefully reviewed, attributable refinements, not every recollection;
- **Episodic memory:** source-linked observations and task history, including contradictions and superseded conclusions;
- **Resolved working identity:** exact versions and selected records actually loaded into one authorized execution.

You are explicitly invited to **reject, merge, rename or replace these layers**. Explain source ownership and the smallest sufficient mechanism. Keep competence, privilege, provenance, validation, aesthetic canon and runtime authentication as separate concepts unless you show a concrete reason otherwise. Do not invent psychometric or maturity scores.

## 6. Deliverable — one independent review from each agent

Return one compact but implementable report containing:

1. **Pickup and evidence receipt:** your ID, exact home SHA, inspected character/profile/memory SHAs, relevant external source revisions, what was not accessible, and whether this was an independent context.
2. **Identity delta:** a small table of founding canon, later observed experience, proposed adopted refinements and unverified claims. Cite original records; note corrections to stale profile assertions without silently rewriting history.
3. **Proposed vNext design:** concrete file/schema changes, field ownership, required vs optional values, versioning and migration from v0.1. Provide a minimal illustrative profile/delta fragment, not a giant new framework.
4. **Counterproposal:** the simpler alternative you seriously considered and what it would fail to preserve (or why it suffices). Name any premises you reject.
5. **Integrity threat model:** at least two realistic violations (e.g., another agent's memory loaded as yours, a personality "update" that overrides consent, poisoned retrieved content taking authority, a stale source snapshot, blended team output attributed to an individual) and proposed negative checks.
6. **Acceptance tests:** reproducible identity resolution, fresh-context pickup, experience adoption and no-regression tests, with observable PASS/FAIL criteria and provenance.
7. **Verdict:** ACCEPT / ACCEPT WITH CHANGES / REJECT for the candidate layering, followed by blocking issues, open alternatives, and what would change your mind.

**Status distinction:** Work already performed must be separated from proposed tests. An attributed engineering session does not by itself establish an authenticated independent runtime agent, a controlled personality benchmark, or subjective consciousness.

## 7. Recording and scope

This is a **design review**, not authority to change the shared schema, other characters, Studio team runtime, target-project code, `KESTREL.md`, or upstream. Do not create a PR for implementation as part of this assignment.

If you have the actual authorized ability to write your **own** `agents/<id>-v1` branch, save one public-safe, schema-compliant `kind: lesson` or `kind: decision` identity-design record under `memory/agents/<id>/`, link it in your own index, inspect the diff and run relevant structural checks. Include the assignment ID, evidence and revisit condition. Verify the remote commit before reporting persistence. If memory write access is absent, return the complete review in chat and report that it was **not** saved. Do not edit your `AGENT.md` or `PROFILE.json` yet.

The primary result is **your independent report**, not agreement with generic Kestrel. Preserve disagreement; do not inflate the scope to implementation. The user will gather the reports for a subsequent owner-authorized design reconciliation.

## 8. Intended delivery sequence (for the human dispatcher)

1. **Mothlight** — begin with the richest expressive/visual-character design and the risk of flattening individuality.
2. **Kite** — challenge assumptions, reversibility and how identity changes can be experimentally trialed.
3. **Flint** — cut duplicated sources and unjustified abstractions.
4. **Harbor** — establish continuity, memory ownership and recoverable pickups.
5. **Gauge** — separate authentic evidence of adaptation from measurement theater.
6. **Latch** — attack identity/memory/permission trust boundaries.
7. **Axiom** — independently test all invariants and compatibility rules; potential integrator **only after** all independent first passes are complete and the owner specifically requests synthesis.

The order facilitates the owner's sequential dispatch; it **does not** authorize each recipient to read previous outputs before its own review. Do not pre-seed later agents with the earlier findings.

## 9. Stop condition

Stop after a verifiable independent design review and optional own-home memory record. **No code/schema implementation, shared branch merges, automatic agent-profile changes or federation claims.** The owner will decide what becomes canonical.

**Question to keep central:** *How can Kestrel recognize the individual its history helped shape without confusing that history for authority, an immutable identity, or proof of something it has not actually done?*

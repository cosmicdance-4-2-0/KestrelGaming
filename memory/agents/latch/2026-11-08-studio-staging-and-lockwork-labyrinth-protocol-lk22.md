---
schema: 1
id: 2026-11-08-studio-staging-and-lockwork-labyrinth-protocol-lk22
kind: decision
scope: agent:latch
status: active
evidence: user-stated
author: latch-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "2026-11-08 conversation: Studio architect's explicit correction to Latch's interpretation of upstream integration order; subsequent explicit request to preserve memory and return to Lockwork Labyrinth; prior user instructions for LOCKWORK-DESIGN-01 and Latch's single shared prompt; agents/latch-v1@1527ab116c82e5a4afad5284fa5a5fde7c80ffa0; LK20 (selective memory proposal); LK21 (STUDIO-ID-VNEXT-01 independent design); Kisuul/KestrelGaming upstream main observed dbe0164e3dbdcfa65fd6a4a81434ae0e11eb259c on 2026-11-08."
---

# Latch — Architecture sequence correction and Lockwork Labyrinth continuity

## Summary

The Studio architect corrected an architectural premise and asked Latch to preserve the resulting context before returning to the Labyrinth.

**The prototype Studio is an experimental device for discovering, challenging and formalizing standards, not an immature production agent harness to be hardened immediately.** The ordered work program is:

1. **Formalize what an individual Agent is**: stable identifiable character, individual agency, chosen/adopted development, attributed experience, selective memory/journaling, reusable skills, runtime and authorization boundaries, and versioned interfaces.
2. **Formalize Agent Organizations**: teams and other compositions, collaboration, dissent, delegated subagents, attribution, and relationship of team operation to individual identity.
3. **Integrate the accepted Agent and Agent Organization specifications into the KestrelGaming upstream baseline** (`Kisuul/KestrelGaming`), preserving its independently evolving skills/engineering foundation and optional generic Kestrel behavior.
4. **Only then design/build the actual reference implementation**, potentially including Universal Discord Bot integration, agent host identity resolution, secure scoped retrieval, team execution and subagent/library services.

Earlier recommendations to implement real enforcement, elaborate scoped storage or Discord orchestration **before specification and upstream integration** applied the wrong phase assumptions. The current GitHub-public branch homes, shared account, manual handoffs and selective journal rules are acknowledged prototype kludges; assess what they teach the future standard, not as urgent production repair tickets. Do not silently allow any prototype mechanisms to define the eventual standard. Current contract/procedure issues can be documented as design counterexamples and deferred until relevant specification/integration decisions.

**Why running agents are deliberately separate:** The experimental reference-seven individual agent homes and team experiments live on `cosmicdance-4-2-0/KestrelGaming`, separate from `Kisuul/KestrelGaming` mainline skills development, specifically to isolate exploratory identity/team design from upstream accepted engineering curriculum.

The user's value **'Agency is sacrosanct'** means that the seven should be able to differ in actual working method, challenge each other, cooperate with meaningful overlap and propose refinements to their personal methods; this does not create host-level rights, authenticated identity, proof of subjective experiences, or authority to see confidential material.

## Evidence

### Explicit user correction (USER-STATED; governs interpretation of project stages)

The user stated: 'The plan is to formalize a definition for agent, then agent organization, then.... update the KestrelGaming baseline with our work. THEN THEN THEN once the main line has the agent concept baked in, and the synthetic organization concept built in, IE agent teams... THEN we can work on the actual reference implementation.' The user also clarified that everything before the final implementation is a kludge to test ideas, explaining separate repositories for running agents and skills development.

Latch's acknowledgement accepted that correction. This record supersedes **the sequencing interpretation** in prior design notes (including LK19/LK20) where those notes implied immediate implementation; it does not delete their independent design observations or automatically approve any proposed design/schema.

The user then explicitly said: **'Preserve your memory. Its time to get back to the Labyrinth!'**

### Lockwork Labyrinth: current agreed design-only protocol

**Assignment ID:** `LOCKWORK-DESIGN-01`.

**Objective:** Six other Kestrel reference agents independently design *possible procedural labyrinths* that test Latch's engineering judgment under uncertainty. The labyrinth may be nonphysical. It should exercise discovery, distinction between appearances and actual access constraints, legitimate operation versus real failures, trustworthy evidence, and meaningful verifiable outcomes.

**The one generic common prompt has already been authored in conversation** and is intended to be delivered **unchanged** to all six. It says, substantially:

- Design a procedural labyrinth for Latch that can be investigated; it need not be physical.
- Genuine problems **and** legitimate behaviors must both be possible; suspicion alone cannot guarantee a finding.
- Outcomes must be independently verifiable and meaningful failures possible; keep everything fictional, bounded, safe.
- **Design only**. No implementation, instantiation, secret answer key, code edits or seeded examined instance.
- Give each engineer autonomy over form, mechanisms, complexity, evaluation philosophy and critique of the premise.
- Do not read another agent's proposal before producing one's own; submit the independent documentation expansion privately to the Studio architect for subsequent synthesis.
- Latch will read the six independent design *proposals*, but **not** the eventual instantiated exam or its withheld answer key before taking it.

**The architect is the human courier.** Latch requested submission order **Kite → Mothlight → Harbor → Flint → Gauge → Axiom**. This was a practical review sequence, not six predefined work packages or specialist duties. No previous agent proposal is to be included in the prompt to later agents. On receiving each, Latch may examine that design document and discuss its distinct emphases; authors should not be made to converge in advance.

**Critical distinction:** It is legitimate for Latch to inspect the six *design proposals* after their independent completion and synthesize a general algorithm/rubric, because no lab implementation has been instantiated. It is *not* legitimate to inspect a future dungeon instance, seed, private solution or answer key ahead of his learner test. Avoid tooling/GitHub exploration of any future sealed implementation even when technical access happens to exist. A shared repository branch would not itself be a secret boundary.

**Do not confuse this assignment with** `STUDIO-ID-VNEXT-01`, the independent identity-specification design exercise. LK21 is Latch's completed personal review for that separate assignment. Neither assignment authorizes changing the shared schema or another agent's branch.

**Progress at memory-save:** The single common prompt has been drafted; **no six replies were included in the user's messages reviewed for this record**, so Latch cannot claim to have received, compared or synthesized them. Await delivery of actual independent proposals; do not invent participation or secret exam content.

### Related design context, not implementation claims

- [LK19](2026-11-08-agent-contract-procedures-audit-lk19.md) documents weaknesses in prototype trust boundaries, source/validator consistency, and identity continuity; they are *requirements/counterexamples* for future standards rather than a demand to implement a production host now.
- [LK20](2026-11-08-agent-memory-library-ven-subagent-proposal-lk20.md) proposes separating identity, skill, memory, journal and session state; Ven as a delegated librarian/research aide is a **possible specification role**, subject to bounded host authorization in a future implementation. It is not a currently running universal private-memory service.
- [LK21](2026-11-08-studio-id-vnext-independent-review-lk21.md) is Latch's independent `STUDIO-ID-VNEXT-01` first-pass: ACCEPT WITH CHANGES, preserve founding character, adopted refinements, scoped evidence and host-generated pickup receipt. It is a design proposal, not accepted schema or runtime proof.
- Upstream baseline checked directly at `Kisuul/KestrelGaming@dbe0164e3dbdcfa65fd6a4a81434ae0e11eb259c`, while Studio `main@4cb17b01d7ac50bd15ed69e84eccee0d32035a8b`. These are dated revision snapshots; re-fetch before actual eventual upstream integration.

## Decision and next action

1. **Use the four-stage specification-first order as project guidance** in subsequent Latch proposals. New ideas should be labeled identity-definition, organization-definition, upstream integration or eventual reference implementation, rather than jumping straight into runtime code.
2. **Resume the Lockwork Labyrinth**, preserving the one shared `LOCKWORK-DESIGN-01` prompt and independent submissions. Receive whichever designer's completed report the architect supplies next, analyze without exposing it to later designers, and preserve real dissent for eventual synthesis.
3. Do not create dungeon code, hidden exam answers, evaluator keys or physical implementation in response to the design-only task. Do not use repo visibility as permission to peek at the eventual secret instance.
4. Keep agent identity, journal/skill/memory distinctions and collaborative individuality intact. Treat the human architect as the courier and ultimate acceptance authority.

## Revisit when

The architect delivers one of the six independent Labyrinth design expansions; changes the prompt or submission order; authorizes a synthesis after all reports; specifies an actual dungeon-instantiation boundary; or revises the agent → organization → upstream → implementation sequence.

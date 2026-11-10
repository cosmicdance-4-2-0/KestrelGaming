---
schema: 1
id: 2026-11-09-stage-fright-stage0-independent-audit-73d4
kind: decision
scope: agent:axiom
status: active
evidence: inferred
author: axiom
created: 2026-11-09
updated: 2026-11-09
sources: "Mothlight STAGE-FRIGHT-V0-REVIEW-01 handoff at MOTHLIGHT_GAME1_STAGE_FRIGHT@09164e820264b7502de58e87d0f31ab5f166592f; all seven independent review inputs read at prescribed immutable design commit 65f470e1c821fcf8c9be85fa0d58399587aabfdb; Axiom home agents/axiom-v1@58a042f60a41cfa2be0ffd4afe29911e0354a9c2."
---

# STAGE-FRIGHT-V0-REVIEW-01 — Axiom's independent Stage 0 design audit

**Agent:** Axiom — The Geometer (`KestrelAgentCharacter 0.1`, draft design personality, not authenticated runtime).  
**Home:** `cosmicdance-4-2-0/KestrelGaming` `agents/axiom-v1@58a042f60a41cfa2be0ffd4afe29911e0354a9c2`.  
**Review source:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT@65f470e1c821fcf8c9be85fa0d58399587aabfdb` — not floating `main` or a later review branch.  
**Assignment handoff:** [Mothlight's signed Stage 0 six-agent handoff](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/09164e820264b7502de58e87d0f31ab5f166592f/docs/reviews/STAGE0_SIX_AGENT_HANDOFF.md).  
**Mode:** Independent first-pass design review, not implementation, code change, PR, merge, gameplay test or owner acceptance.  
**Verdict:** **ACCEPT WITH CHANGES** for the direction; **hold ratification of C00/C01, C04/C05, C09/C10, C11 until interface/fairness questions below are resolved or intentionally scoped as experiments.** This is not a judgment that any implementation is defective; the documents are expressly proposals.

## Summary

Mothlight's most promising decision is not the Ghost's Power meter, the binding route or a pixel-art camera. It is the simultaneous existence of an actual performance, legitimate theater mechanisms, a bounded antagonist, and a physically present player capable of understanding the difference. The critical game promise is that **correctly interpreted evidence changes which actions are rational, and the world respects those actions**.

The smallest falsifier is a single reachable mechanism with one legitimate rehearsed cue and one suspicious event, with time advancing. A player must be able to discover at least one discriminating fact, choose to operate or refrain, and see a consequence causally attributable to that choice. If random clicking is as effective as diagnosis, or the same evidence admits only arbitrary guesses, the core heartbeat is unproven. Do **not** build more systems to hide that result.

The **main architectural risk** is local validity with global incoherence: the Ghost, Director, Show, World, NPC, replay and visual modules are individually specified, but who owns same-tick ordering, physical bindings, knowledge projection, incidents, and semantic visibility remains ambiguous. The source *intends* a single authoritative core, yet does not completely define the contract that prevents those responsibilities leaking across modules.

## 1. Source receipt and source-status distinctions

I read the seven requested design files in Mothlight's prescribed order at exact commit `65f470e1c821fcf8c9be85fa0d58399587aabfdb`:

| Source | Blob SHA | Relevant sections |
| --- | --- | --- |
| `docs/design/STAGE_FRIGHT_DESIGN_v0.1.md` | `26feee1402341b08eb2af8b09ed954a757874b10` | ``3–4`, ``6–10`, `11–12` |
| `docs/contracts/V0_PLANNED_CONTRACTS.md` | `f0e09572f6eae5701650241e1ab4ac93405ac7b2` | C00–C12 and contract ownership |
| `docs/design/V0_GAMEPLAY.md` | `35dd5e67fa9f82e45eb3455cd711e4329ff109d3` | heartbeat, rehearsal/world truths, outcomes |
| `docs/design/V0_DECISION_REGISTER.md` | `97b5e526c15fe258cceedb6f113f6f4433121ccc` | D-001–009; P-001–010; experiment questions |
| `docs/TERMINOLOGY.md` | `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c` | Room/Shot/Play Scene/Production distinctions |
| `docs/design/STAGE1_VISUAL_DIRECTION.md` | `03abd7d16981249a6879c3bc597e98a4d9758358` | art-vs-world ownership; paired Shot trials |
| `docs/ROADMAP.md` | `7ae90a7eac87ca123d9c578b99f33743d893ec1c` | Stage 0–8 gates and non-release policy |

Additional repository-level read-only context at the same **source pin**: `AGENTS.md`, `README.md` and `docs/ARCHITECTURE.md`. The source's `packages/core` is a scaffold and explicitly does not implement the proposed engine.

**Established direction (user-approved as represented by Mothlight):** single-player-first physical stagehand; deterministic headless simulation; genuine hostile House but bounded senses; live, independently operating Play/cast/machinery; legitimate faults and rehearsed effects; completion/evacuation/binding alternatives; modular curated Adventures; fixed-camera layered pixel-art visual starting hypothesis. These directions may be critiqued but should not be silently reversed.

**Proposed design:** Director policy, tiered actions, actor Fear/Trust mechanics, deterministic authored dialogue, binding drain, C00–C12 and illustrative manifest. **Empirical hypothesis:** those mechanisms yield engaging decision-making, fair fear, meaningful improvisation and inexpensive modularity. **Blocking design ambiguities:** findings B1–B4 below. **Speculative / deferred:** fifth-tier crises, sophisticated physics, full content editor, arbitrary third-party scripting, co-op transport, production render pipeline and release plan.

This was an independent review formed **without reading the other five STAGE-FRIGHT-V0-REVIEW-01 reports**. I did not fetch their paths, review summaries or verdicts. The later handoff branch was read **only** to obtain Mothlight's common instructions and immutable design pin. Account-level Git author attribution is not proof of a separate agent instance; this is an Axiom-selected perspective.

## 2. Ranked findings and falsifiers

### B1 — BLOCKING DESIGN CONTRACT: one time source, one transition owner, explicit phase order

**Sources:** [GDD ``4.5, 7.3](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md#L162-L174), [planned C00/C01/C07](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md#L22-L48), GDD `7.3.

**Problem:** The source calls the Play/simulation “two clocks,” while GDD `4.5 says to advance World and Show first, then ghost senses, plans, pays, publishes warnings and resolves effects. It never binds how same-tick player commands, rehearsed Cues, NPC intentions and ghost actions compete for the **same mechanism** or whether a post-tick warning can precede a same-tick hazard.

**Small counterexample:** At tick `t` a rehearsed chandelier sway is due, the player braces the restraint and the Ghost releases it. If Show, player, and Ghost each perform direct world writes, the outcome depends on invocation order. Two legal module executions may disagree about whether the restraint was secured at impact. A deterministic code path can still be **deterministically wrong**.

**Minimum contract:** One world resolver serializes transitions and publishes authoritative events. Simulation **tick** is the only elapsed-time source; Show timing is a state-machine projection/position advanced using ticks, not a separately advancing wall clock. Publish the pre-step snapshot each subsystem may inspect, command envelopes with stable actor/target/tick identity, phase ordering for due cues/player actions/NPC or Ghost proposals/physical effects/perceptions, and ordered collision/invalid-command rules. Define what happens when a command and incident land on the same tick; never select whichever was called first by renderer or import order.

**Proposed proof:** Two permutations of subsystem invocation with identical validated input yield the same state, event order and outcome; scheduled cue and illegal ghost action do not double-write. Render FPS changes no event/tick count. **Tradeoff:** documented phase ordering imposes constraints on pacing creativity, but it removes invisible time and causality loopholes. No need for a universal event bus at Stage 0.

### B2 — BLOCKING FAIRNESS BOUNDARY: a lethal low-cost action needs actionable evidence

**Sources:** GDD ``4.4, 4.7, 10; planned C04/C05/C10; Visual Direction “Legibility and art gates”.

**Problem:** The tier chart says Tier II may cause lethal consequences by releasing stored mechanical energy, while warning rules emphasize higher-tier manifestations. The general guarantee “learnable warnings” does not define whether a player in the reachable danger zone can **respond before irreversible resolution**. Publishing warning and lethal impact in the same tick satisfies naïve “warning exists” validation without being fair.

**Small counterexample:** Ghost pays 15 Power to release a loaded chandelier restraint in the very tick a performer passes beneath it. A creak is emitted, and damage resolves immediately. The audio warning is present in the event log but no legal player command or NPC reaction can precede impact. Its low tier does not make death fair.

**Minimum contract:** Define a **hazard lifecycle** (setup/evidence → commitment → opportunity for diagnosis or response → physical resolution), not a universal artificial two-second countdown. An immediate hazard is allowable only when adequate **earlier discoverable evidence** already existed and reasonable preparation could have mattered. Every potentially lethal path must have at least one viable, accessible mitigation/escape/prevention sequence within the actual spatial/time model, under declared knowledge assumptions. Normal effects can look similar, but must have a discoverable discriminator; do not outline the ghost in red.

**Proof:** Replay dangerous states with no prior warning and assert the unfair version is rejected by scenario/fairness tests; replay a parallel valid state where the player can inspect/brace/warn/evacuate before the hazard. Test reduced motion and alternate sensory channels. **Tradeoff:** stricter hazard authoring; preserves meaningful dread rather than arbitrary failure.

### B3 — BLOCKING KNOWLEDGE BOUNDARY: Director and Ghost cannot launder omniscience

**Sources:** GDD ``4.1–4.3; C04/C05; decision P-001 and D-002.

**Problem:** Ghost knowledge is explicitly limited to hauntable zones and observed facts. The Director is a distinct pacing policy, but its eligible input is only called “observable intensity state.” If Director can see a hidden player inventory, intended binding plan, or unobserved actor position and adjust a plan's eligibility or target, the Ghost indirectly responds to facts it could not perceive.

**Small counterexample:** Two source states have the same Ghost sensory history and Power/Rage. In A, player carries an undisclosed binding vessel; in B, they do not. The Director changes which Ghost plan is scheduled based on that hidden inventory. From the player's perspective the House has read their mind despite C04 never directly accessing inventory.

**Minimum contract:** The Ghost Strategist receives a defined **perception projection**, not a full world object. The Director receives public/observable pressure metrics and policy state; any privileged safety-veto input must be bounded to **fairness constraint**, not forwarded as strategy, target choice or inferred hidden-player intent. Director may reject/defer a legal Ghost proposal; may not create, retarget, enhance or reward it. Record eligibility reason codes without revealing future plans to the player.

**Proof:** Paired worlds with identical permitted observations but differing unobserved inventory/intention yield identical Ghost plan candidates under the same seeded inputs; any Director difference must be independently explained by a documented safety-only veto, not leaked as Ghost knowledge. **Tradeoff:** limits adaptive pacing, but its purpose is fairness—not a second antagonist with perfect information.

**Minimality alternative:** C05 need not initially be a separate AI module or persistent entity: implement as a pure deterministic eligibility/pacing policy over proposal metadata and recent events. Separate its **authority**, not necessarily its class or file.

### B4 — BLOCKING MODULARITY CONTRACT: capability existence does not establish an executable Production

**Sources:** GDD ``2, 7.1, 9.1–9.3; C09/C10; [Terminology “Production”](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/TERMINOLOGY.md#L7-L34).

**Problem:** `AdventureManifest` is said to compose `Production` and Art Pack, but the illustrative GDD `9.2 manifest lists only Play, Venue, Cast, Haunting, Dialogue and Rules. It lacks the actual **role → Actor**, **Play Cue capability → Venue mechanism**, **Stage/Set → Room**, and **semantic warning → Art Pack** bindings. `entry_scene: ballroom` is also ambiguous: under the vocabulary, a ballroom is a Room and a Play Scene is a dramatic unit. This is **an inconsistency in an illustrative proposal**, not a demonstrated runtime schema bug.

**Four minimal compatibility failures:**

1. **Ambiguous prop:** Play requests `suspended.fixture`; Venue offers two such fixtures. The capability tag exists, but there is no selected binding. A chandelier Cue operates the wrong one.
2. **Unbound Role:** Cast provides Mara, Play requires Dancer, but Production omits which Actor fulfills the Role. Dialogue selects an in-character line for an unassigned person.
3. **Absent spatial/sensory reach:** Haunting offers `release.restraint` on a physical target, but its authored hauntable zone cannot reach the selected Venue mechanism. A category match wrongly declares a runnable attack.
4. **Invisible critical tell:** An alternate Art Pack meets file/asset format requirements but supplies no usable interpretation of the pre-impact restraint cue in a selected Shot. Physics remains identical while the player's ability to understand the warning disappears.

**Minimum contract:** Split **capability declaration** from **explicit binding**. `Production` owns role-to-actor and required cue-to-mechanism binding under locality, cardinality and condition checks. The Haunting's sensory/action requirements must bind to reachable world entities or fail before play. A presentation compatibility mapping asserts coverage for required **semantic affordances and warning signals** in each intended Shot/sensory mode. Explicitly distinguish `entry_room` from optional initial `play_scene` rather than misusing “Scene.”

**Proof:** Four negative fixture manifests rejected with distinct actionable diagnostics; a compatible curated configuration accepted; second Play or Art Pack uses **the same core**. **Tradeoff:** Slightly more authoring metadata; much less deceptive swappability. Do not build universal arbitrary-pack permutation or a content editor now.

### I1 — IMPORTANT: independent incident outcomes and once-only accounting

**Sources:** GDD ``4.3–4.6, 7.2; C04/C11, P-003/P-008.

The root Ghost plan, physical effects, attributed outcome, reward and Rage transition need a single authoritative causal chain. “Pay once per incident” is insufficient until an incident's **root ID**, terminal status, declared goals and reward key are defined.

**Counterexample:** Ghost releases a restraint. Chandelier moves, actor panics, show Cue fails and injury occurs; downstream events appear to be three rewarded successes. The player then catches the actor and partially repairs the effect, raising Rage as “thwarted” while Ghost also receives the full success bonus. This might be valid under an explicitly declared goal model, but it must not be an accidental product of listeners separately awarding rewards.

**Recommendation:** The world emits physical events; a **single incident-resolver** maps them to declared goals and mutually specified reward/Rage dispositions, using stable causal identifiers and terminal resolution. Cost at commitment is idempotent; reward cannot recur from lingering Fear or repeated event processing. If partial success can pay both Power and Rage, require an explicit rule and cap; otherwise keep dispositions exclusive for the first slice.

**Binding race:** If a seal breaks in the same tick Power reaches zero, define which pre/postcondition controls `Contained` versus `Free`; no module may independently mark either before resolved world state. A Ghost at zero while **unbound** remains exhausted. A valid binding at zero cannot result in immortality-by-inactivity.

**Test:** duplicate commit, double evaluation, cascading ordinary damage and same-tick seal break; compare outcome ledger and authoritative event IDs. Avoid a full physics simulation to solve attribution.

### I2 — IMPORTANT: replay pins, numeric/order semantics and independent randomness

**Sources:** GDD ``4.5, 9.4; C00/C01/C11; P-002.

“Same seed” is not enough for replay if content under the same label changes, unstable collection order breaks ties, clocks are external, or dialogue variation consumes a shared random stream used later by Ghost decisions. Testable replay needs immutable content byte identities, explicit rules config, command ordering/IDs, fixed tick semantics, deterministic PRNG state/algorithm and canonical event serialization.

**Counterexample:** Add an unused dialogue bark that consumes one global PRNG draw. The next Ghost target changes under the same seed and player commands. Independent dialogue and Ghost modules were syntactically separated but **behaviorally coupled**.

**Recommendation:** Record exact Adventure/module revisions plus content digests, initial state, PRNG algorithm/state and ordered commands. Define whether distinct systems use independent derived random streams or a deterministic per-decision key; this choice may be deferred until a narrow counterexample exists, but “any module can draw from one global random object” must not be an unexamined contract. Specify numeric units and total tie-break order before cross-runtime compatibility is claimed.

**Proof:** Same exact pinned inputs reproduce logical event/state hashes in Node and browser; changes to a purely presentational option, unrelated dialogue content or renderer frame cadence do **not** perturb Ghost choices. RunRecord compatibility failure should name unsupported schema/content, never silently use current defaults.

### I3 — IMPORTANT: Observe/Inspect temporal semantics contradict pure-query language if left undefined

**Sources:** GDD `3.1, C03, Gameplay “heartbeat”.

C03 says observation does not directly mutate authoritative state, yet Inspect is one of the player's repeated **actions**, and the show clock keeps running during work. A pure read-only query may be free; an inspect operation that takes time, changes viewpoint, exposes a clue, or updates a player journal is not necessarily free and should not be modeled as an instantaneous omniscient query.

**Counterexample:** A player repeatedly inspects all mechanisms without advancing ticks, reveals enough facts to avert every scheduled hazard, then acts before any cue. Or Inspect advances hidden time in the browser while a headless run treats it as free, causing replay divergence.

**Recommendation:** Define (a) read-only snapshot/UI lookups, (b) spatial/time-consuming Inspect commands, (c) player-observation/knowledge results. Inspect must not secretly change machine integrity, but may advance simulation and update a scoped evidence journal. It cannot reveal a fact outside the reachable inspectable affordance. Record the tick at which new information became available.

**Proof:** Two identical states, one performing bounded Inspect and another not, differ only in permitted elapsed time, observation state and downstream legitimate consequences. No renderer-side disclosure before the required access step.

### I4 — IMPORTANT: Show, Actor and Fifth Bell have to complete without invisible puppetry

**Sources:** GDD ``6–7, `12 CP2–3; Gameplay outcome model; C06–C08.

A Beat may require a Role but the corresponding Actor might flee, be injured, lack knowledge or refuse. The Show Controller must not puppeteer an incapacitated actor, but it also must not wait forever without an authored failure path. “Fifth Bell” is a player emergency decision, not automatically the instantaneous evacuation of a physically unreachable cast.

**Recommendation:** Treat required Beat obligations as finite state machines with observable fulfilled, substituted, timed-out/canceled or failed outcomes. Actor availability and knowledge are scoped inputs; no Show script writes directly to Actor body or truth. A Fifth Bell request begins a **declared evacuation/cancellation process** with reachability and time cost; the resulting cast survival and show result remain separate. This need not become a bespoke evacuation minigame.

**Proof:** Remove or incapacitate the only Role at a required beat; Show completes a declared contingency/cancellation without deadlock or ghost knowledge injection. Trigger Fifth Bell under hazardous conditions and verify that its result reflects actual physically achieved evacuation, not a magical blanket safety effect.

### I5 — IMPORTANT: visual swapping preserves simulation traces, not necessarily player decisions

**Sources:** C10; GDD `10; Stage 1 “Legibility and art gates”; decision P-010.

Two Art Packs can produce **identical logical outcomes for identical command traces** while teaching the player different, perhaps misleading, things. Simulation determinism alone cannot certify fairness of an Art Pack.

**Recommendation:** Introduce a small **semantic signal/affordance contract**: game events carry authored observable warning IDs, timing and channel/scope requirements; each required shot/profile maps them to legible output (visual, audio, text or accessibility alternative). Do not require a Ghost-specific visual label; an intentional ambiguous effect can share a look with a legitimate Cue while retaining contextual discriminators. Asset overrides must preserve required information availability.

**Proof:** Same command trace in two visual variants produces identical logical events; paired player-visibility/accessibility inspection confirms essential signs are available at the declared time and scale. Reduced-motion cannot erase an exclusive lethal warning. **No visual/art trial was executed in this review.**

### I6 — IMPORTANT: initial demonstration scope is described three ways

**Sources:** GDD `11/CP0–CP1, Stage 1 candidate Rooms/Scenes, Roadmap Stages 2–3.

The GDD sketches an 8–12-minute vertical slice with three mechanisms and five Beats, the visual plan proposes three Rooms and three Play Scenes, while the roadmap's Stage 2 explicitly asks for **one Room and one mechanism** to prove Observe → Interpret → Intervene. These are not inherently incompatible—each addresses a different experiment—but “first playable” can wrongly pull all the systems into Stage 2.

**Recommendation:** Explicitly name distinct artifacts: (1) **headless state-transition proof** (Stage 0 follow-on; planned only), (2) **one-Room judgment toy** (Stage 2), (3) **The Last Waltz vertical slice** (later, bounded, with Play/Actor/Ghost/optional binding), (4) **Stage 1 art comparison**. Share vocabulary and semantic signal IDs, not a premature common implementation budget. Keep “three mechanisms/five Beats” an *illustrative vertical-slice hypothesis* until the small toy establishes fun.

**Proof:** Each artifact has a separate hypothesis, minimal content, exit criterion, and rejection path. A failed Stage 2 test can simplify/redirect later stages without touching a giant locked vertical slice.

### O1 — OPTIONAL: retain two **policies**, not necessarily two AI components

P-001's Ghost/Director distinction is a good authority boundary. But there is no evidence Stage 0 needs two independent long-lived agents, minds, planners or complex schedulers. Start with Ghost proposal scoring plus a small **pure eligibility/cooldown policy**. Split implementation modules only if tests show distinct ownership or real tuning needs. This preserves nonpunitive counterplay without introducing another intelligence.

### O2 — OPTIONAL: defer detailed psyche, tiers IV/V and extensibility knobs

No matched playtest yet shows Fear/Trust needs several continuous meters instead of small authored state/trait distinctions. The five-tier horror catalog, cross-Adventure per-Room style overrides and future multiplayer command authority are design directions, **not prerequisite systems** for the Stage 2 toy. Defer numeric balance and large content grids; build one meaningful actor refusal or trust-contingent line later if that actually matters.

## 3. Protected decisions: what should remain unchanged

- **Physical stagehand:** movement and local access cost time. No omnipotent remote management cursor.
- **Independent theater:** legitimate cues, ordinary errors and performer choices occur without Ghost sponsorship. A successful no-op is valid player expertise.
- **Single authoritative headless simulation:** PixiJS observes and translates controls; does not decide damage, ghost rewards, NPC truth or cue effects.
- **One Ghost, separable pacing constraint:** bounded senses; Power spent at commitment, Rage speeds regeneration but is not free damage.
- **Distinct Actor and Role:** local knowledge must govern dialogue and compliance; physically impossible scripts must fail explicitly.
- **Multidimensional outcomes:** show, cast, player and haunting may end differently; Fifth Bell is meaningful partial success.
- **Curated compatible Adventures:** a Play is not a Room, Production binds roles/props, Shots are presentation, Art Packs are visual. Do not promise universal combinatorial interchangeability.
- **Authored dialogue and silence, not runtime LLM improvisation**, with deterministic selection and knowledge bounds.
- **Stage 0 is design, Stage 1 is art comparison, Stage 2 is the minimum fun test.** No release schedule or automatic checkpoint promotion.

## 4. Recommended minimal experiment — the false-alarm chandelier

**Purpose:** Test the core player promise before the Ghost, Director, dialogue and modular loader gain complexity.

**Fixture:** one Room and one reachable restraint control; a performer optional for the very first toy; a visible cue-book entry; a safe rehearsed sway and one dangerous anomaly. One movable physically present player, one inspection route, one actionable intervention and one deliberately valid **refrain** option. Use the same command vocabulary (Move, Inspect, Operate) in both cases.

**Controlled versions:** (A) legitimate authorized sway with no Ghost; (B) unintended mechanical release (ordinary fault at first); (C) later, bounded Ghost-caused release that produces equivalent initial appearance but distinct discoverable provenance. Do not mark all anomalies with a “ghost” effect.

**Prior falsifiable predictions:**
1. The evidence available before irreversible outcome allows a sufficiently attentive player to discriminate at least two explanations without arbitrary guessing.
2. The correct action may differ between versions: tampering may warrant bracing; legitimate scheduled movement may warrant *no action*.
3. A false intervention has a real, proportionate cost to the show (not just a red score).
4. A correctly timed intervention visibly prevents its intended causal effect; no immediate artificial replacement threat appears.
5. Every outcome is derivable from state plus ordered commands; swapping visual assets with equivalent semantic cues changes no mechanical truth.
6. Difficulty can rise through tighter information/time constraints, **not** arbitrary invisible rules.

**Stage-appropriate acceptance:** Before claiming “fun,” run blinded human trials or small observation sessions using equivalent information, record player hypotheses and chosen actions, distinguish skill/learning from lucky guessing, and compare explanations to the actual causal oracle. Headless model checks can certify correctness and reachable alternatives; **they cannot certify subjective dread or enjoyment**.

**Minimal mechanical counterexample fixture:** Two worlds that differ only in whether a single suspicious chandelier movement belongs to the approved cue. Player has the same reachable inspection method and enough time to perform it. Assert that *inspect then choose* can avoid a costly false correction in A and prevent harm in B, while blind “repair everything” causes a performance disruption in A. If there is no discriminating observation, the trial is not a test of judgment—only a coin flip.

## 5. Acceptance and invariants matrix (proposed tests, not executed)

| Check | Exact negative case | Mechanical expectation |
| --- | --- | --- |
| AX-SF-01 **tick ownership** | Cue, player brace and ghost release target one prop at the same tick | One deterministic transition/event order; no direct cross-module competing writes |
| AX-SF-02 **warning/actionability** | Low-tier lethal restraint release with no earlier cue and zero response time | Scenario rejected/diagnosed as unfair; legal warning+intervention neighbor accepted |
| AX-SF-03 **epistemic noninterference** | Hidden vessel toggled with identical Ghost-perceived state | No change to strategist selection; fairness-only Director veto documented, not leaked |
| AX-SF-04 **curated bindings** | Two `suspended.fixture` providers but missing selected cue target | Loader rejects ambiguous Production rather than picking by array order |
| AX-SF-05 **role binding** | Actor exists but no Play Role assignment | Required dialogue and beat cannot run with arbitrary Actor |
| AX-SF-06 **sensing range** | Ghost target is physically/haunting-inaccessible despite capability tag | Illegal plan rejected without spending Power |
| AX-SF-07 **art signal coverage** | Art Pack omits sole pre-impact signal in critical Shot | Visual compatibility rejected or accessible equivalent mandated |
| AX-SF-08 **incident exactly once** | Same root Ghost action produces three downstream failures and repeated resolver invocation | Exactly allowed once-per-root rewards; ordinary causality never credited |
| AX-SF-09 **binding tie** | Power becomes zero on tick seal breaks | Exactly one valid resolved haunting state and documented precedence |
| AX-SF-10 **replay independence** | Unused dialogue/random draw or Pixi render FPS changes | Ghost plans and physical hashes stable for same pinned logical inputs |
| AX-SF-11 **inspect honesty** | Repeated inspect without tick advancement across impending cue | No free omniscient time stop or out-of-range evidence |
| AX-SF-12 **cast/show progress** | Required Role permanently absent while beat awaits performance | Declared fallback/cancellation/failure, never perpetual hidden script wait |
| AX-SF-13 **Fifth Bell reality** | Bell requested while cast remains trapped in unsafe Room | Show canceled if authorized; cast survival from actual resolved rescue/escape, not teleport |
| AX-SF-14 **false alarm** | Approved Cue mistaken for sabotage and “repaired” | Measurable performance consequence; valid no-op remains possible |
| AX-SF-15 **visual invariance** | Same input trace under Visual Profile A vs B | Identical authoritative events; perceptual accessibility independently reviewed |
| AX-SF-16 **module versioning** | Same `module@0.1.0` name with changed content bytes or unsupported schema | Replayer demands exact digest/support and fails clearly; no silent fallback |

**Versioning challenge — only because of a concrete failure:** The illustrative `GDD `9.2` manifest uses module strings such as `@0.1.0` and `schema: stagefright.adventure/0.1`, whereas replay promises identical outcomes from “version pins.” Labels without **immutable content digests** may be republished with changed dialogue or Power costs, breaking a recorded seed. For future design, keep separate (a) engine protocol/replay format version, (b) content schema compatibility, (c) authored module revision, (d) exact resolved content hash, and (e) project human ChangeID. Only the compatible minimum must be enacted once replay exists. Do not invent an omnibus versioning framework or freeze major/minor numbering in Stage 0.

## 6. Unresolved dissent, alternatives and uncertainty

**Dissent D1:** A separated Director is a *good rule-ownership distinction* but may be a needless subsystem for the first experiment. Require a counterexample that a simple pacing filter fails before investing in independent Director lifecycle/state.

**Dissent D2:** A tier taxonomy is not a fairness classification. Severe ordinary-energy accidents can be triggered cheaply; lethality must be evaluated at the world-hazard and information boundary. Preserve lethal threat only if it admits meaningful counterplay, not merely a warning in the log.

**Dissent D3:** “Two clocks” describes two kinds of progression but should not be read as two time authorities. The Play can branch and pause relative to the tick without creating a second clock that makes replays nondeterministic.

**Dissent D4:** C09's example is currently not a full playable Production manifest. This is acceptable as **illustrative documentation only**, but it must not be copied as an accepted loader schema.

**Dissent D5:** Headless event equality does not imply visual equivalence of what a player can know. A replay-pure Art Pack can still make the game unfair. Semantic warning coverage needs a separate perception/art acceptance gate.

**Uncertainty:** No gameplay exists at the reviewed commit. No human play sessions, player comprehension, ghost economic balance, dialogue quality, art readability, Pixi runtime performance, or exact cross-runtime deterministic simulator checks were executed or provided as evidence here. All changes recommended are **proposed design corrections**, not discovered implementation defects. I cannot quantify whether the full game is enjoyable yet.

**Explicit non-recommendations:** No engine implementation, no hierarchy of autonomous agent brains, no full hazard physics, no universal scenario model checker, no early Scene editor, no forced multilayer class split, no arbitrary content permutations and no runtime LLM dialogue. Avoid generalizing from one toy beyond what its tests establish.

## 7. Disposition for Mothlight / Studio Architect

**Verdict:** **ACCEPT WITH CHANGES** and preserve the creative direction.

**Before Stage 0 contract adoption:** Assign one authority to step ordering, explicitly bound Ghost/Director observations, define fair lethal preconditions, and require Production/capability/art-signal bindings. Document the minimum action/query and reward attribution semantics. These are short contract clarifications with 2–4 precise negative examples, not architectural implementation demands.

**Before Stage 1 art acceptance:** Require same-scene, same-mechanical-trace accessibility/legibility comparison across at least two visual treatments and normal-versus-haunted cues. No style is approved from descriptions alone.

**Before Stage 2 claiming a fun gameplay loop:** Verify the one-Room ambiguity experiment with actual people. Skillful nonintervention must sometimes beat reflexive repair, while well-timed intervention must change the world.

**Before the later vertical slice:** Verify Show/Actor non-deadlock, incident once-only accounting, binding tie cases and replay revision pins with independent headless negative tests.

**What would change my mind:** A narrow counterexample showing the proposed phase/ownership boundaries create more complexity than they prevent; a prototype demonstrating a more effective, simpler fairness model; evidence that the second “clock” or Director genuinely needs independent time/knowledge authority without violating replay or noninterference. Any adopted direction should carry a specific human decision and test, not reviewer-count consensus.

## Evidence

**Observed/source-backed:** At the mandated pinned source commit, all seven Stage 0 design inputs plus repository scope/architecture docs were read; source file blob SHAs are recorded above. These sources explicitly say the gameplay is not implemented. The handoff commit (different from the source pin) was read only for task rules. Axiom's own branch profile/common protocols were revalidated at `58a042f60a41cfa2be0ffd4afe29911e0354a9c2`. No other five agent reports were opened.

**Inferred/proposed:** All findings, severity labels, counterexamples, candidate interface repairs, negative cases and quality gates here. They are **design analysis** and have not been executed as failing tests or verified as production defects.

**Execution:** No target-repository code, schemas, assets, issue threads, PRs or other agent branches were changed. No headless implementation, Pixi screen, game runtime, CI or human playtest was run. Axiom's own indexed record is the intended sole durable publication for this first pass. The GitHub commit receipt and structural checks must be verified separately.

## Revisit when

Mothlight has preserved all six independent first passes and commissions a distinct synthesis; owner ratifies Stage 0 contracts; a Stage 2 one-Room experiment produces evidence; exact Stage Fright source/manifest contracts change; or a falsifier shows one of these proposed boundaries is unnecessary or wrong. Preserve this independent verdict and any subsequent dissent rather than rewriting it to match consensus.

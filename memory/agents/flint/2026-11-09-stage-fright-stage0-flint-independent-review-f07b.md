---
schema: 1
id: 2026-11-09-stage-fright-stage0-flint-independent-review-f07b
kind: lesson
scope: agent:flint
status: active
evidence: inferred
author: flint-stage-fright-independent-review-session
created: 2026-11-09
updated: 2026-11-09
sources: "Mothlight Stage Fright STAGE-FRIGHT-V0-REVIEW-01 handoff at 09164e820264b7502de58e87d0f31ab5f166592f; immutable design baseline 65f470e1c821fcf8c9be85fa0d58399587aabfdb; Flint home agents/flint-v1@e8d4d363f57118fba84a905b4fafddb928cd046d; inspected seven required design documents and architecture."
---

# Flint — independent Stage 0 review of Mothlight's Stage Fright

**Assignment:** `STAGE-FRIGHT-V0-REVIEW-01` (Flint — deliberate minimality).  
**Task outcome:** COMPLETE, independent **design review only**, authored in a Flint-selected ChatGPT context. **No other five reviewers' findings were read** before this submission. No implementation, runtime test, application code, original design revision, PR, or shared-game-repository publication was made. Authorship is a reviewer perspective on a shared GitHub account, not proof of a separately authenticated agent runtime.

## Summary

**Verdict: CONDITIONAL PASS for the Stage 0 *direction*, REQUEST CLARIFICATION of three gate-defining ambiguities before Stage 0 design acceptance.** The recognizable game is not a Ghost AI simulator, general-purpose theater engine, or procedurally assembled content showcase. It is the stagehand's repeated **Observe → Interpret → Intervene or deliberately refrain → Witness** choice while a live production advances. The player should sometimes recognize a harmless rehearsed effect and allow it, sometimes detect a real physical fault or sabotage and avert it, and sometimes make an understandable mistake. The smallest genuine fun test is a single bounded Room, one mechanism, one scheduled legitimate Cue and two *plausible, distinguishable* causes of suspicious behavior. If that is dull with ordinary effects and time pressure, postpone everything else; do not attempt to rescue it with five power tiers, dialogue volume, complex content manifests or visuals.

**Preserve:** physically present stagehand; production continuing independently; legitimate, accidental and hostile anomalies; world-owned consequences; headless replay and authored presentation; different acceptable outcomes. **Defer:** a separate Director executor, 5-tier powers, Fear/Trust dynamics, generalized dialogue engine, binding, full Adventure composition/loader, third-party packs, multiplayer, and elaborate art variants until a staged experiment specifically requires them.

The observations are about proposed documents, not implemented defects or measured fun. Below, **blocking** means a Stage 0 decision/evidence ambiguity that can undermine the *next* experimental gate, not a claim of existing faulty game code.

## 1. Pickup and exact sources

**Agent:** Flint — The Reducer, home `cosmicdance-4-2-0/KestrelGaming@agents/flint-v1`, inspected head `e8d4d363f57118fba84a905b4fafddb928cd046d`; own `agents/flint/AGENT.md` blob `b56d89557a84ddd9f3c234cc4c7ace0ffa6ee76c`. The user explicitly dispatched the Mothlight review link. Fetched handoff `docs/reviews/STAGE0_SIX_AGENT_HANDOFF.md` on game repo `09164e820264b7502de58e87d0f31ab5f166592f`, blob `3bdc0168da0e1a8e1d128820dd0eb4e3fd628ae3`. It explicitly pins **`65f470e1c821fcf8c9be85fa0d58399587aabfdb`** for review. All following game-source interpretations are from this earlier immutable commit, **not** latest main or the handoff commit.

Read the handoff's seven required design inputs in stated order, at the exact pinned commit:

| Document | Git blob |
| --- | --- |
| `docs/design/STAGE_FRIGHT_DESIGN_v0.1.md` | `26feee1402341b08eb2af8b09ed954a757874b10` |
| `docs/contracts/V0_PLANNED_CONTRACTS.md` | `f0e09572f6eae5701650241e1ab4ac93405ac7b2` |
| `docs/design/V0_GAMEPLAY.md` | `35dd5e67fa9f82e45eb3455cd711e4329ff109d3` |
| `docs/design/V0_DECISION_REGISTER.md` | `97b5e526c15fe258cceedb6f113f6f4433121ccc` |
| `docs/TERMINOLOGY.md` | `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c` |
| `docs/design/STAGE1_VISUAL_DIRECTION.md` | `03abd7d16981249a6879c3bc597e98a4d9758358` |
| `docs/ROADMAP.md` | `7ae90a7eac87ca123d9c578b99f33743d893ec1c` |

Also inspected `AGENTS.md` `d64f6b28a8c544610465c8801ba9964d1fbb82f0`, `README.md` `6b9760ab0c330355a877fe026e5b072ccb2e26cc`, and `docs/ARCHITECTURE.md` `6fa47db6b2965a8887934b86d183b86ea52f9d7e` at the pinned commit; the game remains a bootstrap with no implemented playable simulation. The separate `docs/reviews/STAGE0_REVIEW_INTAKE.md` did not resolve at that earlier pinned commit; it exists in the later handoff-commit tree but was **not** substituted into the immutable design input. No peer review reports were consulted. No full local checkout, Node tests, human playtest, browser visual test or model-behavior benchmark occurred here.

## 2. Most important promise, and smallest falsifier

**Established direction** (decision register D-001/D-003 and gameplay “heartbeat”): a stagehand with physical presence and limited time must diagnose anomalies while a Play advances; a rehearsed effect, mundane fault and ghost interference may look similar. A legitimate cue should sometimes be best left alone. Correct counterplay has earned, inspectable consequences.

**Empirical hypothesis, untested:** players enjoy making evidence-based distinctions under time pressure rather than simply interacting with every suspicious object.

**Minimum experiment — one Room, one scheduled cue, one mechanism, two plausible worlds:**

- The same initial visible symptom can arise in a **legitimate revised cue** or an **actual unsecured mechanism**. Each has at least one accessible, causally connected distinguishing clue **before** irreversible consequences. The player is not shown the hidden cause via a UI flag.
- Movement/inspection and intervention each consume intelligible simulation opportunity; the Play continues. Refraining is an explicit outcome, not an unavailable button.
- In the legitimate case, an unnecessary intervention disrupts the performance; informed restraint preserves it. In the fault case, appropriate intervention prevents a real consequence; refraining has a traceable cost. Both offer a genuinely feasible decision within the time and reach constraints.
- Observations are mechanical facts available to the stagehand—effective cue note, restraint position, timing, sound, actor warning—not an omniscient “ghost-caused = true” inspection field.
- A small rehearsal/cue indicator and one deterministic passive performer representation are enough initially. No NPC AI, supernatural planner, dialogue branch matrix or binding is needed to test this player choice.
- Use a **blind first-play control**, not only developer knowledge or repeat-seed mastery. Record available cues, player explanation before consequence, chosen action/nonaction, elapsed opportunity and actual outcome. A player must be able to say what evidence distinguished the worlds, not win by guessing an expected puzzle answer.

**Counterexample that falsifies the fantasy:** both states look identical and all legitimate observations are identical until after the intervention deadline; the correct choice is a coin toss. A second falsifier: `Inspect` gives the true hidden category instantly at no cost, reducing play to “inspect every anomaly and click the corrective action.”

A scripted single true answer without a legitimate alternate world does **not** test this promise. A third Ghost-caused case belongs after Stage 4, when bounded senses/economy can produce it honestly.

## 3. Ranked independent findings

### B1 — BLOCKING Stage 0 clarity: “first playable” is overloaded

**Sources:** Original GDD §11, lines 397–412; original §12 CP0–CP5, lines 414–447; `docs/ROADMAP.md` Stage 2/3/4/6; `docs/design/V0_DECISION_REGISTER.md` open calls 7 and 9.

GDD's “first playable Adventure”/target vertical slice promises approximately 8–12 minutes, three mechanism classes, five Beats, one Actor with Fear/Trust/Health and dialogue, a Ghost, and **both curtain-call and binding routes**. The staged roadmap rightly places *one mechanism and one suspicious deviation* in Stage 2, actor/Play capability in Stage 3, Ghost in Stage 4, and binding in Stage 6. These are compatible as future accomplishments, but using **first playable** for both permits the later feature list to become the acceptance criterion for the first fun experiment.

**Observable failure:** Stage 2 cannot be judged without a multi-system engine, or a dull one-mechanism test is never conducted because content production begins immediately.

**Minimum correction:** Name the first **mechanic proof** (Stage 2) separately from the eventual **integrated Adventure vertical slice** (after validated Stage 4–6 features). Keep the GDD candidate as deferred integration scope; do not implement or specify all of its components for Stage 2. Stage 0 exit includes a one-paragraph proof fixture and one explicit fail criterion.

### B2 — BLOCKING Stage 2 testability: observation/action cost and information ownership are underspecified

**Sources:** Original GDD §3.1, §3.3 and §4.7; `V0_GAMEPLAY.md` “heartbeat” and “two truths”; `V0_PLANNED_CONTRACTS.md` C01/C03; decision register inspection-interest experiment.

The rules protect observer uncertainty but do not specify the minimum *available evidence / player observation* seam. `Inspect` is nominally observational and not an authoritative write; that does not determine whether it costs time, whether hidden causal origin is disclosed, whether it can be performed from impossible distance, or what happens when the cue deadline passes during it.

**Observable failure:** free universal inspection removes meaningful uncertainty, or withheld distinctions make correct judgment arbitrary. A technically correct headless state machine could produce both failures.

**Minimum correction:** In Stage 0 state the testable contract: player observations derive from physical access, perceptible cues and local world history; an Inspect result reports *what is observable*, not hidden cause; command resolution charges physical/time opportunity; nonaction advances the clock; both justified act/refrain decisions are reachable in their respective fixture. Leave exact numbers, menus and controller mappings open.

### B3 — BLOCKING future core integration: “two clocks” lacks one tick authority and a defined same-tick decision order

**Sources:** Original GDD §4.5, §7.3; `V0_PLANNED_CONTRACTS.md` C00/C01/C07; `V0_GAMEPLAY.md` Ghost opposing loop; `docs/ARCHITECTURE.md` core boundary.

GDD correctly names **performance** and **simulation** clocks but C00 says exactly one authoritative fixed-step simulation. Two independently advanced clocks would make cue/action races and replay ambiguous. GDD §4.5 orders world/show advance, new ghost sensing, plan commitment and warning/execution within one cycle, but does not say whether a newly perceived action may trigger an instant, unreactable threat in that same tick.

**Observable failure:** a stagehand operates a latch at the exact tick of a scheduled Cue; different host/update order decides success. Or the Ghost commits and resolves an attack in the same step without a reachable warning interval.

**Minimum correction:** One source-of-truth simulation tick. The performance clock is a derived **beat/schedule state**, not a second wall-clock scheduler. Specify deterministic phase order for queued player/actor/cue/ghost commands, world effects, observation propagation, ghost planning, commitment, warning and delayed consequence; define same-tick collision precedence. No new scheduler framework. Lock this before Stage 2 engine implementation; Stage 0 needs at least a precedence table and counterexample.

### I1 — IMPORTANT: Ghost and Director are separate *policies*, not necessarily separate engines

**Sources:** Original GDD §4.1–4.5; `V0_PLANNED_CONTRACTS.md` C04/C05; decision register P-001/open call 1.

The proposed separation is defensible because hostile preference and fairness constraints must not have the same authority. **But a second stateful Director controller is not yet justified.** Initially express pacing as a pure eligibility predicate on proposed Ghost actions: given current window, recent incidents and configured minimum telegraph/recovery, return allowed or withheld plus an inspectable reason. The Ghost still owns Power and strategic choice; the world owns consequences. Add independent Director state later only if a falsifying case requires history that cannot live in existing state.

**Failure:** Director manufactures replacement attacks after clever counterplay, or duplicated attack-state owners disagree about what was thwarted.

**Tradeoff:** A pure gate cannot by itself drive sophisticated dramatic arcs. That is acceptable until a human test demonstrates the need for autonomous pacing decisions. Do not reject the eventual two-policy *concept*, just the unearned extra runtime.

### I2 — IMPORTANT: Ghost Power/Rage tiers add tuning burden before they create tested choices

**Sources:** Original GDD §4.3–4.4; `V0_PLANNED_CONTRACTS.md` C04/C05; decision register P-003; roadmap Stage 4.

The five tiers and provisional numeric pricing are *proposals*, not balance proof. For Stage 4 begin with **one costed physical interference** and one visible, preventable setup. Test spend-on-commit, replay attribution, and no replacement free attack. Then add a mechanically distinct action if it forces a new player decision. Rage need not be implemented until resource exhaustion and thwart recovery produce an actual pacing/incentive problem.

**Failure:** five action tiers differ mainly in spectacle/cost and produce identical choices, while their combinatorial legality/telegraph/reward testing dominates development.

**Tradeoff:** Early ghost encounters will be less varied; that is useful when verifying their fairness and observability.

### I3 — IMPORTANT: Fairness must be tested against actual player reach and cues, not just an internal telegraph flag

**Sources:** Original GDD §4.4, §4.7 and §10; `V0_PLANNED_CONTRACTS.md` C04/C10; Stage 1 visual legibility requirements.

Tier II interference may produce lethal consequences via stored mechanical energy. That can be a good world-driven hazard, but a generic `warning: true` field or authored signal is insufficient if the fixed Shot hides it, player travel takes longer than the reaction window, or warnings share no accessible modality.

**Minimum correction:** For any future lethal incident, require an evidence trace of **earliest observable warning**, **player-available action/route**, and **time to effective mitigation** under the actual Shot, movement constraints and input accessibility mode. If none exists, deny that attack opportunity; otherwise the Director must not pretend that obeying an abstract warning rule was fair. This is an invariant, not a new horror-meter subsystem.

### I4 — IMPORTANT: Play and Actor ownership needs one cue-resolution handshake

**Sources:** Original GDD §6.2–6.4, §7.1–7.3 and §8.2–8.4; contracts C06–C08; `V0_GAMEPLAY.md` five authored reactions.

An Actor cannot complete an impossible cue, and a Show Controller cannot secretly force an incapacitated Role to perform. The spec says so, but the cross-boundary transition is underspecified: who marks a Cue attempted, failed, covered, canceled, or complete, and when does a fallback Beat become operative?

**Minimum correction:** The Play/Show Controller owns cue/beat status and accepts **world-resolved outcome events**, not arbitrary actor success claims. The Actor owns its own intended action and knowledge-limited response. World resolves mechanism and incapacity constraints; Show advances/branches on those events. Define a short finite transition example and one impossibility test; avoid building general-purpose dialogue/NPC policy frameworks for the initial Stage 3 experiment.

**Failure:** injured Actor delivers a Beat because the script demanded it; fallback speech is selected from facts the Actor never observed; two modules independently mark cue success.

### I5 — IMPORTANT: Proposed “modules” are responsibilities, not independent workspaces or swappable plugins yet

**Sources:** Original GDD §9.1–9.3; contracts C02/C06/C07/C09/C10; decision register D-006; roadmap Stage 7.

The original lists nine internal modules and roughly thirteen planned contracts. That is an acceptable **ownership inventory**, but Stage 2 should not build that package topology or a generalized plug-in loader. Keep a single headless simulation boundary with direct, explicit Play/world state and a separate presentation adapter. Split `ghost-ai`, `show-engine`, `npc-ai`, `dialogue-engine`, `world-physics` into separate modules **when a second implementation or independently exercised seam proves the separation useful**.

A curated Adventure can initially pin one coherent Play/Venue/Cast/Haunting bundle. Validate the *capability mapping* needed for the concrete fixture, rather than designing every third-party content schema. At Stage 7 require a genuinely different valid content combination without rewriting core mechanics, plus an incompatible one that fails with a precise error.

**Failure:** a new Play still needs edits inside the Ghost or renderer despite passing a manifest checklist, or the first slice takes longer to implement because it is spread across speculative services. The principle “one source owner per state” is kept, even if physical files remain few.

### I6 — IMPORTANT: Cosmetic invariance and information equivalence are different tests

**Sources:** `V0_PLANNED_CONTRACTS.md` C09/C10; `V0_GAMEPLAY.md` Stage 0 Art Pack example; `STAGE1_VISUAL_DIRECTION.md` legibility gates; decision register Art Pack trial.

A fixed **command trace** with the same initial game state must have the same authoritative outcome under two Visual Profiles. That does **not** imply two human players will take identical actions under two styles. If one Art Pack hides a restraint warning, the game may be mechanically deterministic but experientially unfair.

**Minimum correction:** Separate (a) **simulation invariance** under a fixed trace/seed from (b) **visual information sufficiency** under each style at target viewing conditions, including accessible alternate cues. Art swaps can change perception and therefore future player commands, but must not change underlying physics, ghost knowledge or legality.

### I7 — IMPORTANT: Dialogue and personality should be sampled through authored intent, not a matrix

**Sources:** Original GDD §6 and §8; `V0_GAMEPLAY.md` Cast reactions; roadmap Stage 3.

The proposed knowledge-limited authored dialogue is sound. Avoid building all four dialogue channels, localization/audio systems, personality traits, cooldowns, relationship simulation, and extensive emergency contingencies before hearing one strong normal line and one contextually justified alternate. A small finite actor state (can act, knows X, has reason to continue/refuse) is enough to test one authored cover line and silence/interruption; numeric Fear/Trust can arrive when the story shows a distinct decision requiring both.

**Failure:** lines become a combinatorial authored burden or generic fallbacks repeatedly make characters seem indifferent to what happened.

**Tradeoff:** Early actors are simpler than their eventual personas; this allows authoring quality and causal coherence to be tested before multiplicative complexity.

## 4. Recommended first-playable experiment and acceptance evidence

**Call it Stage 2 “single-mechanism judgment proof,” not a complete Adventure or integrated ghost demo.**

**Configuration (design only):** one bounded stage/wing Room, one rigging restraint with safe and unsafe states, one scheduled mechanical Cue and visible performance progress, player move/inspect/operate/refrain, one authored ordinary rehearsal revision and one ordinary physical fault. A passive actor cue/line may be used to communicate that there is a show, without actor AI. Both cases present a similar suspicious early movement; available *specific evidence* differs. No Ghost, Director, Power, Rage, Fear/Trust system, binding, dialogue engine, many-Room navigation, content loader or Art Pack system is needed.

**What it proves:** whether players can distinguish causes from observations under finite time, experience meaningful consequences from restraint or intervention, and explain the result without hidden designer trivia.

**Must-pass headless fixtures (future tests, NOT RUN):**
1. Same seed/initial snapshot + exact ordered commands => identical cue status, world events, outcomes and hashes in supported runtimes; no render-frame dependence.
2. Legal revised-Cue case: refraining preserves a promised dramatic Beat, while unjustified disablement makes a measurable, explainable mistake.
3. Actual fault case: inspecting and correctly operating can avert the stateful failure; an unchecked fault has a different world consequence, with warning and feasible timing.
4. `Inspect` returns only accessible observations; remote/omniscient queries and invalid operations cannot reveal hidden cause or mutate mechanics.
5. Cue and player operate on same tick: deterministic, documented precedence with no double execution.
6. Never “fix” one successfully averted hazard by inventing a substitute threat; no AI required to evaluate this principle.

**Human-playtest evidence (future, no fabricated metric):** blind first-time participants can state an evidence-backed explanation of why they acted or refrained, distinguish cue book from physical state, and understand the consequence after the fact. Record false positives, missed clues, indiscriminate inspections, unnecessary intervention and perceived fairness, with the observation transcript available for audit. Reject a fixture where key clues are inaccessible; don't “tune” it to reward random guessing. Determine explicit sample size and thresholds when authorizing Stage 2, not in Stage 0.

**Abandonment condition:** If, after one controlled accessibility/readability correction, informed players still default to inspect-all/click-all or outcomes feel arbitrary, revise the fundamental observation/interaction contract before implementing Ghost intelligence or additional content. The correct response to an unfun core is not a larger ghost.

## 5. Explicit non-goals by checkpoint

**Stage 0:** do not implement game logic, art, entity schemas, or a JSON Adventure plugin spec. Record only ownership, deliberate scope, counterexamples and proposed gates.

**Stage 1:** choose readable art direction and Shot geometry; no full Art Pack ecosystem, shaders as gameplay authority, animation pipeline or alternate styled Adventure.

**Stage 2:** no Ghost, Director, Rage, five-tier power hierarchy, cast psychology, generated dialogue, binding, online networking, external authoring, generalized physics, or cross-Adventure capability engine. The player/tester needs only a stateful causal choice.

**Stage 3:** one Actor/Role and contingent Beat: no deep cast relationship graph, generalized procedural script or comprehensive localization/voice pipeline.

**Stage 4:** one illegal-to-cheat costed Ghost action, ghost sensory boundary and causal economy; Director initially a pure eligibility gate. Add a second distinct action only on demonstrated new decision value.

**Later:** binding/escape, emergent cast relationships, full content modularity, third-party asset validation and multiplayer only against their explicit stage hypotheses. The existing Stage 6/7 headings remain useful as research goals, not preconditions for Stage 2.

## 6. Status distinctions and unresolved uncertainty

- **Established direction:** physically embodied stagehand, an independently progressing Play, real harmless and hostile events, multiple outcomes, headless rules and non-authoritative PixiJS, modular Adventures eventually, artistic variation per Adventure (decision register D-001–D-009). The user approved a *direction*, not any schema or price table.
- **Proposed design:** Ghost/Director split, five actions tiers, Power/Rage values and regeneration, actor state dimensions, authored dialogue selector, optional binding drain, the nine listed conceptual modules, capability manifest and visual profile precedence. No implementation acceptance implied.
- **Empirical hypothesis:** the one-Room interpretation loop is enjoyable; Ghost strategies feel fair; actors feel motivated rather than scripted; multiple art approaches retain legibility; binding is worth its authoring cost. No measured results exist in reviewed source.
- **Blocking Stage 0 clarifications:** B1 two different definitions of first playable; B2 player-observation/time seam; B3 one tick authority and same-tick transition semantics. These do not block further *design exploration*, but should be made unambiguous before authorizing the relevant runtime test.
- **Speculative options:** additional NPC personality metrics, universal art authoring, five supernatural tiers, full Story/Dialogue engines, future multiplayer and third-party executable scripting. Retain as future candidates, not invisible obligations.

**Explicit dissent:** I would prefer postponing the separate Director *runtime* entirely and not creating nine packages from the GDD module inventory. If Mothlight values early high-fidelity storytelling enough to accept more content burden, that is an owner/design choice—but then Stage 2's stated falsifiability must remain independent. I would change my mind if a one-policy Ghost demonstrably creates unfair compensatory attacks and an isolated pacing policy blocks them without duplicate state, or if real second-Adventure authoring demonstrates that earlier package splitting lowers total modification cost.

**Unknowns:** There is no executed player evidence about whether mechanical diagnosis is compelling, no measured inspection/cue time budget, no target accessibility-control acceptance, no tuned Ghost incentive evidence and no second Adventure proving swappability. Do not infer quality from a green bootstrap CI run.

## 7. What must remain unchanged

Keep the live Play and the player's embodied presence as causal design center, the honest possibility that suspicious events are not hostile, physically mediated consequences, cast knowledge limits, genuinely separate show/survival/binding outcomes, Fifth Bell as an intentional responsible cancellation, single headless simulation authority, deterministic replay and independent renderer. Do not merge Scene with Room/Shot, Actor with Role, or Art Pack appearance with authoritative world data. Future interoperability warrants retaining those semantic distinctions in the spec even if the first implementation has only one example each.

**Best single change to the documentation:** insert a one-page **Stage 2 judgment-proof contract** with exactly the two discriminable causes, observation/reach/time constraints, available player verbs, causal outcomes, and abandon/continue gate. Explicitly label GDD §11's elaborate `The Last Waltz` as a **later integrated vertical-slice candidate**. Resist specifying all fourteen planned contracts to implement this one-page proof.

## Evidence

Read GitHub source files at exact pinned commits, the game repo's bootstrap instructions/architecture, and Flint's own authored profile/index. Verified the handoff pin differs from the handoff document's own commit, and based the seven-document review on the mandated earlier commit. This is a static independent document consistency/minimality audit. The proposed counterexamples, headless checks and human trials above were **not run**; no gameplay engine, Ghost AI, NPC behavior or playable build was claimed. No other Stage 0 agents' review records were consulted. This is one loaded character perspective using the account's GitHub connection, not a separately authenticated autonomous agent.

## Revisit when

Mothlight reconciles the six independent Stage 0 reviews, the owner clarifies which “first playable” gate is intended, or a Stage 2 prototype provides actual player investigation/choice data. Re-pin game documentation on any subsequent review and report what changed before revising this verdict. Preserve this first-pass review intact for attribution; the Studio integrates conclusions, not author identities.

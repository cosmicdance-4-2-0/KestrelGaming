---
schema: 1
id: 2026-11-09-kite-stage-fright-stage0-independent-review-r7h2
kind: decision
scope: agent:kite
status: draft
evidence: inferred
author: kite-session
created: 2026-11-09
updated: 2026-11-09
sources: "Mothlight Stage 0 six-agent handoff at cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT@09164e820264b7502de58e87d0f31ab5f166592f (handoff blob 3bdc0168da0e1a8e1d128820dd0eb4e3fd628ae3); seven authoritative design docs at immutable game commit 65f470e1c821fcf8c9be85fa0d58399587aabfdb; Kite home agents/kite-v1@0442df0a1a50d2b1ca8d70d410d90e1b7e05cbae."
---

# Kite — Stage Fright independent Stage 0 design audit

**Assignment:** STAGE-FRIGHT-V0-REVIEW-01 (Kite experiment/falsification perspective).
**Source pin:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT@65f470e1c821fcf8c9be85fa0d58399587aabfdb`; handoff file separately at `09164e820264b7502de58e87d0f31ab5f166592f`.
**Agent:** Kite — The Unlicensed Inventor; home `cosmicdance-4-2-0/KestrelGaming@0442df0a1a50d2b1ca8d70d410d90e1b7e05cbae` on `agents/kite-v1`.
**Review mode:** independent, design-only, no other first-pass reviewer reports read, no gameplay implementation or human playtest executed.

## Summary

**Independent verdict: ACCEPT DIRECTION WITH CHANGES BEFORE STAGE 2 TRIALS.** The crucial promise is a physically situated stagehand's *evidence-based intervention*: recognize a normal/approved cue, ordinary equipment fault, or supernatural sabotage under a running Play clock, then decide whether and how to intervene. Distinguishing cause from appearance is both the main source of fun and the cheapest way to disprove the game concept. Two **blocking design ambiguities for eventual experiments** are (1) what sufficient, reachable, time-bounded evidence means for a fair ambiguous anomaly and (2) what a defensible counterplay window means for a low-tier but potentially lethal Ghost action. Neither requires implementing advanced systems now. Favor one Room, one mechanism, a legitimate cue, and a harmless or ordinary deviation **before** the larger five-beat, multi-mechanism slice.

The documents mostly distinguish declared direction from unverified mechanisms. These findings are design risks and proposed falsifiers, **not** executed defects or claims of poor player experience.

## Evidence receipt

Inspected in the handoff's exact order, all on `65f470e1c821fcf8c9be85fa0d58399587aabfdb`:

1. `docs/design/STAGE_FRIGHT_DESIGN_v0.1.md` (blob `26feee1402341b08eb2af8b09ed954a757874b10`; especially ``3–4, 6–8, 10–14).
2. `docs/contracts/V0_PLANNED_CONTRACTS.md` (blob `f0e09572f6eae5701650241e1ab4ac93405ac7b2`; especially `C03–C10 and C04–C05).
3. `docs/design/V0_GAMEPLAY.md` (blob `35dd5e67fa9f82e45eb3455cd711e4329ff109d3`; ``The heartbeat, The two truths, Stage 0 acceptance examples).
4. `docs/design/V0_DECISION_REGISTER.md` (blob `97b5e526c15fe258cceedb6f113f6f4433121ccc`; `D-001–D-009, P-001–P-010, Trial matrix).
5. `docs/TERMINOLOGY.md` (blob `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c`; `Three kinds of structure).
6. `docs/design/STAGE1_VISUAL_DIRECTION.md` (blob `03abd7d16981249a6879c3bc597e98a4d9758358`; `Candidates to compare, Legibility and art gates).
7. `docs/ROADMAP.md` (blob `7ae90a7eac87ca123d9c578b99f33743d893ec1c`; ``Stage 1–4 and Stage 8).

Also consulted pinned project's root `AGENTS.md` and `README.md` on handoff revision `09164e820264b7502de58e87d0f31ab5f166592f`, solely for status/scope. The later handoff is an invitation, **not** evidence that another review was completed. A separate `docs/reviews/STAGE0_REVIEW_INTAKE.md` was unavailable at authoritative source pin, and was not reconstructed. Did not read other reviewer proposals, code behavior, active PRs, or a floating `main`.

## Ranked findings

### F1 — BLOCKING EXPERIMENTAL GATE: The false alarm needs discriminating evidence, not designer hindsight

**Sources:** original GDD `3.1 and `7.1; gameplay ``The heartbeat and The two truths; decision register ``D-003, Trial matrix, Open calls 9.

The documents correctly require mundane or approved cues that resemble haunting. But `cue book is evidence, not oracle` and `legitimate revision` need an operational fairness rule: the player must have a *reachable* way, perhaps costly, to distinguish relevant possible causes **before** the consequential decision. It need not disclose the answer outright. If an unannounced authorized change is observationally identical to sabotage through every allowed interaction, a false-positive correction is an arbitrary gotcha, not expert judgment.

**Minimum contract proposal:** for an ambiguity intended to test judgment, author at least one accessible *discriminator* (inspection state, time-stamped revision, mechanism condition, credible eyewitness, audible pattern); specify when it becomes available, required traversal/inspection time, reliability and limits. Preserve unresolved cases explicitly as genuine uncertainty with acceptable cautious choices. Do not introduce a new global truth-revealing `Inspect` command.

**Observable failure:** players cannot beat chance on causal classification even with appropriate inspections; or always acting/always inspecting dominates choices. **Tradeoff:** too much evidence eliminates suspense; constrain evidence by opportunity cost and presentation rather than hiding all possible distinctions.

### F2 — BLOCKING EXPERIMENTAL GATE: Fair lethal attack is a reachability property

**Sources:** original GDD `4.4 (low-tier attacks may release lethal stored energy), `4.7 (fairness), `10 (camera); planned contracts `C04–C05, `C10`; visual direction `Legibility and art gates`.

An action can obey all Ghost costs and warning metadata yet be functionally unavoidable: the only warning is offscreen, the stagehand is too far from a usable control, or a camera/audio/accessibility treatment removes the necessary clue. Tier is explicitly not damage, so Tier II needs the same fairness proof as any potentially lethal consequence.

**Proposed authorable fairness envelope:** for each consequential hazard and eligible player state, record at least one reachable warning route and one possible mitigation/escape route. Compare *available lead time* with perception, decision, traversal, interaction and response times in the actual Room/Shot, accounting for supported alternate cue channels. Don't bake in a universal reaction-time constant; measure and calibrate later. An unexpectedly lethal situation may be acceptable if earlier player choices observably created it, but its causal responsibility must be explicit.

**Observable failure:** a deterministic baseline demonstrates death despite a correctly interpreted, timely response with supported controls, or an essential warning is unavailable in a legitimate active Shot/mode. **Tradeoff:** enforcing guaranteed safe outcomes would eliminate risk. Demand *possible, intelligible counterplay*, not automatic success.

### F3 — IMPORTANT: Ghost/Director scheduling boundary is still temporally ambiguous

**Sources:** original GDD `4.1 and `4.5; contracts `C04–C05`; decision register `P-001`.

The Director may withhold or adjust a legal Ghost plan, while Ghost Power is charged at **commit** and warnings follow commitment. Which actor may postpone or cancel between planned and committed states? If the Director reschedules a charged attack without new commitment or fabricates a replacement, a thwarted plan is not actually thwarted.

**Small correction:** explicitly distinguish `candidate -> pacing eligibility -> committed (cost paid) -> warned -> effect -> resolved`. The Director gates *eligibility before commitment* and does not edit the outcome of a committed incident. If any post-commit cancellation is ever allowed, the rules must define cost, warning and attribution; easiest first proof is to prohibit it. Try a single pacing eligibility predicate before engineering a second sophisticated policy.

**Observable failure:** no-cost replacement, duplicated warning, phantom refund, or reordered event invalidating what the player prevented. **Tradeoff:** less dynamic pacing initially; much simpler invariant and test.

### F4 — IMPORTANT: Initial proof scope differs across documents; prefer the smaller falsifier

**Sources:** original GDD `11 (8–12 minute, three mechanisms, five beats, narrow Ghost, possible binding) and `12 CP0–CP3; roadmap `Stage 2 (one Room, one mechanism, one legitimate cue and one suspicious deviation).

This is not necessarily a contradiction: one is a vertical-slice target and the other a research gate. But readers could confuse a large first playable with the prerequisite to demonstrate fun.

**Recommendation:** declare the roadmap Stage 2 experiment the **earliest gameplay falsifier** and GDD `11 a later integrated slice candidate. Do not implement a full Ghost, binding, three-mechanism plant or extensive actor simulation merely to discover that inspecting one prop is boring.

**Observable failure:** the experiment's completion depends on new feature classes that do not affect the primary act/refrain decision. **Tradeoff:** a reduced proof will not establish long-run horror or show continuity; test those separately.

### F5 — IMPORTANT: Authored improvisation may pass legality tests and still sound canned

**Sources:** original GDD `8.1–8.4; planned contracts `C06–C08`; gameplay `Cast and dialogue`; decision register `P-007`.

Context-eligible lines with deterministic tie-break and knowledge filters are sound engineering, but correctness of knowledge does not imply dramatic credibility. A single attractive sample line can conceal repetitive, tone-deaf or mechanically predictable variants after many reruns. The Scene graph can also require unavailable dialogue if an interruption is accepted but no safe fallback can resolve its Beat.

**Recommendation:** compare *same Beat* with a minimal fixed fallback versus an intent-keyed authored variant set. Audit two independent axes: causal fidelity and human-rated plausibility/variety. Treat silence and abandonment as legitimate choices. Prefer a small number of `dramatic intent` tags and explicit fallback/Beat outcomes over expanding state permutations.

**Observable failure:** hallucinated actor knowledge; incorrect continuation after injury/absence; or repeated delivery judged less coherent than plain fallback. **Tradeoff:** more authored branches improve expression but increase writing/localization cost, so record authoring minutes per accepted additional outcome.

### F6 — IMPORTANT: Visual independence requires two different tests, not one

**Sources:** planned contracts `C09–C10`; visual direction ``Candidates, Visual Profile and Art Pack modularity, Legibility`; decision register `P-010`.

`Same game, different Art Pack` has two meanings. **Mechanical invariance**: with the same commands, seed and rules, the authoritative event trace is identical. **Perceptual validity**: human players can actually find the same relevant hazards/interactables and make informed choices across styles. A pixel-on-painted-plate alternative may satisfy the first and fail the second. Conversely, styles should change *player choices and feeling* because presentation matters; therefore don't require identical human decisions.

**Recommendation:** compare full-pixel A with painted-plate B using the *same Room/Shot, cue timing, semantic signals and scripted command trace*, then separately measure human detection and perceived tension at actual play size. Compare accessibility variants and screen-size scaling, not only large concept illustrations.

**Observable failure:** a style obscures a hazard, props appear noninteractive, or alternate warning channels disappear although the core trace remains correct. **Tradeoff:** extra art prototyping before style selection; prevents costly style lock-in. The choice remains provisional until the Stage 2 loop establishes the needed visual affordances.

### F7 — OPTIONAL LATER: Capability contracts must describe behavior, not only asset names

**Sources:** original GDD `9.2–9.3; planned contracts `C09`; roadmap `Stage 7`.

A generic `suspended.fixture` might satisfy loader compatibility yet fail a Play's actual need for a safely lockable, inspectable, controllable fixture with a particular cue and warning. Test one deliberately incompatible alternative Venue/Play pairing later. Do **not** build a general workshop, inheritance engine or comprehensive semantic ontology at Stage 0. A small concrete capability with required operations and observable preconditions is enough for the first module-swapping trial.

## Four discriminating trials (DESIGN ONLY; none executed)

### T1 — Mundane false alarm: Does restraint improve outcomes?

**Claim:** Players enjoy interpreting an anomaly, not clicking suspect objects. **Earliest experiment**, precedes Ghost and complex cast.

- **Set-up:** one Room, stagehand, one visible mechanism, one scripted Cue and an advancing show timer. Prepare paired *authored hypothetical conditions*: legitimate authorized variation versus ordinary malfunction. A later extension adds supernatural interference with the same initial perceptual symptom. Each condition has a distinct, reachable discriminator, not a color-coded answer.
- **Controls:** identical navigation, control vocabulary, cue baseline, accessible information budget, initial affordances, and consequential decision window; randomize condition order and ensure no version always uses the same cue shape. Include a case where **refraining** is optimal and a case where an intervention is justified.
- **Observe:** whether and when the player inspects; source of their interpretation; justified refrain versus unjustified repair; time diverted; valid cue/operation outcomes; post-trial causal explanation and confidence. Log observations made, not only final button presses.
- **Falsifier / failure:** action-first or click-everything policies perform as well as reasoned investigation; knowledgeable players lack an available discriminator; false alarms always impose inconsequential choices; repeated trials reward learning a visual tell unrelated to the policy. Success evidence is an observed *decision difference* linked to a meaningful clue, supported by pre-registered comparisons against trivial strategies—not an unearned percentage or one anecdote.
- **Confounds:** player familiarity with theater cues, order/learning, undisclosed authorized revisions, reaction/reading speed, audiovisual modality, and evaluator coaching.
- **Cheaper alternative:** paper/prose tabletop interaction transcript with deliberate clock/cue choices before building a room renderer. It can test causal comprehension, not navigation or atmosphere.

### T2 — Fair Ghost attack: Can informed play defeat a legal threat?

**Claim:** A capable bounded antagonist can be terrifying without cheating.

- **Set-up:** same physical mechanism and danger volume; compare a legal Ghost action with a matched non-Ghost mechanical malfunction, plus a ghost-free baseline. For the first test, use a narrowly defined Tier II interference affecting a stored-energy mechanism, not a Tier V crisis. Both threat versions require explainable physical consequences.
- **Controls:** same initial Room/player positions, target integrity/load and cue state; fixed seed/ordered commands; declared warning route, start/commit/effect ticks; alternate cue channel. Vary *one* element per paired trace: causal origin, permitted warning lead, or player response, while holding other factors fixed.
- **Observe:** Ghost knowledge provenance, legal target, paid Power, warning availability, response/travel/interact window, outcome, Rage/reward attribution, Director eligibility, and whether successful counterplay persists. For human sessions, record whether danger was perceived and whether failure felt causally earned, distinguishing this from damage avoidance.
- **Falsifier / failure:** Ghost targets unseen private player knowledge; attack commits for no cost; legal and timely defense is ineffective without an earlier attributable mistake; an offscreen or unavailable warning is the only cue; Director replaces a thwarted hit free of charge; no feasible counterplay from an eligible launch state. PASS requires a reproducible fair path, not no deaths.
- **Confounds:** prior scenario learning, camera-specific sightline, accessibility mode, tester reaction times, input latency, cue salience, and stored-energy severity masquerading as Ghost tier.
- **Cheaper alternative:** headless discrete-event timeline enumeration first; human timing trial only when movement/camera inputs exist.

### T3 — Authored improvisation: Does it feel like performance, not state branching?

**Claim:** Context-selected lines preserve dramatic intent when machinery or actors diverge from rehearsal.

- **Set-up:** one Actor, one Role, one short Beat, one rehearsed line, a minimal set of intent-tagged alternatives and an intentional-silence/failure fallback. Compare rehearsed success, authorized late cue, observed mechanical threat, and unseen threat. Include an injured or departed actor who cannot deliver the line.
- **Controls:** same dramatic intent and performer profile; change only observed facts or ability in the semantic test. Compare plain static fallback against proposed context selection in blind presentation samples; match number of authored choices and separate voice acting from wording.
- **Observe:** selected stable line IDs, actor-local evidence at selection, Beat completion/cancellation state, audience comprehension of the event, blind ratings of plausibility and repetition across randomized runs, number of lines authored/localized, and production time.
- **Falsifier / failure:** a line asserts an unknown cause; an incapacitated actor speaks; a required Beat advances despite absent performer with no authorized contingency; variants sound more jarring or repetitive than the simple fallback. PASS on correctness alone does **not** prove entertaining dialogue; keep behavioral and dramatic assessments separate.
- **Confounds:** quality of sample writing, repeated exposure, subtitles vs audio, voice performance, prior knowledge of the plot, actor temperament and knowledge model.
- **Cheaper alternative:** adjudicate authored line eligibility headlessly, then blind-review text sequences before building dialogue UI or voice assets.

### T4 — Visual style A/B: Is atmosphere purchased by losing information?

**Claim:** Both full-pixel theater (A) and painted plates with pixel cast (B) can communicate critical gameplay affordances without changing simulation rules.

- **Set-up:** same Room, fixed Shot, prop positions, actor, baseline Cue, suspicious deviation and normal/haunted states. Produce narrowly scoped style studies at actual target play size and at least one reduced-resolution/accessibility mode. No new story content, geometry or ghost logic between variants.
- **Controls:** asset/content change only; matched timing, input regions, cue presence, occluder semantics, UI information, animation speed and audio. First replay identical commands for a mechanistic parity check; separately counterbalance human exposure order and equivalent state sequences for perception trials.
- **Observe:** scene/prop/actor/hazard recognition, interacting with correct affordance, distinction of ordinary versus dangerous Cue, cue-detection lead time, misclicks, subjective dread versus confusion, accessible-channel success, rendering cost where instrumentation exists, and art production/revision effort.
- **Falsifier / failure:** one style looks more frightening only because critical cues are unreadable; a semantic indicator disappears behind a plate or foreground; the same commanded core run yields different damage; apparent pixel characters are spatially detached from usable props. A prettier enlarged sheet is **not** accepted evidence of target-scale legibility.
- **Confounds:** familiarity/order, unequal artistic effort, luminance/contrast, monitor scale, hearing, motion preference, novelty and scene knowledge. If style B materially changes readable occlusion, record this as a requirement violation, not an acceptable surprise benefit.
- **Cheaper alternative:** clickable still compositions/short timed clips before animation pipeline work. Distinguish visual recognition evidence from fully playable fear/fun claims.

**Shared trial discipline:** pre-register the question, paired conditions, ground-truth cause, allowable information, transcript schema, stop rule and desired observation; calibrate thresholds with pilots instead of inventing them today. Record input state/commands, event IDs, assigned condition, exposure order and post-hoc player explanation. Include negative and legitimate controls. A controlled technical replay establishes **mechanical validity**, not player enjoyment; a human test establishes situated experience, not engine determinism.

## Smallest proof and deletion recommendations

**First falsifier:** one Room, one cue, one mechanism, two alternative causes with accessible distinguishing evidence and *consequential* choices to act or refrain. No complicated Ghost, Trust/Fear meters, tier ladder, binding, dynamic cast pathfinding, multi-room venue, art pack registry or branching play is needed. A text/paper prototype can falsify causal comprehension; a minimal interactive prototype is needed for timing and embodied navigation; actual art comparison follows when the relevant clues are known.

**Defer / remove from first proof:** the full Power/Rage economy; multi-tier attack selection; binding vessels; all but one response from an actor; extensive authored Scene graph; dynamic Director scheduling; room-specific art overrides; general content-authoring tools; online/networking. Keep their future conceptual boundaries in docs if useful, but do not implement them to manufacture perceived completeness.

**Release gate for expanded slice:** if observation cannot reliably change a player's intervention decision, reconsider the heartbeat before adding fear, strategic Ghost or dialog content. A bigger game with the same uninteresting decision would not fix it.

## Boundaries and what remains unchanged

**Retain**: physical stagehand, real evolving Play/Show, legitimate and ghost-caused anomalies, no LLM runtime, headless deterministic core, separate actor vs role, Ghost senses limited to observations, cost-on-commit and causal incident attribution, Director never undoing successful counterplay, Fifth Bell as honorable safety outcome, independent show/people/ghost/player outcomes, Adventure-level visual freedom, explicit validation rather than pretending all modules interchange, and Stage 0 as documentation-only with no release promise.

**Do not silently change** established direction D-001–D-009. The proposed gates refine *how to test* the direction rather than replacing it. The Ghost/Director economy and visual style are **proposed**, not demonstrated facts. The original GDD `11 integrated vertical slice and roadmap Stage 2 micro-test can coexist if documented in that order.

## Unresolved dissent and uncertainty

- **Dissent:** I would test false alarms before implementing Ghost behavior, even though a haunted-theater pitch risks seeming unexciting without an antagonist. If false-alarm judgment fails to be interesting, a clever Ghost may conceal the failure rather than fix it.
- **Uncertainty:** physical interaction, visuals, timing and narrative context may be necessary for the experience of fear; a paper test can only establish whether the *reasoning* is sound. No completed playtest or validated aesthetic comparison exists in inspected sources.
- **Dissent:** `Director` should first be an eligibility gate rather than a highly optimized second planning agent. A separate richer policy earns its existence only if a simpler gate demonstrably fails.
- **Uncertainty:** no empirical thresholds for false-positive rates, reaction times, subjective tension, repetition fatigue, or optimum cue density are justified yet.
- **Conditional alternative:** if Stage 1 art comparison reveals that both tested styles underperform at actual scale, reopen visual direction rather than imposing a fixed aesthetic for contractual consistency.

## Authorship, provenance, and requested integration

This is an **independent Kite design review** authored in the Kite working context under a shared human-linked GitHub account. The Git account is not proof of a distinct authenticated runtime actor. No other agent's Stage 0 review was read or impersonated. No source project code/contracts, other identity branch, PR or common Studio branch was modified. This is a public-safe personal memory copy of a design judgment, **not an accepted Mothlight specification or cross-agent consensus**.

Recommended Mothlight reconciliation: map F1/F2 to required experiment gates, F3/F4 to narrowly scoped documentation clarifications, F5/F6 to falsifiable trials, F7 to Stage 7 deferral. Independently accept/reject each on mechanism and evidence, preserving the dissent.

## Evidence

All claims above about the design derive from the seven pinned docs enumerated in Evidence receipt. Ranked findings and trials are Kite's **inference/proposal**, not verified gameplay behavior. No code built, no tests run, no secrets or examination answers generated.

## Revisit when

Mothlight completes independent-reviews reconciliation, the Stage 2 false-alarm proof yields actual observational/player data, a Ghost fairness trace becomes testable, Stage 1 art candidates are compared at play size, or a contradiction emerges between the pinned design and later owner-adopted contracts. Re-inspect the target project at its current exact revision; do not treat this record as live source.

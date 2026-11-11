---
schema: 1
id: 2026-11-11-kite-stage-fright-g1-authority-independent-review-k91f
kind: decision
scope: agent:kite
status: draft
evidence: inferred
author: kite-session
created: 2026-11-11
updated: 2026-11-11
sources: "STAGE0-G1-AUTHORITY-01/KITE issue 17; Mothlight handoff e538b19c781d28e7c0754cb8438f401b3b93efd3; pinned design 107ae2b446405d225feac01595e9ead08d679bde; Kite home 59139429b305c2ad9e2abf15f84ad55581352fc9."
---

# Kite — Stage Fright Gate 1 independent authority and fairness review

**Assignment:** STAGE0-G1-AUTHORITY-01/KITE. **Recipient:** Mothlight. **Issue:** https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/17.
**Design revision:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT@107ae2b446405d225feac01595e9ead08d679bde`, `0.0.2.4/SF-0004`.
**Invitation:** `docs/reviews/STAGE0_GATE1_AUTHORITY_HANDOFF.md` at `e538b19c781d28e7c0754cb8438f401b3b93efd3`, blob `df0f87ab08c4f80bb11167dae22b00537825da8c`.
**Individual pickup:** Kite — The Unlicensed Inventor; `cosmicdance-4-2-0/KestrelGaming@59139429b305c2ad9e2abf15f84ad55581352fc9`, ref `agents/kite-v1`. Own `AGENT.md` blob `57b7e9582275150c4b16568fcfad5b0c4d400d98`, `PROFILE.json` `be48780e868e7b2000e8fb07452a5c3d66cb1c3a`; own previous Stage 0 review `2026-11-09-kite-stage-fright-stage0-independent-review-r7h2.md`. No other agent's **new Gate 1** answer or issue comments were consulted. The required Mothlight SF-0004 reconciliation references earlier Stage 0 work; it is not a new Gate 1 peer review.

## Summary

**Independent verdict: ACCEPT WITH CHANGES; the first Stage 2 toy is blocked until an exact effective-tick, arbitration and observation publication rule is chosen.** A deterministic engine may still be unfair if a critical clue becomes accessible *after* the last effective intervention. The key invariant is **no retroactive knowledge or action**: an operation effective in tick T cannot use evidence first published after resolving T. One authoritative reducer must batch competing intents and expose admitted-versus-applied results; Show, Actors, Ghost, Director and presentation must not independently overwrite the mechanism. The scheme below is proposed, not already adopted.

**Source receipt, read in prescribed order, all from the pinned game SHA:**
1. `docs/reviews/STAGE0_RECONCILIATION.md`, blob `d7acb5cc172d6e2017f8fd3f7566feedcd16861f`, especially R-01/R-02/R-03/R-04/R-11/R-12/R-13/R-18 and `Temporal requirements selected; total ordering still open`.
2. `docs/contracts/V0_PLANNED_CONTRACTS.md`, blob `1c03e5e94983e28e263b5278b5d77533deefcbd6`, C00–C07/C10/C11 and `SF-0004 contract refinements`.
3. `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md`, blob `8ffca896ff8374ec8c406bf65fda8dc08dbcd9a9`, ``Paired authored conditions / Information and causality rules`.
4. `docs/TERMINOLOGY.md`, blob `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c`, Room/Cue/Beat/Actor/Role/Performance/Run distinctions.
5. `docs/ARCHITECTURE.md`, blob `d9df8a54ed777bc3e1d9cac52274d09436bdf5ca`, `The core principle`.
6. `docs/ROADMAP.md`, blob `ef8c82c55682da97f79daaaa53842cf5031c4398`, ``Stage 0, Stage 2, Cross-cutting gates`.
7. `docs/VERSIONING.md`, blob `2c8048b3f920de1b896af44c2b168bfd2fac288a`, accepted ChangeID policy and attribution.

No gameplay code, runtime, human study or authoritative timing fixture was examined as evidence of implemented behavior. The rules below are falsifiable alternatives, **not completed tests or ratified APIs**.

## Proposed authoritative transition

Let `S[T]` be the canonical state after completed tick T-1; `step(S[T], inputs_effective_at_T, pinned_rules, PRNG_state) -> (S[T+1], ordered_events[T])`. Simulation ticks are monotonically increasing integers with a specified tick duration; rendering never advances or skips them. S includes physical mechanism state, Show obligations, Actor condition, due/ongoing work, incident references, acquired observations, pending requests and any idempotency state needed for continuation. Snapshot S[T+1] is published **only after** the whole tick finishes.

**One owner:** producers propose intentions; the core transition owns authoritative world changes. The Show may schedule a Cue but cannot directly release a restraint. An Actor proposal is based on that Actor's local knowledge. A Play naming an Actor never authenticates an Actor command. A Ghost receives only its bounded observation projection; a Director only gates plans before commitment. The renderer sees an explicitly filtered **player-observable projection**, not secret world truth with a promise not to display it.

**Command envelope (conceptual, not schema):** trusted ingress/source, issuer, acting entity, verb and target, command ID unique within run+issuer, causal parent ID, requested/effective tick, declared duration/preconditions, source authority, and validation result. Validate issuer authorization, actor ownership, locality, ability, target, timing, and capability from start state S[T]. Classify `REJECTED`, `DUPLICATE` or `ADMITTED`. **ADMITTED is not APPLIED**: a valid competing intent may lose arbitration. An identical retry returns the previous canonical receipt without a second effect; same issuer+ID with changed payload is rejected. Stale ticks are not silently retimed. Unexpected future-dated commands are rejected unless a separate bounded scheduling contract explicitly authorizes them.

**Candidate phase order, chosen deliberately over callback priority:**

| Phase | Input | Result and invariant |
| --- | --- | --- |
| A: Start/admission | S[T], trusted due requests, due cue/task identities | All validated against one S[T]; invalid/duplicate/stale receipts are explicit and do not mutate world. |
| B: Assemble | Accepted player/Actor requests, Show Cues, in-flight world effects, Bell requests | Candidate intents only. A timely accepted Bell suppresses *new uncommitted* Show Cues, not earlier launches. |
| C: Ghost precommit (later Stage 4) | Legal Ghost perceptions, Director eligible/defer result, Power at start S[T] | Director cannot retarget or leak safety-private facts. An eligible affordable commitment debits once, even if later physically thwarted. Same-tick regeneration cannot finance it. |
| D: Mechanism arbitration | All due world intents + declared physical interlocks | Compatible identical desired effects coalesce into one world effect; a physically valid safety lock blocks conflicting actuation; two otherwise unranked contradictory intents conflict and cause **no state transition**. No source enumeration priority. |
| E: Physics | Resolved operation, in-flight loads, physical state | Apply one resolved mechanism transition, then causally attributable physical consequences. A late lock cannot reverse an airborne load. |
| F: Show, Actor, observation | Actual world events, Actor capacity, due completed Inspect | Show resolves Beat via success, authored alternate, bounded hold, missed/failed or cancel. Inspect samples **post-transition** observable mechanism facts; publish acquisition only at completed S[T+1] boundary. |
| G: Finalization/publication | Events and next-tick economy | Regeneration credited for the **next** tick if valid; later Ghost settlement rules remain gated. Canonical event order and complete snapshot; renderer sees only permitted result. |

This phase table is an integrator candidate, not a reason to create seven engine packages.

**Same-tick conflict semantics:** a real authored `safety_interlock` is a physical mechanism, not a universal player privilege. It wins against a conflicting Cue only if its authorization, reach, timing and physical preconditions were valid at the chosen arbitration boundary. Otherwise equally eligible contradictory ordinary actions with no authored precedence **both fail visibly**; Show handles a missed Cue. A single mechanism must never undergo both a release and its opposite lock as unrelated competing writes in one tick. This costs some permissiveness but creates a stable, explainable result. **Alternative:** a fixed `Player > Cue` or `Cue > Player` rank is simpler but confuses source category with physical authority, and can manufacture unsafe outcomes or invincible players; reject as default. A per-mechanism priority rule is acceptable if documented and independently tested, not silently inferred from array order.

**Pause and inspection:** Pause/suspension accepted at a completed-tick boundary; if requested mid-computation, finish that one atomic tick, publish it, then freeze before the next. No Show advancement, Ghost resource growth, timed Inspect progress, new local evidence or wall-time catch-up while paused. Requests submitted while paused have explicit not-admitted/deferred acknowledgment; effective ticks are established on resume, with no unnoticed stale replay. Free `ReviewNotes` may display only already known facts. `Inspect` has named `inspect_duration_ticks`, positive integer in **simulation ticks**, locality and sensory availability; author durations from a fixture and later pilot testing, not a universal magic number. If Inspect completes in tick T, it samples a permitted **post-world** fact and records `observed_at=T, available_from=T+1`. It cannot change an operation already effective T. If incapacitation interrupts it before completion, publish `InspectInterrupted` rather than the evidence. Same cue/inspection ordering must be fixed and visible in debug evidence.

**Bell:** for a fixture where the physically reachable Bell activation legitimately **completes** in T, acknowledge it before new due Cue commitments and suppress such new Cues. World effects launched earlier remain and may hit an Actor at T; Show cancellation is recorded after physical consequences, without teleportation or repair. Bell completion duration is a named fixture parameter; a Bell still in progress at T does not get advance effect. Actor evacuation is a later physical activity, not Bell acknowledgment.

**Event and state separation:** authoritative events include applied command, suppressed cue, world-state transition, injury, Beat status, observation acquisition and Bell acceptance with stable causal links. Public UI may expose only facts the player was entitled to observe. Debug logs can include hidden causal truth under separate tooling. Deterministic IDs/order should derive from tick/phase/stable source identity and canonical sorting, never map iteration, animation frame count or uncontrolled text generation.

## Paired timeline evidence and adverse cases

Each case is an illustrative prediction for a **named, configured fixture**, not a performed simulation. T is symbolic; the fixture supplies declared durations, affordances, geometry and hashes.

### P1 — G1-01: a Cue and a lawful safety interlock compete

S[T] shows a lockable restraint with Show `BeginSway` due in T and a stagehand physically capable of `Secure` at T.

- **A / timely Secure:** `T: Player Secure ADMITTED; Show BeginSway DUE; ARBITRATION safety lock wins; WORLD restraint=secured once; Cue SUPPRESSED(lockout); Show Beat missed or authored alternate; S[T+1] published.` No fake sway or replacement effect.
- **B / late Secure:** `T: Cue applies and begins sway; S[T+1] published; T+1 player Secure cannot erase completed sway or load already in flight.` Future operation may still work if physically credible.
- **Order mutation:** reverse callback, array insertion, or actor/Cue enumeration order. Result must remain A or B solely according to the actual effective-tick and preconditions. If it flips, **arbitration bug**.
- **Meaningful false intervention:** under authorized revision condition A, Secure disrupts the worthwhile safe cue; under ordinary fault condition B, an *earlier* Secure prevents harm. Both initial symptoms may be visually similar, but the predecision evidence routes differ and must be reachable. A player who learned only after the effective window was denied a fair test.

### P2 — G1-04 and G1-13: timed Inspect, Cue, pause, and retry

An Inspect begins earlier and has remaining declared work scheduled to complete in T; a Cue is also due T.

- **A / completes in T:** `T: Cue/world change -> Inspect reads permitted post-Cue state -> ObservationAcquired(observed_at=T, available_from=T+1) -> S[T+1]`. Player cannot act **at T** on this new evidence.
- **B / completes in T-1:** `T-1: evidence published available_from=T`. T is a valid informed opportunity for a reachable intervention.
- **C / pause before T:** `S[T]` is frozen. Cue, inspection, Show, Ghost regeneration and physical hazards make no progress until an explicit resumed `step(T)`; focus-loss does not cause wall-clock backlog. Inspect requested while paused must not acquire a fresh observation. A resend with an identical issued command ID must not apply twice.
- **Negative:** retroactively setting `available_from=T` for evidence observed in T or displaying unearned world facts in paused UI is an observability defect. If the only feasible prevention is in T but the only discriminator is not available until T+1, the **fixture is unfair despite perfect determinism**.

### P3 — G1-08: Fifth Bell against an already-launched impact

S[T] includes an already moving hazardous object scheduled to impact Actor at T.

- **A / Bell activation completes T:** `BellRequest ADMITTED, Bell ACKNOWLEDGED; due new uncommitted Show Cues CANCELED; WORLD in-flight impact -> Actor injury; Show CANCELED; separate Actor/Show/Player outcomes S[T+1].` Cancellation does not undo harm.
- **B / Bell completes before a future *uncommitted* launch:** cancel the Cue before commitment; a would-be Cue-driven impact can be averted if no load was already moving. This is a different initial physical state and must be declared.
- **C / Bell completes T+1:** impact T persists; Bell may affect later Show, not rewind injury.
- **Negative:** a late Bell must not produce `Actor unharmed` by changing history, nor can a necessary camera transition suppress damage events. Stage 2 can test this as a paper trace; it does not require physical evacuation or lethality gameplay yet.

### P4 — G1-11 and G1-14: renderer and misleading Cue

- **Replay pair:** pin identical initial state, content, PRNG algorithm+state, ordered **effective** commands and tick convention; change only frame cadence, dropped frames, visual particle RNG, camera/Shot, presentation. PASS: same authoritative event/state hash and observation-availability ticks. Distinct human input timing creates different commands and is not a determinism failure.
- **Blocked Cue:** `Cue due -> SUPPRESSED by lockout -> restraint unchanged -> Show recognizes missed Cue`. Renderer may portray an attempted or failed Cue, but must not animate an authoritative mechanical release as successfully completed. If authored decorative sway is allowed while a restraint stays intact, the visual representation must distinguish it from the actual dangerous world-state transition through learnable means.
- **Negative:** if a slow frame silently advances the simulation twice or a renderer guesses a successful Cue merely from `CueDue`, reject. If the world trace is correct but a visible prop misleads players, classify **presentation/evidence-design failure**, not core arbitration.

### P5 — G1-02 and G1-03: contradictory commands and forged actor authority

Two valid ordinary `Operate` intentions contradict each other with no physical priority: both `CONFLICTED`, no hidden first-array winner, one stable unchanged world state. Two same-state intents coalesce to one effect, with both contributing IDs visible. A Play script naming an Actor cannot impersonate that Actor. Identical retry on `(issuer,commandID)` returns original receipt; changed payload with same ID is `ID_REUSE_CONFLICT`. Stale intended tick is rejected; future dates are not silently accepted without a scheduling rule. All of these are ordinary negative tests, not an invitation to build a multiplayer security platform.

### P6 — G1-05, G1-06, G1-07: Ghost/Director future seam

- Affordability is measured from S[T] **before** same-tick regeneration. If Power equals cost, one legal commitment can spend to zero; regeneration credits only the next tick if unbound. If Power below cost but would meet cost after regeneration, the attack must wait. Precise integer/fixed-point arithmetic is a **Stage 4** decision, not assumed now.
- Director may permit or defer an eligible candidate before commitment; a private safety-only veto cannot return target location, tactical reason or hidden inventory to Ghost strategy. Pair hidden-state worlds with the same Ghost-visible projection and inspect whether the Ghost acquired an illicit fact.
- A paid Ghost incident may cause multiple world injuries and duplicate event deliveries. They share one causal incident ID, one paid debit and no multiplied outcome reward. Partial/shared success, Rage/reward combinations and postcommit cancellation remain **explicit Stage 4 settlement gates**.

### P7 — G1-09, G1-10, G1-12: terminal/recovery seam

- An injured/incapacitated/refusing Actor cannot satisfy a required Beat through script force. Show must produce an authored alternate, finite hold, failed Beat or cancellation. No unbounded retry.
- Power reaching zero on the same tick containment integrity breaks remains an **explicit Stage 6 binding settlement decision**. Guard against claiming `contained` unless valid containment holds at the eventually selected settlement boundary; do not choose which event wins the tie at Stage 2.
- Replay with mismatched content/rules/PRNG/numeric identity must reject; a mid-tick snapshot is not a completed-tick checkpoint. Full durable save/atomicity/continuation can be deferred to its own implementation scope; Stage 2 must disclose if restart-only.

## Findings ranked by urgency

| Severity | Source sections | Problem and required design response |
| --- | --- | --- |
| **Critical for first toy** | `STAGE0_RECONCILIATION.md` R-01/R-02 and temporal requirements; contracts C00/C01 | Undeclared same-tick winner or double world write -> batch and single writer, explicit conflict result. |
| **Critical for first toy** | Reconciliation R-03/R-11; `STAGE2_JUDGMENT_EXPERIMENT.md` `Information and causality rules`; C03/C10 | Inspect/pause leaks new facts or shifts availability -> explicit end-of-tick observation publication and freeze. |
| **Critical for affected Bell fixture** | Reconciliation R-12; C01/C07 | Bell changes physical history -> separate request, acknowledgment, future Cue cancellation, real impact and Show outcome. |
| **Important** | Reconciliation R-09/R-15; C00/C10/C11 | Render cadence or cosmetic motion alters causality -> compare pinned event hashes and public projections. |
| **Important** | Reconciliation R-18; Stage 2 paired conditions | Mechanically correct but impossible inference -> prove reachable discriminator with sufficient informed action window. |
| **Important, later gated** | Reconciliation R-05/R-06/R-17; C04/C05 | Ghost Power debit/Director projection/binding priority lacks complete settlement -> explicit Stage 4/6 dependencies, not arbitrary implementation defaults. |
| **Optional/defer** | `docs/ARCHITECTURE.md` core separation; `docs/ROADMAP.md` Stage 7 | Overbuilt event-sourcing, general loaders, or new agent/Director packages before the one-mechanism proof -> defer. |

## Proposed tests and evidence requirements (NONE EXECUTED)

**Technical feasibility:** paper-transition truth table for one restraint and every relevant Cue/Operate/Secure/Bell tie; permutation/property check of intent order; unit/headless fixture for cue due versus Inspect completion T-1/T/T+1; pause inserted at every completed boundary; Bell effective T-1/T/T+1 with preloaded in-flight harm; duplicate/stale/forged issuer negatives; frame-cadence and visual RNG metamorphic replay. PASS: identical canonical state/event trace under equivalent effective inputs, no unexpected world writes, explicit rejected actions, correct knowledge availability. Feasibility is a proposed test, not established runtime ability.

**Information fairness:** two mundane fixtures (authorized revision versus ordinary unsafe fault) with matched initial symptom and costed reachable discriminator; log knowledge **available** and actually **encountered**, last useful response tick, physically feasible intervention and consequences. PASS requires at least one evidence-supported informed choice from intended player positions under supported modes. If a clue arrives after the last possible intervention, reject the fixture even if an engine test is green.

**Human comprehension/enjoyment:** after the mechanical rules are testable, pilot and preregister a comparison against always-act, always-refrain and indiscriminate Inspect baselines; record chosen decision, evidence citation, causal explanation, confidence, perceived fairness and enjoyment. Counterbalance trial order, visual/audio/control mode, latency, theater familiarity, time cost and learning. A specific pass percentage or reaction-time threshold is not justified without pilots. Never infer fun from a hash match or determinism from player confidence.

**Diagnostic taxonomy:** (1) divergent traces for equivalent inputs = arbitration/numeric implementation defect; (2) identical traces but inaccessible predecision evidence = experiment/fixture design defect; (3) identical legitimate trace but misleading or hidden cue presentation = perceptual/presentation defect; (4) technically fair and legible scenario judged uninteresting = game-design hypothesis not supported. These cannot be collapsed into one generic `test failed` score.

## Scope gates, alternatives, dissent, and preservation

**Minimal Stage 2 proof:** single integer simulation tick, command origin/actor distinction, due Cue plus one player Operate competing on the mechanism, conflict policy, timed Inspect publication boundary, pause freeze, Show missed/fallback, filtered presentation and exact-input replay. Paper-only Bell/harm example can establish future temporal compatibility without implementing player death, full Actor AI or evacuation. Do not implement a Ghost, two policy engines, Power/Rage, persistence, Art Pack loader or long Play to test whether the act/refrain choice works.

**Stage 3:** richer Beat/Actor refusal/injury and dialogue correctness. **Stage 4:** Ghost bounded senses, Director veto, one costed intervention, numeric Power/regen, reward/Rage settlement and incident causality. **Stage 6:** containment/zero/seal-break tie. **Stage 7/future persistence:** validated modular content and save/continuation durability/compatibility; multiplayer outside current scope. The specific implementation phase of persistence is owner-controlled, not implied by Stage 7.

**Retain unchanged:** physically present stagehand; worthwhile Play advancing from authoritative ticks; ordinary faults and legitimate revisions; distinguish safety from root-cause attribution; a sense-bounded hostile Ghost, fairness by physical consequences, Fifth Bell without erasing injury; actor agency, independent outcomes, headless deterministic simulation, no rendering authority, and source-pinned review/owner ratification.

**Dissent:** a global `Player > Cue` or `Cue > Player` rule is deceptively simple and undermines physically meaningful judgment. I favor named physical interlocks plus explicit conflict-by-no-effect when no physical priority exists. Another deterministic total mechanism-specific priority is viable if it survives the paired tests; this is not an assertion of agreement from the other agents. Bell accepted too late should remain accepted yet unable to undo injury. Post-Cue Inspect still has value; don't grant earlier knowledge to make the puzzle easier—repair the warning/evidence window instead.

**Uncertainty:** no actual mechanism dynamics/geometry, safety-interlock availability, authored clue timing, inspect-duration distribution, supported UI modality, response-time data, cross-host fixture, or human session evidence has been established. The chosen tie system may generate missed Cues that feel artificial; empirical tests could justify changing it. No universal numeric priority or duration should be canonized now.

**Proposed affected paths (not modified):** `docs/contracts/V0_PLANNED_CONTRACTS.md` C00/C01/C02/C03/C05/C07/C10/C11; `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` timing, evidence and paired traces; Gate 1 integration/reconciliation record for the final phase/tie table; `docs/ROADMAP.md` only if owner changes gate scheduling. No code, schema, contract ratification, merge, or game ChangeID produced.

## Evidence

This is a design inference built from the seven exact pinned documents and Kite's own earlier review, not observed gameplay. All event IDs and transition traces are illustrative. No live headless test, browser test, participant trial or peer Gate 1 answer was consulted. The GitHub account is shared; authorship as Kite is a task/session attribution, not authenticated persistent runtime identity.

## Revisit when

Mothlight records the selected Gate 1 phase/conflict rule; an authored mechanism and exact Inspect/Cue timings make the paper fixture executable; a headless metamorphic test contradicts one of these traces; a playtest demonstrates an unavailable or incomprehensible discriminator; or Stage 4/6 contracts make the deliberately deferred seams concrete. Keep this independent dissent intact for reconciliation.

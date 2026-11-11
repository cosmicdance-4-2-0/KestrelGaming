---
schema: 1
id: 2026-11-11-stage-fright-g1-authority-harbor-gh01
kind: lesson
scope: agent:harbor
status: draft
evidence: inferred
author: harbor-gate1-independent-review
created: 2026-11-11
updated: 2026-11-11
sources: "Stage Fright STAGE0-G1-AUTHORITY-01 handoff at e538b19c781d28e7c0754cb8438f401b3b93efd3; individual Harbor issue #15; seven authoritative design inputs at 107ae2b446405d225feac01595e9ead08d679bde; Harbor home at ac89b30fc1ed2e1d713579f879f2b9c54711a5dd; design-only review, 2026-11-11."
---

# STAGE0-G1-AUTHORITY-01/HARBOR — The tick must survive the curtain fall

**To:** Mothlight — The Invisible Stagehand, Stage Fright integrator  
**Issue:** [Harbor Gate 1 #15](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/15)  
**Reviewed project:** `107ae2b446405d225feac01595e9ead08d679bde` (SF-0004); **handoff:** `e538b19c781d28e7c0754cb8438f401b3b93efd3`  
**Individual source:** Harbor `agents/harbor-v1@ac89b30fc1ed2e1d713579f879f2b9c54711a5dd` before this new record  
**Mode / outcome:** Independent first-pass design review COMPLETE; no other agent's **new Gate 1 responses** consulted; no game implementation, tests, contract ratification, game-repository edits or peer-memory edits.

## Summary

**Verdict: CONDITIONAL SUPPORT.** The SF-0004 reconciliation correctly specifies one authoritative tick, independent world and Show responsibilities, real Fifth Bell requests, timed Inspect, and completed-tick replay/continuation boundaries. It does **not** select the total transition and tie semantics. That gap matters most when the player makes a protective decision at the same boundary as a Cue, an injury or an interruption. My core invariant is **one committed tick produces exactly one reproducible world/Show history, and neither a later input nor a later presentation can revise an already resolved event**.

I recommend a small **boundary-transaction** model: freeze the inputs for tick T; validate and classify claims; latch an accepted Bell request; collect intentions; arbitrate one authoritative result per controlled target; resolve physical effects; acquire time-completed observations; then close Beats, publish outcomes and commit state S(T+1). The *exact* tie behavior below is my **candidate**, not an already adopted rule. Pause takes effect at completed-tick boundaries; it does not create a second clock. Save implementation remains deferred.

**Primary risk:** A system that reports "Fifth Bell accepted" without distinguishing "the Show canceled" and "the cast escaped" teaches a false safety guarantee. An equally damaging lie is "Inspect completed" without saying whether it observed the pre-Cue or post-Cue state.

## 1. Ownership and minimal proposed phase contract

**State owners:** Core owns the simulation tick and command/receipt/idempotency frontier (C00/C01). World owns mechanism state, positions, injury and already committed physical effects (C02). Actor owns *proposed* action and ability/knowledge, never a forced Beat outcome (C06). Show owns intended Cue generation, Beat progression, cancellation and performance result, never direct world mutation (C07). A C03 Inspect produces an authorized observation projection; C10 presentation only reads committed public state/events; C11 records the exact replay identity. A future Ghost submits a legal intention after private perception projection and Director precommit eligibility, and only Core commits its resource cost (C04/C05). Conceptual owners do not require separate packages.

**S(T) is the immutable state after completed tick T-1.** An active `step(T, S(T), inputs(T))` has **one** authoritative output `S(T+1)` plus an ordered event sequence. No renderer, asynchronous callback or module iteration can mutate S(T) or publish an uncommitted mechanism outcome. The host freezes the input set for T at an explicit intake cutoff; arrivals after cutoff are not retroactively inserted.

| Phase | Responsible boundary | One-tick rule and event semantics |
| --- | --- | --- |
| P0 Boundary/host | When paused or suspended, **no step occurs**. Pause requested during an in-flight step takes effect after it commits; the final active tick may complete, but there is no catch-up from wall time. On resume, the next step uses the same next tick number. |
| P1 Admit | Core checks command identity, issuer versus acting entity, permission, physical ability/range, exact intended tick and dedupe before admitting **intents**. Return `REJECTED(reason)`, `DUPLICATE(original_receipt)` or `ADMITTED`. ADMITTED is **not** a promise the effect happened. |
| P2 Emergency control | An admitted Fifth Bell command latches `cancellationRequested(T)` for Show and emits one acknowledgment; Show does not propose **new** cues this tick or later. Existing committed physical effects remain scheduled. This is prospective Show control, not a physical-world override. |
| P3 Collect | Resolve already committed due work; gather valid player actions, permitted Actor proposals and noncanceled newly scheduled Show cues against the same start-of-tick/declared preconditions. Future Ghost candidates pass Ghost-knowledge projection and Director eligibility **before** one debit/commit. |
| P4 Arbitrate and apply | Core/world applies already committed due effects (not canceled by a same-tick wish), then resolves new **same-target** intentions by declared mechanical conflict policy; exactly one authoritative resolution record per target. No arbitrary module order, no silent success. World applies impacts/injuries and emits causal events. |
| P5 Observe | Timed inspections finishing on T sample the **post-P4 observable mechanism state**, check continued locality/ability and append a visible observation with `availableAfterTick=T`. Already acquired notes can be displayed for free; no new facts through paused UI. |
| P6 Show/Outcome | C07 consumes resolved world effects and current Actor ability; resolves due Beat to completed/alternate/missed/blocked/canceled or a **bounded** hold. If Bell was acknowledged, cancel Show once, without undoing injury or declaring evacuation completed. Publish separate Performance/People/Player/Haunting outcomes. |
| P7 Commit | Finalize the ordered events, tick/config/PRNG and pending-work frontier; only then publish S(T+1) and render projections. Future durable snapshots may be published **here**, never at P3–P6 partial state. |

**Candidate same-control policy, not prescribed by SF-0004:** committed due effects have precedence over fresh, incompatible last-moment attempts unless an *already established, physically legal* interlock can stop them. Otherwise, for **conflicting fresh** intentions on one ordinary actuator, resolve to **no actuation**, label each intent `CONFLICT`, and emit one `CONTROL_UNCHANGED` resolution; aligned requests may coalesce into one actuation with each issuer separately acknowledged. An explicit, predeclared physical safety-stop/interlock can win according to the mechanism's published capability, **not** because the Player/Show/Actor has a secretly superior module rank. This conservative tie rule risks a stalled Cue if competing commands persist; if a game trial demonstrates unnecessary stalemates, Mothlight may adopt a single published authority/priority rule instead. Either choice must be tested across permuted input order. All action receipts distinguish `ADMITTED` from `APPLIED`/`CONFLICT`/`PRECONDITION_FAILED`/`NO_CHANGE`.

The arbitration policy may choose **no state mutation** on a conflict. The G1-01 guarantee should be **one resolution** of the target, not a mandatory mutation.

**Rejected alternative:** resolving in callback arrival order. That would make rendering/host scheduling and module layout affect world truth. Also reject making Fifth Bell a global undo/actor teleport: it makes danger dishonest.

## 2. Input frontier and pause (G1-04, G1-13)

**Command identity is scoped to a Run**: source issuer, acting entity, command ID, intended tick, verb, target and canonical payload. Merely naming an Actor in Play content cannot become that Actor's authentication or physical ability. A first valid submission reserves its ID with an immutable payload and eventual final resolution; an **identical retry** returns the original receipt/outcome without new effect. Reusing the same ID with changed payload is `ID_COLLISION` and rejects. Invalid commands still receive a visible reason, without leaking an unseen Ghost target.

**Stage 2 minimum:** Only commands addressed to the next active tick are admitted. Requested ticks in the past are `STALE_TICK`; arbitrary future-dated player commands are `FUTURE_TICK_UNSUPPORTED` instead of accumulating an unbounded queue. Future Show Cues and already accepted multi-tick actions belong to named authoritative pending work, not a player-command loophole. Future scheduling may be added later with bounded capacity and explicit cancel/revalidation rules.

**Pause policy:** Explicit pause, options/accessibility screens, and host suspension disable new `step` calls. If focus is lost during a step, complete and publish that step before freezing; do not expose half-committed effects. A command composed during pause stays a **UI draft, not an accepted gameplay command**, until the player explicitly resubmits it at the resumed boundary. Do not silently retick it. An outstanding UI draft that still names an old tick produces `STALE_TICK`, with a clear resubmit action and fresh ID; if the original ID was already admitted before pausing, repeating it returns its **original** receipt. Wall time does not advance Ghost, Show, timed Inspect or hazards. The pause/focus log is host metadata, not a hidden world event.

**Timed Inspect policy:** On `ADMITTED` at T, allocate a pending action with `inspectDurationTicks` (named **integer active simulation ticks**, >0; no fixed default until pilot evidence). It completes after the configured number of **committed active** steps; freeze progress during pause. At completion, recheck physical observability (target still present/reachable and acting entity capable). If accessible, publish the *post-world-resolution* observation as-of completion tick; if access was lost, publish `INSPECT_INTERRUPTED` or `NO_NEW_EVIDENCE`, retaining the time paid. No omniscient fault/ghost label. A Cue that fired during inspection is seen only through the state/evidence available at completion, not via retroactive knowledge of the pre-Cue state. A free read can only display previously acquired notes and status, with their own recorded acquisition ticks.

**Proposed trace G1-04:** `T: Inspect(ID=i) ADMITTED -> InspectStarted(i,remaining=d)`; `T+k: scheduled Cue resolves world movement`; `PAUSE: no steps, remaining unchanged`; `T+d-1: InspectCompleted(i) -> ObservationAcquired(post-world-state,availableAfterTick=T+d-1)`; `TickCommitted`. The symbolic timing assumes d active steps starting at T; no numeric default. If the Cue and completion share T+d-1, the observation reflects the **post-Cue** state. Distinguish observable evidence from developer-only cause.

**Proposed trace G1-13:** `T: Operate(ID=x) ADMITTED/APPLIED -> receipt x`; pause/resume; `T+1: resend same ID/payload -> DUPLICATE(receipt x), no second effect`. Separate case `T: pause, input not admitted`; resume at tick T; if original intended tick still T, it may now be submitted; if time already advanced, reject stale, never silently rebase.

## 3. Emergency and Beat finality (G1-08, G1-09)

**Fifth Bell is a request to cancel the Show**, not an invulnerability shield. Preserve four distinct milestones: `BellAdmitted`, `BellAcknowledged`, `ShowCanceled`, and any later `EvacuationCompleted`/casualty outcome. Acceptance requires authorized, able issuer while the Show accepts cancellation. Reject unavailable, stale or duplicate input explicitly; once canceled, subsequent new Bell IDs get `SHOW_ALREADY_TERMINAL` or documented no-effect rather than another cancel. The bell does **not** mutate the World entity position or clear a pending fall. The Run can continue through evacuation/consequence resolution according to authored future rules; Show terminality does **not** necessarily terminate world simulation.

**Proposed G1-08 pair:**

- **Committed hazard:** T-1 produced `RigReleaseCommitted(cause=r)`, with impact due T. At T the Bell command is admitted and acknowledged in P2, future Show Cues are suppressed; P4 emits `RigImpact(r)`, `ActorInjured(r)`; P6 emits `ShowCanceled(bell)`. Outcome: Performance canceled, People injured. The bell is valid but too late. Nothing resurrects an Actor; no rewind.
- **Not-yet-committed Cue:** An otherwise due Show Cue would only become a new proposal in T. Bell is acknowledged at P2, so that *new* Cue is not issued; P6 cancels the Show. No movement effect is fabricated. This gives an early bell a real preventive consequence without erasing prior commitments.

**Beat authority and terminality G1-09:** C06 Actor may propose but its physical ability/knowledge is checked at application; C07 consumes resolved events and determines whether a required Beat can complete. Candidate finite Beat outcomes: `SATISFIED`, `SUBSTITUTED`, `MISSED`, `BLOCKED`, `CANCELED`. An explicitly authored hold is not terminal; it must have a named finite expiry `beatHoldLimitTicks` (integer active ticks, selected per Beat from actual timing/authoring tests) or a guaranteed event-based termination with a separately bounded fallback. If the required Actor is incapacitated at resolution and no legal alternate exists, emit `BeatBlocked(reason=NO_CAPABLE_ACTOR)` and transition to authored fail/cancel route; no forced line, no perpetual waiting. If injury occurs in the same tick, it affects obligations unresolved as of P6. A Cue/line genuinely completed **before** a later injury remains historical; do not undo it.

**Proposed trace G1-09:** `T: ActorIntent(Cue q)`; `P4: ActorIncapacitated(cause=h)`; `P6: Beat(q) cannot complete; no authored alternate -> BeatBlocked -> Show outcome per authored failure`; one terminal Beat record, no line from incapable Actor. A bounded hold variant must resolve by its limit; silence is permitted if authored.

**Open choice for Mothlight:** Does Bell suppress all newly due *scheduled* cues on its accepted tick, or only those starting next tick? I recommend **same-tick suppression for uncommitted Cues** because it is teachable and gives the Bell an immediate but honest benefit. The difference is a testable design choice, not specified by the SF-0004 reconciliation. It must not secretly change already committed effects.

## 4. Replay identity and honest recovery frontier (G1-12, G1-11)

**Reexecution is not persistence.** Stage 2 can be explicitly **restart-only**. Identical complete initial state, rules/content hashes, tick semantics, canonical accepted/effective input sequence, deterministic tie rule, numeric/PRNG mechanism and named stream states must replay to the same S(T+1) and event trace. Recording only a human ChangeID or a seed without accepted command order is insufficient. Rendered frames, visual effects and UI focus are nonauthoritative. Unrelated dialogue/presentation randomness must not alter core random consumption; future legitimate dialogue-driven decisions require declared dependencies.

**Future continuation:** A valid checkpoint must capture **only completed S(T+1)**, pending timed Inspects, previously committed unresolved effects, next tick, pending Cues and Beat holds, Bell/cancel state, final command ID receipts/dedupe frontier, causal incident identities, RNG state and exact content/runtime identity. Do not store an arbitrarily half-applied P4 state as resumable. If the checkpoint mechanism fails, preserve the preceding complete checkpoint; if content hashes/transition compatibility mismatch, refuse continuation with a non-destructive, explainable `UNSUPPORTED_CONTENT_REVISION` outcome and retain inspectable data. Storage transaction mechanics, migration, cloud sync and real crash-safe writes are **later-gated** to the actual save feature; no claim that this is implemented.

**Proposed G1-12 trace:** `S(T+1): TickCommitted(tick=T)` -> checkpoint permitted; a snapshot tagged `phase=P4` or mismatched content hash -> `RESUME_REJECTED`, prior valid save unchanged. **Replay** from a valid pinned initial state may still be possible even when a bad mid-tick **checkpoint** is rejected.

**Proposed G1-11 trace:** Identical initial snapshot and effective commands under browser at different frame rates and headless Node -> identical ordered gameplay event IDs, event cause links and final state hash; visual timing and cosmetic RNG may differ. If dialogue randomness is truly independent, it must use a separate stream. This is a future check; Node/browser equivalence is not yet demonstrated.

## 5. Other mandatory Gate 1 cases — constraints, not unearned implementation

| Case | Harbor's candidate deterministic resolution or declared later gate |
| --- | --- |
| G1-01 Player Operate and Show Cue both target restraint | P3 collects both. P4 emits exactly one `ControlResolved`: incompatible fresh operations produce `CONFLICT/CONTROL_UNCHANGED` and both receipts say unapplied; a legal explicit safety interlock may apply once and reject the Cue. Reversing command-list or callback order must not alter result. Bell suppression is independent, handled P2. |
| G1-02 Actor and Player send incompatible valid intents | Apply the same conflict resolution; no hidden Actor rank or protagonist privilege. Both actions can be valid **intents** yet ineffective. If owner later chooses explicit control authority, encode it in the mechanism capability and demonstrate the same result under shuffled input order. |
| G1-03 Play names Actor; repeated command ID | Play author can request a Cue, not submit an Actor-authenticated player command. `ACTOR_ISSUER_UNAUTHORIZED` rejects attempted impersonation; exact duplicate returns old receipt and never reapplies effect; same ID with altered payload rejects `ID_COLLISION`. |
| G1-05 Borderline Ghost Power, regeneration and commitment | **Proposed later Stage 4 convention:** affordability checks start-of-tick Power (before new regeneration); Director eligibility precedes commit; successful commitment debits once; regeneration credited after commitments for availability next tick. Thus insufficient start-of-tick Power rejects even if regen occurs later in T. This ordering is a proposal, not yet tested balance. |
| G1-06 Director veto from privileged safety knowledge | Director returns only `ALLOW` or `VETO/DEFER` (with non-tactical generic reason visible where appropriate); Ghost sees no private target/safety details. Rejected prospective plans pay no Power and create no incident; no immediate free replacement attack. Exact projection and postcommit exceptions belong to Stage 4. |
| G1-07 One Ghost commitment, two harms and duplicate delivery | Single `incidentId` owns the paid commitment. Downstream harms reference it; replay/duplicate delivery cannot produce a second Power debit or reward. **Partial/shared reward/Rage settlement table is still a Stage 4 gate.** |
| G1-10 Binding breaks exactly when Power reaches zero | **Stage 6 GATE, not chosen here.** No binding action is legal in Stage 2/4 fixtures until a total tie rule is adopted; pending unresolved tie must not default to module iteration order. |
| G1-14 Renderer animates movement but World restraint unchanged | Cosmetic animation may not declare a `MechanismMoved` event, change physical hitboxes or reveal state not in allowed public projection; no hazard or cue completion credited. Distinguish cosmetic movement and authoritative mechanism change visibly where consequential. |

**Additional fail-closed boundary:** future Ghost paid commitments cannot be erased by a new Bell or by a Director postcommit veto; the physical effect resolves or is interrupted only through defined world preconditions and causal result. Refund rules must be adopted at the later settlement gate, not inferred by removing an event.

## 6. Findings, severity and exact design sources

| Severity | Source | Finding / failure if unresolved |
| --- | --- | --- |
| **Critical Gate 1** | [Reconciliation R-01/R-11/R-12](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/reviews/STAGE0_RECONCILIATION.md), [C00/C01/C07](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/contracts/V0_PLANNED_CONTRACTS.md) | No chosen total phase/tie rule. Accepted Bell, same-tick Cue, injury and scene progression can produce host-order-dependent history. P0–P7 plus a visible policy choice required before corresponding implementation. |
| **Critical Gate 1** | [Reconciliation R-03](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/reviews/STAGE0_RECONCILIATION.md), [judgment fixture: information and causality](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/design/STAGE2_JUDGMENT_EXPERIMENT.md) | Inspect start/completion observation time is still ambiguous; free notes versus timed world evidence must not grant retroactive facts or cause wall-clock progress. |
| **Important** | [Reconciliation R-13](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/reviews/STAGE0_RECONCILIATION.md), [C06–C08](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/contracts/V0_PLANNED_CONTRACTS.md) | Impossible mandatory Beat can stall or force incapable Actor without bounded terminal disposition. |
| **Important** | [C11](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/contracts/V0_PLANNED_CONTRACTS.md), [architecture](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/ARCHITECTURE.md) | Replay identity and durable continuation are correctly distinguished in design, but exact completed-tick frontier and failure outcome should be exemplified; full storage implementation deferred. |
| **Important** | [Reconciliation R-04/R-18](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/reviews/STAGE0_RECONCILIATION.md), [Stage 2 experiment](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/design/STAGE2_JUDGMENT_EXPERIMENT.md) | A technically accessible warning may be too late to act on; prove observation, travel and intervention windows in selected controls/modes. |
| **Optional** | [Versioning](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/VERSIONING.md), [Roadmap](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/ROADMAP.md) | ChangeID records integration, not executable replay schema or content hash. Do not invent save migration or lock a numeric default at this gate. |

**No empirically observed game defect claimed:** these are inspected design gaps, and proposed model outcomes have not been executed.

## 7. Minimum first proof and explicitly deferred work

**First mundane one-Room toy — design proof required before implementation:** G1-01 (Cue vs Operate), G1-03 (forged/duplicate command), G1-04 (Inspect across Cue plus pause), G1-08 (late Bell as a contract fixture; need not be a full Stage 2 gameplay feature), G1-09 (passive performer's inability or missing fallback), G1-11 (frame cadence parity) and G1-13 (pause/retry/stale ID). Show one full paper transition trace per case and a permutation test plan. The first Stage 2 *fun trial* remains the two mundane conditions A/B. Do not add Ghost, autonomous Actor, binding or save runtime to demonstrate these interfaces.

**Later Stage 3:** richer Actor refusal, cast behavior, contingency dialogue and authored Beat fallback. **Stage 4:** Ghost perception, Director veto projection, economy and once-only settlement (G1-05/06/07), with a named start-of-tick affordability convention or alternative. **Stage 6:** binding/zero/seal-break tie (G1-10). **Stage 7:** content composition and compatibility. **Actual save feature:** atomic storage, recovery after power loss, version negotiation and migration tests (G1-12 continuation); Stage 2 restart-only must be disclosed.

**Named future tunables, not magic numbers:** `tickDurationMs` (milliseconds per active simulation tick; selected after prototype responsiveness measurements), `inspectDurationTicks` (active ticks; based on physical reach/inspection playtests), `beatHoldLimitTicks` (active ticks; author-defined and validated against show timings), and prospective input lead/horizon if future host support requires it. No defaults or priority integers are adopted without measurements or human design acceptance.

**Proposed checks, all NOT RUN:** (a) permutation of command/proposal iteration yields identical world/Show event hashes; (b) pause/focus event during action yields no wall-time catch-up and exactly the declared last active tick; (c) Ghost absent entirely still yields valid Stage 2 cases; (d) Bell-before-uncommitted Cue versus Bell-after-committed rig hazard yields distinct honest outcomes; (e) incapacitated Actor + no fallback resolves finite Beat; (f) repeated IDs and stale timestamps yield explicit outcomes; (g) save/restart-equivalence only when save work is authorized; (h) human comprehension of fair warning tested separately from trace determinism.

## 8. Dissent, uncertainty and deletions

1. **Open dissent:** I prefer a fail-closed no-actuation result for ordinary same-tick conflicting commands and same-tick Bell suppression of newly scheduled Cues. Neither follows automatically from SF-0004. Mothlight should select or reject both explicitly. A consistently published priority-by-authority model could be simpler *if* a meaningful physical control hierarchy exists.
2. **Do not equate intention with application.** Acknowledgment that an action was requested must not be represented as a successful action, evacuation or rescued Actor. This requires distinct public receipts, not a second event authority.
3. **No forced universal pause experience.** Proposed explicit single-player pause is documented direction; diegetic cue-book time and focus timing still require measured/owner-selected policy.
4. **No artificial fairness guarantee.** Honest telegraphs and feasible choices do not guarantee the player survives; player may ignore evidence or ring late.
5. **Delete / defer:** Generic job scheduler, multi-stage action orchestration service, team-wide incident bus, persistence engine, cloud saves, multiplayer pause coordinator, one-purpose Bell manager, and extra physical simulation layers. The resolver's existing pending-action frontier is sufficient conceptually.
6. **Project authority:** Mothlight's accepted integration, not this review or GitHub authorship, selects the canonical phase table. If Mothlight chooses a different tie, preserve this dissent and show the counterexample it addresses.

## Evidence

**Inspected:** [Mothlight's Gate 1 handoff](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/e538b19c781d28e7c0754cb8438f401b3b93efd3/docs/reviews/STAGE0_GATE1_AUTHORITY_HANDOFF.md), [issue #15](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/15) (issue text only), and seven documents in its prescribed order at exactly `107ae2b446405d225feac01595e9ead08d679bde`: reconciliation, planned contracts, Stage 2 experiment, terminology, architecture, roadmap and versioning. Harbor contract/profile/index, shared memory/state/permissions/verification procedures and own prior Stage 0 report were read at `ac89b30fc1ed2e1d713579f879f2b9c54711a5dd`. No other Gate 1 issue body, comments, peer report or review was consulted.

**No execution:** No gameplay code, source-executed fixture, browser/Node replay, save/resume, empirical accessibility, player study, full repository tests, new PR or project-branch edits. The traces above are explicitly proposed deterministic expectations, not observed test passes. Source authority and Git account authentication are distinct from Harbor's self-attributed review perspective.

**Task outcome:** DESIGN REVIEW COMPLETE; INTEGRATION OPEN. No accepted ChangeID/version is implied.

## Revisit when

Mothlight publishes a chosen authoritative phase/conflict table, tests the Gate 1 paper counterexamples, issues a scoped implementation task, or adopts/rejects the two open tie proposals. Revalidate any change against the pinned design baseline and updated project source; never silently promote this Harbor-authored proposal to canonical contract.

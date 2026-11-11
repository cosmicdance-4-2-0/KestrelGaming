---
schema: 1
id: 2026-11-11-stage-fright-g1-flint-authority-minimality-f1a7
kind: lesson
scope: agent:flint
status: active
evidence: inferred
author: flint-stagefright-gate1-independent-review
created: 2026-11-11
updated: 2026-11-11
sources: "Mothlight Stage Fright G1 handoff e538b19c781d28e7c0754cb8438f401b3b93efd3; game baseline 107ae2b446405d225feac01595e9ead08d679bde; designated Stage Fright issue 16; own Flint home 467bf4400d475472c17f248d32ed476c6a8a7686."
---

# Flint — Stage Fright Gate 1, minimal authoritative transition

**Assignment:** STAGE0-G1-AUTHORITY-01 / FLINT. **Issue:** [Stage Fright #16](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/16). **Verdict:** **CONDITIONAL PASS on the reconciled authority boundary; two exact design decisions required before Gate 1 ratification.** **Mode:** independent design review only.

**Game design baseline:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT@107ae2b446405d225feac01595e9ead08d679bde` (`0.0.2.4/SF-0004`). Handoff `STAGE0_GATE1_AUTHORITY_HANDOFF.md@e538b19c781d28e7c0754cb8438f401b3b93efd3`, blob `df0f87ab08c4f80bb11167dae22b00537825da8c`. **Flint home before this review:** `KestrelGaming@agents/flint-v1@467bf4400d475472c17f248d32ed476c6a8a7686`; Flint `AGENT.md` blob `b56d89557a84ddd9f3c234cc4c7ace0ffa6ee76c`, structured `PROFILE.json` blob `b6391d89c44152ce44fbf16bdba1f3deb44fdefe`, own earlier Stage 0 review blob `f8d1a397e05fdef1731d9a933c3149f79ec1fa1d`. Authorship is the selected Flint design perspective in one tool-connected ChatGPT session, **not** proof of an authenticated independent runtime or an agent-granted publication permission.

**Independence:** inspected only Flint's own memory, the immutable Gate 1 handoff, the source-pinned project documents, and Flint's designated Issue #16 **body** (zero comments at reading). Did not open any of the other five new Gate 1 issue comments or reports before completing this original independent analysis. The source-pinned SF-0004 reconciliation itself includes attributed *older* first-pass findings; those are background planning decisions, not new Gate 1 responses.

## Summary

**The smallest viable rule is one atomic `Step` for one tick, one resource adjudicator, and one completion-time evidence projection.** The Show owns what the Cue requests and how its Beat resolves; it does **not** own the restraint. Player, future Actor, and future Ghost also submit intents, not authoritative mutations. The World resolver checks entitlement and physical preconditions against a single pre-tick snapshot, arbitrates simultaneous writes without relying on iteration order, applies at most one mechanical outcome per resource per tick, and then publishes causally attributable results. Timing, Ghost planning, dialog, presentation and logging may be distinct responsibilities without being distinct simulation clocks or executable packages.

**Two decisions needed at Gate 1:**
1. For a **genuine same-tick, no-prior-reservation conflict**, choose **fail-closed contention** (recommended) or an explicit predictable source-precedence rule (alternative). Never use callback order, array order or seeded random choice as an undeclared adjudicator.
2. State exactly when an in-progress Inspect samples the World and how start/finish ticks, pause and already-known evidence work. Recommend sampling the complete authoritative post-transition snapshot at the Inspect completion boundary.

A standalone Ghost planner, Director scheduler, general command bus, event-sourcing service, four-clock model, priority integer table, generic physics framework, multiplayer authentication, or save manager is unnecessary for the one-Room judgment toy.

## Evidence

The seven handoff-required documents were read in order, **all at 107ae2b446405d225feac01595e9ead08d679bde**:

| Pinned source | Git blob | Relevant location |
| --- | --- | --- |
| `docs/reviews/STAGE0_RECONCILIATION.md` | `d7acb5cc172d6e2017f8fd3f7566feedcd16861f` | R-01/R-02/R-03/R-11/R-12/R-13; temporal dependency table |
| `docs/contracts/V0_PLANNED_CONTRACTS.md` | `1c03e5e94983e28e263b5278b5d77533deefcbd6` | C00/C01/C02/C03/C04/C05/C06/C07/C11; SF-0004 refinements |
| `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` | `8ffca896ff8374ec8c406bf65fda8dc08dbcd9a9` | paired authorized revision/fault conditions; Inspect and pause |
| `docs/TERMINOLOGY.md` | `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c` | Cue/Beat/Room/Actor/Role/Performance/Run |
| `docs/ARCHITECTURE.md` | `d9df8a54ed777bc3e1d9cac52274d09436bdf5ca` | one headless core; presentation nonauthority |
| `docs/ROADMAP.md` | `ef8c82c55682da97f79daaaa53842cf5031c4398` | Stage 0 open; Stage 2 minimal fixture; stages 3/4/6/7 deferred |
| `docs/VERSIONING.md` | `2c8048b3f920de1b896af44c2b168bfd2fac288a` | development state vs exact replay identity; authored attribution |

Also read the own-character home contract, memory protocol and previous Flint Stage 0 analysis. No executable simulation, Node/browser parity test, human playtest, numerical oracle or full checkout validator was run. The outcomes and traces below are **proposed** semantics and falsifiable fixtures, not observed game results.

## 1. Minimal authoritative state and time

Let `S_t` be the **completed-boundary authoritative state** after exactly `t` simulation steps, including the single integer tick `t`, mechanism and world facts, Show Beat/Cue state, active timed jobs, Actor capability where present, player-local observations, command-ID disposition ledger and future Ghost/incident/RNG state only when those capabilities exist. One call `Step(S_t, admitted_inputs_for_t, frozen_rules_and_content) -> (S_{t+1}, ordered_events_t)` is an indivisible logical transaction. Rendering frames, wall time and UI callbacks **never** advance `t`.

All new externally initiated commands must be admitted for the **next not-yet-executed tick `t`**. Record actual effective tick at admission and in replay; wall-clock time and input reception order are not authoritative tie-breaks. The host may collect a batch before `Step`, but cannot sneak a late command into a partially evaluated step. In Stage 2 reject externally supplied future-tick commands explicitly; the Show's previously authored due Cues and existing timed jobs are not external future-command APIs. A future bounded external queue needs an explicit separate acceptance rule.

The Performance has *derived* elapsed/scheduled Beat state as part of `S_t`; it is not a second independently running clock. A Show Cue scheduled for tick `t` becomes a **proposal** at the start of that step, not an immediate mechanism write. A rendered Camera Shot is neither a clock nor a world authority.

**Pause and suspension:** accept a single-player pause/focus-loss transition **at a tick boundary**. If requested during an in-progress computation, finish the atomic `Step` and freeze before the next. While paused, no `Step`, Show advancement, timed Inspect progress, RNG consumption or Ghost regeneration occurs, and resume runs no wall-clock catch-up. Free read displays only previously acquired evidence. New gameplay commands while paused receive a **not-admitted** response (not a burned command-ID gameplay rejection) and may be retried upon resume; previously admitted duplicate IDs return their cached disposition without new execution. A host may record pause/resume in a separate run-control trace, not as fictional elapsed game ticks.

**Snapshot boundary:** authoritative snapshots and state/event hashes refer to whole `S_t` completed ticks. Mid-step state is never a replay/save checkpoint. Stage 2 may deliberately support restart-and-replay only; it does not need a durable save protocol.

## 2. One command meaning and one write owner

A proposal's minimum conceptual fields (names illustrative, **not ratified schema**) are:
- `runId`, `commandId` unique within the trusted issuer namespace, and `effectiveTick`.
- Host-attested `origin` / `issuer` (`player_input`, `show_scheduler`, `actor_policy`, `ghost_policy`), and an independently validated `actingEntityId` where relevant.
- Declared `verb`/`operation`, `targetResourceId`, and bounded arguments; causal lineage `incidentId` where applicable.
- Provenance references: Show Cue ID, Player control/authority binding, Actor policy/Production role assignment or Ghost plan ID as appropriate. **A Play naming an Actor is not authority to submit that Actor's own action.**

The resolver trusts origin only when bound by the host/simulation owner's ingress, not when copied from arbitrary declarative content. The World checks capabilities, ownership, range, mobility, current target state and existing job/reservation against `S_t`. Unauthorised, malformed, stale, impossible, disabled or out-of-range inputs have an explicit terminal receipt with reason; no world mutation. A duplicate previously admitted `commandId` plus identical payload returns the **original** result without a second effect. Reusing the ID with a different payload is a rejection. A not-admitted paused request may use the same ID after resumption, provided no other admitted request already owns it.

One logical **World resource resolver** is sole owner of restraint state and hazards. The Show owns scheduled Cue intent and Beat status. An Actor owns intention and bounded private observations, not arbitrary changes to props or scripted guaranteed Beat fulfillment. The Ghost owns its bounded sensed facts and prospective plans, not access to full `S_t`. Director is a pure precommit eligibility predicate, not an operator. Presentation owns pixels and animation, not damage, mechanism state or observations that were never acquired.

**Prestate rule:** all competing proposals for tick `t` have their permissions/locality/prerequisites evaluated on the same `S_t`, before any one modifies it. Moving into range and operating a device in the same tick requires an explicitly modeled compound/timed action; two independently submitted commands do not gain a hidden sequential benefit from iteration order.

## 3. Complete minimal Step phase proposal

| Phase | Owner and rule | Output / anti-failure property |
| --- | --- | --- |
| **P0 — boundary** | Host admits a frozen finite command batch for tick `t`; paused means do not call `Step` | Stable effective ticks, original duplicate receipts; no wall-clock scheduling |
| **P1 — validate** | Resolver checks identities/permissions, actor/target eligibility, locality and prestate capabilities; progresses preexisting jobs with declared completion ticks | Valid proposals or reasoned rejections; no world writes yet |
| **P2 — scheduling / emergency** | Show proposes due Cues from `S_t`. Valid Fifth Bell request is acknowledged as a prospective Show cancellation; suppresses **new, not yet committed** due Cues for this tick, not earlier physical effects | Cue candidates and explicit skip reasons; Bell does not teleport anyone |
| **P3 — adjudicate** | Resource resolver groups target-writing proposals by resource, validates preexisting reservation and conflict policy against `S_t`. Future Ghost candidate must pass perception, precommit Director gate and affordability **before** it may win | At most one allowed operation per resource/tick; all losers get explicit outcome |
| **P4 — commit and resolve World** | Winner's authorized operation and any already-in-flight world effects execute once; Ghost debit occurs **here** on first actual committed win, never for a veto/conflict; deterministic world consequences and causal IDs recorded | One authoritative restraint result; injuries and loads persist, including after Bell |
| **P5 — observe** | Timed Inspect completing at the new boundary samples permitted physical evidence of the post-P4 World; local actor/ghost sensory projections are computed from their own scopes | New observations can inform **next** tick's intentions, not retroactive choices in tick `t` |
| **P6 — Show/outcome** | Show consumes resolved world/actor events to complete, miss, hold, substitute or cancel Beats; applies accepted Bell cancellation without undoing harm; future incident settlement/regen obey separate gated policies | No forced Actor puppet action; no extra Cue firing in same tick from new Show results |
| **P7 — publish** | Advance to `S_{t+1}`; canonical event ordering and state hash, one completion boundary | No mid-tick save, duplicate external outcome, render-origin mutation |

P0 and pause are host-boundary operations rather than second simulation time. P2 Bell suppression is a **proposed** explicit same-tick rule; if rejected, the owner must choose another rule before implementing G1-08. The above phases can live in **one function/module** for the toy. They are logical semantics, not a package plan.

### Conflict decision C1 — fail-closed contention (preferred)

For each resource/tick:
1. If a previously valid timed operation holds an explicit exclusive reservation spanning this tick, its completion remains eligible; incompatible newcomers reject `BUSY`.
2. If exactly **one** fresh admitted write intent is eligible, it alone applies.
3. If two or more **distinct** fresh eligible write intents contend for the same exclusive control (even if their requested resulting value matches), apply **no** fresh write this tick. Publish one resolved resource outcome `CONTENDED_UNCHANGED` with each command's individually rejected/contended disposition. A due Show Cue records missed/contended, not hidden success. Normal physical world evolution continues.
4. Independent read-only observations are not resource writes. An actual compound mechanism requiring multiple compatible commands needs an **explicit authored combination rule** later; do not merge commands simply because their effects appear equal.

This provides **one authoritative resolved resource transition result**, potentially an unchanged state, not two competing writes. It avoids priority integers, arbitrary issuer favoritism, random selection and module-iteration tie breaks. **Cost:** a same-tick safety intervention may fail when another action contests the same control. Therefore the fair-warning test must show an earlier reachable mitigation interval or an alternative genuine escape/stop. If that cannot be provided, choose a documented stable precedence mechanism before claiming the hazard fair; do not secretly add one only in a lethal case.

**Alternative C2 — explicit fixed policy:** specify a domain-owned and testable priority order for whole operations (e.g. a physical emergency interlock may preempt a scheduled Cue). Such a rule can improve last-moment safety but adds policy decisions, exceptions and potential automatic safety advantages. Treat it as a *mechanism's declared physical property*, not universal Player > Cue > Ghost precedence or a source-type priority integer. Do not claim C2 is implemented or approved.

## 4. Inspect: observation is not authority

A local `Inspect` request admitted at tick `t` begins a timed job with named `inspect_duration_ticks` (positive integer ticks; no value is adopted). Its completion boundary is `S_{t+d}`. The observation is derived from accessible World state **after the resolution of step `t+d-1`**, including any Cue that fired during the interval. It is not a snapshot from Inspect start, a hindsight cause-label, or a UI read that was freely available during pause. Attach `observedAtTick=t+d` and accessible sensor/source to the resulting record; the player can read this acquired record freely afterward.

The contract must specify interruption: for the toy, loss of required proximity/ability or explicit cancellation **fails the job without gaining the new observation**, retaining all elapsed game-time cost; pause merely suspends progress. This prevents moving away during a supposed physical inspection and getting remote knowledge. On same-tick job completion and mechanism mutation, **world transition then observation** wins, by declared phase, not callback order.

Named parameters before Stage 2: `inspect_duration_ticks`, `operate_duration_ticks` if operation is not instantaneous, `cue_deadline_tick` or a named timing-window policy, and player movement/reach units. Default selection policy: **fixture-specific documented values established by pilot feasibility and player evidence**, not hidden universal constants. A missing required timing value fails fixture validation; avoid arbitrary defaults. An immediate operation, if selected, is an admitted tick-`t` intent and can still contend.

## 5. Exact proposed adversarial traces and future gates

All traces assume frozen initial state, unique command IDs, a single mechanism `rig`, and stable effective tick `T`. Expected events are conceptual categories with mandatory causality/reason; JSON wire schemas are intentionally deferred.

| Case | Proposed deterministic result / dependency |
| --- | --- |
| **G1-01 Player Operate + Show Cue** | Both valid, simultaneous, neither previously reserved: `Command(player,CONTENDED)`, `CueAttempt(cue,CONTENDED)`, one `WorldResolution(rig,UNCHANGED)`, then `Beat(missed-or-authored-fallback)`. One settled mechanism result, **zero physical writes**. If an old job holds reservation, it wins and both newcomers receive `BUSY`. Owner must approve C1 as allowed “one resolved transition,” not force an applied mutation. |
| **G1-02 Actor vs Player** | If each has independently validated ability and locality, same-resource conflict yields `CONTENDED_UNCHANGED` regardless of source array order. If Actor is out of range/incapacitated, its intent is rejected first; sole valid Player proposal succeeds. Actor's Role assignment alone cannot authorize action. |
| **G1-03 Actor forgery + duplicate ID** | A Play-origin proposal pretending to be Actor fails `ISSUER_NOT_AUTHORIZED`. Repeated already-admitted `commandId` returns the first recorded receipt, no second World write. Same ID/different payload fails `ID_REUSE_MISMATCH`. |
| **G1-04 Inspect straddles Cue and pause** | Inspect starts `T`, `d` ticks elapse only through `Step`; a Cue changes the rig before `S_{T+d}`. New observation samples the **post-Cue** state at `S_{T+d}`. Pausing or browser suspension freezes progress without wall catch-up; free read reveals no newly unearned observation. |
| **G1-05 borderline Ghost Power** | **Forward-compatibility proposal:** affordability compares cost against `Power(S_T)`; if sufficient and arbitration/Director pass, one debit at P4. Regeneration comes after that commitment, during P6 settlement. Regeneration within `T` cannot retroactively fund an unaffordable attack. Numeric representation and amount tuning belong to Stage 4. |
| **G1-06 privileged Director veto** | Director sees a narrow safety projection, returns `allow/withhold` to resolver, no tactical target or veto reason to Ghost strategy. A withheld candidate never commits/debits. Ghost planning for tick `T` uses previously acquired observations only. Test paired hidden worlds before Stage 4 to ensure veto behavior or logs cannot become a strategy leak. |
| **G1-07 impact with two downstream damage events** | Future Stage 4 ledger: committed `incidentId` links once-only debit and all world-derived child damage events; duplicate delivery/id reuse does not create a second incident, reward or Rage. Settlement policy for partial/shared outcomes remains **Stage 4-gated**; no assumption that two damage events equal two rewards. |
| **G1-08 Fifth Bell + impact** | Valid Bell admitted at P2 suppresses new due Cues and marks cancellation pending. A rig already falling due to earlier committed effects resolves damage at P4. Show receives `BellAcknowledged` and `ShowCanceled` at P6, recording injured Actor; **evacuation remains a physical later action**, not teleportation or undone harm. Distinguish harm from an in-flight mechanism versus a Cue that would first be scheduled this tick. |
| **G1-09 refusing/incapacitated Actor** | Actor cannot submit/execute an impossible action; the Show consumes failure/refusal as an event, uses a specified fallback or marks Beat `MISSED/FAILED/CANCELED`. Any hold has explicit `beat_max_hold_ticks` and fails boundedly at deadline; absent fallback/hold policy, mark Beat failed (do not wait indefinitely). Stage 2 may use only passive performer representation. |
| **G1-10 seal breaks and Power reaches zero** | **Stage 6 hard gate:** do not infer containment solely from `Power==0`. Final binding outcome must depend on **post-World** seal integrity plus an explicit seal-break/zero tie rule selected before binding implementation. No trap state or final settlement is modeled in the mundane toy; acknowledge inability to decide the tie today rather than silently choose. |
| **G1-11 render cadence and unrelated RNG** | Same initial `S_0`, rules/content digests, effective command batch order and simulation RNG streams yield same `S_t` and authoritative events for Node/browser at fixed numeric semantics. Render timing and cosmetic RNG are outside `Step`; future dialogue RNG must not advance Ghost RNG. |
| **G1-12 mismatched hash or midtick continuation** | Refuse replay under a mismatched content/rules hash rather than approximately continue. Replay from `S_0` plus exact admitted input trace is valid; a halfway-through-step checkpoint is **not** a restart point. Full durable checkpoint/resume policy is Stage 7/later persistence work, distinct from re-execution. |
| **G1-13 stale/paused/retry ID** | An unrecognized stale request is explicitly `REJECT_STALE`. While paused, new commands are not admitted (do not burn IDs); retry at resumed tick can be admitted **once** with that same ID and a new effective tick from host. A command **already admitted earlier** returns its cached receipt on retry, never reruns. A future-dated external Stage 2 command is `REJECT_FUTURE_UNSUPPORTED`. |
| **G1-14 cosmetic movement vs unchanged rig** | The renderer may play a declared **nonphysical** effect without claiming a restraint change, but must not silently animate a mechanically significant rig transition or injury when `WorldResolution(rig,UNCHANGED)`. A physical Show Cue must resolve via World; if it failed/contended, the presentation shows failure/uncertainty rather than fake success. Snapshot/event semantics, not animation frame order, drive visible physical state. |

**Important limit on G1-01:** If Mothlight interprets “exactly one resolved mechanism transition” as *exactly one successful actuator write*, C1 intentionally differs: it produces one **adjudicated final mechanism state**, potentially unchanged. That is a deliberate, falsifiable alternative requiring owner selection, not a disguised agreement.

## 6. Ranked findings and changes recommended

### CRITICAL C1 — No total same-tick actuation rule yet
**Sources:** `docs/reviews/STAGE0_RECONCILIATION.md` R-01 and temporal requirements; `docs/contracts/V0_PLANNED_CONTRACTS.md` C00/C01/C02/C07. Until collision outcomes are selected, two internally reasonable modules can both write the rig or produce different results by callback order. **Fix:** one resource adjudication function, prestate validation and a declared C1/C2 tie policy. This is the smallest coherent obligation, not an architecture of source priority tables.

### CRITICAL C2 — Inspection evidence timing still lacks a completion boundary
**Sources:** R-03/R-11; contracts C03/C10; `STAGE2_JUDGMENT_EXPERIMENT.md` information/causality rules. A UI may accidentally reveal post-Cue state immediately or sample stale pre-Cue state when Inspect straddles a Cue. **Fix:** tick-based jobs, post-step completion observation, stamped acquisition and frozen pause. Preserve deliberate ambiguity, not arbitrary guessing.

### CRITICAL C3 — Required Beat / Bell cannot retroactively force World truth
**Sources:** R-12/R-13; contracts C01/C06/C07; roadmap Stage 3. A script that forces incapacitated performance, a Bell that undoes injury or a forever-pending Beat violates independent World/Show authority. **Fix:** Show consumes resolved events; finite fail/fallback paths; Bell acknowledges and cancels prospectively, not physical rescue.

### IMPORTANT I1 — Keep issuer identity separate from narrative role
**Source:** R-02 and C01. A Play naming an Actor does not authenticate an Actor command. Treat origin binding and command ID as ingress concerns; no full multiplayer auth framework required for a single-player toy.

### IMPORTANT I2 — Ghost eligibility before debit, and effects before settlement
**Sources:** R-05/R-06/R-07 and C04/C05. Ghost/Director may be separate decision policies but must share **one** World commitment point. Preserve one debit and causal IDs. **Defer** detailed Rage, partial rewards, binding and Ghost action tiers.

### IMPORTANT I3 — Replay identity is broader than a seed
**Sources:** R-09/R-10, C11, `docs/VERSIONING.md`. Same seed with changed content, rules, numeric model, admission batch or PRNG ordering is **not** same replay. Record canonical effective inputs and frozen identities before supporting the first headless comparison. A human `SF-0004` label is a planning version, not an authoritative replay hash.

### OPTIONAL O1 — Do not create the full conceptual module inventory
**Sources:** `docs/ARCHITECTURE.md` and roadmap Stage 2. Make one world/state step in `packages/core` and a renderer adapter later; Show, Actor, Director, Ghost and observation are logical responsibilities. Separate packages or plug-in schemas are not required by their distinct ownership.

### OPTIONAL O2 — Do not introduce numeric priority scores
A transparent contention result is enough for the first toy. If future hazard fairness demands priority, add it as a named **physical mechanism interlock** with its own negative test, not an invisible universal role ranking.

## 7. The smallest proof versus deferred obligations

**Stage 2 minimal toy:** one Room, one rig state, one Cue schedule, one actor-free passive Beat, player Move/Inspect/Operate/Refrain, paired legitimate revision/fault fixtures, single tick/step, command ID validation, timed observation, pause, explicit conflict and cue failure, canonical event trace. No Ghost, Rage, Director controller, Actor planner, dialog generator, full save, general content loader or art packs.

**Stage 3:** independent Actor intentions/knowledge; explicit mandatory Beat fail/hold/alternate; Bell request/cancellation vs physical evacuation. The partial future rules above are boundary tests, not a requirement to ship cast AI in Stage 2.

**Stage 4:** Ghost sensory projection, precommit Director gate, Power debit/regen, one causal incident, settlement/reward/Rage. Stage 2's arbitration need only accept *another validated source* without a new World owner.

**Stage 6:** binding/seal-break/Power-zero tie with explicit outcome table; do not fake a rule today.

**Stage 7 / persistence work:** alternate Adventure compatibility, stronger replay numerics, durable completed-tick saves and non-destructive restore. The one-Room toy can be restart-only if disclosed. Different presentation styling cannot change authoritative inputs or events.

## 8. Proposed negative tests (NOT EXECUTED)

| Fixture | Exact expected evidence |
| --- | --- |
| **T1 same-tick permutation** | Player+Cue in either input array order yields identical `CONTENDED_UNCHANGED`, accepted/rejected IDs, Show missed status and world hash; reversing callbacks cannot pick a winner. |
| **T2 different issuer same command ID** | IDs are scoped by validated issuer; spoofed Actor origin fails, identical admitted retry returns cached response, changed payload with old ID rejects. |
| **T3 Inspect completion** | D-tick Inspect begun before Cue observes post-Cue state only at `S_{t+D}`, not during progress or pause; moving out of reach cancels without an acquired fact. |
| **T4 pause/focus** | Repeated renders and elapsed wall time while paused do not advance `t`, RNG, Ghost resources, Show deadlines or Inspect job; resume has no skipped ticks. |
| **T5 Bell/harm** | Previously committed falling rig still injures Actor on Bell tick while Show cancels; a newly due Cue suppressed by Bell does not begin new harm. |
| **T6 bounded Beat** | Refusing/incapacitated Actor produces fallback or explicit failure by declared deadline; no infinite hold or scripted puppet completion. |
| **T7 cosmetic mismatch** | Presentational animation cannot create world restraint delta, hazard, injury or private observation; physical Cue contended/failed does not render as physical success. |
| **T8 source addition** | Inserting one future Ghost/Actor candidate using identical World interface does not change player/Cue outcomes in a no-Ghost/no-Actor run. |
| **T9 browser/headless** | Pin exact rules/content, effective commands, PRNG and numeric semantics; two supported hosts yield identical completed-tick event/state digests independent of rendering cadence. |
| **T10 fair timing** | For a hazardous scenario, reachable observation+travel+effective operation fits the authored warning window **or** the scenario explicitly declares an earlier informed exposure/escape; a “warning=true” flag alone fails. |
| **T11 malformed recovery** | Future-tick request rejected, stale request rejected, paused request not admitted, accepted resend idempotent; invalid checkpoint or content hash never produces a false resumed game. |
| **T12 prospective Ghost** | Borderline Power, veto and duplicate incident prove no unauthorized debit, no regen-before-affordability, no private-data leak and no multiplied reward when Stage 4 is separately authorized. |

**Feasibility evidence** would be the ability to describe all T1–T7 on one sheet with one World owner and bounded state transitions. **Determinism evidence** would be exact re-execution, permutation and cross-host trace equivalence. **Fairness evidence** is *separate*: player-accessible cues, reachable interventions, comprehensible consequences, and later blind human trials; determinism alone cannot prove the player could have known what to do. No measurements are asserted here.

## 9. Unresolved dissent and conditions for changing my mind

- **Dissent:** I do not recommend privileging Show Cues or Player operations merely because their source sounds authoritative. Authorship of a Cue is permission to request a World operation, not to win every collision. C1's contested no-op is intentionally austere. If timed human play exposes it as arbitrarily punitive or a legitimate safety mechanism must physically preempt a Cue, adopt C2 for that named mechanism **with one canonical guard**, not a global priority ladder.
- **Potential simplification trap:** C1 may unfairly defeat a last-possible-tick player rescue. That is not solved by saying the game was deterministic. The Stage 2 experiment must test warning/response windows and revise C1 if the physical model warrants priority. This is an explicit regression risk in my favored design.
- **Unchosen timing values:** inspect/operate durations, reach geometry, Cue window, Beat hold bounds and host input buffering need fixture-specific named units/default selection policies and test evidence. None is ratified here.
- **Unsettled later rules:** Ghost partial reward/Rage, settlement under multiple causes, exact numeric representation, binding-zero/seal-break precedence, durable saves and multiplayer authorization remain later-gated. Do not treat these omissions as implicitly decided by a Stage 2 toy.
- **Changes would affect** `docs/reviews/STAGE0_RECONCILIATION.md` Gate 1 follow-up or a new design decision, `docs/contracts/V0_PLANNED_CONTRACTS.md` C00/C01/C02/C03/C07/C11, and `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` timing/collision examples; `docs/ARCHITECTURE.md` only if a clarified owner diagram is needed. **No change to these files is made here.**

**Recommendation to Mothlight:** Adopt the single-step owner/phase boundaries; choose and document C1 versus C2 explicitly, with player-warning fairness as the discriminating test; pin Inspect completion-time semantics. Then retain every future subsystem as a producer/consumer of the **same** World transition, never another writer. A compact phase table plus the G1-01/04/08/09 negative fixtures is enough to close the relevant *design* part of this Gate without building its runtime.

## Revisit when

Mothlight selects the source-pinned Gate 1 phase/tie rule and records its reason; the future Stage 2 one-Room prototype tests same-tick contention and timed evidence; a justified emergency interlock exposes a failure in C1; or the owner separately commissions Stage 4/6 Ghost or binding settlement. Preserve this first pass and its stated tradeoffs during reconciliation.

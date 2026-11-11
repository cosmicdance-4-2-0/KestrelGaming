---
schema: 1
id: 2026-11-11-stage-fright-g1-axiom-authority-9c3d
kind: decision
scope: agent:axiom
status: active
evidence: inferred
author: axiom
created: 2026-11-11
updated: 2026-11-11
sources: "STAGE0-G1-AUTHORITY-01/AXIOM issue #12; immutable Mothlight handoff MOTHLIGHT_GAME1_STAGE_FRIGHT@e538b19c781d28e7c0754cb8438f401b3b93efd3; all seven specified source inputs at game@107ae2b446405d225feac01595e9ead08d679bde; individual home KestrelGaming agents/axiom-v1@f7f7dbf665be89c7957621d255f148ab7d175a19; prior Axiom Stage 0 review f7f7dbf."
---

# Axiom — Stage Fright Gate 1: Authoritative transition and conflict arbitration

**Assignment:** STAGE0-G1-AUTHORITY-01/AXIOM  
**Review type:** Independent, source-pinned, design and falsification only  
**Individual source:** Axiom — The Geometer; `cosmicdance-4-2-0/KestrelGaming` `agents/axiom-v1@f7f7dbf665be89c7957621d255f148ab7d175a19`  
**Pinned game source:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT@107ae2b446405d225feac01595e9ead08d679bde`, SF-0004 (not floating main)  
**Individual assignment:** [Issue #12](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/12); [immutable Gate 1 handoff](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/e538b19c781d28e7c0754cb8438f401b3b93efd3/docs/reviews/STAGE0_GATE1_AUTHORITY_HANDOFF.md).  
**Own verdict:** **ACCEPT WITH CHANGES** — adopt the single-tick/one-world-authority direction but **hold ratification** until conflict ties, effective-time semantics and terminal observations become executable paper rules. No gameplay implementation is authorized or claimed.

## Summary

**The invariant:** For one completed authoritative tick, **exactly one world transition authority** resolves all eligible physical intentions into a single reproducible state/event history. Player, Show, Actor and Ghost can separately propose behavior, but cannot each own the result. An observed Cue, wound, warning or Beat outcome must trace to the same resolved world truth.

**Recommendation:** Use a **sealed-tick, batch-arbitrated transition** with explicit target/control conflict rules, pre-existing-effect precedence, post-world Show settlement, and next-tick observation visibility. Do not use module invocation order, arbitrary actor-ID ordering or a universal “player always wins” policy to decide physical truth. The design's hardest decision is not how many phases to create but which apparently simultaneous actions have already become irreversible. Mark that boundary explicitly.

The selected mundane Stage 2 experiment needs only the clock, authenticated player/cue source, bounded timed operation, mechanism resolver, observable result, pause rule and a finite Beat outcome. Ghost economy, Actor psychology, full saves, a generalized command bus, a separate Show clock and production content loader are not prerequisites.

**Independence:** I read my own Axiom identity/common protocols, my own prior source-pinned Stage 0 report and the seven prescribed SF-0004 files. I did **not** open, query or read other agents' **new Gate 1 responses** before writing this report. SF-0004's pre-existing six-agent *reconciliation* was an expressly mandated source; it is not a new Gate 1 response. Shared GitHub account authentication is not an agent-instance certificate.

## 1. Source record and status

| Source at immutable game baseline | Git blob SHA | Reason |
| --- | --- | --- |
| `docs/reviews/STAGE0_RECONCILIATION.md` | `d7acb5cc172d6e2017f8fd3f7566feedcd16861f` | R-01 one tick, R-02 command provenance, R-11 pause, R-12 Bell, R-13 Beat; expressly *not* a total phase algorithm |
| `docs/contracts/V0_PLANNED_CONTRACTS.md` | `1c03e5e94983e28e263b5278b5d77533deefcbd6` | C00/C01/C02/C03/C04/C05/C06/C07/C11 and remaining gates |
| `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` | `8ffca896ff8374ec8c406bf65fda8dc08dbcd9a9` | One Room, ordinary revision-versus-fault pair; no Ghost runtime |
| `docs/TERMINOLOGY.md` | `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c` | Cue/Beat/Actor/Role/Room/Performance/Run distinctions |
| `docs/ARCHITECTURE.md` | `d9df8a54ed777bc3e1d9cac52274d09436bdf5ca` | Headless/core vs presentation; no gameplay implementation |
| `docs/ROADMAP.md` | `ef8c82c55682da97f79daaaa53842cf5031c4398` | Stage 0 gate versus Stage 2 narrow proof and later Stage 3–7 |
| `docs/VERSIONING.md` | `2c8048b3f920de1b896af44c2b168bfd2fac288a` | ChangeID and actual integration are human-authorized; a review is not an SF build |

**Established planning requirements** at SF-0004: fixed-step single authoritative world, progressing Show derived from ticks, bounded-sense Ghost and precommit Director gate, time-consuming local actions, no silent stale/duplicate effects, nonauthoritative render, physically meaningful Bell, finite Beat outcomes. **This report's phase table and conflict rule are new proposals**, not SF-0004-approved interfaces or tests already performed.

## 2. Canonical ownership and one-step interface

The minimum abstract operation is `F(S[t], Inbox[t], ContentPin, RulesPin, RngState) -> (S[t+1], Events[t], CommandReceipts[t])`, with **all** data inputs frozen at the tick seal.

`S[t]` is the **completed** state before tick `t` (all of tick `t-1` settled). It owns:

- one integer `nextTick=t` and active/terminal run state;
- World entity positions, affordances, mechanical modes, restraints, loads, damage and pre-committed effects;
- Show position, due Cue identities, finite Beat status and pending authored contingencies;
- authorized actor identities/control capabilities, timed action progress and effect completion ticks;
- acquired observation/knowledge states per observer, including their availability ticks;
- applicable Ghost Power/Rage/observed-memory and Director policy state **later**, without making the Ghost the world writer;
- replay PRNG state, idempotency/causality ledger and pending incident state needed for exact restart **later**.

**State owners:**

| Concern | Canonical author of proposals | Only legal state writer |
| --- | --- | --- |
| Clock and admission | Host provides inbox, pause gate, trusted issuer evidence; Core seals effective tick | Core transition (`t`, accepted/rejected receipts) |
| World and injury | Player, Cue, Actor and Ghost intentions | World resolver, via one conflict/hazard procedure |
| Show/Cue/Beat | Play/Production proposes scheduled Cue and Beat obligations | Show reducer **inside the one core step**, consuming world-resolved events |
| Actor | Actor policy proposes locally permitted intentions | Core validates ability/physical effects and publishes resulting Actor state |
| Ghost/Director | Ghost strategy proposes; Director filters precommit | Core validates affordability, commits once, resolves world effects and later settles rewards |
| Presentation | Reads committed snapshots/events and already-acquired evidence | **No authoritative writes**; may create new *commands* for a later tick |

**No circular ownership:** The Show can propose a Cue based on `S[t]` and use world results to change its Beat **in the same step**, but it never directly changes the restraint. It does not regenerate a new Cue from a just-computed Beat until `t+1`. Actor/ghost perceptions produced from `Events[t]` similarly affect their decisions **no earlier than `t+1`**. A single step may execute internal phases; the partially updated intermediate state is neither a published snapshot nor an input to competing autonomous planners.

**State and event boundary:** Emit one final immutable `S[t+1]` and an ordered `Events[t]`. Keep internal provisional candidates private. Report accepted, suppressed, coalesced, conflicting, stale, invalid and completed statuses explicitly; “attempted” is not “effect applied.” Event IDs/ordering are determined from a fixed phase order plus stable canonical keys, never object traversal/hash-map order. A single control facet has at most one **resolved requested actuation** in that tick; world damage may independently affect other facets via a causally attributable physical consequence. This is not “one global state write for the whole game.”

## 3. Proposed sealed-tick phase contract

**Phase P0 — Pause/host admission frontier.** A step can begin only while running, after the previous step completely commits. A pause or loss of browser focus takes effect **at the completed-tick boundary**, never in the middle of an observable half-transition. While paused/suspended: `t`, timed actions, Show, Ghost regen, PRNG, new observations and event trace do not advance. No wall-clock catch-up. Commands arriving while paused get a truthful **not-admitted / PAUSED** response without consuming an authoritative ID or applying effects; a valid resend after resume can be admitted. Read-only access can display only already-acquired observations. Duplicate resends of a formerly accepted ID return its original recorded receipt.

**Phase P1 — Seal and validate.** The host supplies a finite, unmodified inbox for effective tick `t`. Verify that trusted origin/issuer is permitted to request acting-entity behavior, target/verb exists, request is in the same Run, target is reachable where relevant, task/ability/range holds, and declared deadline/effective tick has not expired. Validate a command at **admission** and again at **completion** for changed physical preconditions. Invalid/stale/unsupported submissions generate explicit rejection receipts; never mutate an action because of a forged Play field. A genuinely **new** future-dated command is **not admitted** in the first slice; the host may resubmit for its future tick instead of requiring a hidden arbitrary queue. Duplicate exact command identity/payload returns prior outcome, even after pause; same identity with different payload is `DUPLICATE_MISMATCH` and cannot gain a second effect. A batch supplied in another iteration order must yield the same result.

**Phase P2 — Mature already-committed consequences.** Effects committed in *earlier* ticks whose irreversible completion is due at `t` resolve from their declared state and relevant physical constraints **before newly completed interventions can pretend to prevent them**. Damage and injury become ordinary world facts with causal references. Already-committed effects can have predeclared interrupt windows; an action completed *before* the last effective cutoff may stop them, but an act first becoming effective at the impact tick cannot silently undo past commitment. If a mechanism has an earlier material cutoff, author it as data, not a magic tick priority. This phase ensures Bell and last-second operations do not rewrite injuries.

**Phase P3 — Collect candidates, no mutation.** Generate due Show Cues from `S[t]`, completions of previously admitted timed player/Actor operations, and future Ghost/Actor intentions from their respective permitted **pre-step** knowledge. Starting a new physical operation at tick `t` records a pending timed operation; it cannot “complete” at `t` merely because UI submitted it late. A defined `durationTicks` (positive integer configured per action/fixture) establishes its completion tick. An expressly instantaneous operation, if ever required, must be separately specified and time/fairness reviewed. Show does **not** fabricate an Actor command by naming a Role. If a prior irreversible effect incapacitated an acting entity, completion preconditions are now rechecked and may fail.

**Phase P4 — Authorize and arbitrate by target facet.** Validate each candidate's authority and current physical preconditions. For each control facet, choose at most one compatible operation (or one coalesced idempotent effect) by the **fixture's published control policy**, described below. Candidate order cannot change the winner. Rejected/overridden/conflicted candidates receive typed outcomes and their causal IDs remain traceable. Future Ghost intentions are only *tentative* before legality, Director precommit eligibility and arbitration have succeeded; no debit or warning is created for a refused proposal.

**Phase P5 — Apply resolved operations and consequences.** The world applies selected actuation, state transitions and eligible downstream discrete hazards deterministically. Required warning/evidence timing is part of an authored hazard lifecycle. Damage, safety, actor ability, props, cue effectiveness and observations reflect **actual state**; neither a Ghost module nor the Show performs injury writes. Causal events reference the selected root action and consequences. A lethal consequence cannot be justified by a warning emitted only after the last meaningful response opportunity.

**Phase P6 — Settle Show, emergency and local observations.** Consume `Events[t]` and post-world Actor ability. Advance/expire Beat obligations, select authored contingency/hold/failure, and apply any effective Fifth Bell request to cancel subsequent production obligations **without undoing world events already settled**. Record Bell acceptance/acknowledgment, Show cancellation and physically achieved evacuation as separate transitions/results. Timed Inspect completing at `t` captures an authorized **post-resolution** local observation and stamps `availableFrom=t+1`; no player/Actor/Ghost policy uses it for another decision already resolved at `t`.

**Phase P7 — Publish and seal.** Persist the completed tick's authoritative event order, command receipts/identity ledger, pending timers and PRNG evolution; publish `S[t+1]`. Renderer, accessible UI and future headless replay may observe this finished boundary. The next tick cannot start until this one finishes. An optional durable save may later persist **completed** boundaries; Stage 2 can remain restart-only.

**Important tradeoff:** P2 conservatively prevents a same-tick “miracle rescue” of a previously matured impact. This is an explicit *proposed temporal rule*, not metaphysical truth: a game designer can choose later cutoff semantics for a specific hazard if a physically meaningful earlier preparedness window supports it. The rule must be visible, testable and consistent across player and NPC actions.

## 4. Arbitration table — no global source priority integers

A mechanism's **declared operation mode** defines ordinary automation, permitted manual override and physical interlocks. This is an explicit capability of the controlled fixture, not an invented rank of Player over Actor over Ghost.

| Candidates effective at `t` | Proposed resolution / event | Required state premise |
| --- | --- | --- |
| A single valid operation, no competing actuation | Apply once; `OP_APPLIED` | Correct target/ability/locality, time fully paid |
| Due automatic Show Cue + one valid manual operation | **Manual operation supersedes** the automatic command if that mechanism explicitly supports manual override; log `CUE_SUPPRESSED_BY_OVERRIDE` and `OP_APPLIED`. Otherwise manual is invalid for that mode and Cue may apply | Control supports documented override; manual work completed by `t` |
| Two contradictory valid manual operations with no established exclusive operator | Both `CONFLICT_TIED`; **no actuation**; mechanism holds prior mode. Due lower-precedence Cue is also suppressed for that facet, and Show sees a missed/blocked Cue | Valid at prestate; neither source has a prior state-backed exclusive control lease |
| Two equivalent **idempotent** commands to the same final state | One canonical effect, both commands attributable (`COALESCED`), never two mechanical changes | Semantic equivalence and idempotence independently defined for that verb; otherwise treat as conflict |
| One operator holds a previously established exclusive control claim | That operator's otherwise-valid action can proceed; conflicting commands denied by control permission, not sorted by actor name | Claim was **already in committed `S[t]`**, not invented mid-tick |
| Interlock prohibits all proposed actuation | Reject all relevant candidates and emit inspectable reason; no state change | Interlock is a world-owned physical prerequisite |
| Command would operate a destroyed/inaccessible control | `PRECONDITION_FAILED`; no effect | Revalidate at completion, including already-matured physical damage |
| Physical impact due from earlier tick, Bell or operation newly effective `t` | Already committed impact resolves in P2; later command cannot erase it | Impact's authored last effective intervention time is before `t` |

**Priority is local and semantic**, not a globally hardcoded order. A manual operator is *not always* authorized: an Actor and the stagehand can both have valid local manual access, and their conflict is real gameplay, not arbitrated by player bias. **A valid request does not guarantee application.** An authored control may declare a different policy only with the same explicit, testable total tie behavior and without contradicting headless causality.

**Alternative B — sequential total-order application:** Sort every effective intent by `(tick, source tier, target ID, command ID)` and mutate in that order. Advantage: trivial to implement, easy deterministic replay. Disadvantage: “last writer wins” becomes gameplay policy, can allow Ghost to override successfully completed prevention, makes actor IDs a hidden power structure and may double-trigger intermediate hazards. A fixed total order solves nondeterminism **but not coherence**.

**Alternative C — commutative merge/transactions:** Require independent effects to commute, or use optimistic locks/conflict detection and retry. Advantage: scalable multi-entity effects and future concurrent clients. Disadvantage: additional transaction semantics, conflict retries, unintended second attempts, opaque ownership and complexity without Stage 2 evidence. **Defer**, except for the simple one-target batch conflict logic above.

**Recommendation:** Select A's batch rule for the one-Room toy; preserve a future path for other mechanism-specific arbitration policies only after demonstrated content needs. Do not implement a generic transaction/event-sourcing framework at Gate 1.

## 5. Detailed adversarial trace decisions

Each trace is a **paper proposal**, not an executed test. `E[t]` is the ordered authoritative event set for tick `t`. Event names are descriptive labels, not approved API enums.

### G1-01 — completed Player Operate collides with a legitimate Cue

**Fixture:** At `S[t]` the chandelier mechanism is operable and declares manual override. A legit Show Cue requests `release_for_rehearsed_sway` due at `t`. A physically situated player completed the configured `brace_restraint` action, initiated early enough to become effective at `t`.

**Expected trace:** P3 `CUE_DUE(CueID)` and `OPERATE_READY(commandID)`; P4 `OP_APPLIED(brace)` and `CUE_SUPPRESSED_BY_OVERRIDE(CueID,commandID)`; P5 restraint remains braced, **no second release**; P6 Show records the Cue as missed/overridden and enters an authored finite contingency/hold/failure, not “delivered.” Same input permutations produce identical E[t]. If the player only **starts** timed Operate in tick `t`, it is not ready: Cue executes and any later operation sees the updated mechanism. A different published control mode may disallow manual override and must declare it visibly.

### G1-02 — Actor and Player submit contradictory valid manual operations

Both are locally authorized and complete at `t`, one `SET_LOCKED` and one `SET_RELEASED`, and no exclusive operator is recorded in `S[t]`. Both receive `CONFLICT_TIED`; no actuation occurs; the mechanism holds prior state. A due automatic Cue on the same facet is suppressed and receives a blocked-Cue result. **No object iteration order, Actor ID, human/nonhuman source tier or random tie-break decides the winner.** A separately modeled pre-established control claim could authorize one, but may not be acquired retroactively during this collision.

**Dissent/tradeoff:** Failing closed can interrupt the performance, and coordinated Actor+Player changes might become frustrating. That is a real design cost to test; an alternate explicit operator-lease policy may be simpler for a specific control. What is unacceptable is unexplained apparent success for both requests.

### G1-03 — content attempts issuer impersonation; duplicate command ID

The Play may emit its own bound Cue **request**, not `issuer=actor:Mara`. An envelope with content-origin issuer impersonating Mara is rejected `UNAUTHORIZED_ISSUER` before action generation. Two submissions with the same `(Run, trusted issuer, command ID)` and exactly equal normalized payload: return the **original receipt**, emit no new world transition. Same identity with different payload: `DUPLICATE_MISMATCH`, no second effect. A replay source that forges a trusted-issuer field never authenticates itself merely by choosing a string.

### G1-04 — timed Inspect straddles Cue; pause/focus loss

An Inspect admitted before `t` is scheduled to complete at `t+k` per named `inspectDurationTicks`. A Cue occurs on an intermediate tick. Pausing or host suspension stops progress **between completed ticks**, including the Show; wall time changes nothing. After resume, Inspect completes only after its remaining simulation ticks. It reports the legally inspectable **post-resolution** mechanism observation at completion tick `u`; the observation enters personal knowledge at `S[u+1]`. The player cannot use information from `u` to override a Cue at `u`. A paused UI may reread notes already acquired, not inspect a newly changed mechanism.

### G1-05 — Ghost borderline affordability at regeneration boundary (future Stage 4)

**Provisional resource ordering:** On tick `t`, apply the deterministic, capped regeneration increment exactly once to the available Power account (using `S[t]` Rage and elapsed simulation tick), then evaluate prospective legal plan affordability **against that post-regeneration balance**. Director precommit eligibility and target arbitration follow; only a fully eligible **winning committed** Ghost action pays exactly once. If balance equals action cost, it may commit and reach zero. If Director vetoes or the plan fails precommit conflict, **no debit**. Once committed, later thwarting does not refund the debit. Publish exact account changes and root incident ID; Stage 4 must ratify numeric representation, tick/rate units and payout policy.

### G1-06 — safety-only Director veto (future Stage 4)

The Strategist sees only a configured observation projection. Director returns `ALLOW/DEFER/VETO` against the *specific proposed plan*, with no target rewrite and no counterplan. Privileged safety detail and veto rationale are kept in authoritative audit output, **not Ghost tactical memory**. More subtly, the Ghost must not learn hidden safety facts **from repeated allow/veto decisions** through a plan-selection feedback loop: it may know an action did not commit, but cannot treat privileged veto classification as a new observation or choose a privilegedly inferred target. Design/test this side-channel rather than assuming redaction of one field suffices.

### G1-07 — one Ghost commitment, two damage effects, repeated delivery (future Stage 4)

Root incident `I` is committed and debited once. `DAMAGE(actor)` and `DAMAGE(prop)` carry `causedBy=I` and distinct event identities; repeating either event or reprocessing `I` has **no additional debit or reward**. One settlement owner may later derive a reward from achieved declared goals. Partial success, reward+Rage combinations, incident closure and refund exceptions remain **explicit Stage 4 settlement gates**, not spontaneous behavior by each receiver.

### G1-08 — Fifth Bell effective on same tick as due impact

**Assume** the emergency Bell signal has become a valid, time-paid effective request at `t`; a newly **initiated** physical Bell action is not automatically instantaneous. In P2 an already committed rig impact injures Mara. P6 records `BELL_REQUEST_ACCEPTED`, `SHOW_CANCELED` or its explicitly denied status, and `CAST_STATUS=injured`. Cancellation stops future Show obligations but does not restore Mara, teleport anyone or erase the impact. Separate `evacuation_progress`/`evacuated` follows physical routes later. If the player was already incapacitated **before** Bell activation, signal validation fails; if incapacitated **by the same-tick impact**, a previously valid completed Bell signal is not retroactively unsent. The choice to permit such a coincident signal is proposed and must be made explicit by Mothlight.

### G1-09 — mandatory Beat needs an unavailable/refusing Actor

The Show reads post-world Actor ability and genuine Actor response; it **cannot issue forced movement or lines**. If required Role `R` is incapacitated/refuses, emit `BEAT_BLOCKED(reason,R)`; choose one *authored* substitution if its prerequisites exist, else enter an explicit bounded `HOLD_UNTIL(tDeadline)`, `FAILED` or `CANCELED`. The hold's `maxHoldTicks` and failure destination are authored named values, never implicit “wait forever.” After each completed tick Show has one documented finite next step. A timed hold may be legitimate; an unbounded pending beat is not.

### G1-10 — binding breaks as Power becomes zero (future Stage 6)

**Do not choose a containment winner at Gate 1.** Require one future **world-then-binding settlement** that tests `seal validity` and `Power zero` against a single finished phase snapshot, with a documented tie outcome and no independent Ghost/Binding writes. Exhausted-unbound is never “contained.” The source explicitly defers this race to Stage 6; implementers must not fill the gap by loop ordering. Add a paired test in that gate before any binding action exists.

### G1-11 — rendering cadence / unrelated dialogue draws

Replay identity pins `S[initial]`, exact content/rules digest, ordered admitted effective command records, PRNG algorithm/streams, tick units and a canonical state/event encoding. A renderer can animate at different frame rates, but cannot step or sample authoritative RNG. Cosmetic draws do not share the Ghost decision stream; unrelated dialogue random draws cannot perturb future Ghost choices. Equal logical inputs imply equal post-tick event/state hashes in a **supported Node/browser matrix**, not merely similar screenshots.

### G1-12 — content mismatch and mid-tick continuation

Replaying a trace against changed content bytes with the same human-readable version label returns `INCOMPATIBLE_CONTENT`; never silently replace missing data with current modules. A supposed checkpoint extracted from P3/P5 before P7 (without settled effects/identities/RNG) is rejected as `INCOMPLETE_TICK`. Future valid durable checkpoints include pending actions and incident status **at the completed-tick frontier**. Restart-only Stage 2 is acceptable if disclosed; full persistence and migration remain later-gated.

### G1-13 — stale and paused resend

An incoming command for `t-1` is `STALE`; a genuinely new request for `t+n` is `FUTURE_NOT_ADMITTED` in the narrow first version. No silent retiming. During a pause a new command is `PAUSED_NOT_ADMITTED` and does **not** consume its ID; after resumption it may be **resubmitted with current tick and same ID**. A previously admitted command resent with its original exact identity returns its stored receipt, even if later ticks have passed. A resent ID with changed payload is never an idempotent retry. A host that presents the same command twice to one sealed inbox must produce the same result as receiving it once.

### G1-14 — visual motion with unchanged restraint

A purely cosmetic, explicitly authored `VISUAL_CUE` may animate a harmless sway while restraint remains unchanged, provided it makes no claim of physical release and emits no hazard or injury. But a Cue requiring real mechanical actuation **cannot** be marked successful because PixiJS animated it: absent an authoritative restraint transition, report `CUE_NO_PHYSICAL_EFFECT` and use its Play contingency. Presentation neither creates a `WORLD_ACTUATION` event nor rewrites the hazard trace.

## 6. Critical, important and optional findings

| Severity | Finding and source | Concrete failure prevented |
| --- | --- | --- |
| **Critical / gate blocker** | C00/C01/C02/C07 & reconciliation R-01: distinguish commanded start, effective completion, precommitted impact and observation publication | Same-tick player/Cue writes have order-dependent or retroactively false world results (G1-01/08) |
| **Critical / gate blocker** | C01/C03/C06, R-02: issuer/acting entity and idempotency; source of authority is host/world, not Play text | Script forges an Actor, resend double-operates, two equally valid intents silently “win” by callback order (G1-02/03/13) |
| **Critical / gate blocker** | C07, R-12/R-13: physical Bell/cancellation and finite mandatory Beat outcomes | Cancellation rewrites injury; incapacitated Actor is puppeted; Beat hangs forever (G1-08/09) |
| **Important** | C03/C11, R-03/R-11: timed Inspect, pause and completed-tick records | Free omniscient inspection, wall-clock catch-up, mid-tick fake continuation (G1-04/12) |
| **Important, later gate** | C04/C05, R-05/R-06: affordability/Director precommit/causal incidents | Hidden information leaks, debits on veto, duplicate rewards (G1-05/06/07) |
| **Important, later gate** | C11, R-09: PRNG and exact content identity | Identical run seed diverges under render FPS or dialogue catalog edits (G1-11/12) |
| **Optional** | Build richer control leases, transactions, output channel generalization | Do not build abstractions until one-Room fixture requires them |

### A concrete contradiction to resolve

**“One completed transition” does not mean “only one thing can happen per tick.”** World physics may cause injury, a Player operation may suppress a Cue, and the Show may cancel in the *same resolved step*, all with causal order. The invariant is **one canonical writer and no competing unauthorized writes**, not a single state mutation or one event globally. Freezing every action on a contested facet is conservative but must not freeze unrelated hazards or Show outcomes.

**“Accepted command” does not mean “physical success.”** Return separate admission, readiness, arbitration, world application and dramatic outcome statuses. Without that distinction, the UI can announce a successful brace when the operation was rejected or the impact had already matured.

## 7. Proof sequence, acceptance evidence and deferrals

### First mundane toy / immediate Gate 1 contract acceptance (paper proofs, not executed)

| Test | Fixed setup and adversarial mutation | Required result |
| --- | --- | --- |
| **AX-G1-T01** | Reorder the identical Player/Cue ready-intent input array (G1-01) | Identical authoritative result: manual override wins only when predeclared; otherwise explicit conflict/rejection |
| **AX-G1-T02** | Contradictory Actor/Player commands, swapped invocation order (G1-02) | Tie consistently produces `CONFLICT_TIED` and no control actuation; no arbitrary ID winner |
| **AX-G1-T03** | Forge Actor issuer in Play content, then duplicate a valid command ID (G1-03) | Forbidden origin rejected; exact retry is idempotent; mismatched retry rejected |
| **AX-G1-T04** | Timed Inspect crosses Cue with pause and host-suspension variants (G1-04) | Completed tick count governs cost/evidence; post-tick evidence appears only on next decision boundary |
| **AX-G1-T05** | Impact and effective Bell coincide (G1-08) | Impact preserved, valid Bell may cancel future Show only; no free rescue |
| **AX-G1-T06** | Incapacitate sole required Actor, no authored alternate (G1-09) | Finite declared failure/hold/cancel outcome; never forced performance or indefinite wait |
| **AX-G1-T07** | Change render-frame count and event-list input enumeration (G1-11) | Same source-pinned inputs produce identical logical event/state hash |
| **AX-G1-T08** | Stale ID, duplicated accepted ID, paused not-admitted ID, resume (G1-13) | Stable receipts, no duplicate actuation, no silent timing shift |
| **AX-G1-T09** | Simulate cosmetic sway when world restraint remains braced (G1-14) | Purely cosmetic Cue may animate; physically required actuation cannot be reported successful |
| **AX-G1-T10** | Change valid cue/ordinary-fault fixture while keeping player access and time budget | A reachable inspection distinguishes relevant evidence; act/refrain consequences remain causal and non-arbitrary |

**Mechanical feasibility:** pencil traces, synthetic fixtures and later deterministic headless tests can verify total resolution, causal continuity and non-duplication. **Cross-host determinism** requires real Node/browser execution and exact encoding; it is not established by prose. **Human fairness/fun:** bounded player observation under accessible input modes is a separate Stage 2 study, not certified by headless green tests.

### Later named gates

- **Stage 3:** Actor deliberation under local knowledge, timed intention admission, Show contingencies and nontrivial dialogue; test false Beat puppet success.
- **Stage 4:** Ghost projection/Director safety-only veto, precommit resource ordering, one paid incident, partial/shared settlement and PRNG partition. The provisional G1-05 relationship is not a balance decision.
- **Stage 6:** Binding seal-break/Power-zero tie, forced drain and terminal state compatibility; no fabricated answer now.
- **Stage 7:** Cross-Adventure capability/Production bindings, data validation and alternative Art Packs; do not conflate source/version label with content digest.
- **Persistence/continuation:** Completed-tick checkpoint, pending timers, crash/denied write recovery, incompatibility without data loss, only when scoped. No save framework is needed for a disclosed restart-only toy.

**Named parameters required in any future fixture:** `simulationTickDuration` (time unit, exact integer/timing semantics), `inspectDurationTicks` and `operateDurationTicks` (positive simulation ticks), `maxBeatHoldTicks` (bounded nonnegative ticks with explicit fallback), `hazardLastEffectiveResponseTick` (from physical event scheduling rather than a universal reaction window), and Stage 4 `ghostRegenPerTick`/`powerCost` in an agreed numeric representation. Select values from a bounded one-Room evidence/feasibility pilot, **not hardcoded global magic numbers**. This review does not set defaults.

## 8. Dissent, uncertainty, deletions and compatibility risks

**Dissent A — safe ties may be unfun.** Rejecting two contradictory manual operations avoids hidden priority but may cause repeated Cue misses or allow a legitimate Actor to unintentionally obstruct the stagehand. Mothlight could adopt a per-control state-backed operator lease instead, **provided** its acquisition, expiry and same-tick ownership are explicit. No automatic Player-wins rule.

**Dissent B — the impact cutoff is a creative choice.** Matured-impact-first simplifies truth and Bell history, but it can deny a visually plausible last-moment rescue. If the game benefits from interrupts during physical flight, represent a preexisting interruptible hazard interval in World state and define a genuine last-response cutoff; do not insert a post-hoc exception.

**Dissent C — pre-commit regen is provisional.** Choosing regeneration before affordability makes G1-05 deterministic and supports rational waiting, but a different bounded contract (commit-before-regen) could be valid if selected *before* Ghost implementation and replay pinning. Do not lock the economy today based on one paper trace.

**Dissent D — batch conflict does not need a sprawling event system.** A simple target group, documented tie policy and pure step are enough. The full Game architecture should not be designed from a test fixture's abstract model alone.

**Unresolved:** precise time ticks/units, pause UI intent behavior at process/OS boundaries, hazard spatial geometry, fully fledged Actor concurrent control authority, whether Bell is a timed physical operation or exceptional immediate signal, how to balance punitive collision against stagehand agency, Ghost partial/reward settlement and binding equality. These require later owner/integrator decisions and explicit negative fixtures, not guessed defaults.

**Remove/defer:** second Show time authority, direct Script→Actor mutation, module callback ordering, universal source-priority numbers, global gameplay PRNG consumed by presentation, generic transaction/event-sourcing infrastructure, durable save subsystem for Stage 2, autonomous Ghost implementation, elaborate actor psychology and content editor.

**Affected path proposals (no edits):** `docs/contracts/V0_PLANNED_CONTRACTS.md` C00/C01/C02/C03/C04/C05/C06/C07/C11; `docs/reviews/STAGE0_RECONCILIATION.md` R-01/R-02/R-11/R-12/R-13 appendix or a separate Gate 1 decision with precise supersession; `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` timing/fixture bounds; `docs/ROADMAP.md` later-gate cross-references as necessary; `docs/VERSIONING.md` only upon an authorized accepted integration. The first implementation seam can be a single `core.step` function + deterministic fixture tests, not a new package forest.

**Preserve:** physical stagehand, genuine legitimate Cue and ordinary faults, observable act/refrain consequence, one headless world, Play remaining live and Actors independently capable of refusal, future bounded Ghost with Director gate, nonauthoritative Pixi, multidimensional outcomes and fair emergency cancellation. No review count can override a reproduced counterexample.

## Evidence

**Observed:** The exact issued Gate 1 handoff; exact Axiom issue #12; the seven mandated files at SF-0004, their blob IDs and design status; Axiom's own contract/memory and source-pinned previous first pass. SF-0004 explicitly admits the phase-conflict rule is unresolved. Source documents are planning requirements, not implemented code.

**Proposed/inferred:** The P0–P7 phases, local arbitration semantics, paper event outcomes G1-01–14, time/authority decisions, test oracles and recommendations. **No gameplay tests, user trials, new Ghost/Show system, browser comparison, save/replay run or code build executed** for this task. The record's own remote commit and issue handoff must be verified after writing.

**Task outcome:** **COMPLETE as independent design submission**, pending Mothlight's separate synthesis and human acceptance of Gate 1 contract decisions. No game-repository edits, shared contract ratification, code or another agent's memory changes.

## Revisit when

Mothlight has preserved all six new Gate 1 first passes before cross-reading, an accepted Gate 1 phase-and-tie decision supersedes this proposal, Stage 2 headless/human experiments falsify the timing or fairness assumptions, or later Ghost/Actor/Binding implementation exposes an incompatibility. Preserve this independent first-pass report verbatim; write an attributable addendum for changes instead of rewriting dissent.

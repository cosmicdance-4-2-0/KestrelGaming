---
schema: 1
id: 2026-11-11-stage-fright-gate1-gauge-authority-r11
kind: handoff
scope: agent:gauge
status: draft
evidence: inferred
author: chatgpt-gauge-session
created: 2026-11-11
updated: 2026-11-11
sources: "STAGE0-G1-AUTHORITY-01 handoff MOTHLIGHT_GAME1_STAGE_FRIGHT e538b19c781d28e7c0754cb8438f401b3b93efd3; own assigned issue #14; seven immutable Stage Fright sources at 107ae2b446405d225feac01595e9ead08d679bde (SF-0004); Gauge home pre-report a1afbc2e495eee1f3dfaa925843d4cbbd9d3dcaa; independent theoretical design only, no new Gate 1 peer responses read."
---

# STAGE0-G1-AUTHORITY-01 — Gauge's independent deterministic-transition review

**Authorial perspective:** Gauge — The Witness, operating via a shared human-owned GitHub connection, **not** a cryptographically authenticated independent runtime.
**Requested by:** Mothlight, The Invisible Stagehand, through the human Studio Architect.
**Own issue:** [Stage Fright #14 — Gauge Gate 1](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/14) (issue *body* only; issue comments were not read).
**Shared immutable handoff:** [STAGE0_GATE1_AUTHORITY_HANDOFF.md @ `e538b19c`](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/e538b19c781d28e7c0754cb8438f401b3b93efd3/docs/reviews/STAGE0_GATE1_AUTHORITY_HANDOFF.md).
**Game design source pin:** `107ae2b446405d225feac01595e9ead08d679bde`; planning state `0.0.2.4/SF-0004`. Do not substitute current main.
**Gauge own source home:** `agents/gauge-v1@a1afbc2e495eee1f3dfaa925843d4cbbd9d3dcaa` before this report. Prior own Stage 0 [r10](2026-11-09-stage-fright-stage0-gauge-independent-review-r10.md) used for continuity.
**Task result:** COMPLETE — independent **design-only** handoff; no implementation, schema ratification, code modification or tests of gameplay executed.
**Verdict:** **CONDITIONAL PASS for a minimally executable authority model, with explicit contract changes required before the Gate 1 integrator can ratify a phase/conflict table.** The required changes are not observed runtime defects. Nothing here is binding on Mothlight.

## Summary

The most dangerous ambiguity in this design is a **temporal authority leak**: if a subsystem can spend newly generated Power before it exists, mint a fresh incident for a duplicate consequence, select a conflicting mechanism write from callback iteration order, or publish an observation before its legal completion boundary, the result can be deterministic by accident or unfair by construction. Source SF-0004 correctly requires one authority, but its table is a partial order, not yet a transition function.

**My minimal proposal is a pure, completed-tick transaction** `Step(S_t, I_t, C, R_t) -> (S_{t+1}, E_t, R_{t+1})` with **one owner of all world changes**, one ingress receipt sequence, one timed-action completion boundary, one per-mechanism conflict resolution and independent deterministic random domains. All sources propose *intents*; only the resolver commits effects. For the first mundane experiment, Ghost/Director/Power/incident settlement/binding are disabled capabilities, **not simulated fake systems**. A future Ghost can join the same resolver by the declared eligibility/debit seam.

I choose **pre-tick affordability**: a plan legal at opening `S_t` can commit and debit its opening Power exactly once. Regeneration earned during tick `t` is credited in `S_{t+1}`, never borrowed to pay the commitment in `t`. The alternate "regenerate then spend" is also deterministic but has different threshold behavior; the integrator should choose intentionally. For collision arbitration, the physically motivated precedence is **existing valid exclusive operation claim first**, followed by **simultaneous unreserved conflicting intents fail closed**. This preserves author/actor agency without arbitrary global player-versus-Show priority. A scheduled Cue does **not** magically own the mechanism merely by appearing in the script; a Cue may have a legitimate earlier claim to a physical actuator, but a cue-book line does not impersonate an Actor.

**Most important limit:** a complete mechanical replay with the same inputs is not the same claim as Ghost strategy immunity to independently changed *dialogue random choices*. The former needs **full authoritative trace equality**; the latter needs **mechanical/Ghost projection equality** while dialogue-line IDs may legitimately differ.

## Evidence

### Pinned source receipt

Read in the handoff's specified order, exactly at game `107ae2b446405d225feac01595e9ead08d679bde`:

| Source/section | Blob SHA | Relevance |
| --- | --- | --- |
| [Stage 0 reconciliation: R-01/02/05/06/09/10/11/12/13/17, temporal table](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/reviews/STAGE0_RECONCILIATION.md) | `d7acb5cc172d6e2017f8fd3f7566feedcd16861f` | Adopted planning boundaries; executable sequence *left open* |
| [Planned contracts: C00–C07/C11 and SF-0004 refinements](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/contracts/V0_PLANNED_CONTRACTS.md) | `1c03e5e94983e28e263b5278b5d77533deefcbd6` | State/command/effect/observation ownership and deferred numerical policy |
| [Stage 2 judgment experiment: timed Inspect, revised Cue versus ordinary fault](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/design/STAGE2_JUDGMENT_EXPERIMENT.md) | `8ffca896ff8374ec8c406bf65fda8dc08dbcd9a9` | Minimal first judgment fixture, not full Ghost game |
| [Terminology](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/TERMINOLOGY.md) | `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c` | Cue vs Scene/Shot/Room/Run |
| [Architecture](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/ARCHITECTURE.md) | `d9df8a54ed777bc3e1d9cac52274d09436bdf5ca` | Core alone owns rules; Pixi receives projections |
| [Roadmap: Stage 0, Stage 2/3/4/6, continuation boundary](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/ROADMAP.md) | `ef8c82c55682da97f79daaaa53842cf5031c4398` | No gameplay authority; later feature and experimental gates |
| [Versioning](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/VERSIONING.md) | `2c8048b3f920de1b896af44c2b168bfd2fac288a` | Human ChangeID is *not* replay identity |

Also read the pinned target `AGENTS.md` (blob `8312b4e5876acfa2ec92d670e1e45c2b7bb98d23`) and Gauge's own branch-local individual contract, profile, memory protocol/index and previous Stage 0 review. The reconciliation **names** the first six reviewer sources; I did not open their underlying reports. I have **not** read any other agent's *new Gate 1* issue comments/responses, PRs or memory reports. No code or runtime fixtures were executed. Source dates and historical CI claims are not fresh Gate 1 test evidence.

### Definitions (illustrative notation, not ratified APIs)

- `t` is an integer simulation **boundary index**, not a wall-clock timestamp. `S_t` is the entire authoritative committed state at boundary `t`; `E_t` is the event sequence caused by stepping interval `[t,t+1)`; `S_{t+1}` is the **only newly published state**. A completed tick is the minimum replay/checkpoint boundary.
- `I_t` contains host-admitted, immutable action envelopes effective for tick `t`; due operations and Show Cue proposals are deterministically read from `S_t`, not invoked as separate owner callbacks. `C` is content/configuration pinned by hash; `R_t` is explicitly versioned deterministic random state/counters.
- `issuer` is the actual trusted host/source principal, `actor` is the in-world entity being controlled, `source` identifies player UI / Play scheduler / Actor decision / future Ghost, `command_id` is stable **idempotency identity**, `parent_cause` links antecedents, `incident_id` is minted by the resolver for a committed Ghost plan, and `event_id` is authoritative output identity. These identifiers are **not interchangeable**. The client cannot self-authorize `issuer=Actor` merely by naming the Actor.
- A **reservation** means a previously authorized, still-live exclusive physical action has committed an occupancy/actuator claim as part of state (e.g., a timed operation). This is a mechanism-local concept, *not* an all-purpose lock manager. Claims have duration/tick scope and source IDs and must be replayable.
- A **proposal** can be valid to request but lose arbitration. `admitted`, `precondition-valid`, `committed`, `applied`, `interrupted`, `settled` and `rejected` are separate, inspectable stages; do not reuse the word "accepted" for all of them.
- A **free read** is a UI projection of observations already recorded in participant knowledge at the published boundary. `Inspect` starts a timed local action whose newly gained evidence is available only on completion, never on click/animation.

### Phase contract I recommend (one possible totalization)

| Phase | Owner, inputs and action | Output / causal rule |
| --- | --- | --- |
| **H — host admission, outside Step** | Trusted host binds real `issuer` and actor scope, logs receipt order, validates envelope/ID, translates input to a not-yet-executed **effective tick**, freezes inputs before the step begins. Pause commands are host control, not an in-world action. | Recorded `I_t` and rejected receipts; no world change; never accept a future tick supplied by untrusted content as authority |
| **0 — open S_t** | Resolver reads exact prestate, due timers, previous committed reservations, scheduled Cue proposals, pending terminal/Beat state and one explicit RNG state. | Stable prestate; simulation time is fixed and cannot be advanced by render frame |
| **1 — freeze intents** | Authoritative Show, Actor and player input projections independently propose candidate acts from **S_t**. Future Ghost uses permitted observed history; Director only precommit veto/defer. All proposals carry fixed source/provenance and effective tick. | Deterministically ordered candidate set; no subsystem writes a mechanism or applies damage |
| **2 — validate/commit** | Check ownership, locality, ability, preconditions, action duration, target, existing reservations; for Ghost, compute **affordability from opening Power** and apply eligibility/veto **before** debit. On actual Ghost `COMMITTED` mint one resolver incident and **one charge**. | Accepted timed work/commit records and clean reject/veto reasons; uncommitted Ghost proposals cost nothing; a paid plan can later be thwarted without refund |
| **3 — arbitrate/resolve world** | One mechanism arbiter groups compatible/intended exclusive actuator writes by conflict key and interval; existing valid claims execute first. If no prior claim and ≥2 incompatible same-tick writes remain, reject the conflicting set as `SIMULTANEOUS_CONFLICT`, emit one mechanism resolution/no-op event, rather than choose by callback order. Apply non-conflicting physical events then their discrete hazards with a declared deterministic dependency order. | One final mechanism state and causal event history. **No subsystem may publish its own state patch.** Failed Cue can trigger a later fallback; a failed operation is not a successful world change |
| **4 — consume resolved world** | Show processes authoritative Cue/Beat outcomes and Bell requests; Actor knowledge/perception and the player's newly available observations are derived from the completed world effects, per visibility policy; cue-book revisions remain versioned and effective-tick aware. | Updated performance state and participant-specific observation records; no omniscient causal labels slipped into player UI |
| **5 — end-tick resources/time** | Finalize timed-action counters and completed read-only Inspect observations at the finalized boundary; world-affecting timed Operate completions were already arbitrated in phases 1–3. Apply lawful end-tick regeneration to **next** Power balance only, with exact integer remainder accounting. Ghost outcome reward/Rage settlement is **not enabled at Stage 2**; when Stage 4 exists it occurs after world causes and unique-claim validation, credits `S_{t+1}` only. Binding drain/ties are **Stage 6**. | `S_{t+1}` includes pending timers, claims, duplicate-ID registry, resource balances/remainders, observations and any explicit terminal state. No current-tick action spends end-tick credit |
| **6 — seal publication** | Assign deterministic event IDs/order from resolver decisions, canonicalize `S_{t+1}` and `E_t`, emit hashes and snapshot/observational projections. | Atomic completed-tick receipt. Renderer reads published projections, cannot change state or emit unauthorized observations |

**Timing precision:** `Inspect` started at boundary `t` with named duration `inspect_duration_ticks` completes at `S_{t+d}` after exactly `d` successful transitions, not after `d` animation frames. Its revealed facts are sampled according to a **named** completion-observation policy from that boundary (recommended: committed state `S_{t+d}`); a Cue applied in `[t+d-1,t+d)` is therefore included, a Cue effective in `[t+d,t+d+1)` is not. If paused after `k` transitions, remaining count stays `d-k`; resume performs no catch-up. Remote or impossible Inspect is rejected before a timer begins.

**Conflict precision:** Before adopting `SIMULTANEOUS_CONFLICT`, declare what constitutes a physical exclusive write versus independent read. Competing writes to one restraint—even if each individually valid—are not applied sequentially based on source enumeration; if no earlier valid reservation determines ownership, neither writes. One explicit resolution event is produced (a no-change outcome is a valid world transition). A Cue may have obtained a prior physical reservation through ordinary authority, but its dramatic origin alone confers no exclusive hardware privilege. A human-stagehand intervention must begin early enough to hold a valid claim; it cannot retroactively win solely by being player-authored.

**Tradeoff / genuine counterproposal:** A simpler globally ordered queue can also be deterministic if the trusted host fixes a replayable global admission ordinal and the Cue scheduler explicitly receives its ordinal. That avoids conflicting no-ops but can hide a game-balance rule: one issuer always wins close ties, which may reward command spam or make a safety intervention inexplicably lose. A **predeclared physical actuator interlock + fail-closed equal-start conflict** is preferable for Stage 2. If tests demonstrate that all-conflict-fail-closed creates absurd cue failures, switch to a specified per-mechanism *physical* precedence rule with a genuine state-dependent reason—not alphabetic actor IDs or implicit callback order. No module invocation order is ever evidence of priority.

### Command receipt and pause policy

- Host alone binds authenticated requester/source to the acting entity and authorized actions; the requested actor ID is data. Play authors can create `CueIntent` but cannot create an Actor-signed `Operate` merely by inserting an Actor name. A future Actor decision comes from the authorized Actor policy on its own observations.
- Host mints/validates command identities under a run/source namespace. **Same ID + same immutable request after admission** returns the original receipt and creates no second act; same ID + different payload rejects `ID_REUSE_CONFLICT`. A failed pre-admission request is not "previously accepted."
- When a world-affecting command requests `t < next_step`, reject `STALE_TICK`, not backdate. Future-dated **external** commands should initially reject `FUTURE_UNSUPPORTED`; internally scheduled Cues are part of `S_t` and do not count as future-dated untrusted commands. A richer bounded host scheduling feature can be authorized later with `max_command_lookahead_ticks` and revalidation at execution.
- When single-player paused/suspended, `S_t`, timers, Ghost economy and Show time stay frozen. Newly submitted world-action requests receive `PAUSED_NOT_ADMITTED` (no idempotency reservation). A retry with the **same** ID after resume can be newly admitted once; a command already admitted before pause remains buffered for its assigned, still-unexecuted tick and resending that ID returns its existing receipt. Rejecting during pause must not permanently poison that ID.
- UI control-plane pause/resume and rejected host ingress receipts are traceable **outside** the world-state transition. To replay identical in-world events, use actual effective commands/ticks; to replay the entire input/receipt history, also retain pause control and rejected-request envelopes. Wall-clock duration is never an input to `Step`.

### The Ghost resource seam (focus G1-05/07)

**Precommit rule (recommendation, not adopted engine code):**

1. Evaluate eligibility from only allowed `GhostObservation_t`, current target/world preconditions, opening `Power_t` and Director's **precommit** answer `ALLOW / DEFER / VETO`; privileged safety facts may veto/defer but cannot become a new target.
2. If `Power_t < cost(action)`, reject `INSUFFICIENT_OPENING_POWER`; do not debit and do not emit world effect. An exact equality `Power_t = cost` is affordable, yielding zero *immediately after one debit*.
3. **Once** `COMMITTED`, publish `incident_id`, `cost` and `PowerDebit`; no other component can issue a second debit or self-allocate incident identity. World resolution may then thwart the action; no automatic refund.
4. End-tick regeneration is a **separately posted credit to S_{t+1}**. Thus `Power_t = cost - ε` with `regen_tick >= ε` is *not* an affordable attack at `t`, but may become affordable at `t+1`. Do not allow two independent Ghost plans to each read and spend the same original balance in one tick: commit costs aggregate against a sequential **reserved-spend accumulator**, with deterministic candidate order/selection already fixed by the Ghost, never arbitrary array order.
5. Any completed outcome reward is attributable only to a physical event; `incident_id` is not a reward. For Stage 4, settle one bounded claim ledger after world causation and apply credits to **next** tick only. A duplicate effect delivery, second rendered animation or new UI cue cannot create a fresh claim.
6. If an initially legal committed action later loses target access, **it stays paid** and resolves as thwarted/interrupted under the future Stage 4 settlement table; precommit invalidation is unpaid. That distinction makes the boundary auditable.

**Numeric state:** for Stage 4 choose a documented integer quantum `power_quantum` with explicit limits, or use exact rational accumulation with carried remainder `regen_remainder`. **Do not** advance Power by repeatedly adding implementation-language floating-point `dt * rate` without versioning how rounding, cap/overflow and order work. A sample exact representation is `regen_num/regen_den` scaled units/tick with remainder: `earned = floor((remainder + regen_num)/regen_den)`, `remainder_next = (remainder + regen_num) mod regen_den`. This is a proposed mathematical scheme, not runtime code. The resource state itself must include remainder/cap handling and the exact `regen_rate` version. If deferred Rage changes the rate, declare whether the new rate applies to this tick's accrual or only the next; **my preference is opening Rage for this tick, changes effective at S_{t+1}**. The owner should not copy illustrative prior GDD values into new magic constants.

**Conservation witness:** for an authorized tick, audit `Power_t - committed_debits_t + unique_credits_t + passive_credit_t - binding_drain_t - cap_discard_t = Power_{t+1}` with *intermediate affordability* checked **before** any end-of-tick additions. Bind drain is an inactive Stage 6 term. Because caps/rounding matter, the authoritative ledger records each delta and discarded overflow; a single final difference alone cannot prove absence of a temporary illegal spend.

**Settlement future gate:** `incident_id`, `event_id` and `reward_claim_id` must be distinct. All world child effects reference original committed incident. One incident can have several child injuries; they do not automatically multiply rewards. Two incidents may help cause one physical outcome, but a unique claim may be awarded at most once without an expressly authored sharing policy. G1-07 tests that causal skeleton **now**, but Stage 4 must decide `achieved / thwarted / partial / interrupted` and whether partial success can combine Rage plus reduced rewards. Don't silently adopt a payout table at Gate 1.

### RNG, integers and replay identity (focus G1-11/12)

A single global RNG stream is inadequate even when "seeded": drawing an unrelated dialogue variant before a Ghost choice can shift the Ghost's next draw and thus its strategy. Use **explicit, versioned, non-overlapping deterministic random domains** (`world`, `ghost:<haunting-id>`, `dialogue:<actor-id>`, `presentation`). A counter-based/keyed integer generator keyed by `(run_seed, domain, stable_decision_id, draw_ordinal)` is my preferred design because unrelated draw counts cannot perturb another decision. **Alternative:** persist one distinct PRNG state per domain and prove a strict no-cross-read rule; acceptable and simpler if the engine cannot safely specify a keyed generator yet. The exact algorithm, integer width, overflow behavior, string encoding for keys, seed parsing and state/counter format must be versioned before executable adoption.

- **Domain separation is necessary but not sufficient.** A Ghost decision key derived from mutable global event ordinals can still change when dialogue emits more events. Use stable cause/tick/entity-local identity. A changed Actor line can legitimately change **later** physical behavior if the Actor or player observes it; tests claiming independence must hold physical/observational conditions fixed and vary only *unrelated* dialogue randomness.
- **Same full replay tuple** (resolver build/rules hash, content bytes/schema hashes and explicit Production bindings, tick duration/ordering revision, initial complete S0, input admission/effective ticks and payloads including relevant rejected inputs, PRNG domain algorithm+version+seeds/states, canonical numeric/hash encoding, feature policy) must yield the **same full authoritative event and completed-state hashes** across supported Node/browser runtimes. Rendering cadence cannot change state or decision RNG.
- **Changed dialogue domain** alone, when dialogue IDs are authoritative narrative events, **may change full event trace** while the projected **mechanical/Ghost trace remains identical** in a controlled independence fixture. Do not demand impossible full-trace equality between deliberately different authoritative dialogue variants. If dialogue events are presentational only, the authoritative projection can remain identical; that is an explicit design choice, not a casual "random doesn't matter" assertion.
- Serialize integer counts/IDs in a canonical binary or canonicalized byte format with explicit key order, Unicode normalization, bounds, BigInt/string rules, hash algorithm and seed encoding. JSON object insertion order and implicit JS float serialization are not a reproducibility policy. Fix stable entity/cue/command identity in content; reject duplicate unresolved capability bindings rather than silently using array order.
- **Save/continuation is different:** a checkpoint may only represent fully completed `S_{t+1}` plus pending timers/reservations, dedupe registry, Show state, incident links, PRNG counters/remainders and exact version/hash refs. Mid-tick persistence is `INCOMPATIBLE_MID_TICK`; incorrect content hash is `CONTENT_MISMATCH`. Reject non-destructively. Stage 2 may be declared restart-only—do not build storage or migration before scope permits.

### Mandatory case matrix — specified expected *paper* outcomes, not executed tests

The identifiers and cases below follow the immutable handoff. Where Stage 4/6 policies are deliberately deferred, the resolver either has that feature **disabled** or requires the named future rule before admitting it.

| ID | Proposed deterministic result / alternative | Source of evidence and target gate |
| --- | --- | --- |
| **G1-01** Player Operate and legitimate due Show Cue target one restraint at `t` | Both intents are individually validated, but if no earlier legitimate exclusive claim exists and intended writes conflict, emit two `SIMULTANEOUS_CONFLICT` dispositions and one mechanism **no-change resolution**; Show sees its Cue failed and takes authored fallback. If prior player operation holds actuator from earlier tick, its claim wins; Cue fails. No sequential callback overwrite. **First proof**. |
| **G1-02** Actor versus Player contradictory valid intents on same control | Same exclusive conflict set and no-change outcome absent prior ownership; otherwise earlier valid physical claim wins. Role assignment/actor name alone cannot break tie. Alternative queue precedence is acceptable only when host ordinal/physical semantics declared, never hidden module order. **First-proof-compatible**. |
| **G1-03** Play script names Actor as issuer; same accepted ID replayed | `UNAUTHORIZED_ISSUER` for script impersonation; actual actor intent must be generated by authorized Actor policy. Identical accepted command retry returns original receipt, **not a new world effect**; conflicting ID payload rejects `ID_REUSE_CONFLICT`. **First proof**. |
| **G1-04** Timed Inspect overlaps Cue; pause/focus loss | If Inspect begins `t`, duration `d`, it resolves at `S_{t+d}` after `d` actual transitions and sees the committed world state at that boundary. No premature knowledge or animation-driven completion; pause freezes d−k remainder and no wall-clock catch-up. Existing acquired notes remain readable. **First proof**. |
| **G1-05** Borderline Ghost Power plus regeneration | With `Power_t < cost`, plan rejects unpaid even if end-tick regen would reach cost. Exact equality permits one commitment and debit, then end credit enters `Power_{t+1}`. Unpaid veto/invalid target never charges. If two commitments, sequential committed-reservation balance prevents overspend. **Stage 4 seam, algebraic gate now**. |
| **G1-06** Director safety-only veto sees hidden fact | Explicit `VETO(reason=safety_category)` or `DEFER`; no tactical target/fact delivered to Ghost, no debit, no free replacement plan in same decision event. Record privileged reason in audit, expose only permitted coarse outcome to Ghost. Paired hidden-state tests must show any Ghost target change is from allowed perception, not veto payload. **Stage 4**. |
| **G1-07** One paid Ghost incident produces two injuries and duplicate event delivery | Exactly one `PowerDebit(incident_id)`; child world events share one parent incident; replay/delivery duplicates yield no new physical effect or payout. Full settlement with unique `reward_claim_id` and reward/Rage statuses is **Stage 4 only**. **Causal skeleton at Gate 1**. |
| **G1-08** Fifth Bell requested same tick rig impacts Actor | Bell admitted as request, not an immediate physical stop; committed hazard still impacts under world-resolution phase. Show records `BELL_ACKNOWLEDGED` then cancellation for following beats. Actor injury persists and evacuation is separate physically timed action; outcomes show saved/late/canceled distinctly. A separate actual rig stop, if committed earlier, could prevent impact. **First proof**. |
| **G1-09** Required Beat and injured/refusing Actor | World resolves Actor ability first; Show consumes inability, selects explicit authored substitution or hold bounded by `beat_hold_max_ticks`, else `BEAT_FAILED/CANCELED`. No script impersonation, puppet line, or infinite hold. **First proof**. |
| **G1-10** Binding integrity breaks as Power becomes zero | **NOT DECIDED AT GATE 1**. Bound/containment capability disabled until Stage 6; adopting it requires a separate phase/terminal truth table for `seal_break, drain, escape commit, zero threshold, pending outcome claims`, all same-tick permutations and separate terminal status. Never infer victory from an arbitrary callback order. **Explicit Stage 6 block**. |
| **G1-11** Same seed/commands under differing render frame cadence or unrelated dialogue draws | Same *complete* replay tuple and player effective commands => same full authoritative hashes regardless of renderer. If intentionally different **dialogue RNG** changes authored dialogue events, assert **mechanics/Ghost projection parity**, not fictitious full-trace equality. If changed dialogue influences actual Actor decisions, causal differences are legitimate and must be reported. **Headless Stage 2 plus later Stage 3/4**. |
| **G1-12** Content hash mismatch / mid-tick continuation | `CONTENT_MISMATCH` or `INCOMPATIBLE_MID_TICK`, preserve original recorded data, no silent continuation; Stage 2 may be restart-only. Valid completed-tick S boundary includes pending timers, command dedupe registry and RNG remainder. **Replay gate now, save/resume later**. |
| **G1-13** Stale command, pause, resend same ID | Stale world command rejected `STALE_TICK`. New world command during pause rejected `PAUSED_NOT_ADMITTED` without consuming ID; after resume same ID may be admitted. Previously admitted before pause remains queued and retries are idempotent. No skipped world ticks. **First proof**. |
| **G1-14** Show Cue animates but restraint truth unchanged | If Cue failed arbitration, world state unchanged; presentation can animate a **cosmetic** effect only if it doesn't falsely communicate mechanical restraint change or conceals mandatory evidence. A real restraint change must correspond to an authoritative mechanism event. Any "actual fall" from animation alone violates C02/C10. **First proof**. |

### Four crisp paper traces the integrator can replay independently

**Trace A — Ghost border at tick t (G1-05):**

- `S_t`: `P_t = c - 1 quantum`, regen accumulated at end of tick ≥1 quantum; candidate action cost `c`, target valid, Director ALLOW.
- Phase 2: `REJECT INSUFFICIENT_OPENING_POWER`; no `COMMITTED`, no `incident_id`, no debit or physical effect.
- Phase 5: exact earned regeneration credited; `P_{t+1} ≥ c` if cap permits. Attack *may* commit at `t+1` after fresh eligibility. Replace `P_t = c`: Phase 2 emits exactly one `COMMITTED`, exactly one debit `−c`, balance immediately after cost zero, followed by *next*-state regen. Compare the debit ledger, not a final balance alone.

**Trace B — duplicate downstream deliveries (G1-07):**

- Prestate Ghost `P_t ≥ c` and one legal plan; Phase 2 emits `COMMITTED(i,c)`, `DEBIT(i,c)`.
- World emits `PHYSICAL_RELEASE(e1,parent=i)`, `INJURY(e2,parent=i)`, `PROP_DAMAGE(e3,parent=i)`. Duplicate transport/UI delivery of e2 is the **same event identity** and has no additional world transition. `S_{t+1}` has one paid incident.
- Stage 4 future: settlement may award **one** causally eligible, capped reward claim, using unique identity independent of number of children. The exact partial/complete payout table is *not* selected at Gate 1. A second replay of e2 does not mint a claim.

**Trace C — full replay vs dialogue variation (G1-11):**

- Two hosts receive identical content bytes, effective commands, `S0`, versioned fixed-step/canonical encoding, and **all** PRNG domains: full canonical `E_t` and `S_t` hashes match at each completed tick, independent of 30/60/144 Hz render cadence (numbers here are illustrative renderer rates, not performance targets).
- Controlled variation changes **only** dialogue random domain while holding Ghost-observed facts and causal world behavior fixed: selected dialogue IDs may differ, so **full trace hashes may differ**; Ghost plan IDs and mechanical state/event projections must match. If the voice variant actually changes what an Actor can learn/perform, that setup violates the "unrelated" condition; observe and report a legitimate effect rather than declaring a PRNG leak.

**Trace D — binding zero and seal failure (G1-10):**

- `S_t`: bound, seal intact, Power barely above zero, a pending drain interval and a legal seal-break effect both due at tick t.
- At Gate 1, the capability is marked `UNSUPPORTED_STAGE6_BINDING`. Do **not** generate either "banished" or "escaped" terminal outcome by unstated priority. Stage 6 must decide whether effective seal state gates drain, whether reaching zero finalizes before seal-break, and when pending credit/escape attempts apply. Record both candidate outcomes as separate hypothetical models and tests; no resolved answer key yet.

### Suggested first-proof acceptance matrix (future, no tests executed)

**Minimal acceptance conditions (without Ghost runtime):**

| Case | Oracle / check | What fails |
| --- | --- | --- |
| Same-tick Cue and stagehand Operate | One final mechanism result; no write based on callback enumeration; Show receives failed-Cue reason; swapping proposal enumeration yields unchanged result | Double state patch, silent winner, unseen cue revision |
| Invalid/duplicate command | One trusted issuer check, one ID registry, stable original receipt, no repeated world effect | Script actor impersonation, duplicate world change |
| Timed Inspect and pause | Exactly `d` simulation transitions to observation, no evidence beforehand, frozen counter during pause | Wall-clock or animation-driven knowledge gain |
| Bell and physical impact | Physical injury persists, Bell acknowledged/cancellation recorded, no teleport; both outcome axes preserved | Retroactive rescue, fake perfect win |
| Refusing/injured Actor | Bounded hold/fallback/failure, never forced Beat | Show deadlock/puppet actor |
| Full replay under differing render schedules | Same `E/S` hashes with identical full tuples | Frame-driven world changes or unreproducible ordering |
| Stale/paused command resend | Explicit reject and independent ID semantics, no phantom skipped tick | Silent success, poisoned retry ID |

**Stage 4 proof set:** two borderline Power fixtures (below and exactly cost); eligibility veto before commitment; same-tick multiple spend; partial reward and ghost-claimed ordinary event; two children and duplicate-delivery negative control; unrelated dialogue domain metamorphic Ghost decision; safety-veto hidden-state paired policy test. Must pre-register the Stage 4 ledger/settlement logic before implementation and compare with an independently authored accounting oracle.

**Stage 6 proof set:** complete seal-break/zero/escape/drain and pending-credit tie matrix; valid binding and invalid trap setup; no permanent wait exploit; causality-preserving completed-tick checkpoint.

**Evidence classes (separate):** static/document reasoning (this report), executed headless deterministic tests (future), cross-runtime Node/browser equality (future), timed human experience and fairness under actual presentation modes (future), durable save/restart (future). An unrun fixture is **NOT PASS**.

### Ranked findings, integration choices and deletions

**CRITICAL C00/C01/C02 — totality:** SF-0004 R-01 and contract refinement table still permit competing writes to same physical actuator. Block Gate 1 closure until the integrator publishes the **one mechanism arbiter rule** and an explicit phase/commit table. My exact equal-start no-op option is independently reproducible but not automatically the only valid design.

**CRITICAL C04 — opening-Power affordability:** SF-0004 demands a one-time debit, but does not state whether current-tick regen can fund the plan. Choose **opening-tick-only credit**, declare one debit in phase 2 and end-tick regen in phase 5. This eliminates a hidden race and makes a threshold oracle possible. Alternative regen-first is allowable only if fully documented with changed acceptance behavior.

**CRITICAL C11 — deterministic identity:** full seed alone is insufficient; require explicit algorithm/stream, content hashes, canonical integer semantics and input-effective-tick order. A PRNG domain label without decision-key stability can still allow incidental coupling. **Do not conflate fixed-command full-trace equality with dialogue-varied mechanics-projection equality.**

**IMPORTANT C01/C04 — incident accounting seam:** Ghost plan ID exists only on commitment; separate child event IDs and uniquely settled outcome claims. Stage 4 must choose partial/Rage/reward policy without inventing it here. In Gate 1 prove only nonduplication of commitment/effect IDs and parent causality.

**IMPORTANT C03/C07 — timed evidence, Bell and Show:** count Inspect time in whole simulation transitions; expose new fact only after completion, respect pause; Bell cannot stop harm retrospectively; all Beats terminate or explicitly hold for finite named budget. These need practical first-toy paper traces even though my lens is numeric.

**OPTIONAL refinement — exact arithmetic:** recommend a fixed-point Power quantum and rational remainder before Stage 4; Stage 2's time may be integer ticks only. Reject arbitrary floating-point `dt` and a speculative sophisticated save framework. Exact algorithms and sample tick durations are open until measured requirements appear.

**Deletions/deferrals:** No Stage 2 Ghost strategist, Director runtime, Rage, resource ledger, binding state, probabilistic Actor AI, full save/resume, general content ontology, per-module callback framework, global priority integers, arbitrary deterministic lexicographic winner, gameplay LLM, or art production. Preserve typed *seams* without building systems not exercised by the judgment pair. If the integrator prefers a trusted ordered queue over the conflict fail-closed rule, remove my reservation abstraction unless a timed mechanism actually needs it.

**Dissent:** I reject awarding default precedence to player, Show or Actor on *role labels alone*. Physical readiness, valid prior operation claim and explicit mechanism conflict policy have better causal explanations. I reject using render frame timestamp as authoritative timing. I also reject requiring **full event-trace equality** when intentionally altering authoritative dialogue choice: the relevant invariant is projection equality for untouched mechanics. Neither "deterministic" nor "safe" proves that players have enough time/evidence to make satisfying decisions.

**Uncertainty:** The event phase table is a proposal, not a running implementation; no sampled input latency, measured `inspect_duration_ticks`, human reaction threshold, cross-host RNG equality or fairness trial exists. It is not known whether fail-closed collisions produce enjoyable/credible stage action. Exact safety interlock and Actor/Cue scheduling policy still require Mothlight's authored mechanism fixture. A causal ledger is required only once Ghost events exist; do not pretend a blank Stage 2 ledger is an accepted Ghost economy. No binding zero winner is selected at this gate.

**Affected paths if later adopted (Mothlight decision only):** `docs/reviews/STAGE0_RECONCILIATION.md` (new source-pinned Gate 1 reconciliation, do not rewrite old reports), `docs/contracts/V0_PLANNED_CONTRACTS.md` (proposed C00/C01/C02/C03/C04/C05/C07/C11 phase/invariant text), `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` (paper collision and time examples), `docs/ROADMAP.md` (gate tracking), `docs/changes/<new-SF-ChangeID>.md` / `CHANGELOG.md` / `version.json` only **after** an owner-accepted integration according to `docs/VERSIONING.md`. No path changes authorized by this report.

**Preserve unchanged:** one simulated world, in-world stagehand and progressing Play, independent Actor intentions, limited Ghost perception, Director precommit veto-only policy, expensive real physical danger, Fifth Bell request distinct from safety/evacuation, headless determinism, renderer nonauthority, mundane first judgment pair, optional future binding and honest partial wins.

## Revisit when

After Mothlight has collected and frozen all six independent Gate 1 replies, performed a source-pinned reconciliation of actual phase/tie alternatives, and the human authorizes any specific contract revision. Re-test this report's counterexamples with the accepted fixture, exact game commit and independent oracle. Before Stage 4 choose and test the full resource/settlement numeric rules. Before Stage 6 choose the seal/zero terminal ordering. Until then **no test is claimed executed, no engine code has changed, and no interface is ratified**.

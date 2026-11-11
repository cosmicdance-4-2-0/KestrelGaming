---
schema: 1
id: 2026-11-11-stage-fright-gate1-authority-review-lk26
kind: handoff
scope: agent:latch
status: active
evidence: inferred
author: latch-gate1-authority-independent-2026-11-11
created: 2026-11-11
updated: 2026-11-11
sources: "STAGE0-G1-AUTHORITY-01/LATCH issue #13 and immutable dispatch at e538b19c781d28e7c0754cb8438f401b3b93efd3; mandatory seven Stage Fright source documents inspected at exact 107ae2b446405d225feac01595e9ead08d679bde (SF-0004); own prior LK25 at b8f350dd117e4f46bd20227a97a4372497923e83; own Latch character and Kestrel permissions read from agents/latch-v1. No other agents' Gate 1 results reviewed; all traces are proposed, not executed."
---

# Latch — STAGE0-G1-AUTHORITY-01 independent command-trust design review

**Authorial perspective:** Latch — The Locksmith; individual design/profile source `cosmicdance-4-2-0/KestrelGaming@agents/latch-v1`, `character_id=latch` (draft profile, not authenticated independent runtime).  
**Target:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT` **issue [#13](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/issues/13)**.  
**Authoritative game baseline:** **`107ae2b446405d225feac01595e9ead08d679bde`**; reported development state `0.0.2.4/SF-0004`.  
**Immutable handoff:** [STAGE0_GATE1_AUTHORITY_HANDOFF.md](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/e538b19c781d28e7c0754cb8438f401b3b93efd3/docs/reviews/STAGE0_GATE1_AUTHORITY_HANDOFF.md).  
**Mode:** INDEPENDENT REVIEW, DESIGN ONLY; no code, no runtime, no accepted interface, no implemented tests. The other five *new Gate 1* responses and issue threads were **not read** before recording this review. The source-pinned SF-0004 reconciliation contains summaries of *prior Stage 0* findings, as required reading, not new Gate 1 results.

## Summary

**Verdict: CONDITIONAL ACCEPT of SF-0004's direction; REQUEST CHANGES to the unratified Gate 1 contract before implementation.** The highest-priority invariant is **a command cannot acquire authority by claiming an Actor ID, a source tag, an earlier tick, a retry ID, or a name in authored content**. A trusted ingress/scheduler binds origin and issues an immutable receipt; the one world resolver owns permission, conflict, effects, causal events and observations. For the future Ghost, a Director that sees hidden safety state may still leak information by the *pattern of its vetoes* even when it never returns a target ID. This is a concrete covert-channel risk, not an observed exploit. The smallest correct solution is a per-run command ledger plus explicit admission/settlement semantics and carefully restricted policy projections, **not** multiplayer authentication, general event sourcing or a new ontology.

## Evidence

### Exact inspected sources and applicability

1. [SF-0004 reconciliation §§R-01, R-02, R-05, R-06, R-09–R-13 and temporal requirements](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/reviews/STAGE0_RECONCILIATION.md). *Observed design status:* requirements adopted as planning; executable conflict/phase table intentionally open.
2. [Version 0 planned contracts §§Authority, C00–C07, C11 and SF-0004 refinements](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/contracts/V0_PLANNED_CONTRACTS.md). *Observed:* one authoritative resolver, deterministic ticks, bounded Ghost, distinct Actor/Role, replay; APIs unspecified.
3. [Stage 2 judgment experiment §§Question, paired conditions, information/causality rules, checks and limits](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/design/STAGE2_JUDGMENT_EXPERIMENT.md). *Observed:* one Room/restraint/Cue; revision vs fault; **no autonomous Ghost/Director** in the first toy; tests not run.
4. [Terminology](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/TERMINOLOGY.md): Room/Shot vs dramatic Scene/Beat/Cue, Actor vs Role, Performance and Run.
5. [Architecture](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/ARCHITECTURE.md): one headless core, presentation nonauthoritative; APIs and gameplay unimplemented.
6. [Roadmap §§Stage 0, Stage 2, Stage 3–7, cross-cutting gates](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/ROADMAP.md): Stage 0 not closed; first toy mundane; later features explicitly gated.
7. [Versioning](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/107ae2b446405d225feac01595e9ead08d679bde/docs/VERSIONING.md): ChangeID is not an automatic schema/replay identity or author authentication.
8. [Own prior Stage 0 review LK25](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/b8f350dd117e4f46bd20227a97a4372497923e83/memory/agents/latch/2026-11-09-stage-fright-stage0-independent-review-lk25.md): the command and Ghost projection ambiguities were already raised at a previous baseline. No other author's Gate 1 reply consulted.

**Evidence categories:** SOURCE OBSERVATION describes written contracts, not runtime; DESIGN PROPOSAL describes the rules below; HYPOTHESIS describes possible failure and intended experiment; no fixtures executed or gameplay observed.

## Independent verdict and ranked findings

| Priority | Finding | Exact governing source | Observable design failure to exclude |
| --- | --- | --- | --- |
| **CRITICAL** | Origin must be bound by a trusted component, not accepted from input content; issuer is not acting entity | Reconciliation R-02; contracts C01/C06/C07 | A Play's string `issuer: mara` causes Mara to move/operate without an Actor decision; wrong Actor receives effects |
| **CRITICAL** | Duplicate and tick status must be determined *before* executing an effect; same ID with different payload is never a new command | Reconciliation R-01/R-02/R-10/R-11; C00/C01/C11 | Resent operation reopens a latch or pays twice; old command is silently applied after pause |
| **CRITICAL** | Director's hidden-state veto is a **one-bit and timing covert channel** unless the information boundary specifies permissible declassification | Reconciliation R-05; C04/C05 | Ghost discovers an unseen binding setup by differing veto outcomes, retries or adaptive timing |
| **IMPORTANT** | Conflict order, physical locality and action completion must be explicit even for legitimate concurrent intentions | Reconciliation R-01/R-12/R-13; C01/C02/C07 | Outcome depends on callback order or permits a player to control an absent Actor |
| **IMPORTANT** | World change, incident settlement and observation are separate causal steps | Reconciliation R-03/R-06/R-09; C02/C03/C04/C11 | An Inspect leaks future data; animation becomes evidence; one incident yields many credits |
| **OPTIONAL** | Security tokens, crypto, distributed identity and general event-sourcing are premature | Roadmap Stages 2–7; Architecture | Toy complexity grows without improving any currently testable judgment |

The first three are **blocking ambiguities for Gate 1 design acceptance**, not confirmed implementation flaws. The issue-specific priority is command trust and knowledge isolation; the broader conflict table is an explicit candidate for Mothlight's comparison, not a universal demand.

## Minimal command contract: source, claims, and authority

### Proposed distinct concepts (semantic contract, NOT an API schema)

- **Issuer:** a trusted host/core origin binding: `local-player-input`, `world-show-scheduler`, `actor-controller:<actor>`, or later `ghost-controller:<ghost>`. A literal string submitted by a manifest, UI component or NPC dialogue is never sufficient evidence of that binding.
- **Acting entity:** *who attempts the in-world operation*, with a separate class for Show-system Cues when no bodily Actor is performing it. A Play's Role assignment or authored dialogue can *request* Actor participation, not impersonate an Actor.
- **Run-scoped command identity:** immutable `runId + issuerScope + commandId`, with a canonical payload fingerprint. The ID prevents duplicate effects, **not** cross-issuer authorization. IDs of differing payloads collide and fail explicitly.
- **Timing:** `requestedTick` (untrusted proposal), `admittedForTick` (bound by trusted admission), `effectiveTick` (actual effect or decision), and optional `inProgressSinceTick`. No wall clock advances world ticks. Tick identifiers use a named fixed-step clock with chosen unit/numeric rules (unratified).
- **Causal identity:** the command ID traces the attempted intention; a **separate, trusted incident/effect ID** links actual world changes, warnings and Ghost settlement. A caller cannot select a prior `incidentId` to acquire rewards.
- **Target and verb:** stable world identity/capability plus operation; the resolver checks live state, ability, locality, ownership/authorization and any exclusive resource occupancy. Names/labels in content do not confer access.
- **Disposition:** a durable nonambiguous outcome (`REJECTED`, `ADMITTED_PENDING`, `COMMITTED`, `CONFLICT_LOST`, `COMPLETED`, `IDEMPOTENT_REPLAY`) with reason and effective tick where applicable. Event vocabulary illustrative, not a ratified enum.

**Trusted ingress rule:** A local UI may propose `Operate(player, restraint)`; the host binds the active player and requested action. A Play may declare `Cue at T requests fixture.release`; the validated Show scheduler compiles that declaration into a system-origin intent only at a permitted binding. An Actor controller generates an Actor-origin proposal from that Actor's observations, physical ability and policy; a player conversation creates a communication/request event, not an Actor-origin action. Future multiplayer replaces the local ingress with an authenticated adapter; **core invariants remain unchanged**. A client-supplied `issuer` or `actingEntity` is always a claim requiring host binding.

### Proposed admission matrix — all results recorded

| Condition at authorized ingress / tick frontier | Outcome | Side effects |
| --- | --- | --- |
| Same run+issuer+ID, **same canonical payload**, already pending or settled | `IDEMPOTENT_REPLAY(originalDisposition)` | No additional tick, effect, debit or Actor work. If original is pending, report pending; if settled, report its recorded result |
| Same key, **different payload** | `REJECTED_ID_COLLISION` | Never treat as new action; don't overwrite original fingerprint |
| New command, wrong issuer/actor binding or no permission for source | `REJECTED_ORIGIN` | No operation; useful player-facing message without leaking protected state |
| New command, unknown target, ability/range failed at evaluation | `REJECTED_PRECONDITION` | No effect; checks performed at declared evaluation frontier; avoid revealing hidden objects to unauthorized caller |
| New external request for a **past** completed tick | `REJECTED_STALE` | No catch-up, no replay, no shift to present; **duplicate lookup happens first** |
| New external request targeting a **future** tick | `REJECTED_FUTURE` for minimal toy | No host-side speculative queue. Internal Cues remain predeclared future schedule entries with separate trusted provenance |
| New external world-changing request while paused/suspended | `REJECTED_PAUSED` (not silently buffered) | No tick advancement; UI may retain an **unsubmitted draft** for intentional resubmission on resume |
| Previously admitted pending command when pause begins | Remains `ADMITTED_PENDING` for same next tick | Resume processes once; no wall-clock catch-up; duplicate resends refer to original ticket |
| New valid request for currently open next-tick admission | `ADMITTED_PENDING`; gets trusted stable ticket | No effect until one authoritative step resolves it; client does not choose arbitration order |
| Authorized but physically contested valid intent | `CONFLICT_LOST` or declared compensating outcome | No silent effect; legitimate service/show consequences remain observable |

**Important deliberate choice:** reject externally future-dated commands rather than maintain a general scheduler at Stage 2. This trades away convenience for a much smaller attack/replay surface. Preauthored Show Cues are *not* external commands and must retain their scheduled due-tick behavior. A future queued-input feature can be added explicitly with a bounded horizon and cancellation/replay rules if it proves necessary.

**Deduplication lifetime:** a stable per-Run ingress/disposition index covers all IDs that can be replayed after pause or supported continuation. It need not be a large audit service; the Stage 2 toy can keep it in memory for the Run. Do not truncate history while accepting stale IDs as new. Continuation later must snapshot the index or a logically equivalent bounded non-replayability proof.

## Proposed phase and arbitration model (one plausible full model, not canon)

**State frontier:** `S[T]` is the canonical fully completed-tick state before executing the next tick `T`. The world is advanced only by `step(S[T], sealed admissible inputs, deterministic configuration/PRNG)`, producing `S[T+1]` and an ordered causal trace. A pause/suspension is a host state that simply **does not call step**; simulation/show/Inspect progress all freeze. This requires defining tick indexing precisely in integration, but no chosen real-time duration.

**Phase P0 — Seal admission:** At the start of a tick freeze host-admitted tickets, current world state, due Play Cues and any already executing/reserved work. New input after the frontier belongs to a later tick (not inserted mid-step). Duplicate checks precede stale/future checks.

**Phase P1 — Construct authorized proposals:** Show issues only compiled/bound Cues, Actor controller only its own Actor intents, player only host-bound player intents; future Ghost only from its permitted perception projection. Reject forged source fields before target evaluation. **A module is a proposer, never a writer.**

**Phase P2 — Validate snapshot and eligibility:** Check existence, ownership, bodily ability/locality, expected resource state, tick, knowledge as appropriate and permission against the declared state frontier. Later Director gate runs on a bounded pacing view, before Ghost commitment. Revalidate the winning physical preconditions when applying the effect if earlier legal transitions changed them.

**Phase P3 — Arbitrate exclusive resources:** Use the mechanism's declared affordance/operation conflict relation, not module iteration. Noninterfering operations coexist. For one physical control, at most one conflicting actuation is committed in a tick; losing intents receive recorded conflict dispositions. **Proposed deterministic ticket policy:** pre-existing exclusive physical operation/reservation retains the resource until its recorded completion or cancellation; otherwise compare *trusted, stable admission/reservation tickets* in a declared total order attached to the Run trace. Due Cues receive tickets from canonical Show schedule order, player inputs at authorized host ingress, Actor/Ghost intents from canonical scheduler evaluation order—not arbitrary callback order, client-supplied priority or caller IDs. A due Cue with an earlier valid reservation may outrank a last-moment Operation, while a player action that already lawfully secured the mechanism can block the Cue. All conflict and source-order conventions are visible to integrator/evaluator before testing. **Tie counterproposal:** an explicit `manual-safety-interlock` affordance may trump ordinary actuation if physically established before commitment, but must be modeled as a mechanism constraint, not an unconditional 'player wins' privilege.

**Phase P4 — Commit and resolve physical effects:** Winning eligible actions commit once. Future Ghost Power affordability and **single debit** occur at the same guarded commitment transition, never when a plan is merely suggested or Director-vetoed; the agreed resource calculation may first apply a named per-tick regeneration step. World owns position, restraint, injury, load and actual cue outcome. A later cause/effect uses trusted incident IDs and idempotent settlement.

**Phase P5 — Derive Play and observations:** Show Beat resolution consumes **resolved** world/Actor state, never fabricates Actor action. Timed Inspect completes according to the authoritative simulation clock and samples permitted facts at the declared end-of-tick observation frontier; known notes can be displayed during pause without new sampling. A free renderer read may display available evidence, not alter local character knowledge. A Bell request is acknowledged and Show cancellation becomes effective for later Cue commitments (proposed: after the physical effects of the requesting tick), without undoing injury already incurred; physical evacuation is separate.

**Phase P6 — Seal trace and new state:** Record each command's accepted/rejected/conflict status, causal world events, observation availability, Show status, RNG changes and completed-tick state identity. Only now can a checkpoint exist. Presentation consumes the published projection and may not authoritatively move a rig or create an impact.

**Risk / tradeoff:** Ticket precedence is deterministic given the *recorded* host admission order but not invariant across different real-world input timings; this is appropriate for a time-sensitive game, subject to player fairness tests. If tickets can be silently manufactured or reordered by module registration, the design fails. A central ticket schedule and one mechanism arbiter are enough for Stage 2; do not impose complex reservation infrastructure on every object before the toy needs it.

## Required counterexamples and proposed trace outcomes (NOT EXECUTED)

**Notation:** `@T` denotes authoritative simulation tick; `ticket A ≺ ticket B` is the recorded prior admission/reservation order, not arbitrary numerical priority. `END(T)` is the completed-tick boundary. These are *paper traces for integration choice*, not the engine's existing output.

| Case | Given / proposed exact deterministic disposition | Status/gate |
| --- | --- | --- |
| **G1-01** Player Operate and valid Show Cue target one restraint at T | Both are valid proposals. If Player secured exclusive physical reservation before T: `Player COMMITTED`; `Cue CONFLICT_LOST`; **one** restraint resolution and Show receives missed/blocked Cue. If no prior player reservation and Cue has earlier trusted ticket: Cue commits, late Player loses; next-tick correction may be attempted. **Never** two independent writes. | First toy; declare physical/timing fixture before adopting |
| **G1-02** Actor versus Player contradictory intents at T | Actor and Player must each have valid self-origin. Earlier established operation reservation wins; otherwise trusted stable tickets decide, loser has explicit `CONFLICT_LOST` plus Actor's knowledge of failed attempt. A player `Communicate` is a request, never an Actor actuation. | Stage 3 Actor fixture |
| **G1-03** Play forges Actor and a valid command is repeated | `Play{issuer:'Mara',act:'operate'}` → `REJECTED_ORIGIN`, no Actor effect. Valid `K=(Run,Player,c42)` at T produces one effect; identical `K` resend later → `IDEMPOTENT_REPLAY(original)`, **zero** additional effects. Same K different payload → `REJECTED_ID_COLLISION`. | **Required first proof** |
| **G1-04** Inspect spans Cue; pause before completion | Inspect begins with authorized local reach, spends `inspect_cost_ticks` (named tunable in ticks, no numeric default). Cue resolves while Inspect is in progress. Pause freezes `S[T]` and Inspect remaining ticks; resume has no catch-up. On completion, observation samples the *then-current accessible* restraint state (not an omniscient cause label), with a recorded visibility tick. | **Required first proof** |
| **G1-05** Ghost borderline Power, regeneration and attack at T | **Candidate precedence:** passive regeneration (if allowed) applies first at a named rate per tick; then Ghost candidate+Director eligibility; then affordability check and one commitment debit if winning. If sufficient only after regen and action legal, action may commit; otherwise `REJECTED_UNAFFORDABLE`, no debit. Must settle exact numeric arithmetic before Stage 4. | **Stage 4 gate** |
| **G1-06** Director veto using hidden safety state | Ghost proposes only using `GhostView(T)`. `DirectorView(T)` can gate eligibility using declared safety signals, but returns to world resolver only `ALLOW/DEFER/VETO` for that candidate; **never** a target, tactical hint or reason to Ghost. Vetoed candidate has no debit or action, and no veto feedback enters Ghost memory. Run paired Ghost-visible-equivalent states; see covert-channel caveat below. | **Stage 4 gate** |
| **G1-07** Paid Ghost intervention creates two harms, duplicate delivery | One `IncidentCommitted(I)`, one debit; effects `Damage(A,I)`, `Damage(B,I)`; duplicate event with same trusted effect ID cannot reapply either damage or payout. Settlement one claim for I, with caps/partial outcome rule deferred to Stage 4. | **Stage 4 gate** |
| **G1-08** Fifth Bell requested on rig-impact tick T | `BellRequested@T` recorded; pre-existing physical impact resolves at T, including injury. Candidate policy: `BellAcknowledged/ShowCanceled@END(T)` prevents newly scheduled future Cues from T+1, not damage at T. Evacuation still requires valid physical actions. If an earlier Bell would have prevented actuation, fixture must show it explicitly. | **First proof** for request/impact; full rescue Stage 3–5 |
| **G1-09** Injured/refusing Actor required for a Beat | `ActorOperation REJECTED_ABILITY` or legitimate `ActorRefusal`; Show consumes it and selects authored fallback, bounded hold, missed/failed Beat or cancellation. No puppet Actor action. If no alternate, Beat fails explicitly rather than remaining pending forever. | **First proof** via passive/fixture Actor; fuller autonomy Stage 3 |
| **G1-10** Seal breaks at zero Ghost Power | **No invented winner.** Disallow this unresolved simultaneous transition in any implemented Stage 2–4 scenario; Stage 6 acceptance must specify a total settlement table for seal validity vs Power-zero evaluation and counterexamples. At Stage 6, zero Power and broken seal cannot be resolved by file order or an omitted event. | **Stage 6 gate** |
| **G1-11** Same seed/commands, different frame rate/dialogue cosmetic RNG | Identical authoritative `S[T+1]` and ordered authoritative events/hashes, with presentation RNG outside core and unrelated dialogue randomness not consuming Ghost/world RNG stream. Presentation output may differ. | **First proof** headless; Ghost/dialogue later |
| **G1-12** Wrong content hash or mid-tick resume | Reexecution or continuation rejects unsupported content/rules identity; checkpoint accepted only after `END(T)`, with pending intents, disposition IDs, and PRNG state pinned. **No** mid-tick reinterpretation or destructive auto-migration. Stage 2 may be restart-only with explicit notice. | Replay identity first; durable continuation later |
| **G1-13** Stale/paused/resend | New `requestedTick < nextTick` → `REJECTED_STALE`; new future tick → `REJECTED_FUTURE`; new world-changing input while paused → `REJECTED_PAUSED`; exact resend of already pending/settled command ID → `IDEMPOTENT_REPLAY` **before** stale or paused rejection. Resume retains next tick and original pending commands, no catch-up. | **Required first proof** |
| **G1-14** Cue animation moves but state unchanged | Rendering receives `CueConflict/NoChange` and may animate an attempted jiggle if signaled, but **must not** present world-authoritative restraint release, impact or learned hazard. No simulation state change or damage reward follows cosmetic motion. | **First proof** of world/presentation split |

**Clarify G1-01 and G1-02 in integration:** `ticket order` must be operationally defined by the chosen command-source scheduler and time-cost model. The above model chooses prior real physical reservation before newly competing control operations. If Mothlight prefers a fixed source-class precedence or interlock-based simultaneous effects, document its **actual** effect on fair player intervention and on cast agency; no rule should be smuggled in via array iteration. Merely saying 'stable sorting' is insufficient unless the ticket source is trusted and reproducibly defined.

## Ghost versus Director: the hard information-flow question

**Nominal separation (recommended):**

`GhostView(T) = explicitly sensed facts + established authored lore + timestamped Ghost memory`. No hidden player inventory, undiscovered vessel, omniscient Actor psychology, or debug state. The Ghost Strategist computes candidate action from this view only.

`DirectorView(T) = declared pacing and safety policy signals` (possibly privileged world safety state). It is a distinct projection and can only accept/veto/defer a **candidate** prior to commitment. It has no authority to author tactics, change Ghost target, synthesize damage, credit rewards or undo thwarting. No command output from Director gets an `actor-controller` issuer.

**Information-theoretic caveat:** A binary veto *is information* if the Ghost can observe it, change its candidate as a probe, or learn from the presence/absence/timing of its own attacks. Even a perfect interface which returns no hidden target string can leak location/anchor facts over repeated candidate tests. Thus the claim 'Director sees secret state, but Ghost can never infer any of it' is **not generally achievable** with a state-dependent gate that affects observable outcomes.

**Minimal mitigating rule:** Compute proposals once from GhostView at a defined decision frontier. Director applies a single opaque gate in core; do not expose gate reason, denied candidate list, retries, hidden state, or denial timing as new Ghost knowledge. Do not replan within the same tick after a veto. Evaluate what the Ghost may legitimately infer *later from observable world changes* and specify that declassification explicitly. If strict noninterference is needed, gate only on **nonsecret/public pacing facts** or use a schedule independent of the protected fact. A privileged hidden-state safety veto may be preferable for fair play, but then the spec must state the limited leakage tradeoff rather than promising mathematical zero leakage.

**Paired negative test:** Two world states differ only in a hidden binding vessel. Keep GhostView and Ghost RNG identical. Before Director gating, candidate/target must match. After gating, either (a) identical permitted public safety state gives identical gate behavior; or (b) differing privileged safety state produces a documented permitted veto difference, **without** exposing denial/reason as strategy input or allowing same-tick adaptive probing. A subsequent observed world event may legitimately change GhostView. Test repeated attempts as well as one-step traces; report what is observable.

## Bounded authoring and provenance controls

- Content files may declare **schedule/Role bindings and allowed capabilities**, but are untrusted, validated data, not authority-bearing commands or arbitrary TypeScript.
- At Adventure preflight, reject a Cue whose bound mechanism does not exist or is ambiguous; reject Actor/Role mismatch that would silently cause an unowned action. The *validated configuration* becomes part of replay identity.
- A world-provided observation is scoped by observer/location/tick. A player cannot `Inspect` an inaccessible mechanism by naming its ID, and a free read is constrained to already learned notes. Unauthorized operations should avoid exposing protected hidden state via overly specific error messages.
- Single-player host origin binding is **not cryptographic identity** and provides no real adversarial boundary against an owner controlling a compromised JS runtime. It does defend against accidental privilege elevation through content, composition and module design. Multiplayer trust enforcement is deferred, not assumed.

## Minimal proof fixture versus named future gates

| Gate | Minimum contract needed | Unjustified expansion to avoid |
| --- | --- | --- |
| **Gate 1 paper + Stage 2 toy** | Authoritative completed-tick step; trusted local input vs compiled Show Cue; stable command identity, duplicate/stale/paused handling; one resource contention rule; timed Inspect and observation availability; late Bell and absent Actor fixture; event/status trace; seed and content identity | Ghost planner, network authentication, persistent distributed ledger, giant command API, user scripting, full data pack tooling |
| **Stage 3 Play/Actor** | Actor-origin from actor-local state; Beat finite exit and distinct refusal; actual physically possible Cue/communication | Global psychometrics, forced performance, general dialogue generator |
| **Stage 4 Ghost/Director** | Permitted Ghost/Director views, opaque single veto, regen-affordability-debit order, unique incident ID/settlement, separate AI RNG | Omniscient pacing controller, broad five-tier action catalog, generalized event-sourcing service |
| **Stage 6 Binding** | Seal break and Power-zero total settlement table; refund/cancel policy and binding transition | Inventing the tie from a speculative first toy |
| **Stage 7 Composition** | Validated data-only Adventure binding and compatibility; two fixtures, clear rejection of ambiguities | Arbitrary executable mods and universal ontologies |
| **C11 persistence when authorized** | Completed-tick save including pending queues/IDs/RNG, non-destructive failure and version mismatch checks | Silent mid-tick restore or implicit migration |

## Verification plan — proposed, not run

**Mechanical feasibility:** create a hand-written two-state toy trace (authorized revised Cue / ordinary mechanism fault) and replay all first-proof cases with exact start state, emitted commands, trusted admission tickets, transition dispositions and end state. A rejected forged Actor intent must not consume a world operation. For each candidate, identify independently checkable before/after state, including legitimate no-change outcomes.

**Determinism:** execute identical recorded input/configuration/PRNG traces in Node and browser with rendering cadence varied; compare authoritative event sequence, state identity, command dispositions and observation availability tick. Include duplicate/stale/paused mutations; require negative test to fail when reordering an authoritative ticket or changing content hash. These tests do not yet exist.

**Fairness:** separately expose play testers to a valid revised Cue and an ordinary fault with matched initial symptom. Record what evidence was accessible and noticed, how much legitimate time was available, whether the player understood admission/conflict and why an intervention helped or harmed. Repeat with sensory and input modes. Headless determinism **does not** establish fun, warning legibility or human causal understanding.

**Independent adjudication:** compare against an independently written fixture contract/invariant table, not solely the same resolver's self-reported status. As a positive control, legal Show Cues and legitimate player's prior operations must both succeed in their intended conditions; reject-all is a failing implementation.

## Dissent, uncertainty, proposed deletions and impacted paths

**Dissent:** Do not elevate the Director's use of hidden safety state into an unqualified guarantee of Ghost ignorance. A veto can be a side channel. Preserve the explicit tradeoff between fairness gating and strict secrecy; this is my principal individual objection to a too-easy R-05 interpretation.

**Unresolved:** The precise C01 ticket policy, physical resource reservation lifecycle, failure semantics of conflicted manual/scheduled actions, whether a Bell should ack before vs after current tick physical effects, and the affordable numeric representation are integration decisions; I supplied one coherent proposal and counterexamples, **not an adopted executable contract**. `requestedTick` while paused might be more user-friendly if deliberately deferred rather than rejected; a deferred future queue would need stable admission and cancellation semantics. No measurement yet establishes which choice makes play clearer.

**Deletions:** No agent command signatures in the Stage 2 toy; no automatic future-client queue; no generic privilege engine; no actor impersonation by scripts; no 'Director explains its veto to Ghost' debugging channel; no unneeded actor/ghost modules in the mundane pair; no unjustified reward/currency precision or magic durations.

**Paths/interfaces for Mothlight's reconciliation (not edits):**
- `docs/contracts/V0_PLANNED_CONTRACTS.md` — C00/C01/C03/C04/C05/C06/C07/C11 definitions; documented disposition/ticket and projection boundary.
- `docs/reviews/STAGE0_RECONCILIATION.md` — R-01/R-02/R-05/R-09/R-11/R-12/R-13 proposed phase and tie dispositions, preserved dissent.
- `docs/design/STAGE2_JUDGMENT_EXPERIMENT.md` — one restraint same-tick decision, timed inspection, invalid input, pause and observable fair outcome.
- `docs/ARCHITECTURE.md` — clarify that modules propose intents but only core resolves; no package proliferation needed.
- `docs/ROADMAP.md` — keep stage gates and deferred scope named; no automatic advance.
- `docs/changes/<future-approved-ChangeID>.md`, `CHANGELOG.md`, `version.json` — **only after integrator/owner approves and records a later accepted change**, not as a side effect of this review.

## Outcome and handoff

**COMPLETE as an independent design review; NOT IMPLEMENTED or VALIDATED.** This document is Latch's own first-pass Gate 1 report, suitable for citation by Mothlight. No shared contract was ratified; no production/test/game code modified; no other agent Gate 1 response read; no comparison or synthetic consensus claimed. The GitHub account is shared, so attribution is to the declared Latch authorial perspective, not proof of separate authenticated agent execution.

## Revisit when

Mothlight proposes a concrete authoritative transition/tie table, a Director projection and permitted-declassification policy, accepted Stage 2 fixture semantics, or evidence from actual headless and human tests contradicts these proposals.

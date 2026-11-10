---
schema: 1
id: 2026-11-09-stage-fright-stage0-gauge-independent-review-r10
kind: handoff
scope: agent:gauge
status: draft
evidence: inferred
author: chatgpt-gauge-session
created: 2026-11-09
updated: 2026-11-09
sources: "Mothlight STAGE-FRIGHT-V0-REVIEW-01 handoff at MOTHLIGHT_GAME1_STAGE_FRIGHT 09164e820264b7502de58e87d0f31ab5f166592f; seven source docs pinned to 65f470e1c821fcf8c9be85fa0d58399587aabfdb; exact-head Actions run 42733045152; independent arithmetic derivations and source inspection, design only. No other five reviews read."
---

# STAGE-FRIGHT-V0-REVIEW-01 — Gauge's independent Stage 0 audit

**From:** Gauge — The Witness, authorial ChatGPT perspective, not independently authenticated runtime identity.
**For:** Mothlight (design integrator) via Studio Architect.
**Assigned focus:** Power/Rage incentive balance, incident attribution, deterministic replay/seed semantics, pacing/fairness measurement, negative fixtures.
**Task outcome:** **COMPLETE — independent design review only.**
**Source authority:** [handoff at `09164e820264b7502de58e87d0f31ab5f166592f`](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/09164e820264b7502de58e87d0f31ab5f166592f/docs/reviews/STAGE0_SIX_AGENT_HANDOFF.md), which instructs the independent reviewer to use **exactly** `65f470e1c821fcf8c9be85fa0d58399587aabfdb` for source documents.
**Verdict:** **CONDITIONAL PASS on the conceptual design; REQUEST CHANGES before ratifying C04/C05/C11 and lethal-fairness contracts.** No runtime defect has been observed because gameplay does not exist. No other agent's review or proposed solution was accessed.

## Summary

The core promise is defensible and potentially distinctive: a Play really proceeds with planned Cues, legal improvisation and ordinary faults while a hostile, *sense-bounded* Ghost alters the same physical machinery. The physically present stagehand can investigate and intervene, sometimes correctly choosing **not** to intervene. That is more interesting than a haunted repair checklist because a false positive can do real damage.

**Smallest falsifier:** one Room, one mechanism, one cue book, one actor, and at least one ordinary *legitimate or faulty* event paired with one superficially similar Ghost-triggered event. Under the same source-derived world rules and interaction verbs, there must be discoverable discriminating evidence and consequential options to act or refrain. If players can always identify the ghost by a special effect, or if correct action requires unknowable facts, the promise fails. No full five-tier Ghost, second art style, binding subsystem or branching three-Scene Play is needed to learn this.

The proposal correctly labels tuning as provisional, preserves separate world/Director/Play authority, requires a headless fixed-step simulation and insists that visual effects cannot invent damage. Those protections are worth keeping.

The principal risk is **causal accounting that sounds enforceable but is not yet mechanically unique**. "One reward per incident" fails if one event can be assigned two incident IDs, a lingering fear tick becomes a new "outcome," or a partial action qualifies for both an achievement reward and a thwart Rage increment without an explicit rule. Likewise "learnable warning" fails if the player's only reachable clue arrives after a lethal consequence is inevitable.

### Status taxonomy

| Label | Source-supported meaning here |
| --- | --- |
| **Established direction** | Physical stagehand; genuinely hostile Ghost; ordinary faults; independently advancing Play; bounded senses; multiple legitimate endings; headless authoritative world; fixed-camera visual experiment |
| **Proposed design** | Power/Rage default values, action tier costs, resource rewards, binding drain, separate Director, NPC state machine and dialogue policy |
| **Empirical hypothesis** | Distinguishing cause is fun; ghost feels fair; repeated play produces meaningful choices; cross-platform playback truly matches; visual differences remain legible |
| **Blocking design ambiguity** | Missing event accounting and settlement precedence; unpinned exact step order and numeric semantics; incomplete replay identity; no time-bounded lethal-warning counterplay test |
| **Speculative/deferred option** | Full five-tier action catalog, advanced visual physics, a second complete Adventure, multiplayer, fully dynamic dialogue, broad authoring toolchain |

"Blocking" means **block contract adoption or a corresponding implementation checkpoint until specified**, not a claim of failed current gameplay code. Stage 0 documents are explicitly DRAFT.

## Evidence

### Pinned material and independent receipt

Inspected source documents in the handoff's required order, all at `65f470e1c821fcf8c9be85fa0d58399587aabfdb`:

| Source and review anchor | Git blob | Why it matters |
| --- | --- | --- |
| [Original game design, `3–4, `5–14](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md) | `26feee1402341b08eb2af8b09ed954a757874b10` | Ghost economics, Show and simulation clocks, physical consequences, NPCs, Play, replay |
| [V0 planned contracts, C00–C12](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md) | `f0e09572f6eae5701650241e1ab4ac93405ac7b2` | Planned owners and negative-case classes |
| [V0 gameplay](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_GAMEPLAY.md) | `35dd5e67fa9f82e45eb3455cd711e4329ff109d3` | Rehearsal and world truth, outcomes, false positives |
| [Design decision register](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_DECISION_REGISTER.md) | `97b5e526c15fe258cceedb6f113f6f4433121ccc` | Direction D-001..D-009 and proposals P-001..P-010; open questions |
| [Vocabulary](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/TERMINOLOGY.md) | `ec7cdc68ceb919f92afd5b1ae8fc18560dc6361c` | Avoid confusing Room, Stage, Shot, Scene, Play, Performance, Run |
| [Stage 1 visual-direction trial](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE1_VISUAL_DIRECTION.md) | `03abd7d16981249a6879c3bc597e98a4d9758358` | Fixed-camera, cues, alternative render styles and discoverability |
| [Roadmap Stage 0–8](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/ROADMAP.md) | `7ae90a7eac87ca123d9c578b99f33743d893ec1c` | Intentional stage ordering, Stage 2 minimal loop, no release plan |

Also inspected the pinned repository `AGENTS.md`, `README.md`, `docs/ARCHITECTURE.md`, `packages/core/src/index.ts`, the sole bootstrap test, Pixi smoke entrypoint and `.github/workflows/check.yml`. The core source is only a module-identity marker. **No Ghost, stagehand, incident, saved Run or gameplay simulation exists in this revision.** GitHub [Actions run 42733045152](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/actions/runs/42733045152) is **SUCCESS** for the exact source pin: `npm run check`, **1/1 Node test**, web build/typecheck. The single test confirms the headless core package loads without the renderer; it does **not** certify economics, browser/Node replay, fairness, power balance or any future play loop. Run contents were inspected; no new gameplay tests were independently executed.

**Independent arithmetic only** was recomputed from GDD `4.3 and `4.6. No executable simulation, hidden scenario, seeded fixture, source-code patch, playable experiment, benchmark, human study, or other agent proposal was run/read.

### Ranked finding 1 — BLOCKING FOR C04: incident identity is not a conserved reward claim

**Sources:** GDD §4.3 ("Outcome reward" maximum 12 Power per incident; cost on commit, +10 Rage on thwart), §4.5 decision cycle, §4.7 causality; planned C01/C02/C04; V0 gameplay "ghost's opposing loop."

**Gap:** "Once per incident" is a necessary but insufficient invariant. Nothing yet fixes the ownership/uniqueness of realized consequences. One action may release a restraint, injure an actor, break a prop and disrupt three Play Beats. These are multiple world events from **one causal plan**, not four independently rewardable ghost achievements. Conversely two distinct plans may causally contribute to one outcome. Without a settlement ledger, a designer can accidentally farm distinct incident IDs for one lasting condition, or credit a ghost for an ordinary mechanical failure. A valid world consequence must exist *before* it can be claimed as an earned ghost outcome.

**Propose the smallest coherent contract:** each committed Ghost plan gets a unique `incident_id`, one authoritative `commit` event, the charged cost and target/precondition snapshot, and a causal parent link from every downstream physical event. Every independently rewardable achieved objective has a stable `outcome_claim_id` which must be settled at most once across the Run. Event IDs, incident IDs and outcome IDs serve **different purposes**. A single settlement for each incident declares one terminal status (`achieved`, `thwarted`, `partial`, `expired/aborted`) plus explicit reward/Rage eligibility, bounded credits and a reason. Decide whether `partial` can yield both reduced reward and Rage; do not silently infer yes or no. Duration-based Fear cannot continuously generate fresh rewards without a genuinely new, separately funded and caused incident. Re-reading replay data never settles twice. Pending rewards during binding need explicit handling.

**Falsifiers:** one sabotage, multiple injuries and cue failures should not exceed the explicitly configured **per-incident** reward cap; two different incidents must not both claim the same ordinary damage; replaying the same outcome, saving/reloading, or receiving delayed downstream consequences must not pay again. An actual unrelated equipment defect yields zero Ghost Power even when the ghost wished it would happen.

**Tradeoff:** extra identifiers/settlement bookkeeping, but substantially simpler debugging and no opaque Power farm. Avoid a full generic provenance-graph engine in Stage 0: one incident ledger and one causal parent/claim key suffice to demonstrate the invariant.

### Ranked finding 2 — BLOCKING FOR C00/C04/C05: time and event precedence are undefined at the edges

**Sources:** GDD `4.5 commit cycle, `4.6 binding, `7.3 two clocks; planned C00/C01/C04/C05; GDD `11 first Adventure.

**Gap:** The narrative says "advance world/show, sense, choose, commit, warn, execute, reward, repeat." But the contracts do not yet define the exact same-tick precedence for: player-command reception; Ghost/Director eligibility; regeneration; action affordability; committed costs; warning publication; physical effect; outcome settlement; Rage increment; binding activation; seal failure; Power zero; and Show Cue progression. These orderings can change **whether an actor dies** or **whether a binding wins**, even with the same seed.

**Necessary design decisions, not assumed answers:** define one written step-phase table, with a single authoritative tick and a mapping from performance time to simulation ticks. Keep one PRNG progression owned by the resolver. A Ghost cannot fund a current-tick attack with future regen or an outcome not yet achieved. A warning with no intervening legal response window is not meaningful counterplay. A player who completes a seal on the same tick as lethal impact should receive a predeclared ordering, not a scenario-author preference. At Power zero with valid binding, specify whether containment resolves before/after same-tick seal break; the trace must show the decision. Pausing a scene, actor refusal, and failed Cue cannot leave the Performance clock waiting forever while Ghost regeneration and attacks continue without an authored timeout/outcome policy.

**Tradeoff:** a short precedence table constrains creative edge cases, but protects determinism, causality, safety signals and authored fairness. Do not invent independent asynchronous clocks in Stage 0.

### Ranked finding 3 — BLOCKING FOR C11: "same seed" is not a complete replay identity

**Sources:** planned C00/C01/C11, GDD `9.4 RunRecord, `12 CP0; decision-register P-002 and Open Call 6.

**Gap:** Seed, PRNG state, versions and ordered commands are named, which is correct but not yet sufficient to make replay a falsifiable contract. A deterministic run depends on *all* rules, authored content, initial state, input validity and order, which exact tick each command applies, PRNG algorithm/state-transition and draw ordering, and numeric/serialization semantics. Render settings may not be in the authoritative identity, but a renderer must not use the core's decision PRNG stream.

**Minimum proposal:** identify a canonical replay tuple

    (resolver/version, module content hashes, rules config hash,
     initial authoritative state/hash, PRNG algorithm+version+state,
     fixed tick duration/ordering version, ordered actor-origin commands
     including rejected/stale inputs and effective ticks)

with deterministic tie-breaks, a defined canonical event and state hash and explicit verification against snapshots. A seed alone cannot reproduce two runs with different player commands; a module name/version is insufficient if its bytes change. Define the value representation/precision and how fixed-step fractional regeneration is accumulated without drift; integer resource subunits or a rational remainder accumulator are reasonable *alternatives*, not ratified implementations. No host-dependent wall-clock, locale sorting, unseeded random, renderer callbacks or JSON float/string normalization can silently influence authoritative outcomes. Unknown replay schema or version mismatch must report incompatibility, not silently reinterpret an old Run.

**Falsifiers:** same complete tuple in Node and supported browser yields equivalent canonical event/state hashes. Changing only visual style **while feeding identical commands** must not change core trace. Changing a hidden player item while holding the Ghost's observation history fixed must not change the Ghost plan selection if that item is truly unobserved; otherwise omniscience leaked through policy input. Swapping input order or content hash must either change the declared replay identity or fail compatibility.

**Tradeoff:** explicit reproducibility contracts before code costs less than retrofitting saves and forensic traces. Exact byte-equivalence requires canonical encoding; if that cannot be supported yet, define an exact integer-domain state oracle rather than promising unspecified "same logical result."

### Ranked finding 4 — BLOCKING FOR LETHAL FAIRNESS: "learnable" is not time-bounded

**Sources:** GDD §4.4 Tier II, §4.7 danger fairness, §10 camera; Stage 1 legibility; planned C02/C05/C10.

**Gap:** The GDD explicitly permits Tier II interference (cost 15) to become lethal by releasing large **ordinary stored energy**, while Tier III sabotage costs 28. That is consistent with the rule that tier is not severity, but means cost/tier **cannot** serve as a lethal threat's fairness proxy. "A clue existed" is inadequate if the clue was obscured or unreachable before an impact.

**Proposal:** a lethal-hazard fixture must show one **legally achievable counterfactual** from a declared reachable starting state: pre-impact observable cue (or a clear voluntary pre-risk commitment), time to interpret, traverse and perform a permitted mitigating action, and an impact time whose order is resolved by C00. A clue that requires 30 ticks of traversal and inspection but appears only 5 ticks before impact does not constitute viable first-run counterplay. Show the player's available observations at the decision point, not the omniscient debug truth. For unavoidable consequences following earlier poor player decisions, preserve the earlier warning/choice causal chain. Alternate cues (visual, audio, text, reduced motion) must not silently erase the only warning.

**Falsifier:** a physically valid restrained chandelier drops lethally in the same tick as its first perceptible warning; this violates a generic "fair surprise" claim even if the complete replay graph is correct. Another fixture has an earlier inspectable loosened latch and legal bracing route; lethal consequences after the player ignores it can be fair. The exact warning window thresholds require playtest-informed human constraints, not invented constants.

**Tradeoff:** may limit stealthy instant kills, but preserves suspense through uncertain source rather than impossible reaction timing.

### Ranked finding 5 — IMPORTANT: Director and Ghost must not accidentally form one omniscient policy

**Sources:** GDD `4.1–4.2, `4.5; planned C04/C05; decision-register P-001.

**Gap:** The Ghost's sensory input is bounded. The Director's "observable intensity state" and pressure cadence are less precisely scoped. If the Director schedules pressure based on hidden player plans or hand-picks a countermeasure, the Ghost can appear to know information it never sensed even though the direct Ghost API is clean.

**Recommendation:** distinguish `GhostObservation` (only sensed/recalled facts) from `DirectorPacingState` (permitted pressure history, safety/recovery budget, time, current committed incidents). The Director may **veto or delay** a legally selected attack but may not manufacture a new Ghost intent or target from unseen player inventory. If the Director needs full world state to prevent unfair outcomes, its use is limited to *safety veto* and must be logged; it cannot use the same fact to choose a more lethal attack. Verify identical perceived Ghost history and PRNG inputs produce the same eligible plan set despite changed hidden player inventory.

**Tradeoff:** an extra policy projection, but it can be one pure eligibility filter rather than an independently implemented strategic "AI." Defer any second adaptive scheduler until evidence demands it.

### Ranked finding 6 — IMPORTANT: proposed Power/Rage values permit two very different incentives

**Sources:** GDD §4.3 defaults, §4.4 tiers, §4.6 binding; decision-register P-003/P-008. These are **conditional mathematical consequences of provisional values, not measured balance results**.

    Pmax=100, Pstart=18
    Rstart=20, Rmax=100
    regeneration(R)=6*(1+R/100) Power/min (unbound)
    Rage per thwarted committed plan = +10
    reward cap per attributable incident = 12 Power
    sample costs: I=6, II=15, III=28, IV=48, V=75
    binding drain=45 Power/min when valid

At Rage 20, regen=7.2 Power/min, at Rage 30 it is 7.8, at Rage 100 it is 12. One +10 Rage thwart increases future regen by **only 0.6 Power/min**, at most +3 Power over five uncapped minutes, +6 over ten. It does not instantly replenish an attack. A state at Power 18 that waits without spending, earning rewards or being interrupted reaches: tier III cost 28 at **1m23s**, tier IV cost 48 at **4m10s**, tier V cost 75 at **7m55s**. For an 8–12-minute prototype, tier V may require near-total hoarding until very late; this is not automatically bad, but challenges an assumption of continual escalation.

**Profitable loop counterexample:** if Tier I's 6-Power disturbance could earn the full capped 12-Power reward after an easily repeatable event, it yields **+6 net Power** before regen. Fourteen such genuinely claimable incidents would mathematically raise 18 to the 100 cap absent intervening restrictions. This is only **possible under unspecified reward eligibility, repeated legal action opportunities and suitable outcomes**; not evidence a built Ghost exploits it. The Director may also prevent such frequency. Do not solve this by automatically making every action net-negative; meaningful successful plans may deserve a return. Instead define what success earns and how often, compare outcomes and decide an intended recovery regime.

**Tier dominance test:** Tier II's switch release can cause huge physical damage at cost15; if Tier III sabotage at cost28 has the same prerequisites, warnings, opportunity and result in a given Venue, the cheaper action dominates it. That can be legitimate for that specific Venue, but if universal, the nominal ladder has no strategic diversity. Distinguish access, escalation setup, stealth, counterplay, expected payoff and cooldowns before committing all five tiers.

**Binding:** with constant valid seal, suppressed regen/rewards and no defensive spending, 18 Power drains to zero in **24 seconds**, and 100 Power in **133⅓ seconds**. Those are upper bounds on no-defense *drain time* for the proposed values, not on gameplay duration if seal breaks. A bind at Power0 resolves immediately by the stated outcome rule. Whether escape commitment can occur before a coincident zero threshold must be written in the C00 phase ordering. "Defensive spend" might accelerate exhaustion but may also break the seal and restore regen. Test both branches.

**Recommendation:** retain all numeric values as data and experiments. Require hard invariants (no underflow, unique payout, no ghost earnings from mundane faults, no invalid spending), and measure soft properties (Tier usage, how often an action is affordable, waiting policy, Power occupancy at cap, observed inter-threat intervals, costs per achieved outcome, net growth per incident) **before** adopting balances. "Regenerates faster after thwarting" is analytically true but not enough to demonstrate a satisfying comeback loop.

### Ranked finding 7 — IMPORTANT: two truths require observational projection, not merely a complete debug ledger

**Sources:** GDD §3.1, §6, §7, §8 and §10; V0 gameplay "two truths"; Stage 1 visual trials.

**Gap:** Rehearsal truth (intended Cue) and World truth (actual physical consequence) are correctly separate. The player's **accessible evidence** is a third necessary object for design verification, even if it is only a view/projection and not another persistent world authority. Actor and Ghost perceptions must be derived separately from authorized sensors/observations. A flawless debug causal trace does not prove players could have diagnosed the event. A legitimate revised Cue needs a discoverable version/revision provenance; otherwise an apparent false positive is indistinguishable from author fiat. A correct intervention that makes a legitimate Cue worse must have predecision evidence of what was expected, not retrospectively changed rules.

**Recommendation:** define three questions for every diagnostic case: what the Play intended at this revision, what the world actually did, and what the stagehand or Actor *could observe by this tick*. Log the exact observation(s) exposed to each entity and accessible alternate cues separately from hidden truth. Do not reveal the full Ghost ledger to the player. Maintain stable physical truth across Art Pack swaps under identical commands, while **separately testing** whether different visual profiles make the same hazards detectable to real players.

**Falsifier:** a "normal" rehearsal cue with no accessible cue-book revision is visually identical to sabotage, and the player gets punished for intervening despite no discriminating legal evidence. This is not a fair mystery regardless of replay determinism.

### Ranked finding 8 — IMPORTANT: Stage 2 minimum is smaller than the v0.1 vertical slice; keep it smaller

**Sources:** ROADMAP Stage 2 (one Room, one mechanism, one legitimate Cue and suspicious deviation); GDD `11 ("first playable Adventure" 8–12 minutes, three mechanism classes, five Beats, Ghost, binding route) and `12 CP0–CP5. These are **different checkpoints**, not necessarily contradictory, but share phrases like "first playable."

**Recommendation:** explicitly call Stage 2 the **heartbeat falsification micro-slice** and GDD §11 the **later Adventure vertical slice**. Stage 2 must include an ordinary false alarm/legitimate action pair, but not a full Ghost resource economy: a manually specified (but world-valid) suspicious cause can initially test interpretation. If the micro-slice is dull, fix timing, observability or the player's verbs before adding NPC psychological states, five tiers, AI planning, full binding, large cast and art packs. Avoid enshrining "exactly one false alarm each seed" as a detectable procedural rule; required coverage in test fixtures is not necessarily runtime frequency distribution.

**Tradeoff:** less impressive demo, much stronger evidence about the core fun promise. Full architecture/swappability should be proved later with a second genuinely distinct Adventure, not imposed on the first room.

## Proposed analytic invariants before C00/C04/C05/C11 adoption

**R1 — Resource conservation:** A canonical Power ledger reconciles all per-step changes: authorized prior balance, credited passive regen, newly committed legal costs, *unique* achieved rewards, and valid containment drain, with cap/overflow accounted and intermediate affordability enforced. One committed action has one debit; no action can spend future credits. Power always finite and in [0,100] for the sample rules. An "overflow lost to cap" diagnostic is not hidden reward storage. Rage finite and bounded; success and thwart statuses must have declared effects.

**R2 — Incident conservation:** Every credited reward has (i) a committed incident; (ii) an independently authoritative outcome/world event; (iii) a unique settled claim; (iv) positive eligibility under that incident's rule; (v) no previous settlement. Double-reward claims, recycled IDs, reloaded rewards, attributed mundane faults and fresh reward ticks for lingering Fear are invalid.

**R3 — Ghost knowledge isolation:** If two states differ only in information outside the Ghost's permitted observations/learned memory, then with the same Ghost-visible history and permitted PRNG state the eligible choices cannot depend on those differences. The Director may use world truth only for declared safety veto, not targeting or new intent.

**R4 — Director noninterference:** The Director can delay or reject eligible pressure, not create cost-free actions, reset a success, move Clues, change a recorded outcome or silently heal Ghost resources. A thwarted incident stays thwarted; later attacks must independently pay their own cost.

**R5 — Clock identity:** Exactly one authoritative fixed-step sequence; performance timing is a derived, documented mapping with explicit pause/fallback. Input order, tick/phase priority, time-unit arithmetic, regen remainders and simultaneous-event tie-break are stable under replay and unrelated to visual frame rate.

**R6 — Causal harm:** Every Health/Integrity change comes from a legal world event with causal source, state and tick. Ghost-caused physical changes need not be directly magical damage; ordinary stored loads are allowed. No unidentified direct HP subtraction.

**R7 — Lethal counterplay reachability:** A fixture declared fair admits at least one evidenced, legally timed avoidance/mitigation path from its specified observable decision state, unless it is an explicit downstream consequence of an earlier disclosed choice. Outcome is allowed to be fatal when the player ignores/delays a viable intervention. Record path/inspection/action costs and observation availability; assess accessibility variants.

**R8 — Replay and content parity:** Identical full replay tuple produces the same canonical authoritative state and causal events across supported hosts, independent of render frames or Art Pack, for identical command input. An unknown content/schema revision fails clearly; changing commands, including rejected inputs, changes the declared replay identity. This does **not** mean different artwork gives human players identical choices.

**R9 — Distinct outcomes:** Performance, People, Haunting and Player remain separately reportable; the Fifth Bell can legitimately lose the show while saving a person. No single opaque "victory score" can erase that distinction.

## Negative-fixture and experiment matrix — all proposed, zero executed

| ID | Target/falsifier | Required evidence / pass condition |
| --- | --- | --- |
| **G-SF-01** Free intervention | Ghost with Power below cost attempts action (including multiple same-tick commands) | No commit or world effect; no underflow; reason in authoritative event log |
| **G-SF-02** Invalid plan after intent | Target becomes inaccessible/destroyed between selection and commit | Cancel/reject according to phase order; no effect without valid preconditions; charge only on *actual* commit |
| **G-SF-03** Achievement double payout | One incident triggers prop damage, actor injury and two beat failures; repeat outcome delivery | Single bounded incident settlement; same underlying claimed outcome not credited twice |
| **G-SF-04** Mundane masquerade | Ordinary Cue/loose bolt causes damage while Ghost had considered similar target | No reward or Rage attributed to Ghost, even if impact helped its objective |
| **G-SF-05** Thwart after commitment | Real Ghost action commits, player braces mechanism before effect | Cost remains spent; one declared Rage increment; no Director free replacement; any residual physical risk is causally explicit |
| **G-SF-06** Success/partial/thwart collision | Ghost partially disrupts cue but player saves actor and prevents planned main effect | One unambiguous settlement class/payout/Rage priority; no disguised duplicate incident |
| **G-SF-07** Cheap-action Power farm | Repeat inexpensive, genuinely legal Tier I outcomes at highest allowable reward | Detect sustainable net-positive cycle; decide consciously whether valid, cap-frequency/eligibility if not intended; record action opportunities and Power trajectory |
| **G-SF-08** Bind zero race | Seal breaks on same tick Power drains to zero; delayed reward also arrives | Predeclared resolution and credit suppression order reproduces; no timing-dependent contradictory outcome |
| **G-SF-09** Stalled show | Actor refuses Cue, Show Controller awaits contingency while simulation continues | Authored timeout, cancellation, substitution or recovery; no infinite waiting exploit hidden behind ticking regen |
| **G-SF-10** Ghost omniscience metamorphism | Change unseen inventory/route while holding ghost-visible observations and PRNG history constant | Same eligible Ghost decisions; Director does not covertly retarget |
| **G-SF-11** Exact replay identity | Two identical initial states, source hashes, explicit RNG version/state, command list and tick rules, Node versus browser | Same authoritative event/state hashes; different visuals leave causal output unchanged for identical input |
| **G-SF-12** Deadly but physically legal cue | First perceivable sign occurs only after mitigation deadline, e.g. 5 warning ticks vs 30 necessary action ticks | Fixture **fails fairness gate** even if world physical causation and Ghost Power are valid |
| **G-SF-13** Legitimate vs Ghost lookalikes | Same visible early chandelier sway, one legal Cue revision/ordinary fault, one Ghost interference | At least one discoverable, timely discriminant; deliberate nonintervention can be correct; false repair can carry authored cost |
| **G-SF-14** Visual/accessibility metamorphism | Two Art Packs / reduced motion / alternate subtitle cues, same world trace | Causal simulation parity **and** essential warnings remain accessible in each supported mode |
| **G-SF-15** Outcome independence | Save cast by Fifth Bell while show fails; bind Ghost after Play collapses | Multi-axis outcome correctly recorded; no synthesized perfect score |
| **G-SF-16** Cost-effective observation | Player takes an Inspect action that cannot affect any current hypothesis | Instrumentation surfaces what was learned versus time spent; if no discriminating use, design may remove the redundant action |

**Important:** None of these tests has passed. They are design requirements. A hypothetical fixture is not an instantiated examination or secret answer key.

## Instrumentation plan: hard invariants vs soft experience

**Headless hard gates:** nonnegative bounded resources; exact debit and unique payout; stable causal chain; no unobserved Ghost targeting; no Director synthetic attacks; deterministic step/replay; no impossible NPC speech; all mandated clue routes are reachable; legal source/command handling; no frame-derived world mutation. Any reproducible violating trace blocks the corresponding contract checkpoint.

**Quantitative diagnostic metrics (to discover patterns, not substitute for fun):**
- Power/time trajectories and dwell at cap or exhaustion, Rage distribution, positive/negative net Power per funded incident, credit causality and rejected action rates.
- Time to earliest affordable Tier by policy, time between legitimately scheduled threats, eligible-plan count, fraction of plans blocked by Director and why, incidence of "ghost waits despite affordable actions."
- Incident outcome mix (prevented/achieved/partial), failed intervention rate, valid/no-op action decisions, claim uniqueness and causal fanout.
- Distribution of **warning-to-impact opportunity** in simulation ticks, minimum legal traversal/inspection/mitigation ticks, and whether multiple accessible modalities exist.
- Per-Run distinct state transitions, resulting Play branches and authored dialogue repetition **when later implemented**.
- Replay discrepancies categorized by source tuple, event index, seed/PRNG draw index, host and numeric serialization.

**Human playtest outcomes require humans:** informed choice versus random repair-clicking, recognition of ordinary Cue without hindsight, sense of fairness when killed, cast legibility, meaningful regret/learning, fear versus annoyance, confidence calibration and *whether the intervention decision was enjoyable*. Headless metrics cannot prove dread, fun or perceived fairness.

**Stage 2 falsification trial:** two or more authored cases matched for visible initial cue, time budget and mechanism; one legitimate/ordinary, one Ghost-caused (or simulated disturbance). Give participants the same affordances and **no debug truth**. Log what they inspected, their stated hypothesis and uncertainty, their chosen action/nonaction and resultant world events. Pre-register task success as correctly justifying a consequential choice using accessible clues, not collecting every object or always choosing to intervene. Separate diagnosis and decision consequences. Do not fit thresholds from the same trial used to announce success; iterate then run held-out cases. Later Stage 4 can introduce actual adversarial Ghost choices.

**Statistical/reporting discipline:** Specify sampling of scenarios and seeds, stopped/failed runs, source versions, denominator and uncertainty. An empty dataset has no balance verdict. A passing single-seed baseline does not imply a fair player experience. Do not assign arbitrary pass percentages, "10 FPS budget" or trauma/safety scores without choosing a device, study or criterion.

## Alternatives and deletions

1. **Keep Director as a pure pacing/eligibility filter initially**, not a second adaptive planner with hidden targeting. If a single bounded Ghost policy plus immutable warning constraints passes the test, a complex Director architecture is needless. Tradeoff: fewer nuanced recovery beats until an empirical need appears.
2. **Use one mechanism and two causal explanations before the full Adventure.** Test ordinary and ghost-looking effects first. Stage 0/2 does not need an entire five-tier implementation, binding state machine, elaborate NPC psychometrics or multi-Scene authoring.
3. **Prefer a compact incident settlement table over a generic graph database.** Track immutable ID/cause/commit/cost/outcome/reward/Rage and one claim uniqueness rule; expand only for a demonstrated multi-plan ambiguity.
4. **Preserve explicit source pins but postpone full save-file migration machinery.** CP0 needs an inspectable canonical replay and a rejection reason for unsupported versions; permanent format compatibility belongs to actual save-feature scope.
5. **Do not replace the causal world with a fairness script.** The Director may withhold or delay an illegal/unfair attack but never secretly change physical outcomes or force damage. The more defensible alternative is to make the intended survival options part of authored state/rules and log the veto.

## What should remain unchanged

- **Physically present stagehand, not omnipotent cursor.** Costly movement and proximity make diagnosis consequential.
- **Rehearsal truth versus world truth.** Sometimes the show really is doing the expected thing, and stopping it is harmful.
- **Ghost hostility and bounded senses.** It may try to kill; difficulty must arise from legal mechanisms and observed learning rather than cheating.
- **Authoritative simulation with render-only Pixi.** If the camera changes, no world event changes from that alone.
- **No mandatory binding victory.** Curtain call, Fifth Bell, people and haunting outcomes remain separable and plausible.
- **Actor versus Role, authored deterministic dialogue.** Local knowledge and competent refusal matter more than arbitrary Fear/Trust meters.
- **Explicitly staged proof and no release calendar.** Mothlight's restraint about not claiming a game already exists is correct.

## Unresolved dissent, uncertainty and acceptance recommendation

**Dissent 1 — cost versus danger:** I do **not** recommend an artificial "Tier II cannot be lethal" rule. It would contradict the game's physical causal premise. A cheap move may release ordinary stored energy, but that should entail defensible access, setup, warning and counterplay costs. The reviewer must measure exploitability instead of imposing an arbitrary tier-damage correlation.

**Dissent 2 — success must not always be profitable:** I do **not** recommend blanket negative returns. A resource-owning antagonist may sensibly gain Power from achieved harm. The concerning condition is an *uninteresting, repeatable, low-risk, self-funding action* that defeats the intended pace.

**Dissent 3 — determinism isn't suspense:** Exact authoritative replay is valuable, but if all scenarios are mechanically obvious or diagnostic clues arrive too late, the game can be reproducibly dull or unfair. A successful hard-gate run does not pass a player-experience gate.

**Unresolved owner/Mothlight decisions:** (1) Is `partial` incident resolution mutually exclusive with `thwart` and Power rewards? (2) How can multiple distinct incidents claim one physical effect? (3) Which ordering wins binding-versus-seal break on one tick? (4) What numeric scheme keeps regen deterministic cross-runtime? (5) When may Director use global world data for safety veto without informational leakage? (6) Does Stage 2 intentionally omit a strategic Ghost? (7) What conditions turn a lethal hazard into a fair consequence of earlier player choice? (8) What actual player decision would make the initial inspection loop *fun*, independent of anxiety and mechanics volume?

**Verdict:** **CONDITIONAL PASS** for established Stage Fright direction and roadmap separation. **REQUEST CHANGES for adoption of C04/C05/C11 plus lethal-fairness criteria**: pin a settlement/claim table, step-phase precedence including two clocks/binding, a complete replay tuple and one counterfactual lethal-warning test. The appropriate next implementation authorization remains with the human owner, not this review. The current repository has neither a gameplay runtime nor evidence of playtested balance. Do not mistake this design review for a failed implementation or a certification.

**Authorship/provenance:** Submitted in Gauge's authorial perspective within a ChatGPT conversation. GitHub account activity is a shared authentication route, not proof of an independently running agent instance. Handoff independence preserved: **no other of the six first-pass Stage Fright reports were read**. No game repository writes, PR, issue commentary, profile changes, engine code, art generation or merger performed.

## Revisit when

Mothlight reconciles six independent reports with preserved dissent, C00/C04/C05/C11 is proposed for adoption, a real Stage 2 test produces observed player choices, Stage 4 implements a minimal Ghost, a reproducible RunRecord and actual browser/Node fixtures exist, or the owner changes the physical-danger premise. On subsequent reviews pin the new exact application revision and rerun real controls instead of promoting these theoretical cases to observed defects.

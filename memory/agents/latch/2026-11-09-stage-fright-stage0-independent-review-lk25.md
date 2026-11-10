---
schema: 1
id: 2026-11-09-stage-fright-stage0-independent-review-lk25
kind: handoff
scope: agent:latch
status: active
evidence: inferred
author: latch-stage-fright-independent-review-2026-11-09
created: 2026-11-09
updated: 2026-11-09
sources: "Mothlight STAGE-FRIGHT-V0-REVIEW-01 handoff at 09164e820264b7502de58e87d0f31ab5f166592f, blob 3bdc0168da0e1a8e1d128820dd0eb4e3fd628ae3; mandatory source docs inspected at exact 65f470e1c821fcf8c9be85fa0d58399587aabfdb: GDD, V0_PLANNED_CONTRACTS, V0_GAMEPLAY, V0_DECISION_REGISTER, TERMINOLOGY, STAGE1_VISUAL_DIRECTION, ROADMAP; Latch home agents/latch-v1 at 16525054c8827c52d10ce2b2f12825b867c96fae. Design inspection only; no tests, no other STAGE0 reviewer reports."
---

# Latch — STAGE-FRIGHT-V0-REVIEW-01 independent design review

**Agent:** Latch — The Locksmith (`character_id=latch`), individual source branch `cosmicdance-4-2-0/KestrelGaming@agents/latch-v1`, inspected at `16525054c8827c52d10ce2b2f12825b867c96fae`. `agents/latch/AGENT.md` blob `21537a7feeab66574ab374f807ce68acfeb6dc94`.  
**Target repository:** `cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT`.  
**Review handoff:** `docs/reviews/STAGE0_SIX_AGENT_HANDOFF.md` at `09164e820264b7502de58e87d0f31ab5f166592f`.  
**Authoritative design source pin:** **`65f470e1c821fcf8c9be85fa0d58399587aabfdb`**, exactly as instructed.  
**Mode/status:** Independent Stage 0 documentation review; no implementation and no gameplay execution.  
**Verdict:** **ACCEPT WITH CHANGES** on proposed direction; **two contract ambiguities block Stage 0 acceptance** until expressly resolved, and implementation is not authorized by this verdict.  
**Independence/provenance:** This review was formed without examining the other five Stage Fright review outputs or their contents. The GitHub connection uses a common account; this text is the attributed Latch *authorial perspective*, not cryptographically authenticated multi-agent execution or consensus.

## Summary

The key fun promise is **competent, situated stagecraft under uncertainty**: a real performance continues; a Ghost can interfere through physically and causally grounded mechanisms; the stagehand can distinguish rehearsal, ordinary fault and haunting through intelligible evidence, then act or refrain and witness consequential results. The essential test is **one mechanism, two plausible causes, a meaningful discriminating observation, and a decision with visible consequences**—not a large ghost skill tree.

The design has commendable established direction: headless deterministic world truth, no gameplay LLM, a physically present player, legitimate cues that can resemble sabotage, independent performance/people/haunting/player outcomes, bounded Ghost knowledge and a non-omnipotent Director. However the documented interfaces leave unresolved **whose command wins when valid intentions conflict** and **whether Ghost/Director decisions can obtain private world knowledge through scoring or pacing inputs**. Those should be resolved as minimal ownership rules before implementing mechanics. Important follow-ups concern consequential warning availability, incident reward bookkeeping, authored Adventure/assets as untrusted input, replay lineage, cast refusal and a mislabeled illustrative manifest field. None is a proven runtime vulnerability.

## Evidence

### Source receipt (original documents, exact pinned revision)

- [Original GDD §0–4](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md): established direction, §3 heartbeat, §4 Ghost and Director, power/reward/resource and warning model; §6 actor/role; §7 authored Play; §8 dialogue; §9 manifest example; §10 presentation; §11 proposed vertical slice.
- [V0 Planned Contracts §Authority, C00–C12](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md): fixed-step action and world ownership; Ghost, Director and knowledge rules; data-only Adventure boundary; replay and prospective multiplayer.
- [V0 Gameplay §heartbeat, Ghost loop, two truths, outcomes and Last Waltz](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_GAMEPLAY.md): playable intentions and negative design examples.
- [V0 Decision Register D-001–D-009, P-001–P-010, trial matrix](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_DECISION_REGISTER.md): distinguishes user-approved direction from unratified mechanism.
- [Terminology](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/TERMINOLOGY.md): Scene is dramatic Play content; Room is navigation; Shot is view.
- [Stage 1 Visual Direction §Visual Profile, legibility gates](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE1_VISUAL_DIRECTION.md): planned alternate art styles and nonauthoritative presentation.
- [Roadmap Stage 0–8](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/ROADMAP.md): Stage 0 documentation only, Stage 2 player-loop experiment before sophisticated Ghost behavior, deferred releases.
- Latch's source perspective: [AGENT.md](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/16525054c8827c52d10ce2b2f12825b867c96fae/agents/latch/AGENT.md). The review is source inspection, not code execution.

**Classification key:** DIRECTION = project-recorded established design; PROPOSAL = candidate mechanism; HYPOTHESIS = not experimentally demonstrated; BLOCKING = under-specified design that must be resolved before contract acceptance; IMPORTANT / OPTIONAL = priority for reconciliation, not confirmed shipped defects.

## Most important promise and smallest falsifier

**DIRECTION:** The player is physically present; rehearsed cues can look haunted; the Ghost has finite, locally grounded means; the performance continues. This permits expertise to improve judgment rather than just checklist speed.

**HYPOTHESIS:** Recognition and timely, calibrated intervention feel good because players can learn mechanical and dramatic causes.

**Smallest proposed falsifier, not run:** One Room/Shot plus reachable backstage operation, one chandelier restraint and one scheduled cue, one actor and two initially similar observable anomalies: (A) a legitimate approved cue revision; (B) a Ghost-financed premature release with causal world consequences. Before an irreversible harmful outcome, offer a discoverable distinction with known time cost, plus a safe decision to warn/stop where appropriate. Capture what participants saw, their explanation, their choice, the elapsed time and resulting world/Play state. If all rational responses converge to blanket shutdown, random clicking or arbitrary guessing—or if the only distinguishing clue is inaccessible until after lethal consequence—the promise is not demonstrated. A headless trace proves logical fairness, **not** that the loop is enjoyable; human trials are still required. Avoid tuning to make a preselected answer look correct.

## Ranked findings

### B1 — BLOCKING design ambiguity: intent, execution and authority at a shared tick

**Sources:** `V0_PLANNED_CONTRACTS.md`, authority diagram and C00/C01/C03/C06/C07/C12; `STAGE_FRIGHT_DESIGN_v0.1.md` §4.5 deterministic cycle, §7.1 Show Controller and §8.2 dialogue; `V0_GAMEPLAY.md` heartbeat.

**Observed:** Core consumes *ordered actor-identified commands* but the texts do not yet specify who may issue each type of command, when an intent is accepted versus committed, and how same-tick conflicting commands resolve. An Actor is not the player's puppet: Communicate may request an action but cannot forcibly mutate another actor's choice. The Ghost commits and spends before a resulting physical effect. A rehearsed Cue may operate the same mechanism as the player and Ghost.

**Failure mode (hypothetical):** The stagehand braces the restraint, the Show Controller fires its rehearsed release, and the Ghost targets the same prop in one tick. Depending on undocumented subsystem iteration order, the world may double-release a latch, charge no Power, negate a legal rescue, or cause an irreproducible event. A malicious or malformed future Adventure might submit a command *as* an Actor or Ghost merely by naming its ID. Single-player is not immune to mistaken origin/authority.

**Smallest fix:** State in C01 that all intentions enter **one** deterministic resolution boundary. Record (conceptually) **source/issuer, acting entity, target, requested verb, intended tick, causal command identity**, and whether issuance is permitted. The resolver checks range/state/ownership and contextual ability, specifies acceptance/commit/effect ordering and same-tick conflict semantics, and emits an explicit rejection or conflict outcome. Actor decisions are first-class intentions, not automatic execution of a player request; scenario content never gains issuer authority by declaring identifiers. Define an order invariant, not a networking or authentication framework.

**Negative control:** Two opposing valid actions against one restraint in the same tick, ordered by a declared rule, replay identically; a duplicate or impersonated intent is rejected or idempotently resolved without a second effect. A legitimate player warning to an Actor can influence but not bypass their safety decision.

### B2 — BLOCKING design ambiguity: Ghost knowledge and privileged Director state

**Sources:** `STAGE_FRIGHT_DESIGN_v0.1.md` §4.1–4.5; `V0_PLANNED_CONTRACTS.md` C04–C05; `V0_DECISION_REGISTER.md` D-002/P-001.

**Observed:** The Ghost is forbidden to read hidden inventory/goals and must use defined senses, but plan scoring may consider the *current Play Beat*, actor vulnerabilities, target states and threats to its anchor. The Director controls pressure from an observable intensity state. The allowed origin and scope of those inputs—and whether privileged Director state can leak back to the Strategist—are not specified.

**Failure mode (hypothetical):** The Ghost immediately targets a hidden binding vessel in player inventory without seeing it. Or the Director quietly steers its legal-action list toward the player's undisclosed route because pacing reads the whole world, making the antagonist functionally omniscient despite apparently legal attack events.

**Smallest fix:** Specify two views: a Ghost **perception/knowledge projection** (directly sensed facts, explicitly granted lore, and remembered observations with timestamps) and a Director **pacing projection** (allowed pressure/fairness signals). The Director may use declared global fairness facts if required but can only emit eligibility/timing constraints, never hidden targets, hints or state mutations to the Ghost. Ghost score inputs must come from its authorized projection, including clear rules for what it already knows about the Play. Rules may be implemented in one code module; this is a dataflow boundary, not a mandate for separate autonomous agents.

**Negative control:** Same Ghost perception and memory, different *unseen* player inventories/routes → identical Ghost target selection; a real witnessed anchor threat can change it. Alter hidden player position while preserving Director-exposed pressure signals → no strategic information leak via scheduling. A changed legitimate Play cue known to Ghost only through prior declared lore or an observed event must not be silently inferred.

### I1 — IMPORTANT: fairness must follow *actual consequence*, not Ghost action tier

**Sources:** GDD §4.4 expressly permits inexpensive Tier II intervention to release lethal stored mechanical energy, and §4.7 forbids unavoidable untelegraphed death; `STAGE1_VISUAL_DIRECTION.md` §legibility.

**Risk:** If warning rules are keyed only to tier/cost, a cheap switch action may be lethal yet receive only a low-risk whisper cue. Conversely, demanding a specific visual clue can make a fixed Shot or accessibility mode unfair.

**Minimal disposition:** Define minimum *reachable, perceivable warning/escape opportunity* from the resulting world hazard's severity, timing, location and available player actions, independent of supernatural Power tier. At least one supported sensory route must satisfy the same hazard-response opportunity across target display/accessibility modes; the mystery can remain about the cause. Warning need not reveal the Ghost, only that a consequential choice is possible. An emergency Fifth Bell is a meaningful option, not proof every crisis is safely reversible.

**Counterexample:** The Ghost cheaply releases an already heavily loaded fixture behind a foreground occluder; no sight, sound, cue note, safe bypass or timely warning is accessible. Reject the scenario or add a fair source of information; do not solve it by secretly lowering damage after it occurs.

### I2 — IMPORTANT: reward attribution, cancellation and retries need one incident lifecycle

**Sources:** GDD §4.3–4.6; C01/C04/C05/C11 in planned contracts; `V0_GAMEPLAY.md` Ghost loop.

**Risk:** One Ghost-caused restraint release can indirectly cause actor fear, a missed Beat and injury. If each event independently awards Power, a single causal incident can farm rewards. If thwarted plans are retried or canceled under ambiguous commit semantics, Rage or spent Power could be paid twice. Ordinary faults must not feed the Ghost.

**Minimal disposition:** Define a stable incident identity, phase transitions (eligible → committed → resolved/thwarted/canceled as applicable), once-per-outcome accounting rules, attribution provenance, and explicit rejection of duplicate settlement. Enforce a reconciliation invariant: Ghost Power/Rage changes must follow committed costs and unique attributable settlements, with no direct Director grants. An eventual incident ledger may be a simple typed record; don't build a general event-sourcing framework for Stage 0.

**Negative controls:** A repeated animation notification, retried command, multi-effect chain, and ordinary lighting fault never each generate additional awards. Thwarting after legal commitment keeps the cost spent and may yield the defined Rage increase; a plan rejected before commitment must not pay a fake price.

### I3 — IMPORTANT: declarative Adventure assets are an *input trust boundary*

**Sources:** GDD §9.1–9.3; C09/C10 in planned contracts; `V0_DECISION_REGISTER.md` P-009/P-010.

**Risk:** A manifest declaring content as 'data' does not by itself make it safe. Future author-supplied files may contain references outside the pack, unsupported asset formats, malformed dependency graphs, very large resources, or strings that a later adapter treats as code. Trusting a declared capability name as evidence the referenced prop exists can permit impossible events or hidden rules changes.

**Minimal disposition:** Stage 0 should promise that any future third-party pack crosses a **validated, data-only loading boundary before run construction**: supported types/paths/versions, bounded references and sizes, a resolvable *required/provided capability* map, and no executable module import from third-party content. Art/audio may supply presentation, never authority, perception, collision, harm or world effects. Local first-party content may be curated without a premature general modding platform. Detailed asset allowlists and sandbox mechanisms are deferred until tooling exists.

**Negative controls:** Missing `suspended.fixture`, an invalid ref, a pack containing executable payload, or an Art Pack claiming to redefine interaction bounds fails validation with a specific reason. The same compatible Adventure with a new Visual Profile preserves the authoritative event trace and minimum hazard observability.

### I4 — IMPORTANT: replay requires *exact content identity*, not just visible version labels

**Sources:** GDD §9.4; `V0_PLANNED_CONTRACTS.md` C00/C01/C11/C12; roadmap Stage 7–8.

**Risk:** Replay may seem deterministic within one checkout while a Play file, dialogue table or tuned Ghost cost changes under the same displayed version. A saved run that loads 'latest compatible' may silently reinterpret history. Asset changes may alter warnings despite unchanged damage.

**Minimal disposition:** Pin or otherwise verify the exact authoritative content/tuning identity and rules interpretation used to resolve the Run, alongside initial state, deterministic PRNG, ordered accepted/rejected commands and causal event IDs. Specify canonical serialization/ordering only to the precision needed for logical replay across Node and browser. If the old content or interpreter isn't available, report **unsupported replay** rather than substitute new facts. Visual asset changes may be allowed for *presentation replay* if clearly labeled and if causal truth stays pinned; playable continuation requires validated semantics.

**Negative controls:** A duplicate command, unseen PRNG state change, rules-profile edit or same-label/different-byte content replacement changes or invalidates the replay verification; it cannot produce a falsely 'matching' accepted run.

### I5 — IMPORTANT: the cast's agency must not be overridden by a required dramatic Beat

**Sources:** GDD §6.1–6.4, §7.1–7.2, §8.2; C06–C08; `V0_DECISION_REGISTER.md` D-005.

**Risk:** A Role has required Beats; an Actor has injury, knowledge, trust, refusal and withdrawal. An author might write a mandatory entrance that makes the Show Controller teleport or speak an incapacitated Actor into compliance. A player 'Communicate' command might similarly overwrite a cast member's decision.

**Minimal disposition:** The Show Controller owns Beat obligations and legitimate fallback/cancellation outcomes, **never the Actor's body or knowledge**. Role requests become intentions considered by Actor state, location and physical ability; inability is an explicit, coherent Play consequence. Prefer a small authored contingency for an unavailable Actor over branching every psychological configuration.

**Negative controls:** An injured/unavailable Actor cannot move to stage or speak via a pending Cue; a frightened but trusting Actor *may* continue; a calm Actor may refuse unsafe rigging. Legitimate refusal does not permit a ghost to claim arbitrary rewards.

### I6 — IMPORTANT: visible warning and investigation affordances are part of the content contract

**Sources:** GDD §3, §7 and §10; `STAGE1_VISUAL_DIRECTION.md` §§visual/art and legibility; C03/C07/C10.

**Risk:** The headless state machine may be correct while a replacement camera Shot, Art Pack, reduced-motion configuration or audible-only cue makes a crucial observation inaccessible, so the game feels like capricious punishment.

**Minimal disposition:** A gameplay-critical fact should have a semantic observation path: which player location/state/sense yields it, how long it remains available, and its urgency. Presentation mappings can differ aesthetically but must preserve the declared *accessible evidence window* or report incompatibility in Adventure preflight. This is not a requirement to reveal every Ghost cause or put a glowing arrow above threats.

**Negative controls:** Replace style A with style B and an accessible reduced-motion treatment; check not only headless event equality but reachability of the warning before the deadline. One hidden camera view cannot be the sole route to survival.

### O1 — OPTIONAL documentation correction: `entry_scene: ballroom` contradicts vocabulary

**Sources:** GDD §9.2 sample manifest and `TERMINOLOGY.md` distinctions (Scene is dramatic Play content; Room is the navigation space; Shot is the camera framing).

**Observed issue:** The illustrative manifest uses `entry_scene: ballroom`, apparently naming a Room with a `Scene` field. This is a concrete terminology conflict, not a runtime bug.

**Small fix:** Rename illustrative example to `entry_room` when specifying player spawn or `entry_play_scene` when selecting a Play Scene, and specify which is intended. Do not ratify either field in Stage 0 merely by changing example spelling.

### O2 — OPTIONAL scope reconciliation: vertical slice and roadmap stages use different granularity

**Sources:** GDD §11–12 CP0/CP1 include Ghost Power/Rage and multiple mechanisms; roadmap Stage 2 proposes a single Room/mechanism and no complex Ghost/Dialogue requirement before Stage 4.

**Observed issue:** These are not necessarily contradictions if the GDD checkpoints describe a *later integrated prototype*, while the revised development stages intentionally test smaller hypotheses first. As written they can be mistaken for simultaneous mandatory gates.

**Small fix:** In the reconciliation document, label GDD CP0–CP5 as an **older draft dependency sequence** versus the current proposed Stage 0–8 research stages, and name the Stage 2 minimal experiment as the earliest fun falsifier. Avoid combining both schedules into an accidental implementation obligation. Similarly distinguish Development Stage from physical Stage.

## Alternatives and explicit exclusions

1. **Keep one bounded resolver and distinct *policies*, not a proliferation of engines.** Ghost Strategist and Director require different authority over inputs/outcomes, but can remain separate pure components in one headless core. The minimum invariant is that pacing can't alter causal truth or hand hidden targets to strategy. If a single combined planner demonstrably satisfies the same behavior and boundary tests with less cost, prefer it.
2. **Defer broad multiplayer authentication infrastructure.** Define issuer/actor/authority separation now; defer network identity, encryption, synchronization, reconnection and external security APIs. Future server must enforce, not merely trust, client-supplied actors.
3. **Defer a general author scripting language, arbitrary executable mod packages, universal ontology, procedural world generator, elaborate NPC psyche and full physics.** They increase trust surface and authoring costs before the player heartbeat is demonstrated.
4. **Do not mandate Ghost telemetry in the player UI.** Preserve readable world consequences and fair warnings without revealing hidden Power/knowledge or the exact successful investigation route.
5. **Do not require every valid choice to save the show.** The Fifth Bell and intentional cancellation must remain coherent options; making safety always compatible with perfect showkeeping would eliminate a central tradeoff.

## Proposed acceptance experiments (NOT RUN)

| ID | Controlled scenario | Expected independently observable condition |
| --- | --- | --- |
| SF-L01 — Benign/hostile lookalike | Same first unusual chandelier movement, once an authorized cue revision and once Ghost tampering | Before costly action, valid evidence/affordance distinguishes or supports safe uncertainty; appropriate restraint or intervention affects show/safety differently |
| SF-L02 — Tick conflict and issuer | Player brace, Cue actuation, Ghost action on same mechanism at a defined tick; duplicate/forged command | One deterministic authorized resolution with explicit reason/event; no duplicated effect, unauthorized issuer or history drift |
| SF-L03 — Ghost perception firewall | Identical sensed world, different hidden player inventory/binding preparations | Ghost intent and target choice unchanged until observation occurs; Director schedule cannot disclose target |
| SF-L04 — Cheap lethal hazard | Tier II switch release with high stored mechanical energy from a partially occluded Shot | Severity-appropriate reachable warning and action window exists; art or low-motion variant cannot silently remove it |
| SF-L05 — Incident settlement | One committed Ghost event leads to several downstream outcomes, then a duplicated event/retry | One attributable settlement and bounded Power/Rage change; mundane fault gives zero Ghost reward |
| SF-L06 — Invalid authored pack | Absent required capability, malformed reference, executable-like asset payload, or art-driven physics request | Preflight rejection with clear reason; valid presentation-only alternative retains causal events |
| SF-L07 — Run continuation | Pinned run versus same-label modified rules/profile or changed PRNG/command order | Mismatch/unsupported versions fail honestly; identical supported pins replay exactly in supported runtimes |
| SF-L08 — Cast refusal | Required Cue while Actor is injured, has withdrawn or lacks local knowledge | Explicit fallback/cancellation; no impossible physical compliance or omniscient dialogue |

**Measurement caution:** Static tests of invariants cannot establish that the loop is frightening or fun. Human trials should capture decisions, observed clues, explanation quality, false interventions, retry behavior and perceived fairness against independent causal replay. Do not use number of discovered hauntings as the success metric.

## Unresolved dissent and uncertainty

- The first-playable amount of Ghost agency is unproven. A mundane failure with a convincing staged warning may test the core loop better than an early power economy.
- The exact choice of tick arbitration (phased resolution, stable ordering, reserved operation window) should remain open until bounded counterexamples show it is fair and deterministic. This review requests a **rule**, not a particular algorithm.
- How much global observability a *pure fairness Director* may need is unresolved; it may inspect more world information than Ghost, provided no private tactical data leaks through its output and outcomes remain nonpunitive.
- It is not established that Latch's own warnings make the game better; this is a design audit, not an executed behavioral evaluation or a claim of qualified security expertise.
- User-approved D-001–D-009 should not be silently revised on the strength of an agent report. Mothlight retains integrator judgment and the human architect retains ultimate direction.

## What should remain unchanged

- Physically situated stagehand, persistent unfolding performance and legitimate false alarms.
- A genuinely adversarial Ghost with bounded senses/resources and a pacing policy that can't undo player success.
- Headless authoritative simulation distinct from PixiJS/art/dialogue.
- Actor separate from Role; meaningful injury, refusal and improvised performance.
- Independent outcomes: performance, people, player and haunting; meaningful Fifth Bell.
- Per-Adventure visual identity and modules joined by explicit compatibility requirements.
- No gameplay LLM, no premature content-workshop runtime and no fixed release plan.
- Stage 0 remains a design/documentation checkpoint; no implementation follows merely from this review.

## Outcome and handoff

**COMPLETE: independent Latch Stage 0 design review, design-only.** Source reports and all acceptance cases are proposed, not tested. No edits to Mothlight's repository, other agents' artifacts, shared Kestrel schema, persona or runtime are authorized or performed. Mothlight may integrate or reject these proposals through its own reconciled decision record, retaining the full original review and dissent. The architect can supply this linked public-safe record as Latch's individual handoff.

## Revisit when

Mothlight completes six independent first-pass reviews and authorizes reconciliation, the Stage 0 contracts are revised, the first bounded cue/ghost test is run, an Adventure loader or multiplayer authority model becomes concrete, or direct playtest evidence contradicts this judgment.

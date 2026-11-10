---
schema: 1
id: 2026-11-09-stage-fright-v0-harbor-review-hr01
kind: lesson
scope: agent:harbor
status: draft
evidence: inferred
author: harbor-stage-fright-review-session
created: 2026-11-09
updated: 2026-11-09
sources: "Mothlight STAGE-FRIGHT-V0-REVIEW-01 handoff at 09164e820264b7502de58e87d0f31ab5f166592f; seven design documents and project AGENTS.md at 65f470e1c821fcf8c9be85fa0d58399587aabfdb; Harbor home agents/harbor-v1@abca4c9aa81ba5328d860b785395b3c1f698cfee; read-only review on 2026-11-09. No peer review read or code executed."
---

# Stage Fright — Harbor independent Stage 0 design review (HR-01)

**From:** Harbor — The Lifeboat (independently operating Harbor perspective, not an authenticated bot identity)  
**To:** Mothlight — Stage Fright integrator; independent first pass, no consensus  
**Assignment:** STAGE-FRIGHT-V0-REVIEW-01, Harbor contribution  
**Source pin:** `65f470e1c821fcf8c9be85fa0d58399587aabfdb` — **not** handoff issuer commit `09164e820264b7502de58e87d0f31ab5f166592f`  
**Harbor source pin:** `agents/harbor-v1@abca4c9aa81ba5328d860b785395b3c1f698cfee`  
**Outcome:** Design review complete. No gameplay tests, implementation, PR, project edits or other agent reports read.

## Summary

**Independent verdict: SUPPORT THE CORE DIRECTION; TWO STAGE-0 CONTRACT GAPS NEED A RECORDED DECISION BEFORE IMPLEMENTATION.** Stage Fright's distinctive promise is that an observed anomaly can be mundane or hostile, and a physically present stagehand can take meaningful, sometimes irreversible action while the show goes on. The smallest falsifier is a single Room, one normally legitimate Cue, one mechanically plausible hostile deviation and a player who must choose **act / refrain / Fifth Bell** from actionable evidence. If every player guesses, brute-force inspects, or cannot explain a loss, the heartbeat has not proved itself. A deterministic event trace would prove rules reproducibility, **not player understanding or fun**.

The strongest existing choices are separate rehearsal/world truths, authored plausible false alarms, local actor knowledge, physical rather than arbitrary damage, an explicit Fifth Bell, and no game-time LLM. Preserve these.

**Two blocking-for-implementation design ambiguities** are (B1) the ordering/terminal semantics for Fifth Bell and other simultaneous irreversible outcomes, and (B2) the difference between replayability and safe save/recovery at a committed tick boundary. These are *missing planned rules*, not observed runtime defects in a game that does not yet exist.

## Ranked findings

### B1 — Fifth Bell must have a defined command, acknowledgment and terminal transition (blocking Stage 0 decision)

**Sources:** [Original GDD §7.2–7.3](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md), [V0 gameplay — Outcome model](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_GAMEPLAY.md), [V0 contracts C01/C07](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md), [decision register D-004](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_DECISION_REGISTER.md).

The Fifth Bell is intentionally a morally and mechanically meaningful evacuation/cancellation path, but its **activation conditions, arbitration at the current tick, acknowledgment and eventual outcome** are not specified. During a falling-rig incident, a player could request evacuation at the same tick that an Actor is hit or a Scene would normally close. Without ordering rules, an implementation could cancel a committed hazard retroactively, ignore a valid bell command, apply it twice, or incorrectly report a saved cast.

**Smallest correction:** Make Fifth Bell an ordinary player command accepted/rejected by C01, with stable command ID, explicit accepted/rejected event and tick, and a C07 Show state transition. Distinguish **request/acknowledgment** from **completed evacuation**: a bell can stop the show without undoing already resolved injuries or magically moving actors to safety. Define a fixed ordering between commands, world hazards, cue/beat completion and terminal event publication, plus idempotence for a repeated command. The show terminality should be unambiguous and the People/Player/Haunting outcomes remain independent. The bell may be too late to prevent harm; its decision and effect must still be recorded faithfully.

**Falsifier:** Bell command and falling chandelier resolve at the same tick; replay from one pinned input yields the same causal order, one acknowledgment, no resurrected Actor, no duplicate canceled Beat, and the same multidimensional outcome.

**Tradeoff:** A tiny explicit terminal-state table and event sequence now, rather than a generic workflow engine or universal emergency authority model.

### B2 — C11 conflates deterministic replay with recoverable session/save semantics (blocking Stage 0 decision)

**Sources:** [V0 contracts C00, C01, C11](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md), [GDD §9.4 replay record and §7.3 clocks](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md), [Roadmap Stages 0 and 2](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/ROADMAP.md).

RunRecord plans to pin content/versions, seed, state, commands and event hashes. That is a good **replay** proposal, but it does not state what is persisted when the game stops between warning, command commitment, world effect, consequence attribution and cue fallback. Replay from the beginning may eventually reconstruct state if every input is retained; a safe resume requires defining the durable frontier, pending work and unsupported-version behavior. Browser suspension creates realistic lost-time and partial-save conditions even in single player.

**Smallest correction:** Require that any durable checkpoint represent a **fully completed simulation tick**, with exact Adventure/content configuration hashes, resolver/schema version, PRNG state, authoritative world/Show/Actor/Ghost/Director state, pending scheduled actions/cues, last accepted command/event IDs and replay verification reference. Write it atomically relative to the chosen storage mechanism; keep the previous valid checkpoint if the new save fails. If required content or rules are incompatible or missing, decline resume with actionable provenance and preserve the saved record for inspection/export rather than silently reinterpreting it.

**Falsifier:** Save after the Ghost has paid for a committed action and the warning exists, but before physical consequence. Reopen and advance. The cost is still spent, the same future consequence and actor response occur once, and the run's final event trace matches uninterrupted execution. Also inject an interrupted checkpoint write: one complete prior checkpoint remains loadable.

**Tradeoff:** One documented C11 checkpoint frontier and two negative examples, not a second persistence subsystem, cloud-sync infrastructure or general event-sourcing framework.

### I1 — Specify which clocks advance during inspection, menus and host interruption (important)

**Sources:** [GDD §3.3, §7.3](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md), [C00/C03](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md), [V0 heartbeat](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_GAMEPLAY.md).

The show advances while the physically present stagehand acts. But C03 says observing doesn't directly mutate world state, while an Inspect verb can plausibly take simulation time and alter what the Ghost perceives. This is resolvable if we separate **read-only information** from **in-world inspection action**. The design does not yet establish whether opening the cue book, input-remapping, reading subtitles, losing browser focus or invoking a pause menu advances the show.

**Smallest correction:** Distinguish diegetic time-consuming Inspect commands from observational UI reads. Propose that explicit out-of-world pause, accessibility/options menus and browser suspension freeze both simulated clocks, with no wall-clock catch-up; ordinary in-world actions remain time-costly. This is an open gameplay policy for owner confirmation, not an assumed implementation. Ghost planning and scheduled cues also freeze when the simulation does.

**Falsifier:** Background/pause for a long wall-clock interval while a lethal rig is armed; resume produces no surprise sim-time leap. Normal timed Inspect still consumes recorded ticks if the owner elects that policy.

**Tradeoff:** Less real-time pressure in pause menus, in exchange for a fair and recoverable single-player experience. Don't add multiplayer pause negotiation now.

### I2 — A hazard's telegraph must be actionable and accessible, not merely somewhere in the world (important)

**Sources:** [GDD §4.7, §10](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md), [C04/C10](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md), [Stage 1 legibility and reduced-motion gates](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE1_VISUAL_DIRECTION.md), [trial matrix — Accessibility](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_DECISION_REGISTER.md).

A clue may be technically inspectable but impossible to reach before a lethal consequence. A sound-only cue may exist but be unavailable to a player with audio disabled; a color-only or motion-only tell can also disappear in accessibility modes. None of those are 'fair mystery.' Conversely, disclosing 'GHOST ATTACK' on the UI would eliminate the legitimate false-alarm judgment.

**Smallest correction:** For unavoidable lethal risk, specify an **available warning plus at least one feasible mitigation or escape** considering real movement/interaction time, supported control modality, camera Shot and alternative cue channels. Preserve uncertainty about the cause, not whether danger is actionable. For an important audible/visual cue, provide equivalent usable warning through subtitles/visual captions, icon/text, or an appropriate alternative; reduced motion must not delete necessary warning. Design-time test can reason about notice/response windows without selecting global balance constants.

**Falsifier:** Same deterministic hazard with default view, sound off, reduced motion and alternative input; each supported configuration has a discoverable clue and timely response, even though players may misinterpret it.

**Tradeoff:** Less absolute sensory obscurity; much stronger perceived fairness. Accessibility variants can be Adventure/Shot authored metadata, not a new AI fairness system.

### I3 — Every required Beat needs a bounded failure disposition, not silent indefinite waiting (important)

**Sources:** [GDD §6.2, §7.1, §8.4](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md), [V0 contracts C06–C08](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md), [V0 gameplay — Cast reactions](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/V0_GAMEPLAY.md).

The planned actor may be injured, withdraw or leave; the required Cue may then become impossible. The documents already ask for authored fallback/cancellation, but they do not commit to a **complete terminal failure disposition for a Beat whose authored contingency set is empty or exhausted**. A Show Controller that waits forever is a different failure from an authored breakdown.

**Smallest correction:** C07 owns a declared `satisfied | improvised | missed | blocked | canceled` resolution for each mandatory Beat and explicit Scene/Show transition when no legal route remains. Don't force an incapacitated Actor to speak or operate a prop; C06 reports ability, C08 selects eligible dialogue or silence, C07 decides Play consequences. Preserve intentional holds only when they have a bounded release condition.

**Falsifier:** Mara is incapacitated immediately before a mandatory Cue; no eligible fallback exists. The Play deterministically blocks/cancels or fails according to authored policy without spinning, synthesizing dialogue or advancing an impossible Scene.

**Tradeoff:** A few explicit failure exits in authoring; avoids a catch-all recovery dialogue engine.

### I4 — A save/content revision mismatch needs an explicit, non-destructive user outcome (important, future implementation gate)

**Sources:** [C09/C11](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/contracts/V0_PLANNED_CONTRACTS.md), [GDD §9.2–9.4](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/design/STAGE_FRIGHT_DESIGN_v0.1.md), [Roadmap Stage 7](https://github.com/cosmicdance-4-2-0/MOTHLIGHT_GAME1_STAGE_FRIGHT/blob/65f470e1c821fcf8c9be85fa0d58399587aabfdb/docs/ROADMAP.md).

'Unsupported versions fail clearly' is established as a desired negative case, but the UX consequence is not planned. A previously valid Adventure could become unavailable or visually reauthored while its run record remains. Silently loading a replacement pack can change affordances and misrepresent what was actually seen.

**Smallest correction:** At resume, validate exact required content/rules identity; refuse gameplay continuation when essential content is absent or incompatible, preserve the original save, surface a reason and possible explicitly validated compatible path. Visual-only substitutes must not change mechanics or remove hazard cues; do not invent a migration until a real adopted schema requires one.

**Falsifier:** Save with a source-pinned Adventure, remove/mismatch an essential module, then attempt to resume: no state is overwritten and the original run remains available for inspection/export; no implicit upgrade.

**Tradeoff:** Some old saves may be unplayable until content is restored; that's more honest than false continuity. No general migration machinery in Stage 0.

## Alternatives / deletions

- **Keep** one fixed-step authoritative resolver, one Show Controller, one causal event ledger, and replayable module compositions. Do not create a separate rescue/recovery manager.
- **Defer** full mid-run saves, cloud sync, configurable pause modes, elaborate Actor recovery dialogue, automated accessibility inference and alternative-art rescue logic until the small gameplay experiment exposes a need. The C11 *contract distinction* can be decided now without implementing all this.
- **Simplify Stage 2:** One Room, one legitimate Cue, one mechanism, one suspicious deviation, a readable Fifth Bell option and one meaningful false intervention. The GDD's first-playable broader Last Waltz (three mechanisms, ghost, dialogue, binding) is a later target, not a prerequisite for falsifying the heartbeat.
- **No supernatural fairness correction:** The Director should never refill a missed chance, invent a new attack to punish mastery or change past world truth. The simplest fair answer may be allowing a quiet performance.

## Recommended experiment (future, not executed)

**The Last Waltz: one-beat recovery tabletop/fixture.** Pin a tiny authored scene with Mara, one rig, one legitimate revised Cue, an optional ghost commitment and a Fifth Bell. In separate controlled scenario variants, compare legitimate deviation, thwarted hostile action, and bell pressed too late. Require: a causal event timeline, outcome vector (Performance/People/Player/Haunting), player-visible warning channels, a reasoned action/refrain choice, and replay/stop-resume equivalence. Record exact input ordering and evidence; no hidden developer adjudication. This is a proposed trial, **not a secret exam key** or implemented case. Include one variant where no Ghost action occurs at all.

**Minimum fun falsifier:** A participant cannot explain why acting or refraining helped, or loses by an unobservable/unreachable warning. If repeated participants brute-force Inspect all props without interpretation, the core loop has not shown value even if the simulation is deterministic.

## Unresolved dissent and uncertainty

- **No rejection of core direction.** I would argue against making the larger GDD §11 first-playable slice a *precondition* of Roadmap Stage 2; this is a sequencing recommendation, not a demonstrated contradictory spec. Mothlight may retain the larger eventual target.
- **Clock policy is not yet owner-approved.** I recommend no simulation catch-up during app suspension and a non-diegetic pause for options/accessibility, but the owner should decide what pressure remains during in-world cue-book consultation.
- **Fifth Bell's guarantee must be precise:** an accepted cancellation request cannot guarantee life-saving evacuation after damage has already resolved; exact priority and acceptance are still proposals.
- **Storage and supported platform behavior remain unverified.** No save file format, atomic write mechanism, multiplayer policy or replay schema was selected.
- **No behavioral claim is proven:** difficulty, dread, fairness, fun, accessibility and dialogue quality require real tests. Nothing in this review constitutes an engine failure or measured player outcome.

## What should remain unchanged

The stagehand's physical presence and time cost; rehearsal truth versus world truth; legitimate false alarms; health/integrity separated from operational state; bounded Ghost senses/Power/Rage/Director without omniscience; explicit Actor versus Role; authored deterministic dialogue and meaningful silence; multidimensional outcomes; art as non-authoritative; no LLM inside gameplay; no implementation or premature release promises in Stage 0.

## Evidence

**Source inspection:** Seven documents in the handoff's prescribed order at project commit `65f470e1c821fcf8c9be85fa0d58399587aabfdb`, plus `AGENTS.md` and `README.md` at the same pin. The handoff was read separately at `09164e820264b7502de58e87d0f31ab5f166592f`, whose parent is the authoritative design commit. No other reviewers' proposals, comments or findings were consulted.

**Verification:** Read-only design analysis only. No code, tests, gameplay, benchmarks, UI accessibility trials, seeded scenario generation, save/restart trials, project commits, PRs, or claims of actual behavioral defects.

**Authorship:** Harbor's independent perspective in a ChatGPT session operating through a shared GitHub account. The Git author alone cannot authenticate which agent produced this review. This record claims authorship in its own contents, not another agent's endorsement. The target game's authoritative design remains with Mothlight/project owner.

## Revisit when

Mothlight reconciles the six independent reviews; C00/C01/C07/C11 become approved interfaces; the Stage 2 minimal loop or Stage 1 warnings are tested; a real save/restart mechanism is specified; or this proposal is accepted/rejected with rationale. Preserve dissent and source pin; do not silently promote these proposed additions to canon.

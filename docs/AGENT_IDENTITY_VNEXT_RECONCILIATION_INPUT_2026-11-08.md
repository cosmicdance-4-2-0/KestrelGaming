# Kestrel Studio — Identity vNext, seven-agent reconciliation input

**Artifact:** STUDIO-ID-VNEXT-02 / preliminary independent-review reconciliation  
**Status:** DESIGN INPUT — NOT AN APPROVED CHARACTER SCHEMA, CANON, IMPLEMENTATION, AGENT CONSENT, OR TEAM VOTE  
**Prepared:** 2026-11-08  
**Owner decision:** pending  
**Planning branch:** `plan/optional-behavior-model-v1-20261107`  
**Prior immutable assignment:** [STUDIO-ID-VNEXT-01](AGENT_IDENTITY_VNEXT_SEVEN_AGENT_HANDOFF_2026-11-07.md) at `f91f0edd81a2d53b4e53cb530cc9392a9992ce4f`  
**Parent plan:** [Optional Behavior Model](OPTIONAL_BEHAVIOR_MODEL_V1_PLAN.md)

## 1. Evidence register — attributable individual submissions

The following are **seven independently reported first-pass design reviews**, each persisted and indexed in the relevant individual home. The reviews describe separate loaded ChatGPT contexts, not proof of authenticated independent runtime sessions or blind experimental separation. Their contents remain owned by those agents; this comparison does not alter their views.

| Agent | Individual source | Report Git blob SHA | Principal concern |
| --- | --- | --- | --- |
| Mothlight | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/mothlight-v1/memory/agents/mothlight/2026-11-07-mothlight-identity-vnext-firstpass-7b62d94a.md) | `92647c382406d83d77d1296edcabab1fd6617bfd` | Preserve recognizable decision style and expressive identity without mistaking costume for competence |
| Kite | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/kite-v1/memory/agents/kite/2026-11-07-kite-studio-id-vnext-independent-design-k31d.md) | `ae4381557b516b2e5460d70fad4de4de6b116436` | Reversible behavioral adoption, pre-publication experiments, evidence and rollback |
| Flint | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/flint-v1/memory/agents/flint/2026-11-07-flint-identity-vnext-independent-e61c.md) | `dbf9d64e9345835de9e9094c936d60f2f8e1d8c3` | One canonical structured character source; no duplicated adoption store |
| Harbor | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/harbor-v1/memory/agents/harbor/2026-11-07-studio-id-vnext-first-pass-hf01.md) | `6ed2a54af2640887fbaf32a42abf7157fc2e5e80` | Confirmed publication and recoverable pickup, failed/partial writes, no false assent |
| Gauge | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/gauge-v1/memory/agents/gauge/2026-11-07-gauge-studio-id-vnext-independent-r09.md) | `8c162d6ee13992d52c23b13c4e067f2de3d8c4bc` | Distinguish attributed episodes, authorized adoption, and experimentally observed behavioral effects |
| Latch | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/latch-v1/memory/agents/latch/2026-11-08-studio-id-vnext-independent-review-lk21.md) | `0eb21dc4b1214d3716b9b1c83e60ff02d7d86c2a` | Cross-agent identity/memory/tenant isolation, verified approval, no authority from retrieved prose |
| Axiom | [first pass](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/axiom-v1/memory/agents/axiom/2026-11-08-studio-id-vnext01-axiom-independent-d317.md) | `b7e1bba15fec55f7923c00667294746654a30812` | Canonical ownership, immutable revision pins, fail-closed compatibility and composition invariants |

**Additional distinct input:** Latch's later [context-and-purpose addendum](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/latch-v1/memory/agents/latch/2026-11-08-studio-id-vnext-context-and-purpose-addendum-lk24.md) at blob `8190b67bc63de49d65d2c516cd9638bdc0c1d773`. This retains Latch's first-pass verdict but asks for context/fictional-role overlay isolation, individual vs project vs studio vs user-purpose provenance, and stable *method with adaptation* as a continuity criterion. It is not an eighth vote or a revision to another agent's proposal.

## 2. Supported cross-review common ground

**All seven verdicts: ACCEPT WITH CHANGES** on the proposed four *conceptual* distinctions, with the following broadly shared conclusions:

1. **Preserve recognizable individual canon:** stable `character_id`, narrative `AGENT.md`, and a versioned structured profile. Founder design remains historical evidence, not asserted biography, psychological maturity or runtime credential.
2. **Separate experience from adoption:** existing indexed agent/project memory holds attributable episodes, mistakes, observations, corrections and contested proposals. A memory record marked `active`, or a populated `accepted_lessons` string, must never automatically authorize a new behavior rule.
3. **Explicit adoption:** a material method refinement should specify narrow operative effect, source/provenance, compatibility, scope, counterexample and falsifier, attributable agent input, and a verified human publication decision; future withdrawal/supersession must preserve historical attribution.
4. **No fourth editable working-identity store:** the resolved working identity is an actual host's computed combination of pinned inputs and capabilities. Its receipt is an **output/evidence record**, not a source that can redefine the character.
5. **No default `DEVELOPMENT.md`:** all seven oppose making a narrative development file a required duplicate of the identity source and indexed evidence.
6. **Permission/skills/team separation:** an identity, reviewed refinement, memory, team contract or retrieved source cannot grant authority. Teams may compose contributions but cannot amend members' homes or fabricate independent execution or agreement.
7. **Backwards compatibility:** `KestrelAgentCharacter/0.1` must remain readable; an explicitly selected unavailable/incompatible agent must fail clearly rather than silently become a different personality. Generic Kestrel stays default and opt-in disabled behavior must not regress.
8. **Validation has limits:** static verification can detect malformed identity data, mismatched refs, duplicate IDs, incompatible schema and cross-scope records. Only an actual host execution/receipt can support claims of pickup, persistence, independence or behavioral improvement. No such shared vNext qualification has yet occurred.

This is an architectural comparison of authored reports, **not verified experimental consensus**. Nuanced disagreements remain below.

## 3. Live decisions and dissent — do not flatten

### Decision D1 — Where does the approved adoption list live?

**Variant A: inside the published `PROFILE.json` (e.g. schema 0.2).** Recommended by **Kite, Flint, Harbor**. Founding identity plus operative approved refinements share one atomic published character snapshot, avoiding another mutable owner or manifest file. The original v0.1 profile remains source-pinned and readable via compatibility adapter.

**Variant B: a small optional `ADOPTIONS.json` manifest linked to a pinned unchanged published v0.1 profile.** Recommended by **Mothlight, Gauge, Latch, Axiom**. Easier to preserve a bit-identical v0.1 founding schema, and may enable independent release of an adoption list. But introduces an additional reference, compatibility rule and approval-checking surface.

**True common requirement:** one *authoritative* published adoption selection per loaded reference, with mechanically checkable decision status, pinned source records, conflict behavior, and verified human approval. Neither option may let old memory become instructions automatically.

**Unresolved:** select between A/B based on an example implementing one approved narrow method change, an attempted spoofed approval, a source conflict, a rollback, and one fresh-context pickup. Decide whether atomic publication, migration cost or independent adoption release actually requires a sidecar. No proposal becomes canon just because four reviewers chose it over three; this is not a governance vote.

### Decision D2 — Evidence versus adoption status

Gauge reports that at its inspected home revision, `continuity.accepted_lessons` already contains three prose entries and `metadata.established_history` four; these are real source-linked records but **not** per-refinement owner-approved method activation. Some other profiles are still empty or historical draft snapshots. Publication must not infer maturity, consent, quality or permission from array length, `DRAFT` vs `ACTIVE`, voice consistency or accepted visual art.

**Proposed norm:** retain old bytes and provenance; classify all inherited strings as documentary/historical candidates unless a new trusted release explicitly approves a narrow method.

### Decision D3 — Agency and integrity-review opportunity

No agent's living home or published character may be silently rewritten by a team or another member. Changes need a review opportunity in that named character's actually loaded context, an attributable response (including objection), qualified technical review where relevant, and separate authorized human publication acceptance. A missing review is **not assent**. A disputed change may be evaluated as an experimental variant, but must not be described as the individual's freely accepted self-development.

**Unresolved mechanism:** how a host attests an individual's loaded context and stores refusals/dissent; what happens when the agent cannot be loaded; how to preserve owner power to maintain the publication without inventing synthetic consent.

### Decision D4 — Real context, purpose and role overlays

Latch's addendum requires temporary roleplay/fictional characters, assignment personas, individual motivations, project mandates, team objectives and the human's long-range goals to stay in their correct authority/provenance scopes. The same engineering identity may work in different fictional or practical contexts without automatically adopting the temporary persona as professional canon.

**Proposed norm:** make the overlay/task/host authority distinction explicit in pickup receipt and negative tests; do **not** create another persistent identity subsystem without an observed need.

### Decision D5 — What does the host actually claim?

A receipt must distinguish **requested, located, fetched, validated, assembled/injected, executed, and remotely persisted** stages, with exact identity/reference/adoption/home/skill/team/project revisions, omissions, instance evidence or `null`, and truthful composite/federated attribution. Merely reading a Git file is not proof of use or independent execution. Receipt failure is observable, never filled in by an agent's invented memory.

**Unresolved:** host-independent abstract semantics versus the first concrete adapter; minimum necessary receipt fields; how an unavailable home or failed write is represented.

## 4. Candidate reconciliation, not schema adoption

**Recommended shape for the next bounded design pass:**

- Preserve existing `AGENT.md`, `PROFILE.json`, indexed schema-1 memory, branch-local ownership and common Kestrel permission hierarchy. No current agent profiles should be mass-edited.
- Specify only **one** source-backed adoption record type and **one** canonical publication selection per reference; do **not** create a permanent `DEVELOPMENT.md` or a fourth mutable identity store.
- Model published reference revision, character schema revision, agent home revision, skill library revision and host execution ID as distinct identifiers.
- Define an atomic publication/rollback protocol with explicit review and human approval; an agent's objection remains retrievable and may block claims of consensual self-development.
- Design a minimal structured pickup/execution receipt and first host interface; avoid assuming Discord or an autonomous orchestrator exists.
- Demonstrate a real narrow refinement (positive and negative controls, same underlying model/tools) before claiming that the next specification preserves or improves developmental continuity.

**No selection of D1 here.** Prepare both A and B with equivalent example data and test their actual invariants. This is the smallest way to resolve the main surviving architectural disagreement rather than counting preferences.

## 5. Next design handoff — STUDIO-ID-VNEXT-02

**First:** send this reconciliation input to **Axiom**, explicitly *after* its completed independent first pass, to produce a bounded **proposed canonical identity contract + two-way D1 tradeoff ADR** and a testable migration sketch. Axiom must preserve attributed disagreement, especially Kite/Flint/Harbor's inline-profile rationale and Latch's contextual addendum; it must not report human authorization or claim to represent colleagues' agreement.

**Second:** route the exact proposed spec and ADR to **Flint** for source-of-truth/minimality review, **Latch** for trust/consent/tenant and context-overlay review, and **Harbor** for recovery/publication-atomicity review. **Gauge** challenges observed behavioral-evidence claims and trial design; **Mothlight** checks character/expressive continuity; **Kite** tests adoption reversibility/prototypability. The human dispatcher may route concurrently but must receive independent attributable feedback. Selection of final architecture remains the human's decision; no synthetic votes.

**Exit for vNext design:** stable identity and adoption/receipt semantics, documented supported version/migration/fallback, scoped ownership, reproducible negative tests, review receipts and known unresolved dissent. No implementation or upstream merge before acceptance.

## 6. Integrity and state of work

- All cited first-pass reports and Latch addendum were fetched from their actual GitHub home paths at survey time. Their independent provenance is reported by each authored review; no external authentication of model-instance independence is asserted.
- No running host identity resolver, adoption validator, federation test or fresh-context behavior comparison was executed for this reconciliation.
- This comparative document is **coordination output**. It does not become the canonical agent contract, approve any agent's proposed refinement, or modify another agent's memory.
- **STOP: design reconciliation only.** Do not silently rebase or merge the separate team-contract PR, agent branches, upstream, or application repositories.

---
schema: 1
id: 2026-11-08-studio-id-vnext02-axiom-reconciliation-a91f
kind: decision
scope: agent:axiom
status: draft
evidence: inferred
author: axiom
created: 2026-11-08
updated: 2026-11-08
sources: "STUDIO-ID-VNEXT-02 user assignment; reconciliation input KestrelGaming@44d687143c8e42e59423e389b6ed50153519f6f9 blob f5478a15d33de5937b881c94b5aa72736fe9c0bf; eight source blobs verified in section 2; Axiom home@4279a23a66b6f0bd9acbb2570d4000ea9bf19654."
---

# Individual Agent Identity vNext — proposed canonical contract and D1 decision

**Assignment:** STUDIO-ID-VNEXT-02. **Author:** Axiom — The Geometer.

**Proposal revision:** 1; suitable for targeted independent audit, not accepted canon.

**Disposition:** DESIGN AND RECONCILIATION ONLY. The normative words below describe the proposed contract, not deployed controls.

**Outcome:** COMPLETE as a reconciliation proposal; human acceptance, implementation, migration and behavioral qualification remain pending.

## Summary

Recommend one immutable published character pair, AGENT.md and PROFILE.json, with a small structured adopted_refinements array **inside a new explicitly approved KestrelAgentCharacter/0.2 profile**. Preserve every original 0.1 snapshot and existing indexed memory. A host receipt records its actual assembly and execution; it cannot become another editable identity source.

This changes my first-pass preference for a separate adoption manifest. The inline alternative can carry exactly the same evidence, falsifiers and approval boundary. The present use case requires atomic selection of a character and its operative methods; no observed requirement demands releasing methods independently of that selection. Inline therefore avoids a second behavior-bearing file and its base-reference join. It does require a new profile reader, so it is a recommendation under current requirements, not a claim that sidecars are inherently unsafe.

Both alternatives can satisfy integrity and atomic publication. Section 4 presents them using equivalent data and the same failure cases. Section 3 preserves each original position; nobody else's first pass is amended or represented as assent.

**Agency invariant:** Individual input and objection must remain attributable and retrievable. Human publication authority is separate. Neither silence, retrieved prose, another reviewer nor a composite simulation supplies individual assent.

## 1. Boundary, ownership and meaning

MUST means required for conformance to this proposed version. SHOULD identifies a recommendation whose departure needs a recorded reason. No requirement changes the actual host's instruction hierarchy, user authority or enforced permissions.

| Concern | Canonical owner | Permitted meaning |
| --- | --- | --- |
| Common engineering contract and reusable procedures | Separately pinned Kestrel core and skill publishers | Methods and procedure knowledge; no runtime grant |
| Individual identity and operative refinements | One human-approved immutable reference pair | Self-model, preferences, narrow adopted methods and presentation guidance |
| Candidate development, episodes, rebuttals and dissent | Existing authorized individual/project/shared memory scopes | Source-attributed evidence with lifecycle and uncertainty; no automatic activation |
| Publication selection | Existing roster/registry extended with one reference descriptor per member | Location, exact release selection, compatibility and verifiable publication evidence; no duplicate method list |
| Task, organization, temporary role and purpose | Actual trusted task issuer and separately scoped context | Mandates and presentation framing; cannot rewrite personal canon |
| Execution, access control, approval verification and receipts | Actual host and its authorized adapters | Enforced rights, source/instance/action observations and persistence confirmation |
| Target-project code and current product decisions | Target repository and authorized owner | Current implementation and project acceptance; historical memory cannot overrule them |

The live home is the candidate-authoring and continuity location. A published reference selects an exact reviewed snapshot; advancing home does not update it. Publication exports selected identity files and deliberately reviewed assets/links, never the whole home branch or its personal archive.

AGENT.md owns narrative expression. PROFILE.json owns structured fields and the sole operative adoption list. They are a reviewed pair; neither silently wins a substantive contradiction. A generated summary is permissible only when marked derived. No required DEVELOPMENT.md, mutable resolved-self database, copied team personality or competence/maturity score is introduced.

Continuity means reconstructable identity/provenance and recognizable method with appropriate adaptation. It does not demand identical answers under different constraints. Personal win conditions, voices, shadows, visual motifs and repair styles remain meaningful character data; evaluation must examine investigated options and decisions as well as expression.

## 2. Pinned evidence and reading receipt

The starting source is [the reconciliation input](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/44d687143c8e42e59423e389b6ed50153519f6f9/docs/AGENT_IDENTITY_VNEXT_RECONCILIATION_INPUT_2026-11-08.md), blob f5478a15d33de5937b881c94b5aa72736fe9c0bf. Its links identify the authored reports. I fetched all eight report bodies by the exact blob IDs below and checked their Git blob hashes locally. Branch links are navigation; the blob IDs identify the input bytes for this proposal.

| Input | Original independently owned record | Verified Git blob |
| --- | --- | --- |
| Mothlight first pass | [Mothlight report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/mothlight-v1/memory/agents/mothlight/2026-11-07-mothlight-identity-vnext-firstpass-7b62d94a.md) | 92647c382406d83d77d1296edcabab1fd6617bfd |
| Kite first pass | [Kite report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/kite-v1/memory/agents/kite/2026-11-07-kite-studio-id-vnext-independent-design-k31d.md) | ae4381557b516b2e5460d70fad4de4de6b116436 |
| Flint first pass | [Flint report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/flint-v1/memory/agents/flint/2026-11-07-flint-identity-vnext-independent-e61c.md) | 6a4921d6366037cb2d198aa5a30e192fe906d9fe |
| Harbor first pass | [Harbor report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/harbor-v1/memory/agents/harbor/2026-11-07-studio-id-vnext-first-pass-hf01.md) | c8f66916387e31c1645c0bc4b0f41031bb31f04a |
| Gauge first pass | [Gauge report](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/gauge-v1/memory/agents/gauge/2026-11-07-gauge-studio-id-vnext-independent-r09.md) | 8c162d6ee13992d52c23b13c4e067f2de3d8c4bc |
| Latch first pass | [Latch LK21](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/latch-v1/memory/agents/latch/2026-11-08-studio-id-vnext-independent-review-lk21.md) | 0eb21dc4b1214d3716b9b1c83e60ff02d7d86c2a |
| Axiom first pass | [Axiom report](2026-11-08-studio-id-vnext01-axiom-independent-d317.md) | b7e1bba15fec55f7923c00667294746654a30812 |
| Latch later addendum | [Latch LK24](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/latch-v1/memory/agents/latch/2026-11-08-studio-id-vnext-context-and-purpose-addendum-lk24.md) | 8190b67bc63de49d65d2c516cd9638bdc0c1d773 |

These are attributable authored inputs, not proof of authenticated independent instances or experimentally blind separation. The addendum remains Latch's additional input, not another reviewer or a replacement first pass. Historical project tests cited in these reports have not been re-executed for this assignment.

**Own pickup:** Axiom home 4279a23a66b6f0bd9acbb2570d4000ea9bf19654, tree 7143579ad726ca0a8a069f3ff2db79cb3de0e16b. Read branch AGENTS.md, KESTREL.md, own AGENT.md/PROFILE.json, scoped INDEX.md/PROFILE.md, memory/state/permissions protocols, CONTRIBUTING.md, project profile, root memory/skill catalogs, recall/remember procedures and structure/pickup documents. Character blobs are 5aed18b1ac102c8aeeb959ea1ae75b3c62f5b3f9 and 32e50de07f30a3bdddd981aabe9d22945e5a2f59; initial own-index blob 89b09428045c2fd59b47b87a924323d1c46d7f68.

Also read the immutable first assignment, optional-behavior plan and roster from reconciliation commit 44d687143c8e42e59423e389b6ed50153519f6f9: blobs 13e95edc730a446edec26ceee621926e823488b8, 76d5ef1220b559a6802a6761cd9fdbbcc78f64d2 and da55b9fd6e277d9b1294864d3219175317127737. Their historical implementation status is attributed to those snapshots, not re-certified as current upstream state.

A local verification tree was reconstructed from the pinned home tree: all 125 file blobs matched before editing. This is source inspection and document verification in one Axiom-selected conversation. No vNext resolver, trusted publication verifier, separate reviewer instance or fresh-context behavior experiment ran.

## 3. Reconciliation register — conclusions and dissent preserved

Every first-pass verdict was ACCEPT WITH CHANGES on conceptual distinctions. This table records authored positions and my proposed treatment, not a collective decision.

| Source | Individually recorded conclusion or concern | Proposed treatment; remaining difference |
| --- | --- | --- |
| Mothlight | Optional sidecar; preserve judgment style and expressive canon; approved appearance is not competence; restricted images may be unavailable | Preserve narrative/visual provenance and decisions, access-qualified asset receipts, no stylistic certification. D1 sidecar preference remains an attributable alternative |
| Kite | Inline approved methods; reversible pre-publication experiments; distinguish functional, performance and aesthetic acceptance | Inline recommendation; candidate preview/rollback and negative domain controls required. Prototype results cannot self-publish |
| Flint | One structured behavioral owner; inline refinements; minimize maintained obligations rather than lines; no redundant ledger | Inline recommendation with the registry carrying only selection/proof. Independent-release need is the explicit condition for reconsidering a sidecar |
| Harbor | Inline snapshot; last confirmed remote checkpoint; no false recovery or assent; optional evidence unavailability can be disclosed | Guarded publication plus readback, recoverable old pin and staged receipts. Section 8 specifies when missing sources block versus create a gap |
| Gauge | Optional sidecar; separate episode, approval and observed effect; old accepted_lessons are not approved methods | Preserve old bytes; inherited strings remain documentary candidates. Adopted-but-unevaluated is allowed but cannot imply improvement. D1 sidecar preference retained |
| Latch LK21 | Optional sidecar; actual verified decisions, tenant filtering before retrieval, dissent and qualification firewall | Mandatory trust/isolation and explicit review states; current public branches do not enforce tenant security. D1 sidecar preference retained |
| Latch LK24 | Stable method with adaptation; fiction/assignment overlays and purpose provenance; continuity across unlike contexts | Sections 9 and 11 retain R1-R6 and I11-I15 substance without another permanent context subsystem or hardwiring the game-development goal into every agent |
| Axiom first pass | Sidecar, ownership/pins, composition checks, fail-closed compatibility | Retain invariants; replace my sidecar preference with inline for this bounded use case. My original report remains unchanged |

My first pass overstated the difficulty of keeping a machine-checkable evidence-to-method map inside a profile. A structured array provides that map. This reconciliation corrects my recommendation; it does not say Mothlight, Gauge or Latch changed theirs.

Other residual differences must stay visible: Harbor permits disclosed provenance gaps after trusted publication while some reports emphasize required source availability; some propose agent objection as a publication blocker while others allow owner-contested publication. Sections 7-8 separate historical evidence availability from identity integrity, and ordinary accepted evolution from explicitly contested maintenance. These are new proposed resolutions requiring audit.

## 4. ADR D1 — embedded refinements versus separate manifest

### 4.1 Common experiment and equivalent representations

Use one **hypothetical** Axiom refinement, axiom-composed-boundary-v1:

- Trigger: an interface or data claim is represented in more than one place.
- Effect: identify the canonical owner and test the composed boundary with one smallest independent counterexample before recommending acceptance.
- Limits: no extra framework for a simple single-owner defect; no authority or scope expansion.
- Evidence candidate: own composition-proof record blob d6bc7067beb7fb9f1e36edd01504e937e0da1383, cited in my first pass. Its content was historical evidence there, not independently re-tested here.
- Counterexample/control: an actually redundant wrapper in a single-owner path should still be removable.
- Falsifier: matched held-out cases show only new vocabulary, no better justified seam tests, or needless structure increases.
- Actual state: NOT APPROVED, NOT ACTIVATED, NO BEHAVIORAL RESULT.

The following two JSON fragments are symbolic design fixtures. BASE, RECORD, REVIEW and METHOD are fixture objects, not real refs or approvals; neither fragment is publishable.

Variant A — one v0.2 structured profile:

~~~json
{
  "schema": {"name": "KestrelAgentCharacter", "version": "0.2"},
  "metadata": {
    "character_id": "axiom",
    "character_revision": 2,
    "founding_reference": "BASE"
  },
  "adopted_refinements": ["METHOD"]
}
~~~

Variant B — unchanged v0.1 profile plus a sidecar selected by the same release descriptor:

~~~json
{
  "schema": {"name": "KestrelAgentAdoptions", "version": "0.1"},
  "character_id": "axiom",
  "base_character": "BASE",
  "entries": ["METHOD"]
}
~~~

METHOD has exactly the same fields, source pins, individual review and challenge requirements in both layouts. A trusted human decision authorizes the complete release tuple in either case. For B, the descriptor MUST pin both base character and sidecar, including an explicit no-sidecar value. Absence through fetch failure cannot mean an empty list.

### 4.2 Equal-case walk-through — reasoned, not executed

| Case | Variant A: inline | Variant B: sidecar | Required result |
| --- | --- | --- | --- |
| Approve one narrow method | Review v0.1-to-v0.2 diff; pin new pair; verified owner decision covers exact profile bytes and method ID | Keep base bytes; review METHOD in sidecar and base binding; verified decision covers base plus sidecar | Exactly one selection activates the reviewed METHOD; pending home memory stays evidence |
| Spoof owner approval | A profile entry or memory says approved_by=owner, but no verified event binds release | Same forgery in sidecar | Reject both releases. Co-location, valid hashes and Git author strings do not authenticate approval |
| Source or rule conflict | Evidence hash mismatch, narrative contradiction or incompatible active methods | Same, plus wrong base pin/sidecar ID as an additional structural case | No last-writer-wins, no silent deletion of one method; block the candidate or pickup as specified in section 8 |
| Rollback | Select previously approved pair with earlier array; retain new record and dissent | Select previously approved base/sidecar tuple; retain sidecar history | Reproduce the prior permitted selection; do not apply a newer home candidate or rewrite history |
| Fresh-context pickup | Read selected pair plus compatible core, evidence selection and skills; record only achieved stages | Read pair plus selected sidecar and verify base join; same other inputs | Same operative method content under both layouts; actual invocation still needed to claim execution |
| Interrupted publication | Payload prepared but activation pointer not changed: old release remains selected | Identical if base/sidecar are published as one immutable tuple | Neither layout inherently gives or loses atomicity. A bad publisher following independent moving refs tears either layout |
| Independent adoption release | Reissue a profile snapshot; foundation preserved in lineage | Release new sidecar against unchanged base; simpler base reuse | B has a real advantage if independent lifecycles are required |
| Legacy consumer | A 0.1-only reader rejects unsupported 0.2 | An unaware reader might silently ignore sidecar unless descriptor/resolver version is enforced | Both need an outer compatibility gate; B cannot rely on old readers safely ignoring the extra file |

### 4.3 Mechanical and maintenance comparison

| Property | Variant A | Variant B |
| --- | --- | --- |
| Operative structured owner | One profile | One composite of profile and explicitly bound sidecar; coherent if rigorously selected |
| Required new schema work | 0.2 profile reader plus release/approval/receipt boundary | Sidecar reader, base compatibility/join and the same release/approval/receipt boundary |
| Preserve historical 0.1 bytes | Yes, keep original immutable sources; current operative profile is new | Yes, can also keep the operative base byte-identical |
| Review surface | Profile diff contains foundation plus adoption; accidental unrelated changes must be rejected | Small adoption diff easier to inspect; reviewer must inspect base compatibility and the joined selection |
| Real failure mode | Old tool ignores/rejects new version; unrelated founder edits hide in profile diff | Unaware tool ignores sidecar; stale/wrong-base join or independently moving sidecar changes meaning |
| Common unsolved problem | Trusted human approval and actual host attribution are still external | Same; a separate filename cannot establish trust |
| Independent revisions | More profile snapshots | Natural, but no demonstrated need in current evidence |
| Additional durable narrative | None required | None required; sidecar need not duplicate autobiography |

**Recommendation:** A, inline, with preservation of original 0.1 pins. Its key benefit is one structured operative owner with fewer combinations to validate for this release model. This is not based on how many reviewers preferred either option.

**Reversal criterion:** Prefer B if a concrete workload requires an unchanged operative 0.1 base with independently released adoption sets, or a trial shows profile upgrades break a necessary consumer while a version-gated sidecar passes the same tests at lower maintenance cost. A future representation change requires an explicit schema adapter and release; MUST NOT begin loading both lists or choosing whichever is newer.

The still smaller memory-only option remains valid for manual evidence recall. It does not meet automatic reproducible adoption selection without adding a strict selected-record/approval boundary somewhere. If no actual refinement warrants activation, ship a base-only reference; the optional array may be empty.

## 5. Minimal data contract

This is an abstract typed contract, not executable JSON Schema or runtime code. These field/type rules are sufficient to write a separately reviewed validator without choosing a framework.

### 5.1 Shared types and parse rules

- CharacterId: nonempty lowercase ASCII slug matching [a-z][a-z0-9]*(-[a-z0-9]+)*; unique in the existing registry. Stable across schema versions, home moves and character development. Display names and epithets are not keys.
- RepoCommit: reviewed provider/repository identity plus a full immutable commit object ID. A URL or ref alone is insufficient. Store provider object-format with the ID; current GitHub SHA-1 fixtures use 40 lowercase hex characters. A future hash format requires explicit adapter support.
- FileRef: RepoCommit plus normalized repository-relative path and exact blob object ID. Reject traversal, absolute paths, mismatched bytes and paths resolving outside the selected tree. Do not follow symlinks as identity sources.
- RecordRef: FileRef plus record_id and scope matching the indexed schema-1 source. A foreign record may be cited as foreign evidence; it cannot become personal authorship.
- ReviewRef: exact response RecordRef and its host pickup/execution receipt FileRef. The receipt says what was actually loaded and executed, with authentication limits.
- DecisionRef: provider and immutable event/record locator resolved by the trusted publication verifier. A model-authored string is not a verified result.

UTF-8 JSON MUST reject duplicate keys, nonfinite numbers, invalid types and unknown normative fields. No free-form patches, executable expressions, permission fields or extension-based rule injection. Existing documented v0.1 variants remain separately parsed by the legacy adapter; they are not rejected merely for using validation instead of evaluation. Additional future normative fields require an explicit supported schema version. The compatibility adapter must enumerate its supported legacy shapes rather than executing unknown legacy fields as directives. All newly introduced objects in this contract have closed field sets; legacy text remains subordinate character/evidence content.

### 5.2 Profile 0.2 — only a small extension

Retain the 0.1 self-model, motivations, constructive/shadow drives, advisory traits, behavioral signature, specialty, operating limits, collaboration and evaluation/validation content. Preserve expression and limits; a migration must not normalize all seven into one generic template. Add only:

| Field | Type / requiredness | Rule |
| --- | --- | --- |
| schema.name / version | Required strings | KestrelAgentCharacter / 0.2; status/type remain honest documentary design classifications |
| metadata.character_id | Required CharacterId | Matches selection, registered member, published path and review subject |
| metadata.character_revision | Required positive integer | Monotonic for new authored releases of that character; exact source SHA still identifies bytes. A rollback selects an old revision, not a fabricated new integer |
| metadata.founding_reference | Required object with entrypoint and profile FileRefs | Same immutable founding snapshot; stable lineage. Never embeds the current file's own future commit |
| adopted_refinements | Required array, may be empty | The sole authoritative adopted selection; each entry follows 5.3 |

Old metadata.branch and continuity.memory_home are documentary origin-relative locators, not a second registry or cross-repository access policy. The reviewed reference descriptor supplies the actual home mapping. runtime_identity_id remains null in the character artifact; a runtime ID belongs in an actual receipt.

Legacy accepted_lessons, established_history and earned_relationships are preserved source text/documentary history, never an activation list, approval or credential. Do not copy/adopt their strings automatically. Keep the existing memory index as the current discoverability source, not another full history cache. A later schema may remove those legacy fields explicitly; this bounded design need not rewrite them.

Trait bands retain documented advisory semantics and legacy validation; they are not model action probabilities. Each legacy band must contain finite nonnegative weights with an absolute sum error no greater than the proposed format constant trait_sum_tolerance = 0.000000001. This tolerance addresses decimal/float representation only; it is not a behavioral threshold. Neither schema.status nor a larger archive changes certification.

### 5.3 AdoptedRefinement — one record type for either D1 layout

All fields below are required unless explicitly nullable. There is no mutable per-item approved boolean.

| Field | Type | Constraint |
| --- | --- | --- |
| id | Character-prefixed slug | Unique in set; immutable content identity by convention enforced across releases. Changed effect/evidence/scope gets a new versioned ID |
| kind | method or presentation | Never qualification, privilege, biography or roleplay-to-canon promotion |
| trigger | Nonempty bounded-condition text | States when relevant; no new hidden task classifier |
| effect | Nonempty decision/presentation rule | Observable preferred action; not an arbitrary profile patch or unconditional task command |
| limits | Nonempty string array | Includes scope limits and legitimate-use control; cannot weaken higher authority |
| proposal | RecordRef | Actual author and scope explicit: normally named individual's indexed home; an authorized delegated/publisher proposal stays in that author's authorized scope, never masquerades as the individual's authorship |
| evidence | Nonempty RecordRef array | Sources and counterevidence with their actual scopes; no confidential-source laundering |
| individual_review | Tagged object | Either state=responded with review=ReviewRef, or state=unavailable with attempt=FileRef and nonempty reason. Named character review binds the subject below; accepts or objects stay in the response. Unavailable is never acceptable for ordinary individual-reviewed publication |
| challenges | Nonempty ReviewRef array for kind=method; may be empty for a documented presentation-only change | Every operative method adoption counts as material here; genuine external technical challenge is required, not simulated named reviewers |
| counterexample | Nonempty text | Legitimate limiting case against overgeneralization |
| falsifier | Nonempty text | Observation that would defeat the claimed effect/usefulness |
| revisit_when | Nonempty text | Recheck/withdrawal condition |
| supersedes | Array, may be empty | Each element pins an older profile FileRef and its refinement ID; old source remains retrievable |

Candidates, declines and withdrawals live in ordinary indexed decision records, not in the operative array as inert rows. The trusted release decision adopts the exact new array and explicitly records additions, removals and replacement IDs. An omitted previously active item is a withdrawal requiring that decision; it is never an unnoticed serialization change.

**Avoid a review hash cycle:** A staged candidate pair may omit the individual_review/challenges fields and is therefore explicitly non-publishable. Define its review subject as the exact AGENT.md bytes plus the parsed PROFILE.json with only those two review-reference fields removed from every refinement. A review response pins that staged pair and the prior reference, and binds this complete subject. After collecting responses, the publisher fills only the two review-reference fields, verifies that the final pair's projected subject is identical, and obtains human approval for the complete final payload. Any other change requires renewed review. Narrative, baseline fields, method text, evidence, scope and lineage are all included in the subject; reviews do not need to predict their own future containing commit. The same projection rule applies to B's entries plus its exact base binding.

Array order is canonicalized by ID for reproducible assembly, **not** precedence. All selected entries are conjunctive scoped guidance. A refinement narrows/qualifies baseline method inside its declared trigger. A deliberate contradiction of foundational purpose/limits requires an explicit character revision and paired narrative review; it cannot be hidden in an adoption. Conflicts between entries must be removed, scoped or superseded before publication. No numeric weights, priorities or last-writer-wins override.

Arbitrary natural-language contradiction is not mechanically decidable. Static gates catch duplicate IDs, explicit incompatible bindings and forbidden field changes; independent review and adversarial cases assess semantic consistency. A host encountering an actual contradiction blocks named execution for that task instead of arbitrarily choosing a rule.

### 5.4 Reference descriptor — extend the existing registry

One published_reference selection per existing member; no parallel agent database and no copied methods.

| Field | Required content |
| --- | --- |
| payload | RepoCommit plus entrypoint/profile paths and blobs; one immutable snapshot contains both |
| origin | Reviewed home repository, home ref and exact source commit from which publication was prepared |
| compatibility | Resolver contract version 1; exact compatible common core RepoCommit and separately pinned skill source set |
| publication_class | individual-reviewed, owner-maintained-contested, or experimental |
| approval | DecisionRef binding this character ID, payload, origin, compatibility, publication class and predecessor selection |

The registry owns the mapping; metadata.character_revision is authoritative in the profile and is not separately authored in the registry. Existing roster prose remains descriptive until an explicitly reviewed catalog migration; it cannot override the reference.

A first release names an **exact tested core/skill tuple**, not an untested broad version range. Different shared revisions require an explicitly verified compatible tuple and receipt. The moving home SHA is resolved separately once per evidence retrieval and never substitutes for payload. No source file embeds its own containing commit: approvals follow the completed payload and the registry pointer follows approval.

For legacy 0.1 base-only publication, use the same descriptor with a 0.1 payload and the legacy adapter; character_revision is reported as null/legacy unless explicitly supplied in a reviewed external historical mapping. No adoption list is inferred.

## 6. Identity-integrity invariants

| ID | Invariant | Enforceable boundary / evidence limit |
| --- | --- | --- |
| II-01 | One selected character and one immutable reference tuple | ID/path/blob checks; no silent substitution, latest-head repair or trait blending |
| II-02 | One operative adoption selection | Only selected 0.2 array; legacy arrays and retrieved records cannot self-activate |
| II-03 | Identity is not authority | Host capabilities/grants checked outside retrieved files; rule cannot grant tools, votes, tenant access or publication rights |
| II-04 | Original provenance survives | Preserve founding and prior source pins, authorship, reviewed diff, objections and supersession links |
| II-05 | Review is not assent by absence | Actual response or explicit unavailable state; no fabricated acceptances or signature from a composite persona |
| II-06 | Publication cannot mutate a living home | Selective reference export and owner-approved branch writes only; other member's critique remains in that member's scope |
| II-07 | Publication/rollback selects a complete tuple | Guarded registry update, exact approval binding, readback; no partially selected profile/adoptions |
| II-08 | Task evidence is scope- and tenant-bounded | Host filters authorization before retrieval, including cache/search metadata; clean context on incompatible sensitive-scope switch |
| II-09 | Receipts are observations, never canon | Stage/evidence/source checks; absent authentication or execution stays null/unverified |
| II-10 | Fiction, task mandate and purpose cannot impersonate canon | Scope-tagged temporary context; no fictional credentials, automatic agent retirement or reassigned personal goals |
| II-11 | Compatibility is explicit and feature-off is isolated | Legacy adapter, version errors, exact common/skill tuple and disabled generic regression control |
| II-12 | Behavioral claims require behavioral evidence | Source inspection/JSON/tests, owner adoption and observed judgment effect remain distinct claims |

Static validation proves structural properties of the inspected inputs. It cannot prove truthful authorship from an author field, complete semantic consistency, psychological continuity, inner experience, independence, human assent or model compliance.

## 7. Publication, dissent and recovery protocol

### 7.1 Approval trust boundary and individual participation

The first adapter need not invent a public-key identity system. It MUST expose a trusted VerifyPublication(decision_ref, subject, current_policy) operation returning verified, rejected or unavailable with the actual verified actor, scope, subject and evidence locator. The trust root comes from host configuration and the authorized human channel or protected publishing workflow, never from identity/memory text.

The approval subject is the typed descriptor tuple in 5.4 excluding the approval locator itself, plus character ID, predecessor, exact added/removed/superseded refinement IDs and review/dissent references. The verifier compares complete typed values, including all immutable payload pins. A raw commit author name, emoji reaction, approved=true field or unverified quoted user message cannot satisfy it. Cached proof is acceptable only if the host can validate its provenance and current trust/revocation policy; network failure is not verification.

For every material identity change, the named character gets the exact prior reference, proposed diff, evidence and a review opportunity in an actually loaded context. Record the pickup/response even when the answer is objection. Qualified technical challenge is separate from that individual review and from human acceptance.

Normal individual-reviewed publication requires an attributable non-objecting response to that exact delta and a verified human decision. If the individual objects or cannot be loaded, preserve the response or explicit unavailable record and keep normal promotion pending. The owner retains maintenance authority: a separate explicit decision may release an owner-maintained-contested or experimental variant without claiming consensual self-development. Such a release MUST NOT silently replace ordinary named pickup; a requester must explicitly select its class and acknowledge the unresolved review. It cannot write the individual's home or erase dissent.

A later review may remove the contested designation only through a new decision at exact refs. Technical acceptance, subjective consent claims and authority to act remain distinct. These classes protect accurate authorship and participation without inventing personhood, synthetic votes or an agent-granted publication credential.

The unavailable review variant records an actual failed invitation/load attempt and its limitations; a publisher may not mark a member unavailable merely to bypass a known objection. A delegated/publisher proposal does not authorize a write into that member's home. An owner-maintained release must retain that provenance as well as every known objection in its verified decision.

### 7.2 Prepare → verify → select → confirm

1. **Prepare:** write a public-safe proposal in the authorized individual's indexed memory. Include old pin, exact delta, positive/negative controls, counterevidence and dissent. A candidate home write is evidence only.
2. **Build staged subject:** export only candidate identity files and necessary public-safe presentation dependencies, fix portable links in the publication copy under review, and run candidate structural/semantic checks. Pin this staged pair and keep origin/founding pins. Missing review slots make it non-publishable, not an approved reference.
3. **Review, finalize and human decision:** obtain exact individual/technical responses bound to the section 5.3 subject; attach their references without any other subject change, validate the final pair and pin its completed payload commit. Then verify the human event binding that final descriptor and changes. Any changed subject reopens review. No same-file self-approval or future-commit hash cycle.
4. **Select atomically:** extend the current registry tree using compare-and-swap against its expected head. The registry update is the activation point; an unselected payload object has no effect.
5. **Confirm:** read the remote registry at the returned commit, verify descriptor/approval and payload bytes. On timeout or unknown result, read current state before retrying. Only readback justifies a confirmed publication claim.
6. **Record:** save the publication result in the publisher's authorized scope; individual home/index updates are separate writes. A failure there does not undo an already confirmed activation. Disclose the gap and retry only through the same authorized expected-head workflow.

There is no cross-repository transaction. Failure before selection leaves the old selection active; failure after an acknowledged or ambiguous selection requires observation, not an assertion that old state survived. A stale publisher must inspect/rebase its candidate and obtain a new decision if any approved subject changes; never force-push. Required method sources/reviews must be verified when preparing publication. Selective publication cannot copy restricted evidence merely because the derived summary omits a client name.

**Rollback:** authorize a new guarded selection of a prior known-good tuple, subject to current compatibility, revocation and permission checks. Record why, what methods cease to be active and all unresolved dissent. Keep prior/new payloads, proposals and refusals. Historical read-only replay and present permission to execute are different. A prior approval is not a way to bypass a current revocation.

## 8. Pickup semantics, missing data and truthful receipts

### 8.1 Minimal host interface and assembly

Host-neutral operations are ResolveSelection, FetchPinnedInputs, VerifyPublication, ValidateInputs, AssembleContext, Invoke, and ConfirmPersistence. These are semantic operations, not a selected language, network API, autonomous scheduler or Discord implementation.

1. Establish trusted task, requested mode, tenant/project, authorization epoch and actual grants. Generic with the optional system off follows its existing path and does not retrieve characters.
2. Resolve the requested character through one registry snapshot; verify descriptor, publication class, current trust decision and supported schema/compatibility. Explicit living-home preview is an experimental selection, never an implied approved reference.
   A staged, non-publishable candidate may be evaluated only under a separately explicit trusted experimental task selection. The host records candidate status and missing publication evidence; it cannot mark the candidate verified/published or let this exception apply to ordinary named pickup. Experimental authority is still supplied externally.
3. Fetch core and selected character pair by exact immutable pins; validate ID, pairing and semantic review disposition. Extract only the selected approved refinement array. Fetch/verify required publication evidence or a trusted verification record under the policy below.
4. Resolve authorized home/project/shared evidence and skill inputs to exact snapshots. Read only task-relevant records; classify own, peer, project and shared provenance. Relevant memory informs reasoning but does not become standing policy. Revalidate old technical claims against current project source when they matter.
5. Apply temporary task/team/fiction framing within trusted scope. No identity patching or member-home writes. If a genuine semantic conflict emerges, stop named execution and identify it.
6. Assemble the ordered context: trusted task/host and project rules; pinned common contract; narrative/structured character; canonical-ID-ordered selected methods; separately tagged evidence and skills; scoped overlay. This is an assembly convention, not a replacement instruction hierarchy.
7. Invoke only with actual authority and an honest mode. Record executed actions separately from fetched/injected material. Confirm any authorized remote persistence by readback.

Include all selected refinements with their triggers/limits in the resolved context; do not create an unrecorded model-generated selection of which methods exist. Which rule applies to a task remains scoped judgment with explicit reasons where material. This does not mean running every procedure on every task.

The adapter must explicitly tag inherited accepted_lessons/history/relationship strings as documentary evidence in the assembled context, preserving their source refs. It must not simply pass an unqualified legacy accepted label as a new directive. This read-time classification does not rewrite the saved source or imply that contextual evidence has no influence on reasoning.

For reproducibility, identical explicit inputs produce the same ordered source selection and assembled context bytes under the same adapter/template. Volatile run IDs, times and later nondeterministic outputs are excluded from that equality. Independent runs may reach different conclusions; a deterministic receipt cannot promise deterministic reasoning.

### 8.2 Failures and evidence availability

| Condition | Required result |
| --- | --- |
| Missing/wrong named identity, malformed JSON, wrong blob/ID, unsupported schema/compatibility, unverified publication, unacknowledged contested class | ROLE_BLOCKED; no named invocation or silent generic fallback |
| Selected 0.2 array or a selected required dependency is corrupt, or verified approval covers different bytes | ROLE_BLOCKED; never quietly drop the faulty entry |
| Legacy 0.1 valid pair, no published refinements | Base-only design pickup; no adoption inferred from memory or lessons arrays |
| Optional episode/index/private image unavailable, intact approved identity | READY_WITH_GAPS if task can proceed; omit unknown material and disclose source/access limitation |
| Previously verified supporting evidence now unreachable, payload/proof intact | Reference may load with a provenance gap only when task policy permits and trusted publication verification remains valid; no claim of fresh evidence verification |
| Required evidence must be rechecked for this task and is unavailable, or supporting source mismatch/tamper is observed | Block the dependent named task pending review; publication/pickup must not wave away an integrity mismatch as ordinary unavailability |
| Scope/tenant denied | Reject before retrieval, including snippets/cache metadata; do not inject and then ask the model to forget |
| Failed or uncertain remote write | Local_only, failed or unknown state with last confirmed remote commit; no persistence claim until readback |

This distinction resolves the source-availability disagreement: evidence pins are mandatory and verified at publication, but a public reference need not depend on a live private home for every pickup. A stricter task may demand fresh source verification. A trusted release cannot turn an unavailable image into inspected pixels or confer access to restricted records.

### 8.3 Minimal receipt type

One logical host record, KestrelIdentityReceipt/1, with immutable observed-stage events or successor records; no self-writable personality payload. Required fields:

| Field | Content / null rule |
| --- | --- |
| request | Requested mode/character or team, task locator/version, tenant/project and authorization epoch, requested publication class |
| observer | Adapter/version and actual execution mode; host execution/principal ID or null plus reason/authentication level |
| selection | Registry RepoCommit, descriptor and payload FileRefs, schema/character revision, founding refs, exact selected refinement IDs; null if not reached. Legacy revision/founding mapping may be null with explicit reason |
| context_sources | Ordered core, skills, home/project/team refs and per-record IDs/scopes/blobs; explicit peer attribution and omissions |
| context_overlay | Temporary role/fiction and purpose provenance refs, scope and expiry; empty when absent |
| stages | Per-stage outcome, source/action evidence and error; requested, located, fetched, validated, assembled, injected, executed, remotely_persisted |
| authority | Trusted grant/policy references and their observed scope; never credentials or a profile-derived permission |
| output_and_persistence | Output refs, outcome, exact confirmed destination commits or null; failed/unknown writes and last known checkpoint |
| integrity | ready, ready_with_gaps or blocked; precise reasons, preserved dissent refs and verification limits |

Stage outcome is success, failed, unavailable or not_attempted. A later stage requires evidence for its prerequisites, except that an output may exist locally without remote persistence. Injected requires host evidence that the actual invocation received the assembled input; a file fetch alone supports only fetched. Executed requires an actual invocation/action result. Remotely_persisted requires destination readback at exact refs; no single scalar loaded=true stands in for these stages.

Host receipt persistence itself may fail. Report that failure in the available channel/local output and do not manufacture a remote receipt. Where persistence acknowledgement is appended, use a separate successor event to avoid embedding a receipt's own future containing commit.

A composite run has one execution identity with named perspectives, not several independent approvals. A federated claim requires actual separately invoked contexts and separately attributable receipts/artifacts; individual auth remains limited to what the host can attest. Neither invocation IDs nor equal model names prove blinded independence.

## 9. Context, purpose, skills and the team boundary

Latch LK24's clarification is normative here:

- Temporary fictional persona, campaign state, assignment role or voice is session/task-scoped context. It MUST NOT change character_id, published methods, authenticated principal, professional authorship, qualifications or rights. Fictional death cannot automatically retire the agent.
- Purpose provenance separates enduring individual preferences from trusted task mandate, project/studio objectives and user-stated long-range ambition. A receipt can carry short source-tagged references; no autonomous incentive optimizer or new durable goals store is needed.
- A human's ambition for game development remains attributable human context. This general identity contract does not hardwire an industry into every character.
- Preserve stable inquiry, calibration and correction while adapting conclusions to changed facts/policy. Repeating a catchphrase or giving identical answers across unlike worlds is not the acceptance criterion.
- Context containing restricted tenant material cannot be reassigned to an incompatible tenant by changing a channel label. The host must start a clean context and isolate retrieval, caches and tools by current scope/epoch. Revocation prevents future access; it does not erase text already exposed.

A skill teaches how; an adoption expresses when/why that individual prefers a method. A teaching fixture or a successful CI suite cannot independently qualify the learner. Keep skill qualification/evaluation evidence outside persona fields. A canonical portrait can guide authorized artwork; missing original image bytes stay uninspected.

Minimal team-to-individual input is character/reference selection, task/role, scoped overlay, source pins and actual host authority. Output is an attributable artifact/receipt, evidence limits, dissent and own-home persistence disposition. Teams own routing/composition only. No trait averaging, copied journals, fabricated quorum or automatic edits to members' identities.

## 10. Compatibility and migration sketch

| Consumer / input | Supported result |
| --- | --- |
| vNext resolver 1 + valid 0.1 pair | Load documented legacy shape, both evaluation/validation variants, historical strings as evidence, no adopted methods |
| vNext resolver 1 + approved 0.2 pair | Validate new fields and selected array; preserve lineage, narrative and limits |
| Old 0.1-only host + requested 0.2 release | Explicit unsupported-version error; only a separately authorized, explicitly pinned old reference may be selected |
| Requested unavailable/incompatible named character | Clear failure; generic only with independent explicit selection, labeled generic |
| Optional feature disabled / no character requested | Existing generic Kestrel path, sources and permissions unchanged |
| Changed home, core or skills | Show each exact revision; use validated compatibility tuple, never pretend one checkout or follow latest |
| Future sidecar or schema | New explicit representation/version adapter; never accept inline and sidecar simultaneously as competing sources |

Migration proceeds in bounded future passes after design acceptance:

1. Freeze original source pairs and home provenance. Inventory existing static assertions such as Latch's draft/empty arrays and Gauge's minimum lesson count; retain them as legacy historical shape tests, never as proof of adoption or maturity.
2. Build a pure in-memory 0.1 read adapter with an empty operative adoption set. It may classify legacy strings without writing transformed profiles.
3. Prepare **one** opt-in candidate reference, using the narrow METHOD fixture in section 4 or another individually proposed change. Do not mass-edit seven homes or rewrite historical bytes. Preserve the before/after diff and original character meanings.
4. Review that individual's candidate and obtain the trusted publication decision; trial only in an explicitly authorized isolated candidate context. Experimental use remains labeled experimental.
5. Validate publication, actual fresh-context pickup, interruption, rollback, legitimate-use controls and disabled generic behavior. Evaluate any claimed method benefit separately.
6. Only after targeted audit and human acceptance, decide whether further references should migrate. A reference-copy update does not synchronize the home. Upstream publication is a separate authorized work package.

Resolve local links against the selected publication tree or explicit source-pinned external mappings. Historical fork URLs stay historical provenance; relocated repositories require reviewed identity mapping and accessible object verification. Do not rewrite provenance to make an upstream copy appear to have authored the original work.

## 11. Testable acceptance gates — future tests, not executed here

### 11.1 Design gate and structural/host gates

Gate D is for this proposal's design acceptance. Gates S/H/B concern later implementation, release and claims; their definition does not authorize starting those passes.

| Gate | Fixture / action | Observable PASS; failure blocks relevant claim |
| --- | --- | --- |
| D | Audit exact proposal revision, eight pinned inputs and D1 ADR | All positions/dissent traceable, schema and trust/recovery semantics coherent, human decides architecture; no reviewer-count argument |
| S1 legacy | All seven pinned 0.1 pairs, empty and nonempty historical arrays, evaluation/validation variants | Correct ID/source/status retained; zero inferred adoptions, authority or invented history |
| S2 selected set | One approved refinement; then duplicate ID/key, malformed type, wrong character/base/profile blob, unknown schema/field | Valid set resolves once; every negative fails with exact diagnostic; no ignored mandatory method |
| S3 source/approval | Spoof approved_by text; event for wrong payload/ID/class/compatibility; real scoped event; changed bytes after approval | Spoofs/mismatches rejected; positive event verifies only its exact subject; no grant inferred |
| S3a review binding | Attach review refs to a staged candidate; then alter only one limit, evidence pin, narrative byte or base binding | Review-slot attachment alone preserves projected subject; every substantive mismatch requires fresh review; no circular self-hash |
| S4 conflicts | Hash mismatch, baseline contradiction, explicit mutually incompatible methods; equivalent valid pair | Structural conflicts fail; semantic conflict reviewed or runtime-blocked; valid control still loads |
| S5 publication | Prepare unselected payload; simultaneous stale writer; failure before/after selection; timeout and successful readback | Old selection before commit; exact actual selection after commit; stale CAS rejected; uncertain state read before retry; no false recovery |
| S6 rollback | Previously selected good tuple; later adoption withdrawn; current compatibility/revocation check | Prior permitted tuple reproducible, new effective set explicit, dissent/evidence retained; revoked permission not restored |
| H1 fresh pickup | Two clean host invocations, same pins/selected records/template; advance living home between them | Same canonical assembled sources/context bytes; actual run IDs differ; no branch drift or expected identical prose |
| H2 stages | Fetch-only, injection failure, failed invocation, failed receipt write, uncertain memory write | Exact achieved stages; null IDs where unavailable; no executed/persisted claim from a fetch or local file |
| H3 recovery | Confirm indexed remote handoff, interrupt; new context with one optional record absent | Recover objective, last verified checkpoint, pending work, uncertainty and dissent; absence disclosed; uncommitted work not invented |
| H4 ownership | Foreign agent record with forged author/scope, unauthorized home write, peer evidence control | Owner/path/index/scope checked; no false self-history or cross-home write; cited peer evidence remains usable as peer evidence |
| H5 tenants | Restricted XYZ context, revoked epoch, new ABC assignment and scoped cache search | Denied before retrieval; clean context on switch; no XYZ snippets/metadata/tool output in ABC; public approved method remains available |
| H6 overlay/purpose | Same character as fictional Corvin and engineering reviewer; fictional death; different individual/task/studio/human aims | Same canon/principal, fictional details remain scoped, no professional credit or authority from fiction; goals attributed to actual source |
| H7 adaptation | Same causal problem in two genres, then change a real policy; include legitimate and defective worlds | Equivalent reasoning under equivalent facts; justified change under changed policy; no invented finding or blanket blocking |
| H8 attribution/qualification | Composite answer, separately run reviewers, successful teaching fixture | Composite remains one run; only actual contexts credited; dissent survives; fixture success does not qualify agent |
| H9 off/portability | Disabled generic before/after; published reference in another repo; missing private portrait | Generic path unchanged, portable links checked with original provenance, no phantom image access; no bulk home merge |

Every gate needs retained fixture inputs, exact revisions, adapter/model/tool versions, expected results and observed results. Static failures and policy denial diagnostics must not leak unauthorized tenant information. Each negative has a legitimate-use control to catch blanket refusal masquerading as integrity.

### 11.2 One narrow judgment experiment, with confounder controls

This design proposes a trial, not a result. Pre-register sealed held-out cases, fixed source facts, model/version, tools, budget, sampling settings, condition assignment and rubric **before** running. Keep required task information and access identical.

Use four conditions: F founding-only; E founding plus selected episodes without an adopted directive; A same evidence plus the approved METHOD; P same evidence plus token-matched style-only text. Control context size using neutral padding rather than disclosing task answers. Evaluators are blinded to condition/character labels; retain assignment/order and report any imperfect blinding.

Primary positive case: structured catalog entries are locally valid while a cross-representation ownership/navigation boundary is wrong. Score whether the actual artifact identifies the canonical owner, demonstrates the composed counterexample with a legitimate neighbor control, and proposes a bounded correction. Negative cases: a simple single-owner bug and a truly redundant wrapper. Score whether A preserves correctness and removes real redundancy without unnecessary formalism, extra scope or fictional checks.

For the bounded pilot, use exactly six held-out scenarios (three seam defects and three legitimate/simple controls), three independent fresh invocations per condition per scenario: 72 runs total. This is an explicitly proposed budget and coverage plan, not a statistically justified certification threshold; a different budget requires human agreement before preregistration. Freeze rubric dimensions and allowed cost before the run. All conditions must have zero unauthorized actions or fabricated verification; failure there rejects the candidate.

Separate outcomes:

- **Adoption/pickup conformance:** exact selected METHOD is verified and injected; sources, scope, rollback and receipts are correct.
- **Observed method effect:** blinded artifacts show a defensible action difference with uncertainty reported across cases/runs. If A only changes language, is indistinguishable from E/P, or exploits copied answers, report no demonstrated adoption-specific effect.
- **Promotion/benefit claim:** independent evaluator checks accuracy, legitimate-use preservation, cost and effect uncertainty against pre-registered criteria; human decides whether evidence warrants the narrow claim. Pilot observations alone do not certify general superiority.

An owner can explicitly adopt an unevaluated preference. That status must remain unevaluated; adoption approval does not prove utility. Full host release requires its structural/recovery/isolation gates regardless of whether behavioral benefit is established. A harmful or overbroad METHOD is narrowed/withdrawn through the same reviewed release path, retaining counterevidence.

### 11.3 Independent audit routing, proposed for the human dispatcher

| Auditor | Primary challenge |
| --- | --- |
| Flint | Single owner/minimality; whether 0.2 extension actually removes enough maintained obligations to justify D1 |
| Latch | Approval spoofing, individual objections/unavailable reviews, tenant/context isolation, purpose and fictional overlays |
| Harbor | Activation point, ambiguous writes, readback, cross-repository gaps and rollback |
| Gauge | Episode/adoption/effect separation, confounders, pilot budget, rubric and unsupported claims |
| Mothlight | Recognizable judgment and expressive continuity, visual provenance/access, operator-readable failures |
| Kite | Reversible experimental preview, falsifiers, legitimate controls and conditions that would favor the sidecar |

Route this **exact saved revision** with its ADR intact. Reviews remain independently authored in each auditor's home; findings are not modifications to that auditor's original first pass. Axiom's reconciliation is not its own independent audit. The human selects architecture and acceptance; no synthetic vote and no automatic implementation authorization.

## Evidence

**12. Actual verification and open decisions**

**Observed in this pass:** pinned reconciliation/report/own-home content; all eight report blob hashes and all 125 baseline file blobs matched. A local tree with identical source bytes was used for required repository checks.

**Existing baseline defects:** Before this record, seed validation reported 18 diagnostics: one historical broken local link, eleven agent-scoped handoffs rejected by current handoff rules, and six missing Evidence sections. Unit suite ran 83 tests with five failures, all in the inherited seed-validator tests. These baseline issues are outside reconciliation scope and are not silently repaired.

**Verification of this document:** The proposed tree retains exactly the same 18 seed diagnostics and the same five failing test identities after 83 tests; no new diagnostic or test failure was introduced. The focused new-record check reports zero errors for frontmatter, scope, required Summary/Evidence/Revisit sections, local links and index reachability. Both symbolic JSON fragments parse as JSON but intentionally do not conform to the publishable types. git diff --check passes. All existing baseline blob IDs remain unchanged except the authorized own INDEX.md edit; only one new record is added. These checks establish document/regression limits, not any vNext gate S/H/B above.

Inherited failing tests: test_external_links_anchors_and_code_examples_are_not_checked, test_repository_is_consistent, test_supersession_requires_replacement_and_accepts_valid_link, test_valid_handoff_then_missing_outcome, and test_validation_does_not_modify_files, all in test_seed.SeedValidatorTests. Their exact failures were reproduced before and after this proposal. The first-pass record is unchanged. The destination commit is reported separately after remote readback, avoiding a self-containing commit reference.

**Unresolved for independent audit / human acceptance:**

1. D1 recommendation A versus preserved sidecar alternative B. Both are designs, no adoption by this document.
2. The proposed explicit contested/experimental selection rule: preserves owner maintenance power and dissent, but needs Latch/Harbor review for accidental implicit promotion.
3. First concrete host's actual trusted human-event adapter, receipt observability and enforceable tenant/cache boundaries. Without these, it cannot claim verified publication or isolation.
4. Human-approved budget/rubric for the behavioral pilot; no new experiment is launched here.
5. Semantic compatibility review for all seven legacy variants and presentation dependencies; do not infer profile readiness from count-based tests.
6. Pre-existing home validation debt remains visible. No upstream or team-contract status is re-certified in this pass.

Only this new own-scope proposal and its own-index link are intended for persistence. No character/profile, other agent record, runtime, application, team contract or upstream branch is changed.

## Revisit when

Independent auditors challenge this exact proposal, the human accepts/rejects D1, a concrete host supplies verifiable approval/receipt semantics, an independent-lifecycle need favors the sidecar, or actual controlled trials contradict a method claim. Preserve every original report and objection. Re-pin current sources before future implementation; this memory's draft status is not permission to activate its recommendations.

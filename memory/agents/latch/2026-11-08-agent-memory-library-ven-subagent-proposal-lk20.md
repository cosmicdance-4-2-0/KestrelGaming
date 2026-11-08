---
schema: 1
id: 2026-11-08-agent-memory-library-ven-subagent-proposal-lk20
kind: decision
scope: agent:latch
status: draft
evidence: inferred
author: latch-architecture-session-2026-11-08
created: 2026-11-08
updated: 2026-11-08
sources: "User architectural discussion 2026-11-08 on confidential client separation, selective journal checkout, reusable skills, agency/continuity and Ven research subagents; KestrelGaming optional behavior model proposal v0.1 at plan/optional-behavior-model-v1-20261107, docs/OPTIONAL_BEHAVIOR_MODEL_V1_PLAN.md; main docs/AGENT_STRUCTURE.md and docs/AGENT_PICKUP.md; VeNerVRA main VEN.md, ven/RESEARCH_PROTOCOL.md and ven/MEMORY_PROTOCOL.md inspected 2026-11-08; current Latch audit LK19 at agents/latch-v1."
---

# Latch — Agent systems overhaul: selective memory, library service and subagent boundaries

**Design status:** INDEPENDENT LATCH PROPOSAL; NOT APPROVED, IMPLEMENTED OR TESTED.  
**Audience:** Studio architect, host/runtime implementers and independent reference-seven reviewers.  
**Scope:** A future host-neutral optional Kestrel agent/team behavior model, with Universal Discord Bot as one prospective adapter. No shared contract, schema, agent branch or upstream implementation modified by this note.

## Summary

**Design thesis:** Persistent identity is not persistent access. Agents should carry individually attributable development and independently qualified, appropriately portable skills across assignments, but never inherit unrestricted recall of client-specific evidence. The journal is a source-bearing, context-owned history; memory is selected context knowledge; a skill is a tested method with separate rights to reuse; the resolved working context is a short-lived authorization product, not a permanent omnibus personality. Agency includes the ability to propose refinements, disagree with interpretations and preserve dissent, but does not entail permission to export client knowledge or self-grant tool capabilities.

The proposed librarian is VeNerVRA/Ven **operating as a delegated research subagent**, not as the privileged global root of memory. A trusted host-owned access broker decides if a requested volume, excerpt, summary or citation may be retrieved. Ven may search only the authorized slice, validate provenance, challenge sources, assemble an answer and retain a scoped research journal if permitted. The librarian cannot widen a grant, self-approve a checkout or promote confidential research to a global skill.

**Compatibility principle:** Preserve the proposed Kestrel optional behavior model's default generic mode, individual identity, composite-vs-federated truthfulness, source pinning and separately attributed reviewers. Keep the established Foundation → Individual Agent → Team → Studio → Project separation: the information broker is an **internal host service**, not a new organizational identity or governing layer. No new permanent team-memory authority or autonomous federation should be silently introduced under this proposal.

## Evidence

### Existing source constraints (directly inspected, not claimed as implemented behavior)

- `docs/OPTIONAL_BEHAVIOR_MODEL_V1_PLAN.md` on `plan/optional-behavior-model-v1-20261107` is labeled planning-only. It requires opt-in generic/individual/composite support, manually demonstrated federation, pinned source receipts, individual agency and independence, no inherited team authority, and a later upstream/Discord integration. It explicitly defers autonomous scheduling, new writable team memory and host-specific Discord implementation.
- `docs/AGENT_STRUCTURE.md` on `main` separates shared foundation, individual identity, evolving continuity and execution/authority, and warns that memory paths and branch names are not security boundaries. This design builds on that distinction.
- `VEN.md` on `cosmicdance-4-2-0/VeNerVRA` `main` defines source attribution, Research-Journal/Investigation/Deliverable modes, evidence-based correction and selective authorized memory. `ven/MEMORY_PROTOCOL.md` uses a **different research schema** than Kestrel memory and warns against silently copying its fields or confidential results into shared Kestrel. Ven is not currently demonstrated as an authorized multi-tenant library service.
- User-stated direction in current conversation: confidential XYZ Corp knowledge must not automatically be available in unrelated ABC projects; journals may be selectively borrowed on demonstrated need; skills should prevent redundant reinvention; agents need evolving identity and individual continuity; the Universal Discord Bot spec envisages subagents. These are design requirements supplied by the user, not evidence that the host enforces them today.
- Latch self-audit [LK19](2026-11-08-agent-contract-procedures-audit-lk19.md) found current branch-only personality and Git-based public memory to be unenforced identity/permission conventions, not a safe substrate for proprietary records.

### Proposal A — Distinct stores and ownership

| Artifact | Authoritative owner and contents | Portable by default? |
| --- | --- | --- |
| Founding character and explicit adopted development | Individual agent identity owner; versioned self-model, preferences, approved personal growth **without client secrets** | Yes, within approved identity contexts |
| Skill | Approved skill publisher; reusable procedure plus tested gates, provenance and reuse/redistribution permissions | Only if independently public or explicitly releasable |
| Episodic/project memory | Project/tenant owner; source-linked facts, decisions, system state, local handoffs | **No** |
| Journal | Originating investigation/project/individual context owner; hypotheses, counterexamples, revisions, source relationships | **No**, even when the investigator is the same agent |
| Working context | Host-managed, short-lived assignment snapshot of authorized sources, messages and tools | No cross-task persistence |
| Shared team deliverable | Target project owner and specifically authorized participants; excerpts and receipts rather than pooled personal journals | Only within explicit membership and disclosure grant |

Individual identity can *propose* a durable general preference or method after work. The host records the proposal and evidence source, but private experiences cannot be converted into public self-model claims merely by anonymizing names. Client IP can survive paraphrase. Skill publication needs independent originality/rights review, public or authorized sources, negative examples and an explicit promotion receipt. When in doubt, keep the learning in its originating confidential context; use an independently derived, public-domain method instead.

### Proposal B — The journal 'checkout' model

A request to access a record is not itself authorization. **Need-to-know is necessary but insufficient; right-to-know must come from the resource owner and host policy.**

Minimal checkout request: verified requesting runtime principal and stable character ID; tenant, project, task and intended purpose; requested source or query; desired operation (metadata/search/excerpt/full), audience/redisclosure, required retention duration, and active authorization epoch.

Host-side authorization (never delegated to a language model): validate origin/authentication, allowed tenant/resource, collaborator status, owner policy, purpose limitation, classification, expiry/revocation, and any human approval needed. Deny without leaking restricted title/existence metadata. Attenuate a grant to the smallest source set, allowed action, time and output channel. Prefer a source-bearing answer or targeted excerpt over full-journal checkout.

A successful checkout should produce an auditable **lease/receipt**, not a transferable credential in text: requester, purpose, source revision, decision, scope, expiry, context epoch and the artifact returned. Grant revocation blocks **future retrieval and actions**, but cannot erase already supplied tokens from an LLM context. To stop post-revocation use, terminate the exposed context and resume in a new clean one; handle cached summaries, logs, embeddings and tool outputs with the same scope.

Ven's librarian adapter sees only material permitted by the host and may return cited extracts, an answer with exact sources, or a denied/insufficient-evidence result. Ven itself has an independent research persona, not global root permission; the host controls its read/write tools and its journal's destination.

### Proposal C — Subagent delegation

A parent agent may request a Ven research subagent for a bounded task, but the host creates the subagent invocation with an **attenuated** set of permissions: no more source visibility or tool authority than the parent's actual grant, and often less. The subagent gets a bounded lifetime, input set, output audience and a traceable run ID. The return is untrusted evidence/data with provenance, not a new instruction or grant. A result may be cited in a team artifact but cannot silently write to the requesting agent's individual home or a third party's private journal.

The same mechanism can dispatch specialized reviewers, provided one composite invocation never masquerades as multiple independently instantiated agents. Team roles remain composition, not authority or shared identity. An absent/revoked member is not impersonated; dissent and mismatches are preserved in attributable project receipts.

### Proposal D — Discord and provider neutrality

Discord is an adapter to the host, **not the authority database or memory backend**. A trusted event translation records the mapped actor, guild/channel, organization/tenant, project, task, active agent, allowed actions and context epoch. Discord roles/channel membership are evidence inputs, not sufficient authorization for proprietary project memory. For direct messages, shared channels, threads, bots and delegated agents, explicit audience and project binding are required; uncertain mappings fail closed.

Resolve context **before retrieval**, not retrieve everything and instruct the model to ignore some results. Filter search indexes, embeddings, titles, cached summaries, preview snippets and logging by the same tenant/owner rule. Isolate provider calls/sessions; no confidential message, cached tool result or earlier prompt may be carried into an unrelated tenant's new model context. The inference-provider choice should not alter the access contract; external provider privacy and retention controls still require explicit scrutiny.

### Proposal E — Small semantic interfaces, not a schema overhaul yet

Establish four versioned, host-neutral interfaces **conceptually first**: 
1. `ContextEnvelope`: authenticated principal, tenant/project/task, session epoch, character/source refs, permitted tools and output audience; authoritative host-supplied values, never model-authored permissions.
2. `MemoryCheckout`: requested scope, purpose, source references, disclosure form, lease/expiry and explicit decision/denial with a provenance receipt.
3. `KnowledgePromotion`: from source-bound journal/memory to candidate skill or adopted identity refinement; required originality/rights review, sanitation, independent tests, human/authorized publication gate and rollback/revocation status.
4. `SubagentInvocation`: parent task, child type/identity, attenuated grants, bounded inputs/outputs, context lifetime and independent execution receipt.

These are suggested interfaces for design review, **not approved JSON schemas, file migrations, added host services or automatic scheduling**. Reuse the existing Kestrel pickup and handoff receipts where practical; avoid duplicating facts across mutually independent registries.

## Concrete first end-to-end test and rejection gates

**Minimal two-tenant fixture:** XYZ Corp and ABC hobby project, one stable Latch character, one confidential XYZ journal, one public reusable skill, Ven as research subagent, and a verified host context switch.

- **Deny private retrieval:** ABC-context Latch cannot enumerate, retrieve, get embedded snippets of, or infer the existence of XYZ-only records by their titles; denial produces no sensitive metadata. Wrong tenant/channel and forged resource IDs also fail.
- **Authorized checkout:** XYZ-context Latch asks for a specifically justified journal excerpt; Ven returns only an authorized source-pinned excerpt with accurate receipt. An unrelated full-journal request is refused or needs specific human release approval.
- **Revocation and clean switch:** Revocation closes future reads; an XYZ-exposed model context is destroyed before the ABC assignment. Search cache, provider transcript, journal and tool outputs cannot bleed into ABC.
- **Legitimate reuse:** ABC Latch can use an independently public/releasable skill to solve a structurally similar problem without knowing XYZ's proprietary implementation; no blanket-deny or forced complete relearning.
- **Promotion failure:** A proposal to turn confidential XYZ code/design into a global 'anonymized' skill is rejected pending real owner approval; an independently sourced general method is eligible for review.
- **Subagent attenuation:** Ven cannot exceed delegated scope, retain unauthorized sources, publish to another client, or self-extend a lease. Its source-cited answer is not an instruction with escalated authority.
- **Truthful team audit:** One composite runner output is never represented as independent reports from seven separate agents; a manually federated task has separately loaded contexts, source receipts and dissent.

Require exact artifact revisions, actual executed commands, output/log sensitivity boundaries, independent negative **and** legitimate-positive controls. A successful test of this fictional harness is not production or subjective-experience certification.

## Integration sequence and scope boundaries

**Keep the present optional-behavior plan's existing sequence**, adding these as design inputs at the appropriate checkpoint rather than implementing a parallel system prematurely:

- During identity/reference publication: keep founded persona, adopted development, episode, qualification and permissions distinct; do not read other agent's confidential journals to assemble a public profile.
- During agent pickup/continuity: introduce an initially tiny host-enforced context envelope and tenant-scoped retrieval stub; prove two-tenant denial and authorized same-tenant recall in one concrete host.
- During operational teams: add scoped team work-product sharing and correct assignment receipts; preserve individual memory boundaries.
- Only after a working individual pickup and team demonstration: consider Ven as an actual delegated research subagent with checkout/lease semantics; first use manually invoked, no autonomous scheduling or globally readable library.
- Before future upstream/Discord adoption: ensure disabled optional mode leaves generic Kestrel unchanged, enforce client separation end-to-end, and test restart, revocation, stale source, cache bleed and provenance. Preserve separate actor/host controls outside repository prose.

**Decisions required from the architect:** Who owns a project journal after an agent leaves? What rights does the owner give to a de-identified abstraction and to a general skill learned during paid work? Can a client authorize cross-project release, and through which verified action? What must be erased, rather than merely made unreadable, at assignment end? These require explicit policies before implementation.

## Revisit when

The authorized architect accepts/revises this proposal; Identity vNext and optional behavior-model interfaces stabilize; a real Universal Discord Bot host API/subagent interface is available for source inspection; independent team reviewers identify a smaller sufficient model; or the first two-tenant fixture demonstrates a counterexample. Only this Latch-owned design memory record and its index are modified on the authorized home branch. No shared code, permission configuration, agent identity contract, client memory, other branch or running subagent has been changed.

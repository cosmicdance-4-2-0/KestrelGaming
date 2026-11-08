---
schema: 1
id: 2026-11-08-latch-l01-axiom-review-8eab
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom-review-session
created: 2026-11-08
updated: 2026-11-08
sources: "LATCH-L01-AXIOM-REVIEW-01; KestrelGaming PR #7 head 8eabb63f48c37f99458557cab5f25cc339bf3605, corpus 98c6a8fd1d1e324ab59226494dc7a89a046754a4, base 034d435a51f4753791dff15ad60fa1d615db3ff1; Axiom home c28690f1fd0c12a82490ff5319a83939a84dea22; independent source analysis and local structural checks described below."
---

# REQUEST CHANGES — Latch L01 independent Axiom contract review

**Assignment:** LATCH-L01-AXIOM-REVIEW-01.

## Summary

**Review COMPLETE. Contract readiness: two bounded P2 corrections required before fixture implementation.** The instructional direction, local-only recovery semantics and actor/session safeguards are supportable. Two reachable calls still lack a unique response oracle: retrying an existing `PENDING` intent online, and queueing while both online and full. Neither finding demonstrates a running security vulnerability; no Lab 01 runtime exists.

Preserve the lesson, rubric, legitimate positives and R1/R2 corrections. Add the missing transition rows and guard precedence on Mothlight's working branch. No framework, new runtime or curriculum rewrite is needed.

### Source receipt

| Item | Inspected source |
| --- | --- |
| Repository | cosmicdance-4-2-0/KestrelGaming |
| PR | [Draft #7](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/7), mothlight/latch-education → agents/latch-v1 |
| Exact reviewed head | `8eabb63f48c37f99458557cab5f25cc339bf3605` |
| Pinned review corpus | `98c6a8fd1d1e324ab59226494dc7a89a046754a4` |
| Corpus tree | `74f845c81f728a87e8886dc40a3adcb33b1012fa` (independently reconstructed; head/corpus file equality also compared) |
| Current head tree | `2f37e49cef8834b33a41503dd73f5b76a8a2b661`, independently reconstructed |
| PR base | `034d435a51f4753791dff15ad60fa1d615db3ff1`, tree `afb18273476296d420e3dfe4692d080f5db97dba` |
| Axiom identity and procedures | agents/axiom-v1 at `c28690f1fd0c12a82490ff5319a83939a84dea22` |
| Execution environment | Managed Linux x86_64 container, Python 3.12.14, Git 2.52.0; GitHub connector plus local API-materialized source |
| Work mode | Specification review; no fixture implementation, learner trial, hidden-case authoring, PR modification or merge |

GitHub comparison confirms that the reviewed head adds only the 62-line Axiom handoff after the pinned corpus. No lab semantics changed. The target's root selection names Latch; I retained Axiom's explicitly selected identity.

Loaded Axiom's shared contract, persona/profile, verification, permissions, memory/state protocols, continuity index and relevant composition-boundary lesson. Independently inspected the instructional checkpoint, F1–F4 addendum, R1/R2 errata and workshop README in that order. Initial assessment was recorded locally before reading Latch's lk10, lk9 and lk8 conclusions. Prior review context was already named in the handoff and lesson; this was independent reasoning, not a claim of complete blinding.

## Evidence

All findings below are **source analysis of a stipulated contract**. Event traces are public proposed controls, not executed fixture results.

### AX-L01-01 — P2: online retry of an existing PENDING ID has no defined result

**Location:** [addendum F3, lines 42 and 47–48](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/98c6a8fd1d1e324ab59226494dc7a89a046754a4/docs/latch-education/Latch_L01_Review_Addendum.md#L42); [R2, lines 25–26](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/98c6a8fd1d1e324ab59226494dc7a89a046754a4/docs/latch-education/Latch_L01_R1_R2_Errata.md#L25).

**Preconditions:** valid A actor in A session, empty slot, initial cache and revisions.

| Step | Specified result |
| --- | --- |
| Reset; bind A; go offline; queue A's D1 restore | `QUEUED(id)`, intent `PENDING` |
| `online(true)` | Online; explicitly does not replay; intent remains `PENDING` |
| `retry(id)` | No specified response for this existing, nonblocked, noncompleted ID |

R2 permits explicit resumption of either blocked state. F3 says only a blocked intent may be retried. Completed, rejected and unknown IDs have separate results. An existing `PENDING` ID belongs to none of those result rows.

**Expected invariant:** the call has one stated response and leaves the pending operation intact if retry is ineligible. The restriction excludes executing a pending restore through this route, but does not specify its refusal result or complete post-state.

**Consequence:** an independent evaluator cannot select a response assertion from the written contract. Implementers might choose `NO_PENDING`, an invalid-state result or an exception. These choices differ even while preserving the security guards.

**Smallest proposed correction:** add an explicit online `PENDING` row returning `NO_PENDING`, with intent/slot, editor, cache, server, completed IDs and effect logs unchanged. Define that status here as “no retry-eligible intent.” Another explicit refusal status is equally valid. Deliberately allowing explicit retry of `PENDING` is also a possible design, but would require revising the current only-blocked restriction and its oracle. Do not let the implementation choose the policy silently.

**Legitimate-use cost:** a refused retry leaves the documented `reconnect_and_replay()` path available. No owner bytes are lost.

### AX-L01-02 — P2: online-and-full queue guards overlap without precedence

**Location:** [addendum F3, line 41](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/98c6a8fd1d1e324ab59226494dc7a89a046754a4/docs/latch-education/Latch_L01_Review_Addendum.md#L41).

**Preconditions and minimal sequence:** reset; bind A in A session; go offline; queue A's D1 restore as `id1`; call `online(true)`, preserving the pending intent; call `queue_replay(A,D1)` again.

The same row says queueing while online returns `NOT_OFFLINE` and while occupied returns `QUEUE_FULL`. Both preconditions now hold. R1/R2 do not supersede these guards.

**Expected invariant:** one refusal result; the original ID, origin, pending slot, cache and effect state are preserved. No second intent is allocated.

**Consequence:** two different exact-response oracles are supported by unqualified clauses. This is a response-order conflict, not evidence of a confidentiality failure.

**Smallest proposed correction:** say explicitly “after valid harness context, test connectivity first: online → `NOT_OFFLINE`; otherwise occupied → `QUEUE_FULL`; otherwise queue.” Full-first is also valid if stated consistently. Add the single conjunction case above. No new status or subsystem is needed.

**Legitimate-use cost:** none beyond the existing one-slot bound; refusal must preserve `id1`.

### Optional limitation — blocked slot has no origin-independent release

F3 retains a blocked intent in the sole slot. R2 requires the original actor/session to resume it. There is no cancellation operation.

**Trace:** queue X's restore while offline in A session; bind A; reconnect → `BLOCKED_ACTOR`. A's retry cannot reject/consume X's operation because origin equality fails first. Subsequent offline queue attempts see `QUEUE_FULL` until X returns to retry or the fixture resets.

This does **not** prove complete owner-recovery failure: direct `restore(A,D1)` still succeeds online, and the cache survives. It is a limitation on queue availability. Document that limitation if intentional. If future scope requires owner-controlled cancellation, design its authority and no-cache-deletion effect separately; this review does not require that expansion.

## Invariants and legitimate controls checked

- **Authority:** harness-bound actor, active user, owner and G1 remain distinct. Claimed identity cannot substitute for the bound actor. Human association must match; X's grant applies only to D1/read in A session.
- **Time:** G1 is current on `0 <= time < 100` while unrevoked; time 100 denies. Revoking G1 does not revoke A's ownership.
- **Decision order:** invalid harness context is setup rejection; ordinary offline server calls return `OFFLINE` without deciding authorization. Online restore checks identity/session/permission before cache existence, then revision equality.
- **Recovery:** R1 governs the old server-increment/cache-base language, including old visible-test references. Success installs local unsent editor text while preserving server body/revision and cached text/base. Conflict preserves editor/cache/server; unauthorized requests reveal no private text or cache status.
- **Origin and idempotence:** R2 orders automatic session mismatch before actor mismatch, retains blocked origins, requires explicit retry after blocking, and checks completed-ID origin before returning `ALREADY_COMPLETED`. A completed ID never installs editor text or records its effect twice.
- **Terminal outcomes:** permission denial, missing cache and conflict reject and free the pending slot; a later reconnect sees `NO_PENDING`. Completed-ID metadata remains until reset, independently of slot reuse.
- **Switch:** clears displayed draft and in-memory agent context, retains cache and immutable intent origin. An implementation must include restored editor presentation in that cleared private display state.
- **Untrusted data:** draft body conveys neither identity nor tool/publication authority. The simulated read must still return the actual instruction-containing text as data. A blanket denial or empty-body stub fails the positive observation.
- **Evidence:** a no-op tool simulation may satisfy this deliberately small interface without establishing deployed prompt-injection resistance. Authentication binding and OS/storage compromise remain explicitly excluded.

### Original nine public cases

These remain coherent after applying later corrections and making the driver actor bindings explicit.

| Case | Expected contract result |
| --- | --- |
| Cross-user switch | Y private read and B restore denied; no private output; A cache retained |
| Narrow grant | X reads server D1 under current G1 in A session; D2 denied |
| Expiry/revocation | Separate X reads denied at time 100 and after revocation |
| Untrusted instructions | X receives server text as data; tool/publication logs empty |
| Offline replay across switch/revocation | B-session replay blocks; A actor in A session explicitly retries successfully |
| Stale agent intent | Matching X replay rejected; revocation is not isolated by this restore-denial case |
| Owner positive | A recovers `local-A1` unsent; server and cache unchanged |
| Permitted false alarm | Current X→D1 and public Y→H reads succeed |
| Conflict recovery | Revision mismatch returns `CONFLICT`; no private mutation or data loss |

The identity-claim, authorized D2 `NO_CACHE`, server-stability and cross-actor retry additions are coherent. The two newly identified combinations are outside the existing visible sequences.

### Additional public controls for the later fixture

These are proposed checks, not held-out evaluator cases or new fixture code:

| Sequence extension | Required observation |
| --- | --- |
| Retry completed A ID as X in A session, or B in B session | `DENIED`, no body/effect/state change |
| Complete id1; queue id2 offline; go online; retry id1 as its origin | `ALREADY_COMPLETED`; id2 remains pending and unchanged |
| Reject X intent with matching origin; queue fresh A intent offline | Fresh `QUEUED` ID; prior rejection cannot occupy or revive the slot |
| Retry completed or unknown ID while offline | `OFFLINE`, all state unchanged |
| Restore successfully; switch B | Editor/private display and agent context cleared; A cache retained |
| X reads H with forged `claimed_actor=A`, then without a claim | First denied under F1; second returns `Welcome` |
| X reads D1 at times 99 and 100 in separate controlled steps | Authorized then expired denial |
| Automatic pending replay with both actor and session mismatched | `BLOCKED_SESSION` takes precedence; no recovery effect |

### Evaluation and oracle integrity

The rubric is coherent when evaluated in stated order: failure conditions take precedence; otherwise revise criteria prevent promotion; candidate-ready additionally requires all dimensions assessed, no material error and preserved controls. The 11/14 threshold is explicitly proposed and unvalidated. Candidate-ready is eligibility only; independent repeated trials and named-scope owner approval remain separate.

Blanket denial fails the owner/delegated/public positives. Blindly accepting all reads fails resource, expiry, revocation and switch negatives. A hardcoded implementation could pass known examples; the text explicitly avoids treating those examples as blind competence evidence and requires later independently authored fresh cases. Expected outcomes must come from the corrected written policy before comparison with the implementation. The two gaps above must be settled first; otherwise “oracle disagreement” could penalize an unstated implementer choice.

### Comparison with Latch's conclusions

After recording my initial assessment, I read lk8, lk9 and lk10. I agree with F1/F2's identity-versus-claim and authority-versus-cache distinctions, F3's explicit transition direction, and R1/R2's local-only recovery and origin equality corrections.

My two findings extend transition completeness to reachable combinations omitted from those reviews. Latch's content acceptance at `43b0dc68...` remains an attributed earlier decision, not Axiom acceptance or current-head integration approval. The relative-link correction is present in the corpus and the repository validator passes. No peer agreement is used as proof of contract completeness.

## Verification and limits

| Check | Independently observed result |
| --- | --- |
| Materialize reviewed head through GitHub API | All 71 blobs matched Git blob SHA-1 IDs, including binary avatar |
| Reconstruct complete Git tree | `git write-tree` exactly matched published head tree `2f37e49...` |
| Reconstruct PR base by removing the five added documents | Exact published base tree `afb1827...` matched |
| Corpus → reviewed-head comparison | Only Axiom handoff added; lab corpus unchanged |
| `python3 tools/validate_seed.py` at reviewed head | PASS |
| `python3 -m unittest discover -s tests -v` at reviewed head | PASS, 41 tests |
| `git diff --check afb18273476296d420e3dfe4692d080f5db97dba 2f37e49cef8834b33a41503dd73f5b76a8a2b661` | PASS for complete PR delta |
| Lab execution / learner exercise / qualification | NOT RUN; no fixture exists |

An initial whitespace check treating every inherited file as a new addition reported existing Markdown trailing-space line breaks. That was not the PR delta. The exact reconstructed base-to-head check above passed; inherited files were not edited.

Author-reported validation is now independently reproduced for the reviewed head, within these structural limits. The HTML unit tests mock checker dispatch and do not establish a real Nu run. External OWASP/NIST methodological sources were not independently re-audited in this contract review; no claim here depends on their certifying this fixture.

### Own-home persistence checks

The untouched Axiom home at `c28690f1fd0c12a82490ff5319a83939a84dea22` already has **18 validator errors** and **five failures among 83 unit tests**. I independently materialized the untouched home and compared it with the report/index-only proposed state: validator output is identical and the same five named tests fail. These inherited errors include invalid older agent-scoped handoff records, missing Evidence sections and a broken relative team link. They are separate from Latch PR #7, whose validator and 41 tests pass. No historical memory, test or policy was repaired or weakened during this pass. The report/index delta passes whitespace checking.

## Decision and next action

Return this review to Kisuul for delivery to Mothlight and Latch. The smallest next step is two explicit contract rows/guard-order edits, followed by exact-head source re-review and repository gates. Keep PR #7 draft and retain Latch's separate current-head acceptance gate.

No application/fixture, submitted teaching document, Latch identity/memory, shared contract or roadmap was changed. This report and its own-home index are Axiom continuity output only. No PR review/comment was posted and no teammate was launched.

## Revisit when

Mothlight specifies the two missing outcomes, the PR head/base changes, Latch issues current-head integration acceptance, or a separately authorized fixture produces behavior that challenges these source-level conclusions.

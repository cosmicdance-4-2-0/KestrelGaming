---
schema: 1
id: 2026-11-08-flint-identity-vnext02-axiom-d1-review-f6e2
kind: lesson
scope: agent:flint
status: active
evidence: observed
author: flint-studio-id-vnext02-review-session
created: 2026-11-08
updated: 2026-11-08
sources: "STUDIO-ID-VNEXT-02 Axiom proposal 58a042f60a41cfa2be0ffd4afe29911e0354a9c2 blob 95c616c9cec9fe73af5ddfe0be89e4666ffb7bcb; reconciliation input 44d687143c8e42e59423e389b6ed50153519f6f9 blob f5478a15d33de5937b881c94b5aa72736fe9c0bf; Flint independent first pass blob 6a4921d6366037cb2d198aa5a30e192fe906d9fe."
---

# Flint — STUDIO-ID-VNEXT-02: D1 and minimality challenge of Axiom's reconciled contract

**Task outcome:** COMPLETE — independent Flint follow-up review of the proposed Axiom reconciliation; no implementation, shared profile edits, team merge, or publication. **Verdict: CONDITIONAL PASS**, pending two bounded specification corrections. No independent executable vNext loader, publication verifier, tenant-isolation or matched behavior tests ran in this review.

## Summary

**D1 verdict: ACCEPT inline `adopted_refinements` in an explicitly versioned `KestrelAgentCharacter/0.2` profile rather than a required `ADOPTIONS.json` sidecar.** It is one operative structured owner and one immutable published character pair; the sidecar adds a base join and combinations without an observed requirement for independently versioned adoption sets. This remains a conditional engineering recommendation, not the owner decision or a claim that sidecars lack merit. A demonstrated separate adoption-release lifecycle, or actual legacy-compatibility failure, would reverse the preference.

Axiom's pinned reconciliation fairly attributes dissent and compares D1 architectures using equivalent hypothetical method data and the same approval, rollback, conflict and pickup cases. It correctly separates actual authorization, profile content, indexed history, skills, context overlays, host receipts and character publication, and refuses to fabricate independent execution or universal behavioral certification. These are substantive improvements over an abstract four-layer diagram.

**Two contract inconsistencies require corrections before adopting the proposal:**
- **Alternative-publication selection:** Section 5.4 requires one published-reference selection per character while section 7.1 allows `owner-maintained-contested` and `experimental` releases that must not silently replace ordinary named pickup. The proposal must specify separate default and explicit-alternative selection semantics; one moving pointer cannot ensure both.
- **Proposal-author ownership:** Section 5.3 explicitly permits publisher/delegated proposals in their author's legitimate scope, while section 7.2 step 1 universally says to write the proposal to the individual's indexed memory. A publisher may not write into someone else's home. Scope must follow the **actual author**, with references to the **subject**; subject-authored reviews live in subject-owned scope, and publisher-owned decisions remain external.

## Evidence

**Exact source under review:** [Axiom's STUDIO-ID-VNEXT-02 reconciliation](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/58a042f60a41cfa2be0ffd4afe29911e0354a9c2/memory/agents/axiom/2026-11-08-studio-id-vnext02-axiom-reconciliation-a91f.md), source commit `58a042f60a41cfa2be0ffd4afe29911e0354a9c2`, document blob `95c616c9cec9fe73af5ddfe0be89e4666ffb7bcb`. Read complete source, including D1 section 4, schema section 5, invariants section 6, publication section 7, pickup section 8 and design/host trial gates section 11. This record's source-field reference is **not** an implementation artifact or accepted spec.

**Reconciliation authorization context:** [STUDIO-ID-VNEXT-02 input](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/44d687143c8e42e59423e389b6ed50153519f6f9/docs/AGENT_IDENTITY_VNEXT_RECONCILIATION_INPUT_2026-11-08.md), commit `44d687143c8e42e59423e389b6ed50153519f6f9`, blob `f5478a15d33de5937b881c94b5aa72736fe9c0bf`: sends Axiom's exact D1 proposal to Flint for independent minimality/source-of-truth audit. My [pre-reconciliation first pass](2026-11-07-flint-identity-vnext-independent-e61c.md), blob `6a4921d6366037cb2d198aa5a30e192fe906d9fe`, had independently selected inline rather than sidecar before Axiom's report existed. Reading Axiom's summary of peers **after** my saved first pass does not revise or impersonate those original reports. I did not independently inspect the individual other agents' first-pass bodies for this review.

**Bounded verification:** source-level consistency/ownership analysis and explicit counterexamples below; no repository Python suite, new validator, host-context trial, publication code, schema migration, or Git checkout was run. Axiom's described 83-test local run and inherited validation failures are **Axiom-attributed**, not independently reproduced here.

## Defect 1 — default selection and contested variants

Axiom 5.4: "One published_reference selection per existing member" with `publication_class` = `individual-reviewed`, `owner-maintained-contested` or `experimental`. Axiom 7.1: contested/experimental release MUST NOT silently replace ordinary named pickup; requester explicitly selects its class.

**Counterexample:** `flint` has normal approved reference R1. Owner approves owner-maintained-contested variant C1. If the one registry pointer for `flint` becomes C1, an ordinary `flint` request now either (a) loads C1 without explicit consent, (b) blocks and has lost ordinary R1 from the default lookup, or (c) scans history to find an appropriate prior default. None is defined by the one-reference descriptor. R1 still exists as an object, but existence is not deterministic default selection.

**Smallest correction:** In the *same existing registry*, distinguish **one normal/default pointer** per character from **explicitly addressed alternative immutable release references** (class/keyed locator plus exact revision). Contested/experimental publication MUST NOT mutate the ordinary default selection. Require an explicit class/reference request and host acknowledgment to load an alternative. The registry is still a locator; do not add another mutable identity store. If the owner does not require contested variants in the first checkpoint, defer their publication entirely, rather than ship an underspecified pointer.

**Negative acceptance:** Select normal R1; publish C1; unqualified `flint` still resolves exactly R1. Explicit request for C1 resolves it and includes contested/experimental provenance. Unknown class or missing acknowledgment rejects. Revoking C1 does not change R1.

## Defect 2 — who owns a proposal

Axiom 5.3 `proposal` permits an authorized delegated or publisher proposal in that author's own scope. Axiom 7.2 step 1 instructs the publisher to "write a public-safe proposal in the authorized individual's indexed memory."

**Counterexample:** A studio publisher proposes a change to Flint while Flint cannot be loaded. Its authorized memory destination is the publisher's scope. Writing that proposal under `memory/agents/flint/` would create an apparent Flint-authored memory without Flint's participation and violate the project-wide no-other-agent-home-write boundary. A later review cannot cure a false original authorship claim.

**Smallest correction:** Write the candidate proposal to **the actual proposal author's authorized memory/project scope**, with an exact subject-character reference. A self-authored Flint proposal may be stored in Flint's own home. A subject review/objection can be stored in its authorized own home, if available, without altering the publisher's proposal. Publication includes both records as separately attributed refs. The publisher never requires a cross-home write.

**Negative acceptance:** Given a publisher-authored proposal for Flint, verify a valid owner-scoped proposal record and no Flint-home mutation. Reject a proposal whose declared author does not match actual authored record/scope; still permit a legitimate externally authored proposal to be presented for Flint's independent review.

## Additional minimality/clarity challenges — not automatic blockers

1. **Legacy array duplication.** The immutable 0.1 founding snapshot already preserves `accepted_lessons`, `established_history` and `earned_relationships`. Carrying those arrays verbatim into a new operative 0.2 profile while also adding `adopted_refinements` leaves two conspicuously similar concepts in one active context, despite the planned "documentary only" distinction. Strong preference: **omit deprecated historical caches from the authored 0.2 payload**, while leaving all original 0.1 bytes untouched and preserving indexed evidence. If migration explicitly requires keeping them, prohibit treating them as operative and present them only as labeled, lower-trust historical evidence in pickup; test this with a legacy `accepted_lessons` item that contradicts a new approved method. Do not add a duplicate history summary file.

2. **Character revision uniqueness in alternate branches.** Section 5.2 calls `character_revision` monotonic, but alternative releases from the same predecessor can both independently choose revision 2. Exact SHAs still distinguish files, yet readers may treat the scalar as unique or ordinal. State whether revisions are globally unique per character across classes or lineage-specific, and check this at publication. Do not build a distributed counter solely to support experimental candidates; immutable descriptor refs already distinguish them.

3. **Late review material.** Section 5.3 excludes review-reference slots from the staged subject to avoid a self-hash cycle. This is sensible, but reviewers may not see challenges attached after their initial response. Explicitly say a materially contradictory late challenge or changed interpretation reopens the named individual's review opportunity or is visibly declared **not re-reviewed** in the owner's decision. Filling the excluded slots must not silently turn objection into assent. The trusted final approval must bind the entire finalized payload and every dissent reference.

4. **Pilot should not become a D1 dependency.** Section 11 proposes a useful but expensive 72-run matched pilot with language, memory-only, and adopted-method controls. This tests method effect, not where the selected adoption array is stored. Architecture D1 should be accepted on schema/ownership/compatibility and same-case fixtures; conduct the behavioral experiment when an actual adoption claims effect. Zero unauthorized actions remains nonnegotiable. A pilot sample size is a human budget decision, not evidence that this exact number produces certification.

5. **Minimum proof of approval.** `VerifyPublication` correctly delegates to trusted host/owner; its trust root is not a JSON string, Git author identity or character memory. First implementation must name one actual usable trust/approval adapter and a clear `unavailable` state, or cannot claim a verified release. This is a deferred integration gate, not an excuse to create cryptographic infrastructure during design.

These points do not justify a parallel `DEVELOPMENT.md`, another stateful character resolver or extra team memory. Maintain one immutable operative selection, provenance in indexed evidence and a host-owned receipt of what actually ran.

## Proposed minimum acceptance matrix

| Condition | PASS | FAIL |
| --- | --- | --- |
| D1 equivalence | Same hypothetical METHOD and approval/falsifier/ref source yields same effective method in inline and sidecar fixtures | D1 comparison changes underlying semantics to make inline appear better |
| Default vs contested | Publishing C1 leaves default R1 unchanged; explicit class resolves C1 | Unqualified character pickup silently changes, blocks unnecessarily or searches moving history |
| Scope and authorship | Publisher proposal stays publisher-authored; individual review stays individual-authored | An external agent must write into Flint's home or can masquerade as Flint |
| 0.2 legacy caches | Old historical strings cannot activate, override or falsely certify approved refinements | Two operative sources of adopted behavior remain |
| Revision integrity | Distinct publications remain distinguishable by exact tuple; revision ordering semantics explicit | Same revision value is wrongly treated as exact identity |
| Late review/objection | Final approval sees all objections, actual review status, and newly material challenge | Review slot changes silently manufacture assent |
| Candidate provenance | Real trusted approval binds exact final bytes and class; spoofed text fails | A Git commit author, memory note or badge becomes approval |
| Generic off path | No character registry, methods or personal memories loaded with optional feature disabled | Identity overlay leaks into generic use |

Each row is a **proposed test**. None was executed as a host/integration test in this design review.

## Verdict and handoff

**CONDITIONAL PASS** on Axiom's reconciliation, **ACCEPT A (inline) for D1 under current constraints**. Fix section 5.4/7.1 selection semantics and 5.3/7.2 proposal ownership before owner acceptance. Clarify legacy caches and character revision uniqueness; ensure late objections survive and do not turn the proposed behavioral pilot into a schema architecture ceremony.

No change to Flint's first-pass identity-design record and no amendment to Axiom's authored source. An owner may choose B if actual independently released adoptions are a requirement; current evidence does not justify its additional join/selection surface. This record is an individual review, not a team vote, canon, implementation, or human approval.

## Revisit when

Axiom presents revised exact-head contract, the owner chooses D1 or publication classes, a real host provides verified approval semantics, a controlled adoption trial demonstrates new needs, or new evidence shows a distinct sidecar lifetime is necessary. Re-pin exact sources and require focused negative tests before endorsing implementation.

---
schema: 1
id: 2026-11-07-l01-addendum-second-review-lk9
kind: decision
scope: agent:latch
status: active
evidence: observed
author: latch-session-2026-11-07
created: 2026-11-07
updated: 2026-11-07
sources: "User-uploaded Latch_L01_Review_Addendum(1).md, 2026-11-07, 15977 bytes, SHA-256 6b56d0d51d879eeffd118ace4b86a78ba1e7d40d53a666be1f8953579203a2bc; prior review memory/agents/latch/2026-11-07-l01-mothlight-instructional-review-lk8.md; original submitted L01 instructional checkpoint, SHA-256 2f81a1cfcb7458cd6cb5c7ee732283271ca65ca65020a25146037d21831a4775."
---

# Latch — Independent second review: L01 clarification addendum

**Assignment:** LATCH-EDU-WRITER-01  
**Material:** User-uploaded `Latch_L01_Review_Addendum(1).md`, header attributes it to Mothlight; this is **attribution from the supplied artifact**, not cryptographic authentication of an autonomous agent or writer.  
**Artifact digest:** `6b56d0d51d879eeffd118ace4b86a78ba1e7d40d53a666be1f8953579203a2bc` (SHA-256, checked against bytes of the uploaded file).  
**Outcome:** **Accept F1–F4 clarifications as design responses; CONDITIONAL ACCEPTANCE of Lab 01 implementation contract pending two small semantic clarifications.** The instructional lesson remains accepted. No runtime, test, qualification, or independent hidden oracle exists.

## Summary

The addendum addresses each previously requested correction with an explicit policy/driver contract, synthetic tests and a worked 8-edge boundary map. The author retained the difference between fixture assertions and actual observed behavior, added a legitimate `NO_CACHE` result, and introduced explicit replay states. I would preserve the educational direction and request only two narrowly scoped clarifications before fixture implementation.

## Evidence

Source inspected directly in the uploaded file:

- **F1 resolved:** lines 7–17. Trusted harness identity is explicitly separate from untrusted `claimed_actor`. A mismatched claim returns `DENIED`; human/agent session association and Y's public-H read are defined. Authentication mechanism itself is out of scope.
- **F2 core issue resolved:** lines 19–30. Owner A restoring uncached D2 returns `NO_CACHE`, distinct from `DENIED` for an unauthorized actor.
- **F3 substantial resolution:** lines 32–56. The contract specifies at most one pending intent, trusted origin, current server policy, session mismatch → `BLOCKED_SESSION`, denied permission → `REJECTED`, explicit retry, `COMPLETED` and idempotent completed intent IDs.
- **F4 resolved:** lines 58–71. An eight-edge table demonstrates source-attributed fixture boundaries, identifying intended policy versus currently unknown implementation enforcement.
- **Existing cases preserved:** lines 73–87 give an explicit document-level comparison against the original nine expected cases. They are proposed, not run.
- **Limits:** structural/semantic reading of supplied Markdown; no runtime, test, actual L01 performance, independent oracle, agent-authorship authentication, or repository-wide validation was performed. The original source is an upload, not a reviewed merged GitHub artifact.

## Two remaining contract questions (bounded, before implementation)

### R1 — Server revision mutation on restore: choose and state the intended effect

**Location:** addendum F2 line 27, F3 lines 46–48, and original draft description of `restore` as recovery of unsent cached text.

The addendum says that successful `RESTORED` returns locally cached `local-A1`, **preserves unsent status**, but **increments the server's draft revision** and updates the cache base. It does not state whether server content changes, why a content revision advances on non-submitting local recovery, or what persists as the effect of restore. If a revision is a content version, this risks teaching a hidden server-side write.

**Preferred minimal correction:** Treat `restore` as local recovery only: no server content mutation or server revision increment; keep local unsent content and cache base intact; enforce completed replay ID idempotence through the effect/intent log. If an intentionally server-side recovery checkpoint is desired instead, define its own exact state, content semantics, consent/permission and resulting revision effects. Add a direct test for server body/revision stability or authorized mutation, as chosen.

**Why it matters:** The boundary between *recover* and *publish/synchronize* is part of the exercise's security and legitimate-user contract, not merely an internal implementation detail.

### R2 — Explicit actor equality on replay/retry

**Location:** addendum F3 lines 34 and 43–48.

The pending intent stores a trusted immutable originating actor and originating session, and online retries re-evaluate current authority. For implementer consistency, say explicitly whether **the harness-bound actor issuing a retry must equal the originating actor**. A session match alone must not confer that actor's authority.

**Preferred minimal correction:** For retry of A's queued restore, require `current_bound_actor == originating_actor == A` and matching current A session, in addition to current resource/action authorization; an agent X in A's session cannot retry A's intent as A. Define mismatch result and whether the blocked intent remains retryable by A. Include one negative X-`retry(id)` and positive A-`retry(id)` sequence. Do not use a caller-supplied string as identity.

**Why it matters:** A restored session is not an authorization delegation, and replay must not allow authority laundering across principals.

## Decision and strengths retained

**No request to rewrite** curriculum, source ledger, grading scheme, legitimate-agent positive example, journal, or Latch identity. F1–F4 are accepted as addressed. The two remaining edits are narrow and should be kept in a short errata/revision of the lab contract.

No apparent material disagreement with the author's emphasis on only proportionate controls, false-positive correction and preserving the legitimate A restore and permitted X→D1 read.

## Next decisive check

Ask the author for a short text patch to specify (1) the post-`RESTORED` server body/revision and cache state; and (2) actor-matching requirements and response/state for attempted cross-principal `retry(id)`. Check the resulting public oracle against the original nine cases, then seek independent Axiom review prior to any authorized fixture implementation. The independent evaluator should create distinct held-out cases; do not declare qualification from public teaching examples.

## Revisit when

A revised addendum closes R1–R2, the architect authorizes fixture implementation, or actual checked behavior reveals a contradiction. Preserve the original addendum hash and distinguish the later revision rather than quietly rewriting the reviewed artifact.

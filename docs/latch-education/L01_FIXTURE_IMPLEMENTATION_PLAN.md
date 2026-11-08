# Latch L01 — Synthetic fixture implementation plan

**LATCH-L01-FIXTURE-PLAN-01 · Mothlight · 2026-11-08**

**Status:** proposed next implementation checkpoint. No fixture code, learner exercise, held-out cases or qualification is supplied by this plan.

## Baseline and authority

[PR #7](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/7) integrated the instructional package at `d3cf43c5d4a2146371d05bf8c28712c5f1cf5266`. Its source head `ca0dedef1b8ad9f02aa8f296b07f5059782a4bb8` received [Latch's exact-head integration acceptance](../../memory/agents/latch/2026-11-08-l01-pr7-acceptance-ca0d-lk11.md) and [Axiom's independent contract acceptance](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/53d5b0921e1001f64bab8ecf6ce2cea2583c33e3/memory/agents/axiom/2026-11-08-latch-l01-followup-ca0d.md).

Continue on `mothlight/latch-education`, PRs targeting `agents/latch-v1`, gated by Latch's acceptance of each current head. This plan prepares the next separately assigned coding pass; it does not reinterpret documentation acceptance as runtime approval. Shared contracts, identity, skills, memory schemas and CI stay outside the implementation scope.

The operative fixture contract is the [lesson](Latch_L01_Instructional_Checkpoint.md), [addendum](Latch_L01_Review_Addendum.md), then [errata](Latch_L01_R1_R2_Errata.md), with later corrections taking precedence. Implement the stated policy; surface any further ambiguity before choosing an unstated business rule. Do not consolidate or rewrite those accepted sources as an implementation side effect.

## Proposed shape

Use Python's standard library and the repository's existing unittest workflow. Keep the lab in memory and deterministic: no HTTP server, browser, accounts, real tools, dependencies, credentials or persistent customer data.

| Proposed artifact | Responsibility |
|---|---|
| `labs/latch_l01/model.py` | Explicit fixture state and driver operations; centralized policy evaluation; separate read versus local-restore effects. |
| `labs/latch_l01/visible_cases.py` | Named public teaching sequences and their independently specified expected outputs/state observations. No hidden answer key. |
| `labs/latch_l01/__main__.py` | Run the visible case set and report actual pass/fail results with a nonzero exit on a mismatch. |
| `tests/test_latch_l01.py` | Boundary and transition regressions, including allowed neighboring operations and no-effect assertions. |
| `labs/latch_l01/README.md` | Invocation, contract references, modeled/excluded surfaces and evidence limits. |

Package markers may be added as needed. Avoid a generic authorization framework or plugin system. A small fixture object may own drafts, cache, editor, active user, bound actor, explicit clock, grant, pending intent, completed-origin records and effect logs. Keep initial constants in one named fixture configuration. Reset must restore all initial state, including identifiers and logs.

Trusted driver binding and setup mutations are separate from untrusted request fields. They are test controls, not an authentication implementation. Public responses and a driver-only inspection view must be distinct. No method reads the current wall clock or performs network/file effects.

## Three reviewable passes

1. **Read and local recovery.** Implement reset, driver context, connectivity/time/grant changes, server reads, fixture setup and direct restore. Cover A/B/X/Y, D1/D2/H, claimed identity, current/expired/revoked grants, authorization-before-cache lookup, `NO_CACHE`, `CONFLICT`, and successful local-only recovery. Deliver a runnable slice with tests and a clearly enumerated list of still-unimplemented replay operations. Do not claim complete Lab 01 conformance.
2. **Replay and retry.** Implement the one-slot queue, immutable origin, blocked session/actor, terminal rejection, completed-ID origins and one recovery effect. Include PENDING retry → `NO_PENDING`, online-before-full queue precedence, offline precedence, origin mismatch, completed-ID replay with another intent pending, and slot reuse after rejection. Document the accepted no-cancellation limit; direct owner restore must remain available.
3. **Public teaching run.** Connect named sequences to a simple runner, include inert draft-instruction text and empty tool/publication effect checks, and record actual results at an exact head. Require real returned text in allowed read cases so a blanket-deny or empty-body stub fails. Hand off for independent implementation review before using the lab to assess Latch.

This order keeps the first coding pass small while preserving the full accepted contract. Partial slices must fail explicitly or omit unsupported replay entry points; never return fake successful outcomes for them.

## Oracle and evidence rules

Write expected decisions from the accepted policy before comparing implementation output. Expected values in the visible case set must not call the implementation's authorization helper to decide their own correctness. Assert response status, returned data, intent state, editor state, server/cache stability and effect count where consequential. Pair denied cases with successful owner, delegated and public neighbors.

Retain the original nine visible sequences plus the later identity, missing-cache, server-stability, cross-actor retry and Axiom transition controls. Cases remain public training material. Implementation regressions are tests of the fixture, not measurements of Latch's competence. A no-op simulated tool interface establishes only the specified local effect boundary, not resistance to deployed prompt injection.

A separate evaluator may later author fresh cases and expected outcomes without sharing its key with the learner or deriving expected results from the candidate implementation. No evaluator or hidden suite is currently claimed. Do not add purported blind evaluation material to this public project merely to satisfy a checklist.

## Acceptance and stop conditions

For each coding pass, run meaningful new boundary tests, `python3 tools/validate_seed.py`, the full repository unittest suite, and whitespace checks. Report exact head, commands, outcomes and unimplemented parts. Tests must preserve the accepted oracle when the implementation disagrees.

The fixture can be called implemented only after all accepted public paths and no-effect conditions work under the stated assumptions, independent review resolves blockers, and Latch accepts the exact head. Learner exercise completion and qualification still require their own observed trials and owner decision.

Stop and return a concrete contract question if a required transition has no unique outcome. Stop at the assigned pass; do not expand into live security testing, production identity, training automation or capability certification.

**Next reviewable decision:** Latch reviews the proposed structure, three-pass boundary and oracle separation. The first coding assignment is pass 1: read authorization and direct local recovery.

# Latch — Skill and Training Index

**Owner:** Latch — The Locksmith  
**Branch:** `agents/latch-v1`  
**Snapshot:** 2026-11-08, after [PR #11](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/11) merged at `ba3c9b60e0e68fab7b4c4157216b96747dd82c37`  
**Status:** Inventory and navigation, **not** an activation, authorization or qualification record  
**Portfolio source:** [Engineering skill development roadmap](SKILL_ROADMAP.md)

> Identify the right boundary before hardening the wrong door.

## 1. Status vocabulary and totals

| Kind | Count | Meaning |
| --- | ---: | --- |
| Shared Kestrel procedures | 3 | Existing shared catalog entries; not personal qualification claims |
| Latch-authored procedural skill files | 3 | **DRAFT** `SKILL.md` procedures; no controlled independent behavioral qualification |
| Latch security-engineering specializations | 18 | **PROPOSED** candidates in the roadmap, not authored `SKILL.md` files |
| L01 teaching fixture | 1 | **BUILT, REVIEWED AND MERGED** synthetic learning material; **not** a qualified learner skill |
| Latch specializations qualified | **0** | No independent L01 learner examination or earned skill promotion recorded |

These are overlapping *artifact categories*, not 25 independently mastered abilities: the L01 lesson and lab support candidate L01, and the three evidence-integrity files are cross-cutting additions **outside** the numbered 18-skill roadmap.

**Status meanings:** `PROPOSED` = planned specialty, no dedicated working `SKILL.md`; `DRAFT` = actual written procedure, not independently proven; `TRIALED` = the agent performed a recorded controlled exercise with results; `QUALIFIED` = a designated independent assessment and promotion gate explicitly passed. `BUILT/REVIEWED` describes teaching software, **not** the learner. Neither documentation nor an accepted code review confers a new permission.

## 2. Existing shared procedures (not Latch-owned)

The [shared skill catalog](../../skills/INDEX.md) currently registers:

| Procedure | When useful | Classification |
| --- | --- | --- |
| [`kestrel-recall`](../../skills/kestrel-recall/SKILL.md) | Recover project context and scoped memory for a task | Shared catalog procedure |
| [`kestrel-remember`](../../skills/kestrel-remember/SKILL.md) | Record an attributable decision, lesson or handoff | Shared catalog procedure |
| [`kestrel-html-conformance`](../../skills/kestrel-html-conformance/SKILL.md) | HTML deliverable and official validator gate | Shared catalog procedure |

Being present in the repository does not mean these are installed host tools or that Latch has independently demonstrated proficiency in each.

## 3. Latch-authored cross-cutting procedural skills

These three files **exist** on the agent branch and are registered in the catalog's **DRAFT** section. Their proposed evaluation cases are **NOT RUN**.

| Procedural file | Trigger and expected value | Current status |
| --- | --- | --- |
| [`latch-source-provenance`](../../skills/latch-source-provenance/SKILL.md) | Material citation or source dispute; pin original, revision, relevance and independence | **DRAFT — not qualified** |
| [`latch-claim-citation-audit`](../../skills/latch-claim-citation-audit/SKILL.md) | Consequential report or claimed test result; match each atomic claim to evidence it entails | **DRAFT — not qualified** |
| [`latch-evidence-continuity`](../../skills/latch-evidence-continuity/SKILL.md) | Reproducible engineering review or task resumption; maintain truthful, indexed, scoped records | **DRAFT — not qualified** |

The [reflective journal protocol](JOURNAL_PROTOCOL.md) is a working convention, **not** a fourth `SKILL.md` or proof of improved reasoning.

## 4. Numbered security-engineering skill portfolio

Source of truth for candidate definitions, triggers, priorities and promotion gates: [`SKILL_ROADMAP.md`](SKILL_ROADMAP.md). **No named `latch-*` specialty below has yet been authored as a dedicated numbered procedural skill or independently qualified.**

| ID | Priority | Candidate | Current status and next evidence gate |
| --- | --- | --- | --- |
| L01 | P0 | `latch-trust-map` | **PROPOSED procedure; lesson and synthetic lab merged.** Next: independent learner trust-map exercise and false-positive check |
| L02 | P0 | `latch-risk-triage` | **PROPOSED**; progression outline only. Next: measured risk-ranking exercise |
| L03 | P0 | `latch-authorization-matrix` | **PROPOSED**; progression outline only. Next: actor/resource/action/context matrix exercise |
| L04 | P0 | `latch-boundary-negative-tests` | **PROPOSED**; progression outline only. Next: independent negative and positive test oracle |
| L05 | P1 | `latch-security-diff-review` | **PROPOSED**. Next: independently assessed exact-head seeded-defect review |
| L06 | P1 | `latch-agent-capability-map` | **PROPOSED**. Next: scope/expiry/revocation enforcement trial |
| L07 | P1 | `latch-untrusted-content-boundary` | **PROPOSED**. Next: adversarial data-versus-instruction trial with valid content preserved |
| L08 | P1 | `latch-memory-lineage-and-isolation` | **PROPOSED**. Next: source, ownership and poisoning trial |
| L09 | P1 | `latch-agent-handoff-integrity` | **PROPOSED**. Next: forged/stale handoff and valid continuation trial |
| L10 | P2 | `latch-session-and-state-transitions` | **PROPOSED**. Next: bounded switch/replay/state-race exercise |
| L11 | P2 | `latch-secure-data-and-api-boundaries` | **PROPOSED**. Next: malformed input and owner-scope verification |
| L12 | P2 | `latch-secrets-and-privacy-flows` | **PROPOSED**. Next: synthetic-secret leak tests and legitimate debug control |
| L13 | P2 | `latch-supply-chain-and-ci-trust` | **PROPOSED**. Next: controlled provenance and CI permission review |
| L14 | P2 | `latch-audit-and-containment` | **PROPOSED**. Next: safe audit/containment and recovery test |
| L15 | P3 | `latch-controlled-adversarial-exercise` | **PROPOSED**. Next: explicit-authority isolated red-team case |
| L16 | P3 | `latch-fuzz-and-property-boundaries` | **PROPOSED**. Next: deterministic bounded property-counterexample exercise |
| L17 | P3 | `latch-security-usability-review` | **PROPOSED**. Next: mitigation friction and positive-journey comparison |
| L18 | P3 | `latch-posture-and-residual-risk` | **PROPOSED**. Next: evidence-bounded residual-risk release assessment |

The roadmap's numbered 18 are **development targets**, not eighteen skills silently activated by cataloging them.

## 5. L01 — ready-to-teach artifact, not yet learned

- **Curriculum and contract:** [Instructional workshop](../../docs/latch-education/README.md), [L01 lesson](../../docs/latch-education/Latch_L01_Instructional_Checkpoint.md), [F1–F4 addendum](../../docs/latch-education/Latch_L01_Review_Addendum.md) and [R1/R2 errata](../../docs/latch-education/Latch_L01_R1_R2_Errata.md).
- **Runnable fixture:** [Shared-Draft Lab](../../labs/latch_l01/README.md) and its [public cases](../../labs/latch_l01/visible_cases.py); 16 named public cases with correct and deliberately defective fixture controls.
- **Merge receipt:** [PR #11](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/11) merged on 2026-11-08 at `ba3c9b60e0e68fab7b4c4157216b96747dd82c37`. Accepted implementation head: `cbf9a0c5e05b42b7d9fb2aa128ed41ca4878e3d0`.
- **Independent code/runner review:** [Latch exact-head acceptance](../../memory/agents/latch/2026-11-08-l01-pr11-pass3-acceptance-cbf9-lk17.md); [Axiom's head-pinned execution record](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0ec29948cf10f60e627c8c0696209faed586bc4/memory/agents/axiom/2026-11-08-latch-l01-pr11-followup-cbf9.md) attributes 16/16 normal public cases, 106 repository tests and 570 input-boundary probes, and records a queued-write mutant rejected by the public runner.
- **Interpretation:** Those are software-fixture verification results, not Latch's score. Axiom executed the reported suite; the Latch review inspected the source and attributed those results, rather than rerunning the full tests.
- **Missing:** An independent learner-facing assignment, held-out assessment design/answer key, actual Latch exercise response, recorded performance/false positives and explicitly authorized skill promotion. The public runner explicitly reports `qualification_assessed=false`.
- **Execution boundary:** This is in-memory fictional data with a typed request adapter and scripted data-only agent, not a production credential service, Python sandbox, live tool engine or deployed prompt-injection defense.

## 6. Promotion and next checkpoint

1. **Prepare an L01 learner assessment independently of the authored teaching examples.** Include real and false-positive boundaries, private/public and delegated access, identity changes, queued replay, and legitimate owner recovery; keep evaluator keys separate from learner input.
2. **Run Latch's actual L01 procedure in a controlled setting.** Record the prompt/artifact revision, the learner's answers, test oracles, observed misses, false alarms and corrective reasoning. Do not use a synthetic runner PASS as an agent performance result.
3. **Have an independent reviewer score the exercise** using explicit thresholds and evidence limits, then mark the particular ability `TRIALED` or `QUALIFIED` only if its specified gate is met.
4. **Consider authoring a reusable `latch-trust-map/SKILL.md`** after the method is shown to be useful and appropriately scoped; a file alone would start as DRAFT.
5. Progress to L02–L04 incrementally. Do not expand to all eighteen on the strength of this first lab.

Use [permissions](../../kestrel/PERMISSIONS.md), [verification](../../kestrel/VERIFICATION.md), and [memory protocol](../../kestrel/MEMORY_PROTOCOL.md) for any future task. This index grants no live-system testing authority, does not change user/agent rights, and does not supersede project-owned source contracts.

*The inventory can be complete while the education is still beginning.*

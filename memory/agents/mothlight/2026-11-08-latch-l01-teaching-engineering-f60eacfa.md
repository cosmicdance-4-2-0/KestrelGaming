---
schema: 1
id: 2026-11-08-mothlight-latch-l01-teaching-engineering-f60eacfa
kind: lesson
scope: agent:mothlight
status: active
evidence: observed
author: mothlight
created: 2026-11-08
updated: 2026-11-08
sources: "LATCH-EDU-WRITER-01 in the Mothlight conversation; KestrelGaming PRs 7-11; accepted PR11 head cbf9a0c5e05b42b7d9fb2aa128ed41ca4878e3d0; merge ba3c9b60e0e68fab7b4c4157216b96747dd82c37; Axiom followup f0ec29948cf10f60e627c8c0696209faed586bc4; Latch acceptance record at 593d3f8fb60670260e1c6f08ca6a78b52cce4b2e; Mothlight's local full-suite, runner, structural and tree checks; Kisuul requested this agent update while dispatching Latch to test."
---

# L01 — teaching judgment, engineering the evidence

## Summary

**Completed, attributed Mothlight work:** wrote Latch's first security-engineering
instructional checkpoint and implemented its deterministic in-memory trust-boundary
fixture in three bounded passes. Latch accepted integration; Axiom independently
reviewed the implementation and required a correction to the public runner's checks.
The work is integrated in `agents/latch-v1` through PR #11.

The instructional aim was to reward finding real weaknesses, correcting false
assumptions and recognizing adequate protection. A useful security exercise must
preserve legitimate use as well as reject unauthorized operations. Blanket denial
and an inflated finding count are poor success criteria.

**Current boundary:** Kisuul states that Latch is being dispatched to test the new
skills. No learner result was supplied in this conversation. Do not convert fixture
acceptance, a public runner pass or this memory entry into a claim that Latch learned
L01 or qualified any part of the eighteen-skill roadmap.

### Methods exercised and lessons worth retaining

- **Translate the experience into an explicit state contract.** The recovery story
  needed exact effects and authority: R1 restoration changes only the local editor,
  preserving complete server and cache records; R2 replay and retry require the
  originating actor and session as well as current authority. These are distinct
  questions. Ambiguous recovery semantics caused review work and needed written
  correction before implementation.
- **Challenge the teaching oracle itself.** Axiom found that an intentionally
  faulty queued-only server-writing fixture could pass all sixteen public cases.
  An older unit regression already caught it. The gap was in what the public runner
  observed, not evidence of a server-writing exploit in the shipped core.
- **Measure required non-effects at the action boundary.** The correction captures
  detached pre-action state and compares complete server/cache records after each
  successful queued recovery. It covers automatic replay and explicit retry;
  server body/revision and cache text/base mutations are negative controls. Keep
  valid owner, delegate and public neighbors so rejecting everything cannot pass.
- **Repair narrowly and preserve the failed observation.** The correction changed
  only the visible cases, runner tests and lab README. Core, adapter, CLI and policy
  stayed unchanged. The old false green remains attributable to its old revision;
  it was not rewritten into a historical success.
- **Review and integration are separate evidence.** Acceptance applied to an exact
  source head. The latest target memory changes were combined locally, checked,
  and compared with the actual merged tree. Peer tests remain peer observations;
  Mothlight's reproduced results are recorded separately below.

These methods were exercised on this project. General transfer is an inference,
not a certified specialty or a newly installed reusable skill. No trait weights,
permissions, identity schema, adoption manifest or proposed M01–M05 trial verdicts
are changed by this record. The separately deferred
[experience-engineering goal](2026-11-07-experience-engineering-goal-a63d91c2.md)
remains deferred; L01 work does not silently start that workshop.

## Evidence

### Source and integration receipt

| Milestone | Integrated evidence |
| --- | --- |
| Instructional package, clarification and R1/R2 corrections | [PR #7](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/7), merge `d3cf43c5d4a2146371d05bf8c28712c5f1cf5266` |
| Three-pass implementation plan | [PR #8](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/8), merge `35e03010b505ee59002e28c190bf668a33f0256b` |
| Trusted fixture context, reads and local restoration | [PR #9](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/9), merge `c04331d4ad39ac4c95a1e42d9cd303964715b56a` |
| Immutable-origin queue, replay, explicit retry and idempotence | [PR #10](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/10), merge `ca49d6eabd6e6f17bfd139efd0d3804a16d351c8` |
| Validated request adapter, scripted agent and public runner, including AX-L01-P3-01 correction | [PR #11](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/11), merge `ba3c9b60e0e68fab7b4c4157216b96747dd82c37` |

Canonical project sources stay on the project branch; they are not copied into
Mothlight's home. See the pinned
[instructional package](https://github.com/cosmicdance-4-2-0/KestrelGaming/tree/ba3c9b60e0e68fab7b4c4157216b96747dd82c37/docs/latch-education),
[implementation plan](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/ba3c9b60e0e68fab7b4c4157216b96747dd82c37/docs/latch-education/L01_FIXTURE_IMPLEMENTATION_PLAN.md)
and [fixture](https://github.com/cosmicdance-4-2-0/KestrelGaming/tree/ba3c9b60e0e68fab7b4c4157216b96747dd82c37/labs/latch_l01).
Some accepted source documents still describe then-pending reviews. The subsequent
review and merge receipts establish completion; those historical markers do not
supersede the receipts.

**Mothlight's executed observations during implementation and integration:**

| Check or reproduction | Observed result and limit |
| --- | --- |
| Original queued-only write fault at `f0f6cbbddcec52652233f9bca847a51dc5316b87` | False green: 16/16 public cases; text/JSON exit 0 |
| Same fault after correction at `cbf9a0c5e05b42b7d9fb2aa128ed41ca4878e3d0` | C05/C12/C13/C14 fail named R1 checks; 12 pass/4 fail; text/JSON exit 1; JSON `successful=false` |
| Combined accepted head plus latest target base `593d3f8fb60670260e1c6f08ca6a78b52cce4b2e`: `python3 -m unittest discover -s tests -q` | 106 tests pass; expected checker-error diagnostics are exercised test fixtures, not a failed suite |
| Combined state: `python3 -m labs.latch_l01 --json` | 16/16 public cases; `successful=true`, `qualification_assessed=false` |
| Combined state: `python3 tools/validate_seed.py` and complete PR `git diff --check` | Pass; structural and whitespace checks do not establish educational effectiveness |
| GitHub merge and retained project working branch | Both `agents/latch-v1` and `mothlight/latch-education` verified at `ba3c9b60e0e68fab7b4c4157216b96747dd82c37`; merged tree `468eb078ab9c79e5afdee179fcc33b03533ee5fc` exactly matches locally tested combined tree |

**Peer evidence, separately attributed:**
[Axiom's follow-up](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/f0ec29948cf10f60e627c8c0696209faed586bc4/memory/agents/axiom/2026-11-08-latch-l01-pr11-followup-cbf9.md)
accepts the exact `cbf9a0c` head and reports independently executed 106 tests,
sixteen public cases, 570 adapter probes and fault controls.
[Latch's final record](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/593d3f8fb60670260e1c6f08ca6a78b52cce4b2e/memory/agents/latch/2026-11-08-l01-pr11-pass3-acceptance-cbf9-lk17.md)
accepts that same head and distinguishes Latch's source inspection from Axiom's
executed results. GitHub review `5820130848` is a COMMENT with an explicit verdict;
the shared-account workflow did not provide a formal APPROVE or authenticated
agent identity. Neither acceptance is a learner assessment.

**Environment and provenance limits:** the fixture is deterministic, synthetic and
in memory. There is no live tool/publication engine, deployed authentication,
Python sandbox or unrestricted prompt-injection defense. Local repository trees
were materialized through the GitHub connector and verified against published Git
tree hashes; local snapshot commits are not the remote history and must not be
pushed as substitutes. These checks establish bounded implementation behavior,
not production security, instructional efficacy or general Mothlight competence.

**Task outcome:** the original writing and three-pass fixture assignment is
COMPLETE. Any new learner assessment is a distinct assignment; no hidden trials
were added by Mothlight. No message was sent to Latch as part of this memory update.

### Own-home update verification

This continuity update is based on Mothlight home `ddefa3ea044dc3a2aa0923723f3f8660583568e2`,
tree `797afc6a50655027eb713f29633bb46c3d89d95b`. Its complete source tree was
materialized and matched before editing. `python3 tools/validate_seed.py` reports
the same four errors on that untouched baseline and this updated tree: the four
existing `memory/projects/kisuul/hollowlumen/handoffs/` records lack explicit task
outcomes. The full `python3 -m unittest discover -s tests -v` executes 82 tests and
has the same six failures on both trees, each arising from those inherited
validation errors. This is not a green home-branch gate. No unrelated handoff,
validator, test or structured personality file was changed to conceal the failures.
All seven focused Mothlight profile tests pass, and the complete update passes
`git diff --cached --check`. These are structural checks, not personality trials.

## Revisit when

Latch returns actual learner-test evidence; a new fixture counterexample appears;
the source or trust contract changes; Kisuul assigns a further instructional slice;
or repeated independent use supports extracting a reusable procedure. Record
learner success, error correction, false positives and adequate-protection judgments
with their task/revision and attribution. Preserve a negative result as readily as
a positive one. Update only Mothlight's own conclusions here; Latch owns Latch's
identity, self-assessment and individual memory.

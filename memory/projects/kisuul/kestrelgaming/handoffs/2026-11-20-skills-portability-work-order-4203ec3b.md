---
schema: 1
id: 2026-11-20-skills-portability-work-order-4203ec3b
kind: handoff
scope: project:kisuul/kestrelgaming
status: active
evidence: user-stated
author: generic-kestrel-session-2026-11-20
created: 2026-11-20
updated: 2026-11-20
sources: "Owner's 2026-11-20 requests: skills must work in any agent environment (Claude Code, Codex, Grok and others), then prepare a Kestrel project from the audit. Findings: the 2026-11-20 portability audit at cosmicdance-4-2-0/KestrelGaming 3aef6e5ba9a6c79b28d302f88f2be2fdb12bcb5a."
---

# Work order — cross-host skill portability

## Summary

**Goal and acceptance criteria:** Every Kestrel skill works in each supported agent host by a
documented route, and that is shown by evidence rather than assertion. Acceptance criteria are listed below.

**Task outcome:** IN PROGRESS

Preparation is complete. **No remediation stage has started.** Stage 0 is next.

**Mission:** Turn "works in any agent environment" (user-stated) into tested, tiered guarantees.
Fix the format and validator gaps, declare each skill's real dependencies, document the install
route for each host, and trial the hosts. Evidence base: [the portability audit](../2026-11-20-skills-portability-audit-4203ec3b.md).

**Authorized scope and boundaries (historical; recheck on resume):** This work order was prepared
by generic Kestrel. It does not by itself authorize execution of any stage, merging, or changes outside this repository.
The session that prepared it may push only to `claude/nifty-ritchie-t1cur9`.

**Target repository, branch, and commit:** `cosmicdance-4-2-0/KestrelGaming`, baseline `main` at
`3aef6e5ba9a6c79b28d302f88f2be2fdb12bcb5a`. Refresh it before starting work, because the baseline may have moved.

**Memory revision loaded:** Same commit. Loaded: root and shared indexes, this project's index,
and the 2026-11-19 shared review checkpoint.

### Portability tiers (the target vocabulary)

| Tier | Meaning | Status at baseline |
| --- | --- | --- |
| T0 Readable | Any agent with file access follows AGENTS.md → skill catalog → `SKILL.md` inside a full checkout | Works (inferred from structure; no host trial) |
| T1 Spec-valid | Every `SKILL.md` passes the Agent Skills spec and the official `skills-ref` validator | One known violation; official validator not run |
| T2 Discoverable | A documented install makes each supported host list the skill, with its links resolving | Not available |
| T3 Standalone | The skill folder alone carries its core procedure; anything else it needs is declared in `compatibility` | Not available; repository links throughout |

Target: **all skills at T1 and T2** for every supported host. **T3 is a per-skill decision**
(decision D2 below), not a blanket requirement.

### Acceptance criteria

- [ ] AC1. On the work branch, `tools/validate_seed.py`, the full unittest suite and `git diff --check` pass. CI is confirmed green on the pushed commit.
- [ ] AC2. All 35 skills pass `skills-ref validate`, or appear on an explicit, justified exception list. The run is recorded with its exact command and version.
- [ ] AC3. The validator enforces the spec's hard limits (name rules, description 1–1,024, `compatibility` 1–500, allowed fields). Each rule has a positive and a negative regression test.
- [ ] AC4. Every link leaving a skill's own folder is classified as required or optional. Required repository dependencies are declared in `compatibility`.
- [ ] AC5. No skill description names a specific repository owner.
- [ ] AC6. Install routes for each host are documented. Each route is labeled **verified** (with a trial reference) or **unverified**.
- [ ] AC7. At least Claude Code and Codex are trial-verified. The trial covers listing, invocation by description match, invocation by name, and resolving one link outside the skill folder. Results are recorded as observed.
- [ ] AC8. The audit's listing-budget hypothesis (finding 8) is either tested or explicitly carried forward as unverified.

### In scope

The validator's skill rules and their tests; first-party `SKILL.md` frontmatter and link wording;
`agents/openai.yaml`; [integration](../../../../../docs/INTEGRATION.md),
[contributing](../../../../../CONTRIBUTING.md) and [the skill catalog](../../../../../skills/INDEX.md);
optional discovery shims (D5); host trials in disposable workspaces; and records in this project scope.

### Out of scope unless separately authorized

- Rewriting what a skill teaches.
- Editing vendored PixiJS text without decision D4.
- Changing [the operating contract](../../../../../KESTREL.md).
- Building a plugin or adapter runtime.
- Publishing to skill marketplaces.
- Merging to `main`.
- Changing agent home branches (`agents/*-v1`). They hold skill snapshots, so this work will not reach them until there is a separate, deliberate branch update.
- Adding third-party dependencies to CI.

## Evidence

**Confirmed observations with sources:** See [the audit record](../2026-11-20-skills-portability-audit-4203ec3b.md).
In brief, the format conforms, with one vendored description over the limit. All 9 first-party skills link outside their own folder.
There are no host discovery folders. The validator and 6 of 84 tests fail at baseline because of a shared-scope handoff record.

**Hypotheses and assumptions:**
- H1 (untested): a host following a symlink to `skills/<name>` resolves `../../` links against the real folder.
- H2 (untested): 18,301 characters of descriptions may exceed Codex's documented 8,000-character fallback listing cap.
- A1: "any environment" is taken to mean hosts that implement Agent Skills, plus plain file-reading agents (T0).
  Hosts without filesystem access are excluded unless the owner names them.

### Decisions needed from the owner

| ID | Question | Options | Recommendation |
| --- | --- | --- | --- |
| D1 | How should the shared-scope handoff that breaks `main` be fixed? | (a) Allow shared handoffs, which changes the memory protocol; (b) reclassify the record as `kind: decision` or `fact`, with the text unchanged; (c) move it to a project scope, which its own privacy note argues against | **Decided 2026-11-20 by the owner: (b), `kind: decision`, applied on `claude/nifty-ritchie-t1cur9` as part of DOC-STD-001 PR A.** Stage 0 exits when CI is confirmed green |
| D2 | What portability model per skill? | Checkout-required, standalone, or a hybrid | Recall and remember: **checkout-required**, declared in `compatibility`, located via `KESTREL_HOME`. Math and HTML: **hybrid**, with a self-sufficient core procedure and repository links as optional context. PixiJS: unchanged, installed as a set |
| D3 | Which owner is canonical? | `Kisuul` or `cosmicdance-4-2-0`, for skill wording and memory scope | Owner-neutral skill wording regardless; owner decides the memory scope |
| D4 | What to do about the over-limit PixiJS description? | Report upstream; documented local patch plus manifest update; accepted exception that excludes strict upload paths | Report upstream, and keep a documented exception until upstream fixes it |
| D5 | Add discovery shims in this repository? | Committed `.claude/skills` and `.agents/skills` symlinks; user-level install docs only; both | Docs first. Shims would conflict with the validator's symlink rejection, Windows `core.symlinks`, and a broken cloud-session use case |
| D6 | Which hosts are supported? | Claude Code (local and cloud), Codex, Grok Build, claude.ai upload, other Agent Skills hosts | Claude Code and Codex verified; Grok Build trial-or-unverified; claude.ai upload only for T3 skills |

**Decisions and rationale:** The project is staged so that format and validator fixes (cheap and checkable)
land before host trials (expensive, environment-dependent). This way trials test a stable target.

### Staged plan

**Stage 0: restore green main.** Apply D1 on a work branch. Exit: AC1 locally, then CI is confirmed green after push.

**Stage 1: spec gate.** Extend the validator. Allow `compatibility` for first-party skills.
Allow `metadata` only if the flat parser is deliberately extended. Check description ≤1,024 and `compatibility` ≤500.
Report bodies over 500 lines as advisory. Keep an explicit vendored-exception list with reasons, and add tests.
Run `skills-ref validate` on every skill wherever it is permitted. It needs a permission grant: it was blocked in the preparing session.
Exit: AC2 and AC3.

**Stage 2: dependencies and descriptions.** Apply D2 and D3. Classify every out-of-folder link.
Add `compatibility` where a skill needs the checkout. Make descriptions owner-neutral and add "use when" wording to the math skills.
Optionally add a validator rule that out-of-folder links must be allowlisted. Exit: AC4 and AC5.

**Stage 3: install routes.** Per host in D6, document the install folder, symlink or copy method, reload behavior, and known limits.
For example, Claude Code cloud sessions do not read `~/.claude/skills`, and claude.ai uploads reject non-spec keys.
Keep a T0 fallback for any agent. Exit: AC6, with every route marked unverified until Stage 4.

**Stage 4: host trials.** Use a disposable workspace for each host. Install by the documented route, then record:
the listing, a match on a natural-language trigger, a by-name invocation, H1 link resolution, and H2 listing behavior.
Use the [behavioral scenarios](../../../../../kestrel/evals/SCENARIOS.md) where they fit.
Record the outcome in a new project record. Exit: AC7 and AC8.

**Stage 5: vendor decision.** Carry out D4 and update the [PixiJS provenance](../../../../../third_party/pixijs-skills/UPSTREAM.md) if needed.

**Stage 6: close.** Update the guidance in CONTRIBUTING's "Skill changes" section and the catalog.
Set this handoff to COMPLETE or PARTIAL with evidence, and supersede or refresh the audit record.

**Changed files and uncommitted state to preserve:** Preparation added this handoff, the audit record,
and two rows in [the project index](../INDEX.md). No skill, validator or test file was changed.

| Command or check actually performed | Observed result | Environment / limits |
| --- | --- | --- |
| `python3 tools/validate_seed.py` at baseline | Exit 1, one pre-existing shared-handoff error | Cloud container, CPython 3 |
| `python3 -m unittest discover -s tests` at baseline | 84 run, 6 failures, the same cause | Same |
| Validator after adding these records | See this file's Git history and the preparing session's report; it is not claimed in advance here | Same |

**Persistence:** Prepared on branch `claude/nifty-ritchie-t1cur9`. It is not integrated into `main`.
Agents reading `main` will not see it until a reviewed merge.

## Next action

**Open blockers or risks:**
- `main` is red until D1 is decided.
- The official validator needs a permission grant to run.
- No GitHub connector was available, so CI status is unconfirmed.
- Host trials need real Claude Code and Codex environments. Grok Build has no official skills documentation.

**Next useful step:** The owner decides D1–D6. Answering D1 alone is enough to start Stage 0.

## Revisit when

On resume, compare the actual task, project revision, working tree, instructions,
access, and check results with this handoff before relying on its conclusions. Also revisit
when any decision is made, a stage exits, or the spec or a host's discovery rules change.

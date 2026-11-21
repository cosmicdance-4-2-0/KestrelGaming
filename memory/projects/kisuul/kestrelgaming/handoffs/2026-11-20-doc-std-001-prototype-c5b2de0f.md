---
schema: 1
id: 2026-11-20-doc-std-001-prototype-c5b2de0f
kind: handoff
scope: project:kisuul/kestrelgaming
status: active
evidence: observed
author: generic-kestrel-session-2026-11-20
created: 2026-11-20
updated: 2026-11-21
sources: "Owner-supplied work order DOC-STD-001 (2026-11-20), implemented by generic Kestrel on cosmicdance-4-2-0/KestrelGaming branch claude/nifty-ritchie-t1cur9 (baseline main 3aef6e5, PR A code at cfcada9, merged as PR #12 into main 57b0f71). Mothlight's independent source review (CONDITIONAL ACCEPT, relayed by the owner 2026-11-21); corrections at 79b4eb6. Reference repository Kisuul/Auralprint1 read at 4fb0703. Pilot in a private repository; its details stay there."
---

# DOC-STD-001 — documentation standard and maintenance skills (prototype)

## Summary

**Goal and acceptance criteria:** Deliver a project-agnostic documentation standard (seven exact-case core
documents), a bootstrap and validator, a documentation-maintenance skill and an ASD-STE100-informed writing skill
(PR A, this repository), and pilot it on the owner's private IDIW repository (PR B). The work order's nine-point
Definition of Done is evaluated below.

**Task outcome:** PARTIAL

PR A merged as PR #12 (`main@57b0f71`). An independent review then found three defects (packaging, committed
versus working-tree validation, release evidence); they are corrected at `79b4eb6` in a follow-up PR from the same
branch, pending review. Native discovery is now demonstrated in one host (Claude Code); other hosts remain
unverified. The pilot PR is open, pending review. Owner decisions remain (below).

**Authorized scope and boundaries (historical; recheck on resume):** Scoped repository changes and reviewable
PRs only. No merge, release, publication or deployment authority. Auralprint1 is read-only. On the pilot, no change
to site code, approved copy, contact behavior, release gates, DNS or hosting.

**Target repository, branch, and commit:** `cosmicdance-4-2-0/KestrelGaming`, branch `claude/nifty-ritchie-t1cur9`.
PR A content is at `cfcada9`; this record is committed after it. Baseline `main@3aef6e5`.

**Memory revision loaded:** `3aef6e5`, plus this session's portability audit and work order.

## Evidence

**Delivered in this repository (PR A):**

- [kestrel-documentation-maintenance](../../../../../skills/kestrel-documentation-maintenance/SKILL.md): the standard
  ([DOC_STANDARD.md](../../../../../skills/kestrel-documentation-maintenance/references/DOC_STANDARD.md)), nine operations
  in Audit, Maintain and Reconcile modes (generalized from Auralprint1's documentation-maintenance skill), seven
  factual templates, and `scripts/docstd.py` (standard library only).
- [kestrel-technical-writing-ste100](../../../../../skills/kestrel-technical-writing-ste100/SKILL.md): STE-informed rules in
  original wording, a terminology template, and `scripts/ste_check.py` (protected-token diff and review lint).
  The reference is Issue 9 (January 2025), which ASD sources listed as current on 2026-11-20. No dictionary content.
- Both skills link only inside their own folders or to each other. This applies finding 1 of
  [the portability audit](../2026-11-20-skills-portability-audit-4203ec3b.md).
- `tests/test_doc_standard.py`: 33 tests, including every negative case in the work order.
- The red-main fix (portability decision D1), as a separate commit.

| Command or check actually performed | Observed result | Environment / limits |
| --- | --- | --- |
| `python3 tools/validate_seed.py` at `cfcada9` | Passed | Linux cloud container, CPython 3 |
| `python3 -m unittest discover -s tests` at `cfcada9` | 117 tests, OK | Same |
| `git diff --check` (staged, each commit) | Clean | Same |
| Strict YAML parse of both new `SKILL.md` frontmatters (PyYAML) | Names match; descriptions 497 and 504 characters | Not the official `skills-ref` validator |
| `docstd.py check` on this repository | 376 relative links in 148 Markdown files resolve with exact case | Core-document checks are not applicable here |
| `docstd.py check` on Auralprint1 (read-only) | Finds `docs/Canon/changelog.md` as the equivalent of `Changelog.md`; devlog, decisions and versioning missing | Working tree left clean |
| Pilot (private repository) | Before: 5 FAIL, 4 REVIEW. After: 0 FAIL, 6 REVIEW (each dispositioned). The pilot's own build, Node tests, Nu check and release audit passed locally; merge-push CI conclusions were observed through the GitHub API | Details only in the pilot repository's review record |
| GitHub workflow runs for this repository | **Zero runs on any branch** | CI provides no evidence on this fork |

### Amendment, 2026-11-21 — independent review corrections

Mothlight reviewed PR #12 at head `1b581c2` by source inspection (CONDITIONAL ACCEPT) and found:

- **A, packaging (confirmed):** the maintenance skill linked to the sibling STE skill, so the PR's claim that
  either folder could be installed on its own was **not true at `1b581c2`**. Corrected: the skill is self-contained,
  with an optional by-name integration declared in its description; isolated-install tests now enforce this.
- **B, validation source (confirmed):** links resolved through the file system, so an ignored local file could
  satisfy a committed document's link, and `--ref` changed only Git evidence. Corrected: the inventory comes from Git;
  `--ref` reads documents from the revision; each report names its source; `generated` policy added.
- **C, release evidence (confirmed):** absence of local tags produced a PASS for "no public release". Corrected: it
  is REVIEW (owner confirms); shallow or unchecked cases are UNVERIFIED; opt-in `--remote` lists remote tags.

| Check at `79b4eb6` | Observed result | Environment / limits |
| --- | --- | --- |
| `python3 tools/validate_seed.py` | Passed | Linux cloud container, CPython 3 |
| `python3 -m unittest discover -s tests -v` | 134 tests OK (`test_doc_standard`: 50) | Same |
| `git diff --check` | Clean | Same |
| Native discovery, Claude Code 2.1.330 (this cloud container) | Each skill exported with `git archive 79b4eb6`, copied alone into `~/.claude/skills/`. The host listed the new skill about one minute later (two earlier attempts: "Unknown skill"); invocation by name loaded it and reported its base directory; referenced files resolved, and each skill's tool ran from the installed copy. The maintenance skill loaded while the STE skill was absent. Test installs removed afterwards | One host only. Not tested: description-based selection, symlink install, a fresh session, Codex, Grok |
| Pilot re-run with the corrected tool | 0 FAIL, 7 REVIEW, 0 UNVERIFIED, 8 PASS (was 0 / 6 / 0 / 9). The difference is the changelog "no release" check, now REVIEW by design | Details in the pilot repository |

**Definition of Done status:**

| # | Criterion | Status |
| --- | --- | --- |
| 1 | Seven filenames defined and checked exactly | Met (tests for wrong case, case-fold collision and case-sensitive links) |
| 2 | Skills discoverable and demonstrably usable | **Partial.** Used by path in the pilot (catalog route, T0). 2026-11-21: native discovery demonstrated in Claude Code (personal skills folder, by-name invocation, supporting files resolved). Other hosts unverified; tracked in the portability work order |
| 3 | Bootstrap safe and idempotent | Met (dry run by default, exclusive create, case-variant and equivalent refusal, second-run test) |
| 4 | Ownership explicit and nonduplicated | Met in the standard; the pilot declares two `docs/` locations instead of creating competing root copies |
| 5 | Distinct, tested Changelog and devlog behavior | Met (release-tag ancestry, unreleased-work FAIL, devlog order) |
| 6 | STE-informed writing without compliance claims | Met (claim limit in the skill; a test checks that the lint output makes no compliance claim) |
| 7 | Pilot shows real drift detection and safe correction | Met (stale baselines after the latest merges, a malformed link, missing core documents) |
| 8 | History, approved copy and protected artifacts intact | Met in the pilot (diff limited to documentation; protected paths unchanged) |
| 9 | Both PRs reviewable, with executed evidence | PR A merged (PR #12); its review corrections are in a follow-up PR, pending review. Pilot PR updated with a dated re-run amendment, pending review |

**Hypotheses and assumptions:**
- The fragment-anchor algorithm is a GitHub-style approximation; emphasis inside headings can differ.
- The docstd heuristics (current-state claims, verification claims, README chronology) give REVIEW findings
  only. Two false positives found in the pilot were fixed in `cfcada9`; others are likely in other repositories.
- "Implementer: Kestrel" in the work order was taken to mean generic Kestrel, as the owner selected that day.

**Decisions and rationale:**
- The tools live inside the skill (`scripts/`, `assets/`), so a skill folder can work on its own.
- The validator never reports missing evidence as PASS. UNVERIFIED gives exit 2.
- The pilot keeps the last recorded accepted checkpoint and adds the latest merge beside it. A merge is not
  turned into an acceptance.

**Changed files and uncommitted state to preserve:** None uncommitted.

**Persistence:** The original work is in `main` (PR #12, `57b0f71`). The corrections and this amendment are pushed to
`claude/nifty-ritchie-t1cur9` for a follow-up PR; they are not in `main` until that PR merges.

## Next action

**Open blockers or risks:**
- Native discovery beyond Claude Code: see portability work order stages 3–4.
- Workflow runs: none exist on this fork, so CI cannot confirm the branch.
- Owner decisions recorded in the pilot: relocate or keep `docs/` for the roadmap and decision log; record
  acceptance of the latest merge; route merge chronology to the devlog; choose a version scheme; confirm that no
  public release exists.

**Next useful step:** Owner review of the follow-up PR, then the pilot PR. After merge, run the skill in Reconcile
mode on the pilot repository and continue the portability work order's host trials.

## Revisit when

On resume, compare the actual task, project revision, working tree, instructions,
access, and check results with this handoff before relying on its conclusions. Also revisit when either PR is
reviewed or merged, a host trial is run, or ASD-STE100 publishes a new issue.

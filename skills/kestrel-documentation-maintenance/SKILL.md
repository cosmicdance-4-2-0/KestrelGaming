---
name: kestrel-documentation-maintenance
description: Audit, maintain, or reconcile repository documentation under the Kestrel documentation standard (seven core documents with exact names, one authority per topic, user Changelog.md separate from developer devlog.md). Use when documentation may be stale or contradictory, when links or release notes need repair, when a repository needs its core documents initialized, or after a merge or release changes the current state. Not for release authorization, code audits, or rewriting approved decisions. Self-contained; optionally uses the kestrel-technical-writing-ste100 skill, when installed, for new technical prose.
---

# Documentation maintenance

This skill supplies a procedure. It grants no authority to merge, release, publish, deploy or change source,
specifications or approved decisions. The target repository's `AGENTS.md`, its Definition of Done and the
task's allowed paths take precedence. Apply them; do not create a second Definition of Done here.

The standard is in [DOC_STANDARD.md](references/DOC_STANDARD.md). The tool is
[`scripts/docstd.py`](scripts/docstd.py) (Python 3.9+, standard library only). Run it from any directory:

```sh
python3 <this-skill>/scripts/docstd.py check <repo>                 # working tree; Git evidence from HEAD
python3 <this-skill>/scripts/docstd.py check <repo> --ref <rev>     # only the documents committed at <rev>
python3 <this-skill>/scripts/docstd.py check <repo> --remote        # also list release tags on origin (network)
python3 <this-skill>/scripts/docstd.py init <repo>                  # plan only
python3 <this-skill>/scripts/docstd.py init <repo> --apply          # create missing files; never overwrites
```

Every report names its document source. Report a working-tree result as a working-tree result; use `--ref` when
you claim that a commit, branch or pull-request head is valid.

## Packaging

This folder is self-contained: it holds the standard, the templates and the tool, and every link resolves inside
the folder. It works when it is installed alone.

**Optional integration:** the `kestrel-technical-writing-ste100` skill. Install it beside this skill to apply
STE-informed rules to new technical prose (step 6). If it is not installed, step 6 still applies, and your report
must state that STE-informed review was not applied.

## Modes

Select one mode before you start, and report which mode you used.

| Mode | Use | Writes |
| --- | --- | --- |
| **Audit** | Find drift, conflicts, missing references and unsupported claims | None. Report findings only |
| **Maintain** | Correct living documentation inside an authorized scope | Living documents in scope, after source verification and diff review |
| **Reconcile** | After a merge or release, update current-state documents to the actual result and revision | Current-state documents; dated entries in `devlog.md`; `Changelog.md` only for an actual public release |

## Procedure

1. **Establish context and baseline.** Fetch the remote and record the branch, the exact commit, its ancestry
   and the working-tree state. Keep accepted history separate from newer work, and preserve unrelated changes.
   Read the repository's instructions, README, roadmap and logs, and the source behind each claim you will
   touch. Report verification that you could not do. Do not present an old checkout as current.
2. **Identify audience and authority.** Decide who reads each passage and which document owns it
   ([standard §3](references/DOC_STANDARD.md#3-one-authority-for-each-type-of-information)). Update the existing
   authority before you create a document. Prefer a link to a copied inventory or algorithm.
   Run `docstd.py check` to find missing documents, case errors and duplicate authorities.
3. **Verify claims against source and evidence.** Trace current behavior to source symbols and callers.
   Support historical claims with accepted commits, original evidence and owner decisions. Check plans and
   authority against the roadmap and the task. Documentation and passing tests alone do not prove a technical
   claim. Do not infer acceptance, release or deployment from a merge
   ([standard §7](references/DOC_STANDARD.md#7-evidence-classes)).
4. **Classify each correction before you edit.** Use one disposition for each finding: keep, correct,
   consolidate, link, relocate, remove a duplicate, or **flag for an owner decision**. Account for unique facts
   and authorization context before you remove text. Scope or contract changes need the owner's decision.
   Report out-of-scope defects; do not fix them silently.
5. **Preserve historical evidence.** Do not rewrite historical audits, accepted measurements, original review
   decisions, immutable artifacts or timestamped handoffs. Mark historical text as historical. Link a
   superseding decision; do not change what was originally observed. Relocate unique chronology only inside
   the authorized scope.
6. **Edit concise, factual documentation.** For new technical prose, invoke the `kestrel-technical-writing-ste100`
   skill by name when it is installed; do not copy its rules here. Without it, write short, direct, factual
   sentences, never change identifiers, commands, numbers or units, and say that STE-informed review was not
   applied. Do not rewrite approved marketing copy, quotations or immutable records. Keep compatibility and
   ownership qualifications; do not simplify them into false claims.
7. **Maintain release notes against actual public releases.** Compare `Changelog.md` with the last public
   release. A defect introduced and fixed only during unreleased development is not a public fix. Put
   development chronology in `devlog.md` or PR evidence. A merged PR is not a release.
8. **Validate the complete patch.** Recheck every changed claim and its authoritative destination. Run
   `docstd.py check` before and after, and compare the findings. Check case-sensitive paths, fragments and
   inbound anchors. Confirm that historical evidence and unauthorized paths are unchanged. Run
   `git diff --check` and the repository's documented checks. If you edit a skill, verify its discovery in the
   intended host; a catalog link or a manual file read is not discovery. Report skipped checks and limits.
9. **Deliver within authority.** Make bounded commits and a reviewable PR when requested. Report changes
   separately from findings and deferrals, with the baseline, the head, the evidence and open decisions.
   State whether work is local, committed or pushed. Stop at the review boundary. Never infer permission to
   merge, tag, release, deploy or publish.

## Bootstrap a new repository

Run `init` without `--apply` and review the plan with the owner. `--apply` creates only missing documents
from factual templates. Each created file carries a `docstd:template` marker; `check` reports it as REVIEW
until a person completes the file and removes the marker. Do not invent project history, releases, credentials
or approvals to fill a template.

## Existing repositories

Follow [standard §8](references/DOC_STANDARD.md#8-existing-repositories-migration). Inventory, propose and
review before you move anything. If the migration exceeds the scope, declare the exception in `.docstd.json`
and record the follow-up. Never create a root copy beside an existing authority.

## Limits

`docstd.py` checks structure and applies heuristics. Its REVIEW findings need a person. Its PASS results are
not proof of accuracy, and UNVERIFIED means that the evidence was not available. This procedure was generalized
from a reference repository's documentation-maintenance skill. It has been used on one pilot repository; that
does not certify it for every host or project.

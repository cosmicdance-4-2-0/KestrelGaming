# DOC-STD-001 — Repository documentation standard

**Status:** Proposed standard, prototype version 1. A repository adopts it by an owner decision.
Adoption does not authorize destructive reorganization of existing documents.

**Design principle:** Documentation explains the product, preserves the engineering record and tells
the next developer what is authoritative. It is not an agent diary.

## 1. Core documents

A new repository that uses this standard has these seven files at its root.
**Filename casing is normative.** `CHANGELOG.md` is not a substitute for `Changelog.md`, and
`DEVLOG.md` is not a substitute for `devlog.md`.

| Exact path | Responsibility |
| --- | --- |
| `README.md` | Project identity, current capabilities, usage, setup and navigation |
| `AGENTS.md` | Binding agent and developer contracts, safeguards and one global Definition of Done |
| `ROADMAP.md` | Milestones, planned work, accepted outcomes and deferrals |
| `Changelog.md` | User-facing changes between public releases |
| `devlog.md` | Developer- and agent-facing engineering chronology |
| `DECISIONS.md` | Accepted decisions, authority, rationale and supersession |
| `VERSIONING.md` | Version syntax, compatibility policy, release boundaries and revision rules |

A repository without public releases keeps a `Changelog.md` that states that fact. It does not invent an entry.

## 2. Conditional documents

Create these files only when the project needs them. Do not create empty files or directories to satisfy a template.

| Path | Purpose |
| --- | --- |
| `CONTRIBUTING.md` | Contributor workflow |
| `LICENSE` | Authorized distribution license |
| `SECURITY.md` | Security reporting policy |
| `SUPPORT.md` | User support policy |
| `CODE_OF_CONDUCT.md` | Community participation policy |
| `docs/ARCHITECTURE.md` | System-level architecture |
| `docs/INTERFACES.md` | Stable interfaces and compatibility |
| `docs/CONFIGURATION.md` | Configuration ownership and precedence |
| `docs/TESTING.md` | Verification strategy |
| `docs/RELEASING.md` | Release process |
| `docs/DEPLOYMENT.md` | Deployment and rollback |
| `docs/TERMINOLOGY.md` | Technical vocabulary and approved terms |
| `docs/REQUIREMENTS.md` | Formal requirements |
| `docs/DOCUMENTATION_POLICY.md` | Extended project-specific documentation policy |

Conventional directories, when relevant: `docs/work_orders/`, `docs/reviews/`, `docs/audits/`,
`docs/design/` and `docs/history/`.

## 3. One authority for each type of information

Each type of information has one authoritative document. Other documents link to it; they do not copy it.
Executable source owns the current implementation. If two documents claim the same responsibility,
correct that before you add content.

## 4. Changelog contract

- **Audience:** users.
- Each released-version entry describes changes relative to the previous public release:
  user-visible features, fixes, behavior changes, compatibility changes and important limitations.
- Exclude internal refactors without user impact, agent activity, defects introduced and corrected
  during unreleased development, and release claims that the owner has not approved.
- **A merged pull request is not evidence of a public release.** Each version entry must correspond
  to an actual public release, normally a release tag.

## 5. Development-log contract

- **Audience:** developers, maintainers and agents.
- One entry for each meaningful checkpoint, in one chronological order. Each entry records the date and
  scope, the result, the commit, PR or decision reference, the verification evidence and its limits,
  and significant unresolved work.
- Link to full reproductions, audit reports and PR discussions. Do not copy them.
- Do not write a conversational diary or record every agent action.
- When later evidence changes a conclusion, add a dated amendment or a supersession reference.
  Do not rewrite the earlier entry.

## 6. README boundary

`README.md` describes the project as it exists now. It does not contain development chronology, full test
transcripts, repeated implementation narratives or agent activity. It links to `devlog.md`,
`Changelog.md` and `ROADMAP.md`.

## 7. Evidence classes

Keep these statements distinct. A document must not present one as another:

| Class | Example | Is not |
| --- | --- | --- |
| Merge | "PR #42 merged as `main@1a2b3c4`" | Acceptance, release or deployment |
| Successful CI | "Run 123 passed on `1a2b3c4`" | Human verification or current evidence for a later revision |
| Human verification | "The owner checked the page on a phone on 2026-01-15" | Production authorization |
| Production authorization | An owner decision record | Evidence that a deployment happened |

A current-state statement cites the revision it describes. Historical verification stays dated.

## 8. Existing repositories: migration

The seven-document structure is the target for participating repositories. It is not authorization to rename,
move or delete documents.

1. Inventory existing documents and their current authority.
2. Identify equivalent documents at nonstandard paths.
3. Propose an explicit relocation or compatibility plan.
4. Preserve unique content, historical references and inbound links.
5. Prevent two documents from claiming authority over the same information.
6. Get review before a consequential rename or relocation.

When a migration exceeds the current scope, record a **declared exception** in `.docstd.json` and a reviewable
follow-up. Do not create a competing root copy.

```json
{
  "schema": 1,
  "locations": {
    "ROADMAP.md": {"path": "docs/ROADMAP.md", "reason": "Relocation deferred; see the migration review."}
  },
  "living": ["docs/reviews/RELEASE_READINESS.md"],
  "historical": ["docs/history/**"],
  "generated": ["build/**"]
}
```

- `locations`: the core responsibility is held at another path. The validator reports this as REVIEW, not PASS.
- `living`: extra documents that make current-state claims and must be checked for stale baselines.
- `historical`: glob patterns for archived documents that keep old names. They are excluded from
  duplicate-authority warnings.
- `generated`: glob patterns for build output that is never committed. A link to such a target is REVIEW, not
  FAIL. Without this policy, a link to an ignored or uncommitted target is a FAIL.

## 9. Tools

[`scripts/docstd.py`](../scripts/docstd.py) implements the bootstrap and validation:

- `init` plans the seven documents and, with `--apply`, creates only missing ones. It never overwrites a file.
  A case variant or an equivalent at another path stops creation and asks for review. A second run changes nothing.
- `check` reports PASS, FAIL, REVIEW and UNVERIFIED findings: missing core documents, exact casing,
  case-fold collisions, relative links and fragments with case-sensitive resolution, duplicate authorities,
  stale current-state baselines, unevidenced verification claims, changelog entries against release tags,
  development-log order and README chronology.

**Document source.** Every report names where its documents came from.

- Without `--ref`, the source is the **working tree**: tracked files and untracked files that Git does not ignore.
  Git evidence comes from `HEAD`. A link whose target exists only as an ignored file is a FAIL (or REVIEW under a
  `generated` policy). A link from a tracked document to an untracked target is REVIEW. A working-tree result is
  not a result for any commit.
- With `--ref REV`, documents, the file inventory and Git evidence all come from that revision. The working tree is
  not read. Use this mode to state that a commit, branch or pull-request head is valid.

**Release evidence.** Release checks use local tags by default, so the tool works offline. `--remote` also lists
the remote's tags; a failure to list them is UNVERIFIED. A missing tag never establishes that no public release
exists: a `Changelog.md` without release entries and without tags is REVIEW (the owner confirms). A shallow clone,
or a version entry without a local tag that was not checked against a remote, is UNVERIFIED. A tag found only on
the remote is REVIEW (fetch tags to verify what the release contains). A local tag is accepted as the release
record; publication itself is not verified.

The checks are structural and heuristic. A PASS does not prove that documentation is accurate. Unavailable
evidence is reported as UNVERIFIED, never as PASS.

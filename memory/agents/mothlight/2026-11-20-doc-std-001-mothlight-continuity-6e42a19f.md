---
schema: 1
id: 2026-11-20-doc-std-001-mothlight-continuity-6e42a19f
kind: decision
scope: agent:mothlight
status: active
evidence: user-stated
author: mothlight
created: 2026-11-20
updated: 2026-11-20
sources: "Owner-directed documentation standard discussion on 2026-11-20; public KestrelGaming PR #12 inspected at 1b581c2877050f051c9671087691c943934c81ca; Kisuul/Auralprint1 documentation skill observed at 4fb07033e6fb57ae0d0d6f8005a94f8e78434b23. Private pilot details deliberately excluded."
---

# DOC-STD-001 — Documentation governance and agent continuity

## Summary

**Owner direction, 2026-11-20:** Treat documentation as part of ordinary, reviewable engineering work. Use one authoritative home for each type of information. Do not turn `README.md` into an agent diary. Distinguish user-facing public releases from developer-facing implementation history.

The proposed Kestrel Repository Documentation Standard v1 specifies **seven exact-case core filenames** at the repository root:

| File | Ownership |
| --- | --- |
| `README.md` | Present project identity, usage and navigation |
| `AGENTS.md` | Always-on engineering and authority rules, one global Definition of Done |
| `ROADMAP.md` | Plans, milestones, acceptance and deferrals |
| `Changelog.md` | User-facing differences between actual public releases |
| `devlog.md` | Concise developer/agent engineering chronology, not a transcript |
| `DECISIONS.md` | Accepted decisions, rationale and supersession |
| `VERSIONING.md` | Version and release policy |

**Case is normative.** `CHANGELOG.md` is not `Changelog.md`; `DEVLOG.md` is not `devlog.md`. Other documents are conditional, not empty boilerplate. Existing projects require a reviewed migration or a documented exception; never create a competing second authority.

Auralprint1's [documentation-maintenance procedure](https://github.com/Kisuul/Auralprint1/blob/4fb07033e6fb57ae0d0d6f8005a94f8e78434b23/.agents/skills/auralprint-doc-maintenance/SKILL.md) is the reference pattern: establish baseline, identify ownership, verify source, classify, preserve evidence, edit concisely, maintain public release notes, validate, and deliver within scope.

The owner additionally requested **ASD-STE100-informed** technical prose. Preserve technical terms and exact identifiers; do not rewrite approved creative copy, legal text, quotations or historical evidence. Do not claim formal STE compliance from AI text or a heuristic linter. Skills belong in KestrelGaming, not duplicated in target projects.

## Evidence

- **User-stated:** The owner explicitly selected the seven filenames and casing, requested distinct user `Changelog.md` and developer `devlog.md`, asked to generalize Auralprint1's skill, and directed a prototype followed by review.
- **Observed, 2026-11-20:** [KestrelGaming PR #12](https://github.com/cosmicdance-4-2-0/KestrelGaming/pull/12) was **open**, head `1b581c2877050f051c9671087691c943934c81ca`. It proposes the standard, a bootstrap/validator, and two STE/documentation skills. Its author reports local structural tests; this Mothlight record does not independently reproduce those runs. Native host skill discovery is explicitly not yet demonstrated.
- **Restricted pilot:** A separate project pilot PR was observed open through authorized access. This public record intentionally omits repository-private files, reports, internal decisions, source and contact details. Reopen the authorized project source rather than treating this summary as current project authority.
- **Mothlight memory boundary:** The owner's earlier request to checkpoint continuity should use this agent's authorized Git home, not merely a downloadable attachment. Only public-safe learning belongs on this branch.

## Revisit when

Recheck the exact heads, tests, and review findings of the two work PRs; confirm native skill discovery and packaging; inspect any proposed contract change; and update status after an owner merge or adoption decision. For a restricted project, fetch its current documents using authorized access rather than mirroring them in public agent memory. Distinguish a merge, acceptance, a public release and a production deployment.

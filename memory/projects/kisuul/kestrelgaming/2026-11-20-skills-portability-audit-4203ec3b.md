---
schema: 1
id: 2026-11-20-skills-portability-audit-4203ec3b
kind: lesson
scope: project:kisuul/kestrelgaming
status: active
evidence: observed
author: generic-kestrel-session-2026-11-20
created: 2026-11-20
updated: 2026-11-20
sources: "Read-only audit of cosmicdance-4-2-0/KestrelGaming main 3aef6e5ba9a6c79b28d302f88f2be2fdb12bcb5a (CPython 3, Linux cloud container, 2026-11-20) against the Agent Skills specification at agentskills/agentskills main and host documentation read the same day. Owner request: Kestrel skills must work in any agent environment."
---

# Skills cross-host portability audit — 2026-11-20

## Summary

**Outcome: PARTIAL. The format conforms, but skills can't be distributed on their own.**
At `3aef6e5` the 35 skills (3 Kestrel, 6 mathematics and 26 vendored PixiJS skills)
follow the Agent Skills naming and frontmatter rules, with one exception: a vendored
description over the length limit. They work in any host that can read the whole
checkout and follows [AGENTS.md](../../../../AGENTS.md) to [the skill catalog](../../../../skills/INDEX.md).
They are **not** natively discoverable by any host. A skill folder **cannot be
installed on its own** without breaking its links. "Works in any agent environment" is
therefore true only for manual, checkout-based reading.

The remediation plan is in [the portability work order](handoffs/2026-11-20-skills-portability-work-order-4203ec3b.md).

**Scope note:** this record uses the existing `kisuul/kestrelgaming` scope for the shared
repository. The checkout audited was the reconciled `cosmicdance-4-2-0` fork. Both mains were
brought to a common baseline (see [baseline reconciliation](../../../../docs/BASELINE_RECONCILIATION.md)).
Which owner is canonical for memory scope is an open question in the work order.

## Evidence

### Checks actually performed

| Check | Observed result | Limits |
| --- | --- | --- |
| `python3 tools/validate_seed.py` | **Exit 1:** `memory/shared/2026-11-19-generic-kestrel-review-checkpoint-c83e1b2f.md: Handoff needs project scope and Next action` | Structural only |
| `python3 -m unittest discover -s tests` | **84 run, 6 failures**, all from that same record error | Structural only |
| Frontmatter parse of all 35 `SKILL.md` | Only `name`, `description` and (PixiJS) `license: MIT` are used | Local script |
| Name rule vs spec | All match their folder, are 64 characters or fewer, lowercase with single hyphens | The validator's `SLUG` pattern equals the spec rule |
| Description length vs spec 1–1024 | `pixijs-custom-rendering` = **1,146** characters; all others 135–979 | Measured after decoding the JSON-quoted scalar |
| Body length vs the spec's recommended 500 lines | Only `pixijs-scene-graphics` (576) exceeds it; first-party skills are 29–52 lines | A recommendation, not a hard limit |
| Links leaving the skill's own folder (fenced code excluded) | **All 9 first-party skills**; among PixiJS, only the `pixijs` router (sibling skills only) | Local script; inline code not excluded |
| Discovery folders (`.claude/skills`, `.agents/skills`) | **None present** | Repository tree only |
| Total description characters (the always-loaded metadata) | Kestrel 788, math 917, PixiJS 16,596; **18,301 total** | Character count, not tokens |
| Official `skills-ref` validator (`agentskills` CLI 0.1.1) | Installed in scratch space, but **running it was blocked** by the session permission classifier | **Not run.** No official-validator result is claimed |

### Out-of-folder link inventory (first-party)

- `kestrel-recall`: `KESTREL.md`, `kestrel/MEMORY_PROTOCOL.md`, `kestrel/STATE_PROTOCOL.md`, `memory/INDEX.md`, `skills/INDEX.md`, `kestrel-remember`.
- `kestrel-remember`: `CONTRIBUTING.md`, `kestrel/MEMORY_PROTOCOL.md`, `kestrel/STATE_PROTOCOL.md`, three `kestrel/templates/*`, `memory/INDEX.md`.
- `kestrel-html-conformance`: `kestrel/PERMISSIONS.md`, `kestrel/VERIFICATION.md`.
- Six `math-*` skills: `docs/MATH_CURRICULUM.md` (five of six), `tests/fixtures/MATH_FOUNDATION_VECTORS.md`, and sibling math skills.

[Integration guidance](../../../../docs/INTEGRATION.md) and [contributing](../../../../CONTRIBUTING.md)
describe this repository dependence as deliberate. A "host adapter" is named, but none is specified.

### Findings

1. **No standalone install (observed).** The spec says to reference files relative to the skill root.
   Copying one folder into a host's skills folder or a claude.ai upload breaks every link listed above.
2. **No native discovery (observed).** No host-standard folder exists. The two `agents/openai.yaml`
   files (Codex display metadata) have no effect unless Codex discovers the skill.
3. **Spec violation (observed).** The `pixijs-custom-rendering` description is over 1,024 characters.
   Strict paths (claude.ai upload, Skills API packaging, `skills-ref`) can be expected to reject it.
   Claude Code truncates its listing at 1,536 characters. The text is vendored at a pinned upstream commit.
4. **Validator mismatch with the spec (observed).** First-party skills cannot declare the spec's
   `compatibility` or `metadata` fields. The validator does not check the description limit (1,024),
   the `compatibility` limit (500) or body size.
5. **Hard-coded owner (observed).** The recall and remember descriptions name `Kisuul/KestrelGaming`.
   [The pickup runbook](../../../../docs/AGENT_PICKUP.md) says to default to `cosmicdance-4-2-0/KestrelGaming`.
6. **Descriptions say what but not when (observed, minor).** The six math descriptions state what
   the skill does but rarely when to use it, which the spec asks for.
7. **Main fails its own checks (observed).** CI runs the validator on push, so the main workflow
   is *inferred* to be failing at `3aef6e5`. The GitHub connector failed to connect, so this was not confirmed.
8. **Listing budget risk (hypothesis).** Codex documents a startup skill-list cap of 2% of the context window,
   or 8,000 characters when the window is unknown. Installing all 35 skills (18,301 description characters)
   natively could exceed it. Truncation behavior was not tested.

### External sources (read 2026-11-20; recheck before relying on them)

- [Agent Skills specification](https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx):
  name and description rules, the six frontmatter fields, the under-500-line recommendation, and relative references from the skill root.
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills):
  `.claude/skills` discovery, followed symlinks, `${CLAUDE_SKILL_DIR}`, and upload paths that reject non-spec keys.
  Cloud sessions do not read `~/.claude/skills`.
- [Codex skills documentation](https://developers.openai.com/codex/skills): `.agents/skills` from the working directory
  up to the repository root, `$HOME/.agents/skills`, followed symlinks, optional `agents/openai.yaml`, and the listing cap.
  **Read via a search summary.** The page itself did not download in this container.
- Grok Build: **no official xAI documentation was found.** A [third-party skill page](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-grok)
  claims Grok reads `.claude/` skills. That claim is unverified.

### Not established

No host was observed loading, listing or invoking these skills. Hypothesis to test: when a host
folder holds a symlink to `skills/<name>`, the agent resolves `../../` links against the real folder.
This is plausible but untested. No claim is made about skill effectiveness.

## Revisit when

Any skill frontmatter, link or host-metadata file changes; the validator's skill rules change;
the vendored PixiJS snapshot is refreshed; a host trial is run; or the Agent Skills spec or a
host's discovery rules change. Recheck against the current revision rather than this record's numbers.

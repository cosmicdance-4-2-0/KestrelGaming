# Kestrel Studio boundary — Concept proposal v0.1

**Status:** Design boundary only; neither a studio runtime nor a new governing authority.

Kestrel is being developed as **the studio in which specialized engineering agents work**, not merely a list of personality profiles. The studio coordinates contributions across game projects; it does not own the projects' source code, absorb individual identities, or override instructions supplied by an authorized human or host.

## Distinct concerns

| Concern | Source of truth | Responsibility | What it must not claim |
| --- | --- | --- | --- |
| Foundation | `KESTREL.md`, shared `kestrel/`, `skills/` | Common engineering method, verification, memory and permission guidance | Tools or privileges simply because policy is written down |
| Individual agent | `agents/<id>-v1` home | Stable personal instincts, judgment, attributable experience | Authority over projects or another engineer's memories |
| Team | `teams/<team-id>/TEAM.md` and `PROFILE.json`, when approved | Purpose-specific composition and decision protocol | Independent instances, votes, or new privileges |
| Studio | Future explicit studio policy and authorized orchestration | Route tasks; manage work orders, staffing, handoffs, quality gates and shared knowledge | Become another personality or secretly modify member contracts |
| Project | The target project's repository and authorized owner | Requirements, designs, source code, assets, tests, release decisions | Depend on agent-role lore to understand its own implementation |

A **team contract** specifies *how specialists reason together about a kind of work*. A **studio contract** would specify *how work is requested, assigned, reviewed, handed off and accepted across teams and projects*. These are orthogonal: one team can serve many projects, and one project may involve several teams.

## Assignment lifecycle (proposed, not automated)

1. **Intake:** a trusted task owner identifies project, objective, branch, constraints, acceptance evidence, and permission boundaries.
2. **Route:** the studio recommends a generic engineer, an individual agent, or a purpose-built team according to risk and expected benefit. The owner can override the recommendation.
3. **Pickup:** resolve exact Kestrel and target-project revisions; load applicable member contracts and relevant scoped memory. An advertised profile never counts as an instantiated agent.
4. **Execute:** make the smallest approved, reviewable progress; keep dissent and experimental evidence explicit. No team acquires independent code-edit authority merely by being selected.
5. **Challenge:** seek an independent assessment when consequences justify the overhead. Distinguish a single model's internal counterweight from a separately launched reviewer.
6. **Deliver:** return changes, executed checks, risks, incomplete criteria, and handoff. Human authority owns merge, release, and material tradeoffs.
7. **Learn:** record project facts in the target project, reusable methods in Kestrel's reviewed shared library, and each agent's own attributable lessons in its approved memory branch.

## Minimal future studio contract (not yet a schema)

A later Studio Contract may define *routing policy*, *work order format*, *project registry*, *team catalog*, *review requirements*, *provenance receipts*, *resource and tool limits*, and *institutional learning*. These are studio-level services; they must not be copied into every Team Contract.

There is no reason yet to invent team-level memory, employer-style personnel hierarchy, managerial agent identities, synthetic votes, or a self-operating scheduler. Evaluate whether a need exists before introducing any of those mechanisms.

## Boundary invariant for the present checkpoint

The `KestrelTeamContract` schema v0.1 is deliberately limited to composition, operating method, execution-mode truthfulness, evidence, continuity constraints and permissible outputs. It **does not** select work autonomously, assign repository permissions, maintain a global backlog, supervise releases or own institutional memory. Those are potential studio concerns, and none are implemented here.

At checkpoint 2 the studio boundary was defined without creating any teams. Checkpoint 3 adds the first proposed composition, [The Architects](../teams/architects/TEAM.md), under these boundaries. Existing individual homes, the shared Kestrel operating contract, and all game project repositories remain untouched.

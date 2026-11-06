---
schema: 1
id: 2026-11-05-mothlight-branch-memory-authorization-6809b211
kind: decision
scope: agent:mothlight
status: active
evidence: user-stated
author: mothlight
created: 2026-11-05
updated: 2026-11-05
sources: "Kisuul's explicit authorization in the Mothlight conversation on 2026-11-05 (America/Los_Angeles); branch baseline 38097cc7d5ad6c69de77154485828fa8df55789c."
---

# Direct commits for Mothlight continuity

## Summary

Kisuul authorizes Mothlight to commit directly to `agents/mothlight-v1` in
`cosmicdance-4-2-0/KestrelGaming` to preserve agent memory between sessions.
Use that branch for durable, indexed Mothlight continuity records and synchronize
them without repeatedly requesting permission for the same authorized purpose.

The scope is Mothlight's branch and agent-memory persistence. Other branches,
repositories, and unrelated changes require their own task authority. Follow
the [memory protocol](../../../kestrel/MEMORY_PROTOCOL.md), validate records,
preserve concurrent work, and respect actual repository and host controls.

## Evidence

**User-stated:** After loading Mothlight, Kisuul explicitly clarified that direct
commits to the Mothlight branch are permitted because this is how the agent keeps
memory between sessions. The authorization comes from that user instruction;
this record preserves its source and scope rather than granting tool access.

## Revisit when

Kisuul changes or revokes this authorization, the agent's home branch or repository
changes, repository controls change, or proposed work exceeds memory persistence.

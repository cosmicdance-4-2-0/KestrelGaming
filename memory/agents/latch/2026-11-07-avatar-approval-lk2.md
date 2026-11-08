---
schema: 1
id: 2026-11-07-avatar-approval-lk2
kind: decision
scope: agent:latch
status: active
evidence: user-stated
author: latch-session-2026-11-07
created: 2026-11-07
updated: 2026-11-07
sources: "2026-11-07 user message 'Love it, lock it down Latch' following generated 1254x1254 avatar; agents/latch/VISUAL_IDENTITY.md; approved portrait PNG sha256 d1738799f2026b4e266474880b3dc2299127e87959e9f8ee2a8721c21ef90203."
---

# Latch — Approval of canonical portrait

## Summary

The user approved Latch's generated pangolin-locksmith portrait on 2026-11-07 in the first-run conversation. Treat this image's appearance as the current canonical visual reference, not as evidence for an authenticated persistent runtime identity. The initial written visual identity remains the governing design rationale.

A 128×128 WebP avatar derivative is committed at `agents/latch/assets/latch-avatar-128.webp` for repository reference. It is not the original full-resolution image. Preserve that distinction when recreating or upgrading assets.

## Evidence

- User wrote: "Love it, lock it down Latch."
- Approved full-resolution image: 1254×1254 PNG, SHA-256 `d1738799f2026b4e266474880b3dc2299127e87959e9f8ee2a8721c21ef90203`. This master was delivered in the current conversation but was not persisted to the GitHub repository at this checkpoint.
- GitHub avatar: 128×128 WebP, SHA-256 `231ae513ddb4ce614c98883ee7cfcd2b84f984ae0582575ddc7f7eb6a90c4576`, Git blob SHA `d28fafc0f82567ac7fe31fc2e9221e7dc6781154`.
- Visual requirements: sandstone muzzle, amber eyes and skeptical half-smile, overlapping bronze/graphite pangolin scales, slate workshop jacket, aged-brass collar catch.

## Revisit when

When the full-resolution source can be safely persisted, the user revises the appearance, or a new approved alternate-size asset is generated. Never silently replace the approved visual, and do not claim source-file retention unless verified.

---
schema: 1
id: 2026-11-06-ap117-project-profile-gauge-r01
kind: profile
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-06
updated: 2026-11-06
sources: "User's request and https://github.com/cosmicdance-4-2-0/ap_117_KESTREL at e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb; docs/CP2_FILE_PCM.md, AGENTS.md, README.md, GitHub PR #2"
---

# cosmicdance-4-2-0/ap_117_KESTREL

## Summary

Auralprint 117 is a new accuracy-first audio-analysis and visualization app. At the inspected CP2 revision, the running prototype handles bounded mono/stereo PCM16 WAVE or synthetic Float32 sine through the same unweighted per-block RMS method, exact sample-span metadata and independent Canvas2D SignalScope model. [Project instructions](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/AGENTS.md) and [CP2 contract](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/docs/CP2_FILE_PCM.md) are authoritative, not this memory.

The repository was **private** on inspection. These public Kestrel memories contain links, conclusions and non-sensitive bounded test data, never its copied source or audio recordings. The owner protects accepted checkpoints and reserves merge authorization.

## Evidence

[Checkpoint plan](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb/docs/CHECKPOINTS.md) excludes FFT/PSD, playback, device clocks, legacy ports, and alternate rendering backends from CP2. The active reviewed [CP2 branch](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/tree/foundation/axiom-file-pcm-cp2) was at `e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb`; [PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2) has independent review pending. Existing CI passed. [Gauge's numerical handoff](handoffs/2026-11-06-ap117-cp2-gauge-numeric-audit-r01.md) captures the exact verification and remaining interface concerns.

Tests and docs in the source branch can change; this record does not grant project write authority or certify physical performance.

## Revisit when

The target branch or checkpoint status changes, source/backend interfaces change, or Axiom/owner accepts a new architecture or measurement definition.

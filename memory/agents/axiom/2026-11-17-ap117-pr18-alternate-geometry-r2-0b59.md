---
schema: 1
id: 2026-11-17-ap117-pr18-alternate-geometry-r2-0b59
kind: handoff
scope: agent:axiom
status: draft
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR #18 head 0b5902ba0934205ec1fbf4954c445f8fd80d4ee3 vs main 4ef3d2376f6de1a390024eb65cbad6beab12eadb; GitHub Actions run 44254032526 job 134631292693; PR comment 6971373114; prior reviewer packet 6970456301."
---

# Axiom — AP117-006B alternate-geometry host regression and R2 review dispatch

## Summary

With owner instruction to proceed on the previously recommended PR #18 completion checkpoint, added an **actual-host test-only** legal M8/H4/B12 B0 recovery regression in `cosmicdance-4-2-0/ap_117_KESTREL`, branch `task/ap117-006b-b0-psd-recovery`. The latest exact head is `0b5902ba0934205ec1fbf4954c445f8fd80d4ee3`; base remains `main@4ef3d2376f6de1a390024eb65cbad6beab12eadb`. The PR remains **DRAFT/UNMERGED**.

One new `tests/app-b0-alternate-geometry.test.js` uses a test-only module loader to select 1200 Hz/B12/10ms and M8/H4/N8 while running the real application composition, signal source, pipeline, spectrum producer and PSD session. This does not alter production CONFIG, DSP, schemas, schedulers, native subscription or benchmark source pins.

## Evidence

- In the initial revision0 B12 block `[0,12)`, two real FFT/PSD windows are delivered. A genuine amplitude change triggers the first fence; manual recovery is disabled and an early click is inert.
- The first revision1 B12 `[12,24)` computes two complete FFT windows but the producer's transition fence deliberately retains neither. Only after successful settlement is B0 enabled. New same-epoch attachment witnesses **producer frontier 2, source cursor 24**, no new measurements and no auto-backfill.
- Next revision1 B12 `[24,36)` yields exactly new subscriber ordinals `3,4,5` with spans `[20,28)`, `[24,32)`, `[28,36)`. The first span has **four legal post-revision but pre-attachment PCM frames**. No window includes pre-revision frames. The test enforces one host timer/FrameHost and no additional click-time source read, accept, or FFT.
- First test commit `7b4a3c2a27209d414b27b5e6a7d13a3908e8657a` **failed** GitHub CI due to a test regex escape syntax error. Corrected to `0b5902b` without changing production. Verified [GitHub Actions 44254032526](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44254032526), job `134631292693`: **SUCCESS, 151/151 Node tests**, static build, official HTML validation, Chromium/offline browser smoke and whitelist/whitespace steps. This is **remote CI evidence**, not a local Axiom suite run.
- Posted [exact-head R2 review request](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/18#issuecomment-6971373114), preserving individual Harbor/Latch/Gauge/Mothlight/Flint/Kite responsibilities and independent evidence limits. The comment does not launch agents or count as their review. Current fetched PR remained draft/unmerged; Issue #14 open, Issue #11 parked/open.

## Outstanding gate / handoff

**Outcome: PARTIAL** — implemented and CI-verified the scoped regression; independent second-pass review and owner acceptance are outstanding.

**HOLD owner merge.** Obtain actual independent R2 reports for the corrected PR #18 plus the new test; reconcile any blockers, check current head and CI, and only then issue owner merge GO/NO-GO. Do not treat test passing as source/product certification or six-role consensus. A review may uncover additional geometry, EOF, origin, interaction or producer-currentness risks.

Original AP117-005B benchmark script/pin still refuses the modified host source; **151/151 CI includes an explicit refusal test**, not a fresh 72-trial scientific benchmark or new target-device performance admission. No Issue #11 policy or CP3-B2 presentation implementation is part of this checkpoint.

## Revisit when

A reviewer posts an exact-head R2 verdict, PR #18 changes head or merges, Issue #14 closes, a regression falsifies B0, or target-project requirements change. Revalidate both PR state and current source rather than inheriting a historical CI result as current.

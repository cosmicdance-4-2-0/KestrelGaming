---
schema: 1
id: 2026-11-14-ap117-codex001-review-implementation002-handoff
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-codex-delegation-session
created: 2026-11-14
updated: 2026-11-14
sources: "Human-relayed CODEX-AP117-001 planning report; independently inspected Auralprint main@0531e734a2ece59cd877ea8659069efee2e0a905 AGENTS.md, src/config.js, src/analysis/spectrum-stream.js, docs/CHECKPOINTS.md and package.json; Issue #8 Axiom review comment 6890580687."
---

# Auralprint 117 — Codex plan review and implementation delegation

## Assignment #1: Codex planning report

Human relay provided Codex's read-only planning report recommending **bounded per-subscriber pull delivery** via a private per-`accept` transaction, preserving `createSpectrumStream.accept/readCurrent/isCurrent` and `ap117.spectrum/1`. Proposed `subscribeComplete({capacityObservations})` with `take/readStatus/resync/dispose`, optional producer `dispose()`, generation and BigInt ordinal per completed window distinct from existing CP2 and spectral revisions. Requested sticky per-subscriber overflow, no callbacks during `accept`, entire-waveform finiteness/metadata validation before externally observable commit, source-epoch/currentness fencing, atomic handling of failed late PCM sample, terminal EOF drain, CONFIG-governed resource limits.

**Attribution:** Codex reported 67/67 Node tests and static build passing, source-executed legal CP2 fixture, independent Python DFT max difference ~9.1e-17, invalidation and far-BigInt probes. These reported experiments were **not** independently rerun by Axiom in the reconciliation; Axiom independently confirmed live repository main baseline and actual source/config/AGENTS.md/roadmap/package paths. No first delivery prototype exists yet.

## Axiom's review

Published [Issue #8 design integration review](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/issues/8#issuecomment-6890580687). **GO for bounded implementation proof**, not acceptance/merge. Important corrections:
1. Staged complete-window references are themselves a bounded resource. Naive `ceil(B/H) * binCount` staging can require ~512 MiB under permitted B8192/H1/Nfft16384; don't retain all when subscriber inevitably overruns. Stage only finite budget, keep explicit loss/fence/overrun results and correct latest. Protected latest-only behavior should not suffer extra history allocations without subscribers.
2. Producer generation/currentness and subscriber continuity must not be conflated with latest publication revision. Legitimate historical same-generation windows stay ordered; reset/invalidate revokes old ready; source parameter segmentation and resync may forfeit post-boundary windows and must disclose that loss.
3. Externally visible delivery must be transactional even though CP3-A currently computes some early windows before discovering late invalid PCM. Whole-waveform prevalidation, private staging and atomic commit; no callback during accept; report any revision difference on failure.
4. Gauge's **legal** CP2 fixture: `x[n]=(n+1)/32` exact Float32, fs48000, periodic Hann, M8/H4/Nfft8, one final 20 block at CP2 blockFrames20 versus five 4 blocks at blockFrames4; four spans and DC 0.15625/.28125/.40625/.53125, final latest .53125. CP2 finishing revisions legitimately differ. Prior 8/4/4/4 partition invalid as a single fixed blockFrames8 pipeline and only a direct-adapter hypothetical / negative CP2 control.
5. Compare per-window DFT/PSD algebra with test-only oracle, no B1 PSD shipping; preserve render-fault global stop, EOF replay requirement, one PCM source, no extra FFT, CP2/CP3-A numerics, existing `readCurrent`, no compositor/third-party plugins.

**Implementation assignment:** A self-contained Codex brief `CODEX_AP117_002_Complete_Spectrum_Delivery_Implementation.md` was generated in the human conversation as a downloadable file, and handed back to owner for manual Codex execution. No Codex session has been launched by Axiom; no application code, PR, push, or merge was made in this turn. The prompt allows local isolated task-branch edits/test/commits, disallows push/PR/merge/deploy, and requires exact tests plus senior review after a diff exists.

## Next

Owner forwards CODEX-AP117-002 to Codex and relays its diff/results. Axiom reviews exact resulting branch/commit. Gauge, Flint and Harbor lead math/ownership/lifecycle audits, with targeted Latch, Kite, Mothlight attention. Owner makes final adoption/merge decisions. Revisit on changed accepted baseline, resource-budget blocker, or any discovered interface conflict.

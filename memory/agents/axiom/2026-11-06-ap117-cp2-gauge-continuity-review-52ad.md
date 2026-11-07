---
schema: 1
id: 2026-11-06-ap117-cp2-gauge-continuity-review-52ad
kind: decision
scope: agent:axiom
status: active
evidence: observed
author: axiom-review-session
created: 2026-11-06
updated: 2026-11-06
sources: "Gauge handoff on agents/gauge-v1 (2026-11-06); ap_117_KESTREL at e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb; CP2 PR #2 and CI 42329197868; source and existing tests inspected through GitHub connector."
---

# Axiom CP2 review — stream continuity belongs at publication ingress

## Summary

**Outcome: COMPLETE review; no application modification or merge.** Agree with Gauge's bounded numerical PASS for PCM16 decoding and per-block RMS, relying on Gauge-attributed independent probes and the exact inspected code (not independently rerunning the exhaustive numbers). **Integration verdict: REQUEST CHANGES** before accepting CP2 as a source-interchange foundation: the source-to-AnalysisPipeline boundary lacks cross-block continuity and terminal validation. The checkpoint plan expressly lists gaps/invalid input as CP2 proof; this is an interchange-integrity blocker, not an observed arithmetic defect with the two built-in contiguous sources.

**Decision:** Individual source adapters own sample creation and sample-frame stamping; the host owns source selection, explicit replacement, epoch allocation and cleanup; **AnalysisPipeline ingress owns stream identity, sequence, final/EOF validation and fail-closed publication**. DSP math must consume only validated blocks; consumers cannot infer continuity from multiple ready observations. Source sample clocks are not wall/render/playback clocks.

## Evidence

- Source inspection at CP2 commit [`e9ec16f`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/commit/e9ec16f065559f5cef4a9faa3cd9f18b5de44aeb): `src/analysis/pipeline.js` checks each block independently, invokes the analyzer and verifies that the returned span describes *that same block*, but stores no previous expected end frame, active stream identity or finalized flag.
- [Gauge's source-backed handoff](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/gauge-v1/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-06-ap117-cp2-gauge-numeric-audit-r01.md) attributes an exhaustive signed PCM16 Float32 digest comparison, nine high-precision RMS fixtures (max reported ~0.469 ULP), and direct invalid-sequence probes: gap, overlap, post-final data and null without final. These probes are Gauge-executed; this review inspected source and CI but did not rerun numerical benchmarks.
- [CP2 PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2) remains open at this exact head, stacked on CP1 (PR #1 is now merged). [CI run 42329197868](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42329197868) completed successfully, with 34 existing tests. CI success does not include the missing transition tests.
- The existing `tests/pipeline.test.js` deliberately allows recovery after a transient read exception before any source frames were consumed. Preserve valid recovery if the next block is exactly the expected interval, rather than unconditionally latching every exception as terminal.

## Proposed CP2 ingress contract (review decision, not implemented)

1. On first accepted block for an active CP2 source, require `startFrame === 0n` (both current adapters start at zero). Pin the tuple `sourceId, sourceEpoch, channelId, tap, clockDomain, sampleRateHz`; all must remain stable until explicit `replaceSource`. For a future live source attaching at nonzero position, add an explicit versioned origin/discontinuity contract; do not silently broaden CP2.
2. For subsequent blocks in one source epoch, require `block.startFrame === expectedNextFrame` where `expectedNextFrame` is the previous **accepted** exclusive end. Reject gaps, overlaps, duplicates and reordered intervals. Never silently fill missing frames, trim overlap, resample, or mix epochs.
3. `sourceRevision` is a nondecreasing parameter/configuration revision, not a separate sample clock: an increase at an exact contiguous boundary is legal and does not reset `expectedNextFrame`. A decrease is invalid. The host's `invalidate(reason)` clears a publication but does not restart the source or change its epoch.
4. A `final:true` block is a valid last ready measurement (even if full sized). The next read may return only null EOF, producing `ended` and clearing the current measured publication. A nonnull block after final produces `invalid`. Null without a previously accepted final produces `invalid`, **not** `ended`; unexpected synthetic EOF is also invalid. Once ended, no further ready publication without explicit replacement; repeated ended checks may be idempotent.
5. Validate envelope, source identity, continuity, terminal legality and metadata **before** running DSP, especially before any future stateful analyzer. Commit `expectedNextFrame`, revisions and terminal flags only after measurement metadata and output have been fully validated and atomically published. On error the current view is invalid with null measurement/waveform and previous ready stamp revoked. A transient acquisition error that consumed no frames may recover on a subsequent exact-next-frame block; otherwise explicit source replacement/new epoch is required.
6. `replaceSource` invalidates the old stamp and resets ingress cursor/terminal state, with the host supplying a fresh epoch for a fresh playback/selection. Unexpected in-place source/epoch/clock changes are protocol errors; a future live capture drop needs an **explicit typed discontinuity** or new epoch, never an implicit gap in ready results. Epoch identity is distinct from monotonically increasing publication revision.

## Required negative/positive tests before CP2 integration

- A: ready `[0,4)` then `[100,104)` within one epoch must become invalid; no stale ready data.
- B: ready `[0,4)` then `[2,6)`, or another `[0,4)`, must become invalid.
- C: ready `[0,4)` `final:true`, then another block, must become invalid; final then null must become ended with no current measurement.
- D: nonfinal ready then null EOF must become invalid, not ended; spontaneous null on synthetic is likewise invalid.
- E: unannounced `sourceEpoch`, clock domain, source ID, channel/tap, or rate change must become invalid; replacement with fresh epoch must succeed and start at declared origin.
- F: contiguous sample frames with increased `sourceRevision` must remain ready (no false discontinuity); lower revision must fail.
- G: nonzero initial frame in CP2 must fail; an exact full final block and one-frame final tail must both pass.
- H: after every rejected block or bad analyzer result, current measurement/waveform are null, old `isCurrent` is false, no cursor is committed; test transient throw **before** consuming frames followed by exact-next-frame recovery, and gap after consuming a failed sample.
- I: no renderer, no source-clock reinterpretation, no implicit epoch change on host invalidate; existing 34 positive cases remain passing.

Keep the new state private to the pipeline ingress. No new Camera, Canvas, Scene, DSP algorithm, WAV decoder or renderer changes in the corrective checkpoint. Define these before new CP3/streaming adapters.

**Meter semantics:** `rms-amplitude` remains `unweighted-mean-square-sqrt/1` over the exact finite `[start,end)` sample interval. At 480 frames, duration varies by sample rate. It is not VU/LUFS/dBFS, programme loudness or hardware calibrated level; varying phase at low frequency yields legitimately varying block RMS. A future fixed-duration, integrated, spectral or calibrated meter requires a separately versioned metric/acceptance proof.

**Evidence limits:** Independent numeric tests and measured ULP claims belong to Gauge, not to this review. This session directly inspected source and tests and GitHub CI status but did not run the project's test suite, local browser, device tests, or hardware calibration. No formal PR review or application changes were submitted.

## Revisit when

CP2's ingress validator and its negative/positive transition fixtures are implemented, PR #2 advances, or live/streaming sources need explicit nonzero origins and discontinuities. Review exact new SHA and run the relevant tests before owner acceptance.

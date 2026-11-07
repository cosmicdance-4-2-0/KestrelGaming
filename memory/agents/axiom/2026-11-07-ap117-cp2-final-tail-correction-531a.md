---
schema: 1
id: 2026-11-07-ap117-cp2-final-tail-correction-531a
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-implementation-session
created: 2026-11-07
updated: 2026-11-07
sources: "Harbor PR #4 review on 099a4286d54544c3db5f195afe891cc4db2f188d, https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/4#pullrequestreview-5811871784; PR #4 candidate 531a21c2414c85b66c25dbddf4d133d48aa0dd94; Actions run 42371196077."
---

# CP2.1 — Harbor final-tail correction at PR #4 head 531a21c

## Summary

**Outcome: COMPLETE bounded correction and exact-head GitHub CI PASS; PR #4 OPEN, Harbor/Flint re-review and owner merge pending.** This follows the initial CP2.1 [implementation handoff](2026-11-07-ap117-cp2-recovery-pr4-099a.md), which documents the first candidate at `099a4286`. Harbor's independent exact-source review found one additional recovery hole: Canvas failure during presentation of a final one-frame WAV block invalidated it, then `Retry render` advanced to EOF and displayed misleading `COMPLETE` with RMS unavailable.

## Evidence

- PR [#4](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/4) branch `maintenance/axiom-cp2-recovery` advanced to exact `531a21c2414c85b66c25dbddf4d133d48aa0dd94` via correction commit `a85d26c08e6db4a9d399a6f436b49473ca440b6c` and a test-only paint-timing correction `531a21c2414c85b66c25dbddf4d133d48aa0dd94`. Base remains `main@7a8df54a35f4743e4c223001337d8382dda21122`.
- Three in-scope paths changed from Harbor-reviewed `099a4286`: `src/main.js`, `tests/app-integration.test.js`, `docs/CP2_FILE_PCM.md`. No changes to FrameHost, FileImport, pipeline, decoder, numerical RMS, source/clock/epoch semantics, drawing algorithm or dependencies.
- **Decision:** normal `COMPLETE` still means the actual last ready final-block RMS is displayable. A failed final-block presentation invalidates that publication. On a successful `Retry render`, legal EOF with no current final measurement now shows explicit `EOF — REPLAY REQUIRED`, no numeric or waveform, no continuing timers/frames and a labeled `Replay` control. Only subsequent explicit `Replay` replaces the file source, starts at sample zero with a fresh epoch, and remeasures. No stale republishing or hidden replay.
- Integrated regression extends the existing entrypoint host test with a 481-frame PCM16 WAV: fail Canvas `setTransform` when painting accepted tail `[480,481)`, assert fault+invalid current, retry to truthful EOF state, then explicit replay to `[0,480)` and final `[480,481)` with RMS `0.250000`, no timer leaks. The test polls the scheduled rAF before reading displayed output.
- First candidate [Actions run 42371108788](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42371108788) failed a new test assertion that prematurely checked displayed data before its scheduled rAF; this was a test timing error, corrected in the next commit. **Final [exact-head Actions run 42371196077](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42371196077) succeeded: 53/53 Node tests, static build, offline dependency gate, official Nu built/rendered HTML, Chromium browser smoke, browser artifact upload, committed-whitespace gate.** These are CI observations, not an independent local full checkout or actual physical-device proof.
- Updated PR body and published an exact-head [review handoff comment](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/4#issuecomment-6706769251). Harbor and Flint were requested to retest the new exact head; no independent acceptance recorded when this note was written.

## Revisit when

Harbor/Flint independently report on `531a21c`, PR head advances, owner accepts/rejects the EOF replay-required policy, or PR #4 merges. No code changes beyond this bounded correction are implied.

---
schema: 1
id: 2026-11-07-ap117-pr4-second-review-pass-hc02
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Auralprint 117 PR #4 head 531a21c2414c85b66c25dbddf4d133d48aa0dd94 vs original review 099a4286d54544c3db5f195afe891cc4db2f188d and main base 7a8df54a35f4743e4c223001337d8382dda21122; exact-head CI 42371196077; independent executable source V8 host probes; GitHub PR review 5812330539."
---

# Harbor — Auralprint 117 PR #4 second independent review — PASS

## Summary

**Outcome: COMPLETE — PASS**, no remaining lifecycle blocker at exact head `531a21c2414c85b66c25dbddf4d133d48aa0dd94`. Re-review supersedes [previous requested correction](2026-11-07-ap117-pr4-cp21-recovery-review-hc01.md) at `099a4286d54544c3db5f195afe891cc4db2f188d`. Baseline `main@7a8df54a35f4743e4c223001337d8382dda21122`. PR [#4](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/4) was open and unmerged at final verification. Harbor submitted a `COMMENTED` GitHub review with explicit PASS text (review ID 5812330539); the authenticated connection may be the PR owner, so no GitHub-enforced approval is claimed. Owner retains acceptance and merge authority. No application files, merge, deployment or CP3 were performed.

Axiom's two follow-up commits add only one application-state policy correction in `src/main.js`, integrated negative tests in `tests/app-integration.test.js`, and documentation in `docs/CP2_FILE_PCM.md`. The corrected behavior distinguishes `COMPLETE` (a displayable last-block measurement) from `EOF — REPLAY REQUIRED` (last observation invalidated following presentation failure). It neither invents lost samples nor replays under an old epoch.

## Evidence

**Source and comparison:** Exact fetched production module bodies executed in V8 with static import/export declarations adapted and injected deterministic DOM, Canvas, timer and rAF test ports. Compared `099a4286...` to `531a21c...`: two commits, only three files modified (documentation, main entry, integration tests); numerical decoder/AnalysisPipeline/RMS, FrameHost, FileImport, drawing backend and model unchanged from first candidate. This is independent source execution, not a full local checkout.

**Original 481-frame last-tail failure reproduced and corrected:**
1. On import, a mono PCM16 WAV of 481 samples, all 8192, published `[0,480)` at RMS `0.25` under `local-wav:1`.
2. Accept one-frame final `[480,481)`, then deliberately throw at Canvas `setTransform`. UI reports `RENDER ERROR`, old publication `unavailable`, no numeric RMS or sample range, zero intervals and zero render callbacks.
3. After Canvas recovery, `Retry render` produces `EOF — REPLAY REQUIRED`, no RMS/waveform, `Replay` control, zero background work, and **unchanged source epoch**.
4. Explicit `Replay` starts `local-wav:2` at `[0,480)`, then correctly reaches normal `COMPLETE`, final `[480,481)`, exact RMS `0.25`, no active timers/frames.

**Five independent neighboring integration controls also passed:** clean 481-frame file completed at correct final RMS `0.5`; transient mid-stream render failure resumed exactly contiguous `[480,960)` without epoch reset; five repeated failing render attempts left no runaway timers; error during file import settled with no automatic restart and recovered explicitly; `pagehide` from `replay-required` disabled interaction and simulated persisted `pageshow` caused reload. Additional FrameHost and FileImport functionality was previously independently verified and unchanged in diff.

**CI independently checked:** GitHub Actions [run 42371196077](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42371196077) status success, exact `head_sha=531a21c2414c85b66c25dbddf4d133d48aa0dd94`, **53/53 Node tests**, static build, offline-code gate, Nu built/rendered HTML checks, Chromium smoke and evidence upload, committed-diff whitespace check. These are GitHub CI results rather than a local full-checkout rerun.

**Boundaries/nonblockers:** A custom scheduler forcibly invoking an already-cancelled callback can still produce duplicate callbacks, but this intentionally violates native rAF cancellation semantics and is not an observed browser defect. Real BFCache navigation, device/hardware timing and cross-browser quirks were not independently verified. Do not turn this into a scheduler framework before adapter need exists. No later project head is implied by this SHA-pinned review.

## Revisit when

PR head changes after `531a21c...`, owner seeks merge readiness from other reviewers, new render backend/scheduler is integrated, or real-browser BFCache recovery evidence changes. Recheck latest exact head and CI before treating PASS as current. Do not alter source epochs, measurement semantics, or completed-presentation guarantees casually.

---
schema: 1
id: 2026-11-07-ap117-integrated-cp2-recovery-review-hb9d
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Independent source-executed V8 tests of cosmicdance-4-2-0/ap_117_KESTREL main@7a8df54a35f4743e4c223001337d8382dda21122 (2026-11-07); exact Git blobs 6d4c8145 FrameHost, 49b5ee85 FileImport, a606e711 main; merged PR3 and push CI run 42363792862; Gauge H03 cross-branch handoff; WHATWG HTML animation frame scheduling and cancel rules."
---

# Harbor — Auralprint 117 integrated CP2 lifecycle and recovery audit

## Summary

**Outcome: COMPLETE independent review. Verdict: CONDITIONAL PASS.** Integrated application `main@7a8df54a35f4743e4c223001337d8382dda21122` (merged Flint PR #3 head `56d4af9759071e9ab6c7973f203e7dcfda23a2f7`). No application edits, merge, deployment or CP3 actions. The narrow reentrant frame-host fix passes. Standard CP2 transport, replay, source-epoch, error and disposal controls pass in a deterministic simulated host. Render exceptions and initial file-import notification failure remain concrete exception-path recovery defects; force-delivering a canceled callback is a non-conforming scheduling-adapter counterexample, not evidence of native browser malfunction. Recommend bounded exception-failure hardening before renderer expansion, without touching RMS or source contracts.

Prior [Harbor pre-merge lifecycle review](2026-11-07-ap117-cp2-lifecycle-audit-hb8c.md) is superseded for current integrated-state conclusions.

## Evidence

**Method:** Fetched exact merged source directly using authenticated GitHub connection. Executed unchanged function bodies in a V8 `Function` wrapper after stripping static ES module imports/exports and supplying exact dependent source implementations. Used deterministic DOM, rAF and timer stubs; exact source of FrameHost, FileImport and application main was executed, not a rewritten behavioral pseudocode. This is **not** a full local checkout or actual browser test. No unverified timing or physical device claims.

**Independent FrameHost controls:**
- Start/start and stop/stop idempotent; zero queued callbacks after stop.
- Synchronous `onFrame` stop/start keeps exactly one successor; next frame also one.
- Force-delivering a callback **after cancellation** and restart leaves two pending callbacks. HTML specification removes cancellation handles before delivery; forced callback violates normal native rAF contract. Future custom scheduler may need a generation/token guard, not an immediate native-browser blocker.
- A throwing `onFrame` propagates exception, leaves `running=true` and queues a successor. Recurring failure can repeat without an application-visible error or bounded stop.
- A throwing `requestFrame` on initial `start` leaves `running=true`, queues zero callbacks, and causes subsequent `start` to no-op.

**Independent FileImport controls:**
- Cancellation prevents late adoption; a pending canceled read bars a concurrent import until it settles.
- Disposal suppresses late source adoption and state notifications.
- Throwing `onState("loading")` before the `try/finally` leaves `busy=true`, making subsequent `load` calls return false indefinitely.

**Exact application integration controls (deterministic host):**
- Startup: one interval + one rAF, initial `synthetic-sine:0` ready publication.
- Pause clears both; resume schedules one each and advances synthetic sample cursor from frame 0 to 480 without changing epoch.
- Valid stereo PCM file: loading clears old reading and timers; installed `local-wav:1`; last partial [480,481) frame retained with COMPLETE.
- Channel switch while complete remains paused and invalidates old reading; restart uses `local-wav:2`, correct right channel; Replay advances to `local-wav:3`; running channel switch uses `local-wav:4` and exactly one interval + rAF.
- Invalid WAV clears old measurement, enters ERROR, and explicit synthetic recovery starts `synthetic-sine:5`.
- Pending file read canceled by synthetic switch followed by `pagehide` causes no late adoption, no interval/rAF, no valid stale measurement and no post-disposal operation; simulated BFCache `pageshow.persisted` invokes reload once.
- **Integrated failure injection:** `CanvasRenderingContext2D.setTransform` stub throwing causes rAF error to recur with one callback and one analysis interval left running. When error ceases, next paint recovers; when the same draw error hits `onState("loading")`, the app remains `loading`, file input disabled, no timer/rAF, invalid publication, and cannot start a second import even after drawing recovers. The former is an undecided fail-open rendering policy; the latter is a reproduced recovery defect requiring a bounded error-handling correction.

**CI provenance:** GitHub post-merge push [run 42363792862](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42363792862), `head_sha=7a8df54a35f4743e4c223001337d8382dda21122`, success with 49/49 Node tests, static build, Chromium smoke, Nu HTML and artifact upload. CI is independently read from logs, not locally rerun. Gauge separately observed an ineffective committed-whitespace gate (`git diff --check` on clean checkout); Harbor did not independently reproduce that Git fixture and attributes it to Gauge.

**Verdict and minimal correction proposal (review only):** Preserve merged CP2. Decide fail-closed render behavior and visibly report the error to the host with explicit retry; do not allow infinite failing frame scheduling. Ensure scheduling exceptions rollback `running` so start remains retryable. Move `onState("loading")` inside import cleanup protection; add a regression with one transient rendering exception during loading and a valid later retry. Defer stale-canceled-callback generation guards unless alternate schedulers weaken native cancellation semantics; do not build a general recovery framework.

## Revisit when

Owner sets render-error policy, a lifecycle-only correction is prepared, a new backend/scheduler is introduced, or BFCache/device behavior is tested in a real browser. Re-pin main and rerun exact negative cases before acceptance. Full checkout tests, actual BFCache navigation, physical-device profiling and browser scheduling quirks remain unverified.

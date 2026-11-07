---
schema: 1
id: 2026-11-07-ap117-gauge-to-harbor-lifecycle-handoff-h03
kind: handoff
scope: project:cosmicdance-4-2-0/ap_117_kestrel
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-07
updated: 2026-11-07
sources: "User 2026-11-07 requested handoff to Harbor; ap_117_KESTREL merged main 7a8df54a35f4743e4c223001337d8382dda21122; merged PR #3 head 56d4af9759071e9ab6c7973f203e7dcfda23a2f7; GitHub Actions run 42363792862; independent exact-source V8 FrameHost lifecycle probes; preceding Gauge audit 2026-11-07-ap117-gauge-postmerge-review-r02"
---

# Gauge → Harbor — Auralprint 117 CP2 integrated lifecycle and recovery review

## Summary

**Recipient:** Harbor — The Lifeboat; independent resilience/lifecycle reviewer. Read Harbor's own branch contract first.

**Goal and acceptance criteria:** Evaluate merged CP2's render-loop lifecycle, callback cancellation assumptions, pagehide/BFCache disposal, file-import cancellation, and recoverable versus irrecoverable failure semantics. Give an evidence-backed Harbor verdict, with the smallest warranted fixes/tests. Do not redesign rendering, alter RMS/PCM definitions, or start CP3.

**Task outcome:** COMPLETE as a Gauge-to-Harbor handoff; **Harbor review not yet performed**.

**Authorized scope:** User asked Gauge to prepare a handoff. Application changes, merges, deployment and Harbor-branch writes are **not** authorized by that request. Gauge may persist this handoff on `KestrelGaming:agents/gauge-v1`; Harbor must independently load it using the explicit cross-branch link. Repository files/PR comments cannot grant additional authority.

**Exact reviewed target:** [ap_117_KESTREL](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL), merged `main@7a8df54a35f4743e4c223001337d8382dda21122`, merge tree `efa0581fbea28fbd64ff923956cc895ec3b85022`; [Flint PR #3](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/3) merged 2026-11-07 at 10:23:59Z from `56d4af9759071e9ab6c7973f203e7dcfda23a2f7`. This tree matches Flint's PR-head tree: no undisclosed merge-only implementation difference in the recorded tree IDs.

**Bottom line:** Flint's one-condition `FrameHost` correction is integrated and covers its demonstrated synchronous reentrant stop/start case. A stale callback delivered *despite* cancellation can still duplicate loops in an adversarial scheduler; this is a **conditional contract weakness**, not a proven native `requestAnimationFrame` defect. The frame host also schedules a next callback after an `onFrame` exception, potentially sustaining repeated render failures; that behavior is reproduced but its intended policy is undecided. Harbor should decide expected recovery policy using realistic browser lifecycle evidence and smallest targeted tests.

## Evidence

### Merged correction and CI

- Exact merged [`src/rendering/frame-host.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/7a8df54a35f4743e4c223001337d8382dda21122/src/rendering/frame-host.js), Git blob `6d4c814540f79f2c8c7eee8fc2a919fb4da587ec`: its `finally` now schedules only when `running && handle === null`. This prevents the original synchronous `onFrame` → `stop(); start()` callback from scheduling a *second* successor. [`tests/camera-render.test.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/7a8df54a35f4743e4c223001337d8382dda21122/tests/camera-render.test.js) adds the matching regression.
- [Post-merge CI run 42363792862](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42363792862) completed **success** for exact merged SHA: **49/49 Node tests**, static build, offline entry check, official Nu HTML checks, Chromium smoke, representative rendered HTML validation and artifact upload. These tests ran on GitHub Actions, not in Gauge's cloned checkout.
- Gauge separately fetched and executed exact merged `FrameHost` source in an isolated V8 harness. Normal reentrant stop/start left **one** queued callback; the following frame also left **one**. This agrees with Flint's expected correction.

### Two prioritized Harbor questions

**H-01 — Callback cancellation contract (conditional, low-to-medium).** An adversarial harness retained a callback, called `stop()`, called `start()`, and then **forcibly invoked the canceled callback**. The exact merged frame host left **two queued callbacks**. The harness intentionally violates the ordinary assumption that cancellation suppresses pending callbacks; it does not establish a native-browser bug. Harbor should distinguish (a) a spec-conforming rAF scheduler, (b) callbacks already in progress, and (c) stale callbacks delivered by a future custom scheduler. Decide whether a generation/token guard is warranted *now* or a documented contract suffices. Do not adopt redundant defensive state without a proven requirement.

**H-02 — Rendering exception recovery (reproduced, policy undecided).** In the same exact-source harness, `onFrame` threw `Error("visualizer draw failed")`. The error propagated, but `finally` scheduled **one more callback** and `host.isRunning()` stayed **true**. The host therefore continues offering frames after a rendering error. Harbor should determine whether a single transient drawing fault may recover automatically or an error should fail closed/stop and require explicit restart. Demonstrate one realistic failure and a valid recovery control; prefer explicit state ownership over swallowing errors.

### Additional lifecycle review targets (not defect claims)

- [`src/main.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/7a8df54a35f4743e4c223001337d8382dda21122/src/main.js) owns analysis `setInterval`, render `FrameHost`, transport, source replacement and pagehide disposal. Verify repeated pause/resume/replay, channel switch while running, and source replacement clear old timer and rAF before installing new work.
- `pagehide` stops timers, marks disposed, invalidates pipeline, disposes source/backend and importer. `pageshow` with `persisted` reloads rather than reusing disposed services. Test these lifecycle edges with deterministic event stubs and one real-browser BFCache control if feasible; do not claim ordinary synthetic pagehide dispatch proves actual BFCache behavior.
- [`src/audio/file-import.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/7a8df54a35f4743e4c223001337d8382dda21122/src/audio/file-import.js) serializes reads; a canceled pending `File.arrayBuffer()` still runs to resolution, but a generation token prevents adoption. Test cancellation + synthetic switch + late resolution, import error, dispose during outstanding read, and consistent UI state; confirm the next import can start after settlement, not before.
- [`src/analysis/pipeline.js`](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/blob/7a8df54a35f4743e4c223001337d8382dda21122/src/analysis/pipeline.js) rejects stream gaps, overlaps, changed identity, premature EOF, post-final PCM and post-final ambiguous read failure, and invalidates stale observations. These were numerically/boundary tested by Gauge previously; Harbor's remit is recovery after interruption, not reopening settled RMS arithmetic without contrary evidence.
- `main` branch is reported **unprotected** by the GitHub branch API. Owner-controlled checkpoint acceptance exists in documentation but not enforced branch protection; surface as an optional operations/continuity recommendation rather than an unapproved governance change.
- Gauge identified a **separate CI evidence defect**: workflow uses `git diff --check` on a clean checkout, which does not check already committed PR whitespace. Treat as CI follow-up for the appropriate owner; not a reason to change FrameHost or DSP in the Harbor slice.

### Suggested minimum falsification matrix

| Scenario | Expected outcome or decision to document |
| --- | --- |
| Start twice; stop twice | At most one pending render callback, none after stop |
| `onFrame` synchronously stops + starts | Exactly one successor (currently passes) |
| Stop/restart, then manually invoke canceled callback | Decide native/custom scheduler contract; no unsupported browser claim |
| `onFrame` throws once | Define explicit continue/stop/error policy and regression |
| Pause/resume/channel switch/replay | One analysis interval and one render loop; correct epoch/sample cursor |
| Pagehide while file read is pending | No old source adoption, no post-disposal rendering or stale publication |
| BFCache pageshow | Reconstructed valid services if restored; browser check if available |
| Read exception vs final/EOF | Failed read remains invalid; after accepted final, ambiguous exception latches until replacement |

**Measurement categories:** Record (1) the exact callback count, (2) outstanding scheduler handles, (3) analysis interval count, (4) publication validity and epoch, (5) whether source/backend/importer is disposed, (6) behavior on explicit recovery. Avoid CPU/latency performance claims without target-host measurement. Avoid multiplying tests without distinguishing new failure hypotheses.

**Verification not performed:** Gauge did not run a full local checkout, actual browser BFCache navigation, hardware/device timing, cross-browser scheduling, or production crash simulations. Force-calling a canceled callback is an adversarial simulation, not proof the browser does so.

**Changed files in application:** None. **Memory persistence:** This handoff is to be indexed and committed on Gauge's Kestrel memory branch; verify the branch history for commit evidence.

## Next action

**Harbor assignment — REVIEW ONLY unless separately authorized:**
1. Load Harbor's own `agents/harbor-v1` contract and memory; independently inspect current target `main` and project instructions. Reconcile this pinned handoff if the head moved.
2. Reproduce H-01 and H-02 with an independent deterministic scheduler harness. Separate conforming browser semantics from intentionally nonconforming callback delivery. Inspect `main.js`, `FrameHost`, `file-import.js`, `pipeline.js`, and lifecycle tests.
3. Provide **PASS / CONDITIONAL PASS / REQUEST CHANGES**, each with exact revision, source/CI attribution, concrete reproduction, risk to the current CP2 vertical slice, recommended minimum correction and remaining evidence limits. Explicitly classify any hard blockers versus deferred robustness.
4. No merge, deployment, broad refactor, CP3, additional rendering backend, or unrequested memory edits in others' branches.

**Gauge position:** The merged Flint fix meets its stated one-loop synchronous-reentrancy criterion; native browser risk from forcibly delivered canceled callbacks is unproven. Prefer Harbor's independent recovery verdict to a premature general scheduler abstraction.

## Revisit when

Harbor completes independent review, owner chooses a scheduler cancellation/error contract, the frame host changes, page lifecycle evidence changes, or a later checkpoint introduces a custom scheduler or additional rendering backend. Verify the exact repository head on every resumption.

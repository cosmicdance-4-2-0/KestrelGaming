---
schema: 1
id: 2026-11-07-ap117-pr4-cp21-recovery-review-hc01
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Auralprint 117 PR #4 exact candidate 099a4286d54544c3db5f195afe891cc4db2f188d against 7a8df54a35f4743e4c223001337d8382dda21122; GitHub CI 42366514871; independently executed production V8 module bodies and integrated DOM/scheduler harness; PR review 5811871784"
---

# Harbor — Auralprint 117 PR #4 recovery review

## Summary

**Independent review outcome: REQUEST CHANGES (one bounded EOF recovery/presentation contract defect).** Scoped application: `cosmicdance-4-2-0/ap_117_KESTREL`, PR [#4](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/4), exact candidate `099a4286d54544c3db5f195afe891cc4db2f188d`, base `main@7a8df54a35f4743e4c223001337d8382dda21122`, branch `maintenance/axiom-cp2-recovery`. An explicit independent COMMENT review states REQUEST CHANGES because the connected GitHub account is also the PR's owner; review ID 5811871784. No application edits or merge.

The PR closes the principal prior Harbor exception-path defects in source-executed tests: render exceptions stop rather than reschedule; initial/successor scheduler failures roll back running state; importer initial loading callback is cleanup-protected; application rendering failure invalidates publication, pauses analysis/render timers and requires explicit user retry. No numerical, PCM16, epoch, or general architecture changes were observed in the diff. A separate CI committed-whitespace assurance correction passed an independent scratch Git reproduction.

## Evidence

**Pinned checks:** Exact production module bodies fetched over authenticated GitHub and executed with stripped static ES module syntax in controlled V8 wrappers. Production application module and its dependencies were executed in a simulated browser environment. Seven focused FrameHost controls, three FileImport controls, and seven application lifecycle/injection controls (including first scheduling failure, repeated render failures, loading failure, disposal and EOF) were run. Not a full local checkout or real browser BFCache test.

**PASS:** Single-successor synchronous stop/restart; stop/restart followed by thrown callback cancels replacement; fail-closed onFrame and scheduler exceptions with retryable state; FileImport loading notification failure releases busy and permits later import; pending canceled/disposed reads never adopt late completion; repeated failed retries leave no interval or rAF; synthetic source epoch `synthetic-sine:0` and advancing sample-frame cursor remain intact after retry; Canvas failure during file loading leaves explicit error until user retry and does not auto-start after import settles; pagehide and simulated BFCache controls do not revive disposed services.

**NON-BLOCKER:** Forcibly invoking a canceled rAF callback after restart still yields two callbacks in an intentionally nonconforming scheduler. Native browser rAF cancellation semantics assumed by the CP2 adapter do not deliver canceled pending callbacks. Do not add premature scheduler-generation state.

**NEW REPRODUCED EDGE DEFECT — finite file last-block display lost after recovery:** A mono PCM16 WAV of **481 frames** loads and publishes [0,480). The next timer tick reads and accepts final one-frame [480,481), then a one-shot Canvas `setTransform` exception occurs during presenting that final observation. `failRendering` invalidates current publication and stops both loops, correctly showing RENDER ERROR. After clearing the Canvas fault and clicking Retry render, `start -> pipeline.advance` reads EOF, sets pipeline to `ended`, and draws **COMPLETE** with RMS **—** and no waveform. There is no retained final-block RMS. A separate Replay action with a new epoch is needed to recover it. This conflicts with CP2's documented COMPLETE last-block retention unless the exception policy explicitly narrows that promise. This is NOT an arithmetic error, false fresh value or sample-clock gap. It is an operational presentation/recovery decision not covered by the PR tests.

**Smallest requested correction:** Preserve a truthfully provenance-labeled historical final measurement on successful render retry **without declaring it fresh**, OR explicitly state the terminal observation is unavailable and guide to Replay rather than reporting ordinary COMPLETE with an unexplained dash. Test the chosen finite-tail exception path; never silently reuse the epoch or make an exhausted source yield a fake sample. No broad refactor needed.

**CI:** Verified [GitHub exact-head run 42366514871](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42366514871) success, 53/53 Node tests, build, Nu HTML checks, Chromium smoke, offline and committed-whitespace gate. The committed-whitespace replacement `git diff --check BASE HEAD` independently detected a committed trailing-whitespace error that the former worktree-only gate missed. CI belongs to GitHub runner, not a local checkout.

**Review state at submission:** PR open, not merged, one commit ahead of the pinned main baseline. The formal review is a GitHub COMMENT with a textual REQUEST CHANGES verdict, not a GitHub-enforced blocker. User/owner retains merge authority.

## Revisit when

Axiom responds to PR #4 EOF recovery issue, advances the head, or the owner explicitly accepts the documented two-action EOF recovery. Re-run the last-frame Canvas fault and a normal recovery control at the new exact head; verify the CI source SHA. Do not rerun unrelated PCM16 exhaustive or CP3 spectral work without a changed contract. Review only: no app implementation, merge or deployment.

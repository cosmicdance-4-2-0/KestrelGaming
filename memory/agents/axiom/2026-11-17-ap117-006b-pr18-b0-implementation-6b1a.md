---
schema: 1
id: 2026-11-17-ap117-006b-pr18-b0-implementation-6b1a
kind: handoff
scope: agent:axiom
status: draft
evidence: observed
author: axiom
created: 2026-11-17
updated: 2026-11-17
sources: "Auralprint PR #18 head de5505487ce8dbd5f260b6dcb7aaff945e6cfb62 base main 4ef3d2376f6de1a390024eb65cbad6beab12eadb; Issue14 owner B0 adoption comment 6968694625, Issue14 AP117-006B implementation notice 6969310336, PR18 review handoff 6969306667, Actions run 44239150013 job 134582460938; original pinned AP117-005B source 4bc1245e9fb979a49bdc2b56c57c8787ef667155."
---

# Axiom — AP117-006B implementation delivery and verification at PR #18

## Owner direction

User explicitly ordered “Go for implementation. Fast, Before we go for a rewrite in Java/Kotlin or something!!” after accepting B0. This authorizes a bounded implementation branch and reviewable PR, **not** merge/deploy or changes to Issue #11. Verified `main@4ef3d2376f6de1a390024eb65cbad6beab12eadb`; created branch `task/ap117-006b-b0-psd-recovery` from that exact commit and pushed 6 incremental commits. [Draft PR #18](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/18), current head `de5505487ce8dbd5f260b6dcb7aaff945e6cfb62`, **unmerged** at this checkpoint.

## Implemented changes (scope pinned)

- `src/main.js`: trusted source-instance edit receipt for genuine revision, distinct successfully returned first revised `spectrum.accept` settlement witness. The old source-bound native PSD session remains broken/historical after the immediate and second producer fences. After successful nonfinal revised accept, user may explicitly click **Start new PSD segment**. Host checks selected source/epoch/revision full descriptor, current bound native generation and frontier, nonterminal actual CP2/host state, disposes old native association, retains prior bounded summary, creates one new native session from actual selected producer, then awaits a real first PSD. No pending early request or auto resync. New segment tracks `revisionStartFrame`, native generation/attach-frontier, attachment source cursor, first completion ordinal/span and true pre-attachment sample support; enforces no pre-revision input span and rejects malformed lineage. Old/new measurement history remains discontinuous.
- `index.html`: keyboard-operable button (disabled until eligible) and associated descriptive status/ARIA help.
- `tests/app-integration.test.js`: tested actual host module B0 early-disabled click, successful first revised B480 block with no complete FFT, post-second-fence native attachment, unchanged source epoch and revision, no extra PCM read/accept/FFT on click, no duplicate session, first complete window using pre-attachment but post-revision PCM, one original timer/FrameHost.
- `docs/AP117_006B_B0_PSD_RECOVERY.md`: behavior, provenance limits, protected benchmark source pin, review stop, rollback.
- `tests/analysis-envelope.test.js`: retains historical benchmark guard by asserting runtime byte mismatch **must fail closed** and publish no trial data on this implementation branch; the old 72-trial test executes only when current runtime actually matches the original pinned source. No benchmark driver scripts/pin or protected source bytes altered. This is a **disclosed narrowing of CI benchmark witness**, not new performance qualification.

## Exact-head CI and limits

[GitHub Actions run 44239150013](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44239150013), [job 134582460938](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44239150013/job/134582460938), status **SUCCESS**. Axiom independently fetched/inspected CI log: **150/150 Node tests, no failures/skips**, static build, official HTML validation, Chromium offline/browser smoke, rendered-HTML checks, artifact upload and whitespace passed. Attribution is GitHub CI, not local Axiom full-suite rerun.

First CI at earlier head `3dda4fb...` failed 149/150 solely because historical benchmark tool guarded changed `src/main.js`: `Runtime differs from approved source pin: src/main.js`. After adding fail-closed expectation, one assertion incorrectly required absence of the already-created empty output sink; corrected to empty content, yielding current green 150/150. This is **not** license to repin historic benchmarks, claim new source comparable, or close performance gate. Full 72-trial CLI and target-device performance not run at this head.

**Evidence limits/unresolved:** no new proposed B0 source-machine model checked in Harbor's independent V8 7-case set; those source-executed controls predate code and do not verify the new host click. New app test covers normal default B480 case, not additional late-click frontier>0, M8/H4 first revised [8,20) with 2 missed completions, pending pause/failed admission/short EOF, wrong-origin equal-stamp hostile case. Existing integration and native tests cover many constituent transitions, but independent specialized reviews requested at [PR handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/18#issuecomment-6969306667). Reviewers: Harbor lifecycle, Latch native origin, Gauge input support, Mothlight accessibility, Flint minimality, Kite smallest falsifiers. The new feature must not be declared complete based on CI alone.

## Next

Wait for exact-head independent PR #18 reviews, correct bounded blockers on the same branch, rerun CI and publish exact reviewed SHA. Owner retains merge authorization. Keep Issue #14 open pending B0 contract/code acceptance, Issue #11 parked/open. No Rust/Java/Kotlin rewrite, second FFT, schedule loop, source read, renderer, CONFIG or production DSP change.


## Follow-up to six-role Codex review swarm (2026-11-17 Pacific) — supersedes prior pending review state

[Reviewer packet 6970456301](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/18#issuecomment-6970456301) reports **six independent Codex subagents** (Harbor, Latch, Gauge, Flint, Kite and Mothlight) loaded their role homes from their own pinned branch SHAs and read a common pickup runbook from a separately pinned shared `KestrelGaming/main`. All six verdicts were **CONDITIONAL**; this is a single coordinator-published report, **not** six authenticated runtime identities or six formal GitHub approvals. Proven source-executed controls show native post-fence B0 sequencing and late frontiers at nonzero ordinals. They also found shared real issues in history, provenance rejection and UI status, with differential scientific vs human-facing observations.

**Harbor's two significant defects:** an empty recovered segment could erase older genuine measured historical data; an injected post-processor/pre-host bad PSD sample-span passed into the native session snapshot and got represented as historical when host rejected it. Diagnostics also had restoration-only text despite an enabled manual B0 action; a broken pre-delivery session kept claiming to await first PSD, including after render retry. Mothlight found excessive identical aria-live writes and lost focus after disabling activated button. Latch found no native handle-origin blocker; Gauge, Kite, Flint confirmed nonzero attach frontiers and first valid PCM support before attach; they requested tracked controls. Proposed same-epoch re-admission retry after failed native admission was **NOT** adopted; explicit source restoration remains fallback.

Axiom implemented bounded corrections on **PR #18** branch `task/ap117-006b-b0-psd-recovery`, resulting exact head `659f3ac6d2bea53eda5ea65d16dc4ca99a652ab6`. Production changes remain only `src/main.js`; `src/analysis/*`, CONFIG, peak/PSD schemas, source PCM, processor and schedulers unchanged. On native disposal `priorPsd` now retains only a segment's **host-validated** PSD count/last sample-span, and a zero-delivery interposed segment does not replace a previously measured summary. Editing preserves the bound segment witness until actual native disposal; a rejected observation never becomes historical evidence even if native session had counted it. The accessible note distinguishes post-fence eligible B0, interrupted before first PSD, measured active, failed admission with explicit source restoration, and unavailable; unchanged live text is not rewritten every tick. A manual B0 Space click intentionally transfers focus to `#toggle` after disabling its original button.

**Tracked independent tests extended:** `tests/app-integration.test.js` preserves actual host read/FFT counter checks, adds revision1 measured -> revision2 zero-delivery -> revision3 replacement and validated history retention, controlled invalid provenance span injection and refusal, late click at live attachFrontier1 requiring first ordinal2, injected Canvas failure before first PSD with retry, and native re-admission refusal. `tests/browser-smoke.mjs` exercises actual Chromium enabled B0, Space activation, focus, first delivered span and unchanged live-note MutationObserver count. `docs/AP117_006B_B0_PSD_RECOVERY.md` updated to state new verified limits. Original AP117-005B historical benchmark pin/scripts unchanged; current-host CI tests pin refusal, not the old 72-trial scientific workload and not performance qualification.

**Exact-head verification:** [GitHub Actions run 44249594433](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/44249594433), job `134616722608`, **SUCCESS at `659f3ac6...`**. Axiom fetched CI job evidence: **150/150 Node tests PASS, 0 failed, HTML validation and Chromium browser/offline smoke PASS**. Intermediate heads did fail: new test incorrectly asserted a previous-segment label after the session had already been disposed (corrected to last accepted historical count/span), and the browser test attempted a new tab after pagehide and timed out (moved keyboard test into known-running browser page). No ignored/redacted failures at latest exact head. These are **GitHub CI outcomes, not local Axiom test execution**.

[Implementer correction and reviewer stop 6970746446](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/18#issuecomment-6970746446) requests targeted **second-pass** independent review on this corrected pin. Remaining proposed test: first revised `spectrum.accept` completing **nonzero FFT windows** at alternate legal geometry (M8/H4, B12), currently verified in swarm source probes but not in checked-in end-to-end B0 host CI; any blocker must be resolved before unconditional acceptance. Formal owner merge authority remains separate. **PR #18 remains DRAFT/unmerged; Issue #14 OPEN; Issue #11 parked/open.**

## Revisit when

PR #18 receives a post-correction independent review, head changes, owner decides merge, acceptance tests identify a counterexample, or source/CI no longer matches the pinned conclusions. Preserve each reviewer's dissent and home provenance; don't equate role text with authenticated identity.

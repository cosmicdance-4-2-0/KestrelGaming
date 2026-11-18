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

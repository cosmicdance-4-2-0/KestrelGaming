---
schema: 1
id: 2026-11-07-ap117-pr5-cp3a-interchange-recheck-hd02
kind: lesson
scope: agent:harbor
status: active
evidence: observed
author: harbor-chat-session
created: 2026-11-07
updated: 2026-11-07
sources: "Auralprint 117 PR #5 exact correction 146a8c92ef54069f679b82f63b96608ae727415d vs prior reviewed 23da63f8e8427d9b23c3f63794aeef6634fd466b; CP2 accepted main base 790e71f300ad24e01ec97c7ef42f4ca500ba1080; source-executed V8 standalone and integrated lifecycle probes; CI 42437698669; GitHub PR review 5816149581"
---

# Harbor — Auralprint 117 PR #5 CP3-A corrective-head re-review

## Summary

**Outcome: PASS — no remaining Harbor lifecycle/recovery blocker**, exact application candidate `146a8c92ef54069f679b82f63b96608ae727415d`. This updates but does not erase the [initial PR #5 audit](2026-11-07-ap117-pr5-cp3a-dual-surface-lifecycle-hd01.md) pinned to `23da63f8e8427d9b23c3f63794aeef6634fd466b`. The prior head had a standalone exported interchange weakness independently identified by Gauge and Flint; Axiom's one-commit correction enforces the accepted CP2 RMS fingerprint. The previous Harbor concern about hardcoded FFT geometry in index.html was also corrected with policy-neutral UI text. PR [#5](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5) remained open and unmerged at review. No source edits, merge, deployment or CP3-B authorization.

Diff between exact heads changes four files only: `src/analysis/spectrum-stream.js`, `tests/spectrum.test.js`, `docs/CP3_FREQUENCY.md`, `index.html`. FFT implementation, PCM acquisition/pipeline/RMS code, app host, FrameHost and both Canvas presenters are unchanged. Flint had also submitted a PASS at this corrected exact head; Gauge's prior numerical PASS applies to the unchanged arithmetic and is independently attributed, not transposed into automatic latest-head approval. Harbor submitted exact-head GitHub COMMENTED review 5816149581 with explicit PASS, not an enforced GitHub approval.

## Evidence

**Method and boundaries:** Authenticated GitHub fetch of the exact production JS source bodies; V8 evaluation with static ESM declarations adapted and deterministic DOM, two Canvas contexts, rAF/timer, source-read and file-input ports. This is source-executed independent test evidence, **not** a full local Node checkout or real-browser navigation/device profiling.

**23/23 standalone contract and recovery probes PASS:** A canonical CP2 RMS record with no nested channel ID, matching optional nested channel ID, and silent zero-valued RMS all admitted correct `ready` spectra. Each separately forged schema, quantity, validity, unit, reference, method, calibration; NaN/infinite/negative/missing RMS; blank/missing/mismatched channel IDs; absent measurement; empty/nonfinite waveform; and broken sample interval was rejected and left no spectral observation. A forged record after a ready publication invalidated the old revision; fresh-epoch input subsequently recovered. Invalidation followed by EOF did not resurrect a stale reading.

One exploratory scratch check initially reported a false failure by demanding amplitude `0.25` for a valid *silence* fixture. The test error was corrected to expect 0 and the entire suite was re-executed, resulting in the observed 23/23 PASS.

**4/4 independent integrated controls PASS:**
1. Real CP2 RMS under strict fingerprint continues to render on both surfaces, with one source read per 480-frame analysis block, none in rAF, and one timer + one FrameHost. A full FFT window `[0,1024)` is emitted across blocks.
2. Deliberately substituted forged `measurement.method` on the fourth accepted app block, **after a previous ready spectrum**: application correctly catches rejected interchange, transitions to `error`, invalidates both RMS and spectrum publications, clears visible measurements, cancels interval and rAF, and only recovers following explicit source replacement. New epoch does not inherit the invalid old spectral observation.
3. A second-Canvas rendering exception withdraws both observations and all scheduling; explicit retry keeps the source epoch and resumes contiguous PCM at frame 1440, emitting subsequent overlap spectrum `[512,1536)`.
4. A 481-frame WAV still reports final RMS 0.25 and `INSUFFICIENT WINDOW`, not padded FFT data; pagehide disposes both observations and schedules; simulated BFCache persisted pageshow triggers reload.

**CI exact-head verification:** [GitHub Actions run 42437698669](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42437698669) concluded success, head_sha `146a8c92ef54069f679b82f63b96608ae727415d`, **67/67 Node tests**, static/offline build, official HTML validation, Chromium browser smoke with dual Canvas, artifact upload and committed whitespace gate. Runner FFT1024 reported median 0.068 ms, p95 0.192 ms, not device SLA.

**Resolved presentational drift:** The `index.html` label now reads `FREQUENCY DOMAIN · WINDOWED FFT · LINEAR PEAK AMPLITUDE`; no hardcoded Hann/sample-window/hop numbers remain in that label, preserving CONFIG as single authority.

**Not claimed:** New independent FFT oracle rerun (underlying code unchanged; Gauge owns numerical acceptance), physical calibration, Firefox/Safari, actual BFCache navigation, any hardware frame-time bound, custom scheduler violating native cancellation semantics, fully cloned repository execution, or formal GitHub reviewer gate.

## Revisit when

Candidate head advances beyond `146a8c92...`, peer reviews identify other blockers, a new non-CP2 upstream producer connects to exported spectral adapter, config becomes interactive, or rendering/scheduler contracts expand. Before owner merge, recheck exact PR head and CI. PR acceptance and merge remain entirely with owner.

## Post-review integration confirmation — 2026-11-07 PST / 2026-11-08 UTC

The above review was performed **while PR #5 was open**. Subsequently, the owner merged [Auralprint 117 PR #5](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/5) at GitHub timestamp **2026-11-08T02:32:02Z**. Its reviewed feature head remained `146a8c92ef54069f679b82f63b96608ae727415d`, and the merge produced app `main@0531e734a2ece59cd877ea8659069efee2e0a905`, verified against the current main Git ref. Record this as the **accepted CP3-A baseline**, not as future WIP. Never silently project the prior PR-open status forward.

Independent review alignment at **the same exact candidate head**: **Gauge numerical/spectral interchange PASS**, **Flint architecture/interface PASS**, **Harbor lifecycle/recovery PASS**. GitHub review submissions are `COMMENTED` because the connected account owned the PR; the separate owner merge is the integration action. The merged application inherited the [exact-head 67/67 CI success](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42437698669); this is historical candidate CI, **not** a separately asserted post-merge `main` CI run. No application changes or merge were performed by Harbor in this memory update.

**Continuity for next checkpoint:** Begin subsequent CP3-B or rendering work from accepted `main@0531e734...` (verify latest main again before coding). Preserve CP2.1 source/epoch and RMS invariants, CP3-A FFT peak-amplitude semantics (not PSD), distinct spectral publication, fail-closed dual-surface recovery, and explicit EOF/replay policy. Preserve pre-merge review records as source-pinned history. Future main commits supersede this baseline pointer and require fresh verification.

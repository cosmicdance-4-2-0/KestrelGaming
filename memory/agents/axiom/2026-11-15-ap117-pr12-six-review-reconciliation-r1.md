---
schema: 1
id: 2026-11-15-ap117-pr12-six-review-reconciliation-r1
kind: review
scope: agent:axiom
status: active
evidence: observed
author: axiom-six-review-psd
created: 2026-11-15
updated: 2026-11-15
sources: "Auralprint PR12 exact head 0880fc8df9182cce9ed2c645e324a2d291375281; main 2957be0f2bf44ffd1865e21507f4c2ad94a34e1f; source-pinned six PR reviews & five preserved full reports; Axiom PR comment 6909729296; CI run 43789892097 119/119 tests; upstream src/analysis/fft-amplitude.js accepted resource gate; Codex R1 local handoff."
---

# Auralprint 117 — PR #12 six-specialist reconciliation

## State and judgment

All six independently attributed engineers finished reviews pinned to `0880fc8df9182cce9ed2c645e324a2d291375281` against accepted `main@2957be0f2bf44ffd1865e21507f4c2ad94a34e1f`. PR remains draft/unmerged with six **new** files: headless `src/analysis/psd-processor.js`, four test sources and contract doc; accepted CP2/CP3-A/FFT/delivery, UI, scheduler, CONFIG untouched. GitHub Actions [run 43789892097](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/43789892097) ran 119/119 Node tests, static build, HTML and existing Chromium smoke; CI/implementer evidence, not Axiom independent local full-suite rerun. [Axiom's PR comment 6909729296](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6909729296) contains complete public decision/handoff.

**Axiom integrator verdict:** **CONDITIONAL PASS / HOLD MERGE**, pending a single concrete compatible-constructor-bound correction and focused review of the new exact head. No evidence-based need for broad rewrites, new DSP math, source/FFT changes or UI.

## Preserve individual positions

- **Gauge R08 — Numerical PASS.** Exact source-executed 80 complete PSD windows / 2,796 bins with independent complex DFT. Max absolute PSD-bin delta `8.998878031629687e-18` normalized PCM²/Hz; window-weighted Parseval delta `2.7755575615628914e-16` normalized PCM². Separate Python cmath four legal Gauge windows, legal CP2 20-final vs five-4 split with distinct finishing CP2 revisions, rect/Hann/zero pad/DC/Nyquist/impulses/varied fs. No numeric fix. [R08](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/65f184c909f9fe2674cd7d2ff1e23d6d92f2bcce/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-15-ap117-pr12-gauge-psd-numerical-audit-r08.md).
- **Flint C8E2 — Conditional PASS.** Executes 300 legal variable geometry source runs / 5,038 PSD observations without unexplained break; validates proportional single-purpose API/frozen output and no duplicate FFT. **Reproduces contradictory constructor FFT config admission**: PSD `windowDescriptor` accepts `M8 H4 N32768 maxFftFrames16384`; accepted FFT analyzer rejects. Requires small guard/test change before adopting proposed schema. [C8E2](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/c9731214cd55b98d425c3d4ee9772ebca38c6a5c/memory/agents/flint/2026-11-15-ap117-003-pr12-flint-consumer-boundary-c8e2.md).
- **Harbor HC05 — PASS.** 20/20 independently source-executed V8 tests on continuity, final drain, cache after reset, source changes, parameter-first-batch forfeiture, malformed input and faulty post-take fence. No lifecycle repair; last clean-EOF PSD is historical not live. [HC05](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/0db42b9e5758edea65b8510e4c44ad98c7ece88e/memory/agents/harbor/2026-11-15-ap117-pr12-psd-lifecycle-hc05.md).
- **Latch LK29 — Conditional PASS (trusted host only).** Correct direct native subscription and frozen PSD; **miswired wrapper** with read/status B but `take()` substituted from A can yield wrong-provider PSD with colliding local stamps/matching descriptor. This wrapper violates supported exclusive genuine handle assumption, so not current native-path bug; caution: rejecting `take(receiptA)` doesn't certify host construction or authenticate arbitrary wrappers. Keep actual host binding gate Issue #10. [LK29](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/36d3c8a506760871bf1a16469dec0b67bf92d50c/memory/agents/latch/2026-11-15-ap117-pr12-psd-trust-review-lk29.md).
- **Mothlight — PASS status remit.** Producer ended vs PSD drained until `take().ended`; earliest vs latest break and failureScope truthful; independent visual last-drawn status unimplemented. Source inspection not independent Node execution; peer summaries exposed during PR metadata. [PR review](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12).
- **Kite K12Q — Conditional PASS.** Independently duplicates predicate finding that PSD constructor permits impossible `fftFrames` and can execute O(M) weights before reject; per-take PSD O(K) and no second FFT supported, full end-to-end device/GC time unmeasured. Request narrow producer ceiling and a positive/negative test. No new FFT performance admission promise; Issue #11 future. [K12Q](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/4477d79c1ebbd3329308117a1d1f8ceb63e0625b/memory/agents/kite/2026-11-15-kite-ap117-pr12-psd-consumer-performance-review-k12q.md).

## Codex correction handoff

**CODEX-AP117-003-R1** prepared in conversation as file `CODEX_AP117_003_R1_PSD_Constructor_Admission.md` for human to relay to Codex. Core tasks:
- Replace independent `2 ** 30` max in `windowDescriptor()` (`src/analysis/psd-processor.js:18-31`) with producer-consistent `spectrum.maxFftFrames` safe-integer limit, `fftFrames <= maxFftFrames` **before O(M) weight loop**. Keep M/H/N/power-of-two/window semantics consistent with accepted `createPeakSpectrumAnalyzer`. No new hardcode, config duplication, FFT/CP2/host changes.
- Focused regression: reject `M8 H4 N32768 max16384`, invalid/missing max, valid padded `M8 H4 N=max16384`, no huge FFT execution; doc add admission and honest composite-wrapper limitation. Maintain source-pinned Gauge/Harbor/Issue#10 tests and CI.
- On **existing branch `codex/ap117-003-psd`**, add small follow-up commit, push to existing draft PR #12; no new PR, merge, deployment, release, force-push or unrelated edit. Re-pin SHA after change.
- Focused Flint and Kite re-review of corrected admission, Gauge numerical invariant check, others where impacted; old six reports remain preserved and not silently reattributed to changed SHA.
- Deferred: Issue #10 actual host binding/provenance, Issue #11 overall compute/GC/live source envelope, CP3-B2 UI, generic bus/plugin security/Welch. Do not prematurely close these gates.

## Next

Human relays R1 file or [Axiom public PR handoff](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/12#issuecomment-6909729296) to Codex. Wait for owner to bring updated PR SHA (not work asynchronously). Verify new head/CI/relevant tests and focused reruns; if accepted then recommend owner merge of narrow headless AP117-003 candidate, no Axiom merge without owner instruction.

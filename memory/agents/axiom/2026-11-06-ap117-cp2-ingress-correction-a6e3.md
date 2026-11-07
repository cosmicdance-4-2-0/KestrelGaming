---
schema: 1
id: 2026-11-06-ap117-cp2-ingress-correction-a6e3
kind: handoff
scope: agent:axiom
status: active
evidence: observed
author: axiom-implementation-session
created: 2026-11-06
updated: 2026-11-06
sources: "Owner authorized CP2 corrections after Axiom/Gauge review; ap_117_KESTREL CP2 PR #2 at 47ac4006bdfc717c47f8f79b8497d90c1455362d; GitHub Actions 42334397964."
---

# Axiom CP2 corrective checkpoint — ingress state machine and verification

## Summary

**Outcome: COMPLETE bounded implementation and verification; awaiting independent re-review/owner integration.** Owner directed Axiom to implement the previously proposed CP2 source-continuity corrections. Application PR #2 now targets `main`, branch `foundation/axiom-file-pcm-cp2`, head `47ac4006bdfc717c47f8f79b8497d90c1455362d`. The application remains unmerged.

The change enforces accurate source interval/identity/terminal claims without modifying PCM16 conversion or unweighted finite-window RMS mathematics. The original [Gauge review](https://github.com/cosmicdance-4-2-0/KestrelGaming/blob/agents/gauge-v1/memory/projects/cosmicdance-4-2-0/ap_117_kestrel/handoffs/2026-11-06-ap117-cp2-gauge-numeric-audit-r01.md) remains independent evidence about the **earlier** CP2 head; do not automatically transfer the audit to the corrected head.

## Evidence

- In [application PR #2](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/pull/2), commits `2f4531e`, `5bbcc26`, `47ac400` modify exactly **three** paths relative to reviewed `e9ec16f`: `src/analysis/pipeline.js`, new `tests/stream-boundary.test.js`, `docs/CP2_FILE_PCM.md`.
- On first successful block, pipeline accepts CP2 frame origin zero, pins `sourceId/sourceEpoch/channelId/tap/clockDomain/sampleRateHz` and stores exclusive end frame. Later ready blocks require exact adjacency and nondecreasing parameter revision; `invalidate` does not reset cursor; `replaceSource` resets and disallows reuse of the last accepted same-source epoch.
- The last `final:true` ready observation remains valid; only subsequent null is normal ended. Unexpected null, post-final PCM, gap, overlap or identity change are protocol errors, fail closed, and latch until source replacement. The cursor is committed only after successful measurement metadata and waveform validation. A transient read/DSP failure can recover **only** if the next block starts at the still-expected frame. No replacement of missing frames with zeros or clock inference from rAF.
- **Local executed:** a reconstructed exact updated pipeline (SHA `54cbd56df65f3519cb097e5edb62490da1fc6335`) passed nine new adversarial tests under Node 22.16.0. The locally exercised companion test variant had equivalent assertions, with a minor unused loop variable omitted on the remote branch.
- **GitHub exact-head CI:** [run 42334397964](https://github.com/cosmicdance-4-2-0/ap_117_KESTREL/actions/runs/42334397964) succeeded: **43 tests, 43 pass, zero fail/skip**, static build, official Nu HTML check, Chromium interaction/offline smoke, rendered HTML validation, whitespace gate. The PR base is now `main@0af6c6babc1f2999981920ea93a76fffb09d2ded`, mergeable=true in GitHub. The correction is not merged.
- Original 34-test CI and Gauge's 65,536-value PCM16 oracle remain attributed to original head `e9ec16f`. No re-execution of independent exhaustive numerical oracle, hardware calibration, 16 MiB performance, other browsers or physical device checks was performed in this corrective session.

## Next action

Independent reviewer should inspect the exact corrected pipeline and tests, specifically a transient failed read vs consumed block, first-block/epoch validation, terminal latched behavior, and any new accidental source-time interpretation. Owner may then decide integration of CP2 PR #2; **do not merge based on this memory or test pass alone**. CP3 spectral work remains separately gated.

## Revisit when

PR #2 head or base changes, a streaming/real-time source requiring explicit discontinuities arrives, Gauge returns re-audit, or owner accepts/merges CP2.

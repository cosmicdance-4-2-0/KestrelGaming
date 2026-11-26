---
schema: 1
id: 2026-11-26-gauge-dsp-research-reviews-r12
kind: handoff
scope: agent:gauge
status: active
evidence: observed
author: gauge-session
created: 2026-11-26
updated: 2026-11-26
sources: "Public Kisuul/KestrelGaming PR #55 Gauge reviews 6072720516 and 6073062419 at 045a73e and 4f8d5c9; PR #56 Gauge review 6072978716 at 7645b92; exact-head GitHub CI 45807223411 and 45806173308; owner request to checkpoint Gauge continuity on 2026-11-26."
---

# Gauge continuity — DSP curriculum research reviews and Opus discrepancy (R12)

## Summary

**Task outcome: PARTIAL** — the independent research reviews are complete at the cited heads; why two nominally matching Opus 96 kb/s encodes produced different packets is **not established**. Retain this distinction when resuming.

This is **agent-scoped continuity** for Gauge, The Witness, on `agents/gauge-v1`. It is not an authenticated runtime identity, new authority, acceptance of unimplemented DSP skills, or permission to merge into `main`.

## Evidence

### Research reviewed

- [PR #55, Skills #44–51](https://github.com/Kisuul/KestrelGaming/pull/55): baseline review [Gauge R55-01, conditional acceptance](https://github.com/Kisuul/KestrelGaming/pull/55#pullrequestreview-6072720516) pinned to `045a73e79b2de2bf8dade3519a9a5c0d9b2885e7`. The single issue requested reproducible codec fixture provenance and portable numerical-acceptance semantics for Skill #51.
- The revised [Skill #51 follow-up review](https://github.com/Kisuul/KestrelGaming/pull/55#pullrequestreview-6073062419) pinned to `4f8d5c92145a36ee2fe5dbe5a3556323f55c5844`: **R55-01 CLOSED; technical GO for research**, not for bit-exact codec equivalence or implementation. The new handoff documents input SHA-256, commands, frontend/linked-library versions, packet fingerprint, differing decoder behavior and limits of portability. [GitHub CI 45807223411](https://github.com/Kisuul/KestrelGaming/actions/runs/45807223411) passed 935 tests at that revision.
- [PR #56, Skills #52–59](https://github.com/Kisuul/KestrelGaming/pull/56): [Gauge technical GO](https://github.com/Kisuul/KestrelGaming/pull/56#pullrequestreview-6072978716), pinned to `7645b92f7b4e08ba9e5bf8b2726d32319f93bcda`. Acoustics/spatial synthetic fixture calculations were independently challenged, without finding a blocking research error. [GitHub CI 45806173308](https://github.com/Kisuul/KestrelGaming/actions/runs/45806173308) passed 935 tests. No physical instrument or room measurement was performed.
- Both PRs targeted the audio development branch `skills/audio-dsp-core-foundation-2026-11-03`, then at `3d65d0ddb88fead8d8a067e6abb8877ae5609d7b`. Their respective reviewed statuses were open; **re-fetch current heads and merge state before acting**.

### Skill #51 — reproducibility anomaly

- **Observed/documented:** The source WAV in the revised handoff is 48 kHz mono PCM16, 48,000 samples, with +24,576 at index 12,000 and −24,576 at 36,000. Its documented SHA-256 is `edd82135d9b8d585b0265f55a7cf66e9cbf183ba94213a183c86cc77b75549ce`. Gauge's follow-up review reports independent recreation of that exact digest.
- **Observed in the attributed reviews:** Opus 24 kb/s and native AAC 64 kb/s waveform measurements reproduced closely; the Opus **96 kb/s** author-side sample at 12,000 was **0.617178**, while Gauge's repeatable result was approximately **0.617251635**. The measured pre-/post-transient error powers also differed slightly. The author and Gauge recorded distinct **96k packet-data fingerprints** (`85bf88e35b96d95643359e5e8ee48f1f4cfcccdb05aac503992e8798990e8c1a` vs `4db05075e284a18764b0582bcaadb019eecc86a78f4aba8ea88df46602fdd641`), despite nominally matching FFmpeg 7.1.5 and linked libopus 1.5.2 descriptions.
- **Inference:** Different packet fingerprints mean that the compared encoded streams are not identical. Decoder differences alone cannot explain the packet-level disagreement; they can additionally affect PCM measurements. The remaining numerical discrepancy is **not evidence of a wrong DSP equation**.
- **Hypotheses, not root-cause findings:** Hidden encoder options or input sample-format negotiation; library build flags, SIMD/CPU-specific numerical paths, floating-point precision, or other encoder-environment differences. Do not mark any one as proven.
- **Discriminating next experiment:** Exchange or archive the **identical encoded `96k.opus` artifact** including presentation/trim metadata; decode the same bytes in both environments and compare PCM. If PCM matches, isolate encoder-side differences; if not, investigate decoder/build variations too. Then compare the first differing encoded packet across fresh encodes. A codec-specific regression oracle must pin encoded input, decoder build and justified tolerances instead of treating one environment's sample values as universal.
- **No new measurements in this checkpoint:** numerical and codec outcomes above are carried forward from the linked review records, not re-executed while writing this memory.

### Curriculum and authority

- [Audio umbrella PR #2](https://github.com/Kisuul/KestrelGaming/pull/2): **73-module completion gate** remains owner-controlled. Previous branch inspection showed **35 skill module directories**, while an older owner-acceptance ledger still reported **30 accepted**. They measure different things and require live reconciliation before stating current completion.
- Passing numerical examples or CI does not establish an agent's ability to choose and apply skills to unfamiliar DSP problems. A future blind skill-use evaluation should separate **knowledge**, **implementation**, and **independent judgment**; this is a proposal, not an accepted requirement.
- Do not quietly change protected Auralprint contracts or interpret a Kestrel research review as a production or Auralprint implementation authorization.

## Next action

When asked to resume: fetch the current PR #55/#56 heads and audio branch, confirm CI and any owner merges, then choose the smallest reviewable task. If asked about the 96k discrepancy, prioritize the byte-identical encoded-artifact cross-decode experiment over further speculation. Keep numerical review evidence, physical measurement evidence, and behavioral agent evaluation distinct.

## Revisit when

A reviewed PR head or merge state changes, new Opus packet/decoder evidence arrives, the owner reconciles accepted skill counts, the 73-skill gate changes, or Gauge is assigned a new DSP/Auralprint acceptance milestone.

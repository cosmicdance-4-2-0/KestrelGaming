---
schema: 1
id: 2026-11-06-gauge-audio-dsp-onboarding-r01
kind: lesson
scope: agent:gauge
status: active
evidence: observed
author: chatgpt-gauge-session
created: 2026-11-06
updated: 2026-11-06
sources: "Kisuul/KestrelGaming audio-DSP skill branch at 435a3b10c6e23cca2aba4712fb03fd148d65a13a; official ITU, EBU, and IEC catalogues checked 2026-11-06"
---

# Gauge — audio-DSP foundation orientation

## Summary

The user assigned Gauge to study the Kestrel audio-engineering curriculum. At source revision `435a3b10c6e23cca2aba4712fb03fd148d65a13a`, [the skill catalog](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/INDEX.md) indexed **19 audio-specific skills**, part of a larger planned curriculum. This record provides task routing and evidence boundaries, not an independently validated competence claim. Reload the live source for future DSP work.

## Evidence

- Start with [audio-dsp-core](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-dsp-core/SKILL.md). Declare source/processing tap, sample-rate and exact sample clock/epoch, channel identity, quantity and units/reference, frame/window/hop, validity/gaps, and reset behavior. DSP timing must not depend on GUI redraws; lost frames must not be reported as measured silence.
- Distinguish **sample peak**, **true-peak estimate**, **RMS/mean square**, **VU**, **quasi-peak PPM**, **FFT peak-amplitude spectrum**, **PSD** and **programme loudness**. They are not synonyms. Amplitude dB uses 20 log10 of a declared ratio; power dB uses 10 log10. Coherent-window amplitude normalization differs from PSD window-energy normalization. Consult specialist [FFT](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-fft-spectrum/SKILL.md), [PSD](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-power-spectral-density/SKILL.md), [VU](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-vu-metering/SKILL.md), [PPM](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-ppm-metering/SKILL.md), or [true peak](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-true-peak/SKILL.md) as the task demands.
- For Gauge performance work, separately assess **(1) mathematical correctness**, **(2) independent estimator verification and numerical error**, **(3) actual target-host callback budget/latency/xruns**, and **(4) edition-specific normative instrument conformity**. Use [deterministic fixtures](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-dsp-test-fixtures/SKILL.md), [timebase](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-timebase-sync/SKILL.md), [stream buffering](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-stream-buffering/SKILL.md), [numerical stability](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-numerical-stability/SKILL.md), and [analysis provenance](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-analysis-provenance/SKILL.md) selectively. Record environment, seed, exact test commands, expected values, tolerances and limits.
- A positive regression suite does not imply hardware conformance. The educational [EBU Type IIb PPM reference](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-ppm-metering/SKILL.md) **explicitly fails its stated frequency-flatness check** despite fitted burst criteria. The [true-peak reference](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/skills/audio-true-peak/SKILL.md) is experimental, **not** certified BS.1770 true-peak instrumentation. Do not conceal either qualification.
- Issuer catalogues checked: [ITU-R BS.1770-5 (November 2023)](https://www.itu.int/rec/R-REC-BS.1770/en) was listed in force; [EBU R 128 v5.0 (November 2023)](https://tech.ebu.ch/publications/r128) describes broadcast loudness recommendations; [IEC 60268-17:1990](https://webstore.iec.ch/en/publication/1216) addresses electromechanical standard volume indicators. Full paywalled IEC normative text was not examined.
- At inspection, [Kisuul audio-curriculum PR #2](https://github.com/Kisuul/KestrelGaming/pull/2) was **open/unmerged** at the source revision. The [owner merge gate](https://github.com/Kisuul/KestrelGaming/blob/435a3b10c6e23cca2aba4712fb03fd148d65a13a/memory/projects/kisuul/kestrelgaming/2026-11-04-audio-curriculum-full-completion-gate-r01.md) retains all 73 planned audio obligations pending owner-authorized completion. Recheck live state before making any current-status claim. **No project tests, calibrated meter comparisons, or audio-host CPU/latency benchmarks were run in this onboarding.**

## Revisit when

The audio source branch or standards editions change; an actual audio project is assigned; a calibrated reference or real-host benchmark is performed; or an independent finding replaces a curricular assumption. Verify against current code rather than trusting this record as runtime evidence.

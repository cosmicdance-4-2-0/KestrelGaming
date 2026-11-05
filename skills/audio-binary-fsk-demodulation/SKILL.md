---
name: audio-binary-fsk-demodulation
description: Demodulate candidate binary FSK and AFSK into sample-timed line states with configurable mark/space polarity, clock recovery, scores and erasures before framing.
---

# Binary FSK / AFSK — line states, not text

## When to load

Two distinct alternating tones suggest binary frequency-shift keying. Read the [architecture](../../docs/AUDIO_SIGNAL_RECOGNITION.md).

## Procedure

1. Specify channel and sample clock; mark and space frequency estimates; **which frequency means logical 1**; baud hypothesis; filter/window resolution; drift and noise model. No global hardcoded tone frequencies.
2. Choose an explicit discriminator (tone-bank power difference, Goertzel/matched filters, instantaneous frequency under suitable assumptions, or another justified method). Report scores and method limits.
3. Recover symbol phase and timing in sample coordinates. A fractional samples-per-bit ratio must not accumulate rounding drift. For asynchronous streams, start-edge estimation and bit-center sampling can be coordinated with the framer.
4. Emit bit/line-state, sample center or interval, decision margin, estimated rate, erasure, profile ID and missing-data flags. Do not turn low-confidence states into certain bits merely to obtain legible characters.
5. Hand recovered states to [asynchronous framing](../audio-asynchronous-framing/SKILL.md), then a separate codec. Never infer ITA2 or ASCII directly from the waveform.
6. Bound realtime work; characterize filters, group delay, startup/reset, gaps and recorders' lossy codec effects.

## Acceptance examples

Analytical bit sequences at variable sample rates/baud (including noninteger samples per bit), swapped tones/polarity, silence, random phase, noise, clock drift, a spurious simultaneous dual-tone and dropout. Measure BER and erasures independently of text rendering.

Source: [ITU-T V.23](https://www.itu.int/rec/T-REC-V.23) is an example modem profile **only**, not the definition of every AFSK receiver. See [decoder validation](../audio-decoder-validation/SKILL.md). No BER or realtime benchmark has been executed for this skill.

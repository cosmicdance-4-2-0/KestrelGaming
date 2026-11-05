---
name: audio-signal-recognition
description: Rank and reject candidate audio signalling types such as keyed Morse, simultaneous DTMF tones, and alternating two-tone FSK without assuming a protocol or inventing messages.
---

# Audio signal recognition — competing hypotheses

## When to load

Use for unknown recorded or live audio possibly containing data. Read the [architecture](../../docs/AUDIO_SIGNAL_RECOGNITION.md) and Kestrel [verification guidance](../../kestrel/VERIFICATION.md).

## Procedure

1. Trace sample rate, channel, recording codec, sample indices, clipping, resampling, signal path and missing-data intervals. Do not assume channels can be averaged without cancellation.
2. Estimate noise, energy envelope, time-frequency ridges, frequency stability, onset patterns and whether frequency components are simultaneous or alternating. Calibrate spectrum/window choices and observe more than one time scale where needed.
3. Rank OOK/Morse-like keying, DTMF-like pairs, binary-FSK candidates and UNKNOWN as distinct hypotheses. State the observation interval and adjustable parameter ranges, not just preset frequencies.
4. Provide a reproducible score definition, supporting evidence, counterevidence, sample-clock timing and rejection/insufficient-data reason. A candidate modulation is not a decoded protocol.
5. Route keyed and concurrent tones to [tone-event recovery](../audio-tone-event-recovery/SKILL.md); alternating two-state tones to [binary FSK demodulation](../audio-binary-fsk-demodulation/SKILL.md). Preserve alternatives when evidence is ambiguous.
6. Reset/discontinue deliberately across dropouts and rate changes. Do not fill unknown data with assumed valid zeros.

## Acceptance and limits

Require both positive and negative cases: variable carrier frequencies and baud, single-tone impostors, silence, speech/music, simultaneous DTMF versus alternating FSK, stereo cancellation, compressed audio, transient clicks and unclassifiable signals. Measure false alarm/false rejection rates rather than counting plausible text strings. UNKNOWN is a valid result.

Primary source contexts: [ITU-T Q.23](https://www.itu.int/rec/T-REC-Q.23), [ITU-R M.1677-1](https://www.itu.int/rec/R-REC-M.1677-1-200910-I). Use [independent validation](../audio-decoder-validation/SKILL.md). No receiver accuracy is claimed by this document.

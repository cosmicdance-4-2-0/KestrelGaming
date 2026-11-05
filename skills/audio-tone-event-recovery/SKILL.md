---
name: audio-tone-event-recovery
description: Recover sample-timed keyed-tone intervals and simultaneous tone groups with calibrated thresholds, hysteresis, durations and uncertainty for Morse and DTMF style signalling.
---

# Tone event recovery — samples before symbol grammar

## When to load

The candidate signal contains carrier-on/off intervals or simultaneous pairs. This produces physical events, **not** text. Read the [architecture](../../docs/AUDIO_SIGNAL_RECOGNITION.md).

## Procedure

1. Declare selected channel, rate, sample-clock convention, energy definition, window/hop, detector parameters, observed noise and discontinuity handling.
2. Detect tone energy using a calibrated filter/envelope or FFT/Goertzel bank. Distinguish two concurrent tones from one harmonic-rich carrier. Hysteresis, attack/release and debouncing must be documented, not UI-dependent.
3. Recover start/end samples, duration estimates, candidate frequencies, event quality, and ambiguity. A missing capture interval is not silence.
4. Interpret grammar downstream: Morse uses element/character/word gaps and possibly Farnsworth timing; DTMF checks simultaneous low/high frequency groups, tone twist, cadence and duration. Neither is a serial byte stream.
5. Preserve raw tone evidence under changes in display smoothing, resampling or renderer frame rate. Provide reset semantics and bounded realtime work.

## Acceptance examples

Known element/gap fixtures, repeated Morse characters, variable speed, DTMF tone pairs, incorrect single-tone/harmonic decoys, near-threshold and short/interrupted tones. Report timestamp error and detection precision; do not claim robust decoding from an untested waveform.

Sources: [ITU-R M.1677-1](https://www.itu.int/rec/R-REC-M.1677-1-200910-I), [ITU-T Q.23](https://www.itu.int/rec/T-REC-Q.23), [Q.24](https://www.itu.int/rec/T-REC-Q.24). See [decoder validation](../audio-decoder-validation/SKILL.md).

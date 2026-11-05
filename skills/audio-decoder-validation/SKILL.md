---
name: audio-decoder-validation
description: Validate audio signal recognition and protocol decoding using independent waveform and bit oracles, cross-language fixtures, layered accuracy metrics and negative controls.
---

# Decoder verification — independent evidence

## When to load

Any detector, tone-event extractor, FSK decoder, UART-like framer, Morse/DTMF parser or ITA2/ASCII codec is being built, reviewed or benchmarked. Read the [architecture](../../docs/AUDIO_SIGNAL_RECOGNITION.md) and [verification contract](../../kestrel/VERIFICATION.md).

## Procedure

1. Freeze independent ground truth at **every layer**: PCM samples, expected tone events, symbol bits, serial frames, code-table/control transitions and printable message. A successful text match is neither a bit-error-rate test nor modulation classification proof.
2. Source vectors from analytical examples, a different implementation/language, independently generated encoders and standards-derived tables. Pin generator revision, seed, sample rate, channels, codec, bit order, baud, frequencies, phase and expected tolerance. Encoder/decoder pairs sharing code or assumptions are not independent oracles.
3. Use negative controls: silence, music/speech, one-tone DTMF impostors, wrong FSK polarity, incorrect baud, corrupted framing, parity failure, 1.5-stop variants, USOS on/off, wrong national FIGS mapping, clipped/lossy waveforms, resampling, stereo cancellation and dropped blocks.
4. Record reproducible classification false positives/negatives; tone timing deviation; bit-error and erasure rates; frame/parity errors; code-table/state differences; exact text mismatch **separately**. Unknown/unclassifiable audio is a legitimate outcome.
5. Compare practical runtimes on real workloads without allowing GUI refresh or GPU output to alter sample-timed analytical results. Report end-to-end latency and queue loss separately from numerical correctness.
6. Perform a headless test without a UI. Re-run samples after resets/seeks, source/config transitions and varied buffers. Protect independent goldens; do not rewrite them to match an implementation bug.
7. State measured coverage and gaps precisely. Standards links are sources for test criteria, **not** conformance certificates.

## First verification matrix

| Boundary | Positive | Negative |
| --- | --- | --- |
| Recognizer | Alternating known tones | Simultaneous DTMF/single tone |
| Tone events | Known on/off/gap samples | Dropouts/harmonic impostors |
| FSK bits | Known bits at fractional samples/bit | Reversed polarity/noise/drift |
| Serial frames | 8N1 and 5-bit/1.5-stop | Truncation/parity/stop errors |
| ITA2 state | FIGS, digit, SPACE, LTRS | USOS disabled, unknown national variant |
| IRA text | Printable and control codepoints | Invalid code or frame |
| End-to-end | Independent PCM transmitter | No forced text for unknown audio |

Standards: [S.1](https://www.itu.int/rec/T-REC-S.1-199303-I), [T.50](https://www.itu.int/rec/T-REC-T.50-199209-I), [Q.23](https://www.itu.int/rec/T-REC-Q.23), [Q.24](https://www.itu.int/rec/T-REC-Q.24), [M.1677-1](https://www.itu.int/rec/R-REC-M.1677-1-200910-I). These are procedures, not exercised decoder benchmarks.

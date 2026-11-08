# Audio signal recognition and decoding — skill-family architecture

**Status:** language-neutral engineering guidance, not a working receiver, standards certification, or verified interoperability test. Separate from the ongoing audio-DSP branch.

## Pipeline and dependency boundaries

```text
PCM + channel/sample-clock/gap metadata
  -> signal classification (ranked hypotheses, including UNKNOWN)
     -> tone events (on/off Morse-like keying or simultaneous DTMF pairs)
     -> binary FSK/AFSK demodulation (mark/space line states)
         -> asynchronous serial framing (start/data/parity/stop)
             -> character codec (ITA2 LETTERS/FIGURES or ASCII/IRA)
                -> optional higher-level message interpretation
```

**Modulation is not framing, and framing is not character encoding.** An FSK waveform does not imply ASCII; 8N1 does not imply a particular modulation; Baudot/ITA2 does not imply a unique mark frequency or a universal unshift-on-space behavior. Morse and DTMF are separate branches, not UART encodings.

## Skill entrypoints

- [Signal recognition](../skills/audio-signal-recognition/SKILL.md): candidate classes and falsifiable evidence.
- [Tone-event recovery](../skills/audio-tone-event-recovery/SKILL.md): timed envelope and simultaneous-tone observations.
- [Binary FSK demodulation](../skills/audio-binary-fsk-demodulation/SKILL.md): binary symbols with time and confidence.
- [Asynchronous framing](../skills/audio-asynchronous-framing/SKILL.md): transport bits and framing validity.
- [Character-codec decoding](../skills/audio-character-codec-decoding/SKILL.md): code tables, state and control tokens.
- [Decoder validation](../skills/audio-decoder-validation/SKILL.md): independent waveforms, oracles and negative controls.

## Conceptual typed observation contract

Version any implementation-specific representation; do not make the Rust example into the reference standard.

| Observation | Required fields |
| --- | --- |
| PCM block | source/channel IDs, sample rate, first sample index, valid sample count, discontinuities, source/codec metadata |
| Candidate | signal family, parameter ranges, evidence span, score meaning, competing hypotheses, reject reason |
| Tone event | sample start/end, frequency or simultaneous pair, power convention, detector version, uncertainty and validity |
| Binary symbol | sample center/span, line state, rate/polarity profile, score, erasure, source gap status |
| Serial frame | sample start, raw ordered bits, width, parity, stop duration, sync status, error reasons |
| Decoded token | original code/frame ID, code-table edition/variant, prior/new shift state, text/control/unknown result |

Use sample time independently of GUI frame time. Missing blocks are NOT valid silence; failed decoding is NOT automatically printable text. A visualization reads the typed output but cannot change measurements. Explicitly configure channel, filtering, mark/space frequencies, polarity, baud, bit order, data width, parity, fractional stop duration, code table, initial shift state and optional USOS.

## Acceptance and scope

Test every layer with independently generated reference vectors and independently computed expectations; compare classification precision/false positives, tone onsets, BER/erasures, invalid frames, state transitions and finally message matches. A message that looks plausible is not an independent oracle. Include variable baud and frequency, wrong polarity, simultaneous-tone impostors, noise, codec artifacts, truncation, phase drift, sample drop, stereo cancellation, 1.5-stop framing and USOS both on and off. An unknown input may correctly produce UNKNOWN.

A production receiver additionally requires measured performance and interoperability. This package only establishes procedures and documentation/structure tests. The reference application may be Rust while the curriculum and fixtures stay language-neutral.

## Primary standards

- [ITU-T S.1 (03/1993)](https://www.itu.int/rec/T-REC-S.1-199303-I) — ITA2 code and control repertoire; national variants require explicit profiles.
- [ITU-T T.50 (09/1992)](https://www.itu.int/rec/T-REC-T.50-199209-I) — seven-bit International Reference Alphabet (IRA).
- [ITU-T Q.23](https://www.itu.int/rec/T-REC-Q.23) and [Q.24](https://www.itu.int/rec/T-REC-Q.24) — DTMF and its reception.
- [ITU-R M.1677-1](https://www.itu.int/rec/R-REC-M.1677-1-200910-I) — international Morse.
- [ITU-T V.23](https://www.itu.int/rec/T-REC-V.23) — *one* FSK modem profile, not a universal AFSK default.

No implementation source from an external/private application is copied here.

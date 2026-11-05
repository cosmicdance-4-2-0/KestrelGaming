---
schema: 1
id: 2026-11-04-audio-signal-recognition-r01
kind: handoff
scope: project:kisuul/kestrelgaming
status: active
evidence: observed
author: ChatGPT
created: 2026-11-04
updated: 2026-11-04
sources: "User requested language-neutral signal recognition skills 2026-11-04; KeyLine main d78a419d inspected as design context, no source copied; primary sources are public ITU standards."
---

# Signal recognition and decoding skill family

## Summary

**PARTIAL:** Six language-neutral procedures, one shared architecture guide and structural tests are prepared on branch `skills/audio-signal-recognition-2026-11-04`, based on Kestrel `main` `9033bf9`. This is documentation, **not** an implemented or independently verified decoder. The ongoing audio-DSP skill branch is not modified.

Modules: `audio-signal-recognition`, `audio-tone-event-recovery`, `audio-binary-fsk-demodulation`, `audio-asynchronous-framing`, `audio-character-codec-decoding`, and `audio-decoder-validation`. See [architecture](../../../../../docs/AUDIO_SIGNAL_RECOGNITION.md).

## Evidence

KeyLine's source (private repository, inspected at `d78a419d7f459f5092a8d495e089f108fef881a2`) implements text-to-tone generation for Morse, DTMF, AFSK/serial ASCII, and ITA2. Its README says independent decoder interoperability is not exhaustively validated. No private KeyLine code is copied here. The proposed architecture separates modulation recognition, tone/symbol recovery, serial framing and stateful character tables.

ITU primary references: [S.1](https://www.itu.int/rec/T-REC-S.1-199303-I), [T.50](https://www.itu.int/rec/T-REC-T.50-199209-I), [Q.23](https://www.itu.int/rec/T-REC-Q.23), and [M.1677-1](https://www.itu.int/rec/R-REC-M.1677-1-200910-I).

Structural tests verify discovery and local links only. Numerical correctness, receiver accuracy, real-time behavior and interoperability remain unverified.

## Next action

Review the skill family, then pick one deliberately small end-to-end vertical slice with an independently generated PCM bitstream, FSK demodulator, configurable asynchronous framer and ITA2/ASCII codec. Add wrong-polarity, missing-data, fractional stop and USOS counterexamples. Revalidate active audio branch dependencies before merging shared skill work.

## Revisit when

Independent waveform and cross-language tests exist, the audio skill branch merges, the reference application gains typed APIs, or KeyLine modulation behavior changes.

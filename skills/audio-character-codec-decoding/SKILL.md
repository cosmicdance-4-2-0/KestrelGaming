---
name: audio-character-codec-decoding
description: Interpret framed ITA2/Baudot LETTERS/FIGURES and ASCII/IRA codepoints with explicit national table variants, optional unshift-on-space, controls and error provenance.
---

# Character codecs — state before text

## When to load

The input is already framed data, not PCM. Separate code-table choice from 5-bit/8N1 transport and from AFSK modulation. Read the [architecture](../../docs/AUDIO_SIGNAL_RECOGNITION.md).

## Procedure

1. Pin the exact character table. ITA2 follows [ITU-T S.1](https://www.itu.int/rec/T-REC-S.1-199303-I) with explicit national figure variants. The [T.50 IRA](https://www.itu.int/rec/T-REC-T.50-199209-I) is a **seven-bit** character set; 8N1 carries eight data bits but is not itself an "8-bit ASCII" standard.
2. Require raw code, data width/order, validity, frame ID and sample time. Preserve raw frame observations independently of any printable interpretation.
3. For ITA2, track LETTERS/FIGURES state. FIGS/LTRS are controls, not printable glyphs. Specify initial state; do not guess undefined national punctuation positions.
4. Make unshift-on-space (**USOS**) an explicit optional convention. A space may reset to LETTERS in USOS mode, but there is no universal ITA2 guarantee. Where uncertain, report both labeled possibilities rather than choosing the prettier sentence.
5. Distinguish printable glyphs, controls, state changes, invalid and unknown codes. Do not silently replace non-printables or let a corrupted control mutate the shift state without a documented recovery policy.
6. Emit tokens with original frame/code, code table edition/variant, state before/after, control/text kind, ambiguity and provenance. Reinterpret codec hypotheses without rerunning demodulation.

## Acceptance examples

FIGS -> digit -> space -> letters with USOS on/off, repeated shifts, national-code ambiguity, carriage-return/line-feed, invalid frame, control loss and 7-bit IRA controls. Compare codepoints before string presentation; no language-model correction of uncertain text.

Primary documents: [ITU-T S.1](https://www.itu.int/rec/T-REC-S.1-199303-I), [S.4](https://www.itu.int/rec/T-REC-S.4), [T.50](https://www.itu.int/rec/T-REC-T.50-199209-I). See [decoder validation](../audio-decoder-validation/SKILL.md). No interoperability claim follows merely from these procedures.

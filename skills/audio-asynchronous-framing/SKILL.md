---
name: audio-asynchronous-framing
description: Recover start/data/parity/stop frames from uncertain sample-timed serial line states with explicit bit order, fractional stop duration, frame validity and resynchronization.
---

# Asynchronous framing — transport before characters

## When to load

A binary line state sequence appears to be start/stop serial data. An 8N1 or 5-bit start/stop profile is **not a character encoding or modulation**. Read the [architecture](../../docs/AUDIO_SIGNAL_RECOGNITION.md).

## Procedure

1. Pin data width (e.g. 5, 7, 8), LSB/MSB order, idle and start polarity, parity, nominal bit period, stop duration (including 1.5), accepted clock tolerance, and sync/reset behavior.
2. Qualify idle-to-start transitions rather than treating every low state as a start. Confirm start-bit center, then sample each data-bit center using sample-clock time and noninteger samples-per-bit.
3. Retain raw ordered bits, sample spans, clock estimate and per-bit confidence; assemble integer data in the specified order only.
4. Validate optional parity and stop **intervals** separately. Fractional stop time is not an additional data bit; truncated frames, invalid stops, uncertain sampling and missed samples require explicit flags.
5. Resynchronize after a bad frame by a declared policy. Never quietly discard framing failures until the text is readable.
6. Pass raw verified frames to [character-codec decoding](../audio-character-codec-decoding/SKILL.md); do not mutate codec state here.

## Acceptance examples

Known 8N1 bytes, five-bit frames with 1.5 stop bits, both bit orders, wrong polarity, truncated last frame, parity failure, back-to-back symbols and a fractional baud/sample-rate ratio. Report frame error rates separately from character accuracy.

Verification: [audio-decoder-validation](../audio-decoder-validation/SKILL.md). No particular UART or teleprinter conformance is claimed.

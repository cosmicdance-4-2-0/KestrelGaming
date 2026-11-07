#!/usr/bin/env python3
"""Decode a continuous ITA2 Baudot AFSK burst with 5 data bits and 1.5 stop bits.

Requires ffmpeg, NumPy, and SciPy. Not a general noisy-radio RTTY demodulator.
"""
import argparse
import subprocess
import sys

import numpy as np
from scipy.signal import fftconvolve

# ITA2, indexed by transmitted 5-bit value (LSB first).
LTRS = ("", "E", "\n", "A", " ", "S", "I", "U", "\r", "D", "R", "J", "N", "F",
        "C", "K", "T", "Z", "L", "W", "H", "Y", "P", "Q", "O", "B", "G", "",
        "M", "X", "V", "")
# One documented national-variant choice: FIGS(13)=!, (20)=#, (26)=&.
FIGS = ("", "3", "\n", "-", " ", "'", "8", "7", "\r", "$", "4", "'", ",", "!",
        ":", "(", "5", '"', ")", "2", "#", "6", "0", "1", "9", "?", "&", "",
        ".", "/", ";", "")
FIGS_SHIFT, LTRS_SHIFT = 27, 31
SAMPLE_RATE = 12000


def read_audio(path):
    """Use ffmpeg only to decode/resample local input; never invoke a shell."""
    result = subprocess.run(
        ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-i", path,
         "-vn", "-ac", "1", "-ar", str(SAMPLE_RATE), "-f", "f32le", "pipe:1"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        raise ValueError("ffmpeg failed: " + result.stderr.decode("utf-8", "replace").strip())
    audio = np.frombuffer(result.stdout, dtype="<f4").astype(np.float64)
    if audio.size < SAMPLE_RATE // 10:
        raise ValueError("Too little audio; expected at least 0.1 second")
    return audio


def discriminate(audio, mark, space, baud):
    bit = 1.0 / baud
    times = np.arange(audio.size) / SAMPLE_RATE
    win_len = max(17, round(SAMPLE_RATE * bit * 0.7))
    win = np.hanning(win_len)
    win /= win.sum()
    mark_amp = abs(fftconvolve(audio * np.exp(-2j * np.pi * mark * times), win, mode="same"))
    space_amp = abs(fftconvolve(audio * np.exp(-2j * np.pi * space * times), win, mode="same"))
    envelope = mark_amp + space_amp
    if not np.isfinite(envelope).all() or envelope.max() < 1e-6:
        raise ValueError("No usable AFSK signal")
    polarity = (mark_amp - space_amp) / (envelope + 1e-12)
    return polarity, envelope


def frames(polarity, envelope, baud):
    """Search initial phase for a fixed-cadence single burst, validate framing.

    Assumes no skipped characters, no significant sample-clock drift, no longer
    idle gaps inside a burst. A fresh start/stop scan is needed otherwise.
    """
    bit = 1.0 / baud
    char = bit * 7.5
    # Signal begins with the first START bit, preceded by digital silence.
    # Avoid treating low-level codec pre-echo as a start.
    present = envelope > envelope.max() * 0.20
    locations = np.flatnonzero(present)
    if not len(locations):
        raise ValueError("No signal onset found")
    onset = locations[0] / SAMPLE_RATE
    # Need sufficient audio remaining for the last whole frame.
    seconds = len(polarity) / SAMPLE_RATE
    offsets = np.linspace(max(0, onset - bit * 0.60), onset + bit * 0.55, 121)
    best = None
    for start in offsets:
        count = int((seconds - start) / char)
        if count < 1:
            continue
        centers = start + np.arange(count)[:, None] * char + bit * np.array(
            [.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.0])[None, :]
        samples = polarity[np.clip((centers * SAMPLE_RATE).astype(int), 0, len(polarity) - 1)]
        valid = (samples[:, 0] < -0.5) & (samples[:, 6] > 0.5) & (samples[:, 7] > 0.5)
        quality = (np.mean(valid), np.mean(-samples[:, 0] + samples[:, 6] + samples[:, 7]))
        if best is None or quality > best[0]:
            best = (quality, start, samples, valid)
    if best is None:
        raise ValueError("Cannot fit any complete serial frames")
    _, start, samples, valid = best
    values = np.sum((samples[:, 1:6] > 0) * (1 << np.arange(5)), axis=1).astype(int)
    return start, values, np.flatnonzero(~valid)


def ita2(values, unshift_on_space=False):
    state = "LTRS"
    output = []
    shifts = 0
    for value in values:
        if value == LTRS_SHIFT:
            state = "LTRS"
            shifts += 1
        elif value == FIGS_SHIFT:
            state = "FIGS"
            shifts += 1
        else:
            symbol = (LTRS if state == "LTRS" else FIGS)[int(value)]
            output.append(symbol)
            if symbol == " " and unshift_on_space:
                state = "LTRS"
    return "".join(output), shifts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", help="Local audio file supported by ffmpeg (WAV, WebM, ...)")
    parser.add_argument("--mark", type=float, default=2125, help="Frequency for bit 1, default 2125")
    parser.add_argument("--space", type=float, default=2295, help="Frequency for bit 0, default 2295")
    parser.add_argument("--baud", type=float, default=45.45)
    parser.add_argument("--unshift-on-space", action="store_true", help="Optional amateur RTTY behavior")
    parser.add_argument("--show-codes", action="store_true", help="Print raw ITA2 values to stderr")
    args = parser.parse_args()
    if args.baud <= 0 or not (0 < args.mark < SAMPLE_RATE/2) or not (0 < args.space < SAMPLE_RATE/2) or args.mark == args.space:
        parser.error("mark/space must be distinct positive frequencies below Nyquist; baud must be positive")
    try:
        audio = read_audio(args.file)
        levels, envelope = discriminate(audio, args.mark, args.space, args.baud)
        start, values, errors = frames(levels, envelope, args.baud)
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    if args.show_codes:
        print("ITA2 codes:", " ".join(map(str, values)), file=sys.stderr)
    if len(errors):
        print(f"ERROR: framing failed in {len(errors)} of {len(values)} frames: {errors.tolist()}", file=sys.stderr)
        return 2
    payload, shifts = ita2(values, args.unshift_on_space)
    print(f"PASS: {len(values)} frames; first start {start:.4f}s; {shifts} shift codes", file=sys.stderr)
    print(payload, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())

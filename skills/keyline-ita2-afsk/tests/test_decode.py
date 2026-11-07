"""Synthetic fixed-cadence ITA2 AFSK checks; requires numpy, scipy, ffmpeg."""
from pathlib import Path
import sys
import tempfile
import unittest
import wave

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from decode import FIGS, LTRS, discriminate, frames, ita2, read_audio  # noqa: E402


def synthesize(text, *, prepend=0.08, baud=45.45, sr=12000):
    state = 'LTRS'
    # Each character has 7.5 elements, not 8. Maintain exact bit clock.
    codes = []
    state = 'LTRS'
    for ch in text:
        table = LTRS if state == 'LTRS' else FIGS
        if ch not in table:
            codes.append(27 if state == 'LTRS' else 31)
            state = 'FIGS' if state == 'LTRS' else 'LTRS'
            table = LTRS if state == 'LTRS' else FIGS
        codes.append(table.index(ch))
    segments = []
    for code in codes:
        segments.append((0, 1.0))
        segments.extend(((code >> i) & 1, 1.0) for i in range(5))
        segments.append((1, 1.5))
    end = prepend
    samples = [np.zeros(round(sr * prepend))]
    for bit, length in segments:
        new_end = end + length / baud
        a, b = round(end * sr), round(new_end * sr)
        t = np.arange(a, b) / sr
        samples.append(0.6 * np.sin(2 * np.pi * (2125 if bit else 2295) * t))
        end = new_end
    audio = np.concatenate(samples)
    return audio, codes


class DecoderTests(unittest.TestCase):
    def test_shift_across_space_and_back(self):
        original = 'CQ 1234 TEST! 45 END.'
        audio, codes = synthesize(original)
        with tempfile.TemporaryDirectory() as tmp:
            filename = str(Path(tmp) / 'test.wav')
            with wave.open(filename, 'wb') as out:
                out.setnchannels(1)
                out.setsampwidth(2)
                out.setframerate(12000)
                out.writeframes((audio * 32767).astype('<i2').tobytes())
            samples = read_audio(filename)
            levels, env = discriminate(samples, 2125, 2295, 45.45)
            start, values, errors = frames(levels, env, 45.45)
        self.assertEqual(errors.tolist(), [])
        self.assertEqual(values.tolist(), codes)
        output, shifts = ita2(values)
        self.assertEqual(output, original)
        self.assertGreaterEqual(shifts, 2)
        self.assertAlmostEqual(start, .08, delta=.014)

    def test_optional_amateur_unshift_on_space(self):
        # Stateful ITA2 figures shift persists across spaces by default.
        message = '12 34'
        _, values = synthesize(message)
        self.assertEqual(ita2(values)[0], message)
        self.assertNotEqual(ita2(values, unshift_on_space=True)[0], message)

    def test_reject_silent_signal(self):
        with self.assertRaisesRegex(ValueError, 'No usable AFSK'):
            discriminate(np.zeros(24000), 2125, 2295, 45.45)


if __name__ == '__main__':
    unittest.main()

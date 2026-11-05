"""Structural tests; these do NOT test decoding or instrument conformance."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAMES = (
    "audio-signal-recognition",
    "audio-tone-event-recovery",
    "audio-binary-fsk-demodulation",
    "audio-asynchronous-framing",
    "audio-character-codec-decoding",
    "audio-decoder-validation",
)


class SignalSkillsStructure(unittest.TestCase):
    def test_skill_headers_and_index(self):
        index = (ROOT / "skills/INDEX.md").read_text(encoding="utf8")
        for name in NAMES:
            with self.subTest(name=name):
                content = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf8")
                self.assertTrue(content.startswith(f"---\\nname: {name}\\ndescription: ".replace("\\n", "\n")))
                self.assertIn(f"]({name}/SKILL.md)", index)
                self.assertIn("## Procedure", content)
                self.assertTrue(any(s in content.lower() for s in ("acceptance", "verification", "test")))

    def test_architecture_names_all_skills(self):
        doc = (ROOT / "docs/AUDIO_SIGNAL_RECOGNITION.md").read_text(encoding="utf8")
        for name in NAMES:
            self.assertIn(f"{name}/SKILL.md", doc)
        self.assertIn("not a working receiver", doc)
        self.assertIn("UNKNOWN", doc)

    def test_local_links_in_new_markdown(self):
        paths = [ROOT / "docs/AUDIO_SIGNAL_RECOGNITION.md"]
        paths += [ROOT / "skills" / n / "SKILL.md" for n in NAMES]
        for path in paths:
            content = path.read_text(encoding="utf8")
            for match in re.finditer(r"\]\(([^)]+)\)", content):
                target = match.group(1).split("#", 1)[0]
                if not target or "://" in target or target.startswith("#"):
                    continue
                with self.subTest(path=path.name, target=target):
                    self.assertTrue((path.parent / target).exists())


if __name__ == "__main__":
    unittest.main()

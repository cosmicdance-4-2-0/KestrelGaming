"""Read-only shape checks for Flint's proposed Kestrel character (not a behavioral certification)."""
import json
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FlintProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads((ROOT / "agents/flint/PROFILE.json").read_text(encoding="utf-8"))

    def test_identity_is_draft(self):
        self.assertEqual(self.profile["metadata"]["character_id"], "flint")
        self.assertEqual(self.profile["schema"]["status"], "DRAFT")
        self.assertIsNone(self.profile["metadata"]["runtime_identity_id"])
        self.assertEqual(self.profile["continuity"]["first_state"], "DRAFT_UNINSTANTIATED")

    def test_four_normalized_bands(self):
        bands = self.profile["traits"]["bands"]
        self.assertEqual(len(bands), 4)
        for label, weights in bands.items():
            with self.subTest(label=label):
                self.assertTrue(weights)
                self.assertTrue(all(math.isfinite(v) and 0 <= v <= 1 for v in weights.values()))
                self.assertAlmostEqual(sum(weights.values()), 1.0, places=8)

    def test_drives_have_measurable_correctives(self):
        drives = self.profile["motivations"]["primary_drives"]
        self.assertEqual([d["rank"] for d in drives], [1, 2, 3])
        self.assertEqual(len({d["id"] for d in drives}), 3)
        self.assertTrue(all(d["failure_mode"] and d["progress_evidence"] for d in drives))

    def test_memory_is_scoped_and_indexed(self):
        record = (ROOT / "memory/agents/flint/PROFILE.md").read_text(encoding="utf-8")
        idx = (ROOT / "memory/agents/flint/INDEX.md").read_text(encoding="utf-8")
        catalog = (ROOT / "memory/agents/INDEX.md").read_text(encoding="utf-8")
        self.assertIn("scope: agent:flint", record)
        self.assertIn("kind: profile", record)
        self.assertIn("(PROFILE.md)", idx)
        self.assertIn("(flint/INDEX.md)", catalog)

    def test_behavior_never_grants_authority(self):
        self.assertIn("host permissions", self.profile["operating_limits"]["higher_priority_contract"])
        self.assertIn("No running-agent trials", self.profile["evaluation"]["certification"])

if __name__ == "__main__":
    unittest.main()

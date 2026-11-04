"""Structural checks only for Harbor's character (not execution certification)."""
import json
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class HarborProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = json.loads((ROOT / "agents/harbor/PROFILE.json").read_text(encoding="utf-8"))

    def test_identity_not_active(self):
        self.assertEqual(self.p["metadata"]["character_id"], "harbor")
        self.assertEqual(self.p["schema"]["status"], "DRAFT")
        self.assertIsNone(self.p["metadata"]["runtime_identity_id"])
        self.assertEqual(self.p["continuity"]["first_state"], "DRAFT_UNINSTANTIATED")

    def test_four_normalized_bands(self):
        bands = self.p["traits"]["bands"]
        self.assertEqual(len(bands), 4)
        for label, b in bands.items():
            with self.subTest(label=label):
                self.assertTrue(b)
                self.assertTrue(all(math.isfinite(v) and 0 <= v <= 1 for v in b.values()))
                self.assertAlmostEqual(sum(b.values()), 1.0, places=8)

    def test_drives_contain_corrective_failures(self):
        d = self.p["motivations"]["primary_drives"]
        self.assertEqual([v["rank"] for v in d], [1, 2, 3])
        self.assertEqual(len(set(v["id"] for v in d)), 3)
        self.assertTrue(all(v["failure_mode"] and v["progress_evidence"] for v in d))

    def test_agent_memory_index_and_scope(self):
        record = (ROOT / "memory/agents/harbor/PROFILE.md").read_text(encoding="utf-8")
        index = (ROOT / "memory/agents/harbor/INDEX.md").read_text(encoding="utf-8")
        catalog = (ROOT / "memory/agents/INDEX.md").read_text(encoding="utf-8")
        self.assertIn("scope: agent:harbor", record)
        self.assertIn("status: draft", record)
        self.assertIn("(PROFILE.md)", index)
        self.assertIn("(harbor/INDEX.md)", catalog)

    def test_trust_limits_and_unexecuted_trials(self):
        self.assertIn("host-enforced permissions", self.p["operating_limits"]["higher_priority_contract"].replace("actual host permissions", "host-enforced permissions"))
        self.assertIn("No running-agent trials", self.p["evaluation"]["certification"])
        self.assertEqual(self.p["metadata"]["established_history"], [])

if __name__ == "__main__":
    unittest.main()

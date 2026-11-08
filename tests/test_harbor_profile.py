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
        self.assertIn("actual host permissions", self.p["operating_limits"]["higher_priority_contract"])
        self.assertTrue(self.p["evaluation"]["shared_scenario"]["first_move"])
        self.assertIn("No formal matched-task personality trial", self.p["evaluation"]["certification"])
        self.assertGreaterEqual(len(self.p["metadata"]["established_history"]), 4)
        self.assertGreaterEqual(len(self.p["continuity"]["accepted_lessons"]), 3)

    def test_observed_history_is_provenance_backed_not_runtime_identity(self):
        self.assertEqual(self.p["metadata"]["date"], "2026-11-03")
        self.assertEqual(self.p["continuity"]["first_state"], "DRAFT_UNINSTANTIATED")
        for item in self.p["metadata"]["established_history"]:
            with self.subTest(activity=item["activity"]):
                self.assertTrue(item["date"] and item["outcome"] and item["limits"])
                self.assertTrue((ROOT / item["source"]).is_file(), item["source"])
        for lesson in self.p["continuity"]["accepted_lessons"]:
            with self.subTest(lesson=lesson["id"]):
                self.assertTrue(lesson["lesson"])
                self.assertTrue((ROOT / lesson["source"]).is_file(), lesson["source"])
        for peer in self.p["collaboration"]["known_relationship_history"]:
            self.assertTrue(peer["interaction"] and peer["evidence"] and peer["limits"])
            self.assertTrue(peer["evidence"].startswith("https://github.com/"))
        for peer in self.p["continuity"]["earned_relationships"]:
            self.assertTrue(peer["evidence"] and peer["limits"])
            self.assertIn("not a personal bond", peer["limits"])

    def test_no_empty_required_character_fields(self):
        def walk(value, path=""):
            if isinstance(value, dict):
                self.assertTrue(value, path)
                for key, item in value.items():
                    walk(item, f"{path}.{key}")
            elif isinstance(value, list):
                self.assertTrue(value, path)
                for index, item in enumerate(value):
                    walk(item, f"{path}[{index}]")
            elif isinstance(value, str):
                self.assertTrue(value.strip(), path)
                self.assertNotIn("REPLACE_", value)
            elif value is None:
                self.assertEqual(path, ".metadata.runtime_identity_id")
        walk(self.p)

if __name__ == "__main__":
    unittest.main()

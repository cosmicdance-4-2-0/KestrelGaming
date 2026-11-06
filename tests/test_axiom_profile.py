"""Structural checks only for Axiom's character (not execution certification)."""
import json
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class AxiomProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = json.loads((ROOT / "agents/axiom/PROFILE.json").read_text(encoding="utf-8"))

    def test_design_status_and_founding_state_are_not_runtime_identity(self):
        self.assertEqual(self.p["metadata"]["character_id"], "axiom")
        self.assertEqual(self.p["metadata"]["branch"], "agents/axiom-v1")
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
        record = (ROOT / "memory/agents/axiom/PROFILE.md").read_text(encoding="utf-8")
        index = (ROOT / "memory/agents/axiom/INDEX.md").read_text(encoding="utf-8")
        catalog = (ROOT / "memory/agents/INDEX.md").read_text(encoding="utf-8")
        self.assertIn("scope: agent:axiom", record)
        self.assertIn("status: draft", record)
        self.assertIn("(PROFILE.md)", index)
        self.assertIn("(axiom/INDEX.md)", catalog)

    def test_trust_limits_and_unexecuted_trials(self):
        self.assertIn("actual host permissions", self.p["operating_limits"]["higher_priority_contract"])
        self.assertTrue(self.p["evaluation"]["shared_scenario"]["first_move"])
        self.assertIn("No matched comparative agent trials", self.p["evaluation"]["certification"])
        self.assertEqual(self.p["collaboration"]["known_relationship_history"], [])

    def test_history_is_attributed_local_memory_not_inherited_achievement(self):
        history = self.p["metadata"]["established_history"]
        self.assertTrue(history)
        self.assertEqual(len(history), len(set(history)))
        profile_dir = ROOT / "agents/axiom"
        index = (ROOT / "memory/agents/axiom/INDEX.md").read_text(encoding="utf-8")
        for reference in history:
            with self.subTest(record=reference):
                record = (profile_dir / reference).resolve()
                self.assertIn((ROOT / "memory").resolve(), record.parents)
                text = record.read_text(encoding="utf-8")
                frontmatter = text.split("---", 2)[1].splitlines()
                self.assertIn("author: axiom", frontmatter)
                self.assertTrue(any(line.startswith("sources: ") for line in frontmatter))
                self.assertIn(record.name, index)

    def test_shared_pickup_does_not_erase_branch_selection(self):
        entry = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("**Branch-selected persona:**", entry)
        self.assertIn("agents/axiom/AGENT.md", entry)
        self.assertIn("agents/axiom/PROFILE.json", entry)
        self.assertIn("docs/AGENT_PICKUP.md", entry)
        self.assertIn("docs/AGENT_STRUCTURE.md", entry)

if __name__ == "__main__":
    unittest.main()

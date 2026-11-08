"""Structural checks only for Gauge's character (not execution certification)."""
import json
import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class GaugeProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = json.loads((ROOT / "agents/gauge/PROFILE.json").read_text(encoding="utf-8"))

    def test_identity_not_active(self):
        self.assertEqual(self.p["metadata"]["character_id"], "gauge")
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
        record = (ROOT / "memory/agents/gauge/PROFILE.md").read_text(encoding="utf-8")
        index = (ROOT / "memory/agents/gauge/INDEX.md").read_text(encoding="utf-8")
        catalog = (ROOT / "memory/agents/INDEX.md").read_text(encoding="utf-8")
        self.assertIn("scope: agent:gauge", record)
        self.assertIn("status: draft", record)
        self.assertIn("(PROFILE.md)", index)
        self.assertIn("(gauge/INDEX.md)", catalog)

    def test_trust_limits_and_unexecuted_trials(self):
        self.assertIn("actual host permissions", self.p["operating_limits"]["higher_priority_contract"])
        self.assertTrue(self.p["evaluation"]["shared_scenario"]["first_move"])
        self.assertIn("No running-agent trials", self.p["evaluation"]["certification"])
        history = self.p["metadata"]["established_history"]
        self.assertGreaterEqual(len(history), 4)
        self.assertTrue(all("2026-11-" in item for item in history))
        self.assertGreaterEqual(len(self.p["continuity"]["accepted_lessons"]), 3)
        self.assertGreaterEqual(len(self.p["collaboration"]["known_relationship_history"]), 1)
        self.assertEqual(self.p["continuity"]["earned_relationships"], [])

    def test_portable_visual_canon_is_sourced_not_authenticated(self):
        path = ROOT / "agents/gauge/APPEARANCE.json"
        visual = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(visual["schema"]["name"], "KestrelAgentAppearance")
        self.assertEqual(visual["schema"]["version"], "0.2")
        self.assertEqual(visual["schema"]["status"], "CANONICAL_REFERENCE")
        self.assertEqual(visual["metadata"]["visual_id"], "gauge-witness-visual-03")
        self.assertEqual(visual["reference_sheet"]["source_image"]["sha256"], "291c12694cd915710731339de7a892e586d4d8d2e34e6f8d53bcc6a16d2b95ab")
        self.assertEqual(visual["reference_document"]["original_sha256"], "ac12be7cb4048c4f92e4456a8bca22905ce5c4c7b080f86530cb26802a633dfc")
        self.assertTrue((path.parent / visual["metadata"]["source_document"]).is_file())
        self.assertEqual(visual["metadata"]["character_id"], "gauge")
        self.assertTrue(visual["metadata"]["owner_accepted"])
        self.assertEqual(visual["metadata"]["home_branch"], "agents/gauge-v1")
        svg = path.parent / visual["metadata"]["asset"]
        self.assertTrue(svg.is_file())
        root = ET.parse(svg).getroot()
        self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
        self.assertEqual(root.attrib.get("viewBox"), "0 0 512 512")
        self.assertFalse(any(node.tag.endswith(("script", "foreignObject", "image")) for node in root.iter()))
        self.assertTrue(all(re.fullmatch(r"#[0-9A-Fa-f]{6}", color)
                            for color in visual["design"]["palette"].values()))
        agent = (ROOT / "agents/gauge/AGENT.md").read_text(encoding="utf-8")
        self.assertIn("APPEARANCE.json", agent)
        self.assertIn("avatar.svg", agent)
        self.assertIn("CANONICAL_APPEARANCE.md", agent)
        self.assertEqual(visual["reference_sheet"]["repo_binary_available"], False)
        self.assertEqual(visual["metadata"]["asset_role"], "legacy-v01-svg-fallback-not-v03-image")

if __name__ == "__main__":
    unittest.main()

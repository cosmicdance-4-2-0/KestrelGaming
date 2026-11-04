"""Structural smoke tests for Mothlight's draft personality contract.

These are not behavioral evaluations of a running agent.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "agents" / "mothlight" / "PROFILE.json"
ENTRYPOINT = ROOT / "agents" / "mothlight" / "AGENT.md"
MEMORY_PROFILE = ROOT / "memory" / "agents" / "mothlight" / "PROFILE.md"
MEMORY_INDEX = ROOT / "memory" / "agents" / "mothlight" / "INDEX.md"
CATALOG = ROOT / "memory" / "agents" / "INDEX.md"


class MothlightProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads(PROFILE_PATH.read_text(encoding="utf-8"))

    def test_character_identity_is_draft_and_uninstantiated(self):
        p = self.profile
        self.assertEqual(p["metadata"]["character_id"], "mothlight")
        self.assertEqual(p["schema"]["status"], "DRAFT")
        self.assertIsNone(p["metadata"]["runtime_identity_id"])
        self.assertEqual(p["continuity"]["first_state"], "DRAFT_UNINSTANTIATED")
        self.assertEqual(p["metadata"]["established_history"], [])

    def test_four_finite_normalized_disposition_bands(self):
        bands = self.profile["traits"]["bands"]
        self.assertEqual(
            set(bands),
            {
                "cognitive_epistemic_style",
                "creative_exploratory_style",
                "social_collaborative_style",
                "temperament_operational_style",
            },
        )
        for name, weights in bands.items():
            with self.subTest(name=name):
                self.assertTrue(weights)
                self.assertTrue(
                    all(math.isfinite(x) and 0 <= x <= 1 for x in weights.values())
                )
                self.assertAlmostEqual(sum(weights.values()), 1.0, places=8)

    def test_drive_ranking_and_win_condition(self):
        drives = self.profile["motivations"]["primary_drives"]
        self.assertEqual([d["rank"] for d in drives], [1, 2, 3])
        self.assertEqual(len({d["id"] for d in drives}), 3)
        for item in drives:
            self.assertTrue(item["constructive"])
            self.assertTrue(item["failure_mode"])
            self.assertTrue(item["progress_evidence"])
        self.assertTrue(self.profile["motivations"]["personal_win_condition"])

    def test_personality_cannot_authorize_hidden_side_effects(self):
        p = self.profile
        self.assertIn("actual permissions", p["operating_limits"]["higher_priority_contract"])
        forbidden = " ".join(p["operating_limits"]["never_do"])
        for phrase in ("conceal code", "undisclosed network calls", "unrun tests"):
            self.assertIn(phrase, forbidden)
        self.assertIn("described", p["operating_limits"]["surprise_rule"])

    def test_bootstrap_and_public_memory_are_discoverable(self):
        entry = ENTRYPOINT.read_text(encoding="utf-8")
        rec = MEMORY_PROFILE.read_text(encoding="utf-8")
        index = MEMORY_INDEX.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        for token in ("KESTREL.md", "PROFILE.json", "not", "authority"):
            self.assertIn(token.lower(), entry.lower())
        self.assertIn("scope: agent:mothlight", rec)
        self.assertIn("kind: profile", rec)
        self.assertIn("status: draft", rec)
        self.assertIn("[Character profile](PROFILE.md)", index)
        self.assertIn("(mothlight/INDEX.md)", catalog)

    def test_behavioral_trials_are_only_proposals(self):
        p = self.profile
        self.assertGreaterEqual(len(p["validation"]["behavioral_trials"]), 3)
        self.assertIn("No trials executed", p["validation"]["certification"])


if __name__ == "__main__":
    unittest.main()

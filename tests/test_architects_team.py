"""Regression checks for the first real Kestrel studio team contract.

These checks prove local structural consistency, not runtime instantiation
or any performance advantage over individual engineers.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_team_contracts import validate_team_contracts  # noqa: E402

HOME = ROOT / "teams" / "architects"


class ArchitectsTeamContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads((HOME / "PROFILE.json").read_text(encoding="utf-8"))
        cls.contract = (HOME / "TEAM.md").read_text(encoding="utf-8")
        cls.catalog = (ROOT / "teams" / "INDEX.md").read_text(encoding="utf-8")

    def test_teams_validate_under_standard_kestrel_structure(self):
        self.assertEqual(validate_team_contracts(ROOT), [])

    def test_architects_identity_and_catalog(self):
        self.assertEqual(self.profile["metadata"]["team_id"], "architects")
        self.assertEqual(self.profile["metadata"]["contract_path"], "teams/architects/TEAM.md")
        self.assertIn("architects/TEAM.md", self.catalog)
        self.assertIn("**Team ID:** `architects`", self.contract)

    def test_three_distinct_perspectives_with_explicit_dissent(self):
        comp = self.profile["composition"]
        self.assertEqual(comp["lead_agent_id"], "axiom")
        self.assertEqual(comp["counterweight_agent_id"], "flint")
        self.assertEqual(
            [(m["agent_id"], m["role"]) for m in comp["members"]],
            [("axiom", "lead"), ("flint", "counterweight"), ("harbor", "contributor")],
        )
        for name in ("Axiom", "Flint", "Harbor"):
            self.assertIn(name, self.contract)
        self.assertIn("**Dispute rule:**", self.contract)
        self.assertIn("**Likely team failure mode:**", self.contract)

    def test_review_counterexamples_on_real_architects_layout(self):
        heading = "## Composition — different instincts, not averaged identities"
        table = "\n".join(line for line in self.contract.splitlines() if line.startswith("|"))
        cases = {
            "duplicate section": (self.contract + "\n" + heading + "\n\n" + table.replace("Lead — Axiom", "Lead — Flint"), self.catalog),
            "commented table": (self.contract.replace(table, "<!--\n" + table + "\n-->"), self.catalog),
            "indented table": (self.contract.replace(table, "\n".join("    " + line for line in table.splitlines())), self.catalog),
            "commented catalog": (self.contract, "<!-- [The Architects](architects/TEAM.md) -->"),
            "image catalog": (self.contract, "![The Architects](architects/TEAM.md)"),
        }
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "agents").mkdir()
            (root / "agents/ROSTER_V1.json").write_bytes((ROOT / "agents/ROSTER_V1.json").read_bytes())
            home = root / "teams/architects"
            home.mkdir(parents=True)
            (home / "PROFILE.json").write_text(json.dumps(self.profile), encoding="utf-8")
            for label, (contract, catalog) in cases.items():
                with self.subTest(case=label):
                    (home / "TEAM.md").write_text(contract, encoding="utf-8")
                    (root / "teams/INDEX.md").write_text(catalog, encoding="utf-8")
                    self.assertTrue(validate_team_contracts(root), label)

    def test_composite_mode_is_truthful_and_limited(self):
        p = self.profile
        self.assertEqual(p["execution"]["default_mode"], "composite")
        self.assertTrue(p["execution"]["federated"]["requires_external_host"])
        self.assertEqual(p["authority"]["permissions_granted"], [])
        self.assertFalse(p["authority"]["can_delegate_or_vote"])
        self.assertIsNone(p["metadata"]["runtime_identity_id"])
        self.assertIsNone(p["continuity"]["team_memory_scope"])
        self.assertFalse(p["evaluation"]["behavioral_certified"])

    def test_falsifiable_comparative_trial_is_specified_not_claimed(self):
        p = self.profile
        self.assertIn("generic Kestrel", p["evaluation"]["comparator"])
        self.assertTrue(p["evaluation"]["evidence"])
        self.assertTrue(p["evaluation"]["falsifier"])
        self.assertIn("NOT TESTED", self.contract)


if __name__ == "__main__":
    unittest.main()

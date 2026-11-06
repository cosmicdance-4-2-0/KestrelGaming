"""Synthetic positive/negative tests for team-schema validation; no agent runtime."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_team_contracts import (  # noqa: E402
    FIELDS, FALSE_FIELDS, HEADINGS, LIST_EMPTY_FIELDS, LIST_STRINGS,
    NULL_FIELDS, TRUE_FIELDS, validate_team_contracts,
)


def _shape(where=""):
    if where in FIELDS:
        return {key: _shape((where + "." if where else "") + key) for key in FIELDS[where]}
    if where == "composition.members":
        return [_shape("composition.members[]") for _ in range(2)]
    if where in NULL_FIELDS:
        return None
    if where in TRUE_FIELDS:
        return True
    if where in FALSE_FIELDS:
        return False
    if where in LIST_EMPTY_FIELDS:
        return []
    if where in LIST_STRINGS:
        return ["Documented and testable boundary"]
    return "Documented and testable boundary"


def valid_profile():
    p = _shape()
    p["schema"] = {"name": "KestrelTeamContract", "version": "0.1", "status": "DRAFT", "type": "composition-design-not-runtime"}
    p["metadata"].update(team_id="test-team", display_name="Test Team", tagline="A bounded trial", created_on="2026-11-05", origin="Synthetic test fixture", contract_path="teams/test-team/TEAM.md", source_repository="cosmicdance-4-2-0/KestrelGaming")
    p["composition"].update(lead_agent_id="axiom", counterweight_agent_id="flint")
    for member, agent, role in zip(p["composition"]["members"], ["axiom", "flint"], ["lead", "counterweight"]):
        member.update(agent_id=agent, role=role, home_branch=f"agents/{agent}-v1")
    p["execution"]["default_mode"] = "composite"
    p["continuity"]["shared_contract"] = "KESTREL.md"
    return p


def valid_prose():
    return ("# Test Team\n\n**Team ID:** `test-team`  \n**Display name:** Test Team\n\n"
            "| Lead | `agents/axiom-v1` | challenge |\n"
            "| Counterweight | `agents/flint-v1` | falsifier |\n\n"
            + "\n\n".join("## " + heading + "\n\nA concrete, bounded obligation with evidence and scope constraints. "
                           "No member is independently instantiated by this document."
                           for heading in HEADINGS) + "\n")


class TeamContractValidation(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "agents").mkdir()
        self.roster = self.root / "agents/ROSTER_V1.json"
        self.roster.write_text(json.dumps({"members": [
            {"id": "axiom", "branch": "agents/axiom-v1"},
            {"id": "flint", "branch": "agents/flint-v1"},
        ]}), encoding="utf-8")
        self.home = self.root / "teams/test-team"

    def install(self, profile=None, prose=None):
        self.home.mkdir(parents=True, exist_ok=True)
        (self.home / "PROFILE.json").write_text(json.dumps(valid_profile() if profile is None else profile), encoding="utf-8")
        (self.home / "TEAM.md").write_text(valid_prose() if prose is None else prose, encoding="utf-8")

    def expect(self, fragment):
        problems = validate_team_contracts(self.root)
        self.assertTrue(any(fragment in e for e in problems), problems)

    def test_no_team_homes_yet_is_valid(self):
        self.assertEqual(validate_team_contracts(self.root), [])

    def test_optional_catalog_files_are_not_team_homes(self):
        (self.root / "teams").mkdir()
        (self.root / "teams/ROSTER.json").write_text("{}", encoding="utf-8")
        (self.root / "teams/INDEX.md").write_text("# Team catalog\n", encoding="utf-8")
        self.assertEqual(validate_team_contracts(self.root), [])

    def test_positive_fixture_and_read_only(self):
        self.install()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(validate_team_contracts(self.root), [])
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_missing_pair_file(self):
        self.install()
        (self.home / "TEAM.md").unlink()
        self.expect("exactly TEAM.md and PROFILE.json")

    def test_extra_file_rejected(self):
        self.install()
        (self.home / "secrets.txt").write_text("x")
        self.expect("exactly TEAM.md and PROFILE.json")

    def test_invalid_json(self):
        self.install()
        (self.home / "PROFILE.json").write_text("{")
        self.expect("cannot read/parse files")

    def test_metadata_identity_and_date(self):
        p = valid_profile()
        p["metadata"]["team_id"] = "other"
        p["metadata"]["created_on"] = "2026-02-30"
        self.install(p)
        self.expect("team_id/path mismatch")
        self.expect("invalid metadata.created_on")

    def test_wrong_schema_and_unknown_fields(self):
        p = valid_profile()
        p["schema"]["version"] = "0.2"
        self.install(p)
        self.expect("schema.version")
        p["metadata"]["privilege"] = "administrator"
        self.install(p)
        self.expect("unknown fields")

    def test_fewer_than_two_members(self):
        p = valid_profile()
        p["composition"]["members"].pop()
        self.install(p)
        self.expect("at least two members")

    def test_duplicate_and_unregistered_member(self):
        p = valid_profile()
        p["composition"]["members"][1]["agent_id"] = "axiom"
        self.install(p)
        self.expect("duplicate agent_id")
        p = valid_profile()
        p["composition"]["members"][1]["agent_id"] = "unknown"
        self.install(p)
        self.expect("unknown or invalid agent_id")

    def test_member_branch_and_role(self):
        p = valid_profile()
        p["composition"]["members"][0]["home_branch"] = "agents/other-v1"
        self.install(p)
        self.expect("home_branch/roster mismatch")
        p = valid_profile()
        p["composition"]["members"][1]["role"] = "lead"
        self.install(p)
        self.expect("designated counterweight")

    def test_authority_and_runtime_prohibition(self):
        for path, value, fragment in [
            (("authority", "permissions_granted"), ["admin"], "permissions must remain empty"),
            (("authority", "can_delegate_or_vote"), True, "must be false"),
            (("continuity", "team_memory_scope"), "memory/teams", "must be null"),
            (("evaluation", "behavioral_certified"), True, "must be false"),
            (("metadata", "runtime_identity_id"), "fake", "must be null"),
        ]:
            with self.subTest(path=path):
                p = valid_profile()
                p[path[0]][path[1]] = value
                self.install(p)
                self.expect(fragment)

    def test_default_mode_and_required_evidence(self):
        p = valid_profile()
        p["execution"]["default_mode"] = "federated"
        self.install(p)
        self.expect("default_mode")
        p = valid_profile()
        p["evaluation"]["evidence"] = []
        self.install(p)
        self.expect("expected nonempty list")

    def test_incomplete_prose_and_missing_member(self):
        self.install(prose="## Mission and scope\n")
        self.expect("incomplete prose contract")
        self.install(prose=valid_prose().replace("agents/flint-v1", "agents/axiom-v1"))
        self.expect("missing member branch flint")

    def test_placeholder_in_profile(self):
        p = valid_profile()
        p["purpose"]["mission"] = "REPLACE_THIS"
        self.install(p)
        self.expect("expected completed nonempty text")

    def test_template_is_draft_not_an_instance(self):
        template = ROOT / "kestrel/templates/TEAM_PROFILE.json"
        obj = json.loads(template.read_text(encoding="utf-8"))
        self.assertEqual(obj["schema"]["name"], "KestrelTeamContract")
        self.assertEqual(obj["schema"]["status"], "DRAFT")
        self.assertFalse(obj["evaluation"]["behavioral_certified"])


if __name__ == "__main__":
    unittest.main()

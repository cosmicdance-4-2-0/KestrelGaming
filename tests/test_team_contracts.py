"""Synthetic positive/negative tests for team-schema validation; no agent runtime."""
from __future__ import annotations

import json
import re
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
            + "\n\n".join("## " + heading + "\n\nA concrete, bounded obligation with evidence and scope constraints. "
                           "No member is independently instantiated by this document."
                           for heading in HEADINGS) + "\n").replace("## " + HEADINGS[1] + "\n", "## " + HEADINGS[1] + "\n\n| Role | Individual home | Challenge |\n| --- | --- | --- |\n| Lead | `agents/axiom-v1` | challenge |\n| Counterweight | `agents/flint-v1` | falsifier |\n")


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
        (self.root / "teams/INDEX.md").write_text("[Test Team](test-team/TEAM.md)\n", encoding="utf-8")
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

    def test_role_parity_and_exact_branch_tokens(self):
        prose = valid_prose()
        for changed in (
            prose.replace("| Lead |", "| Temporary |").replace("| Counterweight |", "| Lead |").replace("| Temporary |", "| Counterweight |"),
            prose.replace("agents/flint-v1", "agents/flint-v11"),
            prose.replace("| Counterweight |", "| Contributor |"),
        ):
            with self.subTest(changed=changed):
                self.install(prose=changed)
                self.expect("composition roles or branches")
        self.install(prose=prose.replace("| Lead |", "| Lead — Flint |"))
        self.expect("composition role name/branch mismatch")
        self.install(prose=prose + "\n```\n| Lead | `agents/axiom-v1` |\n```\n")
        self.assertEqual(validate_team_contracts(self.root), [])

    def test_three_member_composition_and_extra_row(self):
        p = valid_profile()
        member = dict(p["composition"]["members"][0], agent_id="harbor", role="contributor", home_branch="agents/harbor-v1")
        p["composition"]["members"].append(member)
        self.roster.write_text(json.dumps({"members": [
            {"id": ident, "branch": f"agents/{ident}-v1"} for ident in ("axiom", "flint", "harbor")
        ]}), encoding="utf-8")
        prose = valid_prose().replace("| Counterweight | `agents/flint-v1` | falsifier |", "| Counterweight | `agents/flint-v1` | falsifier |\n| Contributor | `agents/harbor-v1` | recovery |")
        self.install(p, prose)
        self.assertEqual(validate_team_contracts(self.root), [])
        self.install(p, prose.replace("| Contributor | `agents/harbor-v1`", "| Lead | `agents/harbor-v1`"))
        self.expect("composition roles or branches")
        self.install(p, prose.replace("| Contributor | `agents/harbor-v1` | recovery |", ""))
        self.expect("missing member branch harbor")
        self.install(p, prose.replace("| Contributor | `agents/harbor-v1` | recovery |", "| Contributor | `agents/harbor-v1` | recovery |\n| Contributor | `agents/harbor-v1` | duplicate |"))
        self.expect("composition roles or branches")

    def test_catalog_registration_requires_real_operative_link(self):
        self.install()
        index = self.root / "teams/INDEX.md"
        for contents in ("# No registration", "[Wrong](other/TEAM.md)", "```\n[Test](test-team/TEAM.md)\n```", "`[Test](test-team/TEAM.md)`"):
            index.write_text(contents, encoding="utf-8")
            self.expect("missing team registration")
        index.unlink()
        self.expect("missing team registration")

    def test_duplicate_json_keys_rejected_at_any_depth(self):
        self.install()
        path = self.home / "PROFILE.json"
        path.write_text(path.read_text().replace('"name": "KestrelTeamContract"', '"name": "wrong", "name": "KestrelTeamContract"', 1))
        self.expect("duplicate JSON key: name")
        self.install()
        self.roster.write_text(self.roster.read_text().replace('"members": [', '"members": [], "members": [', 1))
        self.expect("duplicate JSON key: members")

    def test_fenced_sections_and_fenced_composition_are_not_operative(self):
        for fence in ("```", "~~~~"):
            with self.subTest(fence=fence):
                self.install(prose=valid_prose().replace("## Evaluation", fence + "\n## Evaluation\n" + fence))
                self.expect("missing section Evaluation")
                prose = valid_prose().replace("| Lead | `agents/axiom-v1` | challenge |", fence + "\n| Lead | `agents/axiom-v1` | challenge |\n" + fence)
                self.install(prose=prose)
                self.expect("missing member branch axiom")

    def test_identity_spacing_and_exact_match(self):
        prose = valid_prose().replace("**Team ID:** `test-team`", "**Team ID:**   `test-team`").replace("**Display name:** Test Team", "**Display name:**   Test Team   ")
        self.install(prose=prose)
        self.assertEqual(validate_team_contracts(self.root), [])
        self.install(prose=prose.replace("Test Team   ", "Test Team Extra   "))
        self.expect("identity/profile mismatch")
        self.install(prose=prose + "\n**Team ID:** `other`\n")
        self.expect("identity/profile mismatch")

    def test_dangling_teams_symlink_rejected(self):
        (self.root / "teams").symlink_to(self.root / "missing")
        self.expect("expected a regular directory")

    def test_duplicate_composition_sections(self):
        section = valid_prose().split("## " + HEADINGS[1], 1)[1].split("## Working method", 1)[0]
        for prefix, suffix in (("", ""), ("  ", " ##")):
            with self.subTest(prefix=prefix):
                self.install(prose=valid_prose() + "\n" + prefix + "## " + HEADINGS[1] + suffix + section.replace("| Lead |", "| Contributor |"))
                self.expect("exactly one operative Composition section")

    def test_hidden_table_and_required_heading(self):
        prose = valid_prose()
        table = "\n".join(line for line in prose.splitlines() if line.startswith("|"))
        for hidden in ("<!--\n" + table + "\n-->", "\n".join("    " + line for line in table.splitlines()), "\n".join("\t" + line for line in table.splitlines())):
            self.install(prose=prose.replace(table, hidden))
            self.expect("composition table")
        self.install(prose=prose.replace("## Evaluation", "<!--\n## Evaluation\n-->"))
        self.expect("missing section Evaluation")

    def test_catalog_hidden_images_and_escaped_links(self):
        self.install()
        link = "[Test Team](test-team/TEAM.md)"
        for text in ("<!-- " + link + " -->", "!" + link, "    " + link, "\t" + link, "\\" + link):
            with self.subTest(text=text):
                (self.root / "teams/INDEX.md").write_text(text)
                self.expect("missing team registration")

    def test_catalog_safe_link_variants(self):
        self.install()
        for target in ("test-team/TEAM.md", "./test-team/TEAM.md"):
            for title in ("", ' "Founding team"', " 'Founding team'"):
                (self.root / "teams/INDEX.md").write_text(f"[Test Team]({target}{title})")
                self.assertEqual(validate_team_contracts(self.root), [])

    def test_table_header_separator_and_contiguous_rows(self):
        prose = valid_prose()
        for changed in (
            prose.replace("| Role | Individual home | Challenge |\n| --- | --- | --- |\n", ""),
            prose.replace("| --- | --- | --- |", "| - | - | - |"),
            prose.replace("| Counterweight |", "\n| Counterweight |"),
            prose.replace("| Role |", "### Example\n\n| Role |"),
            prose.replace("| Lead | `agents/axiom-v1` | challenge |", "| Lead | `agents/axiom-v1` |"),
            prose.replace("## Working method", "| Lead | `agents/axiom-v1` | alternative |\n\n## Working method"),
        ):
            self.install(prose=changed)
            self.expect("composition table")

    def test_benign_comments_and_fenced_examples(self):
        prose = valid_prose()
        example = "\n~~~~\n<!-- unclosed example\n## " + HEADINGS[1] + "\n| Lead | `agents/flint-v1` |\n~~~~\n"
        self.install(prose=prose + example + "\n<!--\n```\n## Evaluation\n-->\n")
        self.assertEqual(validate_team_contracts(self.root), [])
        self.install(prose=prose.replace("## " + HEADINGS[1] + "\n", "## " + HEADINGS[1] + "\n\n<!-- membership follows -->\n"))
        self.assertEqual(validate_team_contracts(self.root), [])
        self.install(prose=prose + "\nAn inline example: `<!--` and `-->`.\n")
        self.assertEqual(validate_team_contracts(self.root), [])

    def test_unclosed_comment_fails_closed(self):
        self.install(prose=valid_prose() + "\n<!-- unfinished")
        self.expect("unclosed HTML comment")
        self.install()
        (self.root / "teams/INDEX.md").write_text("[Test](test-team/TEAM.md)\n<!-- unfinished")
        self.expect("unclosed HTML comment")

    def test_populated_two_member_template(self):
        prose = (ROOT / "kestrel/templates/TEAM_CONTRACT.md").read_text(encoding="utf-8")
        values = {"REPLACE_TEAM_ID": "test-team", "REPLACE_TEAM_NAME": "Test Team",
                  "REPLACE_LEAD_ID": "axiom", "REPLACE_COUNTERWEIGHT_ID": "flint"}
        # The template introduction contains illustrative placeholder notation.
        prose = prose[prose.index("**Team ID:**"):]
        prose = re.sub(r"REPLACE_[A-Z_]+", lambda m: values.get(m.group(), "A bounded obligation"), prose)
        self.install(prose=prose)
        self.assertEqual(validate_team_contracts(self.root), [])

    def test_linked_home_destination_matches_canonical_locator(self):
        branch = "agents/axiom-v1"
        canonical = "https://github.com/cosmicdance-4-2-0/KestrelGaming/tree/" + branch
        self.install(prose=valid_prose().replace(f"`{branch}`", f"[`{branch}`]({canonical})"))
        self.assertEqual(validate_team_contracts(self.root), [])
        for target in (
            canonical.replace("axiom-v1", "flint-v1"),
            canonical.replace("cosmicdance-4-2-0", "unrelated-owner"),
            canonical.replace("KestrelGaming", "another-repo"),
            "elsewhere", "javascript:alert", canonical + "?redirect=elsewhere",
        ):
            with self.subTest(target=target):
                self.install(prose=valid_prose().replace(f"`{branch}`", f"[`{branch}`]({target})"))
                self.expect("home link destination/branch mismatch")

    def test_catalog_multiline_inline_code_is_not_navigation(self):
        self.install()
        index = self.root / "teams/INDEX.md"
        link = "[Test Team](test-team/TEAM.md)"
        for ticks in ("`", "``", "````"):
            with self.subTest(ticks=ticks):
                example = f"Example: {ticks}not a link\n{link}\nstill not a link{ticks}"
                index.write_text(example)
                self.expect("missing team registration")
                index.write_text(example + "\n\n" + link)
                self.assertEqual(validate_team_contracts(self.root), [])

    def test_catalog_raw_html_cannot_supply_navigation(self):
        self.install()
        index = self.root / "teams/INDEX.md"
        link = "[Test Team](test-team/TEAM.md)"
        for markup in (
            f'<div data-note="{link}"></div>',
            f'<div title=">" data-note="{link}"></div>',
            f'<div\n data-note="{link}"></div>',
            f'<div>\n{link}\n</div>',
        ):
            with self.subTest(markup=markup):
                index.write_text(markup)
                self.expect("missing team registration")
                # HTML examples in code are permitted beside real navigation.
                index.write_text("Example: `" + markup + "`\n\n" + link)
                self.assertEqual(validate_team_contracts(self.root), [])

    def test_template_is_draft_not_an_instance(self):
        template = ROOT / "kestrel/templates/TEAM_PROFILE.json"
        obj = json.loads(template.read_text(encoding="utf-8"))
        self.assertEqual(obj["schema"]["name"], "KestrelTeamContract")
        self.assertEqual(obj["schema"]["status"], "DRAFT")
        self.assertFalse(obj["evaluation"]["behavioral_certified"])


if __name__ == "__main__":
    unittest.main()

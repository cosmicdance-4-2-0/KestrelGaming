"""Regression tests for the DOC-STD-001 bootstrap/validator and the STE guard."""
from __future__ import annotations

import contextlib
import hashlib
import io
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


docstd = load("docstd", ROOT / "skills/kestrel-documentation-maintenance/scripts/docstd.py")
ste = load("ste_check", ROOT / "skills/kestrel-technical-writing-ste100/scripts/ste_check.py")


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), "-c", "user.email=test@example.invalid", "-c", "user.name=Test",
                           "-c", "commit.gpgsign=false", "-c", "tag.gpgsign=false", *args],
                          check=True, capture_output=True, text=True).stdout.strip()


class Workspace(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, rel: str, text: str):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def init_git(self):
        git(self.root, "init", "-q", "-b", "main")

    def commit(self, message: str) -> str:
        git(self.root, "add", "-A")
        git(self.root, "commit", "-q", "--allow-empty", "-m", message)
        return git(self.root, "rev-parse", "HEAD")

    def merge_pr(self, number: int, rel: str, text: str) -> str:
        git(self.root, "switch", "-q", "-c", f"pr{number}")
        self.write(rel, text)
        self.commit(f"change for PR {number}")
        git(self.root, "switch", "-q", "main")
        git(self.root, "merge", "-q", "--no-ff", f"pr{number}", "-m", f"Merge pull request #{number} from x/pr{number}")
        return git(self.root, "rev-parse", "HEAD")

    def bootstrap(self):
        docstd.apply_init(self.root, docstd.plan_init(self.root))
        for name in docstd.CORE_NAMES:   # simulate owner review of templates
            path = self.root / name
            path.write_text("\n".join(l for l in path.read_text().splitlines() if docstd.TEMPLATE_MARKER not in l) + "\n")

    def findings(self, level=None, check=None, ref="HEAD"):
        report = docstd.run_check(self.root, ref)
        return [i for i in report.items if (level is None or i["level"] == level)
                and (check is None or i["check"] == check)], report


class BootstrapTests(Workspace):
    def test_creates_seven_documents_with_exact_names(self):
        plan = docstd.apply_init(self.root, docstd.plan_init(self.root))
        self.assertEqual([i["action"] for i in plan], ["created"] * 7)
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), sorted(docstd.CORE_NAMES))

    def test_repeated_bootstrap_is_idempotent(self):
        docstd.apply_init(self.root, docstd.plan_init(self.root))
        before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.iterdir()}
        second = docstd.apply_init(self.root, docstd.plan_init(self.root))
        after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.iterdir()}
        self.assertEqual(before, after)
        self.assertEqual({i["action"] for i in second}, {"keep"})

    def test_owner_edits_are_never_overwritten(self):
        self.write("README.md", "# Owner text\n\nKeep me.\n")
        plan = docstd.apply_init(self.root, docstd.plan_init(self.root))
        self.assertEqual((self.root / "README.md").read_text(), "# Owner text\n\nKeep me.\n")
        self.assertEqual(next(i for i in plan if i["path"] == "README.md")["action"], "keep")

    def test_wrong_case_variant_blocks_creation(self):
        self.write("CHANGELOG.md", "# Changes\n")
        plan = docstd.apply_init(self.root, docstd.plan_init(self.root))
        item = next(i for i in plan if i["path"] == "Changelog.md")
        self.assertEqual(item["action"], "review")
        self.assertIn("CHANGELOG.md", item["reason"])
        self.assertEqual([p.name for p in self.root.iterdir() if p.name.casefold() == "changelog.md"],
                         ["CHANGELOG.md"])

    def test_equivalent_at_nonstandard_path_is_not_duplicated(self):
        self.write("docs/ROADMAP.md", "# Roadmap\n")
        plan = docstd.apply_init(self.root, docstd.plan_init(self.root))
        self.assertEqual(next(i for i in plan if i["path"] == "ROADMAP.md")["action"], "review")
        self.assertFalse((self.root / "ROADMAP.md").exists())

    def test_declared_location_is_kept(self):
        self.write("docs/ROADMAP.md", "# Roadmap\n")
        self.write(".docstd.json", json.dumps({"schema": 1, "locations": {
            "ROADMAP.md": {"path": "docs/ROADMAP.md", "reason": "migration deferred"}}}))
        plan = docstd.plan_init(self.root)
        self.assertEqual(next(i for i in plan if i["path"] == "docs/ROADMAP.md")["action"], "keep")

    def test_dry_run_writes_nothing(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(docstd.main(["init", str(self.root)]), 0)
        self.assertEqual(list(self.root.iterdir()), [])


class CheckTests(Workspace):
    def test_clean_bootstrap_passes(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        found, report = self.findings()
        self.assertEqual(report.overall(), "PASS", found)

    def test_template_marker_requires_review(self):
        self.init_git()
        docstd.apply_init(self.root, docstd.plan_init(self.root))
        self.commit("init")
        self.assertEqual(len(self.findings("REVIEW", "template")[0]), 7)

    def test_wrong_filename_case_fails(self):
        self.init_git()
        self.bootstrap()
        (self.root / "devlog.md").rename(self.root / "DEVLOG.md")
        self.commit("init")
        fails = self.findings("FAIL", "case")[0]
        self.assertEqual([f["path"] for f in fails], ["DEVLOG.md"])

    def test_case_fold_collision_in_index_fails(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        blob = subprocess.run(["git", "-C", str(self.root), "hash-object", "-w", "--stdin"], input="x\n",
                              capture_output=True, text=True, check=True).stdout.strip()
        git(self.root, "update-index", "--add", "--cacheinfo", f"100644,{blob},readme.md")
        fails = self.findings("FAIL", "case-collision")[0]
        self.assertEqual(len(fails), 1)
        self.assertIn("README.md", fails[0]["message"])
        self.assertIn("readme.md", fails[0]["message"])

    def test_link_case_mismatch_fails_even_on_case_insensitive_hosts(self):
        self.bootstrap()
        self.write("guide.md", "See [readme](readme.md).\n")
        fails = self.findings("FAIL", "links")[0]
        self.assertEqual(len(fails), 1)
        self.assertIn("Case mismatch", fails[0]["message"])

    def test_broken_fragment_fails_and_valid_fragment_passes(self):
        self.bootstrap()
        self.write("guide.md", "# Guide\n\n## 2.1 Schema discipline\n\n[ok](#21-schema-discipline) "
                   "[ok](README.md#setup-and-usage) [bad](README.md#no-such-heading)\n")
        fails = self.findings("FAIL", "links")[0]
        self.assertEqual([f["message"] for f in fails], ["Broken fragment #no-such-heading in README.md."])

    def test_duplicate_headings_get_numbered_anchors(self):
        self.assertEqual(docstd.anchors("## Notes\n\n## Notes\n"), {"notes", "notes-1"})

    def test_links_in_code_are_ignored(self):
        self.bootstrap()
        self.write("guide.md", "```\n[x](missing.md)\n```\n\nUse `[x](missing.md)` literally.\n")
        self.assertEqual(self.findings("FAIL", "links")[0], [])

    def test_malformed_link_requires_review(self):
        self.bootstrap()
        self.write("guide.md", "Beyond the [accepted copy] (revised)(content/COPY.md).\n")
        self.assertEqual(len(self.findings("REVIEW", "links")[0]), 1)

    def test_stale_accepted_baseline_reference(self):
        self.init_git()
        self.bootstrap()
        base = self.commit("init")
        self.write("README.md", (self.root / "README.md").read_text() +
                   f"\n**Status:** accepted baseline `main@{base[:7]}`.\n")
        self.commit("status")
        self.merge_pr(7, "feature.txt", "x\n")
        stale = self.findings("REVIEW", "baseline")[0]
        self.assertEqual(len(stale), 1)
        self.assertIn("Merge pull request #7", stale[0]["message"])

    def test_current_baseline_reference_passes(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        head = self.merge_pr(3, "feature.txt", "x\n")
        self.write("README.md", (self.root / "README.md").read_text() + f"\nCurrent baseline: main@{head[:7]}.\n")
        self.commit("status")
        self.assertEqual(self.findings("REVIEW", "baseline")[0], [])

    def test_old_checkpoint_beside_current_head_is_not_stale(self):
        self.init_git()
        self.bootstrap()
        base = self.commit("init")
        head = self.merge_pr(4, "feature.txt", "x\n")
        self.write("README.md", (self.root / "README.md").read_text() +
                   f"\nStatus: accepted checkpoint main@{base[:7]}; latest merge main@{head[:7]} is not yet accepted.\n")
        self.commit("status")
        self.assertEqual(self.findings("REVIEW", "baseline")[0], [])

    def test_historical_verification_presented_as_current_requires_review(self):
        self.init_git()
        self.bootstrap()
        self.write("README.md", (self.root / "README.md").read_text() + "\nChanges must pass CI before merge.\n"
                   "All tests pass.\nCI passed on 2026-11-20 for main@abc1234.\n")
        self.commit("claims")
        flagged = self.findings("REVIEW", "verification")[0]
        self.assertEqual([f["line"] for f in flagged], [len((self.root / "README.md").read_text().splitlines()) - 1])

    def test_merged_but_unreleased_work_in_changelog_fails(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        self.merge_pr(1, "a.txt", "a\n")
        git(self.root, "tag", "v1.0.0")
        self.merge_pr(2, "b.txt", "b\n")
        self.write("Changelog.md", "# Changelog\n\n## 1.0.0\n\n- Added A (#1).\n- Added B (#2).\n")
        self.commit("changelog")
        fails = self.findings("FAIL", "changelog")[0]
        self.assertEqual(len(fails), 1)
        self.assertIn("PR #2", fails[0]["message"])

    def test_release_entry_without_tag_requires_review(self):
        self.init_git()
        self.bootstrap()
        self.write("Changelog.md", "# Changelog\n\n## 2.0.0\n\n- Something.\n")
        self.commit("changelog")
        self.assertEqual(len(self.findings("REVIEW", "changelog")[0]), 1)

    def test_devlog_out_of_order_fails(self):
        self.bootstrap()
        self.write("devlog.md", "# Development log\n\n## 2026-11-02 — B\n\n- Ref: #2\n\n"
                   "## 2026-11-01 — A\n\n- Ref: #1\n\n## 2026-11-03 — C\n\n- Ref: #3\n")
        self.assertEqual(len(self.findings("FAIL", "devlog")[0]), 1)

    def test_unavailable_git_evidence_is_not_reported_as_pass(self):
        self.bootstrap()   # no Git repository
        found, report = self.findings()
        self.assertEqual(report.overall(), "INDETERMINATE")
        self.assertTrue(any(i["level"] == "UNVERIFIED" and i["check"] == "git" for i in found))
        self.assertFalse(any(i["level"] == "PASS" and i["check"] in ("baseline", "changelog") for i in found))
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(docstd.main(["check", str(self.root)]), 2)
        self.assertIn("Overall: INDETERMINATE", output.getvalue())

    def test_declared_location_and_root_copy_conflict(self):
        self.bootstrap()
        self.write("docs/ROADMAP.md", "# Roadmap\n")
        self.write(".docstd.json", json.dumps({"schema": 1, "locations": {
            "ROADMAP.md": {"path": "docs/ROADMAP.md", "reason": "deferred"}}}))
        self.assertEqual(len(self.findings("FAIL", "authority")[0]), 1)

    def test_invalid_config_fails(self):
        self.bootstrap()
        self.write(".docstd.json", "{not json")
        self.assertEqual(len(self.findings("FAIL", "config")[0]), 1)


class SteGuardTests(unittest.TestCase):
    def test_identifier_change_is_rejected(self):
        old = "Call `Assets.load()` before `app.init()`. Set maxFPS to 60 Hz."
        new = "Call `Assets.loadAll()` before `app.init()`. Set maxFPS to 60 Hz."
        problems = ste.protected_diff(old, new)
        self.assertTrue(any("Assets.load()" in p for p in problems))

    def test_unit_and_number_change_is_rejected(self):
        problems = ste.protected_diff("Wait 30 s before you retry.", "Wait 30 ms before you retry.")
        self.assertTrue(problems)

    def test_plain_wording_change_is_accepted(self):
        old = "The `vnu` checker is utilized in order to validate `dist/index.html`."
        new = "The `vnu` checker validates `dist/index.html`."
        self.assertEqual(ste.protected_diff(old, new), [])

    def test_lint_flags_long_procedural_sentence_and_avoided_term(self):
        text = ("1. Open the panel and then carefully select every option that is shown in the list before you "
                "continue with the next step of the procedure.\n")
        findings = ste.lint(text, {"utilize": "use"})
        self.assertTrue(any("words" in f["message"] for f in findings))
        self.assertTrue(any("utilize" in f["message"] for f in ste.lint("Utilize the tool.", {"utilize": "use"})))

    def test_lint_never_claims_compliance(self):
        output = subprocess.run(["python3", str(ROOT / "skills/kestrel-technical-writing-ste100/scripts/ste_check.py"),
                                 "lint", "-"], input="Open the valve.\n", capture_output=True, text=True)
        self.assertNotIn("compliant", output.stdout.replace("not proof of ASD-STE100 compliance", ""))


class SkillPackagingTests(unittest.TestCase):
    def test_new_skills_are_self_contained(self):
        for name in ("kestrel-documentation-maintenance", "kestrel-technical-writing-ste100"):
            skill = ROOT / "skills" / name
            for md in skill.rglob("*.md"):
                for target in docstd.link_targets(md.read_text(encoding="utf-8")):
                    raw = target[1].split("#", 1)[0]
                    if not raw or docstd.SCHEME.match(raw):
                        continue
                    resolved = (md.parent / raw).resolve()
                    sibling = resolved.is_relative_to(ROOT / "skills") and resolved.name == "SKILL.md"
                    self.assertTrue(resolved.is_relative_to(skill) or sibling, f"{md}: {raw}")

    def test_templates_match_core_manifest(self):
        templates = ROOT / "skills/kestrel-documentation-maintenance/assets/templates"
        self.assertEqual(sorted(p.name for p in templates.iterdir()), sorted(docstd.CORE_NAMES))


if __name__ == "__main__":
    unittest.main()

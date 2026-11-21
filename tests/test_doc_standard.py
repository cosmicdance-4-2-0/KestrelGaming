"""Regression tests for the DOC-STD-001 bootstrap/validator and the STE guard."""
from __future__ import annotations

import contextlib
import hashlib
import io
import importlib.util
import json
from pathlib import Path
import re
import shutil
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

    def findings(self, level=None, check=None, ref=None, remote=None):
        report = docstd.run_check(self.root, ref, remote)
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
    def test_clean_bootstrap_leaves_only_the_release_question(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        found, report = self.findings()
        self.assertEqual(report.overall(), "REVIEW", found)
        open_items = [(i["level"], i["check"]) for i in found if i["level"] != "PASS"]
        self.assertEqual(open_items, [("REVIEW", "changelog")])   # absence of tags is not proof of no release

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

    def test_release_entry_without_local_tag_is_unverified_offline(self):
        self.init_git()
        self.bootstrap()
        self.write("Changelog.md", "# Changelog\n\n## 2.0.0\n\n- Something.\n")
        self.commit("changelog")
        found, report = self.findings(check="changelog")
        self.assertEqual([i["level"] for i in found], ["UNVERIFIED"])
        self.assertEqual(report.overall(), "INDETERMINATE")

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


class CommittedContentTests(Workspace):
    """Correction B: the working tree is not the committed deliverable."""

    def ignored_target_repo(self):
        self.init_git()
        self.bootstrap()
        self.write(".gitignore", "build/\n")
        self.write("guide.md", "See [the report](build/report.md).\n")
        self.commit("guide links to an ignored file")
        self.write("build/report.md", "# Report\n")       # exists locally, never committed

    def test_link_to_ignored_local_file_fails_in_working_tree(self):
        self.ignored_target_repo()
        links, report = self.findings(check="links")
        self.assertEqual([(i["level"], i["path"]) for i in links if i["level"] != "PASS"], [("FAIL", "guide.md")])
        self.assertIn("ignored", links[0]["message"])
        self.assertIn("working tree", report.source["documents"])

    def test_link_to_ignored_local_file_fails_at_revision(self):
        self.ignored_target_repo()
        self.assertEqual(git(self.root, "ls-tree", "-r", "--name-only", "HEAD", "build"), "")
        links, report = self.findings(check="links", ref="HEAD")
        self.assertEqual([i["level"] for i in links], ["FAIL"])
        self.assertIn("not in this revision", links[0]["message"])
        self.assertIn("Git revision", report.source["documents"])

    def test_generated_policy_turns_ignored_target_into_review(self):
        self.ignored_target_repo()
        self.write(".docstd.json", json.dumps({"schema": 1, "generated": ["build/**"]}))
        self.commit("declare generated output")
        levels = [i["level"] for i in self.findings(check="links")[0] if i["level"] != "PASS"]
        self.assertEqual(levels, ["REVIEW"])

    def test_revision_mode_reads_committed_text_not_working_tree(self):
        self.init_git()
        self.bootstrap()
        self.write("guide.md", "See [missing](missing.md).\n")
        self.commit("broken link committed")
        self.write("guide.md", "See [readme](README.md).\n")   # fixed only in the working tree
        self.assertEqual(self.findings("FAIL", "links")[0], [])
        committed = self.findings("FAIL", "links", ref="HEAD")[0]
        self.assertEqual([i["message"] for i in committed], ["Broken relative link: missing.md"])

    def test_untracked_target_of_tracked_document_requires_review(self):
        self.init_git()
        self.bootstrap()
        self.write("guide.md", "See [notes](notes.md).\n")
        self.commit("guide")
        self.write("notes.md", "# Notes\n")                   # not yet committed
        reviews = self.findings("REVIEW", "links")[0]
        self.assertEqual(len(reviews), 1)
        self.assertIn("untracked", reviews[0]["message"])

    def test_unknown_revision_checks_nothing_and_passes_nothing(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        found, report = self.findings(ref="no-such-ref")
        self.assertEqual([i["level"] for i in found], ["UNVERIFIED"])
        self.assertEqual(report.overall(), "INDETERMINATE")

    def test_cli_reports_document_source(self):
        self.init_git()
        self.bootstrap()
        self.commit("init")
        with contextlib.redirect_stdout(io.StringIO()) as output:
            docstd.main(["check", str(self.root), "--ref", "HEAD"])
        self.assertIn("Documents: Git revision", output.getvalue())
        with contextlib.redirect_stdout(io.StringIO()) as output:
            docstd.main(["check", str(self.root), "--json"])
        self.assertIn("working tree", json.loads(output.getvalue())["source"]["documents"])


class ReleaseEvidenceTests(Workspace):
    """Correction C: missing local tags never establish that no public release exists."""

    def release_repo(self, changelog: str, tag: str | None = None):
        self.init_git()
        self.bootstrap()
        self.write("Changelog.md", changelog)
        self.commit("init")
        if tag:
            git(self.root, "tag", tag)

    def bare_remote(self, push_tags: bool):
        remote = self.root / ".." / (self.root.name + "-remote.git")
        git(self.root.parent, "init", "-q", "--bare", str(remote))
        self.addCleanup(subprocess.run, ["rm", "-rf", str(remote)])
        git(self.root, "remote", "add", "origin", str(remote))
        git(self.root, "push", "-q", "origin", "main", *(["--tags"] if push_tags else []))
        return remote

    def levels(self, **kwargs):
        return [i["level"] for i in self.findings(check="changelog", **kwargs)[0]]

    def test_no_tags_in_full_clone_requires_owner_review(self):
        self.release_repo("# Changelog\n\nNo public release has been published.\n")
        found = self.findings(check="changelog")[0]
        self.assertEqual([i["level"] for i in found], ["REVIEW"])
        self.assertIn("does not prove", found[0]["message"])

    def test_shallow_clone_is_unverified(self):
        self.release_repo("# Changelog\n\nNo public release has been published.\n")
        clone = Path(tempfile.mkdtemp())
        self.addCleanup(subprocess.run, ["rm", "-rf", str(clone)])
        subprocess.run(["git", "clone", "-q", "--depth", "1", f"file://{self.root}", str(clone / "c")], check=True)
        report = docstd.run_check(clone / "c")
        self.assertEqual([i["level"] for i in report.items if i["check"] == "changelog"], ["UNVERIFIED"])

    def test_unreachable_remote_is_unverified(self):
        self.release_repo("# Changelog\n\nNo public release has been published.\n")
        git(self.root, "remote", "add", "origin", str(self.root / "no-such-remote.git"))
        self.assertEqual(self.levels(remote="origin"), ["UNVERIFIED"])

    def test_version_missing_locally_and_on_remote_requires_review(self):
        self.release_repo("# Changelog\n\n## 1.0.0\n\n- First release.\n")
        self.bare_remote(push_tags=False)
        self.assertEqual(self.levels(remote="origin"), ["REVIEW"])

    def test_remote_only_tag_requires_fetch_not_pass(self):
        self.release_repo("# Changelog\n\n## 1.0.0\n\n- First release.\n", tag="v1.0.0")
        self.bare_remote(push_tags=True)
        git(self.root, "tag", "-d", "v1.0.0")                 # local checkout without tags
        found = self.findings(check="changelog", remote="origin")[0]
        self.assertEqual([i["level"] for i in found], ["REVIEW"])
        self.assertIn("exists on the remote but not locally", found[0]["message"])

    def test_remote_tags_do_not_hide_an_unlisted_release(self):
        self.release_repo("# Changelog\n\nNo public release has been published.\n", tag="v0.1.0")
        self.assertEqual(self.levels(), ["REVIEW"])

    def test_local_tag_with_contained_work_passes(self):
        self.release_repo("# Changelog\n\n## 1.0.0\n\n- First release.\n", tag="v1.0.0")
        self.assertEqual(self.levels(), ["PASS"])


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


NEW_SKILLS = ("kestrel-documentation-maintenance", "kestrel-technical-writing-ste100")


def frontmatter(text: str) -> dict:
    head = text.split("---", 2)[1]
    return dict(line.split(": ", 1) for line in head.strip().splitlines())


class SkillPackagingTests(unittest.TestCase):
    """Correction A: each new skill works when its folder is installed alone."""

    def install_alone(self, name: str) -> Path:
        home = Path(tempfile.mkdtemp())           # a host skills folder holding only this skill
        self.addCleanup(subprocess.run, ["rm", "-rf", str(home)])
        target = home / "skills" / name
        shutil.copytree(ROOT / "skills" / name, target)
        return target

    def test_isolated_install_has_no_unresolved_references(self):
        for name in NEW_SKILLS:
            skill = self.install_alone(name)
            for md in skill.rglob("*.md"):
                for line, raw in docstd.link_targets(md.read_text(encoding="utf-8")):
                    path = raw.split("#", 1)[0]
                    if not path or docstd.SCHEME.match(path):
                        continue
                    resolved = (md.parent / path).resolve()
                    self.assertTrue(resolved.is_relative_to(skill.resolve()) and resolved.exists(),
                                    f"{name}: {md.relative_to(skill)}:{line} -> {raw}")

    def test_isolated_documentation_skill_runs_its_tool(self):
        skill = self.install_alone("kestrel-documentation-maintenance")
        repo = Path(tempfile.mkdtemp())
        self.addCleanup(subprocess.run, ["rm", "-rf", str(repo)])
        script = skill / "scripts" / "docstd.py"
        applied = subprocess.run(["python3", str(script), "init", str(repo), "--apply"], capture_output=True, text=True)
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        self.assertEqual(sorted(p.name for p in repo.iterdir()), sorted(docstd.CORE_NAMES))
        checked = subprocess.run(["python3", str(script), "check", str(repo)], capture_output=True, text=True)
        self.assertIn("Overall:", checked.stdout)

    def test_isolated_writing_skill_runs_its_tool(self):
        skill = self.install_alone("kestrel-technical-writing-ste100")
        work = Path(tempfile.mkdtemp())
        self.addCleanup(subprocess.run, ["rm", "-rf", str(work)])
        (work / "a.md").write_text("Run `make test`.\n")
        (work / "b.md").write_text("Run `make check`.\n")
        result = subprocess.run(["python3", str(skill / "scripts" / "ste_check.py"), "protect",
                                 str(work / "a.md"), str(work / "b.md")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)

    def test_descriptions_declare_every_other_skill_they_use(self):
        all_skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        for name in NEW_SKILLS:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            description = frontmatter(text)["description"]
            body = text.split("---", 2)[2]
            for other in sorted(all_skills - {name}):
                if re.search(rf"\b{re.escape(other)}\b", body):
                    self.assertIn(other, description, f"{name} uses {other} without declaring it")
                    self.assertRegex(description, r"(?i)optional", f"{name}: say whether {other} is optional")

    def test_templates_match_core_manifest(self):
        templates = ROOT / "skills/kestrel-documentation-maintenance/assets/templates"
        self.assertEqual(sorted(p.name for p in templates.iterdir()), sorted(docstd.CORE_NAMES))


if __name__ == "__main__":
    unittest.main()

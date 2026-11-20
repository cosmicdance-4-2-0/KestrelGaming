#!/usr/bin/env python3
"""Kestrel documentation standard (DOC-STD-001): bootstrap and validation.

Python 3.9+, standard library only. Run from any directory.

  init  [ROOT] [--apply] [--json]
        Plan the seven core documents. The default prints a plan and writes nothing.
        --apply creates only documents that are missing, have no case variant, and
        have no equivalent at another path. It never overwrites a file.
  check [ROOT] [--ref REF] [--json] [--strict]
        Report findings at four levels:
          PASS        verified automatically
          FAIL        a definite discrepancy
          REVIEW      a person must decide; the tool cannot verify it
          UNVERIFIED  the evidence needed for the check is not available

Exit status for check: 0 = no FAIL and no UNVERIFIED (REVIEW items may remain),
1 = at least one FAIL (with --strict, REVIEW also counts as failure),
2 = no FAIL, but some evidence is UNVERIFIED.
Exit status for init: 0 = plan complete; 1 = some items need review. Conflicting
items are never written.

The checks are structural and heuristic. A PASS does not prove that the text is
accurate. Optional per-repository exceptions go in ROOT/.docstd.json; see the
standard in ../references/DOC_STANDARD.md.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import unquote

CORE = (
    ("README.md", "Project identity, current capabilities, usage, setup, and navigation"),
    ("AGENTS.md", "Binding agent/developer contracts, safeguards, and one global Definition of Done"),
    ("ROADMAP.md", "Milestones, planned work, accepted outcomes, and deferrals"),
    ("Changelog.md", "User-facing changes between public releases"),
    ("devlog.md", "Developer/agent-facing engineering chronology"),
    ("DECISIONS.md", "Accepted decisions, authority, rationale, and supersession"),
    ("VERSIONING.md", "Version syntax, compatibility policy, release boundaries, and revision rules"),
)
CORE_NAMES = tuple(name for name, _ in CORE)
# Other basenames (case-folded) that can hold the same responsibility. README and
# AGENTS are absent on purpose: nested copies of those files are normal.
ALIASES = {
    "ROADMAP.md": {"roadmap.md"},
    "Changelog.md": {"changelog.md", "changes.md", "release-notes.md", "release_notes.md"},
    "devlog.md": {"devlog.md", "dev-log.md", "worklog.md", "work-log.md", "development-log.md"},
    "DECISIONS.md": {"decisions.md", "decision-log.md", "decision_log.md"},
    "VERSIONING.md": {"versioning.md", "version-policy.md"},
}
# Living documents that make current-state claims. Changelog, devlog and DECISIONS
# are dated records, so they are not checked for stale "current" claims.
CURRENT_STATE_DOCS = ("README.md", "AGENTS.md", "ROADMAP.md", "VERSIONING.md")
TEMPLATE_MARKER = "<!-- docstd:template"
TEMPLATES = Path(__file__).resolve().parent.parent / "assets" / "templates"
SKIP_DIRS = {".git", "node_modules"}
LEVELS = ("FAIL", "UNVERIFIED", "REVIEW", "PASS")

SHA = r"[0-9a-f]{7,40}"
BRANCH_SHA = re.compile(r"(?<![\w/])[A-Za-z][\w.-]*@(" + SHA + r")\b")
URL_SHA = re.compile(r"github\.com/([\w.-]+)/([\w.-]+)/(?:commit|tree)/(" + SHA + r")\b", re.I)
PR_REF = re.compile(r"(?:\bPR\s*#|/pull/|(?<![\w&])#)(\d+)\b")
CURRENT_CLAIM = re.compile(
    r"\b(current(?:ly)?|latest|now|status|accepted (?:baseline|checkpoint|code))\b", re.I)
VERIFICATION_CLAIM = re.compile(
    r"\b(tests?|checks?|CI|builds?|validation)\b[^.\n]{0,60}\b(pass(?:es|ed|ing)?|green|succeed(?:s|ed)?)\b"
    r"|\b(pass(?:es|ed|ing)?|green)\b[^.\n]{0,30}\b(tests?|checks?|CI)\b", re.I)
EVIDENCE_MARK = re.compile(
    r"\b" + SHA + r"\b|/actions/runs/\d+|\b\d{4}-\d{2}-\d{2}\b|\bas of\b|\brun \d+\b", re.I)
DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
VERSION_HEADING = re.compile(r"^#{2,3}\s+\[?v?(\d+(?:\.\d+)+(?:[-+][0-9A-Za-z.-]+)?)\]?")
UNRELEASED_HEADING = re.compile(r"^#{2,3}\s+\[?(unreleased|upcoming)\]?\b", re.I)
INLINE_LINK = re.compile(
    r"!?\[(?:[^\[\]\n]|\[[^\[\]\n]*\])*\]\(\s*(<[^>\n]*>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"\n]*\"|'[^'\n]*'|\([^)\n]*\)))?\s*\)")
REF_DEFINITION = re.compile(r"^ {0,3}\[[^\]\n]+\]:\s*(<[^>\n]*>|\S+)", re.M)
HTML_HREF = re.compile(r"<a\s[^>]*?href=\"([^\"]+)\"", re.I)
MALFORMED_LINK = re.compile(r"\[[^\]\n]+\]\s+\([^)\s]+\.md[^)\s]*\)|\)\((?![a-z]+:)[^)\s]+\.md[^)\s]*\)", re.I)
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


# ---------------------------------------------------------------- repository facts
class Repo:
    """Read-only view of a documentation root, with optional Git evidence."""

    def __init__(self, root: Path, ref: str = "HEAD"):
        self.root = root.resolve()
        self.ref = ref
        self.git = self._git("rev-parse", "--is-inside-work-tree").stdout.strip() == "true"
        self.shallow = self.git and self._git("rev-parse", "--is-shallow-repository").stdout.strip() == "true"
        self.ref_ok = self.git and self._git("rev-parse", "--verify", "--quiet", ref + "^{commit}").returncode == 0
        self.identity = self._identity() if self.git else None
        self.files = self._files()
        self.config, self.config_errors = self._config()

    def _git(self, *args: str) -> subprocess.CompletedProcess:
        try:
            return subprocess.run(["git", "-C", str(self.root), *args], capture_output=True, text=True,
                                  encoding="utf-8", errors="replace", check=False)
        except OSError:
            return subprocess.CompletedProcess(args, 127, "", "git unavailable")

    def _identity(self):
        url = self._git("remote", "get-url", "origin").stdout.strip()
        match = re.search(r"github\.com[:/]([\w.-]+)/([\w.-]+?)(?:\.git)?/?$", url, re.I)
        return (match[1].casefold(), match[2].casefold()) if match else None

    def _files(self) -> list[str]:
        if self.git:
            out = self._git("ls-files", "-z", "--cached", "--others", "--exclude-standard").stdout
            return sorted({path for path in out.split("\0") if path})
        found = []
        for current, dirs, names in os.walk(self.root):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for name in names:
                found.append((Path(current) / name).relative_to(self.root).as_posix())
        return sorted(found)

    def _config(self):
        path = self.root / ".docstd.json"
        if not path.is_file():
            return {}, []
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return {}, [f".docstd.json is not valid JSON: {exc}"]
        errors = []
        if not isinstance(data, dict) or data.get("schema") != 1:
            return {}, [".docstd.json must be an object with \"schema\": 1"]
        unknown = set(data) - {"schema", "locations", "living", "historical"}
        if unknown:
            errors.append(f".docstd.json has unknown keys: {', '.join(sorted(unknown))}")
        locations = data.get("locations", {})
        for name, entry in list(locations.items()) if isinstance(locations, dict) else []:
            if name not in CORE_NAMES or not isinstance(entry, dict) or not entry.get("path") or not entry.get("reason"):
                errors.append(f".docstd.json location for {name!r} needs a core name, \"path\" and \"reason\"")
                locations.pop(name)
        return {"locations": locations if isinstance(locations, dict) else {},
                "living": [p for p in data.get("living", []) if isinstance(p, str)],
                "historical": [p for p in data.get("historical", []) if isinstance(p, str)]}, errors

    # Exact-case path resolution, independent of the host file system's case rules.
    def resolve(self, rel: str) -> tuple[str, str]:
        """Return ("ok"|"case"|"missing"|"outside", actual relative path or '')."""
        current, actual = self.root, []
        for part in PurePosixPath(rel).parts:
            if part in ("", "."):
                continue
            if part == "..":
                if not actual:
                    return "outside", ""
                actual.pop()
                current = current.parent
                continue
            try:
                entries = os.listdir(current)
            except OSError:
                return "missing", ""
            if part in entries:
                actual.append(part)
                current = current / part
                continue
            folded = [e for e in entries if e.casefold() == part.casefold()]
            if folded:
                return "case", "/".join(actual + [folded[0]])
            return "missing", ""
        return "ok", "/".join(actual)

    def read(self, rel: str) -> str:
        try:
            return (self.root / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return ""

    def is_historical(self, rel: str) -> bool:
        return any(fnmatch.fnmatchcase(rel, pattern) for pattern in self.config.get("historical", []))

    def core_location(self, name: str) -> tuple[str, bool]:
        """Path that holds a core responsibility, and whether it is a declared exception."""
        entry = self.config.get("locations", {}).get(name)
        return (entry["path"], True) if entry else (name, False)

    def commit(self, sha: str) -> bool:
        return self._git("cat-file", "-e", sha + "^{commit}").returncode == 0

    def ancestor(self, older: str, newer: str):
        code = self._git("merge-base", "--is-ancestor", older, newer).returncode
        return True if code == 0 else False if code == 1 else None

    def later_merges(self, sha: str) -> list[str]:
        out = self._git("log", "--first-parent", "--merges", "--format=%h %s", f"{sha}..{self.ref}").stdout
        return [line for line in out.splitlines() if line]

    def tags(self) -> list[str]:
        return [t for t in self._git("tag", "-l").stdout.splitlines() if t]

    def pr_commit(self, number: str):
        out = self._git("log", "--first-parent", "--format=%H%x00%s", self.ref).stdout
        pattern = re.compile(rf"(?:Merge pull request #{number}\b|Merge PR #{number}\b|\(#{number}\)\s*$)")
        for line in out.splitlines():
            sha, _, subject = line.partition("\0")
            if pattern.search(subject):
                return sha
        return None


# ---------------------------------------------------------------- Markdown helpers
def without_fences(text: str) -> list[str]:
    """Lines of text with fenced code blocks and HTML comments blanked (keeps numbering)."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            lines.append("")
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            continue
        if marker:
            fence = marker[1]
            lines.append("")
            continue
        lines.append(re.sub(r"<!--.*?-->", "", line))
    return lines


def without_code(line: str) -> str:
    return re.sub(r"(`+)(.+?)\1", lambda m: " " * len(m[0]), line)


def github_slug(heading: str) -> str:
    text = re.sub(r"<[^>]+>", "", heading)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "").strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(text: str) -> set[str]:
    found, counts = set(), {}
    lines = without_fences(text)
    if lines and lines[0].strip() == "---":
        try:
            end = lines.index("---", 1)
            lines = [""] * (end + 1) + lines[end + 1:]
        except ValueError:
            pass
    for index, line in enumerate(lines):
        atx = re.match(r"^ {0,3}#{1,6}\s+(.*?)\s*#*\s*$", line)
        heading = atx[1] if atx else None
        if heading is None and line.strip() and index + 1 < len(lines) and \
                re.match(r"^ {0,3}(=+|-+)\s*$", lines[index + 1]) and not re.match(r"^\s*([-*+]|\d+\.)\s", line):
            heading = line.strip()
        if heading is not None:
            slug = github_slug(heading)
            if slug in counts:
                counts[slug] += 1
                slug = f"{slug}-{counts[slug]}"
            else:
                counts[slug] = 0
            found.add(slug)
    found.update(re.findall(r"<[a-z][^>]*?\s(?:id|name)=\"([^\"]+)\"", text, re.I))
    return found


def link_targets(text: str):
    """Yield (line number, raw target) for inline, reference-style and HTML links."""
    for number, line in enumerate(without_fences(text), 1):
        clean = without_code(line)
        for pattern in (INLINE_LINK, HTML_HREF):
            for match in pattern.finditer(clean):
                yield number, match[1]
        definition = REF_DEFINITION.match(clean)
        if definition:
            yield number, definition[1]


# ---------------------------------------------------------------- findings
class Report:
    def __init__(self):
        self.items: list[dict] = []

    def add(self, level: str, check: str, message: str, path: str = "", line: int = 0):
        self.items.append({"level": level, "check": check, "path": path, "line": line, "message": message})

    def count(self, level: str) -> int:
        return sum(item["level"] == level for item in self.items)

    def overall(self) -> str:
        if self.count("FAIL"):
            return "FAIL"
        if self.count("UNVERIFIED"):
            return "INDETERMINATE"
        return "REVIEW" if self.count("REVIEW") else "PASS"


def check_core(repo: Repo, report: Report):
    for name, responsibility in CORE:
        path, declared = repo.core_location(name)
        status, actual = repo.resolve(path)
        if declared and status == "ok":
            report.add("REVIEW", "core", f"{name} responsibility is held at {path} by a declared exception: "
                       f"{repo.config['locations'][name]['reason']}", path)
            root_status, _ = repo.resolve(name)
            if root_status == "ok":
                report.add("FAIL", "authority", f"Both {name} and declared location {path} exist: two documents "
                           f"claim the same responsibility.", name)
        elif status == "ok":
            report.add("PASS", "core", f"{name} exists with exact casing ({responsibility}).", name)
        elif status == "case":
            report.add("FAIL", "case", f"Expected exact path {path}, found {actual}. Filename casing is normative.", actual)
        else:
            equivalents = [f for f in repo.files if PurePosixPath(f).name.casefold() in
                           ALIASES.get(name, set()) | {name.casefold()} and f != path]
            where = f"; candidate equivalent: {', '.join(equivalents)} (migration review)" if equivalents else ""
            report.add("FAIL", "core", f"Missing core document {path}{where}.", path)


def check_collisions(repo: Repo, report: Report):
    groups: dict[str, list[str]] = {}
    for path in repo.files:
        groups.setdefault(path.casefold(), []).append(path)
    collisions = [paths for paths in groups.values() if len(paths) > 1]
    for paths in collisions:
        report.add("FAIL", "case-collision", "Paths differ only by case: " + ", ".join(paths), paths[0])
    if not collisions:
        report.add("PASS", "case-collision", f"No case-fold collisions among {len(repo.files)} files.")


def check_links(repo: Repo, report: Report):
    markdown = [f for f in repo.files if f.casefold().endswith((".md", ".markdown"))]
    anchor_cache: dict[str, set[str]] = {}
    checked = 0
    for source in markdown:
        text = repo.read(source)
        for number, line in enumerate(without_fences(text), 1):
            if MALFORMED_LINK.search(without_code(line)):
                report.add("REVIEW", "links", "Possible malformed Markdown link (renders as literal text).", source, number)
        for number, raw in link_targets(text):
            target = raw[1:-1] if raw.startswith("<") and raw.endswith(">") else raw
            if not target or target.startswith("//") or SCHEME.match(target):
                continue
            path_part, _, fragment = target.partition("#")
            path_part = unquote(path_part.split("?", 1)[0])
            if path_part:
                base = PurePosixPath("") if path_part.startswith("/") else PurePosixPath(source).parent
                joined = (base / path_part.lstrip("/")).as_posix()
                status, actual = repo.resolve(joined)
                checked += 1
                if status == "outside":
                    report.add("REVIEW", "links", f"Link leaves the repository: {target}", source, number)
                    continue
                if status == "case":
                    report.add("FAIL", "links", f"Case mismatch: {target} resolves only case-insensitively "
                               f"(actual {actual}).", source, number)
                    continue
                if status == "missing":
                    report.add("FAIL", "links", f"Broken relative link: {target}", source, number)
                    continue
                destination = actual
            else:
                destination = source
            if not fragment or not destination.casefold().endswith((".md", ".markdown")):
                continue
            if (repo.root / destination).is_dir():
                continue
            if destination not in anchor_cache:
                anchor_cache[destination] = anchors(repo.read(destination))
            wanted = unquote(fragment)
            available = anchor_cache[destination]
            if wanted in available:
                continue
            if wanted.casefold() in {a.casefold() for a in available}:
                report.add("REVIEW", "links", f"Fragment #{wanted} matches a heading only by case in {destination}.",
                           source, number)
            else:
                report.add("FAIL", "links", f"Broken fragment #{wanted} in {destination}.", source, number)
    if not any(i["check"] == "links" and i["level"] == "FAIL" for i in report.items):
        report.add("PASS", "links", f"{checked} relative links across {len(markdown)} Markdown files resolve "
                   "with exact casing (fragments use a GitHub-style approximation).")


def check_duplicates(repo: Repo, report: Report):
    for name in CORE_NAMES:
        aliases = ALIASES.get(name)
        if not aliases:
            continue
        holders = [f for f in repo.files if PurePosixPath(f).name.casefold() in aliases and not repo.is_historical(f)]
        if len(holders) > 1:
            report.add("REVIEW", "authority", f"Several documents may hold the {name} responsibility: "
                       f"{', '.join(holders)}. Keep one authority; mark others historical in .docstd.json.", holders[0])


def living_documents(repo: Repo) -> list[str]:
    docs = [repo.core_location(name)[0] for name in CURRENT_STATE_DOCS]
    return [d for d in dict.fromkeys(docs + repo.config.get("living", [])) if repo.resolve(d)[0] == "ok"]


def check_git_claims(repo: Repo, report: Report):
    if not repo.git:
        report.add("UNVERIFIED", "git", "Not a Git work tree: commit, baseline and release claims were not checked.")
        return
    if not repo.ref_ok:
        report.add("UNVERIFIED", "git", f"Reference {repo.ref!r} is not available locally: claims were not checked.")
        return
    stale = 0
    for doc in living_documents(repo):
        for number, line in enumerate(without_fences(repo.read(doc)), 1):
            refs = [m[1] for m in BRANCH_SHA.finditer(line)]
            refs += [m[3] for m in URL_SHA.finditer(line) if repo.identity and
                     (m[1].casefold(), re.sub(r"\.git$", "", m[2].casefold())) == repo.identity]
            current = CURRENT_CLAIM.search(line)
            for sha in dict.fromkeys(refs):
                if not repo.commit(sha):
                    level = "UNVERIFIED" if repo.shallow else "REVIEW"
                    report.add(level, "baseline", f"Commit {sha} is not in local history"
                               f"{' (shallow clone)' if repo.shallow else '; it may belong to another repository'}.",
                               doc, number)
                    continue
                if not current:
                    continue
                ancestry = repo.ancestor(sha, repo.ref)
                if ancestry is False:
                    report.add("REVIEW", "baseline", f"Current-state claim cites {sha}, which is not an ancestor of "
                               f"{repo.ref}.", doc, number)
                    continue
                merges = repo.later_merges(sha)
                if merges:
                    stale += 1
                    report.add("REVIEW", "baseline", f"Current-state claim cites {sha}, but {len(merges)} later "
                               f"merge(s) exist on {repo.ref}; latest: {merges[0]}. Confirm or update the claim.",
                               doc, number)
            if current and not refs:
                numbers = [m[1] for m in PR_REF.finditer(line)]
                merged = [(n, repo.pr_commit(n)) for n in numbers]
                merged = [(n, c) for n, c in merged if c]
                if merged:
                    newest = max(merged, key=lambda item: int(item[0]))
                    later = repo.later_merges(newest[1])
                    if later:
                        stale += 1
                        report.add("REVIEW", "baseline", f"Current-state claim cites PR #{newest[0]}, but "
                                   f"{len(later)} later merge(s) exist; latest: {later[0]}.", doc, number)
            if VERIFICATION_CLAIM.search(line) and not EVIDENCE_MARK.search(line):
                report.add("REVIEW", "verification", "Verification claim without a revision, run or date: confirm it "
                           "is current evidence, not a historical result.", doc, number)
    if not stale:
        report.add("PASS", "baseline", f"No stale current-state baseline claims detected against {repo.ref}.")


def sections(lines: list[str], pattern) -> list[tuple[str, int, list[tuple[int, str]]]]:
    found = []
    for number, line in enumerate(lines, 1):
        match = pattern.match(line)
        if match:
            found.append((match[1], number, []))
        elif found and re.match(r"^#{1,3}\s", line):
            found.append((None, number, []))
        elif found:
            found[-1][2].append((number, line))
    return [s for s in found if s[0]]


def check_changelog(repo: Repo, report: Report):
    path, _ = repo.core_location("Changelog.md")
    if repo.resolve(path)[0] != "ok":
        return
    lines = without_fences(repo.read(path))
    versions = sections(lines, VERSION_HEADING)
    for number, line in enumerate(lines, 1):
        if UNRELEASED_HEADING.match(line):
            report.add("REVIEW", "changelog", "Unreleased section: each item must be a user-visible change relative "
                       "to the last public release, not development churn.", path, number)
    tags = repo.tags() if repo.git else []
    if not versions:
        text = "\n".join(lines).casefold()
        if not re.search(r"no public release|not (yet )?been released|no releases? (yet|have been)", text):
            report.add("REVIEW", "changelog", "No release entries: state explicitly that no public release exists.", path)
        if not repo.git:
            report.add("UNVERIFIED", "changelog", "No Git evidence: absence of public releases is not confirmed.", path)
        elif tags:
            report.add("REVIEW", "changelog", f"Tags exist ({', '.join(tags[:5])}) but no release is listed. "
                       "Confirm whether any tag is a public release.", path)
        elif repo.shallow:
            report.add("UNVERIFIED", "changelog", "Shallow clone: absence of release tags is not confirmed.", path)
        else:
            report.add("PASS", "changelog", "No release entries and no release tags: consistent.", path)
        return
    for version, number, body in versions:
        tag = next((t for t in tags if t in (version, "v" + version)), None)
        if not tag:
            level = "UNVERIFIED" if (not repo.git or repo.shallow) else "REVIEW"
            report.add(level, "changelog", f"Version {version} has no matching tag; a merged PR is not evidence of "
                       "a public release.", path, number)
            continue
        problems = 0
        for line_number, text in body:
            cited = [(f"commit {m[1]}", m[1]) for m in BRANCH_SHA.finditer(text)]
            cited += [(f"commit {m}", m) for m in re.findall(r"`(" + SHA + r")`", text)]
            cited += [(f"PR #{n}", repo.pr_commit(n)) for n in (m[1] for m in PR_REF.finditer(text))]
            for label, sha in cited:
                if not sha or not repo.commit(sha):
                    continue
                if repo.ancestor(sha, tag) is False:
                    problems += 1
                    report.add("FAIL", "changelog", f"Entry under {version} cites {label}, which is not contained "
                               f"in release tag {tag}: merged-but-unreleased work.", path, line_number)
        if not problems:
            report.add("PASS", "changelog", f"Version {version} matches tag {tag}; cited work is contained in it.",
                       path, number)


def check_devlog(repo: Repo, report: Report):
    path, _ = repo.core_location("devlog.md")
    if repo.resolve(path)[0] != "ok":
        return
    lines = without_fences(repo.read(path))
    entries = [(m[1], n) for n, line in enumerate(lines, 1) for m in [re.match(r"^##\s+(\d{4}-\d{2}-\d{2})\b", line)] if m]
    dates = [d for d, _ in entries]
    if dates and dates != sorted(dates) and dates != sorted(dates, reverse=True):
        report.add("FAIL", "devlog", "Entries are not in one chronological order.", path, entries[0][1])
    for index, (date, number) in enumerate(entries):
        end = entries[index + 1][1] if index + 1 < len(entries) else len(lines) + 1
        body = "\n".join(lines[number:end - 1])
        if not re.search(SHA + r"|#\d+|\]\(", body):
            report.add("REVIEW", "devlog", f"Entry {date} has no commit, PR or evidence reference.", path, number)
    if entries and not any(i["check"] == "devlog" and i["level"] == "FAIL" for i in report.items):
        report.add("PASS", "devlog", f"{len(entries)} dated entries in chronological order.", path)


def check_readme(repo: Repo, report: Report):
    status, _ = repo.resolve("README.md")
    if status != "ok":
        return
    lines = without_fences(repo.read("README.md"))
    dated = [n for n, line in enumerate(lines, 1) if DATE.search(line)]
    if len(dated) > 5:
        report.add("REVIEW", "readme", f"{len(dated)} dated lines: README may carry chronology that belongs in "
                   "devlog.md or Changelog.md.", "README.md", dated[0])
    for number, line in enumerate(lines, 1):
        if re.match(r"^#{1,6}\s.*\b(change ?log|history|dev ?log|work ?log|release notes)\b", line, re.I):
            report.add("REVIEW", "readme", "History-type heading in README: link to the owning document instead.",
                       "README.md", number)


def check_templates(repo: Repo, report: Report):
    for name in CORE_NAMES:
        path, _ = repo.core_location(name)
        if repo.resolve(path)[0] == "ok" and TEMPLATE_MARKER in repo.read(path):
            report.add("REVIEW", "template", "Bootstrap template text is not yet reviewed (remove the docstd:template "
                       "marker after review).", path)


def run_check(root: Path, ref: str = "HEAD") -> Report:
    repo, report = Repo(root, ref), Report()
    for error in repo.config_errors:
        report.add("FAIL", "config", error, ".docstd.json")
    for name, entry in repo.config.get("locations", {}).items():
        if repo.resolve(entry["path"])[0] != "ok":
            report.add("FAIL", "config", f"Declared location for {name} does not exist: {entry['path']}", ".docstd.json")
    for step in (check_core, check_collisions, check_links, check_duplicates, check_git_claims,
                 check_changelog, check_devlog, check_readme, check_templates):
        step(repo, report)
    return report


# ---------------------------------------------------------------- bootstrap
def plan_init(root: Path) -> list[dict]:
    repo = Repo(root)
    plan = []
    for name, responsibility in CORE:
        path, declared = repo.core_location(name)
        status, actual = repo.resolve(path)
        if status == "ok":
            reason = "declared exception location" if declared else "exists; never overwritten"
            plan.append({"action": "keep", "path": path, "reason": reason})
            continue
        if status == "case":
            plan.append({"action": "review", "path": path, "reason": f"case variant {actual} exists; creating {path} "
                         "would collide on case-insensitive file systems"})
            continue
        equivalents = [f for f in repo.files if PurePosixPath(f).name.casefold() in ALIASES.get(name, set())
                       and not repo.is_historical(f)]
        if equivalents:
            plan.append({"action": "review", "path": path, "reason": "equivalent exists at "
                         + ", ".join(equivalents) + "; plan a migration or declare it in .docstd.json"})
            continue
        if not (TEMPLATES / name).is_file():
            plan.append({"action": "review", "path": path, "reason": "template missing from the skill"})
            continue
        plan.append({"action": "create", "path": path, "reason": responsibility})
    return plan


def apply_init(root: Path, plan: list[dict]) -> list[dict]:
    for item in plan:
        if item["action"] != "create":
            continue
        target = root / item["path"]
        try:
            with open(target, "x", encoding="utf-8", newline="\n") as handle:
                handle.write((TEMPLATES / item["path"]).read_text(encoding="utf-8"))
            item["action"] = "created"
        except FileExistsError:
            item["action"] = "keep"
            item["reason"] = "appeared during apply; not overwritten"
    return plan


# ---------------------------------------------------------------- command line
def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="plan or create the seven core documents")
    init.add_argument("root", nargs="?", default=".", type=Path)
    init.add_argument("--apply", action="store_true", help="create missing documents (never overwrites)")
    init.add_argument("--json", action="store_true")
    check = sub.add_parser("check", help="validate documentation structure and claims")
    check.add_argument("root", nargs="?", default=".", type=Path)
    check.add_argument("--ref", default="HEAD", help="Git revision for baseline and release checks")
    check.add_argument("--json", action="store_true")
    check.add_argument("--strict", action="store_true", help="treat REVIEW as failure")
    args = parser.parse_args(argv)
    if not args.root.is_dir():
        print(f"ERROR: not a directory: {args.root}", file=sys.stderr)
        return 1

    if args.command == "init":
        plan = plan_init(args.root)
        if args.apply:
            plan = apply_init(args.root, plan)
        if args.json:
            print(json.dumps({"applied": args.apply, "plan": plan}, indent=2))
        else:
            print(f"docstd init ({'apply' if args.apply else 'dry run: nothing written'}) — {args.root.resolve()}")
            for item in plan:
                print(f"  {item['action'].upper():8} {item['path']}: {item['reason']}")
        return 1 if any(item["action"] == "review" for item in plan) else 0

    report = run_check(args.root, args.ref)
    if args.json:
        print(json.dumps({"overall": report.overall(), "findings": report.items}, indent=2))
    else:
        print(f"docstd check — {args.root.resolve()} (ref {args.ref})")
        for level in LEVELS:
            for item in (i for i in report.items if i["level"] == level):
                where = f"{item['path']}:{item['line']}" if item["line"] else item["path"]
                print(f"  {level:10} [{item['check']}] {where + ': ' if where else ''}{item['message']}")
        counts = ", ".join(f"{report.count(level)} {level}" for level in LEVELS)
        print(f"Overall: {report.overall()} ({counts})")
        print("Structural and heuristic checks only; they do not prove that the documentation is accurate.")
    if report.count("FAIL") or (args.strict and report.count("REVIEW")):
        return 1
    return 2 if report.count("UNVERIFIED") else 0


if __name__ == "__main__":
    sys.exit(main())

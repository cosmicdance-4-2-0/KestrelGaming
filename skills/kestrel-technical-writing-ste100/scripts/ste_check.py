#!/usr/bin/env python3
"""STE-informed writing aids (Python 3.9+, standard library only).

  protect OLD NEW     Compare the protected technical tokens in two versions of a text.
                      Exit 1 if an identifier, command, path, number or unit changed.
  lint FILE|-         Report review hints: sentence length, paragraph length, -ing forms,
                      likely passive voice, and project terms marked "avoid" in
                      --terms docs/TERMINOLOGY.md.

These are review aids. They do not use the ASD-STE100 dictionary, and their output is
not proof of ASD-STE100 compliance. A person decides each finding.
"""
from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re
import sys

UNITS = (r"%|°C|°F|°|µs|us|ns|ms|s|min|h|Hz|kHz|MHz|GHz|dB|B|KB|KiB|MB|MiB|GB|GiB|TB|px|em|rem|vh|vw|"
         r"fps|FPS|V|mV|A|mA|W|kW|m|cm|mm|km|kg|g|bit|bits|bytes")
PROTECTED = re.compile(
    r"(`+)(?P<code>.+?)\1"                                  # inline code
    r"|(?P<url>[a-z][a-z0-9+.-]*://[^\s)>\]]+)"             # URLs
    r"|(?P<flag>(?<![\w-])--?[A-Za-z][\w-]*)"               # command-line flags
    r"|(?P<call>\b[A-Za-z_][\w$]*(?:\.[A-Za-z_][\w$]*)+(?:\(\))?)"   # dotted names and calls
    r"|(?P<camel>\b[a-z]+[A-Z][A-Za-z0-9]*\b|\b[A-Z][a-z0-9]+[A-Z][A-Za-z0-9]*\b)"  # camelCase / PascalCase
    r"|(?P<snake>\b[A-Za-z0-9]+(?:_[A-Za-z0-9]+)+\b)"       # snake_case and CONSTANTS
    r"|(?P<path>(?<![\w/])(?:\.{1,2}/|/)?[\w.-]+/[\w./-]+)"  # file paths
    r"|(?P<num>(?<![\w.])[-+]?\d+(?:[.,]\d+)*(?:\s?(?:" + UNITS + r"))?(?!\w))")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
PROCEDURAL = re.compile(r"^\s*(?:\d+[.)]|[-*+])\s+")
ING = re.compile(r"\b[a-z]{3,}ing\b")
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?\w+(?:ed|en)\b", re.I)


def tokens(text: str) -> Counter:
    """Multiset of protected tokens. Fenced code blocks count as single tokens."""
    found, block, fence = Counter(), [], None
    for line in text.splitlines():
        marker = FENCE.match(line)
        if fence:
            if marker and marker[1][0] == fence[0]:
                found["```" + "\n".join(block)] += 1
                block, fence = [], None
            else:
                block.append(line)
            continue
        if marker:
            fence = marker[1]
            continue
        for match in PROTECTED.finditer(line):
            value = match["code"] or match[0]
            found[re.sub(r"\s+", " ", value.strip())] += 1
    if fence:
        found["```" + "\n".join(block)] += 1
    return found


def protected_diff(old: str, new: str) -> list[str]:
    before, after = tokens(old), tokens(new)
    problems = [f"removed or changed: {t!r}" for t in sorted(before - after)]
    problems += [f"added: {t!r}" for t in sorted(after - before)]
    return problems


def sentences(paragraph: str) -> list[str]:
    text = re.sub(r"(`+).+?\1", "CODE", paragraph)
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9`\"'(])", text) if s.strip()]


def load_terms(path: Path | None) -> dict[str, str]:
    """Read 'avoid' terms from a Markdown table with columns: Term | Meaning | Avoid."""
    if not path:
        return {}
    terms = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0] and not set(cells[0]) <= set("-: ") and cells[0].lower() != "term":
            for avoided in filter(None, (a.strip(" `") for a in cells[2].split(","))):
                terms[avoided.lower()] = cells[0].strip("`")
    return terms


def lint(text: str, avoid: dict[str, str] | None = None) -> list[dict]:
    avoid = avoid or {}
    findings, paragraph, start, fence = [], [], 1, None

    def flush():
        if not paragraph:
            return
        joined = " ".join(paragraph)
        procedural = bool(PROCEDURAL.match(paragraph[0]))
        limit = 20 if procedural else 25
        parts = sentences(PROCEDURAL.sub("", joined))
        for sentence in parts:
            words = len(re.findall(r"[\w'-]+", sentence))
            if words > limit:
                kind = "procedural" if procedural else "descriptive"
                findings.append({"line": start, "message": f"{kind} sentence has {words} words "
                                 f"(STE-informed limit {limit}); consider splitting"})
        if not procedural and len(parts) > 6:
            findings.append({"line": start, "message": f"paragraph has {len(parts)} sentences; consider one topic "
                             "per paragraph"})
        plain = re.sub(r"(`+).+?\1", " ", joined)
        for word in sorted(set(ING.findall(plain.lower()))):
            findings.append({"line": start, "message": f"-ing form {word!r}: check that it is a technical name or "
                             "rewrite"})
        if PASSIVE.search(plain):
            findings.append({"line": start, "message": "possible passive voice: prefer the active voice"})
        for term, preferred in avoid.items():
            if re.search(rf"\b{re.escape(term)}\w*\b", plain, re.I):
                findings.append({"line": start, "message": f"project terminology: use {preferred!r}, not {term!r}"})

    for number, line in enumerate(text.splitlines(), 1):
        marker = FENCE.match(line)
        if fence or marker:
            if marker:
                fence = None if fence else marker[1]
            flush()
            paragraph = []
            continue
        if not line.strip() or line.lstrip().startswith(("#", "|", ">")) or PROCEDURAL.match(line):
            flush()
            paragraph, start = ([line], number) if PROCEDURAL.match(line) else ([], number + 1)
            continue
        if not paragraph:
            start = number
        paragraph.append(line.strip())
    flush()
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    protect = sub.add_parser("protect", help="compare protected technical tokens")
    protect.add_argument("old", type=Path)
    protect.add_argument("new", type=Path)
    check = sub.add_parser("lint", help="report STE-informed review hints")
    check.add_argument("file")
    check.add_argument("--terms", type=Path, help="project terminology table (Term | Meaning | Avoid)")
    args = parser.parse_args(argv)

    if args.command == "protect":
        problems = protected_diff(args.old.read_text(encoding="utf-8"), args.new.read_text(encoding="utf-8"))
        for problem in problems:
            print("CHANGED", problem)
        print("Protected tokens unchanged." if not problems else
              f"{len(problems)} protected token change(s): review before you accept the edit.")
        return 1 if problems else 0

    text = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8")
    findings = lint(text, load_terms(args.terms))
    for item in findings:
        print(f"REVIEW line {item['line']}: {item['message']}")
    print(f"{len(findings)} review hint(s). These hints are not proof of ASD-STE100 compliance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

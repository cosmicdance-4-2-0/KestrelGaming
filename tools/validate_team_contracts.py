#!/usr/bin/env python3
"""Read-only structural checks for proposed Kestrel team contracts (schema 0.1).

Standard library only, Python 3.9+. This checks neither remote branch existence,
host identity, agent independence, nor whether team behavior improves results.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
HEADINGS = (
    "Mission and scope",
    "Composition — different instincts, not averaged identities",
    "Working method",
    "Execution mode",
    "Authority, verification, and continuity",
    "Evaluation",
)
# Schema 0.1 is intentionally closed. Extension requires versioned revision.
FIELDS = {
    "": ("schema", "metadata", "purpose", "composition", "operating_method", "execution", "authority", "continuity", "evaluation"),
    "schema": ("name", "version", "status", "type"),
    "metadata": ("team_id", "display_name", "tagline", "created_on", "origin", "contract_path", "source_repository", "runtime_identity_id"),
    "purpose": ("mission", "selection_triggers", "exclusions", "deliverables"),
    "composition": ("semantics", "lead_agent_id", "counterweight_agent_id", "members"),
    "composition.members[]": ("agent_id", "home_branch", "role", "first_question", "challenge"),
    "operating_method": ("phases", "decision_criteria", "deadlock_rule", "composition_shadow", "correction"),
    "execution": ("composite", "federated", "default_mode"),
    "execution.composite": ("supported_by_design", "semantics", "disclosure"),
    "execution.federated": ("requires_external_host", "semantics", "disclosure"),
    "authority": ("precedence", "permissions_granted", "can_delegate_or_vote", "boundaries"),
    "continuity": ("member_profiles", "shared_contract", "project_decisions", "agent_memory", "team_memory_scope", "privacy"),
    "evaluation": ("comparator", "task", "predicted_distinction", "evidence", "falsifier", "behavioral_certified"),
}
LIST_STRINGS = {
    "purpose.selection_triggers", "purpose.exclusions", "purpose.deliverables",
    "operating_method.phases", "operating_method.decision_criteria",
    "authority.boundaries", "evaluation.evidence",
}
NULL_FIELDS = {"metadata.runtime_identity_id", "continuity.team_memory_scope"}
TRUE_FIELDS = {"execution.composite.supported_by_design", "execution.federated.requires_external_host"}
FALSE_FIELDS = {"authority.can_delegate_or_vote", "evaluation.behavioral_certified"}
LIST_EMPTY_FIELDS = {"authority.permissions_granted"}


def _check_shape(value: object, where: str, errors: list[str]) -> None:
    """Check closed object structure, field types and non-placeholder prose."""
    if where in FIELDS:
        if not isinstance(value, dict):
            errors.append(f"{where or 'profile'}: expected object")
            return
        want = set(FIELDS[where])
        got = set(value)
        if missing := sorted(want - got):
            errors.append(f"{where or 'profile'}: missing fields {missing}")
        if extra := sorted(got - want):
            errors.append(f"{where or 'profile'}: unknown fields {extra}")
        for field in want & got:
            subpath = (where + "." if where else "") + field
            _check_shape(value[field], subpath, errors)
        return
    if where == "composition.members":
        if not isinstance(value, list) or len(value) < 2:
            errors.append(f"{where}: expected at least two members")
            return
        for i, member in enumerate(value):
            _check_shape(member, "composition.members[]", errors)
        return
    if where in LIST_STRINGS:
        if (not isinstance(value, list) or not value or
                any(not isinstance(v, str) or not v.strip() or "REPLACE_" in v for v in value)):
            errors.append(f"{where}: expected nonempty list of completed strings")
        return
    if where in LIST_EMPTY_FIELDS:
        if value != []:
            errors.append(f"{where}: permissions must remain empty")
        return
    if where in NULL_FIELDS:
        if value is not None:
            errors.append(f"{where}: must be null")
        return
    if where in TRUE_FIELDS | FALSE_FIELDS:
        expected = where in TRUE_FIELDS
        if type(value) is not bool or value is not expected:
            errors.append(f"{where}: must be {str(expected).lower()}")
        return
    if not isinstance(value, str) or not value.strip() or "REPLACE_" in value:
        errors.append(f"{where}: expected completed nonempty text")


def _load_roster(root: Path, errors: list[str]) -> dict[str, str]:
    path = root / "agents/ROSTER_V1.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        members = data["members"]
        if not isinstance(members, list):
            raise ValueError("members must be an array")
        refs: dict[str, str] = {}
        for member in members:
            ident, branch = member["id"], member["branch"]
            if not isinstance(ident, str) or not SLUG.fullmatch(ident) or ident in refs:
                raise ValueError("invalid/duplicate member ID")
            if branch != f"agents/{ident}-v1":
                raise ValueError(f"invalid branch for {ident}")
            refs[ident] = branch
        return refs
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"agents/ROSTER_V1.json: invalid roster ({exc})")
        return {}


def validate_team_contracts(root: Path) -> list[str]:
    """Validate populated team homes. Empty/uncreated teams are legitimate."""
    root = root.resolve()
    team_dir = root / "teams"
    if not team_dir.exists():
        return []
    if team_dir.is_symlink() or not team_dir.is_dir():
        return ["teams: expected a regular directory"]
    errors: list[str] = []
    roster = _load_roster(root, errors)
    for home in sorted(team_dir.iterdir()):
        relative = f"teams/{home.name}"
        if not home.is_dir() or home.is_symlink() or not SLUG.fullmatch(home.name):
            errors.append(f"{relative}: expected a non-symlinked lowercase team directory")
            continue
        files = {p.name for p in home.iterdir()}
        if files != {"TEAM.md", "PROFILE.json"} or any(p.is_symlink() for p in home.iterdir()):
            errors.append(f"{relative}: expected exactly TEAM.md and PROFILE.json, without symlinks")
            continue
        try:
            prose = (home / "TEAM.md").read_text(encoding="utf-8")
            data = json.loads((home / "PROFILE.json").read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{relative}: cannot read/parse files ({exc})")
            continue
        if not isinstance(data, dict):
            errors.append(f"{relative}/PROFILE.json: expected an object")
            continue
        local: list[str] = []
        _check_shape(data, "", local)
        if local:
            errors.extend(f"{relative}/PROFILE.json: {e}" for e in local)
            continue
        s, meta, comp = data["schema"], data["metadata"], data["composition"]
        for key, expected in (("name", "KestrelTeamContract"), ("version", "0.1"),
                              ("status", "DRAFT"), ("type", "composition-design-not-runtime")):
            if s[key] != expected:
                errors.append(f"{relative}: schema.{key} must be {expected}")
        if meta["team_id"] != home.name:
            errors.append(f"{relative}: metadata.team_id/path mismatch")
        if meta["contract_path"] != f"{relative}/TEAM.md":
            errors.append(f"{relative}: metadata.contract_path mismatch")
        if meta["source_repository"] != "cosmicdance-4-2-0/KestrelGaming":
            errors.append(f"{relative}: metadata.source_repository mismatch")
        try:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", meta["created_on"]):
                raise ValueError("not ISO date")
            date.fromisoformat(meta["created_on"])
        except ValueError:
            errors.append(f"{relative}: invalid metadata.created_on")
        lead, counter = comp["lead_agent_id"], comp["counterweight_agent_id"]
        if lead == counter:
            errors.append(f"{relative}: lead and counterweight must be distinct")
        ids = [m["agent_id"] for m in comp["members"]]
        if len(ids) != len(set(ids)):
            errors.append(f"{relative}: duplicate agent_id")
        for ident, role in ((lead, "lead"), (counter, "counterweight")):
            if sum(m["agent_id"] == ident and m["role"] == role for m in comp["members"]) != 1:
                errors.append(f"{relative}: designated {role} must match exactly one member")
        if sorted(m["role"] for m in comp["members"]).count("lead") != 1 or sorted(m["role"] for m in comp["members"]).count("counterweight") != 1:
            errors.append(f"{relative}: requires exactly one lead and one counterweight role")
        for m in comp["members"]:
            ident = m["agent_id"]
            if not SLUG.fullmatch(ident) or ident not in roster:
                errors.append(f"{relative}: unknown or invalid agent_id {ident}")
            elif m["home_branch"] != roster[ident]:
                errors.append(f"{relative}: {ident} home_branch/roster mismatch")
            if m["role"] not in {"lead", "counterweight", "contributor"}:
                errors.append(f"{relative}: invalid member role {m['role']}")
        if data["execution"]["default_mode"] != "composite":
            errors.append(f"{relative}: execution.default_mode must be composite")
        if data["continuity"]["shared_contract"] != "KESTREL.md":
            errors.append(f"{relative}: continuity.shared_contract must be KESTREL.md")
        for heading in HEADINGS:
            if not re.search(r"^## " + re.escape(heading) + r"\s*$", prose, re.M):
                errors.append(f"{relative}/TEAM.md: missing section {heading}")
        if "REPLACE_" in prose or len(prose.strip()) < 200:
            errors.append(f"{relative}/TEAM.md: incomplete prose contract")
        if f"**Team ID:** `{home.name}`" not in prose or f"**Display name:** {meta['display_name']}" not in prose:
            errors.append(f"{relative}/TEAM.md: identity/profile mismatch")
        for ident in set(ids):
            if f"agents/{ident}-v1" not in prose:
                errors.append(f"{relative}/TEAM.md: missing member branch {ident}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    errors = validate_team_contracts(parser.parse_args().root)
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("Team contract structural checks passed (no team means none to validate).")
    print("This does not certify behavior, remote refs, identity, or host permissions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

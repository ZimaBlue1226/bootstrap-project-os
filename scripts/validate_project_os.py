#!/usr/bin/env python3
"""Read-only structural validation. Semantic readiness requires a separate review."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from inspect_project import SKIP_DIRS, is_sensitive_name

CORE_FILES = {
    "collaboration_rules": "AGENTS.md",
    "stable_context": "project_context.md",
    "current_work": "current_work.md",
    "artifact_navigation": "artifact_index.md",
}
OPTIONAL_ROLES = {"durable_decisions", "effective_history"}
ROLE_MAP_PATTERN = re.compile(r"<!--\s*project-os:role-map=(.*?)-->", re.DOTALL)
GROUNDING_PATTERN = re.compile(r"<!--\s*project-os:grounding-status=(.*?)-->", re.DOTALL)
PLACEHOLDER_PATTERNS = (
    re.compile(r"\{\{[^}\n]+\}\}"),
    re.compile(r"\[TODO:[^\]\n]+\]", re.IGNORECASE),
)


def issue(severity: str, code: str, message: str, path: str | None = None) -> dict[str, str]:
    result = {"severity": severity, "code": code, "message": message}
    if path:
        result["path"] = path
    return result


def safe_local_source(root: Path, value: str) -> Path:
    """Reject unsafe owners before reading any of their content."""
    if "\\" in value or ":" in value or "#" in value or "?" in value:
        raise ValueError("Use a project-relative POSIX file path without fragments.")
    relative = Path(value)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ValueError("Role source must stay within the project root.")
    protected = SKIP_DIRS | {"archive", "archives", ".ssh", ".skill-build"}
    current = root
    for part in relative.parts:
        if part.casefold() in protected or is_sensitive_name(part):
            raise ValueError("Role source enters a protected or non-current location.")
        current = current / part
        if current.is_symlink() or getattr(current, "is_junction", lambda: False)():
            raise ValueError("Role sources must not traverse links or junctions.")
        if current.is_dir() and (current / ".git").exists():
            raise ValueError("Register an independent repository externally; do not read through it.")
    if not current.resolve().is_relative_to(root):
        raise ValueError("Role source resolves outside the project root.")
    return current


def resolve_roles(agents: str) -> dict[str, str]:
    """Use four defaults plus explicit existing owners, without inventing sources."""
    matches = ROLE_MAP_PATTERN.findall(agents)
    if len(matches) > 1:
        raise ValueError("Declare at most one project-os:role-map comment.")
    if not matches:
        if "project-os:role-map=" in agents:
            raise ValueError("Malformed role-map comment.")
        return dict(CORE_FILES)

    def unique_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate role key: {key}")
            result[key] = value
        return result

    mapping = json.loads(matches[0], object_pairs_hook=unique_keys)
    if not isinstance(mapping, dict):
        raise ValueError("Role map must be a JSON object.")
    for role, source in mapping.items():
        if role not in CORE_FILES and role not in OPTIONAL_ROLES:
            raise ValueError(f"Unknown role: {role}")
        if not isinstance(source, str) or not source.strip() or source != source.strip():
            raise ValueError(f"Invalid source for {role}.")
        if role == "collaboration_rules" and source != "AGENTS.md":
            raise ValueError("AGENTS.md remains the local routing and safety entry.")
    return {**CORE_FILES, **mapping}


def is_external(source: str) -> bool:
    if not source.startswith(("https://", "http://")):
        return False
    parsed = urlsplit(source)
    if not parsed.hostname or parsed.username or parsed.password or any(c.isspace() for c in source):
        raise ValueError("External owners require an HTTP/HTTPS URL without embedded credentials.")
    return True


def validate(root: Path) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"Project root is not a directory: {root}")

    issues: list[dict[str, str]] = []
    cache: dict[Path, str | None] = {}

    def read_owner(source: str) -> str | None:
        try:
            path = safe_local_source(root, source)
        except ValueError as exc:
            issues.append(issue("error", "unsafe-role-source", str(exc), source))
            return None
        if path in cache:
            return cache[path]
        cache[path] = None
        if not path.is_file():
            issues.append(issue("error", "missing-core-role", "Declared owner is not a readable file.", source))
            return None
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            issues.append(issue("error", "unreadable-role-source", "Cannot read owner as UTF-8.", source))
            return None
        cache[path] = text
        if not text.strip():
            issues.append(issue("error", "empty-core-file", "Declared owner is empty.", source))
        elif any(pattern.search(text) for pattern in PLACEHOLDER_PATTERNS):
            issues.append(issue("error", "unresolved-placeholder", "Unresolved template placeholder.", source))
        return text

    agents = read_owner("AGENTS.md") or ""
    try:
        role_sources = resolve_roles(agents)
    except ValueError as exc:
        issues.append(issue("error", "invalid-role-map", str(exc), "AGENTS.md"))
        role_sources = dict(CORE_FILES)

    contents: dict[str, str] = {"collaboration_rules": agents}
    external_roles: list[str] = []
    for role, source in role_sources.items():
        if role == "collaboration_rules":
            continue
        try:
            external = is_external(source)
        except ValueError as exc:
            issues.append(issue("error", "unsafe-role-source", str(exc)))
            continue
        if external:
            external_roles.append(role)
            issues.append(issue("review", "external-role-unverified",
                                f"Verify access, scope and freshness of the external owner for {role}."))
        else:
            text = read_owner(source)
            if text is not None:
                contents[role] = text
        if agents and source not in agents:
            issues.append(issue("error", "unregistered-role-source",
                                f"AGENTS.md does not register the owner for {role}.", "AGENTS.md"))

    grounding_status = "undeclared"
    context = contents.get("stable_context", "")
    markers = GROUNDING_PATTERN.findall(context)
    if markers:
        if len(markers) != 1 or markers[0].strip() not in {"ready", "needs-input"}:
            issues.append(issue("error", "invalid-grounding-marker",
                                "Use at most one optional ready or needs-input declaration.",
                                role_sources["stable_context"]))
        else:
            grounding_status = markers[0].strip()
            if grounding_status == "needs-input":
                issues.append(issue("review", "declared-context-gap",
                                    "Review the material context gaps declared by the project.",
                                    role_sources["stable_context"]))
    elif "project-os:grounding-status=" in context:
        issues.append(issue("error", "invalid-grounding-marker", "Malformed grounding comment.",
                            role_sources["stable_context"]))

    errors = sum(item["severity"] == "error" for item in issues)
    return {
        "project_root": str(root),
        "status": "invalid" if errors else "valid",
        "structure_status": "fail" if errors else "pass",
        "semantic_status": "not_checked",
        "role_sources": role_sources,
        "external_roles": external_roles,
        "grounding_status": grounding_status,
        "errors": errors,
        "review_items": sum(item["severity"] == "review" for item in issues),
        "issues": issues,
        "note": "Structural checks only. Review current facts, source scope, access, and cold-start behavior separately.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Project root directory.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()
    try:
        report = validate(Path(args.root))
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Project OS structure: {report['status'].upper()}; semantic review: NOT CHECKED")
        print(f"Errors: {report['errors']}; review items: {report['review_items']}")
        for item in report["issues"]:
            location = f" [{item['path']}]" if "path" in item else ""
            print(f"- {item['severity'].upper()} {item['code']}{location}: {item['message']}")
        print(report["note"])
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

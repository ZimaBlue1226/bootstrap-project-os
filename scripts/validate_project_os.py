#!/usr/bin/env python3
"""Validate Project OS structure, grounding state, and authority boundaries."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


CORE_FILES = {
    "collaboration_rules": "AGENTS.md",
    "stable_context": "project_context.md",
    "current_work": "current_work.md",
    "durable_decisions": "decision_log.md",
    "artifact_navigation": "artifact_index.md",
    "effective_history": "changelog.md",
}

PLACEHOLDER_PATTERNS = (
    re.compile(r"\{\{[^}\n]+\}\}"),
    re.compile(r"\[TODO:[^\]\n]+\]", re.IGNORECASE),
)

GROUNDING_PATTERN = re.compile(
    r"<!--\s*project-os:grounding-status=(ready|needs-input)\s*-->",
    re.IGNORECASE,
)
TASK_BOUNDARY_MARKER = "project-os:task-boundary=declared"
SOURCE_SCOPE_MARKER = "project-os:source-scope-map=declared"
ASSET_PLACEMENT_MARKER = "project-os:asset-placement=declared"
DIRECTORY_MAP_MARKER = "project-os:directory-map=declared"
MARKDOWN_REFERENCE_PATTERN = re.compile(r"`([^`\r\n]+\.md)`", re.IGNORECASE)
ALLOWED_AGENTS_MARKDOWN_REFERENCES = {
    *(filename.casefold() for filename in CORE_FILES.values()),
    "readme.md",
    "archive/readme.md",
}
ALLOWED_ROOT_DOCUMENTS = {
    *(filename.casefold() for filename in CORE_FILES.values()),
    "readme.md",
    "contributing.md",
    "license.md",
    "security.md",
    "support.md",
    "code_of_conduct.md",
    "code-of-conduct.md",
    "claude.md",
}


def issue(severity: str, code: str, message: str, path: str | None = None) -> dict[str, str]:
    item = {"severity": severity, "code": code, "message": message}
    if path:
        item["path"] = path
    return item


def normalize_reference(value: str) -> str:
    return value.strip().replace("\\", "/").casefold()


def validate(root: Path) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"Project root is not a directory: {root}")

    issues: list[dict[str, str]] = []
    contents: dict[str, str] = {}

    for role, filename in CORE_FILES.items():
        path = root / filename
        if not path.is_file():
            issues.append(
                issue("error", "missing-core-role", f"Missing default source for {role}.", filename)
            )
            continue
        text = path.read_text(encoding="utf-8-sig")
        contents[filename] = text
        if not text.strip():
            issues.append(
                issue("error", "empty-core-file", "Core governance file is empty.", filename)
            )
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                issues.append(
                    issue(
                        "error",
                        "unresolved-placeholder",
                        "Unresolved template placeholder found.",
                        filename,
                    )
                )
                break

    agents = contents.get("AGENTS.md", "")
    if agents:
        for filename in CORE_FILES.values():
            if filename not in agents:
                issues.append(
                    issue(
                        "error",
                        "broken-cold-start-route",
                        f"AGENTS.md does not reference {filename}.",
                        "AGENTS.md",
                    )
                )
        if "archive" not in agents.casefold():
            issues.append(
                issue(
                    "warning",
                    "archive-boundary-unclear",
                    "AGENTS.md does not mention archive handling.",
                    "AGENTS.md",
                )
            )
        if TASK_BOUNDARY_MARKER not in agents.casefold():
            issues.append(
                issue(
                    "warning",
                    "task-boundary-marker-missing",
                    "AGENTS.md does not declare the project-level versus work-item boundary marker.",
                    "AGENTS.md",
                )
            )
        if ASSET_PLACEMENT_MARKER not in agents.casefold():
            issues.append(
                issue(
                    "warning",
                    "asset-placement-marker-missing",
                    (
                        "AGENTS.md does not declare a confirmed root and future-asset "
                        "placement policy."
                    ),
                    "AGENTS.md",
                )
            )

        unexpected_references = sorted(
            {
                reference
                for reference in (
                    normalize_reference(match)
                    for match in MARKDOWN_REFERENCE_PATTERN.findall(agents)
                )
                if reference not in ALLOWED_AGENTS_MARKDOWN_REFERENCES
            }
        )
        for reference in unexpected_references:
            issues.append(
                issue(
                    "warning",
                    "domain-source-in-agents",
                    (
                        f"AGENTS.md references non-governance source '{reference}'. "
                        "Verify that it is only a role mapping and does not copy business workflow details."
                    ),
                    "AGENTS.md",
                )
            )

    context = contents.get("project_context.md", "")
    grounding_status = "unknown"
    if context:
        grounding_matches = GROUNDING_PATTERN.findall(context)
        if len(grounding_matches) > 1:
            issues.append(
                issue(
                    "error",
                    "multiple-grounding-markers",
                    "project_context.md contains multiple grounding-status markers.",
                    "project_context.md",
                )
            )
        elif len(grounding_matches) == 1:
            grounding_status = grounding_matches[0].casefold()
        else:
            issues.append(
                issue(
                    "warning",
                    "grounding-marker-missing",
                    (
                        "project_context.md has no grounding-status marker; "
                        "treat onboarding as incomplete until reviewed."
                    ),
                    "project_context.md",
                )
            )

        if len(context.splitlines()) > 500:
            issues.append(
                issue(
                    "warning",
                    "context-too-long",
                    "Stable context exceeds 500 lines and may be mixing roles.",
                    "project_context.md",
                )
            )

    current_work = contents.get("current_work.md", "")
    if current_work and len(current_work.splitlines()) > 400:
        issues.append(
            issue(
                "warning",
                "current-work-too-long",
                "Current work exceeds 400 lines and may contain issue-level detail.",
                "current_work.md",
            )
        )

    artifact_index = contents.get("artifact_index.md", "")
    if artifact_index and SOURCE_SCOPE_MARKER not in artifact_index.casefold():
        issues.append(
            issue(
                "warning",
                "source-scope-map-marker-missing",
                (
                    "artifact_index.md does not declare a source-scope map. "
                    "Verify scope, owned facts, non-owned facts, authority, and lifecycle manually."
                ),
                "artifact_index.md",
            )
        )
    if artifact_index and DIRECTORY_MAP_MARKER not in artifact_index.casefold():
        issues.append(
            issue(
                "warning",
                "directory-map-marker-missing",
                (
                    "artifact_index.md does not declare a directory map. "
                    "Future asset placement may be ambiguous."
                ),
                "artifact_index.md",
            )
        )

    root_document_suffixes = {".md", ".mdx", ".rst", ".txt"}
    for path in sorted(root.iterdir(), key=lambda item: item.name.casefold()):
        if (
            path.is_file()
            and path.suffix.casefold() in root_document_suffixes
            and path.name.casefold() not in ALLOWED_ROOT_DOCUMENTS
        ):
            issues.append(
                issue(
                    "warning",
                    "root-document-placement-review",
                    (
                        "Ordinary document remains at the high-salience project root. "
                        "Confirm that it is a justified project-level anchor or relocate, "
                        "archive, or externalize it."
                    ),
                    path.name,
                )
            )

    archive = root / "archive"
    if archive.exists() and not (archive / "README.md").is_file():
        issues.append(
            issue(
                "warning",
                "archive-readme-missing",
                "archive/ exists without README.md declaring its authority boundary.",
                "archive",
            )
        )

    errors = sum(1 for item in issues if item["severity"] == "error")
    warnings = sum(1 for item in issues if item["severity"] == "warning")
    structure_status = "fail" if errors else "pass"

    placement_status = (
        "declared"
        if (
            ASSET_PLACEMENT_MARKER in agents.casefold()
            and DIRECTORY_MAP_MARKER in artifact_index.casefold()
        )
        else "unknown"
    )

    if errors:
        status = "invalid"
    elif grounding_status == "ready" and placement_status == "declared":
        status = "ready"
    else:
        status = "ready_with_gaps"

    return {
        "project_root": str(root),
        "status": status,
        "structure_status": structure_status,
        "grounding_status": grounding_status,
        "placement_status": placement_status,
        "errors": errors,
        "warnings": warnings,
        "issues": issues,
        "note": (
            "READY means the structure is valid and project_context.md declares grounded core facts. "
            "READY also requires a declared asset-placement policy and directory map. "
            "READY_WITH_GAPS means the governance kernel is usable but onboarding, source authority, "
            "or physical placement still needs input. Manually review the contamination and placement "
            "checks in validation-rubric.md."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a local Project OS and report grounding readiness."
    )
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
        print(f"Project OS validation: {report['status'].upper()}")
        print(
            f"Structure: {report['structure_status'].upper()}  "
            f"Grounding: {report['grounding_status'].upper()}  "
            f"Placement: {report['placement_status'].upper()}"
        )
        print(f"Errors: {report['errors']}  Warnings: {report['warnings']}")
        for item in report["issues"]:
            path = f" [{item['path']}]" if "path" in item else ""
            print(f"- {item['severity'].upper()} {item['code']}{path}: {item['message']}")
        print(report["note"])
    return 1 if report["status"] == "invalid" else 0


if __name__ == "__main__":
    raise SystemExit(main())

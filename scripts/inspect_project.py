#!/usr/bin/env python3
"""Shallow, content-free inspection for Project OS bootstrap and asset placement."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".venv",
    "venv",
    "node_modules",
    "vendor",
    "target",
    "dist",
    "build",
    "coverage",
    ".next",
    ".nuxt",
    ".cache",
    "__pycache__",
}

LARGE_ASSET_NAMES = {
    "assets",
    "audio",
    "video",
    "media",
    "models",
    "datasets",
    "data",
    "output",
    "outputs",
    "generated",
    "artifacts",
}

ARCHIVE_DIR_NAMES = {
    "archive",
    "archives",
}

PLACEMENT_DIR_NAMES = {
    "docs",
    "documentation",
    "product",
    "architecture",
    "design",
    "legal",
    "qa",
    "operations",
    "workstreams",
    "projects",
    "initiatives",
    "tasks",
    "research",
    "notes",
    "proposals",
    "rfcs",
    "assets",
    "archive",
    "archives",
}

GOVERNANCE_NAMES = {
    "agents.md",
    "claude.md",
    "readme.md",
    "project_context.md",
    "current_work.md",
    "decision_log.md",
    "artifact_index.md",
    "changelog.md",
    "roadmap.md",
    "status.md",
    "contributing.md",
}

TECH_MARKERS = {
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "cargo.toml",
    "go.mod",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "pubspec.yaml",
    "composer.json",
    "gemfile",
    "dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
}

SENSITIVE_SUFFIXES = {".pem", ".key", ".p12", ".pfx", ".jks", ".keystore"}
SENSITIVE_NAMES = {
    ".env",
    "credentials.json",
    "service-account.json",
    "secrets.json",
    "id_rsa",
    "id_ed25519",
}


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_sensitive_name(name: str) -> bool:
    lowered = name.casefold()
    return (
        lowered in SENSITIVE_NAMES
        or lowered.startswith(".env.")
        or Path(lowered).suffix in SENSITIVE_SUFFIXES
        or "credential" in lowered
        or "secret" in lowered
    )


def inspect(root: Path, max_depth: int) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError(f"Project root is not a directory: {root}")

    result: dict[str, Any] = {
        "project_root": str(root),
        "git_present": (root / ".git").exists(),
        "governance_candidates": [],
        "documentation_candidates": [],
        "root_document_candidates": [],
        "technology_markers": [],
        "placement_directory_candidates": [],
        "archive_directories": [],
        "archive_boundary_candidates": [],
        "large_asset_candidates": [],
        "sensitive_path_candidates": [],
        "skipped_directories": [],
        "root_entries": [],
    }

    def visit(directory: Path, depth: int) -> None:
        try:
            entries = sorted(os.scandir(directory), key=lambda item: item.name.casefold())
        except (OSError, PermissionError) as exc:
            result.setdefault("inspection_warnings", []).append(
                f"Could not inspect {relative(directory, root) or '.'}: {exc}"
            )
            return

        for entry in entries:
            path = Path(entry.path)
            rel = relative(path, root)
            lowered = entry.name.casefold()

            if depth == 0:
                result["root_entries"].append(
                    {"path": rel, "type": "directory" if entry.is_dir(follow_symlinks=False) else "file"}
                )

            if entry.is_symlink():
                continue

            if entry.is_dir(follow_symlinks=False):
                if depth == 0 and lowered in PLACEMENT_DIR_NAMES:
                    result["placement_directory_candidates"].append(rel)
                if lowered in ARCHIVE_DIR_NAMES:
                    result["archive_directories"].append(rel)
                    result["skipped_directories"].append(rel)
                    for boundary_name in ("README.md", "readme.md"):
                        boundary = path / boundary_name
                        if boundary.is_file():
                            result["archive_boundary_candidates"].append(
                                relative(boundary, root)
                            )
                            break
                    continue
                if lowered in LARGE_ASSET_NAMES:
                    result["large_asset_candidates"].append(rel)
                    continue
                if lowered in SKIP_DIRS:
                    result["skipped_directories"].append(rel)
                    continue
                if depth < max_depth:
                    visit(path, depth + 1)
                continue

            if not entry.is_file(follow_symlinks=False):
                continue

            if is_sensitive_name(entry.name):
                result["sensitive_path_candidates"].append(rel)
                continue

            if lowered in GOVERNANCE_NAMES:
                result["governance_candidates"].append(rel)
            if lowered in TECH_MARKERS:
                result["technology_markers"].append(rel)

            suffix = path.suffix.casefold()
            if suffix in {".md", ".mdx", ".rst", ".txt"} and depth <= max_depth:
                result["documentation_candidates"].append(rel)
                if depth == 0:
                    result["root_document_candidates"].append(rel)

    visit(root, 0)

    for key in (
        "governance_candidates",
        "documentation_candidates",
        "root_document_candidates",
        "technology_markers",
        "placement_directory_candidates",
        "archive_directories",
        "archive_boundary_candidates",
        "large_asset_candidates",
        "sensitive_path_candidates",
        "skipped_directories",
    ):
        result[key] = sorted(set(result[key]), key=str.casefold)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect project structure without reading file contents."
    )
    parser.add_argument("--root", required=True, help="Project root directory.")
    parser.add_argument(
        "--max-depth",
        type=int,
        default=3,
        help="Maximum directory depth to inspect (default: 3).",
    )
    parser.add_argument("--output", help="Optional JSON output file.")
    args = parser.parse_args()

    if args.max_depth < 0 or args.max_depth > 5:
        parser.error("--max-depth must be between 0 and 5")

    try:
        report = inspect(Path(args.root), args.max_depth)
    except ValueError as exc:
        parser.error(str(exc))

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        output = Path(args.output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

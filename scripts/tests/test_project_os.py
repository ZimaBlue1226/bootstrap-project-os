"""Script behavior regressions. Agent trials are a separate validation step."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from inspect_project import inspect
from validate_project_os import CORE_FILES, resolve_roles, validate


class ProjectOSTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="project-os-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def put(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def seed(self, mapping=None):
        owners = {**CORE_FILES, **(mapping or {})}
        texts = {
            "collaboration_rules": "Read project sources before changes.\n" + "\n".join(owners.values()),
            "stable_context": "Atlas helps local walkers find maintained trails. No booking or payment.",
            "current_work": "Pilot released by user confirmation. Next: review feedback.",
            "artifact_navigation": "docs owns specifications; work owns drafts. History is in Git.",
            "durable_decisions": "An existing ADR process owns architecture rationale.",
            "effective_history": "Public release notes are used by the packaging tool.",
        }
        if mapping is not None:
            texts["collaboration_rules"] += "\n<!-- project-os:role-map=" + json.dumps(mapping) + " -->"
        merged = {}
        for role, name in owners.items():
            if not name.startswith(("https://", "http://")):
                merged[name] = merged.get(name, "") + texts[role] + "\n"
        for name, content in merged.items():
            self.put(name, content)

    def codes(self, report):
        return {item["code"] for item in report["issues"]}

    def test_four_owners_without_markers_or_logs(self):
        self.seed()
        result = validate(self.root)
        self.assertEqual(result["status"], "valid")
        self.assertEqual(result["semantic_status"], "not_checked")
        self.assertEqual(result["issues"], [])
        self.assertEqual(set(p.name for p in self.root.iterdir()),
                         {"AGENTS.md", "project_context.md", "current_work.md", "artifact_index.md"})

    def test_no_self_reference_required(self):
        self.seed()
        path = self.root / "AGENTS.md"
        path.write_text(path.read_text(encoding="utf-8").replace("AGENTS.md", "this entry"), encoding="utf-8")
        self.assertEqual(validate(self.root)["status"], "valid")

    def test_inspection_and_validation_never_mutate(self):
        self.seed()
        self.put("docs/spec.md", "existing domain material")
        before = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        inspect(self.root, 3)
        validate(self.root)
        after = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_rendered_templates_form_usable_structure(self):
        values = {
            "PROJECT_NAME": "Atlas",
            "GIT_AND_COORDINATION_POLICY": "Inspect branch and worktree before editing; publish only on request.",
            "ASSET_PLACEMENT_RULES": "docs holds specifications; work holds drafts; create directories only as needed.",
            "PROJECT_PURPOSE_USERS_AND_SCOPE": "Atlas helps local walkers discover trails, without booking.",
            "STABLE_PRINCIPLES_WITH_RELEVANT_RATIONALE": "Offline discovery keeps the pilot usable without a signal.",
            "MAJOR_PARTS_AND_RESPONSIBILITY_BOUNDARIES": "Local catalog and client; domain details are in registered sources.",
            "MATERIAL_UNKNOWNS_OR_REMOVE_SECTION": "No material unknown blocks this document handoff.",
            "CURRENT_STAGE_AND_IMMEDIATE_OUTCOME": "Pilot released by user confirmation; review feedback next.",
            "NEXT_ACTIONS_WITH_SOURCES_AND_MATERIAL_BLOCKERS": "Collect the pilot feedback. No confirmed blocker.",
            "BASELINE_UNSYNCHRONIZED_WORK_AND_ACCESS_LIMITS": "Local synthetic fixture; no external deployment access.",
            "SOURCE": "project_context.md",
            "RESPONSIBILITY_AND_TRIGGER": "Project purpose and scope; read during cold start.",
            "AUTHORITY_SCOPE_AND_ACCESS": "User-confirmed synthetic project context.",
            "USEFUL_LOCAL_SOURCES_AND_ASSET_LOCATIONS": "No separate local assets are needed for this fixture.",
            "PLACEMENT_POLICY_OR_POINTER_TO_ITS_OWNER": "The entry owns placement policy.",
            "VERSION_HISTORY_OR_EXISTING_RETENTION_SOURCE": "Git retains committed versions; untracked files need preservation.",
        }
        templates = Path(__file__).resolve().parents[2] / "assets/templates"
        for template in templates.glob("*.template"):
            rendered = template.read_text(encoding="utf-8")
            for key, value in values.items():
                rendered = rendered.replace("{{" + key + "}}", value)
            self.put(template.name.removesuffix(".template"), rendered)
        self.assertEqual(validate(self.root)["issues"], [])
        self.assertEqual(len(list(self.root.iterdir())), 4)

    def test_reuse_existing_readme_status_and_adr(self):
        self.seed({"stable_context": "README.md", "current_work": "STATUS.md",
                   "durable_decisions": "docs/adr-index.md"})
        self.put("src/app.txt", "user work")
        self.assertEqual(validate(self.root)["status"], "valid")
        self.assertFalse((self.root / "project_context.md").exists())
        self.assertFalse((self.root / "current_work.md").exists())
        self.assertFalse((self.root / "decision_log.md").exists())
        self.assertEqual((self.root / "src/app.txt").read_text(), "user work")

    def test_shared_owner(self):
        self.seed({"stable_context": "README.md", "current_work": "README.md"})
        self.assertEqual(validate(self.root)["status"], "valid")

    def test_purposeful_history_is_optional_but_supported(self):
        self.seed({"effective_history": "RELEASE_NOTES.md"})
        self.assertEqual(validate(self.root)["status"], "valid")
        (self.root / "RELEASE_NOTES.md").unlink()
        self.assertIn("missing-core-role", self.codes(validate(self.root)))

    def test_unmapped_legacy_logs_are_not_read(self):
        self.seed()
        self.put("changelog.md", "{{unrelated template example}}")
        self.put("decision_log.md", "old content")
        original = Path.read_text
        def guarded(path, *args, **kwargs):
            self.assertNotIn(path.name, {"changelog.md", "decision_log.md"})
            return original(path, *args, **kwargs)
        with patch.object(Path, "read_text", guarded):
            self.assertEqual(validate(self.root)["status"], "valid")
        self.assertTrue((self.root / "changelog.md").exists())

    def test_external_owner_is_a_review_item_not_a_local_copy(self):
        self.seed({"current_work": "https://example.invalid/board"})
        result = validate(self.root)
        self.assertEqual(result["status"], "valid")
        self.assertEqual(result["external_roles"], ["current_work"])
        self.assertIn("external-role-unverified", self.codes(result))
        self.assertEqual(result["semantic_status"], "not_checked")
        self.assertFalse((self.root / "current_work.md").exists())

    def test_declared_gap_is_not_a_structural_failure(self):
        self.seed()
        self.put("project_context.md", "Atlas purpose known; current source ownership needs input.\n"
                 "<!-- project-os:grounding-status=needs-input -->")
        result = validate(self.root)
        self.assertEqual(result["status"], "valid")
        self.assertIn("declared-context-gap", self.codes(result))

    def test_ready_marker_cannot_certify_semantics(self):
        self.seed()
        self.put("project_context.md", "Atlas.\n<!-- project-os:grounding-status=ready -->")
        self.assertEqual(validate(self.root)["semantic_status"], "not_checked")

    def test_malformed_or_conflicting_grounding_declaration(self):
        self.seed()
        for value in ("unknown", "ready -->\n<!-- project-os:grounding-status=needs-input"):
            self.put("project_context.md", "<!-- project-os:grounding-status=" + value + " -->")
            self.assertIn("invalid-grounding-marker", self.codes(validate(self.root)))
        self.put("project_context.md", "<!-- project-os:grounding-status=ready")
        self.assertEqual(validate(self.root)["status"], "invalid")

    def test_missing_owner_and_registration(self):
        self.seed()
        (self.root / "current_work.md").unlink()
        self.assertIn("missing-core-role", self.codes(validate(self.root)))
        self.seed()
        self.put("AGENTS.md", "Read project_context.md, then artifact_index.md.")
        self.assertIn("unregistered-role-source", self.codes(validate(self.root)))

    def test_placeholders_empty_and_unreadable_content(self):
        self.seed()
        for content in ("{{UNRESOLVED}}", "[TODO: add context]", ""):
            self.put("current_work.md", content)
            self.assertEqual(validate(self.root)["status"], "invalid")
        (self.root / "current_work.md").write_bytes(b"\xff\xfe\x00")
        self.assertIn("unreadable-role-source", self.codes(validate(self.root)))

    def test_invalid_role_maps(self):
        for value in ('[]', '{bad}', '{"unknown":"file.md"}', '{"stable_context":null}',
                      '{"stable_context":"A.md","stable_context":"B.md"}',
                      '{"collaboration_rules":"elsewhere.md"}'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                resolve_roles("<!-- project-os:role-map=" + value + " -->")
        with self.assertRaises(ValueError):
            resolve_roles("<!-- project-os:role-map={} -->\n<!-- project-os:role-map={} -->")

    def test_invalid_mapping_reported_by_validator(self):
        self.seed()
        self.put("AGENTS.md", "<!-- project-os:role-map={bad} -->")
        self.assertIn("invalid-role-map", self.codes(validate(self.root)))

    def test_unsafe_owner_is_rejected_before_content_read(self):
        self.seed()
        base = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        allowed = set(CORE_FILES.values())
        original = Path.read_text
        def guarded(path, *args, **kwargs):
            self.assertIn(path.name, allowed)
            self.assertEqual(path.parent, self.root)
            return original(path, *args, **kwargs)
        for source in ("../outside.md", "/outside.md", "C:/outside.md", ".env", ".envrc",
                       ".git/config", "archive/old.md", "secrets/data.md", "docs/key.pem",
                       ".tmp/draft.md", "node_modules/README.md", "docs\\context.md"):
            with self.subTest(source=source):
                self.put("AGENTS.md", base + '\n<!-- project-os:role-map='
                         + json.dumps({"stable_context": source}) + ' -->')
                with patch.object(Path, "read_text", guarded):
                    self.assertIn("unsafe-role-source", self.codes(validate(self.root)))

    def test_nested_repository_owner_rejected(self):
        self.seed()
        self.put("backend/.git", "synthetic gitdir boundary")
        self.put("backend/README.md", "must not be consumed by parent validator")
        self.put("AGENTS.md", '<!-- project-os:role-map={"stable_context":"backend/README.md"} -->')
        self.assertIn("unsafe-role-source", self.codes(validate(self.root)))

    def test_directory_cannot_own_role(self):
        self.seed()
        (self.root / "docs").mkdir()
        self.put("AGENTS.md", '<!-- project-os:role-map={"stable_context":"docs"} -->')
        self.assertIn("missing-core-role", self.codes(validate(self.root)))

    def test_linked_entry_and_junction_owner_rejected(self):
        self.seed()
        with patch.object(Path, "is_symlink", lambda p: p.name == "AGENTS.md"):
            result = validate(self.root)
            self.assertEqual(result["status"], "invalid")
            self.assertIn("unsafe-role-source", self.codes(result))
        self.seed({"stable_context": "docs/context.md"})
        with patch.object(Path, "is_junction", lambda p: p.name == "docs", create=True):
            self.assertIn("unsafe-role-source", self.codes(validate(self.root)))

    def test_invalid_external_url(self):
        self.seed()
        for source in ("https://", "https://user:pass@example.invalid/context"):
            self.put("AGENTS.md", '<!-- project-os:role-map='
                     + json.dumps({"stable_context": source}) + ' -->')
            self.assertIn("unsafe-role-source", self.codes(validate(self.root)))

    def test_inspector_boundaries(self):
        for name in ("archive/README.md", "archive/old.md", ".tmp/draft.md", "assets/large.md",
                     "backend/.git/config", "backend/README.md", "node_modules/dep.md",
                     "work/plan.md", "runbooks/publish.md", "tools/helper.md", ".envrc",
                     "credentials.json", "secrets/private.md", ".ssh/private.md", "docs/current.md"):
            self.put(name, "synthetic fixture")
        result = inspect(self.root, 3)
        self.assertEqual(result["nested_repositories"], ["backend"])
        self.assertEqual(result["sensitive_path_candidates"], [".envrc", ".ssh", "credentials.json", "secrets"])
        self.assertEqual(result["archive_boundary_candidates"], ["archive/README.md"])
        self.assertEqual(set(result["documentation_candidates"]),
                         {"work/plan.md", "runbooks/publish.md", "tools/helper.md", "docs/current.md"})

    def test_inspector_junction_not_followed(self):
        self.put("linked/file.md", "must not be discovered")
        with patch.object(Path, "is_junction", lambda p: p.name == "linked", create=True):
            self.assertEqual(inspect(self.root, 3)["documentation_candidates"], [])

    def test_inspector_never_reads_contents(self):
        self.put("docs/spec.md", "opaque")
        with patch.object(Path, "read_text", side_effect=AssertionError("content read")):
            self.assertIn("docs/spec.md", inspect(self.root, 3)["documentation_candidates"])

    def test_no_warning_for_length_or_conditional_runbook(self):
        self.seed()
        path = self.root / "AGENTS.md"
        path.write_text(path.read_text(encoding="utf-8") +
                        "\nRead runbooks/release.md only when publishing.\n", encoding="utf-8")
        self.put("project_context.md", "A maintained fact.\n" * 501)
        self.put("notes.md", "A root document is not itself a governance failure.")
        self.assertEqual(validate(self.root)["issues"], [])

    def test_empty_project_invalid(self):
        self.assertEqual(validate(self.root)["status"], "invalid")

    def test_cli_json_and_exit_status(self):
        self.seed()
        command = [sys.executable, "-B", "-X", "utf8",
                   str(Path(__file__).resolve().parents[1] / "validate_project_os.py"),
                   "--root", str(self.root), "--json"]
        result = subprocess.run(command, text=True, encoding="utf-8", capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["semantic_status"], "not_checked")
        (self.root / "current_work.md").unlink()
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
        command[-2] = str(self.root / "missing")
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)


if __name__ == "__main__":
    unittest.main()

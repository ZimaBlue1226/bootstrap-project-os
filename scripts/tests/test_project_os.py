"""Deterministic regressions, not agent behavior evaluation. Uses disposable fixtures."""
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

    def seed(self, mapping=None, grounding="ready"):
        owners = {**CORE_FILES, **(mapping or {})}
        texts = {
            "collaboration_rules": "Atlas rules. Keep archive non-authoritative.\n"
                "<!-- project-os:task-boundary=declared -->\n"
                "<!-- project-os:asset-placement=declared -->\n" + "\n".join(owners.values()),
            "stable_context": "Atlas maintains trail information.\n"
                f"<!-- project-os:grounding-status={grounding} -->",
            "current_work": "Verify the released search flow.",
            "durable_decisions": "No durable decisions confirmed yet.",
            "artifact_navigation": "<!-- project-os:source-scope-map=declared -->\n"
                "<!-- project-os:directory-map=declared -->\n"
                "docs owns specifications; work owns drafts. Create only when needed.",
            "effective_history": "Governance owners registered today.",
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

    def test_default_kernel_structural_not_semantic(self):
        self.seed()
        report = validate(self.root)
        self.assertEqual(report["status"], "ready")
        self.assertEqual(report["semantic_status"], "not_checked")
        self.assertEqual((report["errors"], report["warnings"]), (0, 0))

    def test_no_directories_or_mutations(self):
        self.seed()
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        inspect(self.root, 3)
        validate(self.root)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_rendered_entry_templates(self):
        self.seed()
        values = {
            "PROJECT_NAME": "Atlas",
            "ASSET_PLACEMENT_RULES": "Confirmed domain facts use docs/; active drafts use work/. Create only with a real asset.",
            "CROSS_PROJECT_OPERATING_RULES": "Do not change production systems or commit without authorization.",
            "GROUNDING_STATUS": "ready",
            "PROJECT_IDENTITY_AND_PURPOSE": "Atlas helps walkers find maintained local trails.",
            "USERS_OR_CONSUMERS": "Local walkers.",
            "CURRENT_PROJECT_SCOPE": "Trail discovery only; no booking or payment.",
            "CORE_MODULES_OR_WORKSTREAMS": "Trail search and details.",
            "STABLE_PROJECT_CONSTRAINTS": "No production access is included in document work.",
            "DOMAIN": "Project",
            "CANONICAL_SOURCE": "project_context.md",
            "SOURCE_SCOPE": "Project identity and scope",
            "AUTHORITY_BASIS": "Synthetic user confirmation",
            "SUMMARY_BOUNDARY": "Detailed trail rules are not specified here.",
            "PROJECT_LEVEL_UNKNOWNS": "No material project-level unknowns for this document-only handoff.",
            "CURRENT_PROJECT_STAGE": "Pilot released; user-confirmed, not independently tested.",
            "IMMEDIATE_PROJECT_OBJECTIVE": "Review pilot feedback for the next iteration.",
            "WORKSTREAM": "Pilot feedback",
            "STATUS_AND_SCOPE": "Planned feedback review, not an implemented product change.",
            "NEXT_MILESTONE": "Agree the next product improvement.",
            "WORKSTREAM_SOURCE": "No separate execution source yet; register when work begins.",
            "BLOCKERS_AND_DECISIONS": "No confirmed project blocker.",
            "HANDOFF_ITEMS": "Ask for existing pilot feedback when starting the review.",
        }
        templates = Path(__file__).resolve().parents[2] / "assets/templates"
        for name in ("AGENTS.md", "project_context.md", "current_work.md"):
            rendered = (templates / (name + ".template")).read_text(encoding="utf-8")
            for key, value in values.items():
                rendered = rendered.replace("{{" + key + "}}", value)
            self.put(name, rendered)
        report = validate(self.root)
        self.assertEqual((report["status"], report["warnings"]), ("ready", 0), report)
        self.assertEqual({p.name for p in self.root.iterdir()}, set(CORE_FILES.values()))

    def test_reuse_readme_adr_and_preserve_code(self):
        self.seed({"stable_context": "README.md", "durable_decisions": "docs/adr-index.md"})
        self.put("src/app.txt", "existing user code")
        self.assertEqual(validate(self.root)["status"], "ready")
        self.assertFalse((self.root / "project_context.md").exists())
        self.assertFalse((self.root / "decision_log.md").exists())
        self.assertEqual((self.root / "src/app.txt").read_text(), "existing user code")

    def test_shared_owner(self):
        self.seed({"stable_context": "README.md", "current_work": "README.md"})
        self.assertEqual(validate(self.root)["status"], "ready")

    def test_external_owner_not_fetched_or_duplicated(self):
        self.seed({"durable_decisions": "https://example.invalid/decisions"})
        report = validate(self.root)
        self.assertEqual(report["status"], "ready_with_gaps")
        self.assertIn("external-role-unverified", self.codes(report))
        self.assertFalse((self.root / "decision_log.md").exists())

    def test_needs_input_stays_gap(self):
        self.seed(grounding="needs-input")
        self.assertEqual(validate(self.root)["status"], "ready_with_gaps")

    def test_missing_mapped_source(self):
        self.seed({"durable_decisions": "docs/adr-index.md"})
        (self.root / "docs/adr-index.md").unlink()
        self.assertIn("missing-core-role", self.codes(validate(self.root)))

    def test_placeholder_invalid(self):
        self.seed()
        self.put("current_work.md", "{{UNRESOLVED}}")
        self.assertEqual(validate(self.root)["status"], "invalid")

    def test_invalid_role_maps(self):
        for value in ('[]', '{bad}', '{"unknown":"file.md"}',
                      '{"stable_context":"A.md","stable_context":"B.md"}',
                      '{"collaboration_rules":"elsewhere.md"}'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                resolve_roles("<!-- project-os:role-map=" + value + " -->")

    def test_multiple_maps(self):
        with self.assertRaises(ValueError):
            resolve_roles("<!-- project-os:role-map={} -->\n<!-- project-os:role-map={} -->")

    def test_unsafe_mappings(self):
        self.seed()
        base = (self.root / "AGENTS.md").read_text(encoding="utf-8")
        for source in ("../outside.md", "/outside.md", "C:/outside.md", ".env",
                       ".git/config", "archive/old.md", "secrets/data.md", "docs/key.pem"):
            with self.subTest(source=source):
                self.put("AGENTS.md", base + '\n<!-- project-os:role-map='
                         + json.dumps({"durable_decisions": source}) + ' -->')
                self.assertIn("unsafe-role-source", self.codes(validate(self.root)))

    def test_junction_mapping(self):
        self.seed({"durable_decisions": "docs/adr-index.md"})
        with patch.object(Path, "is_junction", lambda p: p.name == "docs", create=True):
            self.assertIn("unsafe-role-source", self.codes(validate(self.root)))

    def test_inspector_boundaries(self):
        for name in ("archive/README.md", "archive/old.md", ".tmp/draft.md", "assets/large.md",
                     "backend/.git/config", "backend/README.md", "node_modules/dep.md",
                     "work/plan.md", "runbooks/publish.md", "tools/helper.md",
                     "credentials.json", "secrets/private.md", ".ssh/private.md", "docs/current.md"):
            self.put(name, "synthetic fixture")
        result = inspect(self.root, 3)
        self.assertEqual(result["nested_repositories"], ["backend"])
        self.assertEqual(result["sensitive_path_candidates"], [".ssh", "credentials.json", "secrets"])
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

    def test_empty_project_invalid(self):
        self.assertEqual(validate(self.root)["status"], "invalid")

    def test_cli_json_and_exit_status(self):
        self.seed()
        command = [sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve().parents[1] / "validate_project_os.py"),
                   "--root", str(self.root), "--json"]
        result = subprocess.run(command, text=True, encoding="utf-8", capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["semantic_status"], "not_checked")
        (self.root / "current_work.md").unlink()
        self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()

import tempfile
import unittest
from pathlib import Path

from shared.adopt_harness import AdoptHarnessOptions, adopt_harness


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = REPO_ROOT / "assets" / "harness-template"


class AdoptHarnessTests(unittest.TestCase):
    def test_dry_run_reports_template_docs_as_refactors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "docs").mkdir()
            (target / "docs" / "index.md").write_text("# Existing docs\n")

            options = AdoptHarnessOptions(
                target_dir=target,
                template_dir=TEMPLATE_ROOT,
                project_name="Legacy Service",
                product_description="An existing service that needs harness discipline.",
                dry_run=True,
            )

            result = adopt_harness(options)

            self.assertIn("docs/index.md", result.refactored_paths)
            self.assertFalse(result.conflicts)
            self.assertFalse(result.plan_path.exists())

    def test_dry_run_preserves_non_doc_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "AGENTS.md").write_text("# Existing\n")

            options = AdoptHarnessOptions(
                target_dir=target,
                template_dir=TEMPLATE_ROOT,
                project_name="Legacy Service",
                product_description="An existing service that needs harness discipline.",
                dry_run=True,
            )

            result = adopt_harness(options)

            self.assertIn("AGENTS.md", result.conflicts)
            self.assertEqual("# Existing\n", (target / "AGENTS.md").read_text())
            self.assertFalse(result.plan_path.exists())

    def test_apply_adds_missing_files_refactors_docs_and_keeps_non_doc_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / ".git").mkdir()
            (target / "docs").mkdir()
            (target / "docs" / "index.md").write_text("# Legacy index\n")
            (target / "AGENTS.md").write_text("# Existing agents\n")
            options = AdoptHarnessOptions(
                target_dir=target,
                template_dir=TEMPLATE_ROOT,
                project_name="Legacy Service",
                product_description="An existing service that needs harness discipline.",
                dry_run=False,
            )

            result = adopt_harness(options)

            self.assertTrue((target / "AGENTS.md").exists())
            self.assertTrue((target / "docs" / "index.md").exists())
            self.assertTrue(result.plan_path.exists())
            self.assertIn("docs/index.md", result.refactored_paths)
            self.assertIn("AGENTS.md", result.conflicts)
            self.assertNotEqual("# Legacy index\n", (target / "docs" / "index.md").read_text())
            self.assertEqual("# Existing agents\n", (target / "AGENTS.md").read_text())


if __name__ == "__main__":
    unittest.main()

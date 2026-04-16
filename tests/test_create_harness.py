import tempfile
import unittest
from pathlib import Path

from shared.create_harness import CreateHarnessOptions, create_harness


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = REPO_ROOT / "assets" / "harness-template"


class CreateHarnessTests(unittest.TestCase):
    def test_bootstrap_empty_repo_copies_template_and_creates_plan(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            options = CreateHarnessOptions(
                target_dir=target,
                template_dir=TEMPLATE_ROOT,
                project_name="Acme Radar",
                project_slug="acme-radar",
                product_description="Track product signals and incident risk.",
                primary_stacks=["backend", "frontend"],
                platforms=["web"],
                ops_profile="moderate",
                testing_posture="behavior-first",
                emphasis_areas=["observability"],
            )

            result = create_harness(options)

            self.assertTrue((target / "AGENTS.md").exists())
            self.assertTrue((target / "README.md").exists())
            self.assertTrue((target / "docs" / "plans" / "active").exists())
            self.assertEqual([], result.refused_paths)
            self.assertTrue(result.plan_path.exists())

    def test_bootstrap_refuses_non_empty_repo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            (target / "package.json").write_text('{"name": "existing-app"}')
            options = CreateHarnessOptions(
                target_dir=target,
                template_dir=TEMPLATE_ROOT,
                project_name="Acme Radar",
                project_slug="acme-radar",
                product_description="Track product signals and incident risk.",
                primary_stacks=["backend"],
                platforms=["web"],
                ops_profile="moderate",
                testing_posture="behavior-first",
                emphasis_areas=[],
            )

            with self.assertRaisesRegex(ValueError, "adopt-harness"):
                create_harness(options)


if __name__ == "__main__":
    unittest.main()

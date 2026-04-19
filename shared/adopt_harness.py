from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

from .common import (
    build_replacements,
    copy_with_replacements,
    inventory_template,
    normalize_slug,
    result_to_json,
    today_stamp,
    write_change_plan,
)


@dataclass(frozen=True)
class AdoptHarnessOptions:
    target_dir: Path
    template_dir: Path
    project_name: str | None = None
    product_description: str | None = None
    dry_run: bool = True


@dataclass(frozen=True)
class AdoptHarnessResult:
    plan_path: Path
    copied_paths: list[str]
    refactored_paths: list[str]
    conflicts: list[str]
    matching_paths: list[str]
    dry_run: bool

    def to_json(self) -> str:
        payload = asdict(self)
        payload["plan_path"] = str(self.plan_path)
        return result_to_json(payload)


def is_template_owned_doc(path: Path) -> bool:
    return bool(path.parts) and path.parts[0] == "docs"


def adopt_harness(options: AdoptHarnessOptions) -> AdoptHarnessResult:
    target_dir = options.target_dir.resolve()
    template_dir = options.template_dir.resolve()
    project_name = options.project_name or target_dir.name or "Existing Project"
    project_slug = normalize_slug(project_name)
    product_description = (
        options.product_description
        or f"{project_name} adopting the your-harness workflow."
    )
    replacements = build_replacements(
        project_name=project_name,
        project_slug=project_slug,
        product_description=product_description,
    )

    inventory = inventory_template(
        template_dir=template_dir,
        target_dir=target_dir,
        replacements=replacements,
    )
    refactor_paths = [path for path in inventory.conflicts if is_template_owned_doc(path)]
    manual_conflicts = [
        path for path in inventory.conflicts if not is_template_owned_doc(path)
    ]
    planned_plan_path = (
        target_dir
        / "docs"
        / "plans"
        / "active"
        / f"{today_stamp()}-adopt-{project_slug}.md"
    )

    if options.dry_run:
        return AdoptHarnessResult(
            plan_path=planned_plan_path,
            copied_paths=[],
            refactored_paths=[str(path) for path in refactor_paths],
            conflicts=[str(path) for path in manual_conflicts],
            matching_paths=[str(path) for path in inventory.matching],
            dry_run=True,
        )

    plan_path = write_change_plan(
        target_dir=target_dir,
        slug=f"adopt-{project_slug}",
        title=f"Adopt your-harness in {project_name}",
        summary=(
            f"Introduce the your-harness workflow additively in {project_name}. "
            f"Project context: {product_description}"
        ),
        planned_changes=[
            "Copy missing harness-owned files into the repository without overwriting already-present project files.",
            "Rewrite template-owned docs under `docs/` toward the harness defaults while leaving non-doc conflicts untouched for manual resolution.",
            "Surface copied, refactored, matching, and conflicting paths clearly so the project can finish any manual integration work deliberately.",
        ],
        expected_behavior=[
            "Missing harness docs and templates are added without overwriting existing files.",
            "Template-owned docs are rewritten toward the harness defaults.",
            "Non-doc conflicts remain unchanged and are surfaced for manual resolution.",
            "A live change plan exists before the adoption file updates.",
        ],
        tasks=[
            "Copy missing harness files without overwriting non-conflicting project files.",
            "Rewrite template-owned docs toward the harness defaults and preserve non-doc conflicts for manual resolution.",
            "Review the adoption summary and run repo-specific follow-up checks after applying the scaffold.",
        ],
        hypotheses=[
            "The project already has code or docs that should be preserved.",
            "Template-owned docs should converge on the harness structure during adoption.",
            "Non-doc conflicts should still be merged deliberately rather than overwritten.",
        ],
        tests=[
            "Review refactored docs and manual conflicts after adoption.",
            "Confirm the docs index and plan directories were added when missing.",
            "Run repo-specific checks after integrating any conflicts.",
        ],
        observability=[
            "Use the adoption summary to distinguish copied, refactored, matching, and conflicting paths.",
        ],
    )

    copied_paths: list[str] = []
    for relative_path in inventory.missing:
        source_path = template_dir / relative_path
        copied = copy_with_replacements(
            source_path=source_path,
            template_dir=template_dir,
            target_dir=target_dir,
            replacements=replacements,
        )
        copied_paths.append(str(copied))

    refactored_result_paths: list[str] = []
    for relative_path in refactor_paths:
        source_path = template_dir / relative_path
        rewritten = copy_with_replacements(
            source_path=source_path,
            template_dir=template_dir,
            target_dir=target_dir,
            replacements=replacements,
        )
        refactored_result_paths.append(str(rewritten))

    return AdoptHarnessResult(
        plan_path=plan_path,
        copied_paths=copied_paths,
        refactored_paths=refactored_result_paths,
        conflicts=[str(path) for path in manual_conflicts],
        matching_paths=[str(path) for path in inventory.matching],
        dry_run=False,
    )

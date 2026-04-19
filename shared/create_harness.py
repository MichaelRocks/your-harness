from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path

from .common import (
    build_replacements,
    copy_with_replacements,
    iter_template_files,
    normalize_slug,
    refused_bootstrap_paths,
    result_to_json,
    write_change_plan,
)


@dataclass(frozen=True)
class CreateHarnessOptions:
    target_dir: Path
    template_dir: Path
    project_name: str
    product_description: str
    project_slug: str | None = None
    primary_stacks: list[str] = field(default_factory=list)
    platforms: list[str] = field(default_factory=list)
    ops_profile: str = "standard"
    testing_posture: str = "behavior-first"
    emphasis_areas: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class CreateHarnessResult:
    plan_path: Path
    copied_paths: list[str]
    refused_paths: list[str]

    def to_json(self) -> str:
        payload = asdict(self)
        payload["plan_path"] = str(self.plan_path)
        return result_to_json(payload)


def create_harness(options: CreateHarnessOptions) -> CreateHarnessResult:
    target_dir = options.target_dir.resolve()
    template_dir = options.template_dir.resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    refused_paths = refused_bootstrap_paths(target_dir)
    if refused_paths:
        refused_list = ", ".join(refused_paths)
        raise ValueError(
            f"Target repository is not empty enough for create-harness: {refused_list}. "
            "Use adopt-harness for an existing project."
        )

    project_slug = options.project_slug or normalize_slug(options.project_name)
    replacements = build_replacements(
        project_name=options.project_name,
        project_slug=project_slug,
        product_description=options.product_description,
        primary_stacks=options.primary_stacks,
        platforms=options.platforms,
        ops_profile=options.ops_profile,
        testing_posture=options.testing_posture,
        emphasis_areas=options.emphasis_areas,
    )
    plan_path = write_change_plan(
        target_dir=target_dir,
        slug=f"bootstrap-{project_slug}",
        title=f"Bootstrap the {options.project_name} harness",
        summary=(
            f"Initialize {options.project_name} with the your-harness scaffold. "
            f"Product description: {options.product_description}"
        ),
        planned_changes=[
            "Copy the canonical harness scaffold into the repository with project-specific replacements in the root docs and templates.",
            "Seed the repository with routing docs, planning templates, quality guidance, and operations/reference directories that future tracked changes will use.",
            "Limit this bootstrap to workflow scaffolding and initial project framing rather than adding product-specific executable code.",
        ],
        expected_behavior=[
            "The repository contains the harness routing docs and templates.",
            "The project README captures the initial product framing.",
            "A live plan exists before follow-on tracked changes.",
        ],
        tasks=[
            "Copy the scaffold files into the repository.",
            "Verify the generated README and AGENTS routing reflect the provided project context.",
            "Confirm the docs and plan directories exist for follow-on tracked changes.",
        ],
        hypotheses=[
            f"Primary stacks: {', '.join(options.primary_stacks) or 'TBD'}",
            f"Platforms: {', '.join(options.platforms) or 'TBD'}",
            f"Initial emphasis areas: {', '.join(options.emphasis_areas) or 'None yet'}",
        ],
        tests=[
            "Confirm the copied scaffold paths exist.",
            "Review the generated README and AGENTS routing text.",
            "Run repo-specific validation once executable code exists.",
        ],
        observability=[
            "Keep future change plans and incident reports live in docs.",
        ],
    )

    copied_paths: list[str] = []
    for source_path in iter_template_files(template_dir):
        relative_path = copy_with_replacements(
            source_path=source_path,
            template_dir=template_dir,
            target_dir=target_dir,
            replacements=replacements,
        )
        copied_paths.append(str(relative_path))

    return CreateHarnessResult(
        plan_path=plan_path,
        copied_paths=copied_paths,
        refused_paths=refused_paths,
    )

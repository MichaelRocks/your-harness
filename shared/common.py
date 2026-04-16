from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import hashlib
import json
import shutil
from pathlib import Path
from typing import Iterable


ALLOWED_BOOTSTRAP_PATHS = {
    ".editorconfig",
    ".git",
    ".gitattributes",
    ".github",
    ".gitignore",
}

TEXT_FILE_EXTENSIONS = {
    "",
    ".json",
    ".md",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class TemplateInventory:
    missing: list[Path]
    conflicts: list[Path]
    matching: list[Path]


def today_stamp() -> str:
    return date.today().isoformat()


def normalize_slug(value: str) -> str:
    cleaned = []
    last_was_dash = False
    for char in value.lower().strip():
        if char.isalnum():
            cleaned.append(char)
            last_was_dash = False
            continue
        if not last_was_dash:
            cleaned.append("-")
            last_was_dash = True
    slug = "".join(cleaned).strip("-")
    return slug or "project"


def join_or_default(values: Iterable[str], default: str) -> str:
    items = [value.strip() for value in values if value.strip()]
    return ", ".join(items) if items else default


def build_replacements(
    *,
    project_name: str,
    project_slug: str,
    product_description: str,
    primary_stacks: Iterable[str] | None = None,
    platforms: Iterable[str] | None = None,
    ops_profile: str | None = None,
    testing_posture: str | None = None,
    emphasis_areas: Iterable[str] | None = None,
) -> dict[str, str]:
    return {
        "{{PROJECT_NAME}}": project_name.strip(),
        "{{PROJECT_SLUG}}": project_slug.strip(),
        "{{PRODUCT_DESCRIPTION}}": product_description.strip(),
        "{{PRIMARY_STACKS}}": join_or_default(primary_stacks or [], "TBD"),
        "{{PLATFORMS}}": join_or_default(platforms or [], "TBD"),
        "{{OPS_PROFILE}}": (ops_profile or "standard").strip(),
        "{{TESTING_POSTURE}}": (testing_posture or "behavior-first").strip(),
        "{{EMPHASIS_AREAS}}": join_or_default(emphasis_areas or [], "None yet"),
    }


def render_template_text(content: str, replacements: dict[str, str]) -> str:
    rendered = content
    for token, value in replacements.items():
        rendered = rendered.replace(token, value)
    return rendered


def should_render_text(path: Path) -> bool:
    if path.name.startswith("."):
        return True
    return path.suffix.lower() in TEXT_FILE_EXTENSIONS


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rendered_bytes(path: Path, replacements: dict[str, str] | None = None) -> bytes:
    if replacements and should_render_text(path):
        text = path.read_text()
        return render_template_text(text, replacements).encode()
    return path.read_bytes()


def iter_template_files(template_dir: Path) -> list[Path]:
    return sorted(path for path in template_dir.rglob("*") if path.is_file())


def inventory_template(
    template_dir: Path,
    target_dir: Path,
    replacements: dict[str, str] | None = None,
) -> TemplateInventory:
    missing: list[Path] = []
    conflicts: list[Path] = []
    matching: list[Path] = []

    for source_path in iter_template_files(template_dir):
        relative_path = source_path.relative_to(template_dir)
        target_path = target_dir / relative_path
        if not target_path.exists():
            missing.append(relative_path)
            continue
        if target_path.is_dir():
            conflicts.append(relative_path)
            continue
        if rendered_bytes(source_path, replacements) == target_path.read_bytes():
            matching.append(relative_path)
        else:
            conflicts.append(relative_path)

    return TemplateInventory(missing=missing, conflicts=conflicts, matching=matching)


def copy_with_replacements(
    *,
    source_path: Path,
    template_dir: Path,
    target_dir: Path,
    replacements: dict[str, str],
) -> Path:
    relative_path = source_path.relative_to(template_dir)
    target_path = target_dir / relative_path
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if should_render_text(source_path):
        target_path.write_text(
            render_template_text(source_path.read_text(), replacements)
        )
    else:
        shutil.copy2(source_path, target_path)
    return relative_path


def write_change_plan(
    *,
    target_dir: Path,
    slug: str,
    title: str,
    summary: str,
    expected_behavior: list[str],
    hypotheses: list[str],
    tests: list[str],
    observability: list[str],
) -> Path:
    plan_dir = target_dir / "docs" / "plans" / "active"
    plan_dir.mkdir(parents=True, exist_ok=True)
    filename = unique_plan_filename(plan_dir, slug)
    plan_path = plan_dir / filename

    lines = [
        f"# {title}",
        "",
        "## Change Summary",
        "",
        summary,
        "",
        "## Expected Behavior",
        "",
    ]
    lines.extend(f"- {item}" for item in expected_behavior)
    lines.extend(
        [
            "",
            "## Hypotheses / Findings",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in hypotheses)
    lines.extend(
        [
            "",
            "## Planned Tests",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in tests)
    lines.extend(
        [
            "",
            "## Planned Observability",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in observability)
    lines.extend(
        [
            "",
            "## Completion Notes",
            "",
            "- Pending implementation.",
            "",
        ]
    )
    plan_path.write_text("\n".join(lines))
    return plan_path


def unique_plan_filename(plan_dir: Path, slug: str) -> str:
    base = f"{today_stamp()}-{normalize_slug(slug)}"
    candidate = f"{base}.md"
    suffix = 2
    while (plan_dir / candidate).exists():
        candidate = f"{base}-{suffix}.md"
        suffix += 1
    return candidate


def refused_bootstrap_paths(target_dir: Path) -> list[str]:
    refused = []
    for child in sorted(target_dir.iterdir(), key=lambda item: item.name):
        if child.name in ALLOWED_BOOTSTRAP_PATHS:
            continue
        refused.append(child.name)
    return refused


def result_to_json(payload: dict[str, object]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True)

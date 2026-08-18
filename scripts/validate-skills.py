#!/usr/bin/env python3
"""Validate the skill set for npx skills / plugin discoverability.

Ensures every skill package is complete and that its SKILL.md frontmatter
and agents/openai.yaml parse as strict YAML — the same requirement the
skills.sh installer (`npx skills add`) and the Claude Code plugin rely on.

A description containing an unquoted ': ' (colon-space) is rejected by
skills.sh's YAML parser as a nested mapping in a compact mapping, which
silently drops that skill from the install (it does not error the whole
run). This script exits non-zero on any such problem so a broken skill can
never be pushed.

Run from anywhere:  python3 scripts/validate-skills.py
"""
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("error: PyYAML is required (pip install pyyaml)")
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_ROOT = os.path.join(ROOT, "skills")
errors = []


def read_text(path):
    """Read a file to a string, reporting failure as an error; None on failure."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except OSError as exc:
        errors.append(f"{path}: cannot read -> {exc}")
        return None


def parse_frontmatter(path):
    """Parse the --- delimited frontmatter of a SKILL.md; None on failure."""
    text = read_text(path)
    if text is None:
        return None
    match = re.match(r"\A---\r?\n(.*?)\r?\n---", text, re.S)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter (--- delimiters)")
        return None
    try:
        return yaml.safe_load(match.group(1)) or {}
    except Exception as exc:  # noqa: BLE001 - report any parse failure
        errors.append(f"{path}: frontmatter YAML parse error -> {str(exc).splitlines()[0]}")
        return None


def parse_yaml(path):
    """Parse a standalone YAML file; None on failure."""
    text = read_text(path)
    if text is None:
        return None
    try:
        return yaml.safe_load(text) or {}
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{path}: YAML parse error -> {str(exc).splitlines()[0]}")
        return None


def list_skill_dirs():
    """Return the two-level skill directories under skills/, reporting failures."""
    try:
        cats = sorted(os.listdir(SKILLS_ROOT))
    except OSError as exc:
        errors.append(f"{SKILLS_ROOT}: cannot list -> {exc}")
        return []
    result = []
    for cat in cats:
        cat_dir = os.path.join(SKILLS_ROOT, cat)
        if not os.path.isdir(cat_dir):
            continue
        try:
            names = sorted(os.listdir(cat_dir))
        except OSError as exc:
            errors.append(f"{cat_dir}: cannot list -> {exc}")
            continue
        for name in names:
            if os.path.isdir(os.path.join(cat_dir, name)):
                result.append(os.path.join(cat_dir, name))
    return result


def main():
    for skill_dir in list_skill_dirs():
        name = os.path.basename(skill_dir)
        cat = os.path.basename(os.path.dirname(skill_dir))
        skill_md = os.path.join(skill_dir, "SKILL.md")
        openai = os.path.join(skill_dir, "agents", "openai.yaml")
        docs = os.path.join(ROOT, "docs", cat, f"{name}.md")

        if not os.path.isfile(skill_md):
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        if not os.path.isfile(openai):
            errors.append(f"{skill_dir}: missing agents/openai.yaml")
        if not os.path.isfile(docs):
            errors.append(f"{skill_dir}: missing docs/{cat}/{name}.md")

        meta = parse_frontmatter(skill_md)
        if meta is not None:
            front_name = meta.get("name")
            if not isinstance(front_name, str) or not front_name:
                errors.append(f"{skill_md}: frontmatter 'name' missing or not a string")
            elif front_name != name:
                errors.append(
                    f"{skill_md}: frontmatter name '{front_name}' != directory name '{name}'"
                )
            desc = meta.get("description")
            if not isinstance(desc, str) or not desc.strip():
                errors.append(f"{skill_md}: frontmatter 'description' missing or empty")

        if os.path.isfile(openai):
            oa = parse_yaml(openai)
            if oa is not None:
                interface = oa.get("interface") or {}
                for field in ("display_name", "short_description", "default_prompt"):
                    value = interface.get(field)
                    if not isinstance(value, str) or not value:
                        errors.append(f"{openai}: interface.{field} missing or not a string")

    if errors:
        print(f"VALIDATION FAILED — {len(errors)} problem(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    skill_dirs = list_skill_dirs()
    print(
        f"OK — {len(skill_dirs)} skill package(s) complete; "
        "all SKILL.md frontmatter and agents/openai.yaml parse as strict YAML."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

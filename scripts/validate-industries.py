#!/usr/bin/env python3
"""Validates industries/*.md files for required frontmatter and sections."""
import sys
from pathlib import Path
import re

REQUIRED_FRONTMATTER = {"version", "last_updated", "source", "stale_after_days"}
REQUIRED_SECTIONS = [
    "## Sector Profile",
    "## Mobile-First Rules",
    "## Required Elements",
    "## Banned Patterns",
    "## Trust Signals",
    "## Conversion Path",
    "## Typical Page Structure",
    "## Quick Diagnosis",
    "## Disambiguation",
]

def validate_file(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")

    # Check frontmatter
    fm_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm_match:
        errors.append(f"{path.name}: missing YAML frontmatter")
        return errors

    fm_text = fm_match.group(1)
    for key in REQUIRED_FRONTMATTER:
        if f"{key}:" not in fm_text:
            errors.append(f"{path.name}: frontmatter missing '{key}'")

    # Check sections
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{path.name}: missing section '{section}'")

    # No placeholder content
    for placeholder in ["TBD", "TODO", "PLACEHOLDER", "fill in"]:
        if placeholder in text:
            errors.append(f"{path.name}: contains placeholder '{placeholder}'")

    return errors

def main():
    root = Path(__file__).parent.parent
    industries_dir = root / "industries"
    if not industries_dir.exists():
        print("No industry files found — create industries/*.md files first.")
        sys.exit(0)
    industry_files = sorted(industries_dir.glob("*.md"))
    industry_files = [f for f in industry_files if f.name != "_index.md"]

    if not industry_files:
        print("No industry files found — create industries/*.md files first.")
        sys.exit(0)

    all_errors = []
    for f in industry_files:
        all_errors.extend(validate_file(f))

    if all_errors:
        print(f"VALIDATION FAILED — {len(all_errors)} error(s):")
        for e in all_errors:
            print(f"  ✗ {e}")
        sys.exit(1)
    else:
        print(f"VALIDATION PASSED — {len(industry_files)} file(s) valid.")

if __name__ == "__main__":
    main()

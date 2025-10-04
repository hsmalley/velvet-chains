#!/usr/bin/env python3
"""⚔️ Lore Validator: Ensures `_LORE_/NN_name.md` fragments meet corsair standards.

Checks performed:
  * Filename pattern NN_*.md with zero-padded numeric prefix
  * Unique indices (no collisions)
  * YAML frontmatter (optional) keys limited to: title, order, tags, draft
  * Safe word mention "fiction" somewhere in body
  * Presence of a heading or frontmatter title
  * order must be integer if present
  * tags must be list of strings

Exit codes:
  0 success (no errors, maybe warnings)
  1 errors found

Captain Velvet decrees: Honor consent & structure! ⚔️
"""
from __future__ import annotations
import re
import sys
import yaml
from pathlib import Path

LORE_DIR = Path("_LORE_")
ALLOWED_KEYS = {"title", "order", "tags", "draft"}
FILE_PATTERN = re.compile(r"^(\d+)[-_].*\.(md|mdx)$", re.IGNORECASE)


def split_frontmatter(text: str):
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            fm_raw = parts[0][4:]  # strip leading ---\n
            body = parts[1]
            return fm_raw, body
    return None, text


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    if not LORE_DIR.exists():
        warnings.append("Lore directory `_LORE_` does not exist.")
    indices: dict[int, Path] = {}
    for path in sorted(list(LORE_DIR.glob("*.md")) + list(LORE_DIR.glob("*.mdx"))):
        m = FILE_PATTERN.match(path.name)
        if not m:
            errors.append(f"Invalid filename (pattern NN_name.md): {path.name}")
            continue
        idx = int(m.group(1))
        if idx in indices:
            errors.append(f"Duplicate index {idx:02d} between {indices[idx].name} and {path.name}")
        else:
            indices[idx] = path
        raw = path.read_text(encoding="utf-8")
        fm_raw, body = split_frontmatter(raw)
        meta = {}
        if fm_raw:
            try:
                meta_loaded = yaml.safe_load(fm_raw)
            except Exception as e:  # noqa: BLE001
                errors.append(f"YAML parse error in {path.name}: {e}")
                continue
            if meta_loaded is None:
                meta = {}
            elif isinstance(meta_loaded, dict):
                meta = meta_loaded
            else:
                errors.append(
                    f"Frontmatter must be a mapping (key: value) in {path.name}; got {type(meta_loaded).__name__}. Example:\n"
                    "---\n" "title: Example Title\n" "order: 10\n" "tags: [setting]\n" "draft: false\n" "---"
                )
                continue
            unknown = set(meta.keys()) - ALLOWED_KEYS
            if unknown:
                errors.append(f"Unknown frontmatter keys in {path.name}: {', '.join(sorted(unknown))}")
            if 'order' in meta and not isinstance(meta['order'], int):
                errors.append(f"order must be integer in {path.name}")
            if 'tags' in meta:
                if not isinstance(meta['tags'], list) or not all(isinstance(t, str) for t in meta['tags']):
                    errors.append(f"tags must be list of strings in {path.name}")
            if 'draft' in meta and not isinstance(meta['draft'], bool):
                errors.append(f"draft must be boolean in {path.name}")
        else:
            warnings.append(f"Missing frontmatter in {path.name} (legacy mode) – future versions will require it.")
        # Title check
        has_heading = any(line.startswith('#') for line in body.splitlines())
        if not has_heading and 'title' not in meta:
            warnings.append(f"No heading or title in {path.name}")
        # Safe word check
        if 'fiction' not in body.lower():
            warnings.append(f"Safe word 'fiction' not referenced in body of {path.name}")
    # Report
    if warnings:
        print("⚠️ Warnings:")
        for w in warnings:
            print("  -", w)
    if errors:
        print("❌ Errors:")
        for e in errors:
            print("  -", e)
        return 1
    print("✨ Lore validation passed with theatrical excellence!")
    return 0


if __name__ == '__main__':  # Quartermaster Siren audits the lore manifests
    raise SystemExit(main())

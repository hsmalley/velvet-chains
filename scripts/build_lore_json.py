#!/usr/bin/env python3
"""Emit static lore.json from `_LORE_` for future client features (pure build artifact).

Captures: index, filename, title, tags, draft, order, first_200_chars excerpt.
Skips drafts. Frontmatter required (warn if missing)."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

LORE_DIR = Path("_LORE_")
OUT = Path("public/lore.json")
FILE_PATTERN = re.compile(r"^(\d+)[-_].*\.(md|mdx)$", re.I)


def split_frontmatter(text: str):
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            return parts[0][4:], parts[1]
    return None, text


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = []
    if not LORE_DIR.exists():
        print("No lore directory; emitting empty lore.json")
        OUT.write_text("[]", encoding="utf-8")
        return 0
    for path in sorted(LORE_DIR.iterdir()):
        if not path.is_file():
            continue
        if not FILE_PATTERN.match(path.name):
            continue
        raw = path.read_text(encoding="utf-8")
        fm_raw, body = split_frontmatter(raw)
        meta = {}
        if fm_raw:
            try:
                meta = yaml.safe_load(fm_raw) or {}
            except Exception:
                continue
        else:
            # legacy; fabricate minimal meta
            pass
        if meta.get("draft") is True:
            continue
        title = meta.get("title")
        if not title:
            for line in body.splitlines():
                if line.startswith("#"):
                    title = line.lstrip("#").strip()
                    break
        if not title:
            title = path.stem
        excerpt = body.strip().replace("\r", "")[:200]
        payload.append(
            {
                "filename": path.name,
                "index": int(FILE_PATTERN.match(path.name).group(1)),
                "title": title,
                "tags": meta.get("tags") or [],
                "order": meta.get("order"),
                "excerpt": excerpt,
            }
        )
    # sort final
    payload.sort(
        key=lambda x: (
            x.get("order") is not None,
            x.get("order") if x.get("order") is not None else 10**6,
            x["index"],
        )
    )
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Emitted {len(payload)} fragments -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

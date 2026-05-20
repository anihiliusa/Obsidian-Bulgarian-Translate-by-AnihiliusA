#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate an Obsidian translation file for basic formatting and placeholder safety.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

BLOCK_RE = re.compile(
    r"(?ms)^\[(?P<key>[^\]]+)\]\n"
    r"original=(?P<original>.*?)\n"
    r"translation=(?P<translation>.*?)(?=\n\n\[|\Z)"
)
PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", default="translations/bg.txt")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"ERROR: missing file: {path}")
        return 2

    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n")
    blocks = list(BLOCK_RE.finditer(text))
    if not blocks:
        print("ERROR: no valid blocks found.")
        return 2

    errors = []
    seen = set()
    translated = 0

    for m in blocks:
        key = m.group("key")
        original = m.group("original")
        translation = m.group("translation").rstrip("\n")

        if key in seen:
            errors.append(f"Duplicate key: {key}")
        seen.add(key)

        if translation.strip():
            translated += 1

        op = set(PLACEHOLDER_RE.findall(original))
        tp = set(PLACEHOLDER_RE.findall(translation))
        if translation.strip() and op != tp:
            errors.append(f"Placeholder mismatch [{key}]: original={sorted(op)} translation={sorted(tp)}")

    print(f"Blocks: {len(blocks)}")
    print(f"Translated blocks: {translated}")
    print(f"Empty translations: {len(blocks) - translated}")

    if errors:
        print("\nERRORS:")
        for e in errors[:200]:
            print(f"- {e}")
        if len(errors) > 200:
            print(f"... and {len(errors)-200} more")
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

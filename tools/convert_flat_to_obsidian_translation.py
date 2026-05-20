#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert a flat Obsidian Bulgarian language pack into the official
obsidianmd/obsidian-translations block format.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path
from typing import Dict, List, Tuple

DEFAULT_TEMPLATE_URL = (
    "https://raw.githubusercontent.com/obsidianmd/obsidian-translations/"
    "master/translations/bg.txt"
)

BLOCK_RE = re.compile(
    r"(?ms)^\[(?P<key>[^\]]+)\]\n"
    r"original=(?P<original>.*?)\n"
    r"translation=(?P<translation>.*?)(?=\n\n\[|\Z)"
)

PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def fetch_template(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def parse_blocks(template: str) -> List[Dict[str, str]]:
    blocks = []
    for m in BLOCK_RE.finditer(template):
        blocks.append({"key": m.group("key"), "original": m.group("original"), "translation": m.group("translation").rstrip("\n")})
    if not blocks:
        raise ValueError("No translation blocks found in template.")
    return blocks


def build_translation_map(flat_text: str, mapping_text: str) -> Tuple[Dict[str, str], List[str]]:
    translations = flat_text.splitlines()
    keys = [line.strip() for line in mapping_text.splitlines() if line.strip()]
    warnings: List[str] = []
    if len(translations) != len(keys):
        warnings.append(
            f"Line count mismatch: {len(translations)} translation lines vs {len(keys)} mapping keys. "
            "The converter will use the shortest length and leave the rest unchanged."
        )
    return {key: value.rstrip("\n") for key, value in zip(keys, translations)}, warnings


def placeholder_set(text: str) -> set[str]:
    return set(PLACEHOLDER_RE.findall(text or ""))


def render_blocks(blocks: List[Dict[str, str]], translation_map: Dict[str, str]) -> Tuple[str, List[str]]:
    out: List[str] = []
    warnings: List[str] = []
    used = set()
    for block in blocks:
        key = block["key"]
        original = block["original"]
        translation = block["translation"]
        if key in translation_map:
            new_translation = translation_map[key]
            used.add(key)
            if placeholder_set(original) != placeholder_set(new_translation):
                warnings.append(
                    f"Placeholder mismatch for [{key}]: "
                    f"original={sorted(placeholder_set(original))} translation={sorted(placeholder_set(new_translation))}"
                )
            translation = new_translation
        out.append(f"[{key}]\noriginal={original}\ntranslation={translation}")
    unused = sorted(set(translation_map) - used)
    if unused:
        warnings.append(f"{len(unused)} mapped keys were not found in the current upstream template. First 20: " + ", ".join(unused[:20]))
    return "\n\n".join(out).rstrip() + "\n", warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--flat", default="legacy/bg.raw.txt")
    parser.add_argument("--mapping", default="legacy/mapping.txt")
    parser.add_argument("--template", default="")
    parser.add_argument("--template-url", default=DEFAULT_TEMPLATE_URL)
    parser.add_argument("--output", default="translations/bg.txt")
    parser.add_argument("--warnings", default="translation_warnings.txt")
    args = parser.parse_args()

    flat_path = Path(args.flat)
    mapping_path = Path(args.mapping)
    output_path = Path(args.output)
    warnings_path = Path(args.warnings)

    if not flat_path.exists():
        print(f"ERROR: flat file not found: {flat_path}", file=sys.stderr)
        return 2
    if not mapping_path.exists():
        print(f"ERROR: mapping file not found: {mapping_path}", file=sys.stderr)
        return 2

    flat_text = read_text(flat_path)
    mapping_text = read_text(mapping_path)
    template_text = read_text(Path(args.template)) if args.template else fetch_template(args.template_url)

    blocks = parse_blocks(template_text)
    translation_map, warnings = build_translation_map(flat_text, mapping_text)
    rendered, render_warnings = render_blocks(blocks, translation_map)
    warnings.extend(render_warnings)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8", newline="\n")

    if warnings:
        warnings_path.write_text("\n".join(warnings) + "\n", encoding="utf-8")
        print(f"Generated {output_path} with {len(warnings)} warning(s). See {warnings_path}")
    else:
        if warnings_path.exists():
            warnings_path.unlink()
        print(f"Generated {output_path} with no warnings.")
    print(f"Blocks in output: {len(blocks)}")
    print(f"Mapped translations: {len(translation_map)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Notice

This repository intentionally excludes `obsidian-*.asar` files.

Reason:
- Obsidian is a proprietary application.
- A public translation repository should not redistribute Obsidian application packages.
- Official UI translation contributions should be submitted to:
  `obsidianmd/obsidian-translations`

Included files:
- `legacy/bg.raw.txt` — Bulgarian strings extracted from the local language pack.
- `legacy/mapping.txt` — key order used by the flat language pack.
- `tools/convert_flat_to_obsidian_translation.py` — converts the flat file to official Obsidian translation format.
- `tools/validate_translation.py` — basic format and placeholder validation.

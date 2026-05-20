# Obsidian Bulgarian Translate by AnihiliusA

Bulgarian UI translation toolkit for Obsidian.

This repository prepares a Bulgarian language update that can be submitted to the official
Obsidian translation repository: `obsidianmd/obsidian-translations`.

## Important

This repository does **not** include Obsidian `.asar` files.

Obsidian is a proprietary app, so public contribution should be done through the official
translation text file, not by redistributing patched application packages.

## Included

- `legacy/bg.raw.txt` — flat Bulgarian language strings.
- `legacy/mapping.txt` — Obsidian translation keys in the same order as the flat file.
- `tools/convert_flat_to_obsidian_translation.py` — converts the flat file into official format.
- `tools/validate_translation.py` — validates blocks and placeholders.
- `tools/generate_bg.ps1` — Windows helper for generating `translations/bg.txt`.

## Generate official `translations/bg.txt`

Windows PowerShell:

```powershell
.\tools\generate_bg.ps1
```

Cross-platform:

```bash
python tools/convert_flat_to_obsidian_translation.py \
  --flat legacy/bg.raw.txt \
  --mapping legacy/mapping.txt \
  --output translations/bg.txt

python tools/validate_translation.py translations/bg.txt
```

## Test in Obsidian

1. Open Obsidian.
2. Open Developer Console with `Ctrl+Shift+I`.
3. Run:

```js
selectLanguageFileLocation()
```

4. Select the generated file:

```text
translations/bg.txt
```

To revert:

```js
localStorage.removeItem('language')
```

## Submit to official Obsidian translations

The official target repository is:

```text
obsidianmd/obsidian-translations
```

Bulgarian file:

```text
translations/bg.txt
```

Suggested PR title:

```text
Update Bulgarian translation
```

Suggested PR body:

```text
Bulgarian endonym: български език

This PR updates the Bulgarian UI translation for Obsidian.
Translation prepared by AnihiliusA.
```

## Author

Prepared by AnihiliusA.

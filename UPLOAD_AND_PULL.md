# Upload ZIP package and pull locally

The repository is public and can be cloned with:

```bash
git clone https://github.com/anihiliusa/Obsidian-Bulgarian-Translate-by-AnihiliusA.git
cd Obsidian-Bulgarian-Translate-by-AnihiliusA
```

If already cloned:

```bash
git pull origin main
```

## Add ZIP package manually

Do not upload Obsidian .asar packages.

Safe archive to upload:

```text
Obsidian-Bulgarian-Translate-by-AnihiliusA.zip
```

Recommended location:

```text
dist/Obsidian-Bulgarian-Translate-by-AnihiliusA.zip
```

Local commands:

```bash
mkdir -p dist
cp /path/to/Obsidian-Bulgarian-Translate-by-AnihiliusA.zip dist/
git add dist/Obsidian-Bulgarian-Translate-by-AnihiliusA.zip
git commit -m "Add packaged translation toolkit archive"
git push
```

## Add source files from ZIP

Expected files:

```text
legacy/bg.raw.txt
legacy/mapping.txt
```

Commands:

```bash
mkdir -p legacy
cp /path/to/bg.raw.txt legacy/bg.raw.txt
cp /path/to/mapping.txt legacy/mapping.txt
git add legacy/bg.raw.txt legacy/mapping.txt
git commit -m "Add Bulgarian translation source files"
git push
```

## Generate official Obsidian translation file

```bash
python tools/convert_flat_to_obsidian_translation.py --flat legacy/bg.raw.txt --mapping legacy/mapping.txt --output translations/bg.txt
python tools/validate_translation.py translations/bg.txt
git add translations/bg.txt translation_warnings.txt
git commit -m "Generate Bulgarian Obsidian translation"
git push
```

## PR to Obsidian

A pull request to Obsidian must be opened from a fork of:

```text
obsidianmd/obsidian-translations
```

This repository is a toolkit repository, not a fork of the official translations repository.

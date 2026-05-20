# Manual PR commands for Obsidian

Use this after cloning this toolkit repository locally.

## 1. Prepare the toolkit

```bash
git clone https://github.com/anihiliusa/Obsidian-Bulgarian-Translate-by-AnihiliusA.git
cd Obsidian-Bulgarian-Translate-by-AnihiliusA
```

Add the missing source files from the ZIP if they are not already present:

```text
legacy/bg.raw.txt
legacy/mapping.txt
```

Generate the official Obsidian translation file:

```bash
python tools/convert_flat_to_obsidian_translation.py --flat legacy/bg.raw.txt --mapping legacy/mapping.txt --output translations/bg.txt
python tools/validate_translation.py translations/bg.txt
```

## 2. Fork official Obsidian translations

```bash
gh repo fork obsidianmd/obsidian-translations --clone --remote=true
cd obsidian-translations
```

## 3. Copy generated bg.txt

From inside the cloned official fork:

```bash
cp ../Obsidian-Bulgarian-Translate-by-AnihiliusA/translations/bg.txt translations/bg.txt
```

On Windows PowerShell:

```powershell
Copy-Item ..\Obsidian-Bulgarian-Translate-by-AnihiliusA\translations\bg.txt .\translations\bg.txt -Force
```

## 4. Commit and push

```bash
git switch -c update-bulgarian-translation-anihiliusa
git add translations/bg.txt
git commit -m "Update Bulgarian translation"
git push -u origin update-bulgarian-translation-anihiliusa
```

## 5. Open PR

```bash
gh pr create --repo obsidianmd/obsidian-translations --title "Update Bulgarian translation" --body "Bulgarian endonym: Bulgarian. This PR updates the Bulgarian UI translation for Obsidian. Translation prepared by AnihiliusA."
```

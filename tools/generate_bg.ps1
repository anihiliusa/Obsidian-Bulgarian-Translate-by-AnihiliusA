# Generate official Obsidian Bulgarian translation file from the legacy flat language pack.
# Run from the repository root.

$ErrorActionPreference = "Stop"

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
  Write-Host "Python is not installed or not in PATH." -ForegroundColor Red
  exit 1
}

python tools/convert_flat_to_obsidian_translation.py `
  --flat legacy/bg.raw.txt `
  --mapping legacy/mapping.txt `
  --output translations/bg.txt

python tools/validate_translation.py translations/bg.txt

Write-Host ""
Write-Host "Generated: translations/bg.txt" -ForegroundColor Green
Write-Host ""
Write-Host "To test in Obsidian:"
Write-Host "1. Open Obsidian"
Write-Host "2. Open Developer Console: Ctrl+Shift+I"
Write-Host "3. Run: selectLanguageFileLocation()"
Write-Host "4. Choose translations/bg.txt"
Write-Host ""
Write-Host "To revert:"
Write-Host "localStorage.removeItem('language')"

# legacy

This folder is reserved for the two large source files used to generate the official Obsidian Bulgarian translation file.

Expected files:

- bg.raw.txt
- mapping.txt

They were intentionally not generated from Obsidian proprietary packages inside this repository. Add only the text translation sources, not any .asar file.

After adding both files, run:

python tools/convert_flat_to_obsidian_translation.py --flat legacy/bg.raw.txt --mapping legacy/mapping.txt --output translations/bg.txt
python tools/validate_translation.py translations/bg.txt

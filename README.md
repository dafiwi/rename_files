# Rename Files

This is a simple Python script which renames all files in a directory you specify according to the predefined schema. You have to make manual changes to the schema in the rename_files.py file if necessary. The script was tested successfully with Linux.

## ⚠️ Important Disclaimer

**USE AT YOUR OWN RISK!**

This Python script is provided "as is" without any warranties or guarantees.

- The author is **not responsible** for any data loss, file corruption, or other damages caused by using this script.
- **Always create a full backup** of your data before running the script.
- Test it on a copy of your files first.
- The script may overwrite existing files if not used carefully.
- The files will be renamed in the order in which they are sorted.

By using this script, you agree to assume all risks and indemnify the author from any claims.

## Schema

Example: Files are named like this: 1000000123.jpg, 1000000124.jpg, 1000000125.jpg, and so on
(any other filenames are fine)

You want to name the files like this: your filename-2026-1.jpg, your filename-2026-2.jpg,       your filename-2026-3.jpg, and so on

You can achieve this by running the script.

Adjust schema in rename_files.py first before you execute the script (as described below) if you want to make changes (see schema comment).

## Tech Stack
- Python 3.10+
- Libraries: os, pathlib, re

## Installation
### Requirements
- Python 3.10 or higher.

git clone https://github.com/dafiwi/rename_files.git

cd path/to/script-directory

chmod +x rename_files.py
./rename_files.py

OR

python3 rename_files.py

OR

python rename_files.py

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE). Copyright (c) dafiwi/2026 (https://github.com/dafiwi/rename_files).

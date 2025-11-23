# Digital Automation

A collection of small Python automation scripts to simplify repetitive tasks. Includes utilities for **bulk renaming**, **folder backups**, and other file/folder operations. Use these as templates to build more complex pipelines.

---

## Features

- **Bulk Rename**: Rename multiple files in a folder with a prefix and sequential numbers.  
- **Folder Backup**: Compress any folder into a timestamped ZIP archive.  
- Lightweight, reusable scripts with minimal dependencies.  
- Safe “dry-run” mode for testing file operations.  

---

## Usage


**1. Bulk Rename**

Rename all files in a folder sequentially with a prefix.

```bash
python bulk_rename.py /path/to/folder --prefix img_ --start 1
```
**Arguments:**

- folder: Path to the folder containing files.

- --prefix: Optional prefix for renamed files (default: file_).

- --start: Starting number for sequence (default: 1).

- --dry: Show what would be renamed without actually renaming.

**Example:**
```bash
python bulk_rename.py ./photos --prefix vacation_ --start 1 --dry
```
**2. Folder Backup**

Create a ZIP archive backup of a folder with a timestamped name.
```bash
python backup.py /path/to/source /path/to/destination
```
**Arguments:**

- src: Path to the folder to back up.

- dest: Destination folder where the ZIP will be stored.

**Example:**
```bash
python backup.py ./project ./backups
# Creates backups/project_backup_20251123_170512.zip
```
**Notes**

- All scripts use Python standard library only.

- Dry-run mode is available for file operations to avoid accidental changes.

- Scripts are meant as educational templates—feel free to extend for more complex automation.
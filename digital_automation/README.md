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

### 1. Bulk Rename (YAML Config)

**Config file example: `config.yaml`**

```yaml
source: "/home/noh/Downloads/organized/images"
destination: "/home/noh/Downloads/renamed_images"
prefix: "renamed_"
start: 1
dry: false   # set to true for dry-run
```
**Run the script:**
```bash
python bulk_rename.py --config config.yaml
```
**Behavior:**

- Renames all files in the source folder.

- Moves files to the destination folder if specified.

- Prefix and numbering start can be configured.

- Dry-run mode (dry: true) shows what would happen without actually renaming or moving.

**Example:**
```bash
python bulk_rename.py --config config.yaml
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
# file_organizer/organizer.py 

#!/usr/bin/env python3
"""
Simple File Organizer
Usage:
    python organizer.py --config config.yaml --dry-run
"""
import argparse
import os
import shutil
import yaml
from pathlib import Path

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def ensure_dir(p):
    os.makedirs(p, exist_ok=True)

def unique_target(path):
    """
    If file exists, returns a unique path by adding suffix like file (1).ext
    """
    p = Path(path)
    if not p.exists():
        return p
    parent = p.parent
    stem = p.stem
    suffix = p.suffix
    i = 1
    while True:
        candidate = parent / f"{stem} ({i}){suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def organize(source, dest, categories, default, dup_policy="rename", dry_run=False):
    source_path = Path(source)
    if not source_path.exists() or not source_path.is_dir():
        raise ValueError("Source must be an existing directory.")
    ensure_dir(dest)

    moved = []
    for item in source_path.iterdir():
        if item.is_dir():
            continue
        ext = item.suffix.lower()
        found = None
        for cat, exts in categories.items():
            if ext in exts:
                found = cat
                break
        target_folder = Path(dest) / (found if found else default)
        ensure_dir(target_folder)
        target_file = target_folder / item.name

        if target_file.exists():
            if dup_policy == "skip":
                print(f"[skip] {item} -> already exists at target")
                continue
            elif dup_policy == "overwrite":
                if not dry_run:
                    target_file.unlink()
            elif dup_policy == "rename":
                target_file = unique_target(target_file)

        print(f"{'[DRY]' if dry_run else ''} Moving {item} -> {target_file}")
        if not dry_run:
            shutil.move(str(item), str(target_file))
        moved.append((str(item), str(target_file)))
    return moved

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_config(args.config)
    organize(cfg["source"], cfg["destination"], cfg["categories"], cfg.get("default","others"),
             dup_policy=cfg.get("handle_duplicates","rename"), dry_run=args.dry_run)

if __name__ == "__main__":
    main()

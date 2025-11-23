#!/usr/bin/env python3
"""
Bulk rename files using a YAML config.

Usage:
python bulk_rename.py --config config.yaml
"""
import argparse
from pathlib import Path
import shutil
import yaml

def bulk_rename(source, dest=None, prefix="file_", start=1, dry=False):
    source = Path(source)
    files = [x for x in source.iterdir() if x.is_file()]
    if dest:
        dest = Path(dest)
        dest.mkdir(parents=True, exist_ok=True)

    for i, f in enumerate(sorted(files), start=start):
        newname = f"{prefix}{i}{f.suffix}"
        newpath = (dest / newname) if dest else (source / newname)
        print(f"{'[DRY]' if dry else ''} {f} -> {newpath}")
        if not dry:
            if dest:
                shutil.move(str(f), str(newpath))
            else:
                f.rename(newpath)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    bulk_rename(
        source=cfg["source"],
        dest=cfg.get("destination"),
        prefix=cfg.get("prefix", "file_"),
        start=cfg.get("start", 1),
        dry=cfg.get("dry", False)
    )

if __name__ == "__main__":
    main()

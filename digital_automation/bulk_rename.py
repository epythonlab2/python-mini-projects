#!/usr/bin/env python3
"""
Simple bulk renamer:
python bulk_rename.py /path/to/folder --prefix img_ --start 1
"""
import argparse
from pathlib import Path

def bulk_rename(folder, prefix="file_", start=1, dry=False):
    p = Path(folder)
    files = [x for x in p.iterdir() if x.is_file()]
    for i, f in enumerate(sorted(files), start=start):
        newname = f"{prefix}{i}{f.suffix}"
        newpath = p / newname
        print(f"{'[DRY]' if dry else ''} {f.name} -> {newname}")
        if not dry:
            f.rename(newpath)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--prefix", default="file_")
    parser.add_argument("--start", default=1, type=int)
    parser.add_argument("--dry", action="store_true")
    args = parser.parse_args()
    bulk_rename(args.folder, args.prefix, args.start, args.dry)

if __name__ == "__main__":
    main()

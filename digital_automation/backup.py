#!/usr/bin/env python3
"""
Simple folder backup: compresses a folder to a zip named with timestamp.
"""
import shutil
from datetime import datetime
from pathlib import Path
import argparse

def backup_folder(src, dest_dir):
    src = Path(src)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = dest_dir / f"{src.name}_backup_{timestamp}"
    shutil.make_archive(str(archive_name), 'zip', root_dir=str(src))
    print("Backup created:", str(archive_name) + ".zip")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src")
    parser.add_argument("dest")
    args = parser.parse_args()
    backup_folder(args.src, args.dest)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from cryptography.fernet import Fernet
from pathlib import Path
import os

KEY_FILE = Path(__file__).parent / "data" / "key.key"
KEY_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_key():
    """Load the encryption key or generate a new one if it doesn't exist."""
    if KEY_FILE.exists() and KEY_FILE.stat().st_size > 0:
        return KEY_FILE.read_bytes()

    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)
    os.chmod(KEY_FILE, 0o600)  # restrict file permissions
    print("Generated new encryption key.")
    return key

def show_key():
    """Display the key (for educational purposes)."""
    if KEY_FILE.exists():
        print(KEY_FILE.read_text())
    else:
        print("No key found. Run load_key() to generate one.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("generate")
    sub.add_parser("show")
    args = parser.parse_args()

    if args.cmd == "generate":
        load_key()
    elif args.cmd == "show":
        show_key()
    else:
        parser.print_help()

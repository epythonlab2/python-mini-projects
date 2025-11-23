#!/usr/bin/env python3
import json
from pathlib import Path
from cryptography.fernet import Fernet
import argparse
from key_manager import load_key

DATA_FILE = Path(__file__).parent / "data" / "vault.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_data():
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return {}
    try:
        return json.loads(DATA_FILE.read_text())
    except json.JSONDecodeError:
        print("Warning: vault.json corrupted. Resetting file.")
        return {}

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))

def add(service, username, password):
    key = load_key()
    cipher = Fernet(key)
    data = load_data()

    if service in data:
        confirm = input(f"{service} already exists. Overwrite? (y/n): ")
        if confirm.lower() != "y":
            print("Cancelled.")
            return

    data[service] = {
        "username": username,
        "password": cipher.encrypt(password.encode()).decode()
    }
    save_data(data)
    print("Saved:", service)

def get(service):
    key = load_key()
    cipher = Fernet(key)
    data = load_data()
    entry = data.get(service)
    if not entry:
        print("Service not found")
        return
    print("Username:", entry["username"])
    print("Password:", cipher.decrypt(entry["password"].encode()).decode())

def list_services():
    data = load_data()
    if not data:
        print("No services stored.")
        return
    for k, v in sorted(data.items()):
        print(k, "-", v["username"])

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    a = sub.add_parser("add")
    a.add_argument("service")
    a.add_argument("username")
    a.add_argument("password")
    g = sub.add_parser("get")
    g.add_argument("service")
    l = sub.add_parser("list")
    args = parser.parse_args()

    if args.cmd == "add":
        add(args.service, args.username, args.password)
    elif args.cmd == "get":
        get(args.service)
    elif args.cmd == "list":
        list_services()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

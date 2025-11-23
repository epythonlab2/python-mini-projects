#!/usr/bin/env python3
"""
Habit tracker (JSON backend).

Usage:
    python habits.py add HabitName
    python habits.py done HabitName
    python habits.py streak HabitName
    python habits.py list
"""
import json
from pathlib import Path
from datetime import date, timedelta
import argparse

DATA = Path(__file__).parent / "data" / "habits.json"
DATA.parent.mkdir(parents=True, exist_ok=True)

def load():
    if not DATA.exists() or DATA.stat().st_size == 0:  # check empty file
        return {}
    try:
        return json.loads(DATA.read_text())
    except json.JSONDecodeError:
        print("Warning: habits.json was corrupted. Resetting file.")
        return {}


def save(data):
    DATA.write_text(json.dumps(data, indent=2))

def add_habit(name):
    data = load()
    if name in data:
        print("Habit exists.")
        return
    data[name] = []
    save(data)
    print("Added habit:", name)

def mark_done(name):
    data = load()
    today = date.today().isoformat()
    if name not in data:
        print("Habit not found.")
        return
    if today not in data[name]:
        data[name].append(today)
        save(data)
        print("Marked done for", today)
    else:
        print("Already marked today.")

def streak(name):
    data = load()
    if name not in data or not data[name]:
        print("No records.")
        return
    dates = sorted(data[name], reverse=True)
    streak = 0
    d = date.today()
    for i in range(0, 365):
        string = (d - timedelta(days=i)).isoformat()
        if string in data[name]:
            streak += 1
        else:
            break
    print(f"Current streak for {name}: {streak}")

def list_habits():
    data = load()
    for k, v in data.items():
        print(k, "—", len(v), "records")

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("list")
    a = sub.add_parser("add"); a.add_argument("name")
    d = sub.add_parser("done"); d.add_argument("name")
    s = sub.add_parser("streak"); s.add_argument("name")
    args = parser.parse_args()
    if args.cmd == "list":
        list_habits()
    elif args.cmd == "add":
        add_habit(args.name)
    elif args.cmd == "done":
        mark_done(args.name)
    elif args.cmd == "streak":
        streak(args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

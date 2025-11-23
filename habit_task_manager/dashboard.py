#!/usr/bin/env python3
from pathlib import Path
import json
from datetime import date, timedelta

DATA = Path(__file__).parent / "data" / "habits.json"

def show_last_days(habit, days=14):
    records = set(habit[1])  # habit is a tuple (name, list)
    today = date.today()
    out = []
    for i in range(days-1, -1, -1):
        d = (today - timedelta(days=i)).isoformat()
        out.append("✔" if d in records else "·")
    print(habit[0], "|", " ".join(out))

if __name__ == "__main__":
    if not DATA.exists():
        print("No data.")
        exit()
    data = json.loads(DATA.read_text())
    from sys import argv

    if len(argv) == 1:  # no habit specified
        for habit in data.items():
            show_last_days(habit)
    else:
        habit_name = argv[1]
        if habit_name in data:
            show_last_days((habit_name, data[habit_name]))
        else:
            print("Habit not found.")

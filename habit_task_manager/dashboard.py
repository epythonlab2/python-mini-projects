#!/usr/bin/env python3
from pathlib import Path
import json
from datetime import date, timedelta

DATA = Path(__file__).parent / "data" / "habits.json"

def show_last_days(habit, days=14):
    if not DATA.exists():
        print("No data.")
        return
    data = json.loads(DATA.read_text())
    if habit not in data:
        print("Habit not found.")
        return
    records = set(data[habit])
    today = date.today()
    out = []
    for i in range(days-1, -1, -1):
        d = (today - timedelta(days=i)).isoformat()
        out.append("✔" if d in records else "·")
    print(habit, "|", " ".join(out))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python dashboard.py HabitName")
    else:
        show_last_days(sys.argv[1])

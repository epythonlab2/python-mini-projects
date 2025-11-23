#!/usr/bin/env python3
"""
Minimal CSV-backed expense tracker.

Usage examples:
    python expenses.py add 23.5 Food "Lunch at cafe"
    python expenses.py summary monthly
"""
import argparse
import csv
from datetime import datetime, date
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
FILE = DATA_DIR / "expenses.csv"

HEADERS = ["date", "amount", "category", "note"]

def ensure_file():
    # Create or fix a missing/corrupted header
    need_header = False
    
    if not FILE.exists():
        need_header = True
    else:
        # Check if first row has correct headers
        with open(FILE, "r") as f:
            first_line = f.readline().strip()
            if first_line.replace(" ", "") != ",".join(HEADERS):
                need_header = True

    if need_header:
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)

def add_expense(amount, category, note=""):
    ensure_file()
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date.today().isoformat(), float(amount), category, note])
    print("Added:", amount, category, note)

def summary(period="monthly"):
    ensure_file()
    df = pd.read_csv(FILE, parse_dates=["date"])
    if df.empty:
        print("No expenses recorded.")
        return
    if period == "monthly":
        df["month"] = df["date"].dt.to_period("M")
        agg = df.groupby("month")["amount"].sum().sort_index()
    elif period == "weekly":
        df["week"] = df["date"].dt.to_period("W")
        agg = df.groupby("week")["amount"].sum().sort_index()
    else:
        agg = df.groupby("category")["amount"].sum()
    print(agg)

def top_categories(n=3):
    ensure_file()
    df = pd.read_csv(FILE)
    print(df.groupby("category")["amount"].sum().nlargest(int(n)))

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd")
    a = sub.add_parser("add")
    a.add_argument("amount")
    a.add_argument("category")
    a.add_argument("note", nargs="?", default="")

    s = sub.add_parser("summary")
    s.add_argument("period", nargs="?", default="monthly")
    t = sub.add_parser("top")
    t.add_argument("n", nargs="?", default=3)

    args = parser.parse_args()
    if args.cmd == "add":
        add_expense(args.amount, args.category, args.note)
    elif args.cmd == "summary":
        summary(args.period)
    elif args.cmd == "top":
        top_categories(args.n)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Expense Tracker - expense_tracker/

A lightweight CLI tool for recording expenses, summarizing spending, and exporting your data. All entries are stored in a simple CSV file, and the script automatically repairs missing or corrupted headers.

## Features
- Add expenses from the command line
- Summaries by month, week, or category
- View top spending categories
- CSV-backed storage with automatic header fixing
- Minimal dependencies

## Setup
Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# or
.venv\\Scripts\\activate         # Windows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Add an expense:
```bash
python expenses.py add 23.5 Food "Lunch at cafe"
```

Monthly or weekly summaries:
```bash
python expenses.py summary monthly
python expenses.py summary weekly
```

Summary by category:
```bash
python expenses.py summary category
```

Top spending categories:
```bash
python expenses.py top 3
```

## Storage
All records are saved to:
```
data/expenses.csv
```
The file is auto-created and repaired if headers are missing.

## Notes
If you encounter an error about missing columns, delete `data/expenses.csv` and add a new expense to recreate proper headers.

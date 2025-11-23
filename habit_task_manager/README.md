# Habit & Task Manager

A simple terminal-based habit tracker to help you build consistent habits. Store completion dates in `habits.json`, mark habits done, track streaks, and visualize your progress.

Includes a small `dashboard.py` script that prints a calendar-style view of the last 14 days.

---

## Features

* Add new habits from the terminal
* Mark habits as done for today
* Track current streaks for each habit
* List all habits with completion count
* Dashboard for a quick 14-day overview
* JSON-based storage (no database required)

---

## Setup


**Data File Location**:
    The data file will be automatically created at:
    ```
    data/habits.json
    ```

---

## Usage

### Add a new habit
```bash
python habits.py add "Exercise"
python habits.py add "Read"

### Mark a habit as done for today
```bash
python habits.py done "Exercise"
python habits.py done "Read"

### Check current streak of a habit
```bash
python habits.py streak "Exercise"
python habits.py streak "Read"

### List all habits
```bash
python habits.py list

### Dashboard (Visual View)
```bash
python dashboard.py

Displays a calendar-like view of your habits for the last 14 days, showing which days were completed.

### Example Workflow
```bash
python habits.py add "Exercise"
python habits.py add "Read"
python habits.py done "Exercise"
python habits.py done "Read"
python habits.py streak "Exercise"
python habits.py list
python dashboard.py

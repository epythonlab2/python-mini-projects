# Python Mini Projects (Practical, Everyday Automations)

A collection of **5 small Python projects** designed to solve common everyday problems while teaching practical Python automation skills. Each project is lightweight, beginner-friendly, and can be extended for more advanced workflows.

---

## Projects Included

| # | Project | Description |
|---|---------|-------------|
| 1 | **File Organizer** | Organizes files into category folders by extension. Features YAML config, dry-run, duplicate handling, and console logging. |
| 2 | **Expense Tracker** | CLI tool to track expenses in CSV files, summarize spending by period/category, and show top categories. |
| 3 | **Habit & Task Manager** | Terminal-based habit tracker using JSON. Add/list habits, mark completion, view streaks, and a 14-day dashboard. |
| 4 | **Local Password Manager** | Educational local password vault using `cryptography.Fernet`. Store, encrypt, and retrieve credentials safely. |
| 5 | **Digital Automation** | Collection of small scripts: bulk rename, folder backup, and other file/folder utilities. YAML-config driven for convenience. |

---

## Getting Started

1. **Clone the repository**

```bash
git clone https://github.com/epythonlab2/python-mini-projects.git
cd python-mini-projects
```

2. **Create a virtual environment (recommended for each subproject)**
```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# or
.venv\Scripts\activate           # Windows
```
3. **Install dependencies (per subproject)**

Each subfolder contains a requirements.txt if needed. Example:
```bash
cd file_organizer
pip install -r requirements.txt
```

- Most scripts use the Python standard library only.

### Usage

**Each subfolder has its own README.md with:**

- Setup instructions

- Example commands

- Configuration details

**Subfolders:**
```bash

file_organizer/
expense_tracker/
habit_task_manager/
password_manager/
digital_automation/
```

**Best Practices**

- Use a virtual environment for each project to isolate dependencies.

- Test scripts using dry-run options when available.

- Modify YAML/JSON configs to customize behavior without changing code.

- Extend scripts as learning exercises—these are templates, not production-ready systems (especially the password manager).

**License**

This repository is open-source and free to use for learning and personal projects.



## Contributing

We welcome contributions! Whether it's fixing bugs, adding new features, improving documentation, or suggesting ideas, your help is appreciated.  

**How to contribute:**

1. **Fork the repository** and clone it to your local machine.  
2. **Create a new branch** for your feature or bug fix:

```bash
git checkout -b feature-name
```
3. Make your changes and test them thoroughly.

4. Commit your changes with a descriptive message:
```bash
git commit -m "Add feature XYZ" 
```
5. Push your branch to your fork:
```bash
git push origin feature-name
```

6. Open a Pull Request to the main repository.

**Guidelines:**

- Follow the existing coding style and structure.

- Ensure scripts remain compatible with Python 3.

- Update README or create examples if you add new functionality.

- Respect open-source best practices.

We appreciate all contributions and will review pull requests promptly.


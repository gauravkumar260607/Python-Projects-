<div align="center">

# 💰 Smart Expense Tracker

### A Simple Yet Powerful Python CLI Application for Managing Daily Expenses

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

Track • Organize • Analyze

</div>

---

## 📖 Overview

Smart Expense Tracker is a command-line application developed using Python that helps users record and monitor their daily expenses efficiently.

The application allows users to:

✔ Add expenses with date, category, description, and amount

✔ View all recorded expenses

✔ Calculate total spending

✔ Manage personal financial records

This project demonstrates core Python programming concepts including data structures, loops, conditional statements, dictionaries, and user input handling.

---

## ✨ Features

| Feature | Description |
|----------|-------------|
| ➕ Add Expense | Store expense details with category and date |
| 📋 View Expenses | Display all recorded expenses |
| 💰 Total Spending | Calculate overall expenditure |
| 🗂 Categorization | Organize expenses by type |
| 🖥 CLI Interface | Easy-to-use menu-driven system |

---

## 🏗 Architecture

```text
Expense Tracker
│
├── Add Expense
│   ├── Date
│   ├── Category
│   ├── Description
│   └── Amount
│
├── View Expenses
│
├── Calculate Total Expense
│
└── Exit Program
```

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| List | Store Expense Records |
| Dictionary | Structured Expense Data |
| Loops | Menu Navigation |
| Conditionals | User Choice Handling |

---

## 📂 Project Structure

```text
Smart-Expense-Tracker/
│
├── expense_tracker.py
│
└── README.md
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/yourusername/smart-expense-tracker.git
```

### Navigate to Project

```bash
cd smart-expense-tracker
```

### Run Application

```bash
python expense_tracker.py
```

---

## 🎮 Example Usage

```text
--------MENU--------

1. ADD EXPENSE
2. VIEW ALL EXPENSE
3. TOTAL EXPENSE
4. EXIT

Enter Your Choice: 1

Enter Date: 14-06-2026
Enter Category: Food
Enter Description: Pizza
Enter Amount: 250

✅ Expense added successfully!
```

---

## 🧠 Concepts Demonstrated

- Variables
- Lists
- Dictionaries
- Loops
- Conditional Statements
- Data Management
- User Interaction
- CLI Application Development

---

## 📈 Future Enhancements

### Version 2.0

- [ ] Expense Editing
- [ ] Expense Deletion
- [ ] Monthly Reports
- [ ] Category Wise Analysis
- [ ] CSV Export
- [ ] JSON Storage
- [ ] SQLite Database Integration
- [ ] Matplotlib Expense Charts
- [ ] Expense Search & Filters

---

## ⚡ Challenges Solved

This project helped in understanding:

- Data organization using dictionaries
- Dynamic data storage using lists
- Building interactive command-line applications
- Managing user inputs effectively

---

## 🐞 Known Issues

Current implementation contains some improvements that can be made:

```python
for e in expense:
```

Should be:

```python
for e in ExpenseList:
```

Also:

```python
amount = input()
```

Should be converted to integer:

```python
amount = int(input())
```

to ensure accurate total calculations.

---

## 🎯 Learning Outcome

By completing this project, I gained practical experience in:

- Python Programming Fundamentals
- Problem Solving
- Data Handling
- Software Logic Design
- Building Real-World CLI Applications

---

## 🤝 Contributing

Contributions are welcome!

```bash
Fork → Clone → Improve → Commit → Pull Request
```

---

## 📜 License

Distributed under the MIT License.

---

<div align="center">

### ⭐ Star this repository if you found it useful!

Made with ❤️ using Python

</div>

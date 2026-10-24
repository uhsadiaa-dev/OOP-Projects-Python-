# 🐍 OOP Projects in Python

A repository showcasing Object-Oriented Programming (OOP) concepts in Python through interactive command-line projects.

---

## 📂 Featured Projects

### 1. 🏦 Bank Account System (`BankAccount.py`)
An interactive banking application that simulates account creation, balance inquiry, deposit, and withdrawal processes.

* **Key Features:**
  * Account creation with initial deposit validation.
  * Real-time balance updates and account summary.
  * Deposit and withdrawal mechanism with insufficient balance checks.
  * Menu-driven CLI interface with robust error handling (`try-except`).

* **OOP Concepts Used:**
  * **Encapsulation:** Managing state (`name` and `initialbalance`) inside the `BankAccount` class.
  * **Dunder Methods:** Custom formatting via `__str__`.

---

### 2. 💸 Expense Tracker 2.0 (`Expense_tracker2.py`)
A spending management application that records individual expenses and computes total expenditures.

* **Key Features:**
  * Itemized expense entry with cost, category, and description.
  * View option to display all logged expenses.
  * Total spending calculation logic.
  * Input validation preventing negative cost entries.

* **OOP Concepts Used:**
  * **Class Composition:** The `ExpenseTracker` class manages a collection (`list`) of `Expense` class objects.
  * **Separation of Concerns:** `Expense` represents the data model, while `ExpenseTracker` manages application logic.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed.

### How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/uhsadiaa-dev/OOP-Projects-Python-.git
   cd OOP-Projects-Python-
   ```

2. **Run Bank Account System:**
   ```bash
   python BankAccount.py
   ```

3. **Run Expense Tracker 2.0:**
   ```bash
   python Expense_tracker2.py
   ```

---

## 📝 Concepts Covered

- Class instantiation and constructors (`__init__`)
- Custom string representations (`__str__`)
- Object composition and list handling
- Input validation & Exception handling (`try-except`)

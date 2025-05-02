# 🏦 In-Memory Banking System

![Test Coverage](./coverage.svg)

A lightweight in-memory banking system implemented in Python. This project supports multiple users, each with zero or more bank accounts, and allows basic banking operations with no persistent storage.

---

## ⚙️ Tech Stack

- **Python** (3.10+)
- **PyTest** (unit testing)
- **Python venv** (virtual environment)
- **GitHub Actions** (CI/CD pipeline)

---

## ✨ Features

- ✅ Create users and accounts with an initial balance  
- ✅ Each user may have **zero, one, or more** accounts  
- ✅ Deposit funds into any owned account  
- ✅ Withdraw funds (no overdraft allowed)  
- ✅ Transfer funds between accounts  
- ✅ View account transaction history *(optional)*

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/WideSu/banking_system_backend.git
cd banking-system

### 2. Set up the virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🧠 Example Use
You can run an interactive session like this:
```python
>>> from banking import BankingSystem
>>> bank = BankingSystem()
>>> user = bank.create_user("Alice")
>>> account = bank.create_account("Alice", "Savings", 1000)
>>> account.deposit(500)
>>> account.withdraw(200)
>>> account.get_transaction_history()
```
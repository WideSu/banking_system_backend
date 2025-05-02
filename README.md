# 🏦 In-Memory Banking System

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
- ✅ Each user may have **one** accounts 
    - one user multiple accounts requires authentications which obeys KISS principle
- ✅ Deposit funds into any owned account 
- ✅ Withdraw funds (no overdraft allowed)  
- ✅ Transfer funds between accounts  
- ✅ View account transaction history *(optional)*

---

## Code Structure

```
banking_system/
├── LICENSE
├── README.md
├── banking                 # Python package
│   ├── __init__.py         # Empty file to make it a package
│   └── core.py             # Our main banking code
├── requirements.txt
└── tests
    └── test_banking.py     # Our test file
```

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

### 2. Example Use
You can run an interactive session like this:
```python
>>> from banking.core import *
>>> bank = Bank()
>>> account = bank.create_account("Alice", 100.0)
>>> account.deposit(500)
>>> account.withdraw(200)
>>> account.get_transaction_history()
```
### 3. Run Unit Tests
- 1. Test coverage
```bash
pytest --cov=banking tests/
```
Example output:
```bash
======================================= test session starts =======================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: cov-6.1.1
collected 13 items                                                                                                                                                                    

tests/test_banking.py .............                                                                                                                                             [100%]

========================================= tests coverage 
________________________________ coverage: platform darwin, python 3.10.9-final-0 _________________________________

Name                  Stmts   Miss  Cover   Missing
------
banking/__init__.py       0      0   100%
banking/core.py          55      0   100%
------
TOTAL                    55      0   100%
======================================= 13 passed in 0.03s ========================================
```
- 2. With log for each test case (execuetion time, result)
```bash
pytest --log-cli-level=INFO -v
```
Example output:
```bash
======================================= test session starts =======================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0 -- /Users/huanganni/Documents/GitHub/banking_system/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: cov-6.1.1
collected 13 items                                                                                                                                                                    

tests/test_banking.py::test_account_creation 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_account_creation
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_account_creation
PASSED                                                                                                                                                                          [  7%]
tests/test_banking.py::test_deposit 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_deposit
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_deposit
PASSED                                                                                                                                                                          [ 15%]
tests/test_banking.py::test_withdraw 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_withdraw
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_withdraw
PASSED                                                                                                                                                                          [ 23%]
tests/test_banking.py::test_withdraw_insufficient_funds 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_withdraw_insufficient_funds
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_withdraw_insufficient_funds
PASSED                                                                                                                                                                          [ 30%]
tests/test_banking.py::test_negative_deposit 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_negative_deposit
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_negative_deposit
PASSED                                                                                                                                                                          [ 38%]
tests/test_banking.py::test_negative_withdraw 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_negative_withdraw
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_negative_withdraw
PASSED                                                                                                                                                                          [ 46%]
tests/test_banking.py::test_transfer_successful 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_transfer_successful
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_transfer_successful
PASSED                                                                                                                                                                          [ 53%]
tests/test_banking.py::test_transfer_to_self 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_transfer_to_self
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_transfer_to_self
PASSED                                                                                                                                                                          [ 61%]
tests/test_banking.py::test_create_account 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_create_account
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_create_account
PASSED                                                                                                                                                                          [ 69%]
tests/test_banking.py::test_create_duplicate_account 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_create_duplicate_account
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_create_duplicate_account
PASSED                                                                                                                                                                          [ 76%]
tests/test_banking.py::test_create_account_negative_balance 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_create_account_negative_balance
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_create_account_negative_balance
PASSED                                                                                                                                                                          [ 84%]
tests/test_banking.py::test_get_account_success 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_get_account_success
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_get_account_success
PASSED                                                                                                                                                                          [ 92%]
tests/test_banking.py::test_get_account_not_found 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:19 🚀 Starting test: test_get_account_not_found
INFO     test_banking:test_banking.py:22 ✅ Test passed: test_get_account_not_found
PASSED                                                                                                                                                                          [100%]

======================================= 13 passed in 0.02s ========================================
(venv) (base) huanganni@Huangs-MacBook-Pro banking_system % pytest --log-cli-level=INFO -v
======================================= test session starts =======================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0 -- /Users/huanganni/Documents/GitHub/banking_system/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: cov-6.1.1
collected 13 items                                                                                                                                                                    

tests/test_banking.py::test_account_creation 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_account_creation
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_account_creation
PASSED                                                                                                                                                                          [  7%]
tests/test_banking.py::test_deposit 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_deposit
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_deposit
PASSED                                                                                                                                                                          [ 15%]
tests/test_banking.py::test_withdraw 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_withdraw
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_withdraw
PASSED                                                                                                                                                                          [ 23%]
tests/test_banking.py::test_withdraw_insufficient_funds 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_withdraw_insufficient_funds
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_withdraw_insufficient_funds
PASSED                                                                                                                                                                          [ 30%]
tests/test_banking.py::test_negative_deposit 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_negative_deposit
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_negative_deposit
PASSED                                                                                                                                                                          [ 38%]
tests/test_banking.py::test_negative_withdraw 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_negative_withdraw
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_negative_withdraw
PASSED                                                                                                                                                                          [ 46%]
tests/test_banking.py::test_transfer_successful 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_transfer_successful
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_transfer_successful
PASSED                                                                                                                                                                          [ 53%]
tests/test_banking.py::test_transfer_to_self 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_transfer_to_self
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_transfer_to_self
PASSED                                                                                                                                                                          [ 61%]
tests/test_banking.py::test_create_account 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_create_account
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_create_account
PASSED                                                                                                                                                                          [ 69%]
tests/test_banking.py::test_create_duplicate_account 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_create_duplicate_account
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_create_duplicate_account
PASSED                                                                                                                                                                          [ 76%]
tests/test_banking.py::test_create_account_negative_balance 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_create_account_negative_balance
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_create_account_negative_balance
PASSED                                                                                                                                                                          [ 84%]
tests/test_banking.py::test_get_account_success 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_get_account_success
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_get_account_success
PASSED                                                                                                                                                                          [ 92%]
tests/test_banking.py::test_get_account_not_found 
--------------------------------------- live log call ---------------------------------------
INFO     test_banking:test_banking.py:25 🚀 Starting test: test_get_account_not_found
INFO     test_banking:test_banking.py:33 ✅ Test passed in 0.0001s: test_get_account_not_found
PASSED                                                                                                                                                                          [100%]

======================================= 13 passed in 0.03s ========================================
```

- 3. Without log info (an overview of the results for all tests)
```bash
pytest -v
```

Example output:
```bash
(venv) (base) huanganni@Huangs-MacBook-Pro banking_system % pytest -v
======================================= test session starts =======================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0 -- /Users/huanganni/Documents/GitHub/banking_system/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: cov-6.1.1
collected 13 items                                                                                                                                                                    

tests/test_banking.py::test_account_creation PASSED                                                                                                                             [  7%]
tests/test_banking.py::test_deposit PASSED                                                                                                                                      [ 15%]
tests/test_banking.py::test_withdraw PASSED                                                                                                                                     [ 23%]
tests/test_banking.py::test_withdraw_insufficient_funds PASSED                                                                                                                  [ 30%]
tests/test_banking.py::test_negative_deposit PASSED                                                                                                                             [ 38%]
tests/test_banking.py::test_negative_withdraw PASSED                                                                                                                            [ 46%]
tests/test_banking.py::test_transfer_successful PASSED                                                                                                                          [ 53%]
tests/test_banking.py::test_transfer_to_self PASSED                                                                                                                             [ 61%]
tests/test_banking.py::test_create_account PASSED                                                                                                                               [ 69%]
tests/test_banking.py::test_create_duplicate_account PASSED                                                                                                                     [ 76%]
tests/test_banking.py::test_create_account_negative_balance PASSED                                                                                                              [ 84%]
tests/test_banking.py::test_get_account_success PASSED                                                                                                                          [ 92%]
tests/test_banking.py::test_get_account_not_found PASSED 
```
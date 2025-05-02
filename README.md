# 🏦 In-Memory Banking System

A minimal banking system implementation designed for demonstration purposes, featuring:
- Account Management:
    - Bank account creation with initial balance
    - Support for multiple users (one account per user)
- Core Banking Operations:
    - Deposits and withdrawals (no overdraft, and check invalid deposit/withdraw amount)
    - Inter-account fund transfers
    - Complete transaction history tracking

- Technical Characteristics:
    - Pure in-memory operation (no persistent storage)
    - Custom exception handling for banking-specific errors
    - Clean Python implementation

```mermaid
%% System Architecture Diagram for In-Memory Banking System
graph TD
    subgraph Python_Banking_System["Python Banking System"]
        A[Bank] -->|manages| B[Account]
        B -->|records| C[Transactions]
    end

    subgraph Core_Operations["Core Operations"]
        B --> D[Account Operations]
        D --> D1[Deposit]
        D --> D2[Withdraw]
        D --> D3[Transfer]
        D --> D4[Get Balance]
        C --> E[Transaction Record]
        E --> E1[Timestamp]
        E --> E2[Amount]
        E --> E3[Type]
    end

    subgraph Error_Handling["Error Handling"]
        F[Custom Exceptions]
        G[ValueError]
        F --> F1[InsufficientFundsError]
        F --> F2[AccountNotFoundError]
        F --> F3[NegativeAmountError]
    end

    %% Styling
    style A fill:#1565C0,stroke:#0D47A1,color:#ffffff
    style B fill:#00897B,stroke:#00695C,color:#ffffff
    style C fill:#6A1B9A,stroke:#4A148C,color:#ffffff
    style D fill:#D32F2F,stroke:#B71C1C,color:#ffffff
    style F fill:#FF8F00,stroke:#E65100,color:#000000
    
    %% Subgraph styling
    class Python_Banking_System,Core_Operations,Error_Handling fill:#f5f5f5,stroke:#bdbdbd,stroke-width:2px
```
---

## ⚙️ Tech Stack

- **Python** (3.10+)
- **PyTest** (unit testing)
- **Python venv** (virtual environment)
- **GitHub Actions** (CI/CD pipeline for install, lint, build, test coverage check>=98%)

---

## ✨ Features and Implementation

- ✅ Create users and accounts with an initial balance
- ✅ Each user may have **one** account (assumed)
    - Accounts are stored using **Dictionary** in {'name':'balance'} pair
    - ⚠️ One user multiple accounts requires authentications which obeys KISS principle
- ✅ Deposit funds into any owned account
- ✅ Withdraw funds (no overdraft allowed)
    - Invalid operations trigger appropriate custom exceptions (`InsufficientFundsError`, `AccountNotFoundError`, `NegativeAmountError`) with contextual error messages, while `ValueError` handles general parameter validation.
- ✅ Transfer funds between accounts 
- ✅ View account transaction history
    - Transaction records are stored in **List**

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

Example output:
```bash
['Account created with balance: 100.00', 'Deposited: 500.00', 'Withdrawn: 200.00']
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

========================================= tests coverage =========================================
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
```

- 3. Without log info (an overview of the results for all tests)
```bash
pytest -v
```

Example output:
```bash
========================================= test session starts =========================================
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
tests/test_banking.py::test_get_account_not_found PASSED                                                                                                                        [100%]                                                      
```
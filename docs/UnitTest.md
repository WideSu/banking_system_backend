### Unit Test Design
The unit test cases in the banking_system project cover various functionalities of the system, ensuring its reliability and correctness. Here's a description of the test cases:

1. Account Management:
- Tests for creating accounts successfully.
- Tests for handling errors like creating accounts with negative balances.

2. Balance Retrieval:
- Tests for retrieving the balance of existing accounts.
- Tests for handling non-existent accounts.
3. Deposits:
- Tests for successful deposits into accounts.
- Tests for handling invalid deposit amounts, such as negative values.
4. Withdrawals:
- Tests for successful withdrawals and handling insufficient funds.
5. Transfers:
- Tests for successful transfers between accounts.
- Tests for handling errors during transfers, such as invalid accounts or insufficient funds.
6. Concurrency:
- Tests for concurrent deposits to ensure thread safety.
- Tests for concurrent withdrawals to validate system behavior under simultaneous operations.

These tests ensure the core functionalities of the banking system are robust and handle edge cases effectively.
### Command and result
#### 1. Test coverage
Run the command below in console to show the unit test result with coverage
```bash
pytest --cov=banking tests/
```
Example output:
```bash
======================================== test session starts ========================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: anyio-4.9.0
collected 22 items                                                                                                                                                                    

tests/test_main.py ........                                                                                                                                                     [ 36%]
tests/test_models.py ..............                                                                                                                                             [100%]

======================================== 22 passed in 0.30s =========================================
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
banking/__init__.py       0      0   100%
banking/errors.py         6      0   100%
banking/main.py          55      0   100%
banking/models.py        58      0   100%
---------------------------------------------------
TOTAL                   111      0   100%

```
#### 2. With log for each test case (execuetion time, result)
Run the command below in console
```bash
pytest --log-cli-level=INFO -v
```
Example output:
```bash
======================================== test session starts ========================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0 -- /Users/huanganni/Documents/GitHub/banking_system/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: anyio-4.9.0
collected 26 items                                                                                                                                                                    

tests/test_main.py::test_create_account_success 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
PASSED                                                                                                                                                                          [  4%]
tests/test_main.py::test_create_account_negative_balance 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [  8%]
tests/test_main.py::test_get_balance_existing 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/carol "HTTP/1.1 200 OK"
PASSED                                                                                                                                                                          [ 12%]
tests/test_main.py::test_get_balance_not_found 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/doesnotexist "HTTP/1.1 404 Not Found"
PASSED                                                                                                                                                                          [ 14%]
tests/test_main.py::test_deposit_success 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/dan "HTTP/1.1 200 OK"
PASSED                                                                                                                                                                          [ 18%]
tests/test_main.py::test_deposit_negative_amount 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [ 22%]
tests/test_main.py::test_withdraw_success_and_insufficient 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [ 26%]           
tests/test_main.py::test_transfer_success_and_errors 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_transfer_success_and_errors
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/gina "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/hank "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 400 Bad Request"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 400 Bad Request"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0091s: test_transfer_success_and_errors
PASSED                                                                                                                                                         [ 30%]
tests/test_main.py::test_concurrent_deposits 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_concurrent_deposits
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: setup_accounts
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0022s: setup_accounts
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0139s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0139s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0149s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0178s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0173s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0189s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0191s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0196s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0228s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0130s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0125s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0140s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0125s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0078s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0090s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0126s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0120s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0138s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0143s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0141s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0126s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0103s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0118s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0079s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0099s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0116s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0113s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0115s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0125s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0164s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0149s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0136s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0104s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0104s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0111s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0105s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0125s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0140s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0145s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0164s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0147s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0139s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0142s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0122s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0137s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0199s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0147s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0118s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0119s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0170s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0167s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0153s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0109s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0204s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0208s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0215s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0137s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0138s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0090s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0112s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0102s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0164s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0088s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0106s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0105s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0132s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0102s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0091s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0104s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0119s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0107s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0103s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0122s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0122s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0092s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0099s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0117s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0117s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0128s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0089s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0097s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0102s: deposit_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0090s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0079s: deposit_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0085s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0219s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0214s: deposit_task
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/alice "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.1808s: test_concurrent_deposits
PASSED                                                                                                                                                         [ 34%]
tests/test_main.py::test_concurrent_withdrawals 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_concurrent_withdrawals
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: setup_accounts
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0025s: setup_accounts
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0167s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0142s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0202s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0199s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0149s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0223s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0223s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0177s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0166s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0076s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0140s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0107s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0105s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0112s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0157s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0171s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0167s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0173s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0201s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0140s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0146s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0092s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0140s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0129s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0102s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0095s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0126s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0113s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0122s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0096s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0143s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0103s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0099s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0115s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0098s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0116s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0129s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0104s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0107s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0077s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0128s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0128s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0096s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0109s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0097s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0090s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0098s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0104s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0124s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0132s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0112s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0170s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0133s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0162s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0189s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0232s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0160s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0199s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0136s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0171s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0194s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0135s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0147s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0157s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0162s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0162s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0161s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0202s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0158s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0152s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0153s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0109s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0078s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0126s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0123s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0111s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0097s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0112s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0118s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0103s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0124s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0143s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0158s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: withdraw_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0111s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0167s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0141s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0143s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0090s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0083s: withdraw_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0074s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0068s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0050s: withdraw_task
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/bob "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.1664s: test_concurrent_withdrawals
PASSED                                                                                                                                                         [ 38%]
tests/test_main.py::test_concurrent_transfers 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_concurrent_transfers
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: setup_accounts
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0025s: setup_accounts
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0100s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0127s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0126s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0127s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0136s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0116s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0102s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0125s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0097s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0124s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0398s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0513s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0531s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0531s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0539s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0358s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0568s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0568s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0109s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0574s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0575s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0061s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0091s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0106s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0153s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0129s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0121s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0122s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0164s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0139s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0095s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0074s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0084s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0104s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0118s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0122s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0106s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0111s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0101s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0136s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0137s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0135s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0110s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0099s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0094s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0073s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0069s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0096s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0101s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0119s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0131s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0134s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0129s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0091s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0112s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0142s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0154s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0085s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0094s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0144s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0126s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0132s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0111s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0175s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0255s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0283s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0302s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0249s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0247s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0288s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0351s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0225s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0220s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0143s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0198s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0134s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0145s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0146s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0152s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0156s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0172s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0184s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0200s: transfer_task
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0196s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0192s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0180s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0157s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0114s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0113s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0157s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0108s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0083s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0076s: transfer_task
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0060s: transfer_task
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/alice "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/bob "HTTP/1.1 200 OK"
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.2094s: test_concurrent_transfers
PASSED                                                                                                                                                         [ 42%]
tests/test_models.py::test_account_creation 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_account_creation
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_account_creation
PASSED                                                                                                                                                         [ 46%]
tests/test_models.py::test_deposit_valid 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_deposit_valid
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_deposit_valid
PASSED                                                                                                                                                         [ 50%]
tests/test_models.py::test_deposit_negative 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_deposit_negative
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_deposit_negative
PASSED                                                                                                                                                         [ 53%]
tests/test_models.py::test_withdraw_valid 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_withdraw_valid
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_withdraw_valid
PASSED                                                                                                                                                         [ 57%]
tests/test_models.py::test_withdraw_insufficient 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_withdraw_insufficient
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_withdraw_insufficient
PASSED                                                                                                                                                         [ 61%]
tests/test_models.py::test_withdraw_negative 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_withdraw_negative
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_withdraw_negative
PASSED                                                                                                                                                         [ 65%]
tests/test_models.py::test_transfer_successful 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_transfer_successful
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_transfer_successful
PASSED                                                                                                                                                         [ 69%]
tests/test_models.py::test_transfer_to_self 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_transfer_to_self
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_transfer_to_self
PASSED                                                                                                                                                         [ 73%]
tests/test_models.py::test_transaction_history_is_copy 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_transaction_history_is_copy
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_transaction_history_is_copy
PASSED                                                                                                                                                         [ 76%]
tests/test_models.py::test_bank_create_account_success 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_bank_create_account_success
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_bank_create_account_success
PASSED                                                                                                                                                         [ 80%]
tests/test_models.py::test_bank_create_account_duplicate 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_bank_create_account_duplicate
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_bank_create_account_duplicate
PASSED                                                                                                                                                         [ 84%]
tests/test_models.py::test_bank_create_account_negative_initial 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_bank_create_account_negative_initial
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_bank_create_account_negative_initial
PASSED                                                                                                                                                         [ 88%]
tests/test_models.py::test_get_account_success 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_get_account_success
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0000s: test_get_account_success
PASSED                                                                                                                                                         [ 92%]
tests/test_models.py::test_get_account_not_found 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_get_account_not_found
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0001s: test_get_account_not_found
PASSED                                                                                                                                                         [ 96%]
tests/test_models.py::test_concurrent_transfer_does_not_deadlock 
----------------------------------------  live log call ----------------------------------------
INFO     tests.test_logger:test_logger.py:21 🚀 Starting test: test_concurrent_transfer_does_not_deadlock
INFO     tests.test_logger:test_logger.py:29 ✅ Test passed in 0.0006s: test_concurrent_transfer_does_not_deadlock
PASSED                                                                                                                                                         [100%]
========================================= 26 passed in 0.79s =========================================
```

#### 3. Without log info (an overview of the results for all tests)
Run the command below in console
```bash
pytest -v
```

Example output:
```bash
========================================= test session starts ========================================
platform darwin -- Python 3.10.9, pytest-8.3.5, pluggy-1.5.0 -- /Users/huanganni/Documents/GitHub/banking_system/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/huanganni/Documents/GitHub/banking_system
plugins: anyio-4.9.0
collected 26 items                                                                                                                                                                    
tests/test_main.py::test_create_account_success PASSED                                                                                                         [  3%]
tests/test_main.py::test_create_account_negative_balance PASSED                                                                                                [  7%]
tests/test_main.py::test_get_balance_existing PASSED                                                                                                           [ 11%]
tests/test_main.py::test_get_balance_not_found PASSED                                                                                                          [ 15%]
tests/test_main.py::test_deposit_success PASSED                                                                                                                [ 19%]
tests/test_main.py::test_deposit_negative_amount PASSED                                                                                                        [ 23%]
tests/test_main.py::test_withdraw_success_and_insufficient PASSED                                                                                              [ 26%]
tests/test_main.py::test_transfer_success_and_errors PASSED                                                                                                    [ 30%]
tests/test_main.py::test_concurrent_deposits PASSED                                                                                                            [ 34%]
tests/test_main.py::test_concurrent_withdrawals PASSED                                                                                                         [ 38%]
tests/test_main.py::test_concurrent_transfers PASSED                                                                                                           [ 42%]
tests/test_models.py::test_account_creation PASSED                                                                                                             [ 46%]
tests/test_models.py::test_deposit_valid PASSED                                                                                                                [ 50%]
tests/test_models.py::test_deposit_negative PASSED                                                                                                             [ 53%]
tests/test_models.py::test_withdraw_valid PASSED                                                                                                               [ 57%]
tests/test_models.py::test_withdraw_insufficient PASSED                                                                                                        [ 61%]
tests/test_models.py::test_withdraw_negative PASSED                                                                                                            [ 65%]
tests/test_models.py::test_transfer_successful PASSED                                                                                                          [ 69%]
tests/test_models.py::test_transfer_to_self PASSED                                                                                                             [ 73%]
tests/test_models.py::test_transaction_history_is_copy PASSED                                                                                                  [ 76%]
tests/test_models.py::test_bank_create_account_success PASSED                                                                                                  [ 80%]
tests/test_models.py::test_bank_create_account_duplicate PASSED                                                                                                [ 84%]
tests/test_models.py::test_bank_create_account_negative_initial PASSED                                                                                         [ 88%]
tests/test_models.py::test_get_account_success PASSED                                                                                                          [ 92%]
tests/test_models.py::test_get_account_not_found PASSED                                                                                                        [ 96%]
tests/test_models.py::test_concurrent_transfer_does_not_deadlock PASSED                                                                                        [100%]
======================================== 21 passed in 0.22s ========================================
                                                    
```
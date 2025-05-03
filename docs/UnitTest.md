### Run Unit Tests
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
banking/models.py        50      0   100%
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
collected 21 items                                                                                                                                                                    

tests/test_main.py::test_create_account_success 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
PASSED                                                                                                                                                                          [  4%]
tests/test_main.py::test_create_account_negative_balance 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [  9%]
tests/test_main.py::test_get_balance_existing 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/carol "HTTP/1.1 200 OK"
PASSED                                                                                                                                                                          [ 14%]
tests/test_main.py::test_get_balance_not_found 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/doesnotexist "HTTP/1.1 404 Not Found"
PASSED                                                                                                                                                                          [ 19%]
tests/test_main.py::test_deposit_success 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/dan "HTTP/1.1 200 OK"
PASSED                                                                                                                                                                          [ 23%]
tests/test_main.py::test_deposit_negative_amount 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/deposit "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [ 28%]
tests/test_main.py::test_withdraw_success_and_insufficient 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/withdraw "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [ 33%]
tests/test_main.py::test_transfer_success_and_errors 
---------------------------------------- live log call ----------------------------------------
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/accounts/ "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/gina "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: GET http://testserver/accounts/hank "HTTP/1.1 200 OK"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 400 Bad Request"
INFO     httpx:_client.py:1025 HTTP Request: POST http://testserver/transfer "HTTP/1.1 400 Bad Request"
PASSED                                                                                                                                                                          [ 38%]
tests/test_models.py::test_account_creation 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_account_creation
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_account_creation
PASSED                                                                                                                                                                          [ 42%]
tests/test_models.py::test_deposit 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_deposit
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_deposit
PASSED                                                                                                                                                                          [ 47%]
tests/test_models.py::test_withdraw 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_withdraw
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_withdraw
PASSED                                                                                                                                                                          [ 52%]
tests/test_models.py::test_withdraw_insufficient_funds 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_withdraw_insufficient_funds
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_withdraw_insufficient_funds
PASSED                                                                                                                                                                          [ 57%]
tests/test_models.py::test_negative_deposit 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_negative_deposit
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_negative_deposit
PASSED                                                                                                                                                                          [ 61%]
tests/test_models.py::test_negative_withdraw 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_negative_withdraw
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_negative_withdraw
PASSED                                                                                                                                                                          [ 66%]
tests/test_models.py::test_transfer_successful 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_transfer_successful
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_transfer_successful
PASSED                                                                                                                                                                          [ 71%]
tests/test_models.py::test_transfer_to_self 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_transfer_to_self
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_transfer_to_self
PASSED                                                                                                                                                                          [ 76%]
tests/test_models.py::test_create_account 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_create_account
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_create_account
PASSED                                                                                                                                                                          [ 80%]
tests/test_models.py::test_create_duplicate_account 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_create_duplicate_account
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0001s: test_create_duplicate_account
PASSED                                                                                                                                                                          [ 85%]
tests/test_models.py::test_create_account_negative_balance 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_create_account_negative_balance
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0000s: test_create_account_negative_balance
PASSED                                                                                                                                                                          [ 90%]
tests/test_models.py::test_get_account_success 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_get_account_success
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0000s: test_get_account_success
PASSED                                                                                                                                                                          [ 95%]
tests/test_models.py::test_get_account_not_found 
---------------------------------------- live log call ----------------------------------------
INFO     tests.test_models:test_models.py:25 🚀 Starting test: test_get_account_not_found
INFO     tests.test_models:test_models.py:33 ✅ Test passed in 0.0000s: test_get_account_not_found
PASSED                                                                                                                                                                          [100%]

======================================== 21 passed in 0.22s ========================================
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
collected 21 items                                                                                                                                                                    

tests/test_main.py::test_create_account_success PASSED                                                                                                                          [  4%]
tests/test_main.py::test_create_account_negative_balance PASSED                                                                                                                 [  9%]
tests/test_main.py::test_get_balance_existing PASSED                                                                                                                            [ 14%]
tests/test_main.py::test_get_balance_not_found PASSED                                                                                                                           [ 19%]
tests/test_main.py::test_deposit_success PASSED                                                                                                                                 [ 23%]
tests/test_main.py::test_deposit_negative_amount PASSED                                                                                                                         [ 28%]
tests/test_main.py::test_withdraw_success_and_insufficient PASSED                                                                                                               [ 33%]
tests/test_main.py::test_transfer_success_and_errors PASSED                                                                                                                     [ 38%]
tests/test_models.py::test_account_creation PASSED                                                                                                                              [ 42%]
tests/test_models.py::test_deposit PASSED                                                                                                                                       [ 47%]
tests/test_models.py::test_withdraw PASSED                                                                                                                                      [ 52%]
tests/test_models.py::test_withdraw_insufficient_funds PASSED                                                                                                                   [ 57%]
tests/test_models.py::test_negative_deposit PASSED                                                                                                                              [ 61%]
tests/test_models.py::test_negative_withdraw PASSED                                                                                                                             [ 66%]
tests/test_models.py::test_transfer_successful PASSED                                                                                                                           [ 71%]
tests/test_models.py::test_transfer_to_self PASSED                                                                                                                              [ 76%]
tests/test_models.py::test_create_account PASSED                                                                                                                                [ 80%]
tests/test_models.py::test_create_duplicate_account PASSED                                                                                                                      [ 85%]
tests/test_models.py::test_create_account_negative_balance PASSED                                                                                                               [ 90%]
tests/test_models.py::test_get_account_success PASSED                                                                                                                           [ 95%]
tests/test_models.py::test_get_account_not_found PASSED                                                                                                                         [100%]

======================================== 21 passed in 0.22s ========================================
                                                    
```
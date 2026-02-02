from concurrent.futures import ThreadPoolExecutor, as_completed
import pytest
from fastapi.testclient import TestClient
from banking.main import app
from tests.test_logger import log_test

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_bank(monkeypatch):
    """
    Each test gets a fresh Bank() instance.
    We re-import main and replace its `bank` with a new one.
    """
    from banking.models import Bank
    import banking.main as m
    m.bank = Bank()
    yield

@log_test()
def test_create_account_success():
    resp = client.post("/accounts/", json={"name": "alice", "initial_balance": 100.0})
    assert resp.status_code == 200
    assert resp.json() == {"message": "Account 'alice' created."}
@log_test()
def test_create_account_negative_balance():
    resp = client.post("/accounts/", json={"name": "bob", "initial_balance": -10.0})
    assert resp.status_code == 400
    assert "negative" in resp.json()["detail"].lower()
@log_test()
def test_get_balance_existing():
    client.post("/accounts/", json={"name": "carol", "initial_balance": 50.0})
    resp = client.get("/accounts/carol")
    assert resp.status_code == 200
    assert resp.json() == {"name": "carol", "balance": 50.0}
@log_test()
def test_get_balance_not_found():
    resp = client.get("/accounts/doesnotexist")
    assert resp.status_code == 404
@log_test()
def test_deposit_success():
    client.post("/accounts/", json={"name": "dan", "initial_balance": 0.0})
    resp = client.post("/accounts/dan/deposits", json={"amount": 25.5})
    assert resp.status_code == 200
    assert "25.50 deposited to dan" in resp.json()["message"]

    # verify new balance
    b = client.get("/accounts/dan").json()["balance"]
    assert b == pytest.approx(25.5)
@log_test()
def test_deposit_negative_amount():
    client.post("/accounts/", json={"name": "eve", "initial_balance": 10.0})
    resp = client.post("/accounts/eve/deposits", json={"amount": -5.0})
    assert resp.status_code == 400
    assert "positive" in resp.json()["detail"].lower()
@log_test()
def test_withdraw_success_and_insufficient():
    client.post("/accounts/", json={"name": "frank", "initial_balance": 30.0})
    ok = client.post("/accounts/frank/withdrawals", json={"amount": 10.0})
    assert ok.status_code == 200

    # now withdraw too much
    too_much = client.post("/accounts/frank/withdrawals", json={"amount": 50.0})
    assert too_much.status_code == 400
    assert "balance is only" in too_much.json()["detail"]
@log_test()
def test_transfer_success_and_errors():
    client.post("/accounts/", json={"name": "gina", "initial_balance": 100.0})
    client.post("/accounts/", json={"name": "hank", "initial_balance": 0.0})

    # good transfer
    ok = client.post("/transfers", json={
        "sender": "gina", "recipient": "hank", "amount": 40.0
    })
    assert ok.status_code == 200

    # balances updated
    assert client.get("/accounts/gina").json()["balance"] == pytest.approx(60.0)
    assert client.get("/accounts/hank").json()["balance"] == pytest.approx(40.0)

    # transfer too much
    err = client.post("/transfers", json={
        "sender": "gina", "recipient": "hank", "amount": 1000.0
    })
    assert err.status_code == 400
    assert "balance is only" in err.json()["detail"]

    # same-account transfer
    err2 = client.post("/transfers", json={
        "sender": "gina", "recipient": "gina", "amount": 10.0
    })
    assert err2.status_code == 400
    assert "same account" in err2.json()["detail"].lower()

@log_test()
def setup_accounts():
    client.post("/accounts/", json={"name": "alice", "initial_balance": 1000})
    client.post("/accounts/", json={"name": "bob", "initial_balance": 1000})

@log_test()
def deposit_task(name, amount):
    return client.post(f"/accounts/{name}/deposits", json={"amount": amount})

@log_test()
def withdraw_task(name, amount):
    return client.post(f"/accounts/{name}/withdrawals", json={"amount": amount})

@log_test()
def transfer_task(sender, recipient, amount):
    return client.post("/transfers", json={"sender": sender, "recipient": recipient, "amount": amount})

@log_test()
def test_concurrent_deposits():
    setup_accounts()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(deposit_task, "alice", 10) for _ in range(100)]
        results = [f.result() for f in as_completed(futures)]

    final_balance = client.get("/accounts/alice").json()["balance"]
    assert final_balance == 1000 + 10 * 100

@log_test()
def test_concurrent_withdrawals():
    setup_accounts()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(withdraw_task, "bob", 5) for _ in range(100)]
        results = [f.result() for f in as_completed(futures)]

    final_balance = client.get("/accounts/bob").json()["balance"]
    # All should succeed: 100 withdrawals of 5 from 1000
    assert final_balance == 1000 - 5 * 100

@log_test()
def test_concurrent_transfers():
    setup_accounts()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(transfer_task, "alice", "bob", 5) for _ in range(100)]
        results = [f.result() for f in as_completed(futures)]

    alice_balance = client.get("/accounts/alice").json()["balance"]
    bob_balance = client.get("/accounts/bob").json()["balance"]

    assert alice_balance == 1000 - 5 * 100
    assert bob_balance == 1000 + 5 * 100
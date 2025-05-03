import pytest
from fastapi.testclient import TestClient
from banking.main import app

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

def test_create_account_success():
    resp = client.post("/accounts/", json={"name": "alice", "initial_balance": 100.0})
    assert resp.status_code == 200
    assert resp.json() == {"message": "Account 'alice' created."}

def test_create_account_negative_balance():
    resp = client.post("/accounts/", json={"name": "bob", "initial_balance": -10.0})
    assert resp.status_code == 400
    assert "negative" in resp.json()["detail"].lower()

def test_get_balance_existing():
    client.post("/accounts/", json={"name": "carol", "initial_balance": 50.0})
    resp = client.get("/accounts/carol")
    assert resp.status_code == 200
    assert resp.json() == {"name": "carol", "balance": 50.0}

def test_get_balance_not_found():
    resp = client.get("/accounts/doesnotexist")
    assert resp.status_code == 404

def test_deposit_success():
    client.post("/accounts/", json={"name": "dan", "initial_balance": 0.0})
    resp = client.post("/deposit", json={"name": "dan", "amount": 25.5})
    assert resp.status_code == 200
    assert "25.50 deposited to dan" in resp.json()["message"]

    # verify new balance
    b = client.get("/accounts/dan").json()["balance"]
    assert b == pytest.approx(25.5)

def test_deposit_negative_amount():
    client.post("/accounts/", json={"name": "eve", "initial_balance": 10.0})
    resp = client.post("/deposit", json={"name": "eve", "amount": -5.0})
    assert resp.status_code == 400
    assert "positive" in resp.json()["detail"].lower()

def test_withdraw_success_and_insufficient():
    client.post("/accounts/", json={"name": "frank", "initial_balance": 30.0})
    ok = client.post("/withdraw", json={"name": "frank", "amount": 10.0})
    assert ok.status_code == 200

    # now try too much
    too_much = client.post("/withdraw", json={"name": "frank", "amount": 50.0})
    assert too_much.status_code == 400
    assert "balance is only" in too_much.json()["detail"]

def test_transfer_success_and_errors():
    client.post("/accounts/", json={"name": "gina", "initial_balance": 100.0})
    client.post("/accounts/", json={"name": "hank", "initial_balance": 0.0})

    # good transfer
    ok = client.post("/transfer", json={
        "sender": "gina", "recipient": "hank", "amount": 40.0
    })
    assert ok.status_code == 200

    # balances updated
    assert client.get("/accounts/gina").json()["balance"] == pytest.approx(60.0)
    assert client.get("/accounts/hank").json()["balance"] == pytest.approx(40.0)

    # transfer too much
    err = client.post("/transfer", json={
        "sender": "gina", "recipient": "hank", "amount": 1000.0
    })
    assert err.status_code == 400
    assert "balance is only" in err.json()["detail"]

    # same-account transfer
    err2 = client.post("/transfer", json={
        "sender": "gina", "recipient": "gina", "amount": 10.0
    })
    assert err2.status_code == 400
    assert "same account" in err2.json()["detail"].lower()

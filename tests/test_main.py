
import pytest
import asyncio
from banking.main import app, db

@pytest.mark.asyncio
async def test_create_account_success(client):
    resp = await client.post("/accounts/", json={"name": "alice", "initial_balance": 100.0})
    assert resp.status_code == 200
    assert resp.json() == {"message": "Account 'alice' created."}

@pytest.mark.asyncio
async def test_create_account_negative_balance(client):
    resp = await client.post("/accounts/", json={"name": "bob", "initial_balance": -10.0})
    assert resp.status_code == 400
    assert "negative" in resp.json()["detail"].lower()

@pytest.mark.asyncio
async def test_get_balance_existing(client):
    await client.post("/accounts/", json={"name": "carol", "initial_balance": 50.0})
    resp = await client.get("/accounts/carol")
    assert resp.status_code == 200
    assert resp.json() == {"name": "carol", "balance": 50.0}

@pytest.mark.asyncio
async def test_get_balance_not_found(client):
    resp = await client.get("/accounts/doesnotexist")
    assert resp.status_code == 404

@pytest.mark.asyncio
async def test_deposit_success(client):
    await client.post("/accounts/", json={"name": "dan", "initial_balance": 0.0})
    resp = await client.post("/accounts/dan/deposits", json={"amount": 25.5})
    assert resp.status_code == 200
    assert "25.50 deposited to dan" in resp.json()["message"]

    # verify new balance
    resp = await client.get("/accounts/dan")
    b = resp.json()["balance"]
    assert b == 25.5

@pytest.mark.asyncio
async def test_deposit_negative_amount(client):
    await client.post("/accounts/", json={"name": "eve", "initial_balance": 10.0})
    resp = await client.post("/accounts/eve/deposits", json={"amount": -5.0})
    assert resp.status_code == 400
    assert "positive" in resp.json()["detail"].lower()

@pytest.mark.asyncio
async def test_withdraw_success_and_insufficient(client):
    await client.post("/accounts/", json={"name": "frank", "initial_balance": 30.0})
    ok = await client.post("/accounts/frank/withdrawals", json={"amount": 10.0})
    assert ok.status_code == 200

    # now withdraw too much
    too_much = await client.post("/accounts/frank/withdrawals", json={"amount": 50.0})
    assert too_much.status_code == 400
    assert "balance is only" in too_much.json()["detail"]

@pytest.mark.asyncio
async def test_transfer_success_and_errors(client):
    await client.post("/accounts/", json={"name": "gina", "initial_balance": 100.0})
    await client.post("/accounts/", json={"name": "hank", "initial_balance": 0.0})

    # good transfer
    ok = await client.post("/transfers", json={
        "sender": "gina", "recipient": "hank", "amount": 40.0
    })
    assert ok.status_code == 200

    # balances updated
    resp_gina = await client.get("/accounts/gina")
    assert resp_gina.json()["balance"] == 60.0
    
    resp_hank = await client.get("/accounts/hank")
    assert resp_hank.json()["balance"] == 40.0

    # transfer too much
    err = await client.post("/transfers", json={
        "sender": "gina", "recipient": "hank", "amount": 1000.0
    })
    assert err.status_code == 400
    assert "balance is only" in err.json()["detail"]

    # same-account transfer
    err2 = await client.post("/transfers", json={
        "sender": "gina", "recipient": "gina", "amount": 10.0
    })
    assert err2.status_code == 400
    assert "same account" in err2.json()["detail"].lower()

# Concurrency tests adapted for asyncio

@pytest.mark.asyncio
async def test_concurrent_deposits(client):
    await client.post("/accounts/", json={"name": "alice", "initial_balance": 1000})

    async def deposit_task():
        return await client.post("/accounts/alice/deposits", json={"amount": 10})

    # Run 100 deposits concurrently
    tasks = [deposit_task() for _ in range(100)]
    await asyncio.gather(*tasks)

    final_balance = (await client.get("/accounts/alice")).json()["balance"]
    assert final_balance == 1000 + 10 * 100

@pytest.mark.asyncio
async def test_concurrent_withdrawals(client):
    await client.post("/accounts/", json={"name": "bob", "initial_balance": 1000})

    async def withdraw_task():
        return await client.post("/accounts/bob/withdrawals", json={"amount": 5})

    # Run 100 withdrawals concurrently
    tasks = [withdraw_task() for _ in range(100)]
    await asyncio.gather(*tasks)

    final_balance = (await client.get("/accounts/bob")).json()["balance"]
    assert final_balance == 1000 - 5 * 100

@pytest.mark.asyncio
async def test_concurrent_transfers(client):
    await client.post("/accounts/", json={"name": "alice", "initial_balance": 1000})
    await client.post("/accounts/", json={"name": "bob", "initial_balance": 1000})

    async def transfer_task():
        return await client.post("/transfers", json={"sender": "alice", "recipient": "bob", "amount": 5})

    # Run 100 transfers concurrently
    tasks = [transfer_task() for _ in range(100)]
    await asyncio.gather(*tasks)

    alice_balance = (await client.get("/accounts/alice")).json()["balance"]
    bob_balance = (await client.get("/accounts/bob")).json()["balance"]

    assert alice_balance == 1000 - 5 * 100
    assert bob_balance == 1000 + 5 * 100

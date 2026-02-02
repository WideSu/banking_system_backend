
import pytest
import asyncio
import httpx
from banking.main import app, db

# We need to run the app in a way that allows concurrent requests.
# Since we are testing an ASGI app, we can use httpx.AsyncClient.

@pytest.mark.asyncio
async def test_race_condition_transfer(client):
    # Setup: Clear bank and create two accounts
    # DB reset is handled by autouse fixture in conftest.py
    
    # Create accounts
    await client.post("/accounts/", json={"name": "Alice", "initial_balance": 1000.0})
    await client.post("/accounts/", json={"name": "Bob", "initial_balance": 1000.0})
    
    # We will transfer money back and forth concurrently
    # Alice -> Bob: 10.0
    # Bob -> Alice: 10.0
    # Total balance should remain 2000.0
    
    iterations = 100
    
    async def transfer_a_to_b():
        response = await client.post("/transfers", json={"sender": "Alice", "recipient": "Bob", "amount": 10.0})
        return response.status_code

    async def transfer_b_to_a():
        response = await client.post("/transfers", json={"sender": "Bob", "recipient": "Alice", "amount": 10.0})
        return response.status_code

    tasks = []
    for _ in range(iterations):
        tasks.append(transfer_a_to_b())
        tasks.append(transfer_b_to_a())
        
    # Run all transfers concurrently
    results = await asyncio.gather(*tasks)
    
    # Verify all requests succeeded
    assert all(status == 200 for status in results)
    
    # Verify final balances
    r_alice = await client.get("/accounts/Alice")
    r_bob = await client.get("/accounts/Bob")
    
    alice_bal = r_alice.json()["balance"]
    bob_bal = r_bob.json()["balance"]
    
    print(f"Alice: {alice_bal}, Bob: {bob_bal}")
    
    assert alice_bal + bob_bal == 2000.0

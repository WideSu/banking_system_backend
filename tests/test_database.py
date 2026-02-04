import pytest
from banking.database import Database
from banking.errors import AccountNotFoundError, InsufficientFundsError, NegativeAmountError


@pytest.fixture
def db():
    """Provide a fresh in-memory database for each test."""
    return Database(":memory:")


@pytest.mark.asyncio
async def test_init_db_creates_tables(db):
    await db.init_db()
    conn = await db.get_db()
    async with conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'") as cur:
        assert await cur.fetchone() is not None
    async with conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='transactions'") as cur:
        assert await cur.fetchone() is not None


@pytest.mark.asyncio
async def test_create_account_success(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    balance = await db.get_balance("alice")
    assert balance == 100.0


@pytest.mark.asyncio
async def test_create_account_negative_balance(db):
    await db.init_db()
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        await db.create_account("bob", -10.0)


@pytest.mark.asyncio
async def test_create_account_duplicate(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    with pytest.raises(ValueError, match="Account already exists"):
        await db.create_account("alice", 50.0)


@pytest.mark.asyncio
async def test_get_balance_not_found(db):
    await db.init_db()
    with pytest.raises(AccountNotFoundError):
        await db.get_balance("nonexistent")


@pytest.mark.asyncio
async def test_deposit_success(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.deposit("alice", 50.0)
    balance = await db.get_balance("alice")
    assert balance == 150.0


@pytest.mark.asyncio
async def test_deposit_negative_amount(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    with pytest.raises(NegativeAmountError, match="Amount must be positive"):
        await db.deposit("alice", -10.0)


@pytest.mark.asyncio
async def test_deposit_account_not_found(db):
    await db.init_db()
    with pytest.raises(AccountNotFoundError):
        await db.deposit("nonexistent", 10.0)


@pytest.mark.asyncio
async def test_withdraw_success(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.withdraw("alice", 30.0)
    balance = await db.get_balance("alice")
    assert balance == 70.0


@pytest.mark.asyncio
async def test_withdraw_insufficient_funds(db):
    await db.init_db()
    await db.create_account("alice", 50.0)
    with pytest.raises(InsufficientFundsError, match="Cannot withdraw 60.00; balance is only 50.00"):
        await db.withdraw("alice", 60.0)


@pytest.mark.asyncio
async def test_withdraw_negative_amount(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    with pytest.raises(NegativeAmountError, match="Amount must be positive"):
        await db.withdraw("alice", -10.0)


@pytest.mark.asyncio
async def test_withdraw_account_not_found(db):
    await db.init_db()
    with pytest.raises(AccountNotFoundError):
        await db.withdraw("nonexistent", 10.0)


@pytest.mark.asyncio
async def test_transfer_success(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.create_account("bob", 50.0)
    await db.transfer("alice", "bob", 30.0)
    assert await db.get_balance("alice") == 70.0
    assert await db.get_balance("bob") == 80.0


@pytest.mark.asyncio
async def test_transfer_negative_amount(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.create_account("bob", 50.0)
    with pytest.raises(NegativeAmountError, match="Amount must be positive"):
        await db.transfer("alice", "bob", -10.0)


@pytest.mark.asyncio
async def test_transfer_same_account(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    with pytest.raises(ValueError, match="Cannot transfer to the same account"):
        await db.transfer("alice", "alice", 10.0)


@pytest.mark.asyncio
async def test_transfer_sender_not_found(db):
    await db.init_db()
    await db.create_account("bob", 50.0)
    with pytest.raises(AccountNotFoundError):
        await db.transfer("alice", "bob", 10.0)


@pytest.mark.asyncio
async def test_transfer_recipient_not_found(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    with pytest.raises(AccountNotFoundError):
        await db.transfer("alice", "bob", 10.0)


@pytest.mark.asyncio
async def test_transfer_insufficient_funds(db):
    await db.init_db()
    await db.create_account("alice", 50.0)
    await db.create_account("bob", 100.0)
    with pytest.raises(InsufficientFundsError, match="Cannot withdraw 60.00; balance is only 50.00"):
        await db.transfer("alice", "bob", 60.0)


@pytest.mark.asyncio
async def test_get_transaction_history(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.deposit("alice", 50.0)
    await db.withdraw("alice", 20.0)
    history = await db.get_transaction_history("alice")
    assert len(history) == 3
    assert "Account created: 100.00" in history
    assert "Deposited: 50.00" in history
    assert "Withdrawn: 20.00" in history


@pytest.mark.asyncio
async def test_get_transaction_history_with_transfers(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.create_account("bob", 50.0)
    await db.transfer("alice", "bob", 30.0)
    alice_history = await db.get_transaction_history("alice")
    bob_history = await db.get_transaction_history("bob")
    assert any("Transferred to: 30.00 bob" in entry for entry in alice_history)
    assert any("Received from: 30.00 alice" in entry for entry in bob_history)


@pytest.mark.asyncio
async def test_get_transaction_history_account_not_found(db):
    await db.init_db()
    with pytest.raises(AccountNotFoundError):
        await db.get_transaction_history("nonexistent")


@pytest.mark.asyncio
async def test_reset_db_clears_data(db):
    await db.init_db()
    await db.create_account("alice", 100.0)
    await db.reset_db()
    # Tables should be recreated, so alice should not exist
    with pytest.raises(AccountNotFoundError):
        await db.get_balance("alice")
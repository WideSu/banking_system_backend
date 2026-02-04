import pytest
import pytest_asyncio
import aiosqlite
import os
from banking.database import Database
from banking.errors import AccountNotFoundError, InsufficientFundsError

TEST_DB_PATH = "test_banking_file.db"

@pytest_asyncio.fixture
async def file_db():
    # Setup
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)
    
    db = Database(TEST_DB_PATH)
    await db.init_db()
    
    yield db
    
    # Teardown
    if db._connection:
        await db._connection.close()
        
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

@pytest.mark.asyncio
async def test_file_db_init(file_db):
    assert os.path.exists(TEST_DB_PATH)
    async with aiosqlite.connect(TEST_DB_PATH) as db:
        async with db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='accounts'") as cur:
            assert await cur.fetchone() is not None

@pytest.mark.asyncio
async def test_file_db_create_account(file_db):
    await file_db.create_account("alice", 100.0)
    # Check persistence by creating a new instance
    db2 = Database(TEST_DB_PATH)
    # Note: create_account commits transaction, so data should be on disk.
    # We can check via direct sql or using db2 (but db2 needs connection?)
    # Database class doesn't keep connection open for file-based unless explicitly managed?
    # Wait, Database implementation for file-based:
    # methods use `async with aiosqlite.connect(self.db_path) as db:`
    # So they open/close connection every time.
    
    balance = await db2.get_balance("alice")
    assert balance == 100.0

@pytest.mark.asyncio
async def test_file_db_create_duplicate(file_db):
    await file_db.create_account("alice", 100.0)
    with pytest.raises(ValueError, match="Account already exists"):
        await file_db.create_account("alice", 50.0)

@pytest.mark.asyncio
async def test_file_db_deposit(file_db):
    await file_db.create_account("alice", 100.0)
    await file_db.deposit("alice", 50.0)
    assert await file_db.get_balance("alice") == 150.0

@pytest.mark.asyncio
async def test_file_db_deposit_not_found(file_db):
    # init_db is called in fixture
    with pytest.raises(AccountNotFoundError):
        await file_db.deposit("nonexistent", 10.0)

@pytest.mark.asyncio
async def test_file_db_withdraw(file_db):
    await file_db.create_account("alice", 100.0)
    await file_db.withdraw("alice", 30.0)
    assert await file_db.get_balance("alice") == 70.0

@pytest.mark.asyncio
async def test_file_db_withdraw_insufficient(file_db):
    await file_db.create_account("alice", 50.0)
    with pytest.raises(InsufficientFundsError):
        await file_db.withdraw("alice", 60.0)

@pytest.mark.asyncio
async def test_file_db_withdraw_not_found(file_db):
    with pytest.raises(AccountNotFoundError):
        await file_db.withdraw("nonexistent", 10.0)

@pytest.mark.asyncio
async def test_file_db_transfer(file_db):
    await file_db.create_account("alice", 100.0)
    await file_db.create_account("bob", 50.0)
    await file_db.transfer("alice", "bob", 30.0)
    assert await file_db.get_balance("alice") == 70.0
    assert await file_db.get_balance("bob") == 80.0

@pytest.mark.asyncio
async def test_file_db_transfer_sender_not_found(file_db):
    await file_db.create_account("bob", 50.0)
    with pytest.raises(AccountNotFoundError):
        await file_db.transfer("alice", "bob", 10.0)

@pytest.mark.asyncio
async def test_file_db_transfer_recipient_not_found(file_db):
    await file_db.create_account("alice", 100.0)
    with pytest.raises(AccountNotFoundError):
        await file_db.transfer("alice", "bob", 10.0)

@pytest.mark.asyncio
async def test_file_db_transfer_insufficient(file_db):
    await file_db.create_account("alice", 50.0)
    await file_db.create_account("bob", 50.0)
    with pytest.raises(InsufficientFundsError):
        await file_db.transfer("alice", "bob", 60.0)

@pytest.mark.asyncio
async def test_file_db_history(file_db):
    await file_db.create_account("alice", 100.0)
    await file_db.deposit("alice", 50.0)
    history = await file_db.get_transaction_history("alice")
    assert len(history) == 2

@pytest.mark.asyncio
async def test_file_db_history_not_found(file_db):
    with pytest.raises(AccountNotFoundError):
        await file_db.get_transaction_history("nonexistent")

@pytest.mark.asyncio
async def test_file_db_reset(file_db):
    await file_db.create_account("alice", 100.0)
    await file_db.reset_db()
    with pytest.raises(AccountNotFoundError):
        await file_db.get_balance("alice")

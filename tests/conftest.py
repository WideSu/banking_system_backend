import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from banking.main import app, db

@pytest_asyncio.fixture
async def client():
    """
    Async HTTP client for testing the FastAPI app.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

@pytest_asyncio.fixture(autouse=True)
async def reset_db():
    """
    Use a fresh in-memory database for each test.
    Auto-used for all tests in this directory.
    """
    # Set to memory and reset
    db.db_path = ":memory:"
    # This will initialize the shared connection on the current loop (the pytest loop)
    await db.reset_db()
    yield
    # Cleanup connection to avoid leaks or loop errors
    if db._connection:
        await db._connection.close()
        db._connection = None

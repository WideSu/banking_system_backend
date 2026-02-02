
import aiosqlite
import asyncio
from typing import List
from banking.errors import AccountNotFoundError, InsufficientFundsError, NegativeAmountError

DB_PATH = "banking.db"

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._connection = None
        self._lock = asyncio.Lock()

    async def get_db(self):
        if self.db_path == ":memory:":
            if self._connection is None:
                self._connection = await aiosqlite.connect(self.db_path)
            return self._connection
        return aiosqlite.connect(self.db_path)

    async def init_db(self):
        if self.db_path == ":memory:":
            db = await self.get_db()
            await self._init_tables(db)
        else:
            async with aiosqlite.connect(self.db_path) as db:
                await self._init_tables(db)
                await db.commit()

    async def _init_tables(self, db):
        await db.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                name TEXT PRIMARY KEY,
                balance REAL NOT NULL
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_name TEXT NOT NULL,
                action TEXT NOT NULL,
                amount REAL NOT NULL,
                other_party TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(account_name) REFERENCES accounts(name)
            )
        """)
        await db.commit()
            
    async def reset_db(self):
        if self.db_path == ":memory:":
             db = await self.get_db()
             await db.execute("DROP TABLE IF EXISTS transactions")
             await db.execute("DROP TABLE IF EXISTS accounts")
             await db.commit()
             await self._init_tables(db)
             # Re-init lock for the new test context if needed, 
             # but usually the lock object is reusable if we didn't close it.
             # However, if the loop changed (pytest-asyncio), we MUST create a new lock.
             self._lock = asyncio.Lock()
        else:
             async with aiosqlite.connect(self.db_path) as db:
                await db.execute("DROP TABLE IF EXISTS transactions")
                await db.execute("DROP TABLE IF EXISTS accounts")
                await db.commit()
                await self._init_tables(db)

    async def create_account(self, name: str, initial_balance: float):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        if self.db_path == ":memory:":
             db = await self.get_db()
             try:
                await db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))
                await db.execute("INSERT INTO transactions (account_name, action, amount) VALUES (?, ?, ?)", 
                               (name, "Account created", initial_balance))
                await db.commit()
             except aiosqlite.IntegrityError:
                raise ValueError("Account already exists.")
        else:
            async with aiosqlite.connect(self.db_path) as db:
                try:
                    await db.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))
                    await db.execute("INSERT INTO transactions (account_name, action, amount) VALUES (?, ?, ?)", 
                                   (name, "Account created", initial_balance))
                    await db.commit()
                except aiosqlite.IntegrityError:
                    raise ValueError("Account already exists.")

    async def get_balance(self, name: str) -> float:
        if self.db_path == ":memory:":
            db = await self.get_db()
            async with db.execute("SELECT balance FROM accounts WHERE name = ?", (name,)) as cursor:
                row = await cursor.fetchone()
                if row is None:
                    raise AccountNotFoundError(f"Account '{name}' not found")
                return row[0]
        else:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute("SELECT balance FROM accounts WHERE name = ?", (name,)) as cursor:
                    row = await cursor.fetchone()
                    if row is None:
                        raise AccountNotFoundError(f"Account '{name}' not found")
                    return row[0]

    async def deposit(self, name: str, amount: float):
        if amount <= 0:
            raise NegativeAmountError("Amount must be positive")

        if self.db_path == ":memory:":
            db = await self.get_db()
            async with db.execute("SELECT balance FROM accounts WHERE name = ?", (name,)) as cursor:
                if await cursor.fetchone() is None:
                    raise AccountNotFoundError(f"Account '{name}' not found")

            await db.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, name))
            await db.execute("INSERT INTO transactions (account_name, action, amount) VALUES (?, ?, ?)", 
                           (name, "Deposited", amount))
            await db.commit()
        else:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute("SELECT balance FROM accounts WHERE name = ?", (name,)) as cursor:
                    if await cursor.fetchone() is None:
                        raise AccountNotFoundError(f"Account '{name}' not found")

                await db.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, name))
                await db.execute("INSERT INTO transactions (account_name, action, amount) VALUES (?, ?, ?)", 
                               (name, "Deposited", amount))
                await db.commit()

    async def withdraw(self, name: str, amount: float):
        if amount <= 0:
            raise NegativeAmountError("Amount must be positive")

        if self.db_path == ":memory:":
            db = await self.get_db()
            async with db.execute("SELECT balance FROM accounts WHERE name = ?", (name,)) as cursor:
                row = await cursor.fetchone()
                if row is None:
                    raise AccountNotFoundError(f"Account '{name}' not found")
                balance = row[0]

            if amount > balance:
                raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}; balance is only {balance:.2f}")

            await db.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, name))
            await db.execute("INSERT INTO transactions (account_name, action, amount) VALUES (?, ?, ?)", 
                           (name, "Withdrawn", amount))
            await db.commit()
        else:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute("SELECT balance FROM accounts WHERE name = ?", (name,)) as cursor:
                    row = await cursor.fetchone()
                    if row is None:
                        raise AccountNotFoundError(f"Account '{name}' not found")
                    balance = row[0]

                if amount > balance:
                    raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}; balance is only {balance:.2f}")

                await db.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, name))
                await db.execute("INSERT INTO transactions (account_name, action, amount) VALUES (?, ?, ?)", 
                               (name, "Withdrawn", amount))
                await db.commit()

    async def transfer(self, sender: str, recipient: str, amount: float):
        if amount <= 0:
            raise NegativeAmountError("Amount must be positive")
        if sender == recipient:
            raise ValueError("Cannot transfer to the same account")

        if self.db_path == ":memory:":
            db = await self.get_db()
            
            # Lazy init lock if it doesn't exist (e.g. production first run)
            if self._lock is None:
                self._lock = asyncio.Lock()
                
            async with self._lock:
                try:
                    await db.execute("BEGIN TRANSACTION")
                    
                    async with db.execute("SELECT balance FROM accounts WHERE name = ?", (sender,)) as cursor:
                        row = await cursor.fetchone()
                        if row is None:
                            raise AccountNotFoundError(f"Account '{sender}' not found")
                        sender_balance = row[0]

                    if amount > sender_balance:
                        raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}; balance is only {sender_balance:.2f}")

                    async with db.execute("SELECT 1 FROM accounts WHERE name = ?", (recipient,)) as cursor:
                        if await cursor.fetchone() is None:
                            raise AccountNotFoundError(f"Account '{recipient}' not found")

                    await db.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
                    await db.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, recipient))
                    
                    await db.execute("INSERT INTO transactions (account_name, action, amount, other_party) VALUES (?, ?, ?, ?)", 
                                   (sender, "Transferred to", amount, recipient))
                    await db.execute("INSERT INTO transactions (account_name, action, amount, other_party) VALUES (?, ?, ?, ?)", 
                                   (recipient, "Received from", amount, sender))
                    
                    await db.commit()
                except Exception as e:
                    await db.rollback()
                    raise e
        else:
            async with aiosqlite.connect(self.db_path) as db:
                try:
                    await db.execute("BEGIN TRANSACTION")
                    
                    async with db.execute("SELECT balance FROM accounts WHERE name = ?", (sender,)) as cursor:
                        row = await cursor.fetchone()
                        if row is None:
                            raise AccountNotFoundError(f"Account '{sender}' not found")
                        sender_balance = row[0]

                    if amount > sender_balance:
                        raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}; balance is only {sender_balance:.2f}")

                    async with db.execute("SELECT 1 FROM accounts WHERE name = ?", (recipient,)) as cursor:
                        if await cursor.fetchone() is None:
                            raise AccountNotFoundError(f"Account '{recipient}' not found")

                    await db.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
                    await db.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, recipient))
                    
                    await db.execute("INSERT INTO transactions (account_name, action, amount, other_party) VALUES (?, ?, ?, ?)", 
                                   (sender, "Transferred to", amount, recipient))
                    await db.execute("INSERT INTO transactions (account_name, action, amount, other_party) VALUES (?, ?, ?, ?)", 
                                   (recipient, "Received from", amount, sender))
                    
                    await db.commit()
                except Exception as e:
                    await db.rollback()
                    raise e

    async def get_transaction_history(self, name: str) -> List[str]:
        if self.db_path == ":memory:":
            db = await self.get_db()
            async with db.execute("SELECT 1 FROM accounts WHERE name = ?", (name,)) as cursor:
                if await cursor.fetchone() is None:
                     raise AccountNotFoundError(f"Account '{name}' not found")

            async with db.execute("SELECT action, amount, other_party FROM transactions WHERE account_name = ? ORDER BY timestamp ASC", (name,)) as cursor:
                rows = await cursor.fetchall()
                history = []
                for action, amount, other_party in rows:
                    entry = f"{action}: {amount:.2f}"
                    if other_party:
                        entry += f" {other_party}"
                    history.append(entry)
                return history
        else:
            async with aiosqlite.connect(self.db_path) as db:
                async with db.execute("SELECT 1 FROM accounts WHERE name = ?", (name,)) as cursor:
                    if await cursor.fetchone() is None:
                         raise AccountNotFoundError(f"Account '{name}' not found")

                async with db.execute("SELECT action, amount, other_party FROM transactions WHERE account_name = ? ORDER BY timestamp ASC", (name,)) as cursor:
                    rows = await cursor.fetchall()
                    history = []
                    for action, amount, other_party in rows:
                        entry = f"{action}: {amount:.2f}"
                        if other_party:
                            entry += f" {other_party}"
                        history.append(entry)
                    return history

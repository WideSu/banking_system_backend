from typing import Dict, List
from threading import RLock

from banking.errors import AccountNotFoundError, InsufficientFundsError, NegativeAmountError


class Account:
    def __init__(self, name: str, initial_balance: float):
        self.name = name
        self.balance = initial_balance
        self.transactions: List[str] = [f'Account created with balance: {initial_balance:.2f}']
        self._lock = RLock()  # Add lock

    def deposit(self, amount: float):
        self._validate_positive_amount(amount)
        with self._lock:
            self.balance += amount
            self._record_transaction('Deposited', amount)

    def withdraw(self, amount: float):
        self._validate_positive_amount(amount)
        with self._lock:
            if amount > self.balance:
                raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}; balance is only {self.balance:.2f}")
            self.balance -= amount
            self._record_transaction('Withdrawn', amount)

    def transfer(self, target: 'Account', amount: float):
        if self == target:
            raise ValueError("Cannot transfer to the same account")
        # Lock both accounts to prevent deadlock
        first, second = sorted([self, target], key=lambda x: id(x))
        with first._lock:
            with second._lock:
                self.withdraw(amount)
                target.deposit(amount)
                self._record_transaction('Transferred to', amount, target.name)
                target._record_transaction('Received from', amount, self.name)

    def get_transaction_history(self) -> List[str]:
        return self.transactions.copy()

    def _validate_positive_amount(self, amount: float):
        if amount <= 0:
            raise NegativeAmountError("Amount must be positive")

    def _record_transaction(self, action: str, amount: float, other_party: str = ""):
        transaction = f'{action}: {amount:.2f}'
        if other_party:
            transaction += f' {other_party}'
        self.transactions.append(transaction)


class Bank:
    def __init__(self):
        self.accounts: Dict[str, Account] = {}

    def create_account(self, name: str, initial_balance: float) -> Account:
        if name in self.accounts:
            raise ValueError("Account already exists.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        account = Account(name, initial_balance)
        self.accounts[name] = account
        return account

    def get_account(self, name: str) -> Account:
        account = self.accounts.get(name)
        if account is None:
            raise AccountNotFoundError(f"Account '{name}' not found")
        return account

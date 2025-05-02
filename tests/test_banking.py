import pytest
from banking import Account, Bank, InsufficientFundsError, AccountNotFoundError, NegativeAmountError


# -------- Account Tests --------

def test_account_creation():
    acc = Account("Alice", 100.0)
    assert acc.name == "Alice"
    assert acc.balance == 100.0
    assert "Account created with balance: 100.00" in acc.get_transaction_history()


def test_deposit():
    acc = Account("Bob", 50.0)
    acc.deposit(25.0)
    assert acc.balance == 75.0
    assert "Deposited: 25.00" in acc.get_transaction_history()


def test_withdraw():
    acc = Account("Carol", 100.0)
    acc.withdraw(40.0)
    assert acc.balance == 60.0
    assert "Withdrawn: 40.00" in acc.get_transaction_history()


def test_withdraw_insufficient_funds():
    acc = Account("Dave", 30.0)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(50.0)


def test_negative_deposit():
    acc = Account("Eve", 100.0)
    with pytest.raises(NegativeAmountError):
        acc.deposit(-10.0)


def test_negative_withdraw():
    acc = Account("Frank", 100.0)
    with pytest.raises(NegativeAmountError):
        acc.withdraw(0.0)


def test_transfer_successful():
    acc1 = Account("Alice", 100.0)
    acc2 = Account("Bob", 50.0)
    acc1.transfer(acc2, 25.0)
    assert acc1.balance == 75.0
    assert acc2.balance == 75.0
    assert "Transferred to: 25.00 Bob" in acc1.get_transaction_history()
    assert "Received from: 25.00 Alice" in acc2.get_transaction_history()


def test_transfer_to_self():
    acc = Account("Alice", 100.0)
    with pytest.raises(ValueError):
        acc.transfer(acc, 10.0)


# -------- Bank Tests --------

def test_create_account():
    bank = Bank()
    acc = bank.create_account("Alice", 100.0)
    assert acc.name == "Alice"
    assert acc.balance == 100.0


def test_create_duplicate_account():
    bank = Bank()
    bank.create_account("Bob", 100.0)
    with pytest.raises(ValueError):
        bank.create_account("Bob", 50.0)


def test_create_account_negative_balance():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.create_account("Charlie", -10.0)


def test_get_account_success():
    bank = Bank()
    bank.create_account("Daisy", 200.0)
    acc = bank.get_account("Daisy")
    assert acc.name == "Daisy"


def test_get_account_not_found():
    bank = Bank()
    with pytest.raises(AccountNotFoundError):
        bank.get_account("Ghost")

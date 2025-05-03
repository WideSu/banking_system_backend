import threading
import pytest
from banking.models import Account, Bank
from banking.errors import AccountNotFoundError, InsufficientFundsError, NegativeAmountError
from tests.test_logger import log_test

# ---------- Account Tests ----------
@log_test()
def test_account_creation():
    acc = Account("Alice", 100.0)
    assert acc.name == "Alice"
    assert acc.balance == 100.0
    assert acc.get_transaction_history() == ["Account created with balance: 100.00"]

@log_test()
def test_deposit_valid():
    acc = Account("Bob", 50.0)
    acc.deposit(25.0)
    assert acc.balance == 75.0
    assert "Deposited: 25.00" in acc.get_transaction_history()

@log_test()
def test_deposit_negative():
    acc = Account("Carol", 30.0)
    with pytest.raises(NegativeAmountError):
        acc.deposit(-5)

@log_test()
def test_withdraw_valid():
    acc = Account("Daisy", 100.0)
    acc.withdraw(60.0)
    assert acc.balance == 40.0
    assert "Withdrawn: 60.00" in acc.get_transaction_history()

@log_test()
def test_withdraw_insufficient():
    acc = Account("Eve", 20.0)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(30.0)

@log_test()
def test_withdraw_negative():
    acc = Account("Frank", 100.0)
    with pytest.raises(NegativeAmountError):
        acc.withdraw(0)

@log_test()
def test_transfer_successful():
    acc1 = Account("Gina", 200.0)
    acc2 = Account("Harry", 100.0)
    acc1.transfer(acc2, 50.0)
    assert acc1.balance == 150.0
    assert acc2.balance == 150.0
    assert "Transferred to: 50.00 Harry" in acc1.get_transaction_history()
    assert "Received from: 50.00 Gina" in acc2.get_transaction_history()

@log_test()
def test_transfer_to_self():
    acc = Account("Ivan", 100.0)
    with pytest.raises(ValueError):
        acc.transfer(acc, 10.0)

@log_test()
def test_transaction_history_is_copy():
    acc = Account("Jack", 100.0)
    history = acc.get_transaction_history()
    history.append("Fake transaction")
    assert "Fake transaction" not in acc.get_transaction_history()


# ---------- Bank Tests ----------
@log_test()
def test_bank_create_account_success():
    bank = Bank()
    acc = bank.create_account("Kate", 300.0)
    assert acc.name == "Kate"
    assert acc.balance == 300.0

@log_test()
def test_bank_create_account_duplicate():
    bank = Bank()
    bank.create_account("Leo", 150.0)
    with pytest.raises(ValueError):
        bank.create_account("Leo", 200.0)

@log_test()
def test_bank_create_account_negative_initial():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.create_account("Mona", -10.0)

@log_test()
def test_get_account_success():
    bank = Bank()
    bank.create_account("Nina", 400.0)
    acc = bank.get_account("Nina")
    assert acc.name == "Nina"

@log_test()
def test_get_account_not_found():
    bank = Bank()
    with pytest.raises(AccountNotFoundError):
        bank.get_account("Oscar")


# ---------- Concurrency Test ----------
@log_test()
def test_concurrent_transfer_does_not_deadlock():
    acc1 = Account("Penny", 1000.0)
    acc2 = Account("Quinn", 1000.0)

    def transfer_loop(from_acc, to_acc):
        for _ in range(100):
            try:
                from_acc.transfer(to_acc, 1.0)
            except InsufficientFundsError:
                pass

    t1 = threading.Thread(target=transfer_loop, args=(acc1, acc2))
    t2 = threading.Thread(target=transfer_loop, args=(acc2, acc1))

    t1.start()
    t2.start()
    t1.join(timeout=5)
    t2.join(timeout=5)

    assert not t1.is_alive() and not t2.is_alive(), "Deadlock detected"
    assert abs(acc1.balance + acc2.balance - 2000.0) < 0.001

import pytest
from banking.models import Account, Bank, InsufficientFundsError, AccountNotFoundError, NegativeAmountError

# -------- Logging --------
import logging, time
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def log_test(enable_time_logging=True, level=logging.INFO):
    """Decorator factory that accepts parameters"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Start timer if time logging is enabled
            start_time = time.time() if enable_time_logging else None
            
            # Log test start
            logger.log(level, f"🚀 Starting test: {func.__name__}")
            
            try:
                result = func(*args, **kwargs)
                
                # Log test completion
                if enable_time_logging:
                    duration = time.time() - start_time
                    logger.log(level, f"✅ Test passed in {duration:.4f}s: {func.__name__}")
                else:
                    logger.log(level, f"✅ Test passed: {func.__name__}")
                
                return result
            except Exception as e:
                if enable_time_logging:
                    duration = time.time() - start_time
                    logger.error(f"❌ Test failed after {duration:.4f}s: {func.__name__} - {str(e)}")
                else:
                    logger.error(f"❌ Test failed: {func.__name__} - {str(e)}")
                raise
        return wrapper
    return decorator

# -------- Account Tests --------
@log_test()
def test_account_creation():
    acc = Account("Alice", 100.0)
    assert acc.name == "Alice"
    assert acc.balance == 100.0
    assert "Account created with balance: 100.00" in acc.get_transaction_history()

@log_test()
def test_deposit():
    acc = Account("Bob", 50.0)
    acc.deposit(25.0)
    assert acc.balance == 75.0
    assert "Deposited: 25.00" in acc.get_transaction_history()

@log_test()
def test_withdraw():
    acc = Account("Carol", 100.0)
    acc.withdraw(40.0)
    assert acc.balance == 60.0
    assert "Withdrawn: 40.00" in acc.get_transaction_history()

@log_test()
def test_withdraw_insufficient_funds():
    acc = Account("Dave", 30.0)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(50.0)

@log_test()
def test_negative_deposit():
    acc = Account("Eve", 100.0)
    with pytest.raises(NegativeAmountError):
        acc.deposit(-10.0)

@log_test()
def test_negative_withdraw():
    acc = Account("Frank", 100.0)
    with pytest.raises(NegativeAmountError):
        acc.withdraw(0.0)

@log_test()
def test_transfer_successful():
    acc1 = Account("Alice", 100.0)
    acc2 = Account("Bob", 50.0)
    acc1.transfer(acc2, 25.0)
    assert acc1.balance == 75.0
    assert acc2.balance == 75.0
    assert "Transferred to: 25.00 Bob" in acc1.get_transaction_history()
    assert "Received from: 25.00 Alice" in acc2.get_transaction_history()

@log_test()
def test_transfer_to_self():
    acc = Account("Alice", 100.0)
    with pytest.raises(ValueError):
        acc.transfer(acc, 10.0)


# -------- Bank Tests --------
@log_test()
def test_create_account():
    bank = Bank()
    acc = bank.create_account("Alice", 100.0)
    assert acc.name == "Alice"
    assert acc.balance == 100.0

@log_test()
def test_create_duplicate_account():
    bank = Bank()
    bank.create_account("Bob", 100.0)
    with pytest.raises(ValueError):
        bank.create_account("Bob", 50.0)

@log_test()
def test_create_account_negative_balance():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.create_account("Charlie", -10.0)

@log_test()
def test_get_account_success():
    bank = Bank()
    bank.create_account("Daisy", 200.0)
    acc = bank.get_account("Daisy")
    assert acc.name == "Daisy"

@log_test()
def test_get_account_not_found():
    bank = Bank()
    with pytest.raises(AccountNotFoundError):
        bank.get_account("Ghost")

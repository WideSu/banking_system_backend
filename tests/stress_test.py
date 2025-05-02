from pathlib import Path
import time,os,sys
import random
# Ensure package root is in path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from banking.core import Account, Bank

def stress_test(num_transactions=1000):
    """Run performance test with given transaction count"""
    bank = Bank()
    
    # Create test accounts
    accounts = [
        bank.create_account(f"User{i}", 1_000_000)
        for i in range(10)  # 10 test accounts
    ]
    
    start_time = time.perf_counter()
    
    # Execute transactions
    for _ in range(num_transactions):
        from_acc = random.choice(accounts)
        to_acc = random.choice(accounts)
        amount = random.randint(1, 1000)
        
        try:
            from_acc.transfer(to_acc, amount)
        except Exception:
            pass  # Ignore errors for stress testing
    
    duration = time.perf_counter() - start_time
    return duration, num_transactions

def run_test_suite():
    test_cases = [1000, 2000, 3000, 5000, 10000]
    print(f"{'Transactions':>12} | {'Time (s)':<10} | {'Txn/s':<10}")
    print("-" * 45)
    
    for n in test_cases:
        duration, count = stress_test(n)
        txn_rate = count / duration
        print(f"{n:>12,} | {duration:<10.4f} | {txn_rate:<10.2f}")

if __name__ == "__main__":
    run_test_suite()
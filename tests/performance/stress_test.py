import time
import random
import tracemalloc  # To track memory usage
import sys
import os

# Add the project root to sys.path so we can import 'banking'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from banking.models import Bank

def stress_test(num_transactions=1000):
    """Run performance test with given transaction count"""
    bank = Bank()
    
    # Create test accounts
    accounts = [
        bank.create_account(f"User{i}", 1_000_000)
        for i in range(10)  # 10 test accounts
    ]
    
    tracemalloc.start()
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
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Convert memory usage from bytes to MB
    return duration, num_transactions, current / 1024 / 1024, peak / 1024 / 1024

def run_test_suite():
    test_cases = [1000, 2000, 3000, 5000]
    print(f"{'Transactions':>12} | {'Time (s)':<10} | {'Txn/s':<10} | {'Peak MB':<10}")
    print("-" * 75)
    
    for n in test_cases:
        duration, count, current_mb, peak_mb = stress_test(n)
        txn_rate = count / duration
        print(f"{n:>12,} | {duration:<10.4f} | {txn_rate:<10.2f} | {current_mb:<12.2f} | {peak_mb:<10.2f}")

if __name__ == "__main__":
    run_test_suite()
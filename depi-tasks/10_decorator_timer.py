"""
Task: Python Decorators - Pipeline Performance Logger

Build a reusable decorator that measures and logs function execution time:
1. Define a decorator log_execution_time that wraps any function.
2. Record the start timestamp using time.time().
3. Execute the function using *args and **kwargs to support any arguments.
4. Calculate elapsed duration and print the function name dynamically.
5. Return the original function result.
"""

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"⏱️ Task '{func.__name__}' finished in {elapsed:.2f} seconds.")
        return result
    return wrapper

@log_execution_time
def extract_job_postings(source_name, count):
    print(f"Fetching {count} jobs from {source_name}...")
    time.sleep(1.5)  # Simulating network latency
    return [f"Job_{i}" for i in range(count)]

if __name__ == "__main__":
    extract_job_postings("Adzuna", 5)

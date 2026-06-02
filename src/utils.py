import time
from src.black_scholes import black_scholes_call
# python -m src.utils

#What to include in utils.py
#1. absolute error (black_scholes - monte carlo)
#2. percent error (absolute error / black_scholes) * 100
#3. runtime measurement
#4. currency formatting (for app polish)
#5. format percent value
#can use lambda for 4 and 5

def measure_runtime(function_to_time, *args, **kwargs):
    start_time = time.perf_counter()
    result = function_to_time(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Function runtime: {execution_time:.6f} seconds")
    return result, execution_time

#temporary test cases
if __name__ == "__main__":

    result, runtime = measure_runtime(
        black_scholes_call,
        100, 100, 1, 0.05, 0.2
    )
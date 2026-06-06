import time
from src.black_scholes import black_scholes_call, black_scholes_put, black_scholes_price
from src.monte_carlo import monte_carlo_price
from src.gbm import generate_gbm_paths
# python -m src.utils

#What to include in utils.py
#1. absolute error (black_scholes - monte carlo)
#2. percent error (absolute error / black_scholes) * 100
#3. runtime measurement
#4. currency formatting (for app polish)
#5. format percent value
#can use lambda for 4 and 5

#work on next: absolute error = |Black-Scholes price - Monte Carlo price|

def measure_runtime(function_to_time, *args, **kwargs):
    start_time = time.perf_counter()
    result = function_to_time(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Function runtime: {execution_time:.6f} seconds")
    return result, execution_time

def absolute_error(S, K, T, r, sigma, N, option_type):
    bs_price = black_scholes_price(S, K, T, r, sigma, option_type)
    mc_price = monte_carlo_price(S, K, T, r, sigma, N, option_type)
    abs_error = abs(bs_price - mc_price)
    return abs_error

#temporary test cases
if __name__ == "__main__":
    #Testing a simple, addition function
    print("testing add_multiple function")
    def add_multiple(*args):
        return sum(args)
    result, execution_time = measure_runtime(add_multiple, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(result)

    print("testing black_scholes_call runtime")
    result, execution_time = measure_runtime(
        black_scholes_call,
        100, 100, 1, 0.05, 0.2
    )
    print(result)

    print("testing black_scholes_put runtime")
    result, execution_time = measure_runtime(
        black_scholes_put,
        100, 100, 1, 0.05, 0.2
    )
    print(result)

    print("testing monte_carlo_price for put")
    result, execution_time = measure_runtime(
        monte_carlo_price, 50, 50, 9/12, 0.04, 0.30, 100, "put"
    )
    print(result)

    print("testing monte_carlo_price for call")
    result, execution_time = measure_runtime(
        monte_carlo_price, 50, 50, 9/12, 0.04, 0.30, 100, "call"
    )
    print(result)

    print("testing generate_gbm_paths")
    result, execution_time = measure_runtime(
        generate_gbm_paths, 100, 1, 0.04, 0.05, 252, 10, seed=42
    )
    print(result)
    print("\ntesting absolute error function:")
    print(absolute_error(110, 100, 1, 0.04, 0.05, 10, "call"))
    print(absolute_error(100, 10, 1, 0.05, 0.05, 10000, "call"))
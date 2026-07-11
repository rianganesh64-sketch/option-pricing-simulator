import time
from src.black_scholes import black_scholes_call, black_scholes_put, black_scholes_price
from src.monte_carlo import monte_carlo_price
from src.gbm import generate_gbm_paths


#5. format percent value

def measure_runtime(function_to_time, *args, **kwargs):
    start_time = time.perf_counter()
    result = function_to_time(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"Function runtime: {execution_time:.6f} seconds")
    return result, execution_time

def absolute_error(price_1, price_2):
    abs_error = abs(price_1 - price_2)
    return abs_error

def percent_error(reference, experimental):
    if reference == 0:
        return float("inf")
    else:
        per_error = ((experimental - reference)/reference) * 100
    return per_error

def format_currency(c):
    formatted = "$" + (f"{c:,.2f}")
    return formatted
def format_percent(p):
    formatted = (f"{p:.2f}") + "%"
    return formatted

#temporary test cases
if __name__ == "__main__":
    #Testing a simple, addition function
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
        monte_carlo_price, 50, 50, 9/12, 0.04, 0.30, 1000, "put"
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
    print("\n testing percent error function:")
    print(percent_error(110, 100, 1, 0.04, 0.05, 10, "call"))
    print(percent_error(110, 100, 1, 0.04, 0.05, 10000, "call"))
    print("\ntesting format_currency function")
    print(format_currency(10.4732932883209342))
    print(format_currency(black_scholes_price(100, 110, 1, 0.04, 0.04, "call")))
    print("\ntest format_percent")
    print(format_percent(19.2321212))
    print(format_percent(percent_error(110, 100, 1, 0.04, 0.05, 100, "call")))
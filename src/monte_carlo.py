import numpy as np

def validate_inputs(S, K, T, r, sigma, N):
    """Validates the given inputs for the Monte Carlo simulation, raises a ValueError if needed
    Can be easily used in other functions to validate inputs"""
    if S <= 0:
        raise ValueError("S (initial stock price) must be positive")
    if K <= 0:
        raise ValueError('K (strike price) must be positive')
    if T <= 0:
        raise ValueError ('T (time to maturity (in years)) must be positive')
    if r < 0:
        raise ValueError ('r (risk free interest rate) cannot be negative')
    if sigma <= 0:
        raise ValueError ('sigma (base volatility) must be positive')
    if N % 1 != 0:
        raise ValueError('N (number of simulations) must be a whole number')
    if N <= 0:
        raise ValueError ('N (number of simulations) must be positive')

def simulate_final_prices(S, K, T, r, sigma, N):
    """Uses Geometric Brownian Motion and random standard normal shocks to simulate N possible future stock prices."""
    validate_inputs(S, K, T, r, sigma, N)

    rng = np.random.default_rng(seed=42)
    z_values = rng.standard_normal(N)

    final_prices = S * np.exp(
        (r - (0.5 * (sigma ** 2)))*T
        + (sigma * (np.sqrt(T)) * z_values))
    return(final_prices)

def call_payoffs(S, K, T, r, sigma, N):
    """Calculates the call option payoffs for the simulated stock prices"""
    validate_inputs(S, K, T, r, sigma, N)
    simulated_prices = simulate_final_prices(S, K, T, r, sigma, N)
    call_payoff_values = np.maximum(simulated_prices - K, 0)
    return(call_payoff_values)

def put_payoffs(S, K, T, r, sigma, N):
    """Calculates the put option payoffs for the simulated stock prices"""
    validate_inputs(S, K, T, r, sigma, N)
    simulated_prices = simulate_final_prices(S, K, T, r, sigma, N)
    put_payoff_values = np.maximum(K - simulated_prices, 0)
    return(put_payoff_values)

def monte_carlo_call(S, K, T, r, sigma, N):
    """Discounts the payoff for call options back to the present for a better estimate of value"""
    validate_inputs(S, K, T, r, sigma, N)
    simulated_payoffs = call_payoffs(S, K, T, r, sigma, N)
    average_payoff = np.mean(simulated_payoffs)
    price = average_payoff * np.exp(-r * T)
    return(price)

def monte_carlo_put(S, K, T, r, sigma, N):
    """Discounts the payoff for put options back to the present for a better estimate of value"""
    validate_inputs(S, K, T, r, sigma, N)
    simulated_payoffs = put_payoffs(S, K, T, r, sigma, N)
    average_payoff = np.mean(simulated_payoffs)
    price = average_payoff * np.exp(-r * T)
    return(price)

def monte_carlo_price(S, K, T, r, sigma, N, option_type):
    validate_inputs(S, K, T, r, sigma, N)
    """A container function for the monte_carlo_put and monte_carlo_call functions, returns the correct output based on option_type"""
    if option_type not in ["call", "put"]:
        raise ValueError("Option type must be either 'call' or 'put'")
    elif option_type == "call":
        return(monte_carlo_call(S, K, T, r, sigma, N))
    else:
        return(monte_carlo_put(S, K, T, r, sigma, N))

def standard_error(S, K, T, r, sigma, N, option_type):
    """Calculates the standard error of the Monte Carlo simulation."""
    validate_inputs(S, K, T, r, sigma, N)
    if option_type not in ["call", "put"]:
        raise ValueError("Option type must be either 'call' or 'put'")
    elif option_type == "put":
        payoff = put_payoffs(S, K, T, r, sigma, N)
    else:
        payoff = call_payoffs(S, K, T, r, sigma, N)
    error = np.std(payoff, ddof = 1) / np.sqrt(len(payoff)) # uses sample standard deviation formula, ddof = 1
    return(error)

if __name__ == "__main__":
    # Initial Test Parameters
    S = 50 # Initial stock price
    K = 50 # Strike price
    T = 9 / 12 # Time to maturity in years
    r = 0.04 # Risk free interest rate
    sigma = 0.30 # base volatility
    N = 1000 # Number of simulations
    final_prices = simulate_final_prices(S, K, T, r, sigma, N)
    print("Final prices from GBM")
    print(final_prices[:5])
    print(np.mean(final_prices))
    print(np.max(final_prices))
    print(np.min(final_prices))
    print("Payoffs for call options")
    call_option_payoffs = call_payoffs(S, K, T, r, sigma, N)
    print(call_option_payoffs[:5])
    print(np.mean(call_option_payoffs))
    print(np.max(call_option_payoffs))
    print(np.min(call_option_payoffs))
    print("Payoffs for put options")
    put_option_payoffs = put_payoffs(S, K, T, r, sigma, N)
    print(put_option_payoffs[:5])
    print(np.mean(put_option_payoffs))
    print(np.max(put_option_payoffs))
    print(np.min(put_option_payoffs))
    print("Monte Carlo call payoff")
    call_monte_carlo = monte_carlo_call(S, K, T, r, sigma, N)
    print(call_monte_carlo)
    print("Monte Carlo put payoff")
    call_monte_carlo = monte_carlo_put(S, K, T, r, sigma, N)
    print(call_monte_carlo)
    print("Full Monte Carlo Function Call")
    monte_carlo_call_price = monte_carlo_price(S, K, T, r, sigma, N, "call")
    print(monte_carlo_call_price)
    print("Full Monte Carlo Function Put")
    monte_carlo_put_price = monte_carlo_price(S, K, T, r, sigma, N, "put")
    print(monte_carlo_put_price)
    print("Standard Error Calculations")
    std_error_put = standard_error(S, K, T, r, sigma, N, "put")
    std_error_call = standard_error(S, K, T, r, sigma, N, "call")
    print(std_error_put)
    print(std_error_call)
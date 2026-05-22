import numpy as np

# 1. validate_inputs(...)
#    Makes sure S, K, T, sigma, and N are valid.

# 2. simulate_final_prices(...)
#    Generates N random Z values.
#    Uses GBM to produce N possible final stock prices.

# 3. call_payoffs(...) / put_payoffs(...)
#    Converts simulated stock prices into option payoffs.

# 4. monte_carlo_call(...) / monte_carlo_put(...)
#    Averages the payoffs and discounts them back to present value.

# 5. standard_error(...)
#    Measures how noisy/uncertain the Monte Carlo estimate is.

def validate_inputs(S, K, T, r, sigma, N):
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
    validate_inputs(S, K, T, r, sigma, N)

    rng = np.random.default_rng(seed=42)
    z_values = rng.standard_normal(N)

    final_prices = S * np.exp(
        (r - (0.5 * (sigma ** 2)))*T
        + (sigma * (np.sqrt(T)) * z_values))
    return(final_prices)

def call_payoffs(S, K, T, r, sigma, N):
    validate_inputs(S, K, T, r, sigma, N)
    simulated_prices = simulate_final_prices(S, K, T, r, sigma, N)
    call_payoff_values = np.maximum(simulated_prices - K, 0)
    return(call_payoff_values)

def put_payoffs(S, K, T, r, sigma, N):
    validate_inputs(S, K, T, r, sigma, N)
    simulated_prices = simulate_final_prices(S, K, T, r, sigma, N)
    put_payoff_values = np.maximum(K - simulated_prices, 0)
    return(put_payoff_values)

def monte_carlo_call(S, K, T, r, sigma, N):
    validate_inputs(S, K, T, r, sigma, N)
    simulated_payoffs = call_payoffs(S, K, T, r, sigma, N)
    average_payoff = np.mean(simulated_payoffs)
    price = average_payoff * np.exp(-r * T)
    return(price)

def monte_carlo_put(S, K, T, r, sigma, N):
    validate_inputs(S, K, T, r, sigma, N)
    simulated_payoffs = put_payoffs(S, K, T, r, sigma, N)
    average_payoff = np.mean(simulated_payoffs)
    price = average_payoff * np.exp(-r * T)
    return(price)

def monte_carlo_prices(S, K, T, r, sigma, N, option_type):
    if option_type not in ["call", "put"]:
        raise ValueError("Option type must be either 'call' or 'put'")
    elif option_type == "call":
        return(monte_carlo_call(S, K, T, r, sigma, N))
    else:
        return(monte_carlo_put(S, K, T, r, sigma, N))

def error(S, K, T, r, sigma, N):
    validate_inputs(S, K, T, r, sigma, N)
    results = simulate_final_prices(S, K, T, r, sigma, N)
    standard_error = np.std(results) / np.sqrt(len(results))
    return(standard_error)

if __name__ == "__main__":
    # Initial Test Parameters
    S = 50 # Initial stock price
    K = 50 # Strike price
    T = 9 / 12 # Time to maturity in years
    r = 0.04 # Risk free interest rate
    sigma = 0.30 # base volatility
    N = 10000000 # Number of simulations
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
    monte_carlo_call_price = monte_carlo_prices(S, K, T, r, sigma, N, "call")
    print(monte_carlo_call_price)
    print("Full Monte Carlo Function Put")
    monte_carlo_put_price = monte_carlo_prices(S, K, T, r, sigma, N, "put")
    print(monte_carlo_put_price)
    print("Standard Error Calculations")
    std_error = error(S, K, T, r, sigma, N)
    print(std_error)
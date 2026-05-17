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

# Initial Test Parameters
S = 50 # Initial stock price
K = 50 # Strike price
T = 9 / 12 # Time to maturity in years
r = 0.04 # Risk free interest rate
sigma = 0.30 # base volatility
N = 1000 # Number of simulations

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


    




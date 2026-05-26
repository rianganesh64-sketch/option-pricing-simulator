import numpy as np

#Current testing variables
S = 100 #starting stock price
T = 1 #total time period
r = 0.04 #risk free rate, inputted into drift
sigma = 0.05 #volatility
steps = 252 #number of time steps, 252 trading days in a year
num_paths = 10 #number of paths to generate

def validate_gbm_inputs(S, T, r, sigma, steps, num_paths):
    "Validates the given inputs for the GBM stock prices, raises a ValueError if needed"
    if S <= 0:
        raise ValueError("S (initial stock price) must be positive")
    if T <= 0:
        raise ValueError ('T (time to maturity (in years)) must be positive')
    if r < 0:
        raise ValueError ('r (risk free interest rate) cannot be negative')
    if sigma <= 0:
        raise ValueError ('sigma (base volatility) must be positive')
    if not isinstance(steps, int) or steps <= 0:
        raise ValueError('Steps must be an positive integer')
    if steps <= 0:
        raise ValueError('Steps must be positive')
    if not isinstance(num_paths, int) or num_paths <= 0:
        raise ValueError('num_paths must be a positive integer')
    


def generate_gbm_path(S, T, r, sigma, steps, num_paths, seed=42):
    validate_gbm_inputs(S, T, r, sigma, steps, num_paths)
    rng = np.random.default_rng(seed)
    z_value = rng.standard_normal()

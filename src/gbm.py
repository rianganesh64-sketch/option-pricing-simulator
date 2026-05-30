import numpy as np


def validate_gbm_path_inputs(S, T, r, sigma, steps):
    """Validates the given inputs for the GBM stock prices, raises a ValueError if needed, ONE PATH"""
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

def validate_gbm_paths_inputs(S, T, r, sigma, steps, num_paths):
    """Validates the given inputs for the GBM stock prices, raises a ValueError if needed, MULTIPLE PATHS """
    validate_gbm_path_inputs(S, T, r, sigma, steps)
    if not isinstance(num_paths, int) or num_paths <= 0:
        raise ValueError('num_paths must be a positive integer')

def generate_gbm_path(S, T, r, sigma, steps, seed=42):
    """Generate a singular GBM path, with specific step intervals. Used for visualization."""
    validate_gbm_path_inputs(S, T, r, sigma, steps)
    rng = np.random.default_rng(seed)
    dt = T / steps
    path = [S]
    current_price = S
    for i in range(steps):
        z_value = rng.standard_normal()
        drift = (r - (0.5 * (sigma ** 2))) * dt
        shock = sigma * np.sqrt(dt) * z_value
        growth_factor = np.exp(drift + shock)
        next_price = current_price * growth_factor
        current_price = next_price
        path.append(current_price)
    return path

def generate_gbm_paths(S, T, r, sigma, steps, num_paths, seed=42):
    """Generates num_paths number of parts with GBM, and specific step intervals. Used for visualization"""
    validate_gbm_paths_inputs(S, T, r, sigma, steps, num_paths)
    all_paths = []
    for i in range(num_paths):
        single_path = generate_gbm_path(S, T, r, sigma, steps, seed + i)
        all_paths.append(single_path)
    return all_paths

if __name__ == "__main__":
    #Current testing variables
    S = 100 #starting stock price
    T = 1 #total time period
    r = 0.04 #risk free rate, inputted into drift
    sigma = 0.05 #volatility
    steps = 252 #number of time steps, 252 trading days in a year
    num_paths = 10 #number of paths to generate
    print("Single path")
    print(generate_gbm_path(S, T, r, sigma, steps, seed=42))
    print("Multiple paths")
    print(generate_gbm_paths(S, T, r, sigma, num_paths, steps, seed=42))
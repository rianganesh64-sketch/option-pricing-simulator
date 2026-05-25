import pytest
from src.monte_carlo import validate_inputs, simulate_final_prices, call_payoffs, put_payoffs, monte_carlo_price, standard_error
import numpy as np
#to test, run python -m pytest tests/test_monte_carlo.py


#Global Variables
S = 20
K = 25
T = 5
r = 0.05
sigma = 0.04
N = 100

def test_validate_inputs():
    validate_inputs(20, 25, 5, 0.05, 0.04, 10)
    validate_inputs(20, 25, 5, 0, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(0, 25, 5, 0.05, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(-5, 25, 5, 0.05, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 0, 5, 0.05, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, -10, 5, 0.05, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 0, 0.05, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, -5, 0.05, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 5, -4, 0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 5, 0.05, 0, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 5, 0.05, -0.04, 10)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 5, 0.05, 0.04, 10.5)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 5, 0.05, 0.04, 0)
    with pytest.raises(ValueError):
        validate_inputs(20, 25, 5, 0.05, 0.04, -10)

def test_simulate_final_prices():
    final_prices = simulate_final_prices(S, K, T, r, sigma, N)
    assert len(final_prices) == N
    assert np.all((final_prices) > 0)

def test_call_payoffs():
    final_prices = simulate_final_prices(S, K, T, r, sigma, N)
    payoffs_call = call_payoffs(S, K, T, r, sigma, N)
    assert np.all(payoffs_call >= 0)
    assert np.all(payoffs_call[final_prices > K] > 0)
    assert np.all(payoffs_call[final_prices <= K] == 0)

def test_put_payoffs():
    final_prices = simulate_final_prices(S, K, T, r, sigma, N)
    payoffs_put = put_payoffs(S, K, T, r, sigma, N)
    assert np.all(payoffs_put >= 0)
    assert np.all(payoffs_put[final_prices < K] > 0)
    assert np.all(payoffs_put[final_prices >= K] == 0)

def test_monte_carlo_price():
    call_payoff = call_payoffs(S, K, T, r, sigma, N)
    put_payoff = put_payoffs(S, K, T, r, sigma, N)
    with pytest.raises(ValueError):
        monte_carlo_price(S, K, T, r, sigma, N, "calendar")
    assert monte_carlo_price(S, K, T, r, sigma, N, "call") > 0
    assert monte_carlo_price(S, K, T, r, sigma, N, "put") > 0
    call_price = monte_carlo_price(S, K, T, r, sigma, N, "call")
    expected_call_price = np.mean(call_payoff) * np.exp(-r * T)
    assert round(call_price, 10) == round(expected_call_price, 10)
    put_price = monte_carlo_price(S, K, T, r, sigma, N, "put")
    expected_put_price = np.mean(put_payoff) * np.exp(-r * T)
    assert round(put_price, 10) == round(expected_put_price, 10)

def test_standard_error():
    call_error = standard_error(S, K, T, r, sigma, N, "call")
    assert call_error >= 0
    put_error = standard_error(S, K, T, r, sigma, N, "put")
    assert put_error >= 0
    larger_n = 1000
    smaller_n = 200
    assert standard_error(S, K, T, r, sigma, larger_n, "call") < standard_error(S, K, T, r, sigma, smaller_n, "call")
    assert standard_error(S, K, T, r, sigma, larger_n, "put") < standard_error(S, K, T, r, sigma, smaller_n, "put")
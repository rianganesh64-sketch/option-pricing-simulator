import pytest
from src.black_scholes import d_one, d_two, black_scholes_call, black_scholes_put
import numpy as np
#to test, run python -m pytest tests/test_black_scholes.py

def test_d_one():
    assert round(d_one(100, 100, 1.0, 0.05, 0.2), 2) == 0.35 # At-the-Money
    assert round(d_one(110, 100, 0.5, 0.3, 0.25), 2) == 1.48 # In-the-Money
    assert round(d_one(90, 100, 0.25, 0.02, 0.3), 2) == -0.59 # Out-of-the-Money
    with pytest.raises(ValueError):
        d_one(0, 100, 1, 0.05, 0.2) # S = 0
    with pytest.raises(ValueError):
        d_one(100, 100, 1, 0.05, 0) # Sigma = 0
    with pytest.raises(ValueError):
        d_one(100, 100, 0, 0.05, 0.2) # t = 0

def test_d_two(): #don't need to check value erors as d_two is dependent on d_one
    assert round(d_two(100, 100, 1.0, 0.05, 0.2), 2) == 0.15 # At-the-Money
    assert round(d_two(110, 100, 0.5, 0.3, 0.25), 2) == 1.30 #In-the-Money
    assert round(d_two(90, 100, 0.25, 0.02, 0.3), 2) == -0.74 #Out-of-the-Money

def test_black_scholes_call(): #rigorously checking the public facing function
    assert round(black_scholes_call(100, 100, 1, 0.05, 0.2), 2) == 10.45 #At-the-Money
    assert round(black_scholes_call(120, 100, 1, 0.05, 0.02), 2) == 24.88 #In-the-Money
    assert round(black_scholes_call(80, 100, 1, 0.05, 0.2), 2) == 1.86 #Out-of-the-Money
    assert round(black_scholes_call(100, 100, 1, 0.05, 0.8), 2) == 32.82 #Very high volatility
    assert round(black_scholes_call(100, 100, 1, 0.05, 0.01), 2) == 4.88 #Low volatility
    assert round(black_scholes_call(100, 100, 0.01, 0.05, 0.2), 2) == 0.82 #Near expiration
    assert round(black_scholes_call(100, 100, 10, 0.05, 0.2), 2) == 45.19 #Longer time period
    assert black_scholes_call(100, 100, 10, 0.05, 0.2) < black_scholes_call(100, 100, 10, 0.05, 0.5) #An option with higher volatility will be valued more
    assert black_scholes_call(90, 100, 10, 0.05, 0.2) < black_scholes_call(110, 100, 10, 0.05, 0.2) #Higher stock price increased call price
    with pytest.raises(ValueError):
        black_scholes_call(0, 100, 1, 0.05, 0.2) # S = 0
    with pytest.raises(ValueError):
        black_scholes_call(100, 100, 1, 0.05, 0) # Sigma = 0
    with pytest.raises(ValueError):
        black_scholes_call(100, 100, 0, 0.05, 0.2) # t = 0

def test_black_scholes_put():
    assert round(black_scholes_put(100, 100, 1, 0.05, 0.2), 2) == 5.57 #At-the-money
    assert round(black_scholes_put(80, 100, 1, 0.05, 0.2), 2) == 16.98 #In-the-money
    assert round(black_scholes_put(120, 100, 1, 0.05, 0.2), 2) == 1.29 #Out-of-the-money
    assert round(black_scholes_put(100, 100, 1, 0.05, 0.8), 2) == 27.94 #High volatility
    assert round(black_scholes_put(100, 100, 1, 0.05, 0.01), 2) == 0.00 #Low volatility makes the put option essential worthless
    assert round(black_scholes_put(100, 100, 0.01, 0.05, 0.2), 2) == 0.77 #Near expiration, not worth much
    assert round(black_scholes_put(100, 100, 10, 0.05, 0.2), 2) == 5.85 #Lots of time, worth more
    assert round(black_scholes_put(120, 100, 5, 0.05, 0.8), 2) > round(black_scholes_put(120, 100, 5, 0.05, 0.2), 2) #higher volatility makes it worth more
    assert round(black_scholes_put(120, 100, 5, 0.05, 0.2), 2) > round(black_scholes_put(150, 100, 5, 0.05, 0.2), 2) #lower stock price makes it worth more
    assert round(black_scholes_put(120, 115, 5, 0.05, 0.2), 2) > round(black_scholes_put(120, 90, 5, 0.05, 0.2), 2) #higher strike price increases worth
    with pytest.raises(ValueError):
        black_scholes_put(0, 100, 1, 0.05, 0.2) # S = 0
    with pytest.raises(ValueError):
        black_scholes_put(100, 100, 1, 0.05, 0) # Sigma = 0
    with pytest.raises(ValueError):
        black_scholes_put(100, 100, 0, 0.05, 0.2) # t = 0
    with pytest.raises(ValueError):
        black_scholes_put(100, 0, 1, 0.05, 0.2) # K = 0
    with pytest.raises(ValueError):
        black_scholes_put(100, 100, 1, 0.05, -0.4) # Negative sigma

def test_put_call_parity():
    assert round(black_scholes_call(100, 100, 1, 0.05, 0.2) - black_scholes_put(100, 100, 1, 0.05, 0.2), 2) == round(100 - 100 * np.exp(-0.05 * 1), 2)
    # This checks the put_call_parity with Black-Scholes, a foundational principle in options pricing theory
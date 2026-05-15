import pytest
from src.black_scholes import d_one, d_two, black_scholes_call, black_scholes_put
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
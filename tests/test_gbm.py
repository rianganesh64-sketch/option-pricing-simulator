import pytest
from src.gbm import validate_gbm_path_inputs, validate_gbm_paths_inputs, generate_gbm_path, generate_gbm_paths
#to test, run python -m pytest tests/test_gbm.py
    
def test_validate_gbm_path_inputs():
    validate_gbm_path_inputs(20, 1, 0.4, 0.5, 300)
    validate_gbm_path_inputs(20, 1, 0, 0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(0, 1, 0.4, 0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(-50, 1, 0.4, 0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, 0, 0.4, 0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, -5, 0.4, 0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, 1, -0.4, 0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, 1, 0.4, -0.5, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, 1, 0.4, 0, 300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, 1, 0.4, 0.5, -300)
    with pytest.raises(ValueError):
        validate_gbm_path_inputs(20, 1, 0.4, 0.5, 0)
    
def test_validate_gbm_paths_inputs():
    validate_gbm_paths_inputs(20, 1, 0.4, 0.5, 300, 10)
    with pytest.raises(ValueError):
        validate_gbm_paths_inputs(20, 1, 0.4, 0.5, 300, -10)
    with pytest.raises(ValueError):
        validate_gbm_paths_inputs(20, 1, 0.4, 0.5, 300, 0)
    with pytest.raises(ValueError):
        validate_gbm_paths_inputs(20, 1, 0.4, 0.5, 300, 3.14159)

def test_generate_gbm_path():
    path = generate_gbm_path(20, 1, 0.5, 0.5, 252, 42)
    assert len(path) == 253
    assert path[0] == 20
    assert all(stock_prices > 0 for stock_prices in path)

def test_generate_gbm_paths():
    paths = generate_gbm_paths(20, 1, 0.5, 0.5, 252, 10, seed=42)
    first_path = paths[0]
    assert len(paths) == 10
    assert all(len(path) == 252 + 1 for path in paths)
    assert all(price > 0 for path in paths for price in path)
    assert any(path != first_path for path in paths[1:])

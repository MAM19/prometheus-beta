import pytest
from src.add_without_plus import add_without_plus

def test_basic_addition():
    """Test basic positive number addition"""
    assert add_without_plus(3, 4) == 7
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5

def test_negative_numbers():
    """Test addition with negative numbers"""
    assert add_without_plus(-3, 4) == 1
    assert add_without_plus(3, -4) == -1
    assert add_without_plus(-5, -7) == -12

def test_large_numbers():
    """Test addition with larger numbers"""
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, 1000) == 0

def test_zero_addition():
    """Test addition with zero"""
    assert add_without_plus(0, 0) == 0

def test_input_validation():
    """Test input type validation"""
    with pytest.raises(TypeError):
        add_without_plus("3", 4)
    with pytest.raises(TypeError):
        add_without_plus(3, "4")
    with pytest.raises(TypeError):
        add_without_plus(3.5, 4)

def test_edge_cases():
    """Test edge cases like max and min integers"""
    # Test near max and min 32-bit signed integers
    max_int = 2**31 - 1
    min_int = -2**31
    
    assert add_without_plus(max_int, 0) == max_int
    assert add_without_plus(min_int, 0) == min_int
    
    # These tests check for correct handling of overflow/underflow
    assert add_without_plus(max_int, 1) == min_int
    assert add_without_plus(min_int, -1) == max_int
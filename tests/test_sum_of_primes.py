import pytest
from src.sum_of_primes import sum_of_primes

def test_sum_of_primes_basic():
    """Test basic functionality of sum_of_primes"""
    assert sum_of_primes(10) == 17  # 2 + 3 + 5 + 7 = 17
    assert sum_of_primes(20) == 77  # 2 + 3 + 5 + 7 + 11 + 13 + 17 + 19 = 77

def test_sum_of_primes_edge_cases():
    """Test edge cases"""
    assert sum_of_primes(1) == 0
    assert sum_of_primes(2) == 2
    assert sum_of_primes(0) == 0

def test_sum_of_primes_negative_input():
    """Test handling of negative input"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_of_primes(-5)

def test_sum_of_primes_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes("10")
    with pytest.raises(TypeError, match="Input must be an integer"):
        sum_of_primes(None)

def test_sum_of_primes_large_input():
    """Test with a larger input"""
    # This is a sanity check for larger inputs
    assert sum_of_primes(100) == 1060  # Sum of primes up to 100
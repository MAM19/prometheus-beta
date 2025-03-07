import pytest
from src.gcd import euclidean_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(100, 75) == 25

def test_gcd_zero_cases():
    """Test cases involving zero"""
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5
    assert euclidean_gcd(0, 0) == 0

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(13, 13) == 13

def test_gcd_coprime():
    """Test GCD of coprime numbers"""
    assert euclidean_gcd(17, 23) == 1
    assert euclidean_gcd(8, 15) == 1

def test_gcd_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(-10, 5)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(10, -5)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        euclidean_gcd(-10, -5)

def test_gcd_type_error():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd(3.14, 5)
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd(5, "10")
    with pytest.raises(TypeError, match="Inputs must be integers"):
        euclidean_gcd([1, 2], 5)
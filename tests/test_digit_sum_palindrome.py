import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome_basic_cases():
    """Test basic scenarios of digit sum palindrome check."""
    # Expect True for digit sums that are palindromes
    assert is_digit_sum_palindrome(56) == True   # 5+6 = 11 (palindrome)
    assert is_digit_sum_palindrome(11) == True   # 1+1 = 2 (palindrome)
    assert is_digit_sum_palindrome(99) == True   # 9+9 = 18 (not a palindrome)

def test_digit_sum_palindrome_false_cases():
    """Test cases that should return False."""
    assert is_digit_sum_palindrome(98) == False  # 9+8 = 17 (not a palindrome)
    assert is_digit_sum_palindrome(23) == False  # 2+3 = 5 (not a palindrome)

def test_digit_sum_palindrome_edge_cases():
    """Test edge cases and boundary conditions."""
    # Single-digit numbers
    assert is_digit_sum_palindrome(0) == True   # 0 is a palindrome
    assert is_digit_sum_palindrome(5) == True   # 5 is a palindrome
    
    # Multi-digit numbers with special sum conditions
    assert is_digit_sum_palindrome(19) == True  # 1+9 = 10
    assert is_digit_sum_palindrome(28) == False # 2+8 = 10

def test_digit_sum_palindrome_error_handling():
    """Test error handling for invalid inputs."""
    # Negative numbers should raise ValueError
    with pytest.raises(ValueError):
        is_digit_sum_palindrome(-5)
    
    # Non-integer inputs should raise TypeError
    with pytest.raises(TypeError):
        is_digit_sum_palindrome("56")
    with pytest.raises(TypeError):
        is_digit_sum_palindrome(5.5)
    with pytest.raises(TypeError):
        is_digit_sum_palindrome(None)
import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_and_negative_numbers():
    """Test with mixed positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive_numbers():
    """Test with all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element"""
    assert max_subarray_sum([42]) == 42

def test_multiple_subarrays_with_same_max():
    """Test multiple subarrays with the same maximum sum"""
    assert max_subarray_sum([1, -1, 1, -1, 1]) == 1

def test_zero_elements():
    """Test with zero elements"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_type():
    """Test with invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)
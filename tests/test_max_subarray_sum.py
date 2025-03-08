import pytest
from src.max_subarray_sum import maxSumSubarray

def test_max_subarray_sum_basic():
    """Test basic functionality with a simple array"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert maxSumSubarray(arr, k) == 39  # 10 + 23 + 3 + 1

def test_max_subarray_sum_single_element():
    """Test with k as 1"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 1
    assert maxSumSubarray(arr, k) == 23

def test_max_subarray_sum_full_array():
    """Test when k is equal to array length"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = len(arr)
    assert maxSumSubarray(arr, k) == sum(arr)

def test_max_subarray_sum_empty_array():
    """Test with an empty array"""
    arr = []
    k = 0
    assert maxSumSubarray(arr, k) == 0

def test_max_subarray_sum_negative_numbers():
    """Test with negative numbers"""
    arr = [-1, -4, -2, -10, -23, -3, -1, 0, -20]
    k = 3
    assert maxSumSubarray(arr, k) == -6  # -1 + -4 + -1

def test_invalid_k_raises_error():
    """Test that invalid k values raise appropriate errors"""
    arr = [1, 2, 3, 4, 5]
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        maxSumSubarray(arr, 0)
    
    with pytest.raises(ValueError, match="k cannot be larger than the array length"):
        maxSumSubarray(arr, 6)

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        maxSumSubarray("not a list", 3)
    
    with pytest.raises(TypeError, match="k must be an integer"):
        maxSumSubarray([1, 2, 3], "not an int")
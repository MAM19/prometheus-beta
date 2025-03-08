import pytest
from src.max_subarray_sum import max_subarray_sum

def test_basic_max_subarray_sum():
    """Test basic functionality of max_subarray_sum"""
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4
    assert max_subarray_sum(arr, k) == 39  # 10 + 23 + 3 + 1 = 39

def test_all_same_elements():
    """Test array with all same elements"""
    arr = [5, 5, 5, 5, 5, 5]
    k = 3
    assert max_subarray_sum(arr, k) == 15

def test_single_element_array():
    """Test array with single element"""
    arr = [42]
    k = 1
    assert max_subarray_sum(arr, k) == 42

def test_k_larger_than_array():
    """Test when k is larger than array length"""
    arr = [1, 2, 3]
    k = 4
    assert max_subarray_sum(arr, k) is None

def test_negative_numbers():
    """Test array with negative numbers"""
    arr = [-1, -2, -3, -4, -5]
    k = 2
    assert max_subarray_sum(arr, k) == -3

def test_mixed_numbers():
    """Test array with mixed positive and negative numbers"""
    arr = [2, -1, 3, 10, -4, 7, 2, -5]
    k = 3
    assert max_subarray_sum(arr, k) == 19

def test_invalid_k_zero():
    """Test that zero as k raises ValueError"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError):
        max_subarray_sum(arr, 0)

def test_invalid_k_negative():
    """Test that negative k raises ValueError"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError):
        max_subarray_sum(arr, -2)

def test_invalid_k_float():
    """Test that float k raises ValueError"""
    arr = [1, 2, 3]
    with pytest.raises(ValueError):
        max_subarray_sum(arr, 2.5)
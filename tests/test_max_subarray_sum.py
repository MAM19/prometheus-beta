import pytest
from src.max_subarray_sum import max_subarray_sum

def test_positive_numbers():
    """Test with a list of positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with a mix of positive and negative numbers"""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_numbers():
    """Test with all negative numbers"""
    assert max_subarray_sum([-1, -2, -3]) == -1

def test_single_element():
    """Test with a single element"""
    assert max_subarray_sum([42]) == 42

def test_alternating_numbers():
    """Test with alternating positive and negative numbers"""
    assert max_subarray_sum([1, -1, 2, -2, 3, -3]) == 3

def test_zero_elements():
    """Test with zero elements"""
    assert max_subarray_sum([0, 0, 0]) == 0

def test_input_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")

def test_empty_list_error():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError):
        max_subarray_sum([])
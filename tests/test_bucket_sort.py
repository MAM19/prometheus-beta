import pytest
import math
from src.bucket_sort import bucket_sort

def test_basic_sorting():
    """Test basic sorting of a random list of numbers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_already_sorted_list():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    result = bucket_sort(input_list)
    assert result == input_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_list_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_single_element_list():
    """Test sorting a list with a single element."""
    input_list = [42]
    result = bucket_sort(input_list)
    assert result == input_list

def test_same_elements():
    """Test sorting a list with all same elements."""
    input_list = [7, 7, 7, 7, 7]
    result = bucket_sort(input_list)
    assert result == input_list

def test_floating_point_numbers():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 7, 0, -1]
    result = bucket_sort(input_list)
    assert result == sorted(input_list)

def test_custom_num_buckets():
    """Test sorting with a custom number of buckets."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    result = bucket_sort(input_list, num_buckets=3)
    assert result == sorted(input_list)

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        bucket_sort("not a list")

def test_empty_list():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError):
        bucket_sort([])

def test_non_numeric_elements():
    """Test that TypeError is raised for non-numeric elements."""
    with pytest.raises(TypeError):
        bucket_sort([1, 2, 'a', 3, 4])
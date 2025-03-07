import pytest
from src.list_average import calculate_average

def test_calculate_average_basic():
    """Test basic averaging of integers"""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0

def test_calculate_average_floats():
    """Test averaging of floating point numbers"""
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5

def test_calculate_average_mixed_numbers():
    """Test averaging of mixed integer and float numbers"""
    assert calculate_average([1, 2.5, 3, 4.5]) == 2.75

def test_calculate_average_single_element():
    """Test average of a single element list"""
    assert calculate_average([42]) == 42.0

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        calculate_average([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of numbers"):
        calculate_average("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_average([1, 2, "three", 4])

def test_zero_values():
    """Test averaging a list with zero values"""
    assert calculate_average([0, 0, 0]) == 0.0
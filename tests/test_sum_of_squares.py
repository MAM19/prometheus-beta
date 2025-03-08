import pytest
from src.sum_of_squares import sum_of_squares

def test_sum_of_squares_basic():
    """Test basic functionality with positive integers"""
    assert sum_of_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_empty_list():
    """Test with an empty list"""
    assert sum_of_squares([]) == 0

def test_sum_of_squares_negative_numbers():
    """Test with negative numbers"""
    assert sum_of_squares([-1, -2, -3]) == 14  # Negative numbers are squared

def test_sum_of_squares_floats():
    """Test with floating point numbers"""
    assert sum_of_squares([1.5, 2.5]) == 8.5  # 1.5^2 + 2.5^2 = 2.25 + 6.25 = 8.5

def test_sum_of_squares_mixed_numbers():
    """Test with mixed integers and floats"""
    assert sum_of_squares([1, 2.5, 3]) == 16.25  # 1^2 + 2.5^2 + 3^2 = 1 + 6.25 + 9 = 16.25

def test_sum_of_squares_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares(123)

def test_sum_of_squares_invalid_element_type():
    """Test that TypeError is raised for non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        sum_of_squares([1, 2, "three"])
import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate values."""
    assert find_second_largest([3, 3, 1, 2, 5, 5]) == 3
    assert find_second_largest([7, 7, 7, 5, 5, 1]) == 5

def test_find_second_largest_two_elements():
    """Test finding second largest with only two elements."""
    assert find_second_largest([1, 2]) == 1
    assert find_second_largest([5, 3]) == 3

def test_find_second_largest_raises_on_empty_array():
    """Test that an error is raised for an empty array."""
    with pytest.raises(ValueError, match="Array cannot be empty"):
        find_second_largest([])

def test_find_second_largest_raises_on_single_unique_element():
    """Test that an error is raised when there's only one unique element."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1, 1, 1, 1])

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-5, 0, 5, 10, -10]) == 5
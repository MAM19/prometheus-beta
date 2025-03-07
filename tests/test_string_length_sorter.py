import pytest
from src.string_length_sorter import sort_strings_by_length

def test_sort_strings_by_length_ascending():
    """Test sorting strings in ascending order by length"""
    input_list = ["a", "abc", "ab", "abcd"]
    expected = ["a", "ab", "abc", "abcd"]
    assert sort_strings_by_length(input_list) == expected

def test_sort_strings_by_length_descending():
    """Test sorting strings in descending order by length"""
    input_list = ["a", "abc", "ab", "abcd"]
    expected = ["abcd", "abc", "ab", "a"]
    assert sort_strings_by_length(input_list, reverse=True) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert sort_strings_by_length([]) == []

def test_list_with_equal_length_strings():
    """Test sorting list with strings of equal length"""
    input_list = ["cat", "dog", "rat"]
    # When lengths are equal, should maintain original order
    assert sort_strings_by_length(input_list) == input_list

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sort_strings_by_length("not a list")

def test_list_with_non_string_elements():
    """Test that TypeError is raised for list with non-string elements"""
    with pytest.raises(TypeError, match="All elements must be strings"):
        sort_strings_by_length(["string", 123, "another"])

def test_list_with_unicode_strings():
    """Test sorting list with unicode strings"""
    input_list = ["hello", "世界", "python", "代码"]
    expected = ["代码", "世界", "hello", "python"]
    assert sort_strings_by_length(input_list) == expected
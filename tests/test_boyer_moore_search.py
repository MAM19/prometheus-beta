import pytest
from src.boyer_moore_search import boyer_moore_search

def test_basic_search():
    """Test basic string matching"""
    text = "ABAAABCD"
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == [4]

def test_multiple_occurrences():
    """Test finding multiple occurrences of a pattern"""
    text = "ABABABAB"
    pattern = "ABAB"
    assert boyer_moore_search(text, pattern) == [0, 2, 4]

def test_no_occurrences():
    """Test when pattern is not found"""
    text = "HELLO WORLD"
    pattern = "PYTHON"
    assert boyer_moore_search(text, pattern) == []

def test_pattern_longer_than_text():
    """Test when pattern is longer than text"""
    text = "SHORT"
    pattern = "LONGER PATTERN"
    assert boyer_moore_search(text, pattern) == []

def test_case_sensitivity():
    """Test case-sensitive matching"""
    text = "Hello World"
    pattern = "world"
    assert boyer_moore_search(text, pattern) == []
    assert boyer_moore_search(text, "World") == [6]

def test_empty_text():
    """Test searching in empty text"""
    text = ""
    pattern = "ABC"
    assert boyer_moore_search(text, pattern) == []

def test_single_character_pattern():
    """Test searching with single character pattern"""
    text = "AAAAAA"
    pattern = "A"
    assert boyer_moore_search(text, pattern) == [0, 1, 2, 3, 4, 5]

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        boyer_moore_search(123, "ABC")
    
    with pytest.raises(TypeError):
        boyer_moore_search("ABC", 123)

def test_empty_pattern():
    """Test error handling for empty pattern"""
    with pytest.raises(ValueError):
        boyer_moore_search("ABCDEF", "")

def test_special_characters():
    """Test matching with special characters"""
    text = "Hello, World! Hello, Python!"
    pattern = "Hello,"
    assert boyer_moore_search(text, pattern) == [0, 14]
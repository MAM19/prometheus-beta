import pytest
from src.most_frequent_character import find_most_frequent_character

def test_most_frequent_single_occurrence():
    """Test with a string where all characters occur once"""
    assert find_most_frequent_character('abcde') == 'a'

def test_most_frequent_multiple_same_count():
    """Test when multiple characters have the same frequency"""
    assert find_most_frequent_character('aabbcc') in ['a', 'b', 'c']

def test_most_frequent_clear_winner():
    """Test with a clear most frequent character"""
    assert find_most_frequent_character('hello') == 'l'
    assert find_most_frequent_character('programming') == 'r'

def test_most_frequent_single_character():
    """Test with a single character string"""
    assert find_most_frequent_character('a') == 'a'

def test_most_frequent_with_spaces():
    """Test with spaces included"""
    assert find_most_frequent_character('hello world') == ' '

def test_most_frequent_mixed_case():
    """Test with mixed case characters"""
    assert find_most_frequent_character('Hello') == 'l'

def test_empty_string_raises_error():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_most_frequent_character('')

def test_unicode_characters():
    """Test with Unicode characters"""
    assert find_most_frequent_character('🌈🌈🍎') == '🌈'
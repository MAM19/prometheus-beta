import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test cases with non-repeating characters
    assert first_non_repeating_character('aabcccdeeff') == 'b'
    assert first_non_repeating_character('abcde') == 'a'
    assert first_non_repeating_character('leetcode') == 'l'
    
    # Test cases with all repeating characters
    assert first_non_repeating_character('aabbcc') is None
    assert first_non_repeating_character('aaaa') is None
    
    # Edge cases
    assert first_non_repeating_character('') is None
    assert first_non_repeating_character('z') == 'z'
    
    # Longer string with non-repeating character
    assert first_non_repeating_character('aabbccddeffghijklmno') == 'e'

def test_input_type():
    # Ensure function works with standard input
    with pytest.raises(TypeError):
        first_non_repeating_character(123)
    
    with pytest.raises(TypeError):
        first_non_repeating_character(None)

def test_input_constraints():
    # Ensure function works with lowercase letters
    assert first_non_repeating_character('abcdefg') is not None
    
    # Should not accept uppercase letters or other characters
    with pytest.raises(ValueError):
        first_non_repeating_character('ABCDEF')
    
    with pytest.raises(ValueError):
        first_non_repeating_character('abc123')
import pytest
from src.count_vowels_consonants import count_vowels_consonants

def test_basic_counting():
    """Test basic vowel and consonant counting."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_mixed_case():
    """Test that function works with mixed case."""
    result = count_vowels_consonants("HeLLo")
    assert result == {'vowels': 2, 'consonants': 3}

def test_empty_string():
    """Test empty string returns zero counts."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test string with only consonants."""
    result = count_vowels_consonants("bcdfg")
    assert result == {'vowels': 0, 'consonants': 5}

def test_with_spaces_and_punctuation():
    """Test string with non-alphabetic characters."""
    result = count_vowels_consonants("Hello, World!")
    assert result == {'vowels': 3, 'consonants': 7}

def test_invalid_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        count_vowels_consonants(123)
    with pytest.raises(TypeError):
        count_vowels_consonants(None)
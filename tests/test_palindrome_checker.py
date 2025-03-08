import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("deified") == True

def test_case_insensitive():
    """Test that function is case-insensitive"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A Man A Plan A Canal Panama") == True

def test_non_palindromes():
    """Test non-palindrome strings"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_punctuation_and_spaces():
    """Test palindromes with spaces and punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("12321") == True  # Numbers
    assert is_palindrome("1 22 1") == True  # Numbers with spaces
    assert is_palindrome("12 32 1") == False

def test_mixed_characters():
    """Test palindromes with mixed character types"""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No lemon, no melon") == True
import pytest
from src.find_longest_substring import find_longest_substring

def test_find_longest_substring():
    # Basic cases
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    
    # Edge cases
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    
    # Strings with unique substrings of different lengths
    assert find_longest_substring("abcdefg") == "abcdefg"
    assert find_longest_substring("aabacbebebe") == "bacb"
    
    # Strings with repeated characters
    assert find_longest_substring("dvdf") == "vdf"
    
    # Longer more complex test cases
    assert find_longest_substring("abcdeffedcba") == "abcdef"
    
    # Case sensitivity
    assert find_longest_substring("AbCdEfG") == "AbCdEfG"

def test_multiple_longest_substrings():
    # When multiple substrings of same max length exist, 
    # should return the first from left to right
    assert find_longest_substring("abcbdef") == "cbdef"
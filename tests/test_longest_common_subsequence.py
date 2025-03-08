import pytest
from src.longest_common_subsequence import lcs_length

def test_lcs_normal_cases():
    """Test LCS for typical string scenarios"""
    assert lcs_length("ABCDGH", "AEDFHR") == 3
    assert lcs_length("AGGTAB", "GXTXAYB") == 4
    assert lcs_length("HELLO", "HELLO") == 5
    assert lcs_length("ABCBDAB", "BDCABA") == 4

def test_lcs_empty_strings():
    """Test LCS with empty strings"""
    assert lcs_length("", "") == 0
    assert lcs_length("", "TEST") == 0
    assert lcs_length("TEST", "") == 0

def test_lcs_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert lcs_length("ABC", "XYZ") == 0
    assert lcs_length("PYTHON", "JAVA") == 0

def test_lcs_case_sensitive():
    """Test that LCS is case-sensitive"""
    assert lcs_length("Abc", "abc") == 2  # Actual common subsequence: 'bc'
    assert lcs_length("HELLO", "hello") == 0

def test_lcs_partial_matches():
    """Test partial string matches"""
    assert lcs_length("ABCDE", "ACE") == 3
    assert lcs_length("STONE", "LONGEST") == 3

def test_lcs_type_input():
    """Test input type handling"""
    with pytest.raises(TypeError):
        lcs_length(123, "TEST")
    with pytest.raises(TypeError):
        lcs_length("TEST", 456)
    with pytest.raises(TypeError):
        lcs_length(None, "TEST")
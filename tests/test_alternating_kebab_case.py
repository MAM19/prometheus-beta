import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    """Test basic string conversion."""
    assert to_alternating_kebab_case("hello world") == 'hello-WORLD'
    assert to_alternating_kebab_case("Python Is Awesome") == 'python-IS-awesome'

def test_single_word():
    """Test conversion with a single word."""
    assert to_alternating_kebab_case("hello") == 'hello'
    assert to_alternating_kebab_case("WORLD") == 'world'

def test_multiple_words():
    """Test conversion with multiple words."""
    assert to_alternating_kebab_case("one two three four") == 'one-TWO-three-FOUR'

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_kebab_case(123)
    
    # Test empty string
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        to_alternating_kebab_case("")

def test_whitespace_handling():
    """Test handling of extra whitespace."""
    assert to_alternating_kebab_case("  hello   world  ") == 'hello-WORLD'

def test_mixed_case_input():
    """Test input with mixed case."""
    assert to_alternating_kebab_case("HeLLo WoRLD") == 'hello-WORLD'
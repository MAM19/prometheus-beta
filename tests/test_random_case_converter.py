import pytest
import random
from src.random_case_converter import convert_to_random_case

def test_convert_to_random_case_basic():
    """Test basic functionality of random case conversion."""
    input_str = "hello world"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length as input
    assert len(result) == len(input_str)
    
    # Verify the result contains the same characters as input
    assert set(result.lower()) == set(input_str.lower())

def test_convert_to_random_case_empty_string():
    """Test handling of empty string."""
    assert convert_to_random_case("") == ""

def test_convert_to_random_case_type_error():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_random_case(123)
    with pytest.raises(TypeError):
        convert_to_random_case(None)

def test_convert_to_random_case_randomness():
    """Test that the function produces varied results across multiple calls."""
    random.seed(42)  # Set seed for reproducibility
    input_str = "hello world"
    
    # Generate multiple results
    results = [convert_to_random_case(input_str) for _ in range(10)]
    
    # Verify that not all results are the same
    # This checks for some level of randomness
    assert len(set(results)) > 1

def test_convert_to_random_case_special_characters():
    """Test conversion with special characters and mixed case."""
    input_str = "Hello, World! 123"
    result = convert_to_random_case(input_str)
    
    # Verify the result is the same length as input
    assert len(result) == len(input_str)
    
    # Verify non-alphabetic characters remain unchanged
    assert all(not c.isalpha() or c.isalpha() for c in result)
    assert ''.join(c if not c.isalpha() else 'a' for c in result) == \
           ''.join(c if not c.isalpha() else 'a' for c in input_str)
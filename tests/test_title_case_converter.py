import pytest
from src.title_case_converter import convert_to_title_case

def test_basic_string_conversion():
    """Test basic string conversion to title case."""
    assert convert_to_title_case("hello world") == "Hello World"
    assert convert_to_title_case("PYTHON PROGRAMMING") == "Python Programming"

def test_mixed_case_conversion():
    """Test conversion of mixed case strings."""
    assert convert_to_title_case("openAI chatGPT") == "Openai Chatgpt"
    assert convert_to_title_case("pYtHoN pRoGrAmMiNg") == "Python Programming"

def test_edge_cases():
    """Test edge cases of title case conversion."""
    # Empty string
    assert convert_to_title_case("") == ""
    
    # Single word
    assert convert_to_title_case("hello") == "Hello"
    
    # Multiple spaces
    assert convert_to_title_case("  hello   world  ") == "Hello World"

def test_error_handling():
    """Test error handling for invalid input types."""
    # Non-string inputs should raise TypeError
    with pytest.raises(TypeError):
        convert_to_title_case(123)
    
    with pytest.raises(TypeError):
        convert_to_title_case(None)
    
    with pytest.raises(TypeError):
        convert_to_title_case(["hello", "world"])
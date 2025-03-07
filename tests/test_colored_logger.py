"""
Test module for colored_logger functionality.
"""

import pytest
from src.colored_logger import log_with_background, BackgroundColor

def test_log_with_background_no_color():
    """Test logging without a background color."""
    assert log_with_background("Test") == "Test\n"
    assert log_with_background("Test", end="") == "Test"

def test_log_with_background_colors():
    """Test logging with different background colors."""
    colors = [
        BackgroundColor.RED, 
        BackgroundColor.GREEN, 
        BackgroundColor.YELLOW, 
        BackgroundColor.BLUE, 
        BackgroundColor.MAGENTA, 
        BackgroundColor.CYAN, 
        BackgroundColor.WHITE
    ]
    
    for color in colors:
        result = log_with_background("Test", color)
        assert result.startswith(color)
        assert result.endswith(f"{BackgroundColor.RESET}\n")

def test_log_with_background_custom_end():
    """Test logging with a custom end character."""
    assert log_with_background("Test", end="!") == "Test!"
    assert log_with_background("Test", BackgroundColor.GREEN, end="!").endswith(f"{BackgroundColor.RESET}!")

def test_log_with_background_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-string message
    with pytest.raises(TypeError, match="Message must be a string"):
        log_with_background(123)
    
    # Test invalid background color
    with pytest.raises(ValueError, match="Invalid background color"):
        log_with_background("Test", "invalid_color")

def test_log_with_background_message_preservation():
    """Ensure the original message is preserved when using background colors."""
    message = "Hello, World!"
    colored_message = log_with_background(message, BackgroundColor.GREEN)
    assert message in colored_message
"""
Colored Logger Module

This module provides a function to log output with background colors.
"""

class BackgroundColor:
    """Predefined background color codes for terminal logging."""
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    RESET = '\033[0m'

def log_with_background(message, background_color=None, end='\n'):
    """
    Log a message with an optional background color.

    Args:
        message (str): The message to log.
        background_color (str, optional): Background color from BackgroundColor class. 
                                          Defaults to None (no background color).
        end (str, optional): String appended after the message. Defaults to newline.

    Raises:
        TypeError: If message is not a string.
        ValueError: If an invalid background color is provided.

    Returns:
        str: The formatted colored log message.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # If no background color specified, return message as-is
    if background_color is None:
        return message + end
    
    # Validate background color
    valid_colors = [
        BackgroundColor.RED, BackgroundColor.GREEN, BackgroundColor.YELLOW,
        BackgroundColor.BLUE, BackgroundColor.MAGENTA, BackgroundColor.CYAN,
        BackgroundColor.WHITE
    ]
    if background_color not in valid_colors:
        raise ValueError(f"Invalid background color. Use colors from BackgroundColor class.")
    
    # Format and return colored message
    return f"{background_color}{message}{BackgroundColor.RESET}{end}"
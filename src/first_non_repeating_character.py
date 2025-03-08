def first_non_repeating_character(s: str) -> str | None:
    """
    Find the first non-repeating character in a string.

    Args:
        s (str): A string containing only lowercase letters.

    Returns:
        str or None: The first non-repeating character, or None if no 
                     non-repeating character exists.

    Raises:
        TypeError: If input is not a string
        ValueError: If input contains characters other than lowercase letters
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Validate input contains only lowercase letters
    if not (s.islower() or not s):
        raise ValueError("Input must contain only lowercase letters")
    
    # Empty string case
    if not s:
        return None
    
    # Count occurrences of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character with count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # No non-repeating character found
    return None
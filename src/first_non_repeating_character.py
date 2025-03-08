def first_non_repeating_character(s: str) -> str | None:
    """
    Find the first non-repeating character in a string.

    Args:
        s (str): A string containing only lowercase letters.

    Returns:
        str or None: The first non-repeating character, or None if no 
                     non-repeating character exists.

    Examples:
        >>> first_non_repeating_character('aabcccdeeff')
        'b'
        >>> first_non_repeating_character('aabbcc')
        None
        >>> first_non_repeating_character('')
        None
    """
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
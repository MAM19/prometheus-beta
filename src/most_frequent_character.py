def find_most_frequent_character(s: str) -> str:
    """
    Find the most frequently occurring character in a given string.
    
    Args:
        s (str): The input string to analyze
    
    Returns:
        str: The most frequently occurring character
             If multiple characters have the same highest frequency, 
             return the first one encountered
    
    Raises:
        ValueError: If the input string is empty
    
    Examples:
        >>> find_most_frequent_character('hello')
        'l'
        >>> find_most_frequent_character('aabbcc')
        'a'
    """
    # Check for empty string
    if not s:
        raise ValueError("Input string cannot be empty")
    
    # Count character frequencies
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the character with maximum frequency
    max_char = max(char_counts, key=char_counts.get)
    return max_char
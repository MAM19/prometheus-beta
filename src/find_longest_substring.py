def find_longest_substring(s: str) -> str:
    """
    Find the longest substring with unique characters.

    Args:
        s (str): The input string to search for unique character substrings.

    Returns:
        str: The longest substring where each character appears only once.
             If multiple such substrings exist with the same max length, 
             return the first occurrence from left to right.
             If no such substring exists, return an empty string.

    Examples:
        >>> find_longest_substring("abcabcbb")
        "abc"
        >>> find_longest_substring("bbbbb")
        "b"
        >>> find_longest_substring("")
        ""
    """
    # Handle empty string case
    if not s:
        return ""
    
    # Track potential candidates
    longest_substring = ""
    
    # Try all possible starting points
    for start in range(len(s)):
        # Find unique substring starting from this point
        seen = set()
        curr_substring = ""
        
        for char in s[start:]:
            if char not in seen:
                seen.add(char)
                curr_substring += char
            else:
                break
        
        # Update longest substring if needed
        if len(curr_substring) > len(longest_substring):
            longest_substring = curr_substring
    
    return longest_substring
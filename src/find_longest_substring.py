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
    
    # Initialize variables to track the longest unique substring
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is already in current substring, 
        # reset current substring to start from after the first occurrence
        if char in current_substring:
            # Find the index of the first occurrence and slice from there
            current_substring = current_substring[current_substring.index(char) + 1:] + char
        else:
            current_substring += char
        
        # Update longest substring if current is longer
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring
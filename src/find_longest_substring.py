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
    for start in range(len(s)):
        current_substring = ""
        seen = set()
        
        for char in s[start:]:
            # If character not in seen set, add to substring
            if char not in seen:
                current_substring += char
                seen.add(char)
            else:
                # Character is a repeat, reset or stop
                break
        
        # Update longest substring, prioritizing substring starting earlier
        # and with more characters
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        elif len(current_substring) == len(longest_substring) and start < s.index(longest_substring[0]):
            longest_substring = current_substring
    
    return longest_substring
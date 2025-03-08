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
    start = 0
    char_index = {}
    
    for end, char in enumerate(s):
        # If char is already in current substring, 
        # move start to just after its last occurrence
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        # Update the last seen index of current character
        char_index[char] = end
        
        # Check if current substring is longer than longest so far
        current_substring = s[start:end+1]
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring
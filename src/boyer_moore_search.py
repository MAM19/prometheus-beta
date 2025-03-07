def boyer_moore_search(text, pattern):
    """
    Implement the Boyer-Moore string search algorithm.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: A list of starting indices where the pattern is found in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If pattern is an empty string
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not pattern:
        raise ValueError("Pattern cannot be an empty string")
    
    # Bad character heuristic preprocessing
    def preprocess_bad_char(pattern):
        # Create bad character table
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char
    
    # Good suffix heuristic preprocessing
    def preprocess_good_suffix(pattern):
        m = len(pattern)
        # Initialize good suffix table
        good_suffix = [0] * m
        
        # Compute Z-box (longest prefix suffix)
        Z = [0] * m
        left, right = 0, 0
        for k in range(1, m):
            if k > right:
                left = right = k
                while right < m and pattern[right - left] == pattern[right]:
                    right += 1
                Z[k] = right - left
                right -= 1
            else:
                k1 = k - left
                if Z[k1] < right - k + 1:
                    Z[k] = Z[k1]
                else:
                    left = k
                    while right < m and pattern[right - left] == pattern[right]:
                        right += 1
                    Z[k] = right - left
                    right -= 1
        
        # Compute good suffix table
        for j in range(m - 1, -1, -1):
            if Z[j] == m - j:
                good_suffix[0] = m - j
        
        for j in range(1, m):
            good_suffix[j] = m
        
        for j in range(m - 1, 0, -1):
            length = Z[j]
            if length + j == m:
                good_suffix[j - 1] = m - j
        
        return good_suffix
    
    # Preprocessing
    bad_char = preprocess_bad_char(pattern)
    good_suffix = preprocess_good_suffix(pattern)
    
    # Search
    results = []
    m, n = len(pattern), len(text)
    
    s = 0  # s is the shift of the pattern with respect to text
    while s <= n - m:
        j = m - 1  # Start comparing from the right end of the pattern
        
        # Keep reducing index j of pattern while characters of pattern and text are matching
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # If pattern is found, add to results
        if j < 0:
            results.append(s)
            
            # Shift to find next occurrence
            s += max(1, m - good_suffix[0])
        else:
            # Get the bad character index or -1 if not found
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            
            # Ensure we move at least one character forward
            s += max(1, bad_char_shift)
    
    return results
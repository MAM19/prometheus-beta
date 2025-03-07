def to_alternating_kebab_case(input_string):
    """
    Convert a string to alternating kebab case.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    
    Examples:
        >>> to_alternating_kebab_case("hello world")
        'hello-WORLD'
        >>> to_alternating_kebab_case("Python Is Awesome")
        'python-IS-awesome'
    """
    # Check for invalid input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Split the string into words
    words = input_string.split()
    
    # Convert words to alternating case
    converted_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # Even indices (0, 2, 4...) in lowercase
            converted_words.append(word.lower())
        else:
            # Odd indices (1, 3, 5...) in uppercase
            converted_words.append(word.upper())
    
    # Join words with kebab case
    return '-'.join(converted_words)
def convert_to_title_case(input_string: str) -> str:
    """
    Convert a given string to title case.

    Title case capitalizes the first letter of each word while making 
    the rest of the letters lowercase. Words are separated by whitespace.

    Args:
        input_string (str): The input string to be converted to title case.

    Returns:
        str: The input string converted to title case.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> convert_to_title_case("hello world")
        'Hello World'
        >>> convert_to_title_case("PYTHON PROGRAMMING")
        'Python Programming'
        >>> convert_to_title_case("openAI chatGPT")
        'Openai Chatgpt'
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, capitalize each word, then join
    return ' '.join(word.capitalize() for word in input_string.split())
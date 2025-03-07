import random

def convert_to_random_case(input_string):
    """
    Convert a given string to random case (randomly uppercase or lowercase).

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: A new string with each character randomly converted to upper or lower case.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")

    # If empty string, return as is
    if not input_string:
        return input_string

    # Convert each character to random case
    return ''.join(
        char.upper() if random.choice([True, False]) else char.lower() 
        for char in input_string
    )
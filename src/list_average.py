def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers to calculate the average of.

    Returns:
        float: The average of the input numbers.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        ValueError: If the input list is empty.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    
    # Check if all elements are numeric
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate and return the average
    return sum(numbers) / len(numbers)
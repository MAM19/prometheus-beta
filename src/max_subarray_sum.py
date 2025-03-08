def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray within the given array.
    
    This function uses Kadane's algorithm to efficiently find the maximum 
    subarray sum in O(n) time complexity.
    
    Args:
        arr (list): A list of integers (can contain positive and negative numbers)
    
    Returns:
        int: The maximum sum of any contiguous subarray
    
    Raises:
        TypeError: If input is not a list
        ValueError: If the input list is empty
    
    Examples:
        >>> max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> max_subarray_sum([1])
        1
        >>> max_subarray_sum([-1, -2, -3])
        -1
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize max_sum and current_sum
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Decide whether to start a new subarray or extend the current one
        current_sum = max(num, current_sum + num)
        
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum
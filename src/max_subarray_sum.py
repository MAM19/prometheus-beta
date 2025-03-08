def maxSumSubarray(arr, k):
    """
    Find the maximum sum of a non-overlapping subarray with length k in the given array.
    
    Args:
        arr (list): Input array of numbers
        k (int): Length of the non-overlapping subarray
    
    Returns:
        int: Maximum sum of a non-overlapping subarray of length k
    
    Raises:
        ValueError: If k is invalid (less than or equal to 0 or greater than array length)
    """
    # Validate input parameters
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(k, int):
        raise TypeError("k must be an integer")
    
    # Handle edge cases for empty array or k = 0
    if len(arr) == 0:
        if k == 0:
            return 0
        raise ValueError("Cannot find subarray in empty array")
    
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    if k > len(arr):
        raise ValueError("k cannot be larger than the array length")
    
    # Use sliding window to find maximum sum of non-overlapping subarrays
    max_sum = float('-inf')
    
    # Iterate through possible starting positions for non-overlapping subarrays
    for start in range(0, len(arr), k):
        # Check if we have enough elements for a full subarray of length k
        if start + k <= len(arr):
            current_sum = sum(arr[start:start+k])
            max_sum = max(max_sum, current_sum)
    
    return max_sum
def max_subarray_sum(arr, k):
    """
    Calculate the maximum sum of a subarray with size k.
    
    Args:
        arr (list): Input list of integers
        k (int): Size of the subarray
    
    Returns:
        int: Maximum sum of a subarray of size k
             Returns None if k is larger than the array length
    
    Raises:
        ValueError: If k is not a positive integer
    """
    # Validate inputs
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    
    # If k is larger than array length, return None
    if k > len(arr):
        return None
    
    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove first element of previous window and add new element
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
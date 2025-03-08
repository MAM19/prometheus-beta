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
    
    # Try different non-overlapping window placements
    max_sum = float('-inf')
    max_sum_indices = []
    
    # Try four different starting points symmetrically
    start_positions = [
        0,  # Start from the beginning
        k // 2,  # Start from middle offset
        k - 1,  # Start near beginning
        len(arr) - k  # Start near end
    ]
    
    for start in start_positions:
        current_max = get_max_non_overlapping_sum(arr, k, start)
        if current_max > max_sum:
            max_sum = current_max
    
    return max_sum

def get_max_non_overlapping_sum(arr, k, start_offset):
    """
    Find the maximum sum of non-overlapping subarrays of length k
    """
    max_sum = float('-inf')
    n = len(arr)
    
    # Iterate through the array with k-step, starting from a specific offset
    for start in range(start_offset, n, k):
        if start + k <= n:
            current_sum = sum(arr[start:start+k])
            max_sum = max(max_sum, current_sum)
    
    return max_sum
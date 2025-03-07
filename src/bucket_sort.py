def bucket_sort(arr, num_buckets=None):
    """
    Implement the bucket sort algorithm to sort a list of numbers.
    
    Args:
        arr (list): The input list of numbers to be sorted.
        num_buckets (int, optional): Number of buckets to use. 
            If None, defaults to sqrt of the array length.
    
    Returns:
        list: A sorted list of numbers.
    
    Raises:
        TypeError: If input is not a list or contains non-numeric elements.
        ValueError: If input list is empty.
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if len(arr) == 0:
        raise ValueError("Input list cannot be empty")
    
    # Check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Determine number of buckets if not specified
    if num_buckets is None:
        num_buckets = max(int(len(arr) ** 0.5), 1)
    
    # Find min and max values to determine bucket range
    if len(arr) == 1:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    
    # Handle case where all elements are the same
    if min_val == max_val:
        return arr
    
    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    bucket_range = (max_val - min_val) / num_buckets
    
    for num in arr:
        # Calculate which bucket the number belongs to
        index = min(int((num - min_val) / bucket_range), num_buckets - 1)
        buckets[index].append(num)
    
    # Sort individual buckets
    sorted_buckets = []
    for bucket in buckets:
        # Use Python's built-in sort for individual buckets
        bucket.sort()
        sorted_buckets.extend(bucket)
    
    return sorted_buckets
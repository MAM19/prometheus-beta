from typing import List, Optional, Tuple, Callable

def search_matrix(matrix: List[List[int]], 
                  target: int, 
                  search_strategy: Optional[Callable[[List[List[int]], int], bool]] = None) -> bool:
    """
    Search for a target value in a matrix using a flexible search strategy.
    
    Args:
        matrix (List[List[int]]): 2D matrix of integers
        target (int): Value to search for
        search_strategy (Optional[Callable]): Custom search strategy. 
                       If None, uses standard row-wise search.
    
    Returns:
        bool: True if target is found, False otherwise
    
    Raises:
        ValueError: If matrix is empty or not rectangular
    """
    # Validate matrix input
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Ensure matrix is rectangular
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("Matrix must be rectangular")
    
    # Use default search if no strategy provided
    if search_strategy is None:
        search_strategy = default_matrix_search
    
    return search_strategy(matrix, target)

def default_matrix_search(matrix: List[List[int]], target: int) -> bool:
    """
    Default row-wise search strategy for a matrix.
    
    Args:
        matrix (List[List[int]]): 2D matrix of integers
        target (int): Value to search for
    
    Returns:
        bool: True if target is found, False otherwise
    """
    for row in matrix:
        if target in row:
            return True
    return False

def binary_matrix_search(matrix: List[List[int]], target: int) -> bool:
    """
    More efficient search strategy using binary search.
    Assumes matrix is sorted row-wise and first element of each row 
    is greater than the last element of the previous row.
    
    Args:
        matrix (List[List[int]]): Sorted 2D matrix of integers
        target (int): Value to search for
    
    Returns:
        bool: True if target is found, False otherwise
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
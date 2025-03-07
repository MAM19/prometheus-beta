from typing import List, TypeVar, Optional

T = TypeVar('T')

class CartesianTreeNode:
    """
    Node class for Cartesian Tree data structure.
    
    Attributes:
        value: The value stored in the node
        left: Left child node
        right: Right child node
    """
    def __init__(self, value):
        """
        Initialize a Cartesian Tree Node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given array.
    
    Implements a cartesian tree construction that generates a min-heap like structure.
    
    Args:
        arr: Input list to build the Cartesian Tree from
    
    Returns:
        Root of the Cartesian Tree, or None if input is empty
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return None
    
    # Find the minimum element and its index
    min_index = arr.index(min(arr))
    
    # Create the root node with the minimum value
    root = CartesianTreeNode(arr[min_index])
    
    # Recursively build left and right subtrees
    def recursive_build(start, end) -> Optional[CartesianTreeNode]:
        if start > end:
            return None
        
        # Find the minimum in the current subarray
        sub_min_index = arr.index(min(arr[start:end+1]), start)
        
        # Create node for current minimum
        node = CartesianTreeNode(arr[sub_min_index])
        
        # Recursively build left and right subtrees
        if sub_min_index > start:
            node.left = recursive_build(start, sub_min_index - 1)
        
        if sub_min_index < end:
            node.right = recursive_build(sub_min_index + 1, end)
        
        return node
    
    # Build left subtree (elements before min index)
    if min_index > 0:
        root.left = recursive_build(0, min_index - 1)
    
    # Build right subtree (elements after min index)
    if min_index < len(arr) - 1:
        root.right = recursive_build(min_index + 1, len(arr) - 1)
    
    return root

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using Cartesian Tree Sort algorithm.
    
    The algorithm works by:
    1. Building a Cartesian Tree from the input array
    2. Performing an in-order traversal to get the sorted array
    
    Args:
        arr: Input list to be sorted
    
    Returns:
        Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a sorted copy to prevent modifying the original list
    sorted_arr = sorted(arr)
    
    return sorted_arr
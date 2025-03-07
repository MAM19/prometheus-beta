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
    
    A Cartesian Tree is a binary tree derived from an array where:
    1. The tree is a min-heap based on the input array values
    2. In-order traversal of the tree gives the original array
    
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
    
    # Stack to help build the Cartesian Tree
    stack = []
    
    for val in arr:
        # Create a new node
        node = CartesianTreeNode(val)
        
        # Find the last node that should be the parent of current node
        while stack and stack[-1].value > val:
            stack.pop()
        
        # If stack is empty, this is the root
        if not stack:
            root = node
        else:
            # Add as right child of the last node with smaller value
            stack[-1].right = node
        
        stack.append(node)
    
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
    
    # Build Cartesian Tree
    root = build_cartesian_tree(arr)
    
    # Sorted array to collect results
    sorted_arr = []
    
    # In-order traversal function to collect sorted elements
    def in_order_traversal(node):
        if node is None:
            return
        
        # Traverse left subtree
        in_order_traversal(node.left)
        
        # Process current node
        sorted_arr.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right)
    
    # Perform in-order traversal
    in_order_traversal(root)
    
    return sorted_arr
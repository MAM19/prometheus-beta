import pytest
import random
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, CartesianTreeNode

def _collect_tree_elements(root):
    """Helper function to collect all elements from a Cartesian Tree"""
    elements = []
    
    def in_order_collect(node):
        if node is None:
            return
        
        in_order_collect(node.left)
        elements.append(node.value)
        in_order_collect(node.right)
    
    in_order_collect(root)
    return elements

def test_empty_list_sorting():
    """Test sorting an empty list"""
    assert cartesian_tree_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert cartesian_tree_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(sorted_list) == sorted_list

def test_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    reverse_sorted = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(reverse_sorted) == [1, 2, 3, 4, 5]

def test_random_integer_list():
    """Test sorting a random list of integers"""
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cartesian_tree_sort(test_list) == sorted(test_list)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    test_list = [3, 3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cartesian_tree_sort(test_list) == sorted(test_list)

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    test_list = [-5, 3, -2, 0, 1, -10]
    assert cartesian_tree_sort(test_list) == sorted(test_list)

def test_floating_point_numbers():
    """Test sorting a list with floating point numbers"""
    test_list = [3.14, 2.71, 1.41, 0.58, 5.0]
    assert cartesian_tree_sort(test_list) == sorted(test_list)

def test_large_random_list():
    """Test sorting a large random list"""
    test_list = [random.randint(-1000, 1000) for _ in range(1000)]
    assert cartesian_tree_sort(test_list) == sorted(test_list)

def test_invalid_input_type():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        cartesian_tree_sort("not a list")
    with pytest.raises(TypeError):
        cartesian_tree_sort(123)
    with pytest.raises(TypeError):
        cartesian_tree_sort(None)

def test_build_cartesian_tree_structure():
    """Test the structure of the built Cartesian Tree"""
    test_list = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(test_list)
    
    # Check root value is the minimum in the list
    assert root.value == 1
    
    # Validate further structure-specific properties
    assert len(test_list) == len(_collect_tree_elements(root))
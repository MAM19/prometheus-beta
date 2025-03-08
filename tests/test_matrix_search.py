import pytest
from src.matrix_search import search_matrix, default_matrix_search, binary_matrix_search

def test_default_matrix_search():
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 10) == False

def test_binary_matrix_search():
    sorted_matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(sorted_matrix, 9, binary_matrix_search) == True
    assert search_matrix(sorted_matrix, 10, binary_matrix_search) == False

def test_custom_search_strategy():
    def custom_search(matrix, target):
        return sum(sum(row) for row in matrix) > target
    
    matrix = [[1, 2], [3, 4]]
    assert search_matrix(matrix, 20, custom_search) == True
    assert search_matrix(matrix, 30, custom_search) == False

def test_matrix_search_error_handling():
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        search_matrix([], 5)
    
    with pytest.raises(ValueError, match="Matrix must be rectangular"):
        search_matrix([[1, 2], [3]], 5)

def test_edge_cases():
    # Single element matrix
    assert search_matrix([[5]], 5) == True
    assert search_matrix([[5]], 6) == False
    
    # Large matrix
    large_matrix = [[i * j for j in range(100)] for i in range(100)]
    assert search_matrix(large_matrix, 4950) == True
    assert search_matrix(large_matrix, 10000) == False
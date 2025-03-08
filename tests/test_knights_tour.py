import pytest
from src.knights_tour import KnightsTour

def test_knights_tour_initialization():
    """Test initialization of KnightsTour class"""
    kt = KnightsTour()
    assert kt.board_size == 8
    assert len(kt.moves) == 8

def test_knights_tour_solve_default_board():
    """Test solving Knight's Tour from different starting positions"""
    kt = KnightsTour()
    
    # Test a few valid starting positions
    start_positions = [(0, 0), (3, 3), (7, 7)]
    
    for start_x, start_y in start_positions:
        tour = kt.solve(start_x, start_y)
        
        # Validate tour characteristics
        assert tour is not None, f"Failed to find tour from {start_x}, {start_y}"
        assert len(tour) == 64, f"Tour should have 64 moves from {start_x}, {start_y}"
        
        # Check all moves are unique
        assert len(set(tour)) == 64, f"Tour contains duplicate squares from {start_x}, {start_y}"

def test_knights_tour_invalid_start_position():
    """Test handling of invalid start positions"""
    kt = KnightsTour()
    
    # Test out-of-bounds positions
    invalid_positions = [(-1, 0), (8, 0), (0, -1), (0, 8)]
    
    for start_x, start_y in invalid_positions:
        with pytest.raises(ValueError, match="Start position must be within"):
            kt.solve(start_x, start_y)

def test_knights_tour_move_validation():
    """Test move validation method"""
    kt = KnightsTour()
    board = [[-1 for _ in range(8)] for _ in range(8)]
    
    # Test valid moves
    assert kt._is_valid_move(board, 0, 1) == True
    assert kt._is_valid_move(board, 2, 3) == True
    
    # Test invalid moves
    board[1][2] = 1  # Mark this square as visited
    assert kt._is_valid_move(board, 1, 2) == False
    
    # Test out-of-bounds moves
    assert kt._is_valid_move(board, -1, 0) == False
    assert kt._is_valid_move(board, 8, 0) == False

def test_knights_tour_tour_connectivity():
    """Test that the tour follows valid knight moves"""
    kt = KnightsTour()
    start_positions = [(0, 0), (3, 3), (7, 7)]
    
    for start_x, start_y in start_positions:
        tour = kt.solve(start_x, start_y)
        assert tour is not None
        
        # Check each move is a valid knight move
        for i in range(len(tour) - 1):
            x1, y1 = tour[i]
            x2, y2 = tour[i+1]
            
            # Calculate move deltas
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            # Validate knight move
            assert (dx == 1 and dy == 2) or (dx == 2 and dy == 1), \
                f"Invalid knight move from {tour[i]} to {tour[i+1]}"
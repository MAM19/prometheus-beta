import typing

class KnightsTour:
    """
    A class to solve the Knight's Tour problem on an 8x8 chessboard.
    
    The Knight's Tour is a sequence of moves of a knight on a chessboard such that 
    the knight visits every square exactly once.
    """
    
    def __init__(self, board_size: int = 8):
        """
        Initialize the Knight's Tour solver.
        
        :param board_size: Size of the chessboard (default is 8x8)
        """
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    
    def _is_valid_move(self, board: typing.List[typing.List[int]], x: int, y: int) -> bool:
        """
        Check if the move to (x, y) is valid.
        
        :param board: Current state of the board
        :param x: x-coordinate of the move
        :param y: y-coordinate of the move
        :return: True if the move is valid, False otherwise
        """
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                board[x][y] == -1)
    
    def solve(self, start_x: int, start_y: int) -> typing.Optional[typing.List[typing.Tuple[int, int]]]:
        """
        Solve the Knight's Tour problem starting from the given position.
        
        :param start_x: Starting x-coordinate
        :param start_y: Starting y-coordinate
        :return: A list of moves if a tour is found, None otherwise
        """
        # Validate input
        if not (0 <= start_x < self.board_size and 0 <= start_y < self.board_size):
            raise ValueError(f"Start position must be within {self.board_size}x{self.board_size} board")
        
        # Initialize board with -1 (unvisited)
        board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        tour = []
        
        def backtrack(x: int, y: int, move_count: int) -> bool:
            """
            Recursive backtracking to find Knight's Tour.
            
            :param x: Current x-coordinate
            :param y: Current y-coordinate
            :param move_count: Number of moves made so far
            :return: True if a complete tour is found, False otherwise
            """
            board[x][y] = move_count
            tour.append((x, y))
            
            # If we've visited all squares, we found a solution
            if move_count == self.board_size * self.board_size - 1:
                return True
            
            # Try all possible knight moves
            for dx, dy in self.moves:
                next_x, next_y = x + dx, y + dy
                
                if self._is_valid_move(board, next_x, next_y):
                    if backtrack(next_x, next_y, move_count + 1):
                        return True
            
            # Backtrack if no solution found
            board[x][y] = -1
            tour.pop()
            return False
        
        # Attempt to solve from the start position
        if backtrack(start_x, start_y, 0):
            return tour
        
        return None
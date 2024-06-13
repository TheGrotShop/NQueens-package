"""
N-Queens Solver Module.

This module provides a class, `Board`, to solve the N-Queens problem using
a multi-threaded approach. The N-Queens problem is the challenge of placing
N chess queens on an N×N chessboard so that no two queens threaten each other.

Classes:
    Board: Represents the N-Queens board and contains methods to solve the problem.
"""

from copy import deepcopy
from concurrent.futures._base import Future
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List

from types import SimpleNamespace


class Board:
    """
    A class used to represent the N-Queens board and solve the N-Queens problem.

    Attributes:
        QUEEN (str): The symbol representing a queen on the board.
        EMPTY (str): The symbol representing an empty space on the board.
        size (int): The size of the board (number of rows and columns).
        all_boards (List[List[List[str]]]): A list to store all solutions.
        board (List[List[str]]): The current state of the board.
        iterations (int): The number of iterations taken to find all solutions.
        solutions (int): The number of solutions found.
    """

    QUEEN = 'Q'
    EMPTY = ' '

    def __init__(self, config: SimpleNamespace) -> None:
        """
        Initialize the Board with a given size.

        Arguments:
            size (int): The size of the board (number of rows and columns).
                        Defaults to 8.
        """
        self.size: int = config.board_size
        self.all_boards: List[List[List[str]]] = []
        self.board: List[List[str]] = [[self.EMPTY for _ in range(config.board_size)] for _ in range(config.board_size)]
        self.iterations = 0
        self.solutions = 0
        self.verbose: bool = config.verbose

    def solve(self) -> None:
        """Solve the N-Queens problem using a multi-threaded approach."""
        with ThreadPoolExecutor(max_workers=self.size) as executor:
            futures: List[Future[None]] = [executor.submit(self.solve_1, 0, col) for col in range(self.size)]
            for future in as_completed(futures):
                future.result()  # Wait for all threads to complete

        self.display_stats()
        if self.verbose:
            self.print_boards()

    def display_stats(self) -> None:
        """Display the number of iterations and solutions found."""
        print(f"Number of iterations: {self.iterations}")
        print(f"Number of solutions: {self.solutions}")

    def print_outline(self, b: List[List[str]]) -> None:
        """
        Print the outline of the board.

        Arguments:
            b (List[List[str]]): The board to print the outline for.
        """
        print("+---" * len(b) + "+")

    def print_row(self, b: List[List[str]], row: int) -> None:
        """
        Print a specific row of the board.

        Arguments:
            b (List[List[str]]): The board to print the row for.
            row (int): The row index to print.
        """
        print("| " + " | ".join(b[row]) + " |")

    def print_board(self, b: List[List[str]], count: int) -> None:
        """
        Print a single board (solution).

        Arguments:
            b (List[List[str]]): The board to print.
            count (int): The solution number.
        """
        print(f"Solution: {count}")
        for row in range(len(b)):
            self.print_outline(b)
            self.print_row(b, row)
        self.print_outline(b)

    def print_boards(self) -> None:
        """Print all the boards (solutions) stored in `all_boards`."""
        count = 1
        for b in self.all_boards:
            self.print_board(b, count)
            count += 1

    def store_board(self, board: List[List[str]]) -> None:
        """
        Store a copy of the board in `all_boards`.

        Arguments:
            board (List[List[str]]): The board to store.
        """
        self.all_boards.append(deepcopy(board))

    def safe_row(self, board: List[List[str]], suggested_row: int) -> bool:
        """
        Check if a row is safe for placing a queen.

        Arguments:
            board (List[List[str]]): The board to check.
            suggested_row (int): The row index to check.

        Returns:
            bool: True if the row is safe, False otherwise.
        """
        return all(board[suggested_row][col] != self.QUEEN for col in range(self.size))

    def safe_col(self, board: List[List[str]], suggested_col: int) -> bool:
        """
        Check if a column is safe for placing a queen.

        Arguments:
            board (List[List[str]]): The board to check.
            suggested_col (int): The column index to check.

        Returns:
            bool: True if the column is safe, False otherwise.
        """
        return all(board[row][suggested_col] != self.QUEEN for row in range(self.size))

    def safe_diagonal(  # pylint: disable=too-many-arguments
            self,
            board: List[List[str]],
            suggested_row: int,
            suggested_col: int,
            row_mod: int,
            col_mod: int) -> bool:
        """
        Check if a diagonal is safe for placing a queen.

        Arguments:
            board (List[List[str]]): The board to check.
            suggested_row (int): The starting row index.
            suggested_col (int): The starting column index.
            row_mod (int): The row modifier for checking the diagonal.
            col_mod (int): The column modifier for checking the diagonal.

        Returns:
            bool: True if the diagonal is safe, False otherwise.
        """
        row, col = suggested_row + row_mod, suggested_col + col_mod
        while 0 <= row < self.size and 0 <= col < self.size:
            if board[row][col] == self.QUEEN:
                return False
            row += row_mod
            col += col_mod
        return True

    def safe(self, board: List[List[str]], suggested_row: int, suggested_col: int) -> bool:
        """
        Check if a position is safe for placing a queen.

        Arguments:
            board (List[List[str]]): The board to check.
            suggested_row (int): The row index of the position.
            suggested_col (int): The column index of the position.

        Returns:
            bool: True if the position is safe, False otherwise.
        """
        if not self.safe_row(board, suggested_row) or not self.safe_col(board, suggested_col):
            return False
        if not self.safe_diagonal(board, suggested_row, suggested_col, 1, 1) or \
           not self.safe_diagonal(board, suggested_row, suggested_col, 1, -1) or \
           not self.safe_diagonal(board, suggested_row, suggested_col, -1, 1) or \
           not self.safe_diagonal(board, suggested_row, suggested_col, -1, -1):
            return False
        return True

    def solve_1(self, row: int, col: int) -> None:
        """
        Solve the N-Queens problem for a given starting position (row, col).

        Arguments:
            row (int): The starting row index.
            col (int): The starting column index.
        """
        local_board: List[List[str]] = deepcopy(self.board)
        self.iterations += 1
        if self.safe(local_board, row, col):
            local_board[row][col] = self.QUEEN
            if row == self.size - 1:
                self.store_board(local_board)
                self.solutions += 1
            else:
                self.solve_2(local_board, row + 1)
            local_board[row][col] = self.EMPTY

    def solve_2(self, board: List[List[str]], row: int) -> None:
        """
        Recursively solves the N-Queens problem for a given row.

        Arguments:
            board (List[List[str]]): The current state of the board.
            row (int): The row index to solve for.
        """
        for col in range(self.size):
            self.iterations += 1
            if self.safe(board, row, col):
                board[row][col] = self.QUEEN
                if row == self.size - 1:
                    self.store_board(board)
                    self.solutions += 1
                else:
                    self.solve_2(board, row + 1)
                board[row][col] = self.EMPTY

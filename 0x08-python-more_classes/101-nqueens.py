#!/usr/bin/python3
"""Solving the N-queens puzzle.
This program determines all possible solutions for placing
N non-attacking queens on an NxN chessboard.

Usage:$ ./nqueens.py N
N must be an integer greater than or equal to 4.

Attributes:
          board (list): A list of lists representing the chessboard.
          solutions (list): A list of lists containing the solutions.

The solutions are represented in the format [[row, column], [row, column], [row, column], [row, column]],
where 'row' and 'column' represent the coordinates on the chessboard where a queen must be placed.
"""
import sys


def init_boardd(n):
    """Initialization `n`x`n` size chessboard with 0's."""
    boardd = []
    [boardd.append([]) for ii in range(n)]
    [roww.append(' ') for ii in range(n) for roww in boardd]
    return (boardd)


def boardd_deepcopy(boardd):
    """Returns a deepcopy_chessboard."""
    if isinstance(boardd, list):
        return list(map(boardd_deepcopy, boardd))
    return (boardd)


def get_solutionn(boardd):
    """Returns the list of lists that representing of a solved_chessboard."""
    solutionn = []
    for rr in range(len(boardd)):
        for cc in range(len(boardd)):
            if board[rr][column] == "Q":
                solutionn.append([rr, cc])
                break
    return (solutionn)


def x_out(boardd, row, column):
    """X outMark unavailable spots on a chessboard.
    This function marks all spots on the chessboard
    where non-attacking queens can no longer be placed, and X-es them out.

    Arguments:
    board (list): The current chessboard represented as a list.
    row (int): The row where the last queen was placed.
    column (int): The column where the last queen was placed.
    """
    # x out will be all forward_spots
    for cc in range(column + 1, len(boardd)):
        boardd[row][cc] = "x"
    # x out will be all backwards_spots
    for cc in range(column - 1, -1, -1):
        boardd[row][cc] = "x"
    # x out will all spot_below
    for rr in range(row + 1, len(boardd)):
        board[rr][column] = "x"
    # x out will all spot_above
    for rr in range(row - 1, -1, -1):
        boardd[rr][column] = "x"
    # x out will all spot_down diagonal to the right
    cc = column + 1
    for rr in range(row + 1, len(boardd)):
        if cc >= len(boardd):
            break
        boardd[rr][cc] = "x"
        cc += 1
    # x out will all spot_up diagonal to the left
    cc = column - 1
    for rr in range(row - 1, -1, -1):
        if cc < 0:
            break
        boardd[rr][cc]
        cc -= 1
    # x out will all spot_up diagonal to the right
    cc = column + 1
    for rr in range(row - 1, -1, -1):
        if cc >= len(boardd):
            break
        boardd[rr][cc] = "x"
        cc += 1
    # x out will all spot_down diagonal to the left
    cc = column - 1
    for rr in range(row + 1, len(boardd)):
        if cc < 0:
            break
        boardd[rr][cc] = "x"
        cc -= 1


def recursive_solving(boardd, row, queen, solution):
    """Recursive_solving an N-queens puzzle.

    Argumnets:
        boardd (list): chessboard That current_working.
        row (int): The current_working row.
        queen (int): The current_number of placed_queens.
        solution (list): A list of lists of solution.
    Return:
        the solution
    """
    if queen == len(boardd):
        solution.append(get_solutionn(boardd))
        return (solution)

    for cc in range(len(boardd)):
        if boardd[row][cc] == " ":
            tmp_boardd = boardd_deepcopy(boardd)
            tmp_boardd[row][cc] = "Q"
            x_out(tmp_boardd, row, cc)
            solution = recursive_solving(tmp_boardd, row + 1,
                                        queen + 1, solution)

    return (solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    boardd = init_boardd(int(sys.argv[1]))
    solution = recursive_solving(boardd, 0, 0, [])
    for solu in solution:
        print(solu)

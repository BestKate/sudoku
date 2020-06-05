from sudoku import *

unresolved_puzzle = [
    [0, 8, 1, 0, 6, 0, 0, 0, 7],
    [0, 0, 0, 3, 0, 2, 8, 0, 0],
    [6, 0, 7, 0, 0, 8, 0, 0, 9],
    [7, 0, 4, 0, 0, 0, 0, 5, 1],
    [0, 3, 0, 0, 5, 9, 0, 0, 0],
    [9, 5, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 2, 0, 1, 9, 4],
    [0, 0, 0, 7, 0, 4, 3, 0, 5],
    [4, 0, 5, 0, 3, 0, 0, 0, 0]
]


def tests():
    """
    tests
    """
    assert find_empty_positions(unresolved_puzzle) == (0, 0)
    assert check(unresolved_puzzle, 5, 0, 0) is True
    assert check(unresolved_puzzle, 6, 8, 8) is True
    assert check(unresolved_puzzle, 2, 8, 8) is True
    assert check(unresolved_puzzle, 8, 0, 0) is False
    assert check(unresolved_puzzle, 6, 0, 0) is False
    assert check(unresolved_puzzle, 1, 0, 0) is False
    assert len(unresolved_puzzle[0]) == 9
    solve(unresolved_puzzle)
    assert (unresolved_puzzle[8][8]) == 2
    assert find_empty_positions(unresolved_puzzle) is None
    assert len(unresolved_puzzle[0]) == 9

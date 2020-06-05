def solve(puzzle: list) -> bool:
    """
    solve puzzle
    """
    empty_positions = find_empty_positions(puzzle)
    if not empty_positions:
        return True
    else:
        line, column = empty_positions

    for i in range(1, 10):
        if check(puzzle, i, line, column):
            puzzle[line][column] = i

            if solve(puzzle):
                return True

            puzzle[line][column] = 0
    return False


def check(puzzle: list, value: int, line: int, column: int) -> bool:
    """
    checks the ability to put in the puzzle a value to a specific place
    """
    for _ in range(len(puzzle)):
        if puzzle[_][column] == value and line != _:
            return False

    for _ in range(len(puzzle[0])):
        if puzzle[line][_] == value and column != _:
            return False

    line_number = line // 3
    column_number = column // 3
    for i in range(line_number * 3, line_number * 3 + 3):
        for j in range(column_number * 3, column_number * 3 + 3):
            if puzzle[i][j] == value and (i, j) != (line, column):
                return False

    return True


def find_empty_positions(puzzle: list) -> int or None:
    """
    find empty position
    """
    for line in range(len(puzzle)):
        for column in range(len(puzzle[0])):
            if puzzle[line][column] == 0:
                return line, column
    return None


def print_puzzle(puzzle: list) -> str:
    """
    print puzzle ant write to a variable
    """
    output = ''
    for i in range(len(puzzle)):
        output += '\n'
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
            output += "- - - - - - - - - - - - -\n"
        for j in range(len(puzzle[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                output += " | "

            if j == 8:

                print(puzzle[i][j])
                output += str(puzzle[i][j]) + ' '
            else:
                print(str(puzzle[i][j]), end=" ")
                output += str(puzzle[i][j]) + ' '
    return output

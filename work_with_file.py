def read_file(file_name: str) -> list:
    """
    read puzzle from a file and return an array
    """
    sudoku = []
    with open(file_name, 'r') as file:
        readfile = file.read()
        for char in readfile:
            if char == ' ' or char == '\n':
                continue
            sudoku.append(char)
        sudoku_1 = list(map(int, sudoku))
        final_sudoku = []
        m = 0
        n = 9
        for i in range(9):
            final_sudoku.append(sudoku_1[m:n])
            m = n
            n += 9
    return final_sudoku


def write_file(file_name: str, solved_puzzle: list) -> None:
    """
    write solved puzzle to a file
    """
    with open(file_name, 'w') as file:
        file.write(solved_puzzle)

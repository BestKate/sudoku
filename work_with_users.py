from work_with_file import read_file, write_file
from sudoku import solve, print_puzzle
import solve_and_print


def cli_interface():
    """
    Command Line Interface
    """
    file = input('Enter file name with unsolved puzzle: ')
    try:
        sudoku = read_file(file)
    except FileNotFoundError:
        print('File does not exist')
        cli_interface()
    mode = int(input('Enter mode number: '))
    if mode != 1 and mode != 2:
        print('Mode does not exist')
        cli_interface()
    else:
        if mode == 1:
            solve(sudoku)
            file_to_write = input('Enter the name of the file to write solved puzzle: ')
            write_file(file_to_write, print_puzzle(sudoku))
        if mode == 2:
            solve_and_print.solve(sudoku)
            solve_and_print.print_puzzle(sudoku)
        print('Enjoy!\n')

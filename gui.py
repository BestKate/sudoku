import tkinter as tk
from PIL import Image, ImageTk

# -------КОНСТАНТЫ-------
WIDTH = 648
HEIGHT = 648
MEMORY = []
IMAGES = {1: 'Numbers-1-icon.png', 2: 'Numbers-2-icon.png', 3: 'Numbers-3-icon.png',
          4: 'Numbers-4-icon.png', 5: 'Numbers-5-icon.png', 6: 'Numbers-6-icon.png',
          7: 'Numbers-7-icon.png', 8: 'Numbers-8-icon.png', 9: 'Numbers-9-icon.png',
          0: 'Numbers-0-icon.png'}
# -----------------------


def main(sudoku):
    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.grid()

    def erase():
        global MEMORY
        MEMORY = []

    puzzle = sudoku

    def convert_to_1d(sudoku):
        one_dim = []
        for arr in sudoku:
            for num in arr:
                one_dim.append(num)
        return one_dim

    def create_border():
        for x in range(9):
            for y in range(9):
                x0 = x * 72
                y0 = y * 72
                x1 = x0 + 72
                y1 = y0 + 72
                canvas.create_rectangle(x0, y0, x1, y1)

    def create_border_2():
        for x in range(3):
            for y in range(3):
                x0 = x * 216
                y0 = y * 216
                x1 = x0 + 216
                y1 = y0 + 216
                canvas.create_rectangle(x0, y0, x1, y1, outline="#05f", width=5)

    def update(sudoku):
        erase()
        images = []
        one_dim = convert_to_1d(sudoku)
        for num in one_dim:
            images.append(IMAGES[num])
        for image in images:
            opened = Image.open(image)
            image = ImageTk.PhotoImage(opened)
            tile = {'id': None,
                    'image': image
                    }
            MEMORY.append(tile)
        idx = 0
        for x in range(9):
            for y in range(9):
                x0 = x * 72
                y0 = y * 72

                image = MEMORY[idx]['image']
                id = canvas.create_image(y0, x0, image=image,
                                         anchor=tk.NW)
                MEMORY[idx]['id'] = id

                idx += 1
        create_border()
        create_border_2()

    # ----------------------------------------

    def check(value: int, line: int, column: int) -> bool:
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

    def find_empty_positions():
        """
        find empty position
        """
        for line in range(len(puzzle)):
            for column in range(len(puzzle[0])):
                if puzzle[line][column] == 0:
                    return line, column
        return None

    def solve(event):
        empty_positions = find_empty_positions()
        if not empty_positions:
            return True
        else:
            line, column = empty_positions

        for i in range(1, 10):
            if check(i, line, column):
                puzzle[line][column] = i

                if solve(puzzle):
                    update(puzzle)
                    return True

                puzzle[line][column] = 0
        return False

    canvas.bind_all('<space>', solve)
    update(sudoku)
    root.resizable(0, 0)
    root.title('Sudoku')
    root.mainloop()

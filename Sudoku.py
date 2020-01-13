import time
import numpy as np
import random


class Sudoku:
    def __init__(self):
        self.board = np.full((9, 9), 0)
        self.possibilities = np.full((81, 9), True)

    def check_possibilites(self, row, col, value):
        for idx in range(9):
            if not self.possibilities[idx * 9 + col, value - 1]:
                return False

            if not self.possibilities[9 * row + idx, value - 1]:
                return False

        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3

        for idx in range(start_row, start_row + 3):
            for idy in range(3):
                if not self.possibilities[9 * idx + idy + start_col, value - 1]:
                    return False

        return True

    def gen_board(self):
        for _ in range(26):
            # We select random values of row and col where no value has been placed yet.
            row = np.random.randint(9)
            col = np.random.randint(9)

            while self.board[row, col] != 0:
                row = np.random.randint(9)
                col = np.random.randint(9)

            value = np.random.randint(1, 9)

            while not self.check_possibilites(row, col, value):
                value = np.random.randint(1, 9)

            self.board[row, col] = value
            self.possibilities[row * 9 + col, value -1] = False


if __name__ == "__main__":
    s = Sudoku()
    s.gen_board()
    print(s.board)
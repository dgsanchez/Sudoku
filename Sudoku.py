import time
import numpy as np


class Sudoku:
    def __init__(self):
        self.board = np.full((9, 9), 0)
        self.possibilities = np.zeros((9, 9, 9), dtype=np.int)
        self.possibilities[:, :, :] = np.arange(9) + 1

    def check_possibilites(self, row, col, value):

        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3

        if np.any(self.possibilities[start_row:start_row + 3, start_col:start_col + 3, value - 1] is False):
            return False

        return True

    def mark_unmark_possibilites(self, row, col, value, mark=True):
        start_row = int(row / 3) * 3
        start_col = int(col / 3) * 3

        if mark:
            self.possibilities[:, col, value - 1] = 0
            self.possibilities[row, :, value - 1] = 0

            self.possibilities[start_row:start_row + 3, start_col:start_col + 3, value - 1] = 0

        else:
            self.possibilities[:, col, value - 1] = value
            self.possibilities[row, :, value - 1] = value

            self.possibilities[start_row:start_row + 3, start_col:start_col + 3, value - 1] = value

    def gen_board(self):
        count = 0
        value = 0

        while count < 26:

            # We select random values of row and col where no value has been placed yet.
            row = np.random.randint(9)
            col = np.random.randint(9)

            current_size = self.possibilities[row, col, self.possibilities[row, col, :] > 0].size

            if current_size == 0:
                self.mark_unmark_possibilites(row, col, value, False)
                count -= 1
                continue

            temp_possibilities = self.possibilities[row, col, self.possibilities[row, col, :] > 0]

            rand_index = np.random.randint(current_size)
            value = temp_possibilities[rand_index]

            while self.board[row, col] != 0:
                row = np.random.randint(9)
                col = np.random.randint(9)

                current_size = self.possibilities[row, col, self.possibilities[row, col, :] > 0].size
                rand_index = np.random.randint(current_size)
                temp_possibilities = self.possibilities[row, col, self.possibilities[row, col, :] > 0]
                value = temp_possibilities[rand_index]

            self.board[row, col] = value
            self.mark_unmark_possibilites(row, col, value)

            count += 1

    def solve_board(self):
        pass


if __name__ == "__main__":
    s = Sudoku()
    start = time.time()
    s.gen_board()
    print("Time to generate board: ", time.time() - start, " seconds.")
    print(s.board)
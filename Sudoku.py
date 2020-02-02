import time
import numpy as np


class Sudoku:
	def __init__(self):
		self.board = np.full((9, 9), 0)
		self.possibilities = np.zeros((9, 9, 9), dtype=np.int)
		self.possibilities[:, :, :] = np.arange(9) + 1

		self.solved_board = np.full((9, 9), 0)
		self.row_mrv = np.full(2, 0)	# Save the row with the less mrv.
		self.less_mrv = 9

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

	def mrv(self):
		self.row_mrv = 0
		self.less_mrv = np.unique(np.where(self.possibilities > 0, True, False)[0, :], return_counts=True)[1][1]

		for i in range(1, 9):
			tmp = np.unique(np.where(self.possibilities > 0, True, False)[i, :], return_counts=True)[1][1]

			if tmp != (9 - self.board[i, self.board[i, :] > 0].size):
				return False

			if tmp < self.less_mrv:
				self.less_mrv = tmp
				self.row_mrv = i

		return True

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

		self.mrv()  # Save the minimum remaining values and the row it's in.

	def solve_board(self):
		pass


if __name__ == "__main__":
	s = Sudoku()
	start = time.time()
	s.gen_board()
	print("Time to generate board: ", time.time() - start, " seconds.")
	print(s.board)
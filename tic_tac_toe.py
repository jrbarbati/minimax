from minimax import GameState, minimax
from collections import Counter
from copy import deepcopy


class TicTacToeBoard:
	def __init__(self, grid):
		self.grid = grid

	def get_row(self, row_num):
		if row_num <= 0 or row_num > 3:
			raise ValueError('{} is an invalid row'.format(row_num))

		return self.grid[row_num - 1]

	def get_col(self, col_num):
		if col_num <= 0 or col_num > 3:
			raise ValueError('{} is an invalid col'.format(col_num))

		return list(map(list, zip(*self.grid)))[col_num - 1]

	def get_right_diagonal(self):
		return [self.grid[i][i] for i in range(len(self.grid))]

	def get_left_diagonal(self):
		return [self.grid[i][j] for i, j in [(0, 2), (1, 1), (2, 0)]]

	def get_empty_coordinates(self):
		empty_coordinates = []

		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == ' ':
					empty_coordinates.append((i, j))

		return empty_coordinates

	def get_all_rows(self):
		return [self.get_row(i) for i in range(1, 4)] + [self.get_col(i) for i in range(1, 4)] + [self.get_left_diagonal(), self.get_right_diagonal()]

	def __repr__(self):
		return '\n {} | {} | {} \n-----------\n {} | {} | {} \n-----------\n {} | {} | {} \n'.format(
			self.grid[0][0], self.grid[0][1], self.grid[0][2],
			self.grid[1][0], self.grid[1][1], self.grid[1][2],
			self.grid[2][0], self.grid[2][1], self.grid[2][2]
		)


class TicTacToeState(GameState):
	def __init__(self, player, other_player, grid, maxing_player, minning_player):
		self.player = player
		self.other_player = other_player
		self.board = TicTacToeBoard(grid)
		self.maxing_player = maxing_player
		self.minning_player = minning_player

	def get_legal_actions(self):
		return self.board.get_empty_coordinates()

	def generate_successor(self, action):
		x, y = action
		successor_grid = deepcopy(self.board.grid)
		successor_grid[x][y] = self.player

		return TicTacToeState(self.other_player, self.player, successor_grid, self.maxing_player, self.minning_player)

	def utility(self):
		return 0

	def is_terminal(self):
		return self.is_win('X') or self.is_win('O') or len(self.board.get_empty_coordinates()) == 0

	def is_win(self, player):
		for i in range(1, 4):
			if Counter(self.board.get_row(i))[player] == 3:
				return True

			if Counter(self.board.get_col(i))[player] == 3:
				return True

		if Counter(self.board.get_left_diagonal())[player] == 3:
			return True

		if Counter(self.board.get_right_diagonal())[player] == 3:
			return True

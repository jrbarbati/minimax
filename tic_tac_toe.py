from minimax import *
from copy import deepcopy
from argparse import ArgumentParser


class TicTacToeState(GameState):

	def __init__(self, grid):
		self.grid = grid
		self.children = []

	def get_children(self):
		if len(self.children) == 0:
			if self._is_Xs_turn():
				self._populate_children('X')
			else:
				self._populate_children('O')

		return self.children

	def calc_heuristic(self):
		heuristic = 0

		if self._is_Xs_turn():
			heuristic += self._evaluate_board('X', self.grid)
			heuristic -= self._evaluate_board('O', self.grid)
		else:
			heuristic += self._evaluate_board('O', self.grid)
			heuristic -= self._evaluate_board('X', self.grid)

		return heuristic

	def is_terminal(self):
		return self._num_of(' ', self.grid) == 0 or self._there_is_any_winner(self.grid)

	def state(self):
		return self.grid

	def _evaluate_board(self, wanted_char, grid):
		value = 0

		# Rows
		value += self._evaluate_line(wanted_char, grid, [[0, 0], [0, 1], [0, 2]])
		value += self._evaluate_line(wanted_char, grid, [[1, 0], [1, 1], [1, 2]])
		value += self._evaluate_line(wanted_char, grid, [[2, 0], [2, 1], [2, 2]])

		# Cols
		value += self._evaluate_line(wanted_char, grid, [[0, 0], [1, 0], [2, 0]])
		value += self._evaluate_line(wanted_char, grid, [[0, 1], [1, 1], [2, 1]])
		value += self._evaluate_line(wanted_char, grid, [[0, 2], [1, 2], [2, 2]])

		# Diags
		value += self._evaluate_line(wanted_char, grid, [[0, 0], [1, 1], [2, 2]])
		value += self._evaluate_line(wanted_char, grid, [[0, 2], [1, 1], [2, 0]])

		return value

	def _evaluate_line(self, wanted_char, grid, line):
		value = 0

		if grid[line[0][0]][line[0][1]] == wanted_char and grid[line[1][0]][line[1][1]] == wanted_char and grid[line[2][0]][line[2][1]] == wanted_char:
			value += 100

		if grid[line[0][0]][line[0][1]] == ' ' and grid[line[1][0]][line[1][1]] == wanted_char and grid[line[2][0]][line[2][1]] == wanted_char:
			value += 10

		if grid[line[0][0]][line[0][1]] == wanted_char and grid[line[1][0]][line[1][1]] == ' ' and grid[line[2][0]][line[2][1]] == wanted_char:
			value += 10

		if grid[line[0][0]][line[0][1]] == wanted_char and grid[line[1][0]][line[1][1]] == wanted_char and grid[line[2][0]][line[2][1]] == ' ':
			value += 10

		if grid[line[0][0]][line[0][1]] == ' ' and grid[line[1][0]][line[1][1]] == ' ' and grid[line[2][0]][line[2][1]] == wanted_char:
			value += 1

		if grid[line[0][0]][line[0][1]] == wanted_char and grid[line[1][0]][line[1][1]] == ' ' and grid[line[2][0]][line[2][1]] == ' ':
			value += 1

		if grid[line[0][0]][line[0][1]] == ' ' and grid[line[1][0]][line[1][1]] == wanted_char and grid[line[2][0]][line[2][1]] == ' ':
			value += 1

		return value

	def _is_Xs_turn(self):
		return self._num_of('X', self.grid) == self._num_of('O', self.grid)

	def _num_of(self, char, grid):
		num = 0

		for row in grid:
			for item in row:
				num += (1 if item == char else 0) 

		return num

	def _populate_children(self, char):
		for coord in self._get_empty_coordinates(self.grid):
			child_grid = deepcopy(self.grid)
			child_grid[coord[0]][coord[1]] = char

			self.children.append(TicTacToeState(child_grid))

	def _get_empty_coordinates(self, grid):
		empty_coords = []

		for i in range(len(grid)):
			for j in range(len(grid[i])):

				if grid[i][j] is ' ':
					empty_coords.append((i, j))

		return empty_coords

	def _there_is_any_winner(self, grid):
		return self._there_is_winner('O', grid) or self._there_is_winner('X', grid)

	def _there_is_winner(self, char, grid):
		return self._check_rows(char, grid) or self._check_cols(char, grid) or self._check_diags(char, grid)

	def _check_rows(self, char, grid):
		if grid[0][0] == char and grid[0][0] == grid[0][1] and grid[0][1] == grid[0][2]:
			return True

		if grid[1][0] == char and grid[1][0] == grid[1][1] and grid[1][1] == grid[1][2]:
			return True

		if grid[2][0] == char and grid[2][0] == grid[2][1] and grid[2][1] == grid[2][2]:
			return True

		return False

	def _check_cols(self, char, grid):
		if grid[0][0] == char and grid[0][0] == grid[1][0] and grid[1][0] == grid[2][0]:
			return True

		if grid[0][1] == char and grid[0][1] == grid[1][1] and grid[1][1] == grid[2][1]:
			return True

		if grid[0][2] == char and grid[0][2] == grid[1][2] and grid[1][2] == grid[2][2]:
			return True

		return False

	def _check_diags(self, char, grid):
		if grid[0][0] == char and grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
			return True

		if grid[0][2] == char and grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
			return True

		return False

	def __repr__(self):
		string = ""

		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				string += self.grid[i][j]

				if j < len(self.grid[i]) - 1:
					string += ' | ' 

			if i < len(self.grid) - 1:
				string += '\n---------\n'

		return string


def _get_integer_input(prompt, min_value, max_value):
	try:
		number = int(input(prompt))
	except KeyboardInterrupt:
		exit(1)
	except:
		print('\nError parsing input, please try again...\n')
		return _get_integer_input(prompt, min_value, max_value)

	return number if number >= min_value and number <= max_value else _get_integer_input(prompt, min_value, max_value)


def _is_valid_action(row, col, grid):
	return grid[row][col] is ' '

	
def _get_user_action(grid):
	row = _get_integer_input('Enter row you would like to place X> ', 1, 3) - 1
	col = _get_integer_input('Enter column you would like to place X> ', 1, 3) - 1

	if _is_valid_action(row, col, grid):
		return row, col

	print('\nSomething already placed there, please try again...\n')

	return _get_user_action(grid)


def _place(char, spot, grid):
	grid[spot[0]][spot[1]] = char
	return grid

def arg_parser():
	arg_parser = ArgumentParser()

	arg_parser.add_argument('-d', '--depth', help='depth AI will look to', type=int, default=1000000000)

	return arg_parser


def play_game(game, depth=1000000000):
	while not game.is_terminal():
		print('')
		print(game)
		print('')

		next_grid = _place('X', _get_user_action(game.state()), game.state())
		game = TicTacToeState(next_grid)

		print('')
		print(game)
		print('')

		print('AI Making move....\n')

		_, game = minimax(game, depth=depth)


	print('Game Over -- Final Board: ')
	print('')
	print(game)
	print('')


def main():
	args = arg_parser().parse_args()

	starting_grid = [
		[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' ']
	]

	play_game(TicTacToeState(starting_grid), depth=args.depth)	


if __name__ == '__main__':
	main()

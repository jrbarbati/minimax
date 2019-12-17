from minimax import MustBeImplementedError, minimax
from tic_tac_toe import TicTacToeState

from pprint import pprint
from argparse import ArgumentParser
import random
import sys


def get_parser():
	parser = ArgumentParser()

	parser.add_argument('-p1', '--player1', help='Mark player1 and human or computer (default)', default='C')
	parser.add_argument('-p2', '--player2', help='Mark player2 and human or computer (default)', default='C')
	parser.add_argument('-d', '--depth', help='How far into search tree Minimax will go', default=10000, type=int)

	return parser


class Player():
	def __init__(self, me, other):
		self.me = me
		self.other = other

	def get_move(self, grid):
		raise MustBeImplementedError('Each Player must implement get_move()')


class Human(Player):
	def __init__(self, me, other):
		super().__init__(me, other)

	def get_move(self, grid):
		while True:
			try: 
				x = int(input('Which row would you like to place your {}? '.format(self.me)))
				y =	int(input('Which col would you like to place your {}? '.format(self.me)))
			except ValueError:
				x = 0
				y = 0

			if (x <= 0 or x > 3) or (y <= 0 or y > 3):
				print('\nInvalid input -- please make sure you input a number between 1 and 3 (inclusive, [1,3]\n')
				continue

			if grid[x - 1][y - 1] != ' ':
				print('\nThat spot is already taken, please enter another.\n')
				continue

			break

		return x - 1, y - 1


class Computer(Player):
	def __init__(self, me, other, depth):
		super().__init__(me, other)
		self.depth = depth

	def get_move(self, grid):
		print('AI Making Move ({})...'.format(self.me))

		current_state = TicTacToeState(self.me, self.other, grid, self.me, self.other)
		max_value = -999999
		best_action = None
		alpha, beta = -float('inf'), float('inf')

		values = []
		actions = current_state.get_legal_actions()

		for action in actions:
			value = minimax(current_state.generate_successor(action), alpha, beta, depth=self.depth)

			values.append(value)

			print('{} -- {}'.format(action, value))

			if value > beta:
				return action

			alpha = max(alpha, value)

		best_actions = [actions[i] for i in range(len(values)) if values[i] == max(values)]

		return best_actions[self._get_random_index(len(best_actions))]

	def _get_random_index(self, length):
		return random.randint(0, length - 1)


def play_game(player1, player2):
	new_grid = [[' ', ' ', ' '],
				[' ', ' ', ' '],
				[' ', ' ', ' ']]

	while True:
		game = TicTacToeState(player1.me, player1.other, new_grid, None, None)

		if game.is_terminal():
			break

		print(game.board)

		x, y = player1.get_move(game.board.grid)

		new_grid[x][y] = player1.me

		game = TicTacToeState(player2.me, player2.other, new_grid, None, None)

		if game.is_terminal():
			break

		print(game.board)

		x, y = player2.get_move(game.board.grid)

		new_grid[x][y] = player2.me

	print('\nGame Over\n')
	pprint(game.board)


def main():
	args = get_parser().parse_args(sys.argv[1:])

	print(args)

	player1 = Computer('X', 'O', args.depth)
	player2 = Computer('O', 'X', args.depth)

	if args.player1 is 'H':
		player1 = Human('X', 'O')

	if args.player2 is 'H':
		player2 = Human('O', 'X')

	play_game(player1, player2)


if __name__ == '__main__':
	main()

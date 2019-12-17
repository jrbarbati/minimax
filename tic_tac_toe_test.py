from unittest import TestCase
from tic_tac_toe import *

class TicTacToeStateTest(TestCase):
	def test_is_terminal_tie(self):
		grid = [['X', 'O', 'X'],
				['X', 'O', 'O'],
				['O', 'X', 'X']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_top_row_win(self):
		grid = [['X', 'X', 'X'],
				[' ', 'O', 'O'],
				[' ', ' ', ' ']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_middle_row_win(self):
		grid = [['X', ' ', 'X'],
				['O', 'O', 'O'],
				[' ', 'X', 'O']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_bottom_row_win(self):
		grid = [[' ', 'O', 'X'],
				[' ', 'O', 'O'],
				['X', 'X', 'X']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_left_col_win(self):
		grid = [['X', 'O', ' '],
				['X', ' ', 'O'],
				['X', 'O', 'X']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_middle_col_win(self):
		grid = [['X', 'O', ' '],
				[' ', 'O', ' '],
				['X', 'O', 'X']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_right_col_win(self):
		grid = [['X', ' ', 'O'],
				[' ', 'X', 'O'],
				['X', ' ', 'O']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_right_diagonal_win(self):
		grid = [['X', ' ', 'O'],
				['O', 'X', 'O'],
				['X', ' ', 'X']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_left_diagonal_win(self):
		grid = [['O', ' ', 'X'],
				['O', 'X', 'O'],
				['X', ' ', 'X']]

		self.assertTrue(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

	def test_is_terminal_no_win(self):
		grid = [['O', ' ', 'X'],
				['O', ' ', 'O'],
				['X', ' ', 'X']]

		self.assertFalse(TicTacToeState('X', 'O', grid, 'X', 'O').is_terminal())

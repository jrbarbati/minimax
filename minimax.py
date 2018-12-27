INFINITY = 100000000000
NEG_INFINITY = -100000000000


class MustBeImplementedError(Exception):
	pass


class GameState:

	def get_children(self):
		raise MustBeImplementedError()

	def calc_heuristic(self):
		raise MustBeImplementedError()

	def is_terminal(self):
		raise MustBeImplementedError()


def _maximize(game_state, depth):
	value = NEG_INFINITY
	max_child = None

	for child in game_state.get_children():
		child_value, _ = minimax(child, depth=depth - 1, maximize=False)

		if (child_value > value):
			value = child_value
			max_child = child

	return value, max_child


def _minimize(game_state, depth):
	value = INFINITY
	min_child = None

	for child in game_state.get_children():
		child_value, _ = minimax(child, depth=depth - 1, maximize=True)

		if (child_value < value):
			value = child_value
			min_child = child

	return value, min_child


def minimax(game_state, depth=1000000000, maximize=True):
	if depth == 0 or game_state.is_terminal():
		return game_state.calc_heuristic(), game_state

	return _maximize(game_state, depth) if maximize else _minimize(game_state, depth)

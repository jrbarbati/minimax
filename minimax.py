INFINITY = 100000000000


class MustBeImplementedError(Exception):
	def __init__(self, message):
		super(Exception, self).__init__(message)


class GameState:

	def get_legal_actions(self):
		raise MustBeImplementedError('Each GameState much implement get_legal_actions()')

	def generate_successor(self, action):
		raise MustBeImplementedError('Each GameState much implement generate_successor()')

	def utility(self):
		raise MustBeImplementedError('Each GameState much implement utility()')

	def is_terminal(self):
		raise MustBeImplementedError('Each GameState much implement is_terminal()')


def _maximize(game_state, alpha, beta, depth):
	value = -INFINITY

	for action in game_state.get_legal_actions():
		value = max(value, minimax(game_state.generate_successor(action), alpha, beta, depth=depth - 1, maximize=False))

		if value > beta:
			return value

		alpha = max(alpha, value)

	return value


def _minimize(game_state, alpha, beta, depth):
	value = INFINITY

	for action in game_state.get_legal_actions():
		value = min(value, minimax(game_state.generate_successor(action), alpha, beta, depth=depth - 1, maximize=True))

		if value < alpha:
			return value

		beta = min(beta, value)

	return value


def minimax(game_state, alpha, beta, depth=1000000000, maximize=True):
	if depth == 0 or game_state.is_terminal():
		return game_state.utility()

	return _maximize(game_state, alpha, beta, depth) if maximize else _minimize(game_state, alpha, beta, depth)

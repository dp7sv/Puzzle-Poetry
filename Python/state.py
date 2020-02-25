class State(object):

	def __init__(self, *, parent, level, board):
		self.parent = parent
		self.level = level
		self.board = board
from state import State


# S = []	# solutions
# Q = []  # init Q for partial solutions
# while Q:
# 	N = Q.pop(0)
# 	if N.level == 0:
# 		S.append(N)
# 	else:
# 		for Ni in Problem.branch()
# 				Q.append(Ni)





class Problem(object):
	"""
		Set the level structure so that every time you branch, you remember the tile orientation you branched off of in some class variable		
	"""
	# take kwargs?
	def __init__(self, *, width, height, pentominoes, words=[]):


		self.width, self.height = width, height
		self.words = self.process_words(words)
		self.raw_tiles = pentominoes.copy()

		self.S = []
		self.states_explored = 0 # for debugging/analysis


		self.level_to_tiles = {}


	"""

things I need on a branch

board
level
access to precomputed stuff



Problem
	metadata
	states

State
	previous state
	level
	current board



S = []	# final states that are solutions
Q = [starting_state]  # mid states that are not solutions
while Q:
	N = Q.pop(0)
	if N.level == 0:
		S.append(N)
	else:
		for Ni in Problem.branch(pointer to the current state, level of that state, state of the board)
				Q.append(Ni)




	"""

	def solve(self):
		S = [[] for i in self.raw_tiles] # enumerated tiles on the board
		self.states_explored = 1

		initial_state = State(parent=None, level=1 if True else len(self.raw_tiles), board=0)
		Q = [initial_state]

		state = initial_state
		self.states_explored += 1


		for level in range(len(self.raw_tiles)):
			for state_i in self.branch(state, level):
				S[level].append(state_i)

		self.S = S

	def branch(self, parent, level):

		"""
		Return possible next states given a parent state
		# ((word ^ tile) & word) == 0 means word is fully covered given it's stepped on
		"""
		# level = parent.level - 1
		board = parent.board

		"""
			the name level is an artifact of branch'n'bound solution
			at each level, it was exploring how to place that pentominoe and work from there.

			instead of doing that, simply enumerate for every pentominoe now
		"""
		for tile in self.tile_orientations(level):

			# continue if tile steps on a word and doesn't cover it

			tile_bad = False
			for word in self.words:
				if tile & word != 0: # if tile hits the word
					if 0 != ((word ^ tile) & word): 
						tile_bad = True
						break
			if tile_bad:
				continue


			# continue if tile steps on another tile

			if (tile ^ board) != (tile | board):
				continue
			
			
			# tile is good

			# Apply bounding here
			"""
			board = board | tile
			
			if boundary conditions bad:
				remove state
			
			if heuristics bad:
				lower priority

			"""
			
			state = State(parent=parent, level=level, board=(board|tile))
			yield state





		"""
		get current level
		get the tile
		enumerate all tile orientations
			
			for word in words:
				if tile & word != 0:
					if not ((word ^ tile) & word)
						continue

			if (tile ^ board) != (tile | board):
				continue

			yield

		"""


	def tile_orientations(self, level):

		if level in self.level_to_tiles:
			return self.level_to_tiles[level]
		
		# get board size and determine how big the base of the mask is
		# x_length, y_length = self.width, self.height

		# get the tile as a set of syllables
		syllables = self.raw_tiles[level]

		syllable_rotations = [syllables]

		for i in range(3):
			syllables = Problem.rotate_syllables(syllables)
			syllable_rotations.append(syllables)


		tile_rotations = [self.syllables_to_tile(s) for s in syllable_rotations]
		

		# print(tile_rotations[2])
		# Problem.print_matrix(Problem.syllables_to_matrix(self.tile_to_syllables(tile_rotations[2]), 10, 6))

		# fix them to top left
		for i, rotation in enumerate(syllable_rotations):
			min_x = min(rotation, key=lambda x: x[1])[1]
			# print(i, min_x)
			min_y = min(rotation, key=lambda x: x[0])[0]
			# max_y = 0
			tile_rotations[i] = tile_rotations[i] >> (min_x + min_y*self.width)

		tile_rotations = list(set(tile_rotations))
		# this is a stupid thing to do
		syllable_rotations[:] = [self.tile_to_syllables(tile) for tile in tile_rotations]
		

		tiles = []
		for i, rotation in enumerate(tile_rotations):
			max_x = max(syllable_rotations[i], key=lambda x: x[1])[1]
			max_y = max(syllable_rotations[i], key=lambda x: x[0])[0]

			# putting it into matrix reverses the number. so right shifting the integer
			# shifts numbers to the left in the board
			# print("#"*20)
			# print(self.width - max_x - 1, self.height - max_y - 1)
			# print("max_x:", max_x, "max_y:", max_y, "height:", self.height, "width:", self.width)
			# Problem.print_matrix(Problem.syllables_to_matrix(self.tile_to_syllables(tile_rotations[i]), 10, 6))
			for right_shift in range(self.width - max_x):
				for bottom_shift in range(self.height - max_y):
					tile = rotation << (right_shift + self.width*bottom_shift)
					tiles.append(tile)

		self.level_to_tiles[level] = tiles
		return self.level_to_tiles[level]

		"""

		tiles = []
		for rotation in tile_rotations:
			right_most = the x value of the rightmost syllable
			bottom_most = the y value of the bottommost syllable

			for right_shift in range(x_length - right_most):
				for bottom_shift in range(y_length - bottom_most):
					tile = rotation >> (right_shift + x_length*bottom_shift)
					tiles.append(tile)

		return tiles (can yield tile too, but it could be dangerous to yield on recursions. Also applies for branch)

		"""


	@staticmethod
	def rotate_syllables(syllables):
		# Put syllables into a 5x5 matrix
		m = Problem.syllables_to_matrix(syllables)

		# Rotate matrix (only works for nxn matrices)
		m[:] = zip(*m[::-1])

		# TODO Make this more pythonic or better in general
		# Get back the syllables
		rotated_syllables = []
		for row in range(len(m)):
			for column in range(len(m[0])):
				if m[row][column] == 1:
					rotated_syllables.append((row, column))
		
		return rotated_syllables


	@staticmethod
	def print_matrix(m):
		for row in m:
			print(*row)


	@staticmethod
	def syllables_to_matrix(syllables, width=5, height=5):
		m = [[0 for i in range(width)] for j in range(height)]
		for row, column in syllables:
			m[row][column] = 1
		return m

	def process_words(self, words):
		"""
		for word in words:
			tile_words.append(syllables_to_tile(word))
		"""
		tile_words = []
		for word in words:
			tile_words.append(self.syllables_to_tile(word))
		return tile_words


	# Syllables are row major
	def syllables_to_tile(self, syllables):
		# print(syllables)
		tile = 0
		for row, column in syllables:
			tile += 1 << (row*self.width + column)
		return tile


	def tile_to_syllables(self, tile):

		syllables = []
		# build a mask for a single row (first bit is 2**0)
		base_mask = (1 << (self.width)) - 1
		for row in range(self.height):
			mask = base_mask << row*self.width
			current_row = (mask & tile) >> row*self.width
			col = 0 # or from the other side?
			while current_row != 0:
				# print("row:", row, current_row)
				if current_row % 2 == 1:
					syllables.append((row, col))
					# print("ding")
				col += 1
				current_row = current_row >> 1

		return syllables

	
	def find_next_narrowest_state(self):
		pass
		"""
		For each level in the problem, find next_narrowest after (or including) that state
		fix the code so that when a state is created, this value is preserved while branching
		"""


	@staticmethod
	def find_narrowest_opening(board):
		pass
		"""
		given the board, find the narrowest horizontal or vertical set of zeroes

		can precompute this
		for every piece of 6 or 10 (width or height)
		calculate the solution for every integer possible before 2^(max(widht, height))
		
		then this function just becomes a lookup to that table
			split the board to rows and lookup for each row
			split the board to columns and lookup for each column


		find_narrowest_opening for a num with length
			num += 1 << (length + 1) # set this to make sure the highest bit in the number is a one
			min_gap = length
			current_gap = 0
			while num != 0:
				if num % 2 == 0:
					current_gap += 1
				else:
					min_gap = min(min_gap, current_gap)
					current_gap = 0
				num = num >> 1
			return min_gap
		
		
		given a board (tile), width, and height: return a list of numbers to run find_narrowest_opening
			rows = []
			# build a mask for a single row (first bit is 2**0)
			base_mask = (1 << (self.width)) - 1
			for row in range(self.height):
				mask = base_mask << row*self.width
				current_row = (mask & tile) >> row*self.width
				rows.append(current_row)

			columns = []
			# build a mask for a single column
			base_mask = 0
			for row in rows:
				base_mask += 1 << row*self.width
			for col in range(self.width):
				mask = base_mask << col
				current_col = (mask & tile) >> col
				cols.append(current_col)
			
			return rows + columns

		"""
	

	# inefficient for readibility
	def get_rows(self, tile):
		"""
		given a tile, get the rows of it
		"""
		rows = []
		# build a mask for a single row (first bit is 2**0)
		base_mask = (1 << (self.width)) - 1
		for row in range(self.height):
				mask = base_mask << row*self.width
				current_row = (mask & tile) >> row*self.width
				rows.append(current_row)

		return rows


	# returns vertical!
	def get_cols(self, tile):
		"""
		given a tile, get the columns of it
		"""
		columns = []
		# build a mask for a single column
		base_mask = 0
		for row in range(self.height):
			base_mask += 1 << row*self.width
			for col in range(self.width):
				mask = base_mask << col
				current_col = (mask & tile) >> col
				columns.append(current_col)

		return columns

	# get the board run these two, run find_narrowest_opening for a num for rows and something for cols
	# return to minimum opening





"""
Precompute all rotations and shifting variables before hand (8 rotations + how right? + how down?)
shift right --> bitshift right
shift down --> calculate the leap number bit shift right x leapnumber

"""













"""
# get current level
# get the tile
# enumerate all tile orientations
	# does tile cross a word?
		# continue if so

	# can tile be placed here?
		# continiue if not

	# yield
"""


"""
Does tile cross a word?

for word in words:
	if tile & word != 0:
		if not ((word ^ tile) & word)
			continue # does cross so skip

"""

"""
Can tile be placed here?

if (tile ^ board) != (tile | board):
	continue # the spot is occupied so skip

"""



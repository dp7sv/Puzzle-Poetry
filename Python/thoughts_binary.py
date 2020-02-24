


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
	def __init__(self, width, height, pentominoes):


		self.width, self.height = width, height

		self.raw_tiles = pentominoes.copy()





	def is_valid(self):
		"""

		"""
		pass

	def branch(self):
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
		pass

	def tile_orientations(self, level):

		
		
		# get board size and determine how big the base of the mask is
		x_length, y_length = self.width, self.height

		# get the tile as a set of syllables
		syllables = self.raw_tiles[level]

		syllable_rotations = [syllables]

		for i in range(3):
			syllables = Problem.rotate_syllables(syllables)
			syllable_rotations.append(syllables)

		tile_rotations = [self.syllables_to_tile(s) for s in syllable_rotations]

		return tile_rotations

		# fix them to top left

		# tile_rotations = []

		# for i in range(4):
		# 	tile = self.syllables_to_tile(syllables)
		# 	stop = False
		# 	while not stop:
		# 		for row in range(self.height):
		# 			if (1 << row*self.width) & tile != 0:  	# if num[0 + row*x_length] == 1:
		# 				stop = True
		# 				break
		# 			else:
		# 				tile = tile << 1

		# 	tile_rotations.append(tile)
		# 	Problem.rotate_syllables(syllables)




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

		# Rotate matrix
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
	def syllables_to_matrix(syllables):
		m = [[0 for i in range(5)] for j in range(5)]
		for row, column in syllables:
			m[row][column] = 1
		return m


	# Syllables are row major
	def syllables_to_tile(self, syllables):
		tile = 0
		for row, column in syllables:
			tile += 1 << (row*self.width + column)
		return tile


	def tile_to_syllables(self, tile):
		syllables = []
		shift = -1
		while tile != 0:
			shift += 1
			if tile % 2 == 1:
				col = shift % self.width
				row = (shift - col) // self.width
				syllables.append((row, col))
			tile = tile >> 1

		return syllables




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



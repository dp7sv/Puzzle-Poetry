


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
	def __init__(self, *, width, height, pentominoes):


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


		# print(tile_rotations[2])
		# Problem.print_matrix(Problem.syllables_to_matrix(self.tile_to_syllables(tile_rotations[2]), 10, 6))

		# fix them to top left
		for i, rotation in enumerate(syllable_rotations):
			min_x = min(rotation, key=lambda x: x[1])[1]
			# print(i, min_x)
			min_y = min(rotation, key=lambda x: x[0])[0]
			# max_y = 0
			tile_rotations[i] = tile_rotations[i] >> (min_x + min_y*self.width)



		tiles = []
		for i, rotation in enumerate(tile_rotations):
			max_x = max(syllable_rotations[i], key=lambda x: x[1])[1]
			max_y = max(syllable_rotations[i], key=lambda x: x[0])[0]

			# putting it into matrix reverses the number. so right shifting the integer
			# shifts numbers to the left in the board
			print("#"*20)
			print(self.width - max_x, self.height - max_y)
			print("max_x:", max_x, "max_y:", max_y, "height:", self.height, "width:", self.width)
			Problem.print_matrix(Problem.syllables_to_matrix(self.tile_to_syllables(tile_rotations[i]), 10, 6))
			for right_shift in range(min(self.width - max_x, 2)):
				for bottom_shift in range(min(self.height - max_y, 2)):
					tile = rotation << (right_shift + self.width*bottom_shift)
					tiles.append(tile)

		return tiles

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


	# Syllables are row major
	def syllables_to_tile(self, syllables):
		print(syllables)
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



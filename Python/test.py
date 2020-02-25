from thoughts_binary import Problem



height = 6
width = 10
pentominoes = [
				[(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)],
			]

problem = Problem(height=height, width=width, pentominoes=pentominoes)

def print_syllables(syllables):
	print(syllables)
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print("\n\n")


# print_syllables(pentominoes[0])
# print("\n\n")
# print_syllables(Problem.rotate_syllables(pentominoes[0]))

for tile in problem.tile_orientations(0):
	# print_syllables(problem.tile_to_syllables(tile))
	# print(tile)
# print(len(problem.tile_orientations(0)))

# print("409993216 << 0")
# print_syllables(problem.tile_to_syllables(409993216))
# print("409993216 << 1")
# print_syllables(problem.tile_to_syllables(409993216 >> (0 + 6)))


# tile0 = problem.syllables_to_tile([(0, 0)])
# tile2 = problem.syllables_to_tile([(0, 2)])

# print(tile0, tile2, tile2 >> 2)

# for i in range(4):
# 	print("409993216 <<", i)
# 	print_syllables(problem.tile_to_syllables(409993216 << i))


# for i in range(60):
# 	print("1 <<", i)
# 	print_syllables(problem.tile_to_syllables(1 << i))


# print(problem.tile_to_syllables(1))

# height width was inverse so re test everything

from problem import Problem



height = 6
width = 10
# pentominoes = [
# 				[(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)],
# 			]

pentominoes = [

	[(0,0), (0,1), (0,2), (0,3), (0,4)],		# (I)
	[(0,0), (0,1), (0,2), (0,3), (1,0)],		# (L)
	[(0,0), (1,0), (2,0), (2,1), (2,2)],		# (V)
	[(0,0), (0,1), (1,0), (2,0), (2,1)],		# (U)
	[(0,1), (1,0), (1,1), (1,2), (2,1)],		# (X)
	[(0,2), (1,1), (1,2), (2,0), (2,1)],		# (W)
	[(0,1), (1,0), (1,1), (1,2), (2,0)],		# (F)
	[(0,0), (0,1), (1,1), (1,2), (1,3)],		# (N)
	[(0,1), (1,0), (1,1), (1,2), (1,3)],		# (Y)
	[(0,0), (0,1), (1,1), (2,1), (2,2)],		# (Z)
	[(0,0), (0,1), (1,0), (1,1), (2,1)],		# (P)
	[(0,2), (1,0), (1,1), (1,2), (2,2)],		# (T)

]


problem = Problem(height=height, width=width, pentominoes=pentominoes)

def print_syllables(syllables):
	print(syllables)
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print("\n\n")


# print_syllables(pentominoes[0])
# print("\n\n")
# print_syllables(Problem.rotate_syllables(pentominoes[0]))

# for tile in problem.tile_orientations(0):
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

tiles = [
	31, # (I)
	(15 << 10) + (1 << 20), # (L)
	(1 + (1 << 10) + (7 <<20)) << 30, # (V)
	(6 + (2 << 10) + (6 << 20)) << 20, # (U)
	((1 << 3) + (7 << 12) + (1 << 23)) << 30, # (X)
	((1 << 5) + (3 << 14) + (3 << 23)) << 30, # (W)
	(1 << 5) + (7 << 14) + (1 << 24), # (F)
	(3 << 5) + (7 << 16) << 20, # (N)
	(1 << 6) + (15 << 15) << 40, # (Y)
	(3 << 6) + (1 << 17) + (3 << 27), # (Z)
	(3 << 8) + (3 << 18) + (1 << 29), # (P)
	(1 << 9) + (7 << 17) + (1 << 29) << 30, # (T)
	

]
# for tile in tiles:
# 	print_syllables(problem.tile_to_syllables(tile))

# for i in range(12):
# 	print("level", i)
# 	found = False
# 	for tile in problem.tile_orientations(i):
		
# 		if tiles[i] == tile:
# 			found = True
# 			print("found for level", i, tile)

# 	if not found:
# 		print("could not found")
# 		print_syllables(problem.tile_to_syllables(tiles[i]))


for tile in problem.tile_orientations(4):
	# print_syllables(problem.tile_to_syllables(tile))
	pass
from problem import Problem



height = 6
width = 10
pentominoes = [

	[(0,0), (0,1), (0,2), (0,3), (0,4)],		# (I)
	[(0,0), (0,1), (0,2), (0,3), (0,1)],		# (L)
	[(0,0), (1,0), (2,0), (2,1), (2,2)],		# (V)
	[(0,0), (0,1), (1,0), (2,0), (2,1)],		# (U)
	[(0,1), (1,0), (1,1), (1,2), (2,1)],		# (X)
	[(0,2), (1,1), (1,2), (2,0), (2,1)],		# (W)
	[(0,1), (1,0), (1,1), (1,2), (2,0)],		# (F)
	[(0,1), (0,2), (1,1), (1,2), (1,3)],		# (N)
	[(0,1), (1,0), (1,1), (1,2), (1,3)],		# (Y)
	# [(0,0), (0,1), (1,1), (2,1), (2,2)],		# (Z)
	# [(0,0), (0,1), (1,0), (1,1), (2,1)],		# (P)
	# [(0,2), (1,0), (1,1), (1,2), (2,1)],		# (T)

]

words = [
	[(0, 1), (0, 2)], [(0, 3), (0, 4)], [(0, 8), (0, 9)],
	[(1, 2), (1, 3)], [(1, 5), (1, 6)],
	[(3, 6), (3, 7), (3, 8)],
	[(4, 1), (4, 2)],
	[(5, 5), (5, 6)]
    
]

easier_words = [
	[(0, 1), (0, 2), (0, 3), (0, 4)], [(0, 8), (0, 9)],
	[(1, 0), (1, 1), (1, 2), (1, 3)], [(1, 4), (1, 5), (1, 6)],
	[(3, 2), (3, 3), (3, 4)], [(3, 6), (3, 7), (3, 8)],
	[(4, 1), (4, 2)], [(4, 7), (4, 8), (4, 9)],
	[(5, 0), (5, 1), (5, 2)], [(5, 5), (5, 6), (5, 7), (5, 8)] # shorten the last word to reveal a bug

]


problem = Problem(height=height, width=width, pentominoes=pentominoes, words=easier_words)

def print_syllables(syllables):
	print(syllables)
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print("\n\n")

def print_tiles(tiles, p):
	for tile in tiles:
		print_syllables(p.tile_to_syllables(tile))


def print_solution(problem, index=0):
	state = problem.S[0]
	while state:
		print_syllables(problem.tile_to_syllables(state.board))
		state = state.parent


problem.solve()
print_solution(problem)

for key in problem.level_to_tiles:
	print(len(problem.level_to_tiles[key]))


# print(problem.words)
# print_tiles(problem.words, problem)

# for word in easier_words:
# 	print_syllables(word)
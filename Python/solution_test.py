from problem import Problem



height = 6
width = 10
pentominoes = [

	[(0,0), (0,1), (0,2), (0,3), (0,4)],		# (I)
	[(0,0), (0,1), (0,2), (0,3), (1,1)],		# (L)
	[(0,0), (1,0), (2,0), (2,1), (2,2)],		# (V)
	# [(0,0), (0,1), (1,0), (2,0), (2,1)],		# (U)
	# [(0,1), (1,0), (1,1), (1,2), (2,1)],		# (X)
	# [(0,2), (1,1), (1,2), (2,0), (2,1)],		# (W)
	# [(0,1), (1,0), (1,1), (1,2), (2,0)],		# (F)
	# [(0,1), (0,2), (1,1), (1,2), (1,3)],		# (N)
	# [(0,1), (1,0), (1,1), (1,2), (1,3)],		# (Y)
	# [(0,0), (0,1), (1,1), (2,1), (2,2)],		# (Z)
	# [(0,0), (0,1), (1,0), (1,1), (2,1)],		# (P)
	# [(0,2), (1,0), (1,1), (1,2), (2,1)],		# (T)

]

problem = Problem(height=height, width=width, pentominoes=pentominoes)

def print_syllables(syllables):
	print(syllables)
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print("\n\n")


problem.solve()

# print(problem.S[0])


def print_solution(problem, index=0):
	state = problem.S[0]
	while state:
		print_syllables(problem.tile_to_syllables(state.board))
		state = state.parent

print_solution(problem)


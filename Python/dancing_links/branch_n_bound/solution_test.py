from problem import Problem
import time

def print_syllables(syllables):
	print(syllables)
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print('\n\n')

def reduce_to_X(*, pentominoes, words, height, width):

	problem = Problem(height=height, width=width, pentominoes=pentominoes, words=words)

	start_time = time.time()
	problem.solve()
	end_time = time.time()

	# for i in range(len(problem.S)):
	# 	state = problem.S[i][0]
	# 	print(print_syllables(problem.tile_to_syllables(state.board)))

	print('Solutions Found: ', len(problem.S))
	print('Time taken:', end_time-start_time)
	print('States explored:', problem.states_explored)

	entries = []
	for level, orientations in enumerate(problem.S):
		for orientation in orientations:
			# build the row
			entry = [0 for i in range(len(pentominoes) + height*width)]

			# mark the pentominoe
			entry[level] = 1

			# mark the points the pentominoe covers
			syllables = problem.tile_to_syllables(orientation.board)
			for syllable in syllables:
				entry[len(pentominoes) + syllable[0]*width + syllable[1]] = 1
			
			entries.append(entry)

	# pentominoe names + locations (row major)
	names = ['I', 'X', 'Z', 'N', 'Y', 'L', 'T', 'V', 'W', 'F', 'U', 'P']

	for i in range(height):
		for j in range(width):
			names.append('r' + str(i) + 'c' + str(j))

	return entries, names

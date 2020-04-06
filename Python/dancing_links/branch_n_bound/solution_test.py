from problem import Problem
import time


height = 6
width = 10

pentominoes = [

	[(0,0), (0,1), (0,2), (0,3), (0,4)],		# (I) 
	[(0,1), (1,0), (1,1), (1,2), (2,1)],		# (X)
	[(0,0), (0,1), (1,1), (2,1), (2,2)],		# (Z)
	[(0,0), (0,1), (1,1), (1,2), (1,3)],		# (N)
	[(0,1), (1,0), (1,1), (1,2), (1,3)],		# (Y)
	[(0,0), (0,1), (0,2), (0,3), (1,0)],		# (L)
	[(0,2), (1,0), (1,1), (1,2), (2,2)],		# (T)
	[(0,0), (1,0), (2,0), (2,1), (2,2)],		# (V)
	[(0,2), (1,1), (1,2), (2,0), (2,1)],		# (W)
	[(0,1), (1,0), (1,1), (1,2), (2,0)],		# (F)
	[(0,0), (0,1), (1,0), (2,0), (2,1)],		# (U)
	[(0,0), (0,1), (1,0), (1,1), (2,1)],		# (P)

]  # pid = 43951    portal pid = 127154  slurm job id = 3899072


# pentominoes = [

# 	[(0,0), (0,1), (0,2), (0,3), (0,4)],		# (I) 
# 	[(0,0), (0,1), (0,2), (0,3), (1,0)],		# (L)
# 	[(0,0), (1,0), (2,0), (2,1), (2,2)],		# (V)
# 	[(0,0), (0,1), (1,0), (2,0), (2,1)],		# (U)
# 	[(0,1), (1,0), (1,1), (1,2), (2,1)],		# (X)
# 	[(0,2), (1,1), (1,2), (2,0), (2,1)],		# (W)
# 	[(0,1), (1,0), (1,1), (1,2), (2,0)],		# (F)
# 	[(0,0), (0,1), (1,1), (1,2), (1,3)],		# (N)
# 	[(0,1), (1,0), (1,1), (1,2), (1,3)],		# (Y)
# 	[(0,0), (0,1), (1,1), (2,1), (2,2)],		# (Z)
# 	[(0,0), (0,1), (1,0), (1,1), (2,1)],		# (P)
# 	[(0,2), (1,0), (1,1), (1,2), (2,2)],		# (T)

# ]  # list of final states = [32, 1162, 26263, 442839, 762954]
	# with easy words = [19, 277, 2192, 7869, 4298, 4074, 3165, 668, 241, 33, 1, 1]
# desmos inputs: (0, 32), (1, 1162), (2, 26263), (3, 442839), (4, 762954)
#				(0, 19), (1, 277), (2, 2192), (3, 7869), (4, 4298), (5, 4074), (6, 3165), (7, 668), (8, 241), (9, 33), (10, 1), (11, 1)
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

semi_easier_words = [
	[(0, 1), (0, 2), (0, 3), (0, 4)], [(0, 8), (0, 9)],
	[(1, 2), (1, 3)], [(1, 5), (1, 6)],
	[(3, 6), (3, 7), (3, 8)],
	[(4, 1), (4, 2)], [(4, 7), (4, 8), (4, 9)],
	[(5, 5), (5, 6)],
]

problem = Problem(height=height, width=width, pentominoes=pentominoes, words=easier_words)

def print_syllables(syllables):
	print(syllables)
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print('\n\n')

def print_tiles(tiles, p):
	for tile in tiles:
		print_syllables(p.tile_to_syllables(tile))


def print_solution(problem, index=0):
	state = problem.S[0]
	while state:
		print_syllables(problem.tile_to_syllables(state.board))
		state = state.parent

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

# print(names)
print(entries[0])
print(len(entries))

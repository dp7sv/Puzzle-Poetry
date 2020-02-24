from thoughts_binary import Problem



height = 6
width = 10
pentominoes = [
				[(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)],
			]

problem = Problem(height, width, pentominoes)

def print_syllables(syllables):
	Problem.print_matrix(Problem.syllables_to_matrix(syllables, 10, 6))
	print("\n\n")


# print_syllables(pentominoes[0])
# print("\n\n")
# print_syllables(Problem.rotate_syllables(pentominoes[0]))

for t_rotation in problem.tile_orientations(0):
	print_syllables(problem.tile_to_syllables(t_rotation))


print("409993216 << 0")
print_syllables(problem.tile_to_syllables(409993216 << 0))
print("409993216 << 1")
print_syllables(problem.tile_to_syllables(409993216 << 1))
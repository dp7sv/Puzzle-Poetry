import time
import sys
sys.path.append('branch_n_bound')

from ideation import main
from solution_test import reduce_to_X


# 6 x 10
sonnet3 = [  # Charlotte Smith, Sonnet III
    [(0, 1), (0, 2)], [(0, 3), (0, 4)], [(0, 8), (0, 9)],
   	[(1, 2), (1, 3)], [(1, 5), (1, 6)],
   	[(3, 6), (3, 7), (3, 8)],
   	[(4, 1), (4, 2)],
   	[(5, 5), (5, 6)]
]

# 14 x 10
# sonnet16 = [  # Shakespeare, Sonnet 16
#     [(0, 1), (0, 2)], [(0, 7), (0, 8)],
#     [(1, 2), (1, 3)], [(1, 5), (1, 6)], [(1, 7), (1, 8)],
#     [(2, 1), (2, 2), (2, 3)], [(2, 4), (2, 5)], [(2, 8), (2, 9)],
#     [(3, 3), (3, 4)], [(3, 7), (3, 8)],
#     [(4, 7), (4, 8)],
#     [(5, 1), (5, 2)], [(5, 3), (5, 4)], [(5, 5), (5, 6)],
#     # [(6, 1), (6, 2), (6, 3)], []
# ]

pentominoes = [

	[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],		# (I)
	[(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],		# (X)
	[(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],		# (Z)
	[(0, 0), (0, 1), (1, 1), (1, 2), (1, 3)],		# (N)
	[(0, 1), (1, 0), (1, 1), (1, 2), (1, 3)],		# (Y)
	[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0)],		# (L)
	[(0, 2), (1, 0), (1, 1), (1, 2), (2, 2)],		# (T)
	[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],		# (V)
	[(0, 2), (1, 1), (1, 2), (2, 0), (2, 1)],		# (W)
	[(0, 1), (1, 0), (1, 1), (1, 2), (2, 0)],		# (F)
	[(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],		# (U)
	[(0, 0), (0, 1), (1, 0), (1, 1), (2, 1)],		# (P)

    
]

# returns the height and width of the board
matrix, names = reduce_to_X(height=6, width=10, pentominoes=pentominoes, words=sonnet3)
print('Size of matrix', len(matrix))


# need to pass in the height and width of the matrix
start_time = time.time()
main(len(matrix), len(matrix[0]), matrix, names)
end_time = time.time()
print('Time Taken: ', end_time - start_time)


"""
Todo also add support for stop at one solution

"""
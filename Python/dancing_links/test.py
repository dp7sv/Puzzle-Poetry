import time
import sys
sys.path.append('branch_n_bound')

from ideation import main
from solution_test import reduce_to_X

# returns the height and width of the board
height, width, matrix, names = reduce_to_X()
print('Size of matrix', len(matrix))


# need to pass in the height and width of the matrix
start_time = time.time()
main(len(matrix), len(matrix[0]), matrix, names)
end_time = time.time()
print('Time Taken: ', end_time - start_time)
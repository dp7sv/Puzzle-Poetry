def printer(func):

	def wrapper(*args, **kwargs):

		print(func.__name__, "started")
		result = func(*args, **kwargs)
		print(func.__name__, "finished")

		return result

	return wrapper


def search(k):
	"""
	if nothing left in the graph (Exact cover)
		print result
	pick a column and cover it
	for each row
		select a row
		cover all the columns this row crosses
		search inside remaining graph
		record the result
		undo everything


	"""
	global h, O

	if h.r == h:
		print_solution()
		return

	# pick a column object
	c = choose_column()
	cover_column(c)

	# loop over all rows. Stop if r hits the header of the column (c)
	r = c.d
	while r != c:
		if len(O) <= k:
			O.append(r)
		else:
			O[k] = r

		# cover the columns this row already covers
		j = r.r
		while j != r:
			cover_column(j.c)
			j = j.r
		
		search(k+1)
		r = O[k]
		
		c = r.c
		# undo your work of colver_columns
		j = r.l
		while j != r:
			uncover_column(j.c)
			j = j.l

		r = r.d

	uncover_column(c)
	return


def print_solution():
	global O

	for Oi in reversed(O):
		print(Oi.n, Oi.c.n, end=" ")
		o = Oi.r
		while o != Oi:
			print(o.c.n, end=" ")
			o = o.r
		print()

# Loop overall column objects and pick the one with the minimum size
def choose_column():
	global h

	s = float("inf")

	j = h.r
	while j != h:
		if j.s < s:
			c = j
			s = j.s
		j = j.r

	return c


# cover the column and all rows crossing it
def cover_column(c):
	# remove c from the header list (a.k.a cover c)
	c.r.l = c.l
	c.l.r = c.r

	# cover all rows that cross c
	i = c.d
	while i != c:
		j = i.r
		while j != i:
			# cover the node vertically
			j.d.u = j.u
			j.u.d = j.d
			# decrement the count of the column
			j.c.s -= 1

			j = j.r

		i = i.d


def uncover_column(c):
	# do exactly the reverse of cover column to uncover it

	# first uncover this column's rows appearances on other columns
	i = c.u
	while i != c:
		j = i.l
		while j != i:
			j.c.s += 1
			j.d.u = j
			j.u.d = j

			j = j.l

		i = i.u

	# then add the column back to the header list
	c.r.l = c
	c.l.r = c


class Dancer():
	def __init__(self):
		self.l, self.r, self.u, self.d = None, None, None, None
		self.c = None


class ColumnObject():
	def __init__(self):
		self.l, self.r, self.u, self.d = None, None, None, None
		self.n, self.s = None, None


# height x width (taller == more rows, wider == more columns)
# @printer
def setup(height, width, matrix, names):
	global h, O


	# Make widht many columns
	columns = [None for column in range(width)]
	for j in range(width):
		columns[j] = ColumnObject()

	# Set its attrs (not setting c because I didn't know if it was useful)
	for j in range(width):
		columns[j].r = columns[(j+1)%width]
		columns[j].l = columns[(j-1)%width]

		columns[j].n = names[j]
		# Set u, d, and s later

	# Set h
	h = ColumnObject()
	h.r = columns[0]
	columns[0].l = h
	h.l = columns[-1]
	columns[-1].r = h



	dancers = [[None for column in range(width)] for row in range(height)]
	# Make height * width many dancers
	for i in range(height):
		for j in range(width):
			dancers[i][j] = Dancer()

	# Loop in dancers, set attributes for all
	for i in range(height):
		for j in range(width):
			dancers[i][j].r = dancers[i][(j+1)%width]
			dancers[i][j].l = dancers[i][(j-1)%width]

			dancers[i][j].u = dancers[(i-1)%height][j]
			dancers[i][j].d = dancers[(i+1)%height][j]

			dancers[i][j].c = columns[j]
			dancers[i][j].n = "r" + str(i)

	# connect column headers with dancers
	for j in range(width):
		dancers[0][j].u = columns[j]
		columns[j].d = dancers[0][j]

		dancers[-1][j].d = columns[j]
		columns[j].u = dancers[-1][j]

	# Uncover and delete all zeroes
	for i in range(height):
		for j in range(width):
			if matrix[i][j] == 0:
				# delete object
				dancer = dancers[i][j]
				dancer.u.d = dancer.d
				dancer.d.u = dancer.u
				dancer.l.r = dancer.r
				dancer.r.l = dancer.l

				# Trigger garbage collection early? For reasons?
				dancers[i][j] = None

	# Set the size of the columns
	for c in columns:
		i = c.d
		size = 0
		while i != c:
			size += 1
			i = i.d
		c.s = size

	return h, columns, dancers


"""

iterate the row


"""



	# do this for exact cover 
	# but it should be about our problem later
		# enumerate tile orientations
		# discard the ones that crosses the words


k = None
O = None
h = None

def main(height, width, matrix, names):
	global k, O, h

	h, columns, dancers = setup(height, width, matrix, names)

	# for column in columns:
	# 	print(column.n, end=" ")
	# print()

	# for row in dancers:
	# 	for dancer in row:
	# 		print(0 if dancer is None else dancer.c.n, end=' ')
	# 	print("")


	k = 0
	O = [None for i in range(k+1)]

	print("results:")

	search(k)

if __name__ == "__main__":
	height = 6
	width = 7

	names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	matrix = [  # A, B, C, D, E, F, G,
		[0, 0, 1, 0, 1, 1, 0],
		[1, 0, 0, 1, 0, 0, 1],
		[0, 1, 1, 0, 0, 1, 0],
		[1, 0, 0, 1, 0, 0, 0],
		[0, 1, 0, 0, 0, 0, 1],
		[0, 0, 0, 1, 1, 0, 1],
	]

	main(height, width, matrix, names)


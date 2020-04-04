

def search(k):
	if h.r == h:
		print_solution()
		return

	# pick a column object
	c = choose_column()
	cover_column(c)

	# loop over all rows. Stop if r hits the header of the column (c)
	r = c.d
	while r != c:
		O[k] = r

		# cover the columns this row already covers
		j = r.r
		while j != r:
			cover_column(j)
			j = j.r
		
		search(k+1)
		r = O[k]
		
		c = r.c
		# undo your work of colver_columns
		j = r.l
		while j != r:
			uncover_column(j)
			j = j.l

		r = r.d

	uncover_column(c)
	return


def print_solution():
	for Oi in reversed(O):
		print(Oi.c.n)
		o = Oi.r
		while o != Oi:
			print(o.c.n)
			o = o.r


def choose_column():
	s = float("inf")

	j = h.r
	while j != h:
		if j.s < s:
			c = j
			s = j.s
		j = j.r

	return c


def cover_column(c):
	# remove c from the header list (a.k.a cover c)
	c.r.l = c.l
	c.l.r = c.r

	# remove/cover all rows appearing in c on other columns
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
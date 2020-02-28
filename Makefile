M?="I didn't feel like adding a commit message"

all:
	git add -A
	git commit -m $(M)
	git push

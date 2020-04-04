# Poetry
Some of my scribbles I worked earlier. Trying to enumerate tile orientations.


# Things to do


- for a given state find the narrowest set of 0s. (bot horizontal and vertical)
- for each state, remember the length of next shortest pentominoe
- for each state if the next shortest pentominoe won't fit the narrowest entry, don't branch off of it

- explore if we can order the pentominoes / levels to make this more powerful

### Note
- Can do look for the smallest cloud width bread first search too


thread supervisor

run experiments on different ordering of pentominoes / levels

somehow not try to place it to places that are not going to work
	(e.g. there's something on the top left so ommit those from the search space)







## Other notes

- maybe fast check contigious spaces

- pre-compute small chunks of boards. I.e.
    - here's this 5x6 board
    - these tiles are not allowed
    - this is the pentomino
    - can I fit it?
- hash all these chunks and lookup while running the algorithm.
- this grows super fast: 2^30 many 5x6 boards






## Bit fiddling

Extras:
- How to scale
	- bitsets
	- python has built in large integers but it kills the purpose
	- build for 6x10 for now, all small boards then, divide work into different variables

















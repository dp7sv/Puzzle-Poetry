# Poetry
Some of my scribbles I worked earlier. Trying to enumerate tile orientations.


# Things to do

- after you're done, study yields and see if you can yield instead of returning the entire enumarations 












## Other notes

- maybe fast check contigious spaces
- super vague idea
	do some sort of version control instead storing copies of the board for each level. 
	(like the hashy link list git uses)

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
- How to check crossing words
	- 
- How to branch and bound


His stuff:
- How to rotate and shift the tiles around

















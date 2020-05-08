Tile display engine

For the program to view the tilings, the SDL2 graphics library is required

* on Linux I ran: `sudo apt-get install &ast;SDL2&ast;`

* I have seen others use this library on OSX but am not sure how to install it there

Two running options:

* With sanitizer: `make sanitizer`

* Without sanitizer: `make`

Once compiled, use `make tile` to show all tilings

* To set input file add src = <input poem>

* To make it enumerate all tilings instead of just finding the first add all=true

* `space` can be used in the program to advance through the tilings

tilings will also be placed in `./resources/research/out.txt` and written to the terminal

Once compiled, `make run` can be used to view the current contents of `./resources/research/out.txt`

Without compiling or needing the library, `make solve` can be run to generate the solutions in `./resources/research/out.txt`

* To set input file add src = <input poem>

* To make it enumerate all tilings instead of just finding the first add all=true

for example the command: `make && make tile src="./resources/research/poem0.txt" all=true` can be used to compile and run the program to find all 9356 tilings of a poem with only 1 syllable words and display them




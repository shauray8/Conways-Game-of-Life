# Conways-Game-of-Life
The Game of Life is a cellular-automaton, zero player game, developed by John Conway in 1970. The game is played on an infinite grid of square cells, and its evolution is only determined by it's initial state


## Slides for the game is in the assets folder !!

maybe i will make a webapp to interact with the game.

## what exactly is Convay's game of life ?

### Rules for the game !

<b>Birth</b> -- a cell is dead at time "t" will be alive at time "t+1" if 3 of its 8 neigbours are 
alive at the same time
</br>
<br>
<b>Death</b> -- a cell can die (ofcourse)<br>
* Overcrowding -- if a cell is alive at time "t" and 4 or more of its neigbours are also
alive at the same time "t" the cell will be declared dead at time "t+1"

* Exposure -- if a live cell at time "t" has 1 live neigbour or no live neighours,
it will be dead by time "t+1"
    
<b>Survival</b> -- a cell survives from time "t" to time "t+1" iff 2 or 3 of its neighbours are
alive at the same time "t".
</br><br>
this is how the grid look like with some life in it represented by "+". 
</br>
`. . . . . . . . . . . . . . . . . . . . . . . . . infinty`</br>
`. . + . . . . . . . . . . . + . . . .`</br>
`. + . + . . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`. . . . . . . . + . . . . . . . . . .`</br>
`. . . . . . . + . + . . . . . . . . .`</br>
`. . . . . . . . + . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . + + . . . .`</br>
`. . . . . . . . . . . . . + + . . . .`</br>
`. . . . + . . . . . . . . . . . . . .`</br>
`. . . . + . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`. . . . . . . . . . . . . . . . . . .`</br>
`.`</br>
`.`</br>
`.`</br>
`.infinity`</br><br> 
many configurations show unusuall effects like a glider or a boat.
## use cases
It is the study of how elaborate patterns and behaviors can emerge from very simple rules. It helps us understand, for example, how the petals on a rose or the stripes on a zebra can arise from a tissue of living cells growing together. 
</br><br>
It can even help us understand the diversity of life that has evolved on earth.
</br>

## Resources 
[Book (not sure about the quality of the content written) ](https://www.amazon.in/Game-Cellular-Automata-Andrew-Adamatzky/dp/1849962162)<br>
[Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)<br>
[Try stuff in your browser](https://playgameoflife.com/)<br>
[Youtube Video](https://www.youtube.com/watch?v=C2vgICfQawE)<br>
[Yet another youtube video](https://www.youtube.com/watch?v=R9Plq-D1gEk)<br>
[Maybe one more youtube video](https://www.youtube.com/watch?v=FWSR_7kZuYg)<br>

I think thats it to understand what this is all about !

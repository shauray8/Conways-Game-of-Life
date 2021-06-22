## Rules for the game !

## Birth -- a cell is dead at time "t" will be alive at time "t+1" if 3 of its 8 neigbours are 
## alive at the same time

##Death -- a cell can die (ofcourse)
    ## Overcrowding -- if a cell is alive at time "t" and 4 or more of its neigbours are also
    ## alive at the same time "t" the cell will be declared dead at time "t+1"

    ## Exposure -- if a live cell at time "t" has 1 live neigbour or no live neighours,
    ## it will be dead by time "t+1"

## Survival -- a cell survives from time "t" to time "t+1" iff 2 or 3 of its neighbours are
## alive at the same time "t".

## this is how the grid look like with some life in it represented by "+". 

#. . . . . . . . . . . . . . . . . . . . . .  . infinty
#. . + . . . . . . . . . . . + . . . .
#. + . + . . . . . . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#. . . . . . . . + . . . . . . . . . .
#. . . . . . . + . + . . . . . . . . .
#. . . . . . . . + . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#. . . . . . . . . . . . . + + . . . .
#. . . . . . . . . . . . . + + . . . .
#. . . . + . . . . . . . . . . . . . .
#. . . . + . . . . . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#. . . . . . . . . . . . . . . . . . .
#
#
#
# infinity


## many configurations show unusuall effects life a glider or a boat.

## use cases

# It is the study of how elaborate patterns and behaviors can emerge from very simple rules. It helps us understand, for example, how the petals on a rose or the stripes on a zebra can arise from a tissue of living cells growing together. 
# It can even help us understand the diversity of life that has evolved on earth.


import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

width  = 13
height = 13
blockSize=13

margin = 3
starty = 2

size = [500, 500]
grid = []
active = []
for row in range(size[0]//2):

    grid.append([])
    for column in range(size[1]//2):
        grid[row].append(0) 

def getNeighbors(cell):
    for x in range(int(grid[cell[0]])-1, int(grid[cell[0]])+2):
        for y in range(grid[cell[1]] - 1, grid[cell[1]] + 2):
            if (x, y) != (grid[cell[0]], grid[cell[1]]):
                yield grid[x][y]


def getNeighborCount():
    neighbor_counts = []
    for cell in active:
        for neighbor in getNeighbors(cell):
            neighbor_counts[neighbor] += 1
    return neighbor_counts

def advanceBoard():
    for cell, count in getNeighborCount():
        if count == 3 or (cell in grid and count == 2):
            active.add(cell)
            print(cell)


pygame.init()

screen = pygame.display.set_mode(size)
done = False

rect = pygame.Rect(2, 2, 200, 30)

clock = pygame.time.Clock()
START = WHITE
start = False
while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)

            grid[row][column] = 1
            active.append([row, column])
            print(active)

            if rect.collidepoint(pos):
                # prints current location of mouse

                print('button was pressed at {0}'.format(pos))

                start = True

    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, rect)

    if not start:
        for row in range(starty, size[0]//2):
           for column in range(0, size[1]//2):
                color = WHITE
                if grid[row][column] == 1:
                    color = RED
                pygame.draw.rect(screen, color, [
                    (margin+width)*column+margin,
                                  (margin+width)*row+margin,
                                  height,
                                  width], 1)

    if start:
        advanceBoard()
        for row in range(starty, size[0]//2):
           for column in range(0, size[1]//2):
                
                color = RED
                if grid[row][column] == 1:
                    color = RED
                pygame.draw.rect(screen, color, [
                    (margin+width)*column+margin,
                                  (margin+width)*row+margin,
                                  height,
                                  width], 1)




    clock.tick(90)

    pygame.display.flip()

pygame.quit()


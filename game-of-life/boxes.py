import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

width  = 13
height = 13
blockSize=13

margin = 3

size = [500, 500]
grid = []
for row in range(size[0]//2):

    grid.append([])
    for column in range(size[1]//2):
        grid[row].append(0) 

pygame.init()

screen = pygame.display.set_mode(size)
done = False


clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            pos = pygame.mouse.get_pos()

            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)

            grid[row][column] = 1

            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    for row in range(0, size[0]//2):
       for column in range(0, size[1]//2):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen, color, [
                (margin+width)*column+margin,
                              (margin+width)*row+margin,
                              height,
                              width])

    clock.tick(90)

    pygame.display.flip()

pygame.quit()

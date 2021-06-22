import pygame, sys
from pygame.locals import *

FPS = 30
BGCOLOR = (3, 115, 46)
BEFORECLICK = (22, 22, 106)
AFTERCLICK = (200, 200, 200)

boardWidth = 500
boardHeight = 500
rectX = 10
rectY = 10
rectWidth = 200
rectHeight = 200
myRectangle = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
RED = (255,0,0)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((boardWidth, boardHeight))
    pygame.display.set_caption("Klikni, kar klikni.")
    DISPLAYSURF.fill(BGCOLOR)

    mousex = 0
    mousey = 0
    button_color = BEFORECLICK
    mouseOver = False

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                if mouseOver:
                    # Change the current color if button was clicked.
                    button_color = AFTERCLICK

        mouseOver = determine_mouseOver(mousex, mousey)

        # Just draw the rect with the current button color.

        if mouseOver:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle, 3)

        pygame.display.update()
        FPSCLOCK.tick(30)

def determine_mouseOver(valx, valy):
    if myRectangle.collidepoint(valx, valy):
        return True
    else:
        return False


def drawGrid():
    blockSize = 13 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect, 1)
            
if __name__ == "__main__":
    main()

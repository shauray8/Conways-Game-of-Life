import pygame, sys
from pygame.locals import *

FPS = 30
BGCOLOR = (3, 115, 46)
BEFORECLICK = (22, 22, 106)
AFTERCLICK = (200, 200, 200)

boardWidth = 500
boardHeight = 500
rectX = 150
rectY = 150
rectWidth = 200
rectHeight = 200
myRectangle = pygame.Rect(rectX, rectY, rectWidth, rectHeight)

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((boardWidth, boardHeight))
    pygame.display.set_caption("Klikni, kar klikni.")

    mousex = 0
    mousey = 0
    button_color = BEFORECLICK
    mouseOver = False

    while True:
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

        DISPLAYSURF.fill(BGCOLOR)
        # Just draw the rect with the current button color.
        pygame.draw.rect(DISPLAYSURF, button_color, myRectangle)

        if mouseOver:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle, 3)

        pygame.display.update()
        FPSCLOCK.tick(30)
    #while True:
    #    mouseClicked = False
    #    DISPLAYSURF.fill(BGCOLOR)
    #    pygame.draw.rect(DISPLAYSURF, BEFORECLICK, myRectangle)

    #    for event in pygame.event.get():
    #        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
    #            pygame.quit()
    #            sys.exit()
    #        elif event.type == MOUSEMOTION:
    #            mousex, mousey = event.pos
    #        elif event.type == MOUSEBUTTONUP:
    #            mousex, mousey = event.pos
    #            mouseClicked = True

    #    mouseOver = determine_mouseOver(mousex, mousey)
    #    if mouseOver == True and mouseClicked == True:
    #        pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle)
    #    elif mouseOver == True and mouseClicked == False:
    #        pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle, 3)

    #    pygame.display.update()
    #    FPSCLOCK.tick(30)

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
            pygame.draw.rect(SCREEN, COLOR, rect, 1)
            
if __name__ == "__main__":
    main()

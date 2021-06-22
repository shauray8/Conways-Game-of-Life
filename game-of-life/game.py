import pygame
import sys
import random

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
RED = (255,0,0)


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        random_initial()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    blockSize = 13 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            

def random_initial():
    blockSize = 13 #Set the size of the grid block
    number = random.randint(1,20)
    for i in range(number):
        x = random.randint(0, WINDOW_HEIGHT)
        y = random.randint(0, WINDOW_HEIGHT)
        rect = pygame.draw.rect(x, y, blockSize, blockSize)
        print(x, y)
        pygame.draw.rect(SCREEN, RED, rect, 1)


def manual_initial():
    pass


def convay():
    pass
    

if __name__ == "__main__":
    main()

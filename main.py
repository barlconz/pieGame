import pygame
import time
import random

WIDTH, HEIGHT = 612, 408
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bullocks brett")

backGround = pygame.image.load("resources/background-image.jpg")

def draw():
    WIN.blit(backGround,(0,0))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()


if __name__ == "__main__":
    main()
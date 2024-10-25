import pygame
from constants import *

def main():
    print("Starting asteroids!")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black (0, 0, 0 is the RGB value for black)
        screen.fill((0, 0, 0))

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()


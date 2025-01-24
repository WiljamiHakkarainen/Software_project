import pygame
from functions import game_loop
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from startscreen import display_start_screen

try:
    pygame.init()
    pygame.mixer.init()
except pygame.error as e:
    print(f"Failed to initialize Pygame: {e}")
    exit(1)

pygame.display.set_caption("Tetris")
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == "__main__":
    if display_start_screen():
        game_loop()
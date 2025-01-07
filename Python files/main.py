import pygame
from functions import game_loop
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

pygame.display.set_caption("Tetris")
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

if __name__ == "__main__":
    game_loop()
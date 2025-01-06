import pygame
from functions import game_loop


pygame.init()

pygame.display.set_caption("Tetris")


if __name__ == "__main__":
    game_loop()
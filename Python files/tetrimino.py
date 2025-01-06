import pygame
import random
from constants import GAME_AREA_WIDTH, BLOCK_SIZE, SIDEBAR_WIDTH, TETROMINO_COLORS, TETRIMINOS

class Tetrimino:
    def __init__(self):
        self.shape = random.choice(TETRIMINOS)
        self.color = random.choice(TETROMINO_COLORS)
        self.x = GAME_AREA_WIDTH // BLOCK_SIZE // 2 - len(self.shape[0]) // 2
        self.y = 0

    # Draws the Tetrimino on the screen.
    def draw(self, screen, block_size, board):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x_pos = SIDEBAR_WIDTH + (self.x + col_idx) * block_size
                    y_pos = (self.y + row_idx) * block_size
                    pygame.draw.rect(screen, self.color, (x_pos, y_pos, block_size, block_size))

    # Draws the ghost block to show where the Tetrimino would land.
    def draw_ghost(self, screen, block_size, board):
        ghost_y = self.y
        # Moves the ghost piece down until it collides
        while not self.check_collision(board, x_offset=0, y_offset=ghost_y + 1 - self.y):  # Keep moving down
            ghost_y += 1

        # Draws the ghost block in a bright cyan color (light blue-green)
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x_pos = SIDEBAR_WIDTH + (self.x + col_idx) * block_size
                    y_pos = (ghost_y + row_idx) * block_size
                    pygame.draw.rect(screen, (169, 169, 169), (x_pos, y_pos, block_size, block_size))  # Light cyan color
    # Moving the Tetrimino
    def move_down(self, board):
        if not self.check_collision(board, y_offset=1):
            self.y += 1
        else:
            self.place_on_board(board)
            return False  # Stop the piece from moving further down
        return True  # Continue moving down

    def move_left(self, board):
        if not self.check_collision(board, x_offset=-1):
            self.x -= 1

    def move_right(self, board):
        if not self.check_collision(board, x_offset=1):
            self.x += 1

    def rotate(self, board):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        original_shape = self.shape
        self.shape = new_shape
        if self.check_collision(board):
            self.shape = original_shape  # Reverts if collision occurs

    def check_collision(self, board, x_offset=0, y_offset=0):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx + x_offset
                    new_y = self.y + row_idx + y_offset

                    # Checks if out of bounds or overlapping with an existing block
                    if (
                        new_x < 0 or
                        new_x >= len(board[0]) or
                        new_y >= len(board) or
                        (new_y >= 0 and board[new_y][new_x])
                    ):
                        return True
        return False

    # Places the Tetrimino on the game board.
    def place_on_board(self, board):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x = self.x + col_idx
                    new_y = self.y + row_idx
                    if 0 <= new_x < len(board[0]) and 0 <= new_y < len(board):
                        board[new_y][new_x] = self.color

    # Drops the Tetrimino to the lowest possible position when pressing space.
    def hard_drop(self, board):
        while not self.check_collision(board, y_offset=1):
            self.y += 1
        self.place_on_board(board)

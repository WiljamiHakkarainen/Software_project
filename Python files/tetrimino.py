import pygame
import random

# Tetrimino shapes
TETRIMINOS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]]   # L
]

# Colors for each Tetrimino
COLORS = [
    (0, 255, 255),  # Cyan for I
    (255, 255, 0),  # Yellow for O
    (128, 0, 128),  # Purple for T
    (0, 255, 0),    # Green for S
    (255, 0, 0),    # Red for Z
    (0, 0, 255),    # Blue for J
    (255, 165, 0)   # Orange for L
]

class Tetrimino:
    def __init__(self):
        # Random shape and color
        self.shape = random.choice(TETRIMINOS)
        self.color = random.choice(COLORS)
        
        # Starting position of the Tetrimino on the board
        self.x = 3  # Start near the center
        self.y = 0  # Start at the top of the board

    def draw(self, screen, block_size):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # Only draw blocks that are part of the shape
                    pygame.draw.rect(
                        screen,
                        self.color,
                        ((self.x + col_idx) * block_size, (self.y + row_idx) * block_size, block_size, block_size)
                    )

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        # Rotate the shape 90 degrees
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def check_collision(self, board):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    # Calculate the prospective position
                    new_x = self.x + col_idx
                    new_y = self.y + row_idx + 1
                    # Check if we're at the bottom or if there's a block below
                    if new_y >= len(board) or new_x < 0 or new_x >= len(board[0]) or board[new_y][new_x]:
                        return True
        return False

    def place_on_board(self, board):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    board[self.y + row_idx][self.x + col_idx] = self.color

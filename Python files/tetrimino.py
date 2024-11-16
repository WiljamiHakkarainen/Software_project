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

# Tetrimino colors
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
        self.x = 3  
        self.y = 0 

    # Method that draws the Tetrimino
    def draw(self, screen, block_size, board):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:  # Only draw blocks that are part of the shape
                    pygame.draw.rect(
                        screen,
                        self.color,
                        ((self.x + col_idx) * block_size, (self.y + row_idx) * block_size, block_size, block_size)
                    )

        # Draw the ghost block (shadow)
        ghost_y = self.get_ghost_position(board)
        self.draw_ghost(screen, block_size, ghost_y)

    # Method that simulates dropping the Tetrimino to the lowest position without collision
    def get_ghost_position(self, board):
        ghost_y = self.y
        while not self.check_collision_at_position(board, self.x, ghost_y + 1):
            ghost_y += 1
        return ghost_y

     # Method that checks for collision at a specific position (new_x, new_y)
    def check_collision_at_position(self, board, new_x, new_y):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    new_x_pos = new_x + col_idx
                    new_y_pos = new_y + row_idx
                    if new_y_pos >= len(board) or new_x_pos < 0 or new_x_pos >= len(board[0]) or board[new_y_pos][new_x_pos]:
                        return True
        return False
    
    # Method for drawing the "ghost" of the Tetrimino at the ghost position
    def draw_ghost(self, screen, block_size, ghost_y):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    # Semi-transparent color for the ghost
                    pygame.draw.rect(
                        screen,
                        (200, 200, 200),  # Light gray color for the ghost
                        ((self.x + col_idx) * block_size, (ghost_y + row_idx) * block_size, block_size, block_size)
                    )
                    pygame.draw.rect(
                        screen,
                        (255, 255, 255),  # Outline color for the ghost
                        ((self.x + col_idx) * block_size, (ghost_y + row_idx) * block_size, block_size, block_size), 1
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
    def hard_drop(self, board):
     while not self.check_collision(board):
        self.move_down()  # Fully drops the block down


    def check_collision(self, board):
        for row_idx, row in enumerate(self.shape):
           for col_idx, cell in enumerate(row):
            if cell:
                # Calculate the prospective position of the block
                new_x = self.x + col_idx
                new_y = self.y + row_idx + 1  # Just add 1 to y for downward movement

                # Check if the block is out of bounds or colliding with existing blocks
                if new_y >= len(board) or new_x < 0 or new_x >= len(board[0]) or board[new_y][new_x]:
                    return True
        return False


    def place_on_board(self, board):
        for row_idx, row in enumerate(self.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    board[self.y + row_idx][self.x + col_idx] = self.color

import pygame

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Testing out a gradient Background (color fades from for example grey to black)
def draw_gradient_background(screen, color1, color2):
    screen_height = screen.get_height()
    for y in range(screen_height):
        ratio = y / screen_height
        color = (
            int(color1[0] * (1 - ratio) + color2[0] * ratio),
            int(color1[1] * (1 - ratio) + color2[1] * ratio),
            int(color1[2] * (1 - ratio) + color2[2] * ratio),
        )
        pygame.draw.line(screen, color, (0, y), (screen.get_width(), y))

# Draws the game board
def draw_board(screen, board, block_size):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]:
                pygame.draw.rect(screen, board[row][col], (col * block_size, row * block_size, block_size, block_size))
            pygame.draw.rect(screen, WHITE, (col * block_size, row * block_size, block_size, block_size), 1)
    pygame.display.update()

# Clears the full rows
def clear_rows(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    while len(new_board) < len(board):
        new_board.insert(0, [0 for _ in range(len(board[0]))])
    return new_board

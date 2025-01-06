import pygame

BLOCK_SIZE = 30 

GAME_AREA_WIDTH = 10 * BLOCK_SIZE
GAME_AREA_HEIGHT = 20 * BLOCK_SIZE
SIDEBAR_WIDTH = 200

# Total screen dimensions
SCREEN_WIDTH = GAME_AREA_WIDTH + SIDEBAR_WIDTH
SCREEN_HEIGHT = GAME_AREA_HEIGHT
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
TETROMINO_COLORS = [
    (0, 255, 255),  # Cyan for I
    (255, 255, 0),  # Yellow for O
    (128, 0, 128),  # Purple for T
    (0, 255, 0),    # Green for S
    (255, 0, 0),    # Red for Z
    (0, 0, 255),    # Blue for J
    (255, 165, 0)   # Orange for L
]
# Colors
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (50, 50, 50)  # Dark grey background
TEXT_COLOR = (200, 200, 200)       # Soft red for the "Game Over" text
BUTTON_COLOR = (100, 100, 255)   # Muted blue for buttons
BUTTON_HOVER_COLOR = (150, 150, 255)  # Lighter blue for hover
BUTTON_TEXT_COLOR = (255, 255, 255)  # White text for buttons
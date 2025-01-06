import pygame
from constants import WHITE, SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, BLOCK_SIZE, GAME_AREA_WIDTH, SIDEBAR_WIDTH, GAME_AREA_HEIGHT
from tetrimino import Tetrimino
from gameover import display_game_over

# Gradient Background (color fades from for example grey to black)
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
            x_pos = SIDEBAR_WIDTH + col * block_size
            y_pos = row * block_size
            if board[row][col]:
                pygame.draw.rect(screen, board[row][col], (x_pos, y_pos, block_size, block_size))
            pygame.draw.rect(screen, WHITE, (x_pos, y_pos, block_size, block_size), 1)


# Clears the full rows
def clear_rows(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    while len(new_board) < len(board):
        new_board.insert(0, [0 for _ in range(len(board[0]))])
    return new_board

# Empty game board (10 columns, 20 rows)
board = [
    [0 for _ in range(GAME_AREA_WIDTH // BLOCK_SIZE)]
    for _ in range(GAME_AREA_HEIGHT // BLOCK_SIZE)
]

def draw_sidebar(screen):
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, SIDEBAR_WIDTH, SCREEN_HEIGHT))
    # Adds any text, stats, or graphics
    font = pygame.font.Font(None, 24)
    text = font.render("Sidebar", True, WHITE)
    screen.blit(text, (10, 10))

# Main game loop
def game_loop():
    global board
    clock = pygame.time.Clock()
    tetrimino = Tetrimino()

    while True:
        # Draws sidebar and game area
        SCREEN.fill((0, 0, 0))
        draw_sidebar(SCREEN)
        draw_board(SCREEN, board, BLOCK_SIZE)

        tetrimino.draw_ghost(SCREEN, BLOCK_SIZE, board)

        # Handles game logic and draw Tetriminos
        if not tetrimino.move_down(board):
            # Places the tetrimino on the board and clear rows if full
            board = clear_rows(board)
            tetrimino = Tetrimino()

            if tetrimino.check_collision(board) and tetrimino.y == 0:
                play_again = display_game_over(SCREEN)
                if play_again:
                    board = [
                        [0 for _ in range(GAME_AREA_WIDTH // BLOCK_SIZE)]
                        for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)
                    ]
                    game_loop()
                else:
                    pygame.quit()
                    exit()

        # Draws the current Tetrimino
        tetrimino.draw(SCREEN, BLOCK_SIZE, board)

        pygame.display.update()
        clock.tick(5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    tetrimino.move_left(board)
                    if tetrimino.check_collision(board):
                        tetrimino.move_right(board)

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    tetrimino.move_right(board)
                    if tetrimino.check_collision(board):
                        tetrimino.move_left(board)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    tetrimino.move_down(board)

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    tetrimino.rotate(board)
                    if tetrimino.check_collision(board):
                        tetrimino.shape = [list(row) for row in zip(*tetrimino.shape[::-1])]

                elif event.key == pygame.K_SPACE:
                    tetrimino.hard_drop(board)
                    board = clear_rows(board)
                    tetrimino = Tetrimino()






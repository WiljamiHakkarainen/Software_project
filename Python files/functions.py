import pygame
from constants import WHITE, BLACK, GRAY, SCREEN, SCREEN_HEIGHT, BLOCK_SIZE, GAME_AREA_WIDTH, SIDEBAR_WIDTH, GAME_AREA_HEIGHT, INITIAL_GAME_SPEED, SPEED_DECREASE_PER_LEVEL, MIN_GAME_SPEED, LINES_PER_LEVEL
from tetrimino import Tetrimino
from gameover import display_game_over

# Initialize game variables
lines_cleared = 0  # Number of lines cleared
level = 1  # Current level
lines = 0  # Total lines cleared by the player
paused = False  # Pause state
game_speed = INITIAL_GAME_SPEED  # Starting game speed

# Update the game speed based on the current level
def update_game_speed():
    global game_speed
    game_speed = max(MIN_GAME_SPEED, INITIAL_GAME_SPEED - (level - 1) * SPEED_DECREASE_PER_LEVEL)

# Gradient Background (color fades from for example gray to black)
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
    new_board = [row for row in board if any(cell == 0 for cell in row)]  # Keep non-full rows
    lines_cleared = len(board) - len(new_board)  # Number of lines cleared
    while len(new_board) < len(board):  # Add empty rows at the top to replace cleared ones
        new_board.insert(0, [0 for _ in range(len(board[0]))])
    return new_board, lines_cleared

# Draw Sidebar
def draw_sidebar(screen, font, score, level, lines, next_tetrimino, paused):
    pygame.draw.rect(screen, GRAY, (0, 0, SIDEBAR_WIDTH, SCREEN_HEIGHT))

    text = font.render("Next", True, BLACK)
    screen.blit(text, (SIDEBAR_WIDTH // 2 - text.get_width() // 2, 20))
    pygame.draw.rect(screen, BLACK, (10, 50, SIDEBAR_WIDTH - 20, 100), 2)

    if next_tetrimino:
        tetrimino_width = len(next_tetrimino.shape[0])  # Number of columns
        tetrimino_height = len(next_tetrimino.shape)  # Number of rows

        max_width = min(tetrimino_width, (SIDEBAR_WIDTH - 20) // BLOCK_SIZE)
        max_height = min(tetrimino_height, 100 // BLOCK_SIZE)

        x_offset = (SIDEBAR_WIDTH - 20 - max_width * BLOCK_SIZE) // 2 + 10
        y_offset = (100 - max_height * BLOCK_SIZE) // 2 + 50

        for row_idx, row in enumerate(next_tetrimino.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    x_pos = x_offset + col_idx * BLOCK_SIZE
                    y_pos = y_offset + row_idx * BLOCK_SIZE
                    pygame.draw.rect(screen, next_tetrimino.color, (x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, BLACK, (x_pos, y_pos, BLOCK_SIZE, BLOCK_SIZE), 1)

    labels = ["Score", "Level", "Lines"]
    values = [score, level, lines]
    for i, (label, value) in enumerate(zip(labels, values)):
        y_offset = 170 + i * 50
        text_label = font.render(label, True, BLACK)
        text_value = font.render(str(value), True, BLACK)
        pygame.draw.rect(screen, BLACK, (10, y_offset, SIDEBAR_WIDTH - 20, 40), 2)
        screen.blit(text_label, (15, y_offset + 5))
        screen.blit(text_value, (SIDEBAR_WIDTH - 30 - text_value.get_width(), y_offset + 5))

    pygame.draw.rect(screen, BLACK, (10, SCREEN_HEIGHT - 120, SIDEBAR_WIDTH - 20, 40), 2)
    mute_icon = pygame.image.load("Images/mute_icon.png")
    mute_icon = pygame.transform.scale(mute_icon, (30, 30))
    screen.blit(mute_icon, (SIDEBAR_WIDTH // 2 - mute_icon.get_width() // 2, SCREEN_HEIGHT - 115))

    pygame.draw.rect(screen, BLACK, (10, SCREEN_HEIGHT - 60, SIDEBAR_WIDTH - 20, 40), 2)
    pause_text = font.render("Unpause" if paused else "Pause", True, BLACK)
    screen.blit(pause_text, (SIDEBAR_WIDTH // 2 - pause_text.get_width() // 2, SCREEN_HEIGHT - 55))

# Main game loop
def game_loop():
    global board, paused, lines, level, game_speed
    lines = 0
    paused = False
    clock = pygame.time.Clock()
    prev_level = level  # Track the previous level

    drop_timer = 0  # Timer for automatic piece drops
    board = [
        [0 for _ in range(GAME_AREA_WIDTH // BLOCK_SIZE)]
        for _ in range(GAME_AREA_HEIGHT // BLOCK_SIZE)
    ]

    tetrimino = Tetrimino()
    next_tetrimino = Tetrimino()

    while True:
        SCREEN.fill((0, 0, 0))  # Clear screen before drawing again
        draw_sidebar(SCREEN, pygame.font.SysFont("Arial", 20), score=0, level=level, lines=lines, next_tetrimino=next_tetrimino, paused=paused)
        draw_board(SCREEN, board, BLOCK_SIZE)
        tetrimino.draw_ghost(SCREEN, BLOCK_SIZE, board)
        tetrimino.draw(SCREEN, BLOCK_SIZE, board)

        if not paused:
            drop_timer += clock.get_time()
            if drop_timer >= game_speed:  # Drop piece based on game_speed
                drop_timer = 0
                if not tetrimino.move_down(board):
                    board, lines_cleared = clear_rows(board)
                    if lines_cleared > 0:
                        lines += lines_cleared
                        level = lines // LINES_PER_LEVEL + 1
                        if level != prev_level:
                            prev_level = level
                            update_game_speed()  # Update speed on level change
                            print(f"Level: {level}, Game Speed: {game_speed}")

                    tetrimino = next_tetrimino
                    next_tetrimino = Tetrimino()

                    if tetrimino.check_collision(board) and tetrimino.y == 0:
                        play_again = display_game_over(SCREEN)
                        if play_again:
                            board = [
                                [0 for _ in range(GAME_AREA_WIDTH // BLOCK_SIZE)]
                                for _ in range(GAME_AREA_HEIGHT // BLOCK_SIZE)
                            ]
                            tetrimino = Tetrimino()
                            next_tetrimino = Tetrimino()
                            lines = 0
                            level = 1
                            game_speed = INITIAL_GAME_SPEED
                            prev_level = level
                        else:
                            pygame.quit()
                            return

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

                elif event.key == pygame.K_SPACE and not paused:
                    tetrimino.hard_drop(board)
                    board, lines_cleared = clear_rows(board)
                    lines += lines_cleared
                    tetrimino = next_tetrimino
                    next_tetrimino = Tetrimino()

                elif event.key == pygame.K_p:
                    paused = not paused

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 10 <= mouse_x <= SIDEBAR_WIDTH - 10 and SCREEN_HEIGHT - 60 <= mouse_y <= SCREEN_HEIGHT - 20:
                    paused = not paused  

        pygame.display.update()
        clock.tick(60)














import pygame
from tetrimino import Tetrimino
from functions import draw_gradient_background, draw_board, clear_rows
from gameover import display_game_over

pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Empty game board (10 columns, 20 rows)
board = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]

# Main game loop
def game_loop():
    global board
    clock = pygame.time.Clock()
    tetrimino = Tetrimino()

    while True:
        draw_gradient_background(SCREEN, (75, 75, 75), (0, 0, 0))

        # Check for collision (only once before trying to move or rotate)
        if tetrimino.check_collision(board):
            tetrimino.place_on_board(board)
            board = clear_rows(board)
            tetrimino = Tetrimino()

            # Game over condition: collision at the top
            if tetrimino.check_collision(board) and tetrimino.y == 0:
                play_again = display_game_over(SCREEN)
                if play_again:
                    # Resetting the game
                    board = [[0 for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
                    game_loop()
                else:
                    pygame.quit()
                    exit()

        # Draw the game board and the current Tetrimino
        draw_board(SCREEN, board, BLOCK_SIZE)
        tetrimino.draw(SCREEN, BLOCK_SIZE, board)
        tetrimino.move_down()  # Automatically move down each frame if no collision

        pygame.display.update()  # Update the display
        clock.tick(5)  # Control game speed (currently 5 fps)

        # Event handling for quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Handle key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    tetrimino.move_left()
                    if tetrimino.check_collision(board):
                        tetrimino.move_right()  # Undo if collides

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    tetrimino.move_right()
                    if tetrimino.check_collision(board):
                        tetrimino.move_left()

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    tetrimino.move_down()
                    if tetrimino.check_collision(board):
                        tetrimino.y -= 1  # Undo down movement (move up)

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    tetrimino.rotate()
                    if tetrimino.check_collision(board):
                        tetrimino.shape = [list(row) for row in zip(*tetrimino.shape[::-1])]  # Undo rotation 

                elif event.key == pygame.K_SPACE:
                    tetrimino.hard_drop(board)  # Drop the tetrimino to the bottom
                    tetrimino.place_on_board(board)
                    board = clear_rows(board)
                    tetrimino = Tetrimino()

if __name__ == "__main__":
    game_loop()

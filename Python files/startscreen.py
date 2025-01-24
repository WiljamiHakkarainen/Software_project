import pygame
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR, BLACK, BACKGROUND_COLOR, TEXT_COLOR, lARGE_FONT, SMALL_FONT

def display_start_screen():
    pygame.init()

    start_game_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 200, 50)
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 20, 200, 50)

    while True:
        SCREEN.fill(BACKGROUND_COLOR)

        # Draw title
        title_text = lARGE_FONT.render("Tetris", True, TEXT_COLOR)
        SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))

        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button, text in [(start_game_button, "Start Game"), (quit_button, "Quit")]:
            # Change button color on hover
            button_color = BUTTON_HOVER_COLOR if button.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(SCREEN, button_color, button, border_radius=10)
            pygame.draw.rect(SCREEN, BLACK, button, 2, border_radius=10)
            button_text = SMALL_FONT.render(text, True, BUTTON_TEXT_COLOR)
            SCREEN.blit(button_text, (button.x + (button.width - button_text.get_width()) // 2, button.y + (button.height - button_text.get_height()) // 2))

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_button.collidepoint(mouse_pos):
                    return True  # Start the game
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
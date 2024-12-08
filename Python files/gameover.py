import pygame
from constants import BACKGROUND_COLOR, TEXT_COLOR, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR

def display_game_over(screen):

    # Fonts
    pygame.font.init()
    large_font = pygame.font.Font(None, 50)  # Font for "Game Over"
    button_font = pygame.font.Font(None, 36)  # Font for buttons

    # Screen dimensions
    screen_width, screen_height = screen.get_size()

    # Buttons
    button_width = 200
    button_height = 50
    button_padding = 20

    play_again_button = pygame.Rect(
        (screen_width - button_width) // 2,
        screen_height // 2,
        button_width,
        button_height,
    )
    quit_button = pygame.Rect(
        (screen_width - button_width) // 2,
        screen_height // 2 + button_height + button_padding,
        button_width,
        button_height,
    )

    # Display the Game Over screen
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Render "Game Over" text
        game_over_text = large_font.render("GAME OVER", True, TEXT_COLOR)
        screen.blit(
            game_over_text,
            ((screen_width - game_over_text.get_width()) // 2, screen_height // 4),
        )

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Draw buttons
        for button, text in [(play_again_button, "Play Again"), (quit_button, "Quit")]:
            # Change button color on hover
            button_color = BUTTON_HOVER_COLOR if button.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(screen, button_color, button, border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), button, 2, border_radius=10)  # Add button border

            # Render button text
            button_text = button_font.render(text, True, BUTTON_TEXT_COLOR)
            screen.blit(
                button_text,
                (
                    button.x + (button_width - button_text.get_width()) // 2,
                    button.y + (button_height - button_text.get_height()) // 2,
                ),
            )

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(mouse_pos):
                    return True  # Restart the game
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()

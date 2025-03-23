import pygame

# Constants for window's dimensions
WINDOW_WIDTH = 800

def final_results(WIN, best_genome, generation):
    """
    This will display the final results on the end screen 
    with an option for the user to close the game.
    """

    # Initializes pygame font and other required styles
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 28)
    background_color = (30, 30, 30)             # Dark background
    text_color = (255, 255, 255)                # White text
    button_color = (200, 0, 0)                  # Red button
    button_hover_color = (255, 50, 50)          # Bright red button on hover

    # Clears the screen before we render the text and button
    WIN.fill(background_color)

    # Renders the required text
    final_title = font.render("NEAT AI Simulation Complete!", True, text_color)
    generation_final_text = font.render(f"Final Generation Number: {generation}", True, text_color)
    genome_id_text = font.render(f"Best Generated Genome ID: {best_genome.key}", True, text_color)
    genome_fitness_text = font.render(f"Fitness Of Best Genome: {best_genome.fitness:.2f} / 2000", True, text_color)

    # Positions the required text onto the screen
    WIN.blit(final_title, (WINDOW_WIDTH // 2 - final_title.get_width() // 2, 100))
    WIN.blit(generation_final_text, (WINDOW_WIDTH // 2 - generation_final_text.get_width() // 2, 200))
    WIN.blit(genome_id_text, (WINDOW_WIDTH // 2 - genome_id_text.get_width() // 2, 300))
    WIN.blit(genome_fitness_text, (WINDOW_WIDTH // 2 - genome_fitness_text.get_width() // 2, 340))

    # Creates a button to allow the user closing the game
    button_rect = pygame.Rect(WINDOW_WIDTH // 2 - 75, 400, 150, 50)  # The button's dimensions
    running = True

    while running:
        # Handles the events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Detects the button click to close the game window 
                if button_rect.collidepoint(event.pos):
                    running = False  # Closes the game

        # Checks for the hover effect and applies it
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(WIN, button_hover_color, button_rect)
        else:
            pygame.draw.rect(WIN, button_color, button_rect)

        # Renders the close button's text
        button_text = button_font.render("Close Game", True, text_color)
        WIN.blit(button_text, (button_rect.x + button_rect.width // 2 - button_text.get_width() // 2,
                               button_rect.y + button_rect.height // 2 - button_text.get_height() // 2))

        # Updates the display with the design
        pygame.display.update()

import pygame
import os

# Background images (REFERENCES IN README)
BG_IMG1 = pygame.image.load(os.path.join("Assets", "parallax-forest-back-trees.png"))
BG_IMG2 = pygame.image.load(os.path.join("Assets", "parallax-forest-middle-trees.png"))

class Draw:
    
    def draw_window(screen, cappies, bg1_x1, bg1_x2, bg2_x1, bg2_x2, obstacles, elapsed_time): 
        # Draws the backgrounds to the screen
        screen.blit(BG_IMG1, (bg1_x1, 0))
        screen.blit(BG_IMG1, (bg1_x2, 0))
        screen.blit(BG_IMG2, (bg2_x1, 0))
        screen.blit(BG_IMG2, (bg2_x2, 0))

        # Draws obstacles onto the screen 
        for obstacle in obstacles:
            obstacle.draw(screen)

        # Draw all the current active sprites used by the NeatAI
        for cappy in cappies:
            cappy.draw(screen)

        # Displays a timer onto the screen
        total_seconds = int(elapsed_time)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

        font = pygame.font.SysFont(None, 55)
        text = font.render(f"Time: {formatted_time}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.update()


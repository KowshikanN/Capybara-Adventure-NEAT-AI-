import pygame
import os

# Load the image for the Cappybara sprite (REFERENCES IN README)
CAPPY_IMG = pygame.image.load(os.path.join("Assets", "CappyWalk1.png"))

class Cappy:
    IMG = CAPPY_IMG 
    GRAVITY = 0.8           # Gravity constant for jump logic / physics 
    JUMP_STRENGTH = -24     # Adjustable jump strength for cappybara sprite 

    def __init__(self, x, y):
        self.img = self.IMG
        self.player_pos = pygame.Vector2(x, y)
        self.cappy_velocity_y = 0
        self.is_jumping = False      

    def move(self, dt, window_width):
        # Handles the sprite's movement and jumping
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and not self.is_jumping: 
            self.cappy_velocity_y = self.JUMP_STRENGTH
            self.is_jumping = True
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * dt
            if self.player_pos.x < 0:
                self.player_pos.x = 0
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * dt
            if self.player_pos.x > (window_width - self.img.get_width()):
                self.player_pos.x = window_width - self.img.get_width()

        # Updates the vertical position of the sprite and will apply gravity to jumps
        self.cappy_velocity_y += self.GRAVITY
        self.player_pos.y += self.cappy_velocity_y

        # Checks for collision with the ground so the sprite doesnt go off screen
        if self.player_pos.y >= 260:
            self.player_pos.y = 260
            self.cappy_velocity_y = 0
            self.is_jumping = False

    def draw(self, screen):
        # Draws the sprite onto the screen for visulization
        screen.blit(self.img, (self.player_pos.x, self.player_pos.y))       

    def get_hitbox(self):
        """
        Creates a hitbox for Cappy.
        Implemented the hitbox smaller than the full ,
        size of the image for accurate collisions.
        """
        padding = 140                               # Constant value for desired padding
        return pygame.Rect(
            self.player_pos.x + padding,            # Added some padding to the left side
            self.player_pos.y + padding,            # Add some padding to the top side
            self.img.get_width() - padding * 2,     # Shrunk the width
            self.img.get_height() - padding * 2     # Shrink the height
        )


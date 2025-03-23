import pygame
import os
import random
import time

# Loads the image for the tree sprite (REFERENCES IN README)
TREE_IMGS = [pygame.image.load(os.path.join("Assets", "STUMP.png"))]

class Tree:
    VEL = 4             # A fixed velocity value for the speed of the trees (can be changed for more difficulty)

    def __init__(self, x):
        self.img = random.choice(TREE_IMGS)
        self.x = x
        self.y = 320

    def move(self):
        # Updates the tree position based on velocity 
        self.x -= self.VEL

    def draw(self, screen):
        # Draws the tree  sprite onto the screen
        screen.blit(self.img, (self.x, self.y))

    def off_screen(self): 
        # Checks if the current object's x-coordinate is less than the negative width of its image,
        # if it is then they can be considered to be off the screen
        return self.x < -self.img.get_width()
    
    def collision(self, obj):
        """
        Checks for collision between the tree sprite and the cappybara sprite using bounding boxes.
        """
        tree_rect = self.get_hitbox()  # The tree's hitbox
        cappy_rect = obj.get_hitbox()  # The cappybara's hitbox

        # A bounding box collision check
        return tree_rect.colliderect(cappy_rect)

    def get_hitbox(self):
        """
        Creates a hitbox for tree sprite
        """
        return pygame.Rect(
            self.x,
            self.y,
            self.img.get_width(),
            self.img.get_height()
        )

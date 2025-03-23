import pygame
import os
from NeatAI import NeatAI

# Initializes Pygame and helps to set up the game window
pygame.init()

# Constants for window dimensions (Do not change!)
WIN_WIDTH = 800
WIN_HEIGHT = 471

# Creates the game window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Cappybara Adventure with NEAT AI")

def main():
    # Loads the provided NEAT AI configuration file
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')

    # Runs the NEAT AI training model, and passes the game window
    neat_ai = NeatAI()
    neat_ai.run(config_path, WIN)

if __name__ == "__main__":
    main()

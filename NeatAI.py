import pygame
import neat
import os
import random
import time
from Cappy import Cappy
from Obstacles import Tree
from Draw import Draw
from Results import final_results

# Constants for window dimensions (Do not change!)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 471

# Background images (REFERENCES IN README)
BG_IMG1 = pygame.image.load(os.path.join("Assets", "parallax-forest-back-trees.png"))
BG_IMG2 = pygame.image.load(os.path.join("Assets", "parallax-forest-middle-trees.png"))


class NeatAI:
    def __init__(self):
        self.gen = 0        # Tracks the current generation of the AI's cappybaras

    def genome_evaluate(self, genomes, config, WIN):
        """
        This will simulate a generation of genomes within the game environment,
        it will assign fitness scores based on the AI's performance.
        """
        self.gen += 1

        # Initializes the game clock within the game window
        clock = pygame.time.Clock()
        dt = 0
        start_time = time.time()

        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        # The scrolling positions of the backgrounds
        bg1_x1, bg1_x2 = 0, BG_IMG1.get_width()
        bg2_x1, bg2_x2 = 0, BG_IMG2.get_width()
        scroll_speed1 = 1
        scroll_speed2 = 2

        # Creates a set of Neural networks, Cappybara objects, and the genomes
        nets = []
        cappy_objects = []
        ge = []

        for genome_id, genome in genomes:
            genome.fitness = 0   # Initializes the fitness starting at 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            cappy_objects.append(Cappy(0, 260))  # Starting position of the cappybaras
            ge.append(genome)

        # Initializes the obstacles (trees) used within the game
        obstacles = []
        tree_cooldown = 0
        tree_distance = 600  # The minimum distance between each obstacles

        running = True

        while running and len(cappy_objects) > 0:
            # Updates the time and the scrolling background
            dt = clock.tick(60) / 1000.0  # Delta time
            bg1_x1 -= scroll_speed1
            bg1_x2 -= scroll_speed1
            bg2_x1 -= scroll_speed2
            bg2_x2 -= scroll_speed2

            # Loops the background seamlessly to make it seem like the cappybara is moving
            if bg1_x1 <= -BG_IMG1.get_width():
                bg1_x1 = BG_IMG1.get_width()
            if bg1_x2 <= -BG_IMG1.get_width():
                bg1_x2 = BG_IMG1.get_width()
            if bg2_x1 <= -BG_IMG2.get_width():
                bg2_x1 = BG_IMG2.get_width()
            if bg2_x2 <= -BG_IMG2.get_width():
                bg2_x2 = BG_IMG2.get_width()

            # Handles the Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            # Obstacle spawning logic
            tree_cooldown -= dt
            if tree_cooldown <= 0 and (not obstacles or (WINDOW_WIDTH - obstacles[-1].x >= tree_distance)):
                obstacles.append(Tree(WINDOW_WIDTH))
                tree_cooldown = random.uniform(1, 3)

            # Moves the obstacles accross the screen
            for obstacle in obstacles:
                if obstacle.x + obstacle.img.get_width() < 0:
                    continue  # Skip processing the current obstacle if it's off the screen
                obstacle.move()

            # Removes the off-screen obstacles
            obstacles = [obstacle for obstacle in obstacles if not obstacle.off_screen()]

            # Logic for collision detection and negitive/positive fitness scoring
            for obstacle in obstacles:
                for i, cappy in enumerate(cappy_objects):
                    # Gives a reward for avoiding the obstacles
                    if not obstacle.collision(cappy): 
                        ge[i].fitness += 0.25

                        # Rewards the AI for passing obstacles
                        if obstacle.x + obstacle.img.get_width() < cappy.player_pos.x:
                            ge[i].fitness += 0.2 

                        # Rewards the AI for using momentum to help avoid obstacles
                        if abs(obstacle.x - cappy.player_pos.x) < 50 and abs(cappy.cappy_velocity_y) > 0:
                            ge[i].fitness += 0.2

                    if obstacle.collision(cappy):  # Penalizes the AI for collision with obstacles
                        ge[i].fitness -= 2.5
                        nets.pop(i)
                        ge.pop(i)
                        cappy_objects.pop(i)

            # Logic for the Neural network control of each Cappy
            for i, cappy in enumerate(cappy_objects):
                # Inputs: Normalize values for better neural network processing
                if len(obstacles) > 0:
                    obstacle = obstacles[0]
                    inputs = (
                        cappy.player_pos.y / WINDOW_HEIGHT,                  # The vertical position of cappybara sprite
                        (obstacle.x - cappy.player_pos.x) / WINDOW_WIDTH,    # The horizontal distance between objects and obstacles
                        (obstacle.y - cappy.player_pos.y) / WINDOW_HEIGHT,   # The vertical distance between objects and obstacles
                        cappy.cappy_velocity_y / WINDOW_HEIGHT               # Momentum of the cappybara sprite
                    )
                else:
                    inputs = (cappy.player_pos.y / WINDOW_HEIGHT, 0, 0, 0)  # Default inputs if there are no obstacles

                # Outputs the neural network's results
                output = nets[i].activate(inputs)

                # Simulates the AI's keypressing decisions
                keys = {
                    "jump": output[0] > 0.5,       # Simulates the SPACE/W key being pressed
                    "move_left": output[1] > 0.5,  # Simulates the A key being pressed
                    "move_right": output[2] > 0.5  # Simulates the D key being pressed
                }

                # this replace the AI's decisions with the apporiate key presses
                if keys["jump"] and not cappy.is_jumping:
                    cappy.cappy_velocity_y = cappy.JUMP_STRENGTH
                    cappy.is_jumping = True

                    # Penalizes any unnecessary jump when there is no visable threat nearby
                    if keys["jump"] and abs(obstacle.x - cappy.player_pos.x) > 100 and abs(cappy.player_pos.y - obstacle.y) > 50:
                        ge[i].fitness -= 1

                    # Penalizes the AI for jumping with no momentum
                    if keys["jump"] and abs(cappy.cappy_velocity_y) < 0.1:
                        ge[i].fitness -= 1

                if keys["move_left"]:
                    cappy.player_pos.x -= 300 * dt
                    if cappy.player_pos.x < 0:          # This prevent the sprite from moving out of bounds
                        cappy.player_pos.x = 0

                if keys["move_right"]:
                    cappy.player_pos.x += 300 * dt
                    if cappy.player_pos.x > WINDOW_WIDTH - cappy.img.get_width():
                        cappy.player_pos.x = WINDOW_WIDTH - cappy.img.get_width()

                # Rewards the AI for staying closer to the middle of the screen
                middle_x = WINDOW_WIDTH / 2
                distance_from_middle = abs(cappy.player_pos.x - middle_x) / (WINDOW_WIDTH / 2)
                ge[i].fitness += max(0, 1 - distance_from_middle)  # When the AI is closer to middle = higher reward

                # Rewards the AI for staying alive longer over time
                ge[i].fitness += 0.2

                # Updates Cappy's position
                cappy.move(dt, WINDOW_WIDTH)

            # Updates the display with the objects. background, obstacles, etc
            if cappy_objects:  # Makes sure there are still Cappies left
                elapsed_time = time.time() - start_time
                Draw.draw_window(WIN, cappy_objects, bg1_x1, bg1_x2, bg2_x1, bg2_x2, obstacles, elapsed_time)

            # This stops the simulation after 45 seconds or when no Cappies are alive
            if time.time() - start_time > 45:
                break

    def run(self, config_file, WIN):
        """
        Runs the NEAT algorithm to train the AI to play the game.
        """
        # Loads the NEAT configuration from the provided file
        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_file
        )

        # Creates a NEAT population for testing
        population = neat.Population(config)

        # Adds the progress of the AI using reporters
        population.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        population.add_reporter(stats)

        # Runs the NEAT AI for multiple generations for better results
        winner = population.run(lambda genomes, config: self.genome_evaluate(genomes, config, WIN), 50)

        # Display the final results on the game screen at the end
        final_results(WIN, winner, self.gen)


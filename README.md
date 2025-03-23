# NEAT AI Capybara Adventure

---

## **Project Overview**
This project showcases a **NEAT (NeuroEvolution of Augmenting Topologies)** AI implementation for a game called **Capybara Adventure**, where a NEAT AI-powered Capybara sprites navigate obstacles in a dynamically scrolling environment. The AI uses **neural networks** and **genetic algorithms** to evolve and improve its gameplay over multiple generations.

---

## **NEAT Setup**
- **Inputs**:  
  - Capybara's vertical position (`Cappy.y`)  
  - Horizontal distance to the nearest obstacle (`Obstacle.x - Cappy.x`)  
  - Vertical distance to the nearest obstacle (`Obstacle.y - Cappy.y`)  
  - Capybara's vertical velocity (`Cappy.velocity_y`)
  
- **Outputs**:  
  - Jump (Simulating SPACE/W key)  
  - Move Left (Simulating A key)  
  - Move Right (Simulating D key)
  
- **Activation Function**:  
  - **TanH** for smooth and normalized outputs.

- **Population Size**:  
  - 30 genomes in each generation.

- **Fitness Function**:  
  - Rewards:
    - Surviving longer.
    - Covering more distance.  
    - Passing obstacles.
  - Penalizes:
    - Collisions with obstacles.
    - Unnecessary movements.

- **Maximum Generations**:  
  - 50 Generations

---

## **Game Mechanics**
1. **Capybara Movement**:  
   - Controlled by neural networks outputting movement decisions (jump, left, right).  
   - Gravity is applied for realistic physics during jumps.  
   - Prevents moving out of screen bounds.

2. **Obstacles**:  
   - Randomly spawn across the scrolling background.  
   - Trees serve as the primary obstacles to be avoided.

3. **Fitness Evaluation**:  
   - AI is rewarded for:
     - Time spent alive.
     - Distance covered.
     - Momentum usage to clear obstacles.
   - AI is penalized for:
     - Collisions with obstacles.  
     - Unnecessary or ineffective jumps.

---

## **Resources Used**
- **Images**:
  - **Background Images**:  
    - Forest Background: [OpenGameArt](https://opengameart.org/content/forest-background)  
  - **Capybara Sprite**:  
    - Artist: ANGEL HOU  
  - **Log Sprite**:  
    - Artist: ELLA HO  

- **NEAT Algorithm**:
  - Based on tutorials by **Tech with Tim**:  
    - [Tech with Tim YouTube Series](https://www.youtube.com/watch?v=MPFWsRjDmnU&list=PLzMcBGfZo4-lwGZWXz5Qgta_YNX3_vLS2&index=5)  
    - [NEAT Configurations](https://neat-python.readthedocs.io/en/latest/neat_overview.html)  

---

## **How It Works**
1. **Training**:  
   - NEAT evolves a population of neural networks to maximize fitness.  
   - Networks are evaluated based on gameplay performance, and  the top-performing networks are selected to "breed" the next generation.

2. **Evolution**:  
   - Over 50 generations, genomes improve their ability to avoid obstacles through mutation and crossover.

3. **User Visualization**:  
   - Players can observe the Capybara sprites controlled by the AI as they attempt to survive and learn from mistakes.

4. **Results Screen**:  
   - At the end of the simulation, the game displays:
     - The final generation number.
     - The best genome ID and its fitness (out of 2000).

---

## **Features**
- **Dynamic Scrolling Background**:  
  - Immersive forest-themed background loops to simulate Capybara movement.
  
- **Customizable Configurations**:  
  - Adjustable obstacle difficulty, jump strength, and NEAT parameters.

- **AI Performance Metrics**:  
  - Fitness tracking.
  - Real-time adjustments for better navigation.

- **Modular Design**:  
  - The project is split into separate files for **sprites**, **obstacles**, **drawing utilities**, and **results rendering** for maintainability.

---

## **How to Run the Project**
1. **Setup**:
   - Clone the repository.
   - Ensure all dependencies are installed (`pygame`, `neat-python`).

2. **Start the Simulation**:
   - Run `MainAI.py` to launch the NEAT AI simulation.  
   - Observe AI-controlled Capybaras navigating obstacles.

3. **View Results**:
   - After 50 generations, the game window will display:
     - Simulation complete message.
     - Best genome ID and fitness.

---

## **Future Improvements**
- **Replay Feature**:  
  - Allow users to replay the best genome's performance.
  
- **Advanced Obstacles**:  
  - Introduce varied obstacle types for more challenging gameplay.  

- **Leaderboards**:  
  - Display historical best genomes for comparison.

---

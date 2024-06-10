import pygame
from sys import exit
import random

# Importing global constants
from game.globals import *

# Importing classes
from game.car import Car
from game.track import Track
from neat.population import Population
from neat.genome import Genome
from neat.gene import Gene
from neat.synapse import Synapse


pygame.init()


# Set Font
font = pygame.font.SysFont("Segoe", 26)

# Window
window = pygame.display.set_mode((1500, 700), pygame.RESIZABLE)

clock = pygame.time.Clock()

population = Population(POPULATION_SIZE, NUM_INPUTS, NUM_OUTPUTS)


def main():
    
    timer_var = 0
    generation = 1
    race_track = Track(TRACK_IMAGE)
    running = True
    
    race_cars = []
    for individual in population.individuals:
        race_cars.append(Car(individual, INITIAL_X, INITIAL_Y))
    end_generation = False
    
    while running:
                

        if end_generation:
            race_cars = []
            generation += 1
            
            for individual in population.individuals:
                race_cars.append(Car(individual, INITIAL_X, INITIAL_Y))
        
        
        end_generation = False
        
        timer_var += 1/FPS
        timer_text = font.render(f'Time: {int(timer_var)}', True, (0, 0, 0))
        
        max_car = max(race_cars, key=lambda x: x.individual.fitness)
        
        for race_car in race_cars:
            if race_car != max_car:
                race_car.show_radar = False
        max_car.show_radar = True
 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                    
        key = pygame.key.get_pressed()
        
        if key[pygame.K_q]:
            running = False
            
        if TEST_MODE:
            if key[pygame.K_LEFT]:
                race_cars[0].left = True
            if key[pygame.K_RIGHT]:
                race_cars[0].right = True
            if key[pygame.K_UP]:
                race_cars[0].forward = True
        else:
            for race_car in race_cars:
                race_car.think()
                
            
        window.fill(WHITE)
        race_track.draw(window)
        
            
        for race_car in race_cars: 
            
            race_car.check_track_limits(race_track)
    
            race_car.update(race_track)
                
            if all(race_car.dead for race_car in race_cars):
                for race_car in race_cars:
                    race_car.dead_action()
                    end_generation = True
                    population.evolve()
                    
            if HEAVY_GRAPHICS:
                race_car.display(window)
                
            race_car.radar_scan(race_track, window)
        
        if not HEAVY_GRAPHICS:
            max_car.display(window)
        
        if HEAVY_GRAPHICS:
            num_cars_font = font.render(f'Remaining cars: {len([alive for alive in race_cars if alive.dead == False ])}', True, (0, 0, 0))
            generation_font = font.render(f'Generation: {generation}', True, (0, 0, 0))
            max_fitness_text = font.render(f'Max fitness: {int(max_car.individual.fitness)}', True, (0, 0, 0)) 
            radar_text = font.render(f'Radar: {[int(x) for x in max_car.radar]}', True, (0, 0, 0))
            window.blit(timer_text, (10, 10))  # Change the position as needed
            window.blit(radar_text, (10, 40))
            window.blit(max_fitness_text, (10, 70))
            window.blit(num_cars_font, (10, 100))
            window.blit(generation_font, (10, 130))
            
        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()
    exit()    
         
# Run only if this file is executed
if __name__ == "__main__":
    main()
import pygame
from sys import exit
import random

# Importing global constants
from game.globals import *

# Importing classes
from game.car import Car
from game.track import Track

pygame.init()


# Set Font
font = pygame.font.SysFont("Segoe", 26)

# Window
window = pygame.display.set_mode((1500, 700), pygame.RESIZABLE)

clock = pygame.time.Clock()

def main():
    race_car = Car(INITIAL_X, INITIAL_Y)
    race_track = Track()
    
    running = True
    
    while running:
        
        race_car.timer += 1/FPS
        timer_text = font.render(f'Time: {int(race_car.timer)}', True, (0, 0, 0))
        max_fitness_text = font.render(f'Max fitness: {int(race_car.fitness)}', True, (0, 0, 0)) 

        
        radar_text = font.render(f'Radar: {[int(x) for x in race_car.radar]}', True, (0, 0, 0))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                    
        key = pygame.key.get_pressed()
        
        if key[pygame.K_q]:
            running = False
        if key[pygame.K_LEFT]:
            race_car.left = True
        if key[pygame.K_RIGHT]:
            race_car.right = True
        if key[pygame.K_UP]:
            race_car.forward = True
         
        race_car.check_track_limits(race_track)
    
        race_car.update(race_track)
                
        if race_car.dead:
            race_car.dead_action()
            race_car.timer = 0
                
        window.fill(WHITE)
        race_track.draw(window)
        race_car.display(window)
        race_car.radar_scan(race_track, window)
        
        window.blit(timer_text, (10, 10))  # Change the position as needed
        window.blit(radar_text, (10, 40))
        window.blit(max_fitness_text, (10, 70))


        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()
    exit()    
         
# Run only if this file is executed
if __name__ == "__main__":
    main()
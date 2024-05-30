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
        
        window.fill(WHITE)
        race_track.draw(window)
        race_car.display(window)

        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()
    exit()    
         
# Run only if this file is executed
if __name__ == "__main__":
    main()
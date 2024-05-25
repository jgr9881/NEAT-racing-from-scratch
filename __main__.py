import pygame
from sys import exit
import random

# Importing global constants
from game.globals import *

# Importing classes
from game.car import Car

pygame.init()


# Set Font
font = pygame.font.SysFont("Segoe", 26)

# Window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

def main():
    race_car = Car(INITIAL_X, INITIAL_Y, RED)
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
            
        race_car.update()
        
        window.fill(WHITE)
        race_car.display(window)

        pygame.display.flip()
        
        clock.tick(FPS)
        
    pygame.quit()
    exit()    
         
# Run only if this file is executed
if __name__ == "__main__":
    main()
import pygame
import math
from game.globals import *

# TO DO : ADD BRAKES -> FORCES THE AGENT TO BRAKE TO TURN BETTER (rapport between speed and turn speed)

class Car:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.angle = 0
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        self.color = color
        self.left = False
        self.right = False
        self.forward = False
        self.speed = 0
        self.acceleration = CAR_ACCELERATION
        self.deceleration = CAR_DECCELERATION
        self.max_speed = MAX_SPEED
        self.turn_speed = TURNING_SPEED
        self.original_image = pygame.image.load(CAR_IMAGE)
        self.image = pygame.transform.scale(self.original_image, (CAR_WIDTH, CAR_HEIGHT))
        self.dead = False
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def reset_data(self):
        self.left = False
        self.right = False
        self.forward = False
        self.backward = False
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def rotate(self):
        if self.angle > 360:
            self.angle = 0
        else:
            if self.angle < 0:
                self.angle = 360
        if self.left and self.speed != 0:
            self.angle += self.turn_speed / (self.speed/2 + 1)
        if self.right and self.speed != 0:
            self.angle -= self.turn_speed / (self.speed/2 + 1)
        self.rect = self
    
    def move(self):
        if self.forward:
            if self.speed < self.max_speed:
                self.speed += self.acceleration + (self.speed / 100)
        else:
            if self.speed > MIN_SPEED:
                self.speed -= self.deceleration
            else:
                self.speed = MIN_SPEED

        angle_rad = deg_to_rad(self.angle)
        self.move_x = -(float(self.speed * math.sin(angle_rad)))
        self.move_y = -(float(self.speed * math.cos(angle_rad)))
        self.x += self.move_x
        self.y += self.move_y

    def display(self, window):
        temp_image = pygame.transform.rotate(self.image, self.angle)
        window.blit(temp_image, (self.rect.x, self.rect.y))
        

    def update(self):
        self.move_x = 0
        self.move_y = 0
        self.rotate()
        self.move()
        self.reset_data()   

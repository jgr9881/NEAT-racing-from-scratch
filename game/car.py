import pygame
import math
import random
from game.globals import *

# TO DO : ADD BRAKES -> FORCES THE AGENT TO BRAKE TO TURN BETTER (rapport between speed and turn speed)
# and can't turn while braking (understeer)

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RANDOM_COLOR_LIST[random.randint(0, len(RANDOM_COLOR_LIST) - 1)]
        self.angle = 0
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
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
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.timer = 0
        self.radar = []
        self.radar_angles = []
        self.show_radar = True
        self.fitness = 0 # fitness of the car
    
    def update_fitness(self, track):
        if not self.dead:
            self.fitness += FITNESS_TIME
            self.fitness += self.speed * FITNESS_SPEED
            if track.image.get_at((int(self.x), int(self.y))) == CHECKPOINT_COLOR:
                self.fitness += FITNESS_CHECKPOINT
        
    def calculate_distance(self, point1, point2):
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    
    def radar_scan(self, track, window):
        self.radar = RADAR_INIT
        self.radar_angles = RADAR_ANGLES
        radar_size = len(self.radar)
        for i in range(radar_size):
            angle = self.radar_angles[i] + self.angle
            x = self.x
            y = self.y
            while True:
                x += math.cos(math.radians(angle))
                y -= math.sin(math.radians(angle))
                if x < 0 or y < 0 or x >= track.image.get_width() or y >= track.image.get_height():
                    break
                if self.calculate_distance((self.x, self.y), (x, y)) > RADAR_LENGTH:
                    break
                if track.image.get_at((int(x), int(y))) == DEATH_COLOR:
                    break
                if self.show_radar:
                    pygame.draw.line(window, (255, 0, 0), (self.x, self.y), (x, y), 1)
                self.radar[i] = self.calculate_distance((self.x, self.y), (x, y))

              
    def check_track_limits(self, track):
        if self.x < 0:
            self.dead = True
        if self.x > track.width:
            self.dead = True
        if self.y < 0:
            self.dead = True
        if self.y > track.height:
            self.dead = True
        # Check if the car is on the track
        if track.image.get_at((int(self.x), int(self.y))) == DEATH_COLOR:
            self.dead = True

    
            
    def dead_action(self):
        self.reset_data()
        self.x = INITIAL_X
        self.y = INITIAL_Y
        self.angle = 0
        self.speed = MIN_SPEED
        self.dead = False
        if TEST_MODE:
            self.fitness = 0
    
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
            self.angle += self.turn_speed / (self.speed/TURNING_SPEED_REDUCTION + 1)
        if self.right and self.speed != 0:
            self.angle -= self.turn_speed / (self.speed/TURNING_SPEED_REDUCTION + 1)
        self.rect = self
    
    def move(self, track):
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
        self.check_track_limits(track)

    def display(self, window):
        #temp_image = pygame.transform.rotate(self.image, self.angle)
        #window.blit(temp_image, (self.rect.x, self.rect.y))
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), 5)


    def update(self, track):
        self.move_x = 0
        self.move_y = 0
        self.rotate()
        self.move(track)
        self.reset_data() 
        self.timer += 1
        self.update_fitness(track)  

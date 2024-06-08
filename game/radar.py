import pygame
import math
from game.globals import *

class Radar:
    def __init__(self, car, track):
        self.car = car
        self.track = track
        self.radar_length = 100
        self.radar_points = []

    def update(self):
        # Calculate the endpoints of the lines
        left_end = (self.car.rect.x, self.car.rect.y - (self.car.rect.y - self.track.y))
        right_end = (self.car.rect.x, self.car.rect.y + (self.track.y + self.track.height - self.car.rect.y))
        front_end = (self.car.rect.x + (self.track.x + self.track.width - self.car.rect.x), self.car.rect.y)

        # Update the radar points
        self.radar_points = [left_end, right_end, front_end]

    def draw(self, window):
        # Draw the lines
        for point in self.radar_points:
            pygame.draw.line(window, (255, 0, 0), (self.car.rect.x, self.car.rect.y), point)


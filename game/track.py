import pygame
from game.globals import *

class Track:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load(TRACK_IMAGE), (TRACK_WIDTH, TRACK_HEIGHT))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        
    def draw(self, window):
        window.blit(self.image, (0, 0))
# Description: Global variables for the game

import math

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 60

# Car constants
CAR_WIDTH, CAR_HEIGHT = 10, 20
MAX_SPEED = 15
MIN_SPEED = 1.5
TURNING_SPEED = 4.4
CAR_IMAGE = 'assets/Grey.png'
INITIAL_X, INITIAL_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
CAR_ACCELERATION, CAR_DECCELERATION = 0.08, 0.2

# Useful functions
def deg_to_rad(degrees):
    return degrees / 180.0 * math.pi
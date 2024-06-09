# Description: Global variables for the game

import math

TEST_MODE = True # Set to True to test individual cars

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1500, 800
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
RANDOM_COLOR_LIST = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, BROWN, CYAN]
BLEU_CIEL_CIRCUIT = (112, 146, 190)
GRIS_CIRCUIT = (127, 127, 127)
BLEU_CHECKPOINT = (63, 72, 204)
FPS = 60

# Car constants
CAR_WIDTH, CAR_HEIGHT = 10, 20
MAX_SPEED = 15
MIN_SPEED = 2
TURNING_SPEED = 4.8
CAR_IMAGE = 'assets/formula_one.png'
INITIAL_X, INITIAL_Y = SCREEN_WIDTH // 2 - 80, (SCREEN_HEIGHT // 2) - 230
CAR_ACCELERATION, CAR_DECCELERATION = 0.08, 0.2
TURNING_SPEED_REDUCTION = 1.8

# Track constants
TRACK_IMAGE = 'assets/grey_track_checkpoints.png'
DEATH_COLOR = GRIS_CIRCUIT
TRACK_WIDTH, TRACK_HEIGHT = 1500, 700
CHECKPOINT_COLOR = BLEU_CHECKPOINT

# Radar constants
RADAR_LENGTH = 1200
RADAR_INIT = [0, 0, 0, 0, 0, 0, 0, 0, 0]
RADAR_ANGLES = [180, 150, 110, 92, 90, 88, 70, 30, 0]

# Fitness constants
FITNESS_CHECKPOINT = 1000
FITNESS_SPEED = 1
FITNESS_TIME = 1

# NEAT constants
MIN_SYNAPSES = 3
MIN_GENES = 12

# Mutation constants
INIT_MEAN = 0
INIT_STD = 1
MUTATION_RATE = 0.8
MUTATE_POWER = 0.5
REPLACE_RATE = 0.1
MIN_MUTATE = -20
MAX_MUTATE = 20

# Useful functions
def deg_to_rad(degrees):
    return degrees / 180.0 * math.pi

def gene_activation_function(x):
    return 1 / (1 + math.exp(-x))
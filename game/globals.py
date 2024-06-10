# Description: Global variables for the game

import math

TEST_MODE = False # Set to True to play the game manually
HEAVY_GRAPHICS = True # Set to True to show the radar and graphic details

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
RADAR_ANGLES = [180, 150, 110, 92, 90, 88, 70, 30, 0]
RADAR_INIT = [0] * len(RADAR_ANGLES)

# Fitness constants
FITNESS_CHECKPOINT = 4000
FITNESS_SPEED = 3
FITNESS_TIME = 1

# NEAT constants
MIN_SYNAPSES = 1
NUM_OUTPUTS = 3
NUM_INPUTS = len(RADAR_ANGLES) + 3
MIN_GENES = NUM_INPUTS + NUM_OUTPUTS # Number of radar inputs + speed + angle + fitness + 3 outputs (left, right, forward)


FIT_POPULATION = 3 # Number of selected individuals to reproduce each generation
POPULATION_SIZE = 80
MAX_GENERATIONS = 100
EVOLVE_RANDOM = 0.8

# Mutation constants
INIT_MEAN = 0
INIT_STD = 1
MUTATION_RATE = 0.8
GENE_MUTATE_POWER = 0.4
SYNAPSE_MUTATE_POWER = 0.4
REPLACE_RATE = 0.1
REPLACE_VARIATION_BIAS = 3
REPLACE_VARIATION_WEIGHT = 3
ADD_SYNAPSE_RATE = 0.4
REMOVE_SYNAPSE_RATE = 0.2
ADD_GENE_RATE = 0.4
REMOVE_GENE_RATE = 0.2

# Useful functions
def deg_to_rad(degrees):
    return degrees / 180.0 * math.pi

def safe_exp(x):
    # Clamp x to a range that won't cause overflow
    x = max(min(x, 50), -50)
    return math.exp(x)

def gene_activation_function(x):
    return 1 / (1 + math.exp(-safe_exp(x)))

def input_activation_function(x):
    return x
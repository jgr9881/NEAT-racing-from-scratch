# neuron gene
import random
from game.globals import *

class Gene:
    def __init__(self, neuron_id, bias, activation_function):
        self.neuron_id = neuron_id
        self.bias = bias
        self.activation_function = activation_function
        self.input = 0
        self.weight = random.uniform(-1, 1)
        self.output = 0
        self.layer = 0
        
    def crossover_gene(self, other_gene):
        if self.neuron_id not in range(-1, -NUM_INPUTS - 1, -1) and self.neuron_id not in range(1, NUM_OUTPUTS + 1):
            assert self.neuron_id == other_gene.neuron_id
            neuron_id = self.neuron_id
            bias = (self.bias + other_gene.bias) / 2
            if random.random() < 0.5:
                activation_function = self.activation_function
            else:
                activation_function = other_gene.activation_function
            return Gene(neuron_id, bias, activation_function)        
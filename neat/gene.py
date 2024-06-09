# neuron gene
import random

class Gene:
    def __init__(self, neuron_id, bias, activation_function):
        self.neuron_id = neuron_id
        self.bias = bias
        self.activation_function = activation_function
        
    def crossover_gene(self, other_gene):
        assert self.neuron_id == other_gene.neuron_id
        neuron_id = self.neuron_id
        bias = (self.bias + other_gene.bias) / 2
        if random.random() < 0.5:
            activation_function = self.activation_function
        else:
            activation_function = other_gene.activation_function
        return Gene(neuron_id, bias, activation_function)        
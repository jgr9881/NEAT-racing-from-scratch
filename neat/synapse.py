# synapses connect the genes
import random

class Synapse:
    def __init__(self, input_id, output_id, weight, enabled):
        self.input_id = input_id
        self.output_id = output_id
        self.weight = weight
        self.enabled = enabled # if the synapse is enabled or not (boolean)
        
    def crossover_synapse(self, other_synapse):
        assert self.input_id == other_synapse.input_id and self.output_id == other_synapse.output_id
        input_id = self.input_id
        output_id = self.output_id
        weight = (self.weight + other_synapse.weight) / 2
        if random.random() < 0.5:
            enabled = self.enabled
        else:
            enabled = other_synapse.enabled
        return Synapse(input_id, output_id, weight, enabled)
        
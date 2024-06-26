# group of genes (also known as a chromosome)
from neat.gene import Gene
from neat.synapse import Synapse
import random

class Genome:
    def __init__(self, genome_id, num_inputs, num_outputs, genes, synapses):
        self.genome_id = genome_id
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.genes = genes
        self.synapses = synapses
        self.max_layer = 1
                 
    def update_layers(self):
        for gene in self.genes:
            if gene.layer > self.max_layer:
                self.max_layer = gene.layer
    
    def add_gene(self, gene):    
        self.genes.append(gene)
        
    def remove_gene(self, gene):
        self.genes.remove(gene)

    def add_synapse(self, synapse):
        self.synapses.append(synapse)
        
    def remove_synapse(self, synapse):
        self.synapses.remove(synapse)
        
    def gene_exists(self, neuron_id):
        for gene in self.genes:
            if gene.neuron_id == neuron_id:
                return True
        return False
    
    def get_gene(self, neuron_id):
        zero_gene = Gene(0, 0, 0)
        for gene in self.genes:
            if gene.neuron_id == neuron_id:
                return gene
        return zero_gene
    
    def synapse_exists(self, input_id, output_id):
        for synapse in self.synapses:
            if synapse.input_id == input_id and synapse.output_id == output_id:
                return True
        return False

    def get_synapse(self, input_id, output_id):
        for synapse in self.synapses:
            if synapse.input_id == input_id and synapse.output_id == output_id:
                return synapse
        return None
    
    def would_create_cycle(self, input_id, output_id, visited=None):
        if visited is None:
            visited = []
        if input_id == output_id:
            return True
        visited.append(input_id)
        for synapse in self.synapses:
            if synapse.input_id == input_id:
                if synapse.output_id not in visited:
                    if self.would_create_cycle(synapse.output_id, output_id, visited):
                        return True
        return False
    
    def new_neuron_id(self):
        if len(self.genes) == 0:
            return 1
        else :
            neuron_ids = [gene.neuron_id for gene in self.genes]
            return max(neuron_ids) + 1

from game.globals import *
from neat.genome import Genome
from neat.synapse import Synapse
from neat.gene import Gene
import random

def mutate_add_synapse(genome):
    # find two random neurons
    gene1_id = random.choice(genome.genes).neuron_id
    gene2_id = random.choice(genome.genes).neuron_id
    weight = random.uniform(-1, 1)
    # add a synapse between the two neurons
    visited = []
    if not genome.would_create_cycle(gene1_id, gene2_id, visited) and not genome.synapse_exists(gene1_id, gene2_id):
        genome.add_synapse(Synapse(gene1_id, gene2_id, weight, True))
    
def mutate_remove_synapse(genome):
    if len(genome.synapses) > MIN_SYNAPSES:
        synapse = random.choice(genome.synapses)
        genome.synapses.remove(synapse)
        
def mutate_add_gene(genome):
    if len(genome.synapses) > MIN_SYNAPSES:
        synapse = random.choice(genome.synapses)
        # disable the synapse
        synapse.enabled = False
        
        # determine the layer position of the new neuron
        layer_position = genome.get_gene(synapse.output_id).layer
        
        # Increase the layer of all genes with a layer greater or equal to the layer of the gene
        for gene in genome.genes:
            if gene.layer >= layer_position:
                gene.layer += 1
                
        # add a new gene
        new_neuron_id = genome.new_neuron_id()
        new_gene = Gene(new_neuron_id, 0, gene_activation_function)
        new_gene.layer = layer_position
        genome.add_gene(new_gene)
        
        # add two new synapses
        genome.add_synapse(Synapse(synapse.input_id, new_neuron_id, 1, True))
        genome.add_synapse(Synapse(new_neuron_id, synapse.output_id, synapse.weight, True))
        
        # update the layers
        genome.update_layers()

def mutate_remove_gene(genome):
    if len(genome.genes) > MIN_GENES:
        removable_genes = [gene for gene in genome.genes if gene.neuron_id > NUM_OUTPUTS]
        if len(removable_genes) != 0:
            gene = random.choice(removable_genes)
            synapses_to_delete = [synapse for synapse in genome.synapses if synapse.input_id == gene.neuron_id or synapse.output_id == gene.neuron_id]
            genome.remove_gene(gene)
            # remove all synapses connected to the gene
            for synapse in synapses_to_delete:
                genome.remove_synapse(synapse)
            
def non_structural_mutation(genome):
    if random.random() < REPLACE_RATE:
        for gene in genome.genes:
            gene.bias = random.uniform(-REPLACE_VARIATION_BIAS, REPLACE_VARIATION_BIAS)
        for synapse in genome.synapses:
            synapse.weight = random.uniform(-REPLACE_VARIATION_BIAS, REPLACE_VARIATION_BIAS)
    for gene in genome.genes:
        if random.random() < MUTATION_RATE:
            gene.bias += random.uniform(-GENE_MUTATE_POWER, GENE_MUTATE_POWER)
    for synapse in genome.synapses:
        if random.random() < MUTATION_RATE:
            synapse.weight += random.uniform(-SYNAPSE_MUTATE_POWER, SYNAPSE_MUTATE_POWER)            
            
def mutate(genome):
    if random.random() < ADD_SYNAPSE_RATE:
        mutate_add_synapse(genome)
    if random.random() < REMOVE_SYNAPSE_RATE:
        mutate_remove_synapse(genome)
    if random.random() < ADD_GENE_RATE:
        mutate_add_gene(genome)
    if random.random() < REMOVE_GENE_RATE:
        mutate_remove_gene(genome)
    non_structural_mutation(genome)
    return genome
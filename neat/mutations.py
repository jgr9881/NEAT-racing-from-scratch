from game.globals import *
from genome import Genome
from synapse import Synapse
from gene import Gene
import random

def mutate_add_synapse(genome):
    # find two random neurons
    gene1_id = random.choice(genome.genes).neuron_id
    gene2_id = random.choice(genome.genes).neuron_id
    weight = random.uniform(-1, 1)
    # add a synapse between the two neurons
    if not genome.would_create_cycle(gene1_id, gene2_id) and not genome.synapse_exists(gene1_id, gene2_id):
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
        # add a new gene
        new_neuron_id = genome.get_new_neuron_id()
        new_gene = Gene(new_neuron_id, 0, gene_activation_function)
        genome.add_gene(new_gene)
        # add two new synapses
        genome.add_synapse(Synapse(synapse.input_id, new_neuron_id, 1, True))
        genome.add_synapse(Synapse(new_neuron_id, synapse.output_id, synapse.weight, True))

def mutate_remove_gene(genome):
    if len(genome.genes) > MIN_GENES:
        gene = random.choice(genome.genes)
        synapses_to_delete = [synapse for synapse in genome.synapses if synapse.input_id == gene.neuron_id or synapse.output_id == gene.neuron_id]
        genome.remove_gene(gene)
        # remove all synapses connected to the gene
        for synapse in synapses_to_delete:
            genome.remove_synapse(synapse)
            

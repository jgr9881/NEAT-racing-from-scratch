from neat.genome import Genome
from neat.gene import Gene
from neat.mutations import *
from neat.feedforward import Feedforward
import random

class Individual:
    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness
        
    def reproduce(self, dominant_individual, recessive_individual):
        assert dominant_individual.fitness >= recessive_individual.fitness
        offspring_genome = Genome(None, dominant_individual.genome.num_inputs, dominant_individual.genome.num_outputs, [], [])
        offspring_genome.genome_id = offspring_genome.new_neuron_id()
        # Add genes for the inputs
        for j in range(1, NUM_INPUTS + 1):
            input_gene = Gene(-j, 0, input_activation_function)
            input_gene.layer = 0
            offspring_genome.add_gene(input_gene)            
        # Add genes for the outputs
        for j in range(1, NUM_OUTPUTS + 1):
            output_gene = Gene(j, random.uniform(-1, 1), gene_activation_function)
            output_gene.layer = 1                
            offspring_genome.add_gene(output_gene)
        # inherit neuron genes
        new_gene_layer = min(dominant_individual.genome.max_layer - 1, recessive_individual.genome.max_layer - 1)
        for gene in dominant_individual.genome.genes:
            if gene.neuron_id > NUM_OUTPUTS:
                gene.layer = new_gene_layer
                neuron_id = gene.neuron_id
                if not recessive_individual.genome.gene_exists(neuron_id):
                    offspring_genome.add_gene(gene)
                else:
                    recessive_gene = recessive_individual.genome.get_gene(neuron_id)
                    offspring_gene = gene.crossover_gene(recessive_gene)
                    offspring_genome.add_gene(offspring_gene)
        # inherit synapse genes
        for synapse in dominant_individual.genome.synapses:
            input_id = synapse.input_id
            output_id = synapse.output_id
            if not recessive_individual.genome.synapse_exists(input_id, output_id):
                offspring_genome.add_synapse(synapse)
            else:
                recessive_synapse = recessive_individual.genome.get_synapse(input_id, output_id)
                offspring_synapse = synapse.crossover_synapse(recessive_synapse)
                offspring_genome.add_synapse(offspring_synapse)
        
        if random.random() < MUTATION_RATE:
            return mutate(offspring_genome)        
        else:
            return offspring_genome
    
    # random actions
    def think(self, inputs):
        outputs = []
        for i in range(NUM_OUTPUTS):
            outputs.append(bool(random.getrandbits(1)))
        return outputs
    
    def think_feedforward(self, inputs):
        neat = Feedforward()
        return neat.output(self.genome, inputs)
from genome import Genome
from gene import Gene

class Individual:
    def __init__(self, genome, fitness):
        self.genome = genome
        self.fitness = fitness
        
    def crossover_individual(self, dominant_individual, recessive_individual):
        offspring_genome = Genome(None, dominant_individual.genome.num_inputs, dominant_individual.genome.num_outputs, [], [])
        # inherit neuron genes
        for gene in dominant_individual.genome.genes:
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
                
        return offspring_genome
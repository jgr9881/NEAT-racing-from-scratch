from game.globals import *
from neat.gene import Gene
from neat.synapse import Synapse
from neat.genome import Genome

class Feedforward:
    def __init__(self):
        self.activation_function = gene_activation_function
        
    def output(self, genome, inputs):

        input_genes = [gene for gene in genome.genes if gene.neuron_id <= 0]
        
        # Set the output values in the input neurons
        for gene in input_genes:
            gene.input = inputs[-gene.neuron_id - 1]
            gene.output = inputs[-gene.neuron_id - 1]

            
        # Compute the output of the neural network
        for layer in range(genome.max_layer + 1):
            for gene in genome.genes:
                if gene.layer == layer:
                    # here -> all the inputs of the previous layer are computed
                    for synapse in genome.synapses:
                        if synapse.output_id == gene.neuron_id:
                            gene.input += genome.get_gene(synapse.input_id).output * synapse.weight
                    gene.output = self.activation_function(gene.input + gene.bias)
                    
        # Return the output of the output neurons
        
        output_ids = [x + 1 for x in range(NUM_OUTPUTS)]        
        outputs = [gene.output for gene in genome.genes if gene.neuron_id in output_ids]
        
        boolean_outputs = [activation_outputs > 0.5 for activation_outputs in outputs]
                        
        return boolean_outputs
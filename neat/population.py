from neat.genome import Genome
from neat.gene import Gene
from neat.synapse import Synapse
from neat.individual import Individual
from game.globals import *
from itertools import combinations
from neat.mutations import *


import random

class Population:
    def __init__(self, population_size, num_inputs, num_outputs):
        self.population_size = population_size
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.individuals = []
        
        # Initialize the population (simple feedforward neural network with no hidden layers)
        for i in range(population_size):
            genome = Genome(i, num_inputs, num_outputs, [], [])
            # Add genes for the inputs
            for j in range(1, num_inputs + 1):
                input_gene = Gene(-j, 0, input_activation_function)
                input_gene.layer = 0
                genome.add_gene(input_gene)
            # Add genes for the outputs
            for j in range(1, num_outputs + 1):
                output_gene = Gene(j, random.uniform(-1, 1), gene_activation_function)
                output_gene.layer = 1
                genome.add_gene(output_gene)
            # Add synapses between all inputs and outputs
            for input in range(1, num_inputs + 1):
                for output in range(1, num_outputs + 1):
                    genome.add_synapse(Synapse(-input, output, random.uniform(-1, 1), True))
                           
            self.individuals.append(Individual(genome, 0))
            
    def evolve(self):
        # Select the len(FIT_POPULATION) most fit individuals
        sorted_individuals = sorted(self.individuals, key=lambda x: x.fitness, reverse=True)
        fittest_individuals = sorted_individuals[:FIT_POPULATION]

        # Reproduce them 2 by 2 with the fittest individual being the dominant individual
        new_individuals = []
        couples = list(combinations(fittest_individuals, 2))
        for couple in couples:
            if couple[0].fitness < couple[1].fitness:
                couple = (couple[1], couple[0])
            dominant_individual = couple[0]
            recessive_individual = couple[1]
            offspring_genome = dominant_individual.reproduce(dominant_individual, recessive_individual)
            offspring = Individual(offspring_genome, 0)
            new_individuals.append(offspring)
        
        # Replace the least fit individuals with the new offspring
        self.individuals = fittest_individuals + new_individuals 
        
        # Complete the remaining population with random individuals
        while len(self.individuals) < POPULATION_SIZE:
            if random.random() < EVOLVE_RANDOM:
                # pick a random genome from the fittest individuals:
                fit_genome = random.choice(fittest_individuals).genome
                if random.random() < MUTATION_RATE:
                    fit_genome = mutate(fit_genome)
                self.individuals.append(Individual(fit_genome, 0))
            else :
                genome = Genome(None, self.num_inputs, self.num_outputs, [], [])
                # Add genes for the inputs
                for j in range(1, self.num_inputs + 1):
                    input_gene = Gene(-j, 0, input_activation_function)
                    input_gene.layer = 0
                    genome.add_gene(input_gene)
                # Add genes for the outputs
                for j in range(1, self.num_outputs + 1):
                    output_gene = Gene(j, random.uniform(-1, 1), gene_activation_function)
                    output_gene.layer = 1
                    genome.add_gene(output_gene)
                # Add synapses between all inputs and outputs
                for input in range(1, self.num_inputs + 1):
                    for output in range(1, self.num_outputs + 1):
                        genome.add_synapse(Synapse(-input, output, random.uniform(-1, 1), True))
                self.individuals.append(Individual(genome, 0))
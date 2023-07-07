import random
import time

POPULATION_SIZE = 100

ALL_GENEs = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''

indi='abcdefghijklmnopqrstuvwxyz'

TARGET = 'Khai thac du lieu - KTDL'

#region Individual
class Individual(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @classmethod
    def create_random_gene(self):
        global ALL_GENEs
        gene = random.choice(ALL_GENEs)
        return gene

    @classmethod
    def create_random_chromosome(self):
        global TARGET
        chromosome_len = len(TARGET)
        chromosome = []
        for _ in range(chromosome_len):
            random_gene = self.create_random_gene() 
            chromosome.append(random_gene)
        return chromosome

    def crossover(self, individual_2):
        child_chromosome = []
        for gene_of_ind1, gene_of_ind2 in zip(self.chromosome, individual_2.chromosome):
            prob = random.random()

            if prob < 0.45:
                child_chromosome.append(gene_of_ind1)
            elif prob < 0.9:
                child_chromosome.append(gene_of_ind2)
            else:
                random_gene = self.create_random_gene()
                child_chromosome.append(random_gene)
        child = Individual(child_chromosome)
        return child

    def calculate_fitness(self):
        global TARGET
        fitness = 0
        for gene_of_ind, gene_of_target in zip(self.chromosome, TARGET):
            if gene_of_ind == gene_of_target:
                fitness += 1
        return fitness
#endregion

#region Main
def main():
    global POPULATION_SIZE
    global TARGET
    target_len = len(TARGET)

    max_generation = 100
    current_generation = 1

    population = []

    # initialize population
    for _ in range(POPULATION_SIZE):
        random_chromosome = Individual.create_random_chromosome()
        _individual = Individual(random_chromosome)
        population.append(_individual)

    # genetic process
    while current_generation < max_generation:
        population = sorted(population, key = lambda x:x.fitness, reverse=True)
        
        next_generation_of_population = []   

        _10_percent_len = int(10*POPULATION_SIZE/100)
        next_generation_of_population.extend(population[:_10_percent_len])

        _50_percent_len = int(POPULATION_SIZE/2)
        _90_percent_len = int(90*POPULATION_SIZE/100)
        for _ in range(_90_percent_len):
            # crossover top 50% individuals
            parent1 = random.choice(population[:_50_percent_len])
            parent2 = random.choice(population[:_50_percent_len])
            child = parent1.crossover(parent2)

            next_generation_of_population.append(child)

        population = next_generation_of_population
        current_generation += 1

        print("Generation: {0} -- Fitness: {2} -- String: {1}".format(
                                current_generation, 
                                "".join(population[0].chromosome), 
                                population[0].fitness))

        time.sleep(0.05)
#endregion

main()
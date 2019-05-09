import numpy as np


class Individual:
    def __init__(self, target, **kwargs):
        if "ch_size" in kwargs:
            self.ch_size = kwargs["ch_size"]
            self.genes = np.random.randint(0, 2, self.ch_size)
        elif "genes" in kwargs:
            self.ch_size = len(kwargs["genes"])
            self.genes = kwargs["genes"]
        self.target = target

    def random_inst(self):
        self.genes = np.random.randint(0, 2, self.ch_size)

    def get_chromosome(self):
        return self.genes

    def crossover(self, pair_chromosome):
        if self.ch_size == pair_chromosome.get_chromosome().size:
            cross_point = np.random.randint(0, self.ch_size)
            self.genes = np.concatenate(
                (
                    self.genes[0:cross_point],
                    pair_chromosome.get_chromosome()[cross_point : self.ch_size],
                )
            )
        return self.genes

    def mutate(self, num_to_mutate):
        for _ in range(num_to_mutate):
            to_swap = np.random.randint(0, self.genes.size)
            self.genes[to_swap] = abs(self.genes[to_swap] - 1)

    def compute_fitness(self):
        return np.square(self.genes - self.target).mean()

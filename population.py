import numpy as np
from random import shuffle

from individual import Individual


class Population:
    def __init__(self, ch_size, pop_size, target, survival_fraction):
        self.population = []
        self.ch_size = ch_size
        self.target = target
        self.survival_fraction = survival_fraction
        self.pop_size = pop_size

        for _ in range(self.pop_size):
            self.population.append(Individual(self.target, ch_size=self.ch_size))

    #def update_population(self, new_pop):
        #self.population = new_pop

    def get_population(self):
        #return [i.get_chromosome() for i in self.population]
        return self.population

    def get_pop_size(self):
        return len(self.population)

    def select_fittest(self):
        sorted_pop = sorted(self.population, key = lambda x: x.compute_fitness())
        num_to_keep = int(len(sorted_pop)*self.survival_fraction)
        if num_to_keep % 2 == 1:
            num_to_keep-=1
        survivors = sorted_pop[0:num_to_keep]
        return survivors

    def reproduce(self, fittest):
        self.population = fittest

        while len(self.population)<self.pop_size:
            shuffle(fittest)
            half_point = int(len(fittest)/2)

            half1 = fittest[0 : half_point]
            half2 = fittest[half_point : len(fittest)]

            for indiv1, indiv2 in zip(half1, half2):
                if len(self.population)>=self.pop_size:
                    break
                new_indiv = Individual(self.target, genes=indiv1.crossover(indiv2))
                self.population.append(new_indiv)
        return len(self.population)

    def check_convergence(self):
        pass



p = Population(ch_size = 10, pop_size = 150, target = np.zeros(10), survival_fraction = 0.4)
fittest = p.select_fittest()
print(p.reproduce(fittest))

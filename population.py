import numpy as np
from random import shuffle

from individual import Individual


class Population:
    def __init__(self, ch_size, pop_size, target, survival_fraction, convergence_target):
        self.population = []
        self.ch_size = ch_size
        self.target = target
        self.survival_fraction = survival_fraction
        self.pop_size = pop_size
        self.convergence_target = convergence_target

        self.cur_err = 0.0
        self.last_err = 0.0

        self.in_a_row = 0

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
            crossover_point = np.random.randint(0, int(len(fittest)))

            pt1 = fittest[0 : crossover_point]
            pt2 = fittest[crossover_point : len(fittest)]

            for indiv1, indiv2 in zip(pt1, pt2):
                if len(self.population)>=self.pop_size:
                    #break the loop and end the method
                    return len(self.population)
                new_indiv = Individual(self.target, genes=indiv1.crossover(indiv2))
                self.population.append(new_indiv)

    def check_convergence(self):
        self.last_err = self.cur_err
        self.cur_err = np.array([i.get_chromosome() for i in self.get_population()]).mean()

        if self.last_err == self.cur_err:
            self.in_a_row += 1
        else:
            self.in_a_row = 0

        if self.in_a_row == self.convergence_target:
            return True, self.cur_err

        return False, self.cur_err

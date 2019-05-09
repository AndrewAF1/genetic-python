from population import Population

import numpy as np
from itertools import count


print_iter = 10
chromosome_size = 10000
population_size = 10000
target = np.zeros(chromosome_size)
survival_fraction = 0.5
convergence_target = 100000  # times print_iter


p = Population(
    ch_size=chromosome_size,
    pop_size=population_size,
    target=target,
    survival_fraction=survival_fraction,
    convergence_target=convergence_target,
)

for epoch in count(1):
    fittest = p.select_fittest()
    p.reproduce(fittest)
    if epoch % print_iter == 0:
        done, error = p.check_convergence()
        print("Epoch", epoch, "complete. \t Error:", error)

        if done:
            break

print("Converged with error", p.check_convergence()[1])

import numpy as np
from pso import PSO
import matplotlib.pyplot as plt

def plot_pso(x, y, name):
    plt.grid(which='major', axis='y', color='darkgray')
    plt.grid(which='major', axis='x', color='darkgray')
    plt.plot(x,y,color='fuchsia', marker='P', linestyle='dashed')
    plt.xlabel('Number of iteration',size = 15)
    plt.ylabel('Fitness value (cost)',size = 15)
    plt.title('PSO Optimisation')
    # plt.show() 
    plt.savefig(name)

if __name__ == "__main__":
    iterations = 20
    p = PSO(
        worm_size = 15, 
        iterations = iterations, 
        c1 = 2, 
        c2 = 2, 
        pop_size = 30, 
        w = 1
        )

    p.run()

    name = 'particle_explore/cost_records.pdf' 
    x = np.arange(iterations)
    y = p.get_gbest_records()
    print(y)
    plot_pso(x, y, name)
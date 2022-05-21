# PSO class

from hashlib import new
import random
import numpy as np
from util import prep_image
from operator import attrgetter
from cost import CostFunction as cf
from util import Camo_Worm, matrix_to_camo, draw

IMAGE_DIR = 'images'
IMAGE_NAME='original'
MASK = [320, 560, 160, 880] # ymin ymax xmin xmax
rng = np.random.default_rng()

image = prep_image(IMAGE_DIR, IMAGE_NAME, MASK, is_show=False)
imshape = image.shape
(ylim, xlim) = imshape

def get_image():
    return image

(radius_std, deviation_std, width_theta) = (40, 30, 1)

class Particle: 
    
    def __init__(self, solution, velocity, fitness):
        self.solution = solution
        self.pbest = solution

        self.current_solution_fit = fitness
        self.pbest_solution_fit = fitness
    
        self.velocity = velocity
    

    def set_pbest(self, new_pbest):
        """set pbest"""
        self.pbest = new_pbest
    
    def get_pbest(self):
        """returns the pbest """
        return self.pbest

    def set_velocity(self, new_velocity):
         """set the new velocity"""
         self.velocity = new_velocity

    def get_velocity(self):
        """returns the velocity"""
        return self.velocity
    
    def set_current_solution(self, solution):
        """set current solution"""
        self.solution = solution

    def get_current_solution(self):
        """get current solution"""
        return self.solution

    def set_cost_pbest(self, fitness):
        """set fitness value for pbest solution"""
        self.pbest_solution_fit = fitness

    def get_cost_pbest(self):
        """gets fitness value of pbest solution"""
        return self.pbest_solution_fit

    def set_cost_current_solution(self, fitness):
        """set fitness value for the current solution"""
        self.current_solution_fit = fitness

    def get_cost_current_solution(self):
        """gets fitness value of the current solution"""
        return self.current_solution_fit

    def clear_velocity(self):
        """removes all elements of the list velocity"""
        del self.velocity[:]


class PSO:
    
    def __init__(
        self, 
        worm_size = 50,
        iterations = 50,
        pop_size = 50, 
        num_dim = 8, 
        w = 0.8, 
        c1 = 2, 
        c2 = 2
        ):
        """
        param iterations : max iterations to convergence
        param pop_size   : population size
        param num_dim    : dimension of the given task
        param w          : inertia weight
        param c1         : cognitive learning factor for pbest (local best position)
        param c2         : cognitive learning factor for gbest (global best position)
        """

        self.worm_size = worm_size
        self.iterations = iterations
        self.pop_size = pop_size
        self.num_dim = num_dim
        self.w = w
        self.c1 = c1
        self.c2 = c2

        self.particles = []
        self.gbest_record = []

        self.init_swarm()
        self.init_gbest = min(self.particles, key=attrgetter('pbest_solution_fit'))

    def _random_init_worms(self):
        """
        x, y, r, theta, deviation_r, deviation_gamma, width, colour
        """
        mat = np.array(
            [
                [
                    xlim * rng.random(),
                    ylim * rng.random(), 
                    radius_std * np.abs(rng.standard_normal()),
                    rng.random() * np.pi, 
                    deviation_std * np.abs(rng.standard_normal()),
                    rng.random() * np.pi,
                    width_theta * rng.standard_gamma(3),
                    rng.random()
                ]
                for _ in range(self.worm_size)
            ]
        )

        return mat

    def init_swarm(self):  
        print('swarm init...')
        velocity = np.zeros((self.worm_size, self.num_dim))           # Init velocity 
        for i in range(self.pop_size):
            position = self._random_init_worms()
            if position.shape[0] != velocity.shape[0] or position.shape[1] != velocity.shape[1]:
                raise ValueError(f"size of position does not fit for velocity at iter {i}")
            self.particles.append(Particle(position, velocity, self.get_fitness(position)))
        print('swarm init done !')

    def get_init_gbest(self):
        return self.init_gbest.get_pbest()

    def get_fitness(self, position):
        """calling get_cost_worm(position) ? """
        # clew = [Camo_Worm(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]) for i in position]
        return cf.get_particle_cost(matrix_to_camo(position), image)

    def set_gbest(self, new_gbest):
        self.gbest = new_gbest

    def _update_particle(self, par):
        solution_gbest = self.gbest.get_pbest() # gets solution of the gbest
        solution_pbest = par.get_pbest()[:] # gets the pbest solution
        solution_particle = par.get_current_solution()[:] # gets the current solution of the particle
        cost_cur_solution = self.get_fitness(solution_particle) # get the cost of current solution

        # Calac (pbest - pos) and (gbest - pos)
        vel_pbest = self.c1 * random.random() * (solution_pbest - solution_particle)
        vel_gbest = self.c2 * random.random() * (solution_gbest - solution_particle)

        # Genrate particle's velocity and position
        new_vel = self.w * par.get_velocity() + (vel_pbest + vel_gbest)
        new_pos = solution_particle + new_vel

        for pos in new_pos:
            if pos[0] > xlim or pos[0] < 0:
                pos[0] =  xlim * rng.random()
            
            if pos[1] > ylim or pos[1] < 0:
                pos[1] = ylim * rng.random()

            if pos[6] < 1:
                pos[6] = 1

            if pos[7] > 1:
                pos[7] = 1
            elif pos[7] < 0:
                pos[7] = 0.01

        # Update  velocity and position
        par.set_velocity(new_vel)
        par.set_current_solution(new_pos)

        # checks if current solution is pbest solution
        if cost_cur_solution < par.get_cost_pbest():
            par.set_pbest(solution_particle)
            par.set_cost_pbest(cost_cur_solution)

    def run(self):
        for iter in range(self.iterations):
            # updates gbest (best particle of the population)
            self.gbest = min(self.particles, key=attrgetter('pbest_solution_fit'))
            self.gbest_record.append(self.gbest.get_cost_pbest())
            print("gbest is :{} at {} iter".format(self.gbest.get_cost_pbest(), iter))
            name = 'gbest_imgs/gbest_' + str(iter)
            draw(image, matrix_to_camo(self.get_gbest()), name)

            for par in self.particles:
                self._update_particle(par)

    def get_gbest(self):
        return self.gbest.get_pbest()
            

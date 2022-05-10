# PSO class

class Particle: 
    
    def __init__(self, solution, fitness):
        self.solution = solution
        self.pbest = solution

        self.current_solution_fit = fitness
        self.pbest_solution_fit = fitness
    
        self.velocity = []
    

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
        iterations,
        pop_size, 
        num_dim, 
        w, 
        c1, 
        c2
        ):
        """
        param iterations : max iterations to convergence
        param pop_size   : population size
        param num_dim    : dimension of the given task
        param w          : inertia weight
        param c1         : cognitive learning factor for pbest (local best position)
        param c2         : cognitive learning factor for gbest (global best position)
        """

        self.iterations = iterations
        self.pop_size = pop_size
        self.num_dim = num_dim
        self.w = w
        self.c1 = c1
        self.c2 = c2

        self.init_swarm()

    def init_swarm(self):
        pass

    def get_fitness(self):
        pass

    def set_gbest(self, new_gbest):
        self.gbest = new_gbest

    def run(self):
        pass

    def get_gbest(self):
        return self.gbest
    
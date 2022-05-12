from groupcost import *
from internalcost import *

# Base Class to take in a clew of worms and return a cost value

class CostFunction:
    # Static Class Variables to represent Weight Parameters for:
    w_i = 1 # Internal knowledge
    w_g = 1 # Group knowledge
    w_e = 1 # External knowledge

    # Extra Static Variables ...
    max_possible_width = 720

    def __init__(self, clew):
        self.clew = clew
        self._worm = None

    @staticmethod
    def get_particle_cost(clew):
        cost_obj = CostFunction(clew)
        particle_cost = 0
        for worm in clew:
            particle_cost += cost_obj.get_cost_worm_total(worm)
        return particle_cost

    def get_cost_worm_total(self, worm):
        self._worm = worm

        # Normalise the cost ?
        internal_cost = CostFunction.w_i * self.get_internal_knowledge_cost()

        # group_cost = CostFunction.w_g * self.get_group_knowledge_cost()
        # external_cost = CostFunction.w_e * self.get_external_knowledge_cost()

        group_cost = 0
        external_cost = 0
        worm_cost = internal_cost + group_cost + external_cost
        return worm_cost

    def get_internal_knowledge_cost(self):
        
        # Better representation in case we need to normalize component values of each knowledge

        component_1_cost = width_cost(self._worm, CostFunction.max_possible_width)

        components_cost_arr = [component_1_cost]

        return sum(components_cost_arr)

    def get_group_knowledge_cost(self):

        # needs to modularized
        def intersect(a1, a2, b1, b2):
            area = lambda p1, p2, p3 : (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
            v1 = area(a1, a2, b1)/1000
            v2 = area(a1, a2, b2)/1000
            return v1 * v2

        min_cost = 10000
        for worm2 in self.clew:
            if self._worm == worm2: continue
            points1 = self._worm.control_points()
            points2 = worm2.control_points()

            for i in range(len(points1)-1):
                cost1 = intersect(points1[i], points1[i+1], points2[i], points2[i+1])
                cost2 = intersect(points2[i], points2[i+1], points1[i], points1[i+1])
                cost = max([cost1, cost2])
                if cost < min_cost:
                    min_cost = cost
        if min_cost > 0:
            return 0
        else:
            return 1

    def get_external_knowledge_cost(self):
        #TODO
        return -1

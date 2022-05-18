from groupcost import *
from internalcost import *
from externalcost import *

# Base Class to take in a clew of worms and return a cost value

class CostFunction:
    # Static Class Variables to represent Weight Parameters for:
    w_i = 0.1 # Internal knowledge
    w_g = 0.1 # Group knowledge
    w_e = 0.8 # External knowledge

    def __init__(self, clew, image):
        self.clew = clew
        self._worm = None
        self.image = image

    @staticmethod
    def get_particle_cost(clew, image):
        cost_obj = CostFunction(clew, image)
        particle_cost = cost_obj.get_cost_clew()
        return particle_cost

    def get_cost_clew(self):
        internal_cost = CostFunction.w_i * self.get_internal_knowledge_cost()
        group_cost = CostFunction.w_g * self.get_group_knowledge_cost()
        external_cost = CostFunction.w_e * self.get_external_knowledge_cost()

        print('Internal Cost:', internal_cost)
        print('Group Cost:', group_cost)
        print('External Cost:', external_cost)

        clew_cost = internal_cost + group_cost + external_cost
        return clew_cost

    def get_internal_knowledge_cost(self):
        component_1_cost = approximate_clew_displacement(self.clew, 720*240) #720*240 is image area
        component_2_cost = straightness_cost(self.clew)

        return sum([
            0.7 * straightness_cost(self.clew),
            0.2 * length_cost(self.clew, 720),
            0.1 * width_cost(self.clew),
        ])

    def get_group_knowledge_cost(self):
        component_1_cost = worm_segments_intersect(self.clew)

        return sum([
            distance_cost(self.clew)
        ])

    def get_external_knowledge_cost(self):
        component_1_cost = colour_cost(self.clew, self.image)
        return sum([component_1_cost])

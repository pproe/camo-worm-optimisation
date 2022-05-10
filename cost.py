# Base Class to take in a clew of worms and return a cost value

class CostFunction:
    # Static Class Variables to represent Weight Parameters for:
    w_i = -1 # Internal knowledge
    w_g = -1 # Group knowledge
    w_e = -1 # External knowledge

    def __init__(self, clew):
        self.clew = clew
        self._worm = None

    @staticmethod
    def get_particle_cost(clew):
        cost_obj = CostFunction(clew)
        total_cost = 0
        for worm in clew:
            total_cost += cost_obj.get_cost_worm_total(worm)
        return total_cost

    def get_cost_worm_total(self, worm):
        self._worm = worm

        # Normalise the cost ?
        internal_cost = CostFunction.w_i * self.get_internal_knowledge_cost()
        group_cost = CostFunction.w_g * self.get_group_knowledge_cost()
        external_cost = CostFunction.w_e * self.get_external_knowledge_cost()
        total_cost = internal_cost + group_cost + external_cost
        return total_cost

    def get_internal_knowledge_cost(self):
        #TODO
        return -1

    def get_group_knowledge_cost(self):
        #TODO
        return -1

    def get_external_knowledge_cost(self):
        #TODO
        return -1



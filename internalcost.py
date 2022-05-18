import math
import numpy as np

def approximate_worm_area(worm):
    worm_area = worm.width * worm.approx_length() + math.pi * ((worm.width/2) ** 2)
    return worm_area

# This function returns a cost of 0 when the summation of all areas of worms in a clew equal to the size of the image (img_total_area).
# When PSO optimises this cost, the worms will converge to fill the space of the image. It may be innaccurate due to approximation however.
def approximate_clew_displacement(clew, img_total_area):
    opt_area = img_total_area / len(clew)
    cost = 0
    for worm in clew:
        cost += opt_area - approximate_worm_area(worm)
    return abs(cost)

def straightness_cost(clew):
    costs = []
    for worm in clew:
        p = worm.control_points()
        d = np.cross(p[2]-p[0], p[1]-p[0]) / np.linalg.norm(p[2]-p[0])
        costs += [d / worm.approx_length()]
    return np.average(costs, weights=(costs >= np.mean(costs)))

def length_cost(clew, max):
    costs = []
    for worm in clew:
        costs += [1 - worm.approx_length()/max]
    return np.average(costs, weights=(costs >= np.mean(costs)))

def width_cost(clew):
    costs = []
    for worm in clew:
        # magic number for optimal width, we can decide later
        val = 1 - worm.width/20
        if val < 0: val = 0
        costs += [val]
    return np.average(costs, weights=(costs >= np.mean(costs)))
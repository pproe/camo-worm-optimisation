from itertools import combinations, product
import numpy as np
from util import weighted_average

def intersect(a1, a2, b1, b2):
    area = lambda p1, p2, p3 : (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
    v1 = area(a1, a2, b1)/1000
    v2 = area(a1, a2, b2)/1000
    return v1 * v2

def worm_segments_intersect(clew):
    costs = []
    for worm in clew:
        min_cost = 10000
        for worm2 in clew:
            if worm == worm2: continue
            points1 = worm.control_points()
            points2 = worm2.control_points()

            for i in range(len(points1)-1):
                cost1 = intersect(points1[i], points1[i+1], points2[i], points2[i+1])
                cost2 = intersect(points2[i], points2[i+1], points1[i], points1[i+1])
                cost = max([cost1, cost2])
                if cost < min_cost:
                    min_cost = cost
        if min_cost > 0:
            costs.append(0)
        else:
            costs.append(1)
    return sum(costs)

def distance_cost(clew):
    costs = []
    for worm1, worm2 in combinations(clew, 2):
        p1 = worm1.control_points()
        p2 = worm2.control_points()

        avg_1 = [0,0]
        avg_2 = [0,0]
        avg_1[0] = (p1[0][0] + p1[-1][0])/2 
        avg_1[1] = (p1[0][1] + p1[-1][1])/2 
        avg_2[0] = (p2[0][0] + p2[-1][0])/2 
        avg_2[1] = (p2[0][1] + p2[-1][1])/2 
        dist = (avg_2[0] - avg_1[0])**2 + (avg_2[1] - avg_2[1])**2
        if dist**0.5 > 150:
            costs += [0]
            continue
        

        p_all = list(product(p1, p2))
        dist = [np.linalg.norm(d[1]-d[0]) for d in p_all]
        cost = 1 - np.min(dist)/200
        if cost < 0: cost = 0
        costs += [cost]
    return weighted_average(costs)
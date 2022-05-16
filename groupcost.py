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
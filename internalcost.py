import math

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

def line_from_points(p1, p2):
    m = (p1[1] - p2[1])/(p1[0] - p2[0])
    C = p2[1] - m*p2[0]
    return (m, 1, C)

def straightness_cost(clew):
    total = 0
    for worm in clew:
        points = worm.control_points()
        print(points)
        A, B, C = line_from_points(points[0], points[2])
        d = abs(A*points[1][0] + B*points[1][1] + C) / (A**2+B**2)**0.5
        dist = (points[2][0] - points[0][0])**2 + (points[2][1] - points[0][1])**2
        total += d / dist**0.5
    return total
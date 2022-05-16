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

def straightness_cost(clew):
    #TODO
    return -1
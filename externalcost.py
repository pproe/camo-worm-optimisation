import numpy as np
# Function compares the colour of the worm's region in the area vs the worm's colour and returns absolute difference
def camo_difference(clew, image):
    total_cost = 0
    for worm in clew:
        worm_length = round(worm.approx_length())
        _wl = worm_length
        # print(worm_length)
        region_colour_total = 0
        for discrete_unit in range(worm_length):
            colour_at_point = int(worm.colour_at_t(discrete_unit / worm_length, image))
            if colour_at_point == -1:
                _wl -= 1
            else:
                region_colour_total += colour_at_point
        total_cost += abs(region_colour_total - (_wl * worm.colour))
    return total_cost


def colour_cost(clew, image):
    costs = []
    for worm in clew:
        l = int(worm.approx_length())
        w = int(worm.width)
        colours = [worm.colour_at_t_square(t, w, image) for t in np.linspace(0,1,l)]
        avg_colours = [np.average(c) for c in colours if c.size != 0]
        sum_colours = [abs(c-worm.colour) for c in avg_colours if c != -1]
        costs += [np.average(sum_colours)]
    return np.average(costs, weights=(costs > np.mean(costs)))
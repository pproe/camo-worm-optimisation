import numpy as np
# Function compares the colour of the worm's region in the area vs the worm's colour and returns absolute difference
def camo_difference(clew, image):
    total_cost = 0
    for worm in clew:
        worm_length = round(worm.approx_length())
        _pixels_counted = 0
        region_colour_total = 0
        for discrete_unit in range(worm_length):
            worm_point =  worm.bezier.point_at_t(discrete_unit / worm_length)
            circ_mask = create_circular_mask(image.shape[0], image.shape[1], center=(worm_point[0], worm_point[1]), radius=worm.width)
            region_colour_total += sum(image[circ_mask])
            _pixels_counted += circ_mask.sum()
        total_cost += abs(region_colour_total - (_pixels_counted * worm.colour))
    return total_cost

# Function to create a boolean array of circle given coordinates center, and h,w of image. 
def create_circular_mask(h, w, center=None, radius=None):
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])
    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask


def colour_cost(clew, image):
    costs = []
    for worm in clew:
        l = int(worm.approx_length())
        w = int(worm.width)
        colours = [worm.colour_at_t_square(t, w, image) for t in np.linspace(0,1,l)]
        avg_colours = [np.average(c) for c in colours if c.size != 0]
        sum_colours = [abs(c-worm.colour) for c in avg_colours if c != -1]
        costs += [np.average(sum_colours)]
    return np.average(costs, weights=(costs >= np.mean(costs)))
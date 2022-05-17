
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

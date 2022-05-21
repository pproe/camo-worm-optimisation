from pso import PSO, get_image
from util import  matrix_to_camo , draw


image = get_image()
x = PSO(
    worm_size = 15, 
    iterations = 15, 
    c1 = 2, 
    c2 = 2, 
    pop_size = 30, 
    w = 1
    )
# init_gbest = matrix_to_camo(x.get_init_gbest())

x.run()
# gbest_clew = matrix_to_camo(x.get_gbest())

# draw(image, init_gbest , 'init_gbest')
# draw(image, gbest_clew, 'gbest')

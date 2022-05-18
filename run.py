from pso import PSO, get_image
from util import Camo_Worm, Drawing, matrix_to_camo   

def draw(image, clew, save_name):
    drawing = Drawing(image)
    drawing.add_worms(clew)
    drawing.show(save=save_name)

image = get_image()
x = PSO(iterations = 5)
init_gbest = matrix_to_camo(x.get_init_gbest())

x.run()
gbest_clew = matrix_to_camo(x.get_gbest())

draw(image, init_gbest , 'init_gbest')
draw(image, gbest_clew, 'gbest')

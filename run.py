import imp
from pso import PSO
from util import Camo_Worm
from util import Drawing    

x = PSO()
x.run()
gbest = x.get_gbest()

# Draw a single worm along with control points and some sample points
# self, x, y, r, theta, deviation_r, deviation_gamma, width, colour

# worm = Camo_Worm(200, 100, 50, np.pi/6, 70, np.pi/3, 10, 0.8)
# drawing = Drawing(image)
# drawing.add_worms(worm)
# drawing.add_dots(worm.intermediate_points(8), radius=2, color='green')
# drawing.add_dots(worm.control_points(),color='orange')
# drawing.add_dots((200,100), color='blue')

# drawing.show(save='bezier.png')
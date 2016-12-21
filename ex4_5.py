'''
draw fermat's spiral
ideas from Downey's original code.

'''
try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *


def draw_spiral(t, n, length, a, b):

    theta = 0.0

    for i in range(n):
        fd(t, length)
        dtheta = 1 / (a + b * theta)

        rt(t, dtheta)
        theta += dtheta
		
def draw_spiral_n(t, n, length, a, b):

    theta = 0.0

    for i in range(n):
        bk(t, length) #inverse move
        dtheta = 1 / (a + b * theta)

        rt(t, dtheta)
		
        theta += dtheta		


import math
# create the world and bob
world = TurtleWorld()
bob = Turtle()
bob2 = Turtle()
bob.delay = 0
bob2.delay = 0
draw_spiral(bob, n=1000, length=3, a=0.01, b=0.0002)
draw_spiral_n(bob2, n=1000, length=3, a=0.01, b=0.0002)


bob.die()
bob2.die()

wait_for_user()
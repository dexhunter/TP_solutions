from swampy.TurtleWorld import *
from polygon import *

def flower(turtle, petals, radius, angle):
    for i in range(petals):
        petal(t, radius, angle)
        lt(t, 360.0/petals)


def petal(turtle, radius, angle):
    for i in range(2):
        arc(turtle, radius, angle)
        lt(turtle, 180-angle)


world = TurtleWorld()
t = Turtle()
t.delay = 0.01

petals = 5
arc_radius = 120
angle = 60

flower(t, petals, arc_radius, angle)

die(t)
wait_for_user()

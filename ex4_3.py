def isosceles(t, l, theta):
	# t : turtle
	# l: length of legs
	# theta: inner angle 
	
	b = 2 * l * math.sin(((theta/2)/180) * math.pi) #base length
	
	t.fd(l)
	t.rt(90+theta/2)
	t.fd(b)
	t.rt(90+theta/2)
	t.fd(l)
	t.lt(180)
	


def pie(t, n, l):
	# t : turtle
	# n : the amount of pieces of pie
	# l : the length of leg
	
	theta = 360.0 / n # inner angle
	for i in range(n):
		isosceles(t, l, theta)
		
		
from swampy.TurtleWorld import *
import math
		
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

pie(bob, 5, 30)
bob.pu()
bob.fd(120)
bob.pd()

pie(bob, 6, 30)
bob.pu()
bob.fd(120)
bob.pd()

pie(bob, 7, 30)
bob.pu()
bob.fd(120)
bob.pd()

pie(bob, 8, 30)
bob.pu()
bob.fd(120)
bob.pd()

bob.die()
wait_for_user()
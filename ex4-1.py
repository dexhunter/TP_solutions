	def square1(t):
	for i in range(4):
		fd(t, 100)
		lt(t)

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)
		
'''def polygon(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)
//orginal version from book Think Python		'''
		
'''def circle(t, r):
	for i in range(100):
		fd(t, 0.628 * r)  
		lt(t, 3.6)
	// my original version, it succeeds 
		'''
		
'''def arc(t, r, angle):
	for i in range(angle):
		fd(t, angle*3.14*r/180)
		lt(t, 360/angle)
// my original version, it fails
'''
	
'''def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1 
	step_length = arc_length / n
	step_angle = float(angle) / n
	
	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle) 
// The first version from BOOK Think Python
		'''

def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)
		
		
def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)


def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)
	
def circle(t, r,):
	arc(t, r, 360)
	
	
		
from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01

'''arc(bob, 100, 90)'''
circle(bob, 50)
bob.die()
wait_for_user()
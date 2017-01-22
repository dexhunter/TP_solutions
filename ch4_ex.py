#!/usr/bin/env python2

def square(t):
	for i in range(4):
		t.fd(100)
		t.lt(90) # move a right angle to the left  
		
def square_modified(t,length):
	for i in range(4):
		t.fd(length) #custom length
		t.lt(90) # move a right angle to the left  
		
def polygon(t,length, n):
	move_angle = 360.0 / n #!!!make angle to float
	for i in range(n):
		t.fd(length) #custom length
		t.lt(move_angle) # move a right angle to the left  
		
def circle(t, r):
	#figure out the circumference of the circle and make sure that length * n = circumference
	n = 20
	circumference = 2 * math.pi * r
	length = circumference  / n
	polygon(t, length, n)
	
def arc(t, r, angle):
	n = 10
	circumference = 2 * math.pi * r
	length = circumference / n
	arc_angle = (float) (angle / n)
	for i in range(n + 1): # + 1 to draw the closing after turning angle
		t.fd(length)
		t.lt(arc_angle)
	


import math
from swampy.TurtleWorld import *

if __name__ == '__main__':
	world = TurtleWorld()
	bob = Turtle()
	print bob
	bob.delay = 0.001
	#circle(bob,  20)
	#polygon(bob, 1, 200)
	arc(bob, 10, 180)
	bob.die()
	wait_for_user()
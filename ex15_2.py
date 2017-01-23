#!/usr/bin/env python2

class Rectangle:
	'''Represents a rectangle
	
	Attributes: width, height, corner.
	'''
	
class Point:
	'''Represents a point in 2-D space.'''
	
class Circle:
	'''Represents a circle.
	
	Attributes: center, radius
	'''

import math
# for turtle reference, see: https://docs.python.org/2/library/turtle.html#turtle.setheading
import turtle
from ex15_1 import *

def draw_rect(t, rect):
	t.pu()
	t.setx(rect.corner.x) # set x cordinate
	t.sety(rect.corner.y) # set y cordinate
	print(t.position())

	t.seth(0) # set heading to east
	t.pd() # put pen down
	t.fd(rect.width)
	print(t.position())

	t.seth(90)
	t.fd(rect.height)
	print(t.position())
	t.seth(180)
	t.fd(rect.width)
	print(t.position())
	t.seth(270)
	t.fd(rect.height)
	
	
	
def draw_circle(t, crc):
	# given center find a point on circle
	t.pu()
	t.setx(crc.center.x)
	t.sety(crc.center.y)
	t.fd(crc.radius)
	print(t.position())
	t.lt(90)
	t.pd()
	t.circle(crc.radius)

	
if __name__ == '__main__':
	bob = turtle.Turtle()

	bob.delay = 0.001


	
	rect = Rectangle()
	rect.height = 100.0
	rect.width = 200.0
	rect.corner = Point()
	rect.corner.x = 50.0
	rect.corner.y = 80.0
	

	# draw a circle
	crc = Circle()
	crc.center = Point()
	crc.center.x = 150.0
	crc.center.y = 10.0
	crc.radius = 75.0
	
	draw_rect(bob, rect)
	draw_circle(bob, crc)
	print("are there any overlap")
	print(rect_circle_overlap(crc, rect))
	
	# wait for the user to close the window
	turtle.mainloop()
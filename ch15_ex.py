class Point:
	'''Represents a point in 2-D space.'''
	

	
class Rectangle:
	'''Represents a rectangle
	
	attributes: width, height, corner.
	'''
def find_center(rect):
		p = Point()
		p.x = rect.corner.x + rect.width/2
		p.y = rect.corner.y + rect.height/2
		return p
	
def print_point(p):
	print(  '(%g, %g)' % (p.x, p.y)  )
	
def distance_between_points(p1, p2):
	distance = math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 )
	return distance
	
def move_rectangle(rect, dx, dy):
	'''Creates and returns a new rectangle
	
	'''
	rect_new = copy.deepcopy(rect) #not only copy the object but also the references it contains
	rect_new.corner.x += dx
	rect_new.corner.y += dy
	
import copy
import math
if __name__ == '__main__':
	blank = Point()
	blank.x = 3.0
	blank.y = 4.0
	b = Point()
	b.x = 0.0
	b.y =0.0
	print (distance_between_points(blank, b))
	print_point(blank)
	bob = Rectangle()
	bob.width = 100.0
	bob.height = 200.0
	bob.corner = Point()
	bob.corner.x = 0.0
	bob.corner.y = 0.0
	
	center = find_center(bob)
	print_point(center)
	move_rectangle(bob, 50, 50)
	print_point(find_center(bob))
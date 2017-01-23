class Point:
	'''Represents a point in 2-D space.'''
def print_point(p):
		print(  '(%g, %g)' % (p.x, p.y)  )
		
def distance_between_points(p1, p2):
		distance = math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 )
		return distance

class Rectangle:
	'''Represents a rectangle
	
	Attributes: width, height, corner.
	'''
	
def find_center(rect):
		p = Point()
		p.x = rect.corner.x + rect.width/2
		p.y = rect.corner.y + rect.height/2
		return p
	
def move_rectangle(rect, dx, dy):
		'''Creates and returns a new rectangle
		
		'''
		rect_new = copy.deepcopy(rect) #not only copy the object but also the references it contains
		rect_new.corner.x += dx
		rect_new.corner.y += dy

class Circle:
	'''Represents a circle.
	
	Attributes: center, radius
	'''
	
def point_in_circle(crc, pt):
		d = distance_between_points(crc.center, pt)
		print(d)
		return d <= crc.radius
	
def rect_in_circle(crc, rect):
		d = distance_between_points(crc.center, rect.corner)
		return d <= crc.radius
		
def rect_circle_overlap(crc, rect):
#reference: http://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
	rect_center = find_center(rect)
	d_center = Point()
	d_center.x = abs(rect_center.x - crc.center.x)
	d_center.y = abs(rect_center.y - crc.center.y)
	
	if(d_center.x > (rect.width/2 + crc.radius)):
		return False
	if(d_center.y > (rect.height/2 + crc.radius)):
		return False
	if(d_center.x <= (rect.width/2)):
		return True
	if(d_center.y <= (rect.height/2)):
		return True
	#check whether the corner of rectangle is inside the circle
	cornerDistance_sq = (d_center.x - rect.width/2) **2 + (d_center.y - rect.height/2) **2 
	
	return cornerDistance_sq <= (crc.radius ** 2)
	
	
import math	
import copy
if __name__ == '__main__':


	bob = Rectangle()
	bob.width = 100.0
	bob.height = 200.0
	bob.corner = Point()
	bob.corner.x = 50.0
	bob.corner.y = 50.0

	print_point(find_center(bob))
	crc = Circle()
	crc.center = Point()
	crc.center.x = 150.0
	crc.center.y = 100.0
	crc.radius = 75.0
	print(point_in_circle(crc, bob.corner))
	print(rect_in_circle(crc, bob))
	print(rect_circle_overlap(crc,bob))
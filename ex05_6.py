def koch(t, l):
	# t: turtle
	# l: length
	if l < 3:
		t.fd(l)
	else:
		koch(t,l/3)
		t.lt(60)
		koch(t,l/3)
		t.rt(120)
		koch(t,l/3)
		t.lt(60)
		koch(t,l/3)
	
#inner angle summation is 360 degrees
def snowflake(t, l):
		koch(t, l)
		t.rt(120)
		koch(t,l)
		t.rt(120)  
		koch(t,l)


from swampy.TurtleWorld import *
import math

if __name__ == '__main__':
	world = TurtleWorld()    
	bob = Turtle()
	bob.delay = 0
	#koch(bob, 550) #the same as figure 5-2 shows
	snowflake(bob, 300)
	bob.die()
	wait_for_user()
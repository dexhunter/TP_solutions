def draw(t, length, n):
	if n == 0:
		return
	angle = 50 # initialize angle
	t.fd(length * n)
	t.lt(angle)
	draw(t, length, n-1)  #recursive call
	t.rt(2*angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length*n)
	
# if product of n and length is big it will draw something like a spiral but not circular
# and when product reduces, it draws something like a snowflake
	
from swampy.TurtleWorld import *
import math

if __name__ == '__main__':
	world = TurtleWorld()    
	bob = Turtle()
	bob.delay = 0.001
	draw(bob, 3, 30)
	wait_for_user()
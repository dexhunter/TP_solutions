#first: draw a stack diagram 
'''
set r = 5
set t = Bob
__main__

<module>

polygon_n length= 1.571 move_angle = 18 n = 0
polygon_n length= 1.571 move_angle = 18 n = 1  
polygon_n length= 1.571 move_angle = 18 n = 2  
polygon_n length= 1.571 move_angle = 18 n = 3  
polygon_n length= 1.571 move_angle = 18 n = 4  
polygon_n length= 1.571 move_angle = 18 n = 5  
polygon_n length= 1.571 move_angle = 18 n = 6  
polygon_n length= 1.571 move_angle = 18 n = 7  
polygon_n length= 1.571 move_angle = 18 n = 8  
polygon_n length= 1.571 move_angle = 18 n = 9  
polygon_n length= 1.571 move_angle = 18 n = 10  
polygon_n length= 1.571 move_angle = 18 n = 11
polygon_n length= 1.571 move_angle = 18 n = 12  
polygon_n length= 1.571 move_angle = 18 n = 13  
polygon_n length= 1.571 move_angle = 18 n = 14 
polygon_n length= 1.571 move_angle = 18 n = 15 
polygon_n length= 1.571 move_angle = 18 n = 16 
polygon_n length= 1.571 move_angle = 18 n = 17 
polygon_n length= 1.571 move_angle = 18 n = 18 
polygon_n length= 1.571 move_angle = 18 n = 19 
polygon_n length= 1.571 move_angle = 18 n = 20  
  


'''

#second: Totally make sense

'''


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

'''
class Time:
	'''Represents the time of day.
	
	attributes: hour, minute, second
	'''
	
def print_time(t):
	print ('(%.2d:%.2d:%.2d)' % (t.hour, t.minute, t.second))
	
def is_after(t1, t2):
	return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
	
def mul_time(t, n):
	'''Multiple time t by n
	
	n: int
	
	Returns a time tr
	'''
	return int_to_time(time_to_int(t) * n)

def add_time(t1, t2):
	sum = Time()
	sum.hour = t1.hour + t2.hour
	sum.minute = t1.minute + t2.minute
	sum.second = t1.second + t2.second
	
	while sum.second >= 60:
		sum.second -= 60
		sum.minute += 1
		
	while sum.minute >= 60:
		sum.minute -= 60
		sum.hour += 1
	
	return sum
	
def increment(t, sec):
	'''Writes a inc function does not contain any loops
	#for the second exercise of writing a pure function, I think you can just create a new object by copy.deepcopy(t) and modify the new object. I think it is quite simple so I will skip this one, if you differ please contact me and I will try to help
	
	idea: using divmod
	sec: seconds in IS
	'''
	t.second += sec
	inc_min, t.second = div(t.seconds, 60)
	t.minute += inc_min
	inc_hour, t.minute = div(t.minute, 60)
	t.hour += inc_hour
	return t

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
	
if __name__ == '__main__':
	t = Time()
	t.hour = 17
	t.minute = 43
	t.second = 6
	print_time(mul_time(t, 3))
	
	t2 = Time()
	t2.hour = 17
	t2.minute = 44
	t2.second = 5
	print_time(t)
	
	start = Time()
	start.hour = 9
	start.minute =45
	start.second = 0
	
	duration = Time()
	duration.hour = 1
	duration.minute = 35
	duration.second = 0
	
	done = add_time(start, duration)
	print_time(done)
	
	print( is_after(t, t2) )
	
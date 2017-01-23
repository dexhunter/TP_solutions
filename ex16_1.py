from ch16_ex import *

def mul_time(t, n):
	''' the same as in ch16_ex '''
	return int_to_time(time_to_int(t) * n)
	
def average_pace(t, delta_x):
	''' Represents average pace in a race
	t: finishing time
	delta_x: movement during race
	unit : time per mile '''
	return int_to_time(time_to_int(t) / delta_x )
	


if __name__ == '__main__':
	t = Time()
	t.hour = 3
	t.minute = 30
	t.second = 30
	print_time(mul_time(t, 3))
	print_time(average_pace(t,30))
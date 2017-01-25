class Time:
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
		
	def print_time(self):
		print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
	
	def int_to_time(seconds):
		minutes, self.second = divmod(seconds, 60)
		self.hour, self.minute = divmod(minutes, 60)
		return self
		
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds
		
	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)
		
		
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def __str__(self):
		return '(%d,%d)' % (self.x, self.y)
		
if __name__ == '__main__':
	start = Time()
	start.hour = 9
	start.minute = 45
	start.second = 00
	start.print_time()
	time = Time(9, 45, 1)
	print(time)
	d = Point(3,4)
	print(d)
	#print( int_to_time(500) )
	end = start.increment(1337)
	end.print_time
class Time:
	def __init__(self, hour=0, minute=0, second=0):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
		
	def __add__(self, other):
		''' change the behavior of + operator, aka operator overloading'''
		#type-based dispatch
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(seconds)
			
	def __radd__(self, other):
		'''right-side addition
		make addition commutative '''
		return self.__add__(other)
			
	def add_time(self, other):
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)
		
	def print_time(self):
		print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
		
	def time_to_int(self):
		minutes = self.hour * 60 + self.minute
		seconds = minutes * 60 + self.second
		return seconds
		
	def increment(self, seconds):
		seconds += self.time_to_int()
		return int_to_time(seconds)
	
	def is_after(self, other):
		return self.time_to_int() > other.time_to_int()
		
		
def int_to_time(seconds):
	'''No need to rewrite it as a method since there is no object to invoke
	
	'''
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)
	return time	
	
class Point:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		
	def __str__(self):
		return '(%d,%d)' % (self.x, self.y)
		
	def __add__(self, other):
		if isinstance(other, Point):
			return self.add_point(other)
		else: #if second operand is a tuple
			return self.add_tuple(other)
		
	def add_point(self, other):
		vector = Point()
		vector.x = self.x + other.x
		vector.y = self.y + other.y
		return vector
		
	def add_tuple(self, other):
		if isinstance(other, tuple):
			self.x += other[0]
			self.y += other[1]
			return self
		else:
			print("Input format is wrong, return given Point")
			return self
			
	def __radd__(self, other):
		return self.__add__(other)
		
if __name__ == '__main__':
	start = Time()
	start.hour = 9
	start.minute = 45
	start.second = 00
	start.print_time()
	time = Time(9, 45, 1)
	print(time)
	print(time.is_after(start))
	d1 = Point(3,4)
	print(d1)
	d2 = Point(5,12)
	print(d2)
	print(d1+d2)
	print(d1+(5,12))
	d1 = Point(3,4) #__add__ is a modifier function
	print((5,12)+d1)
	print(d1)
	print(d1)
	#print( int_to_time(500) )
	end = start.increment(1337)
	end.print_time()
	print(start + end)
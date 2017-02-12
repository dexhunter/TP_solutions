'''following code are adapted from http://greenteapress.com/thinkpython2/code/Time2.py'''
from __future__ import print_function, division

class Time:
	'''Change the attributes of Time to be a single integer representing seconds since midnight
	
	attributes: seconds
	'''
	
	def __init__(self, hour=0, minute=0, second=0):
		minutes = hour * 60 + minute
		self.seconds = minutes * 60 + second

	def __str__(self):
		minutes, second = divmod(self.seconds, 60)
		hour, minute = divmod(minutes, 60)
		return '%.2d:%.2d:%.2d' % (hour, minute, second)
		
	def __lt__(self, other):
		t1 = self.seconds
		t2 = other.seconds
		return t1 < t2

	def print_time(self):
		"""Prints a string representation of the time."""
		print(str(self))
		
	def time_to_int(self):
		"""Computes the number of seconds since midnight."""
		return self.seconds

	def is_after(self, other):
		"""Returns True if t1 is after t2; false otherwise."""
		return self.time_to_int() > other.time_to_int()

	def __add__(self, other):
		"""Adds two Time objects or a Time object and a number.

		other: Time object or number of seconds
		"""
		if isinstance(other, Time):
			return self.add_time(other)
		else:
			return self.increment(other)

	def __radd__(self, other):
		"""Adds two Time objects or a Time object and a number."""
		return self.__add__(other)

	def add_time(self, other):
		"""Adds two time objects."""
		assert self.is_valid() and other.is_valid()
		seconds = self.time_to_int() + other.time_to_int()
		return int_to_time(seconds)

	def increment(self, seconds):
		"""Returns a new Time that is the sum of this time and seconds."""
		seconds += self.time_to_int()
		return int_to_time(seconds)

	def is_valid(self):
		minutes, second = divmod(self.seconds, 60)
		hour, minute = divmod(minutes, 60)
		if hour < 0 or minute < 0 or second < 0:
			return False
		if minute >= 60 or second >= 60:
			return False
		return True

def int_to_time(seconds):
	return Time(0,0,seconds)

'''belowing code not changed'''
def main():
	start = Time(9, 45, 00)
	start.print_time()

	end = start.increment(1337)
	#end = start.increment(1337, 460)
	end.print_time()

	print('Is end after start?')
	print(end.is_after(start))

	print('Using __str__')
	print(start, end)

	start = Time(9, 45)
	duration = Time(1, 35)
	print(start + duration)
	print(start + 1337)
	print(1337 + start)

	print('Example of polymorphism')
	t1 = Time(7, 43)
	t2 = Time(7, 41)
	t3 = Time(7, 37)
	total = sum([t1, t2, t3])
	print(total)
	print(t1 < t2)
	print(t3 < t2)

if __name__ == '__main__':
	main()
import math


def estimate_pi():
	sum = 0
	epsilon = math.pow(10, -15)
	k = 0
	i = 1 #initialize i, the value doesn't matter
	while i > epsilon:
		i = (math.factorial(4*k) * (1103 + 26390 * k)) / (math.pow((math.factorial(k)), 4) * math.pow(396, 4*k) )
		sum += i
		k += 1 #!important
	inverse = 2 * math.sqrt(2) * sum / 9801
	return 1/inverse
	
print estimate_pi()
print math.pi
print estimate_pi() - math.pi
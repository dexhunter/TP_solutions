# using exclusive method as Wikipedia suggests

from __future__ import division
import math

def p_cal(n):
# probability calculator for n people (generalized)
	np_of_a = math.factorial(365) / math.factorial(365-n) / math.pow(365, n)
	return (1 - np_of_a)
	
print p_cal(23)
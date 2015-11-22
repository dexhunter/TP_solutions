import math

def factorial(i):
	if i == 0:
		return 1
	else:
		j = factorial(i-1)
		r = i * j
		return r
		

def estimate_pi():
		a = math.sqrt(2)
		q = 0
		p = 1103
		while p > 1e-15:
			q = p + q
			k = 1
			p = (factorial(4*k)*(1103 + 26390*k))/(((factorial(k))**(4)) * 396**(4*k))
			k = k + 1
		pi = 9801/(2*a*q)
		print q,"\t",p,"\t",pi,"\t",math.pi

estimate_pi()

//my code sucks XD
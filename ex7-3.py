import math

def square_root(a):
	x = 3.0
	epsilon = 0.00000001
	while True:
		y = (x + a/x) / 2.0
		if abs(y - x) < epsilon:
			break
		x = y
	return y

		
def test_square_root(i):
	while i <= 9.0:
		a = square_root(i)
		b = math.sqrt(i)
		c = abs(a-b)
		print i," ",a," ",b," ",c 
		print "\n"
		i = i + 1.0
		
		
test_square_root(1.0)
		
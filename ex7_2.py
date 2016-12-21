def square_root(a):
	x = 3.0
	epsilon = 0.0001
	while True:
		
		y = (x + a/x) / 2.0
		if abs(y - x) < epsilon:
			break
		x = y
		print x
			
square_root(12)

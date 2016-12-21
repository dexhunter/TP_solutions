def gcd(a, b):
	a = int(a)
	b = int(b)
	if a > b:
		c = a - b
		gcd(b, c)
	elif a < b:
		c = b - a
		gcd(a, c)
	else:
		print a
		
gcd(252, 105)
		

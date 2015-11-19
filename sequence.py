def sequence(n):
	while n != 1:
		print n,
		if n % 2 == 0:
			n = n/2
		else:
			n = n*3+1
			
sequence(22)
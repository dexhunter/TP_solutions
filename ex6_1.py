def b(z):
	prod = a(z, z) #calculate product of
	print (z, prod)
	return prod
	
def a(x, y):
	x = x + 1   #increment x 
	return x * y   
	
def c(x, y, z):
	total = x + y + z
	square = b(total) ** 2
	return square
	
x = 1
y = x + 1
print (c(x, y+3, x+ y))

'''
steps : c(1, 2 + 3, 1 + 2)
		total = 1 + 5 + 3 = 9
		square = b(9)
		inside b: prod = a(9, 9)
		inside a: x = 10 return 90
		back to b: print(9, 90) return 90
		back to c: square = 90 ^2 = 8100
		print 8100
'''
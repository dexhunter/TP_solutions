def is_triangle(a, b, c):
	if a + b > c and a + c > b and b + c > a:
		print "Yes"
	else:
		print "No"
		
is_triangle(3, 4, 5)

def is_triangle_custom():
	a = input("Please input a: ")
	b = input("Please input b: ")
	c = input("Please input c: ")
	return is_triangle(a, b, c)
	
is_triangle_custom()
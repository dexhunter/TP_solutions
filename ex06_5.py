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
		
#another version instruted from book
# I wonder how to prove it mathematically. Hmm...
# Update: This algorithm is based on Bezout's identity which states that let a and b be nonzero integers and let d be their greatest common divisor. Then there exist integers x and y such that ax + by = d, https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
def gcd_euclid(a,b):
	if (b == 0):
		return a
	else:
		return gcd_euclid(b, a%b)

		
print gcd_euclid(105, 252)
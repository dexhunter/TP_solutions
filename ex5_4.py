def recurse(n, s):
	if n == 0:
		print(s)
	else:
		print "n is: %d" % n
		print "s is: %d" % s
		recurse(n-1, n+s)
		
recurse(3, 0)
recurse(-1, 0) #Runtime error: maxmimum recursion depth exceeded
'''
input n (n>0) since n need to approach 0
'''
def binomial_coeff(n, k):
	'''Compute the binomial coefficient
	
	n: number of trials
	k: number of successes
	
	returns: int
	'''
	if k==0:
		return 1
	if n==0:
		return 0
		
	res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
	return res
	
	
def b(n,k):
	'''rewrite the function in a compact way
	I failed to rewrite in conditional expression. :/
	But this is the end of the course so meh. never mind
	'''

	memo = {}
	if (n,k) in memo:
		return memo[(n,k)]
	if k==0:
		return 1
	if n==0:
		return 0
	
	r = b(n-1, k) + b(n-1, k-1)
	memo[(n,k)] = r	
	return r
	
if __name__ == '__main__':
	a = binomial_coeff(3,4)
	# b(3,4) = b(2, 4) + b(2,3)
	# b(2,4) = b(1,4) + b(1,3)
	# b(1,4) = b(0,4) + b(0,3) = 0 + 0 = 0
	# b(1,3) = b(0,3) + b(0,2) = 0 + 0 = 0
	# b(2,3) = b(1,3) + b(1,2)
	# b(1,2) = b(0,2) + b(0,1) = 0 + 0 = 0
 	print(a)
	print(b(3,4))
	c = binomial_coeff(10,4)
	print(c)	
	print(b(10,4))
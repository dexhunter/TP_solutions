
def ack(m, n):
	A = {}
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	else:
		A[m, n] = ack(m-1, ack(m, n-1) )
		return A[m, n]
		
print ack(3,4)
print ack(3,6)
#print A
		
		
		
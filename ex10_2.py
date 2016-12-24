def cumsum(l):
	total = 0
	for i in range(len(l)):
		total += l[i]
		l[i] = total
	return l
	
t = [1, 2, 3]
print cumsum(t)
		
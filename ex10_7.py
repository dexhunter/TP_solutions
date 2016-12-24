def has_duplicate(l):
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			if l[i] == l[j]:
				return False
	return True
	
print has_duplicate([1,2,3,4,5])
print has_duplicate([1,2,3,4,5,5])
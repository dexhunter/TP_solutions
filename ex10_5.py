def is_sorted(l):
	if len(l) == 1:
		return True
	else:
		if(l[0] > l[1]):
			return False
		return is_sorted(l[1:])
		
print is_sorted([1,2,2])
print is_sorted(['b','a'])
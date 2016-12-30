def has_duplicate(l):
	d = {}
	for c in l:
		if c not in d:
			d[c] = 1
		else:
			return True
	return False
	
print has_duplicate([1,2,3,4,5])
print has_duplicate([1,2,3,4,5,5])


'''In author's answer, there is a better solution'''

def has_duplicate2(l):
	return len(set(l)) < len(l) # Sets are lists with no duplicate entries
	#http://stackoverflow.com/questions/3949310/how-is-set-implemented
print ''
print has_duplicate2([1,2,3,4,5])
print has_duplicate2([1,2,3,4,5,5])

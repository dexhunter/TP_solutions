def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		inverse.setdefault(val, []).append(key) # searched online to get this answer and it's same as the author's 
	return inverse
	
	
hist = histogram('parrot')
print hist
inverse = invert_dict(hist)
print inverse
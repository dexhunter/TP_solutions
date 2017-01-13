#version 2 for exercise 1 in chapter 12

def map_dict(s):
	'''
	Returns a dictionary mapping each letter with corresponding frequency
	
	s: string
	
	'''
	d = {}
	for i in s:
		d[i] = d.get(i, 0) + 1
	return d

def most_frequent(s):
	'''
	Sorts the letters in reverse order of frequence
	
	s: string
	
	Retruns a list of letters
	'''
	d = map_dict(s)
	
	l = []
	
	for x, f in d.items():
		l.append((f,x))
		
	l.sort(reverse = True)
	
	result = []
	
	for f, x in l:
		result.append(x)
		
	return result
	
	
	
if __name__ == '__main__':
	# emma.txt is provided from author's code
	with open('emma.txt', 'r') as fin:
		string = fin.read()
		print most_frequent(string)
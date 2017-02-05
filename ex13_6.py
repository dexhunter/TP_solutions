'''
Find a word in the book but not word list using set (data structure)
'''
import string
def read_file(filename):
	'''Reads a file and return stripped strings
	
	filename: str
	
	Returns a generator contains byte unicode?
	'''
	remove_chars = list(string.punctuation + string.whitespace)
	with open(filename, encoding="utf8") as fin:
		for line in fin:
			if not line.strip().startswith('#'):
				for word in line.split():
					yield word.translate({ord(x): '' for x in remove_chars}).lower().encode("utf-8")

def subtraction(s1, s2):
	'''
	in the s1 but not s2
	s1 - s2
	'''
	return s1 - s2
					
if __name__ == '__main__':
	s2 = set(read_file('words.txt'))
	s1 = set(read_file('PrideandPrejudice.txt'))
	print (subtraction(s1, s2))
	print(len(subtraction(s1,s2)))
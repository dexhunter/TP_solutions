'''
According to http://stackoverflow.com/questions/3900054/python-strip-multiple-characters,
 string.translate(string.maketrans()) is the fastest way to remove undesired chars
 
 maketrans syntax: str.maketrans(intab, outtab)
'''
import string

def read_file(filename):
	'''Reads a file and return stripped strings
	
	filename: a string
	'''
	remove_char = string.punctuation + string.whitespace
	with open(filename) as fin:
		for line in fin:
			yield line.translate(line.maketrans("", "", ), remove_char).lower()
			
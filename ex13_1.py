'''
I was first approach this problem by using translate function in python 2 according to:http://stackoverflow.com/questions/3900054/python-strip-multiple-characters

but soon I switched to python 3 and found that advantage of using translate vanished due to unicode feature in python 3 according to: http://stackoverflow.com/questions/1450897/python-removing-characters-except-digits-from-string

and my solution is based on one of answers in:
http://stackoverflow.com/questions/10017147/removing-a-list-of-characters-in-string
and I feel it is still quite fast
'''

import string

def read_file(filename):
	'''Reads a file and return stripped strings
	
	filename: str
	'''
	remove_chars = list(string.punctuation + string.whitespace)
	with open(filename, encoding="utf8") as fin:
		for line in fin:
			if not line.strip().startswith('#'):
				for word in line.split():
					yield word.translate({ord(x): '' for x in remove_chars}).lower().encode("utf-8")
				
if __name__ == '__main__':
	print(list(read_file('words.txt')))
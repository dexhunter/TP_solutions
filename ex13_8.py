import random
import string
import collections

def read_and_analyze(filename, skip_header=True):
	'''Read a text file and perform Markov analysis.

	structure: dict[prefix] = suffix
	
	Returns a markov dict
	'''
	dic = {}
	with open(filename, encoding="utf8") as fin:
		if skip_header:
			skip_gutenberg_header(fin)
		
		for line in fin:
			line = line.replace('-', ' ')
			strippables = string.punctuation + string.whitespace
			for word in line.split():
				word = word.strip(strippables)
				word = word.lower()
				
				hist[word] = []

	prefix = 
	suffix = 
	
def read_file(filename, skip_header=True):
	"""Makes a histogram that contains the words from a file. **Rewrite the author's method for simplicity**

	filename: string
	skip_header: boolean, default=True
   
	returns: map from each word to the number of times it appears.
	"""
	hist = collections.Counter()

	with open(filename, encoding="utf8") as fin:
		#skip the header
		skip_gutenberg_header(fin) if skip_header
		#update
		hist.update([word.strip(string.punctuation + string.whitespace).lower() for word in line.replace('-', ' ').split()])

	return hist
	
def skip_gutenberg_header(fp):
	"""Reads from fp until it finds the line that ends the header.

	fp: open file object
	
	copied from author's answer
	"""
	for line in fp:
		if line.startswith('*END*THE SMALL PRINT!'):
			break

if __name__ == '__main__':
'''
TODO: draw the rank-frequency plot
y = -s*x + b (y= logf, x=logr, b=logc)'''

import string
import collections

def read_file(filename, skip_header=True):
	"""Makes a histogram that contains the words from a file. 
	**Rewrite the author's method for simplicity**

	filename: string
	skip_header: boolean, default=True
   
	returns: map from each word to the number of times it appears.
	"""
	hist = collections.Counter()

	with open(filename, encoding="utf8") as fin:
		#skip the header
		if skip_header:
			skip_gutenberg_header(fin)
		#update
		for line in fin:
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
			
def freq_and_rank(hist):
	freq = list(hist.values())
	freq.sort(reverse=True)
	rank = 1
	for f in freq:
		yield rank, f
		rank += 1

def main():
	hist = read_file('emma.txt')
	for rank, freq in freq_and_rank(hist):
		print (rank, freq)	

				
if __name__ == '__main__':
	main()
import random
import string
from collections import defaultdict

def read_and_analyze(filename, skip_header=True):
	'''Read a text file and perform Markov analysis.

	structure: dict[prefix] = suffix
	
	Returns a markov dict
	'''
	d = defaultdict(list)
	with open(filename, encoding="utf8") as fin:
		if skip_header:
			skip_gutenberg_header(fin)
		
		for line in fin:
			line = line.replace('-', '')
			line_split = line.split()
			for i in range(0,len(line_split)-1):
				strippables = string.punctuation + string.whitespace
				word = line_split[i]
				word = word.strip(strippables).lower()
				# simple behavior with low effiency
				d[word].append(line_split[i+1]) 
				# This method could have problem with next line
	return d
	
def generate_random_content(d, prefix_len=2, text_len=50):
	'''Generate a random text based on a given markov dict
	
	Starts again if raised error
	'''
	des = []
	word_list = []
	for word in list(d.keys()):
		if len(word) == prefix_len:
			word_list.append(word)
	first = random.choice(word_list)
	des.append(first)
	first_s = d[first]
	index2 = random.randint(0,len(first_s)-1)
	for i in range(text_len):
		previous = first_s[index2]
		sub = d[previous]
		random_index = random.randint(0,len(sub)-1)
		des.append(sub[random_index])
	
	print(' '.join(des))
	
	
	
	
def skip_gutenberg_header(fp):
	"""Reads from fp until it finds the line that ends the header.

	fp: open file object
	
	copied from author's answer
	"""
	for line in fp:
		if line.startswith('*END*THE SMALL PRINT!'):
			break
			
def main():

	d = read_and_analyze('emma.txt')
	#for prefix, suffix in d.items():
	#	print(prefix, suffix)
	print("Generating random text")
	generate_random_content(d)

if __name__ == '__main__':
	main()
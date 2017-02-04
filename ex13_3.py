from ex13_1 import *
from ex13_2 import *

from collections import Counter
# I have downloaded _Pride and Prejudice_ from Gutenberg website and modified header with '#'

def count_number_frequency(l):
	'''Print the 20 most frequently used words in the book'''
	c = Counter(l)
	print(c.most_common(20)) 

if __name__ == '__main__':
	#print(list(read_file('PrideandPrejudice.txt'))) #check
	l = list(read_file('PrideandPrejudice.txt'))
	count_number_frequency(l)
	print("Total number of unique different words is: ", len(set(l))) #8141
	print("Total number of words is:", len(l)) #124493
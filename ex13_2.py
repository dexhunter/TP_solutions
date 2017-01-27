from ex13_1 import *
from collections import Counter
# I have downloaded Pride and Prejudice

def count_number(l):

	c = Counter(l)
	#print(c)

if __name__ == '__main__':
	#print(list(read_file('PrideandPrejudice.txt'))) #check
	l = list(read_file('PrideandPrejudice.txt'))
	#count_number(l)
	print("Total number of unique words is: ", len(set(l)))
	print("Total number of words is:", len(l))
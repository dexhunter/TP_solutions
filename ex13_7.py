import string
import sys
import codecs
from random import randint
from bisect import bisect

def read_file(filename):
	'''adapted from author's answer
		Read a file and return histogram of frequency of every word
	'''
	hist  = {}
	fp = open(filename, encoding="utf8")
	for line in fp:
		line = line.replace('-', ' ') # remove hyphens
		for word in line.split():
			word = word.strip(string.punctuation + string.whitespace) #remove punctuation and whitespace
			word = word.lower() #lowercase all the chars
			hist[word] = hist.get(word, 0) + 1 #increment if word is already encountered once else set to 1
	return hist
	
def cumsum(l):
	total = 0
	for i in range(len(l)):
		total += l[i]
		l[i] = total
	return l

def choose_from_random(hist):
	l = list(hist.keys()) # get word list
	#print(repr(l))
	cs = cumsum(list(int(i) for i in hist.values())) #cumulative sum of wordlist
	total = cs[-1] 
	x = randint(0,total-1)
	index = bisect(cs, x)
	return l[index]
	
if __name__ == '__main__':
	hist = read_file('emma.txt') #it is not working on 'PrideandPrejudice.txt' since there are different encoing schemes involved 
	# TO DO: learn encoding souce: http://stackoverflow.com/questions/14630288/unicodeencodeerror-charmap-codec-cant-encode-character-maps-to-undefined
	print(choose_from_random(hist))
	
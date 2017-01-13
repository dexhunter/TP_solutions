# mathesis pair 
# my idea: to start the pair of word need to be anagram (consist of all the same letter)
# secondly only 1 char's position can be changed. 


'''
According to author's answer it is easier to find the distance between a pair of word!
'''
from collections import defaultdict

def load_words(filename = "words.txt"):
	with open(filename) as fin:
		for line in fin:
			yield line.rstrip()
			
def all_anagram(s):
	'''
	s: string
	'''
	d = defaultdict(list)
	for i in s:
		signature = ''.join(sorted(i)) # siganature is a after-sort string of chars in the word
		d[signature].append(i)
		
	for k, v in d.items():
		if len(v) == 1:
			del d[k]
			
	return d
	
def pair_distance(a, b):
	# credit to http://www.greenteapress.com/thinkpython/code/metathesis.py
	assert len(a) == len(b) # if not equal raise AssertionError
	ctr = 0
	for c1, c2 in zip(a,b): # zip(a,b) returns a tuple for each corresponding char pair eg. "apple" & "paple" returns [('a', 'p'), ('p', 'a'), ('p', 'p'), ('l', 'l'), ('e', 'e')]
		if c1 != c2:
			ctr += 1
	return ctr

def find_metathesis(s):
	d = all_anagram(s)
	for v in d.itervalues():
		for a in v:
			for b in v:
				if a < b and pair_distance(a,b) == 2:
					print a, b
					
find_metathesis(load_words())
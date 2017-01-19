from __future__ import print_function, division
'''
I misunderstodd what 'middle' mean in the question. I thought it was exactly the mid, however, in the hint and answer of author's the middle mean actually anywhere between the first and last char. So I rewrite my program to fit the problem.
'''
# more on this
'''
I used others' codes to test but found only when using memo can you improve performance significatnly, otherwise the process is really slow
'''

from collections import defaultdict

memo = {}
memo[''] = ['']

def child(word, d):
	res = []
	for i in range(len(word)):
		child = word[:i] + word[i+1:]
		if child in d:
			res.append(child)
	return res
	
def children(word, d):
	'''Gets the child of a string which is in the list
	'''
	if word in memo:
		return memo[word]
	
	rest = []
	for x in child(word, d):
		if children(x, d): #if list is not empty
			rest.append(x)
			
	memo[word] = rest
	return rest

def all_children(d):
	res = []
	for word in d:
		t = children(word, d)
		if t != []:
			res.append(word)
	return res

def map_words(filename="words.txt"):
	d = defaultdict(list)
	with open(filename) as fin:
		for line in fin:
			word = line.strip().lower()
			d[word] = None
			
	for letter in ['a', 'i', '']:
		d[letter] = letter
	return d
	
def print_trail(word, d):
	if len(word) == 0:
		return
	print(word, end =' ')
	t = children(word, d)
	print_trail(t[0], d)

def print_longest(d):
	t = []
	words = all_children(d)
	for word in words:
		t.append((len(word), word))
	t.sort(reverse = True)
	
	for _,word in t[0:1]: #without _ underscore list index out of index
		print_trail(word, d)
		print('\n')
'''
	
def list_of_words(filename="words.txt"):
	f = open(filename)
	l = []
	for line in f:
		word = line.strip().lower()
		l.append(word)
	f.close()
	l.append('a')
	l.append('i')
	l.append('')
	return l
'''

print_longest(map_words())


'''
!another thought: start from the smallest 'a', 'i', and to get the longest consequence.
'''
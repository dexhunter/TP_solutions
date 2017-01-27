'''http://stackoverflow.com/questions/8286554/using-python-find-anagrams-for-a-list-of-words

# hughdbrown did an amazing job and I tried to understand his code and found this one is the better so far.
'''
from collections import defaultdict

def load_words(filename = "words.txt"):
	with open(filename) as f:
		for word in f:
			yield word.rstrip() # return a generator

def all_anagram(l):
	'''Reads a list and return a set of anagram words
	
	l: list
	
	Returns: set
	'''
	d = defaultdict(list) # avoid KeyError in dict()
	for word in l:
		signature = "".join(sorted(word)) #sorted: leave the original word untouched
		d[signature].append(word)
	return d

def print_anagram(l):
	d = all_anagram(l)
	for key, anagram in d.iteritems():
		if len(anagram) > 1:	
			print (anagram)
			#print (key, anagram)
			
def print_anagram_in_order(l):
	d = all_anagram(l)
	new_list = []
	for v in d.values():
		if len(v) > 1:
			new_list.append((len(v), v))
	new_list.sort(reverse=True) # sort in descending order
	
	for x in new_list:
		print (x)
		
		
		
if __name__ == '__main__':
	l = load_words()
	#print_anagram(l)
	print_anagram_in_order(l)

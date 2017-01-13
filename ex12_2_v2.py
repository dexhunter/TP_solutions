from collections import defaultdict

def load_words(filename = "words.txt"):
	with open(filename) as f:
		for word in f:
			yield word.rstrip() # return a generator
			
def all_anagram(s):
	'''
	s: string
	'''
	d = defaultdict(list)
	for i in s:
		signature = ''.join(sorted(i)) # siganature is a after-sort string of chars in the word
		d[signature].append(i)
		
	return d
		
def print_anagram_in_order(s):
	d = all_anagram(s)
	l = []
	for signature, words in d.items():
		if len(words) > 1:
			l.append((len(words),words))
	l.sort(reverse=True)
	for x in l:
		print x
	
def select_bingo(s, n=8):
	d = all_anagram(s)
	l = {}
	for signature, words in d.iteritems():
		if len(words) > 1:
			if len(signature) == n:
				l[signature] = words 
	res = []
	for k, v in l.iteritems():
		res.append((len(v),v))
	
	for x in sorted(res, reverse=False):
		print x
	
#print_anagram_in_order(load_words())
select_bingo(load_words())
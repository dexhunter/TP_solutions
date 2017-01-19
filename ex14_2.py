''' pickle is GREAT for this saving specified data structure task.
'''
import pickle
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
		
	for k, v in d.items(): #remove d[k] if there is only one value corresponding to the key which means there is no anagram for the word 
		if len(v) == 1:
			del d[k]

	return d

def save_dict(d):
    with open('shelf.pkl', 'wb') as f: #wb for write byte
        pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)

def look_up_dict(word):
	#look up a word and return its anagram in the 'shelf'
    with open('shelf.pkl', 'rb') as f: #rb for read byte
        d = pickle.load(f)
	for k, v in d.iteritems():
			for i in v:
				if i == word:
					return v

if __name__ == '__main__':
	books = all_anagram(load_words())
	save_dict(books)
	print ''
	print look_up_dict('tired')
	print look_up_dict('cosets')
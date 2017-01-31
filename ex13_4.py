'''I was wondering to use bisect search but still lack of effiency to tell wether a word is typo or should be included in the word list

Besides, it will be a good practice to use a dict to store both word lists but I will just skip this one for now and read the answer

(28/01/2017)Update: after reading author's answer, I found there are several things I ignored during process. For example, hyphens are not processed. But author does not even bother with translate at all. :/
'''

import string
'''
another method for ex13_1,13_2,13_3
'''

def load_word_as_dict(filename):
	'''Loads a file as a "memoized" dictionary mapping from word to frequency
	
	Return the dictionary
	'''
	d = {}
	with open(filename, encoding='utf8') as fin:
		for line in fin:
			if not line.strip().startswith('#'):
				for word in line.split():
					new_word = word.translate({ord(c): None for c in (string.punctuation + string.whitespace)}).lower().encode("utf-8")
					if new_word not in d:
						d[new_word] = 1
					else:
						d[new_word] += 1
	return d
				

def check_word_in_book(wordlist, book_wordlist):
	#l = [] 
	for word in book_wordlist.keys():
		if word not in wordlist.keys():
			print(word)
			#l.append(word)
	#print(len(l)) #2110

if __name__ == '__main__':
	d1 = load_word_as_dict('words.txt')
	#for i in d1:
	#	print(i, d1[i]) #test
	d2 = load_word_as_dict('PrideandPrejudice.txt')
	#for i in d2:
	#	print(i, d2[i]) #test
	check_word_in_book(d1, d2)
	
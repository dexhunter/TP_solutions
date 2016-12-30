from pronounce import read_dictionary

def hp_word(d):
	'''Prints all the homophone words as puzzle said
	
	d: given dictionary
	
	Returns: None
	'''
	for word, sound in d.items():
		word_cut = word[1:]
		word_sliced = word[0] + word[2:]
		if word_cut in d:
			if d[word] == d[word_cut]:
				if word_sliced in d:
					if d[word] == d[word_sliced]:
						if len(word) == 5:
							print word

		
if __name__ == '__main__':
	d = read_dictionary()
	nd = hp_word(d)

'''
I got answers:

eerie
llama
llano
llana
scent
ooohs
lloyd
aaron

while in author's solution answers are:
(which might not be correct because puzzle said the answer should be a five character word)
llama lama lama
llamas lamas lamas # this one is 6 char!
scent cent sent

But as long as you found _a_ word, then you solved the puzzle
'''	
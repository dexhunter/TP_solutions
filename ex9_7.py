def find_double(word):
	i = 0
	ctr = 0 # double counter
	while i < len(word) - 2:
		if word[i+1] == word[i]:
			ctr += 1
			i += 2
			if ctr == 3:
				return word
		else:
			ctr = 0
			i += 1

	return None
	

# ans: bookkeeper, etc
if __name__ == '__main__':

    with open('words.txt', 'r') as fin:
        words = [line.strip() for line in fin]
	for c in words:
		if find_double(c) != None:
			print (find_double(c))
		
	

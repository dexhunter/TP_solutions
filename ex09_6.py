def is_abecedarian(word):
	for i in range(len(word)):
		for j in range(i+1, len(word)):
			if ord(word[i]) > ord(word[j]):
				return False
	return True
	
def count_abecedarian(word):
	ctr = 0
	for c in word:
		if is_abecedarian(c):
			ctr += 1
	print ctr
		
		
if __name__ == '__main__':
    with open('words.txt', 'r') as fin:
        words = [line.strip() for line in fin]
	count_abecedarian(words)
# ans: The amount of abecedarian words is 596 
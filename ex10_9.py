def read_a(file):
	words = []
	for i in file:
		words.append(i.strip())
	return words
	
def read_b(file):
	words = []
	for i in file:
		words = words + [i.strip()]
	return words


if __name__ == '__main__':
    with open('words.txt', 'r') as fin:
		print len(read_a(fin))
    with open('words.txt', 'r') as fin2:
		print len(read_b(fin2)) #much slower
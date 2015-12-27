def read(object):
	fin = open(object)
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			print word
			
read('words.txt')
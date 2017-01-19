def read(f):
	with open(f) as file:
		for line in file:
			word = line.strip()
			if len(word) > 20:
				print word
			
read('words.txt')
#read('test.txt')
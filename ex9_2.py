def has_no_e(word):
	if "e" not in word:
		return True
	else:
		return False
		
def read(object):
	fin = open(object)
	all = 0.0
	no_e = 0.0
	for line in fin:
		all += 1
		word = line.strip()
		checked = has_no_e(word)
		if checked == True:
			print word
			no_e += 1
	print no_e/all
			
			
read('words.txt')
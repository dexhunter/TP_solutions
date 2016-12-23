def has_no_e(word):
	if "e" not in word:
		return True
	else:
		return False
		
def read(f):
	ctr_e = 0.0
	ctr_all = 0.0
	with open(f) as file:
		for line in file:
			ctr_all += 1
			word = line.strip()
			if has_no_e(word):
				print word
				ctr_e += 1
		print ctr_e / ctr_all	
			
read('words.txt')
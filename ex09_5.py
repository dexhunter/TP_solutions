def uses_all(word, letters):
	# if letter in letters does not appear in word, it means this letter was not used in word which will return False
	for c in letters:
		if c not in word:
			return False
	return True
	
print (uses_all("To day is a good day", "god"))
print (uses_all("To day is a good day", "godA"))
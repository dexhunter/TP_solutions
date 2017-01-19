def uses_only(word, letters):
	for c in "".join(word.split()):
		#print c # test
		if c not in letters:
			return False
	return True
	
print (uses_only("hoe alfalfa", "acefhlo" ))
# Ace, lohf?
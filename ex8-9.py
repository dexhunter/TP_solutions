def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	i = 0
	j = len(word2) - 1
	
	while j >= 0:
		if word1[i] != word2[j]:
			return False
		i += 1
		j -= 1
	
	return True
	

print is_reverse("applea", "eelppa")
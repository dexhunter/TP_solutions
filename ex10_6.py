def is_anagram(a, b):
	for c in a:
		if c not in b:
			return False
	for c in b:
		if c not in a:
			return False
	return True
	
print is_anagram("apple", "palpe")
print is_anagram("applex", "palpe")
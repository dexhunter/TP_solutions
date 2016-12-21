def count(string, letter, index):
	count = 0
	for i in string[index:]:
		if i == letter:
			count += 1
	print count

count('banana', 'a', 2)
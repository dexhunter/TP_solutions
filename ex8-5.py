def count(string, letter):
	count = 0
	for i in string:
		if i == letter:
			count += 1
	print count
	
count('banana', 'a')
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O' or letter == 'Q':
		suffix = 'uack'
		print letter + suffix
	else:
		suffix = 'ack'
		print letter + suffix
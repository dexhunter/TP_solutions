#running on python 2 is fine

def ducklings():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'

	for letter in prefixes:
		if letter == 'O' or letter == 'Q':
			suffix = 'uack'
			print letter + suffix
		else:
			suffix = 'ack'
			print letter + suffix
			
ducklings()

#friut[:] will return the full string which is "banana"

def find(string, letter, index):
	while index < len(string):
		if string[index] == letter:
			return index
		index = index + 1
	return -1

find_second_e = find("I revised this exercise to make it more readable", "e", 5)
print find_second_e

def count(string, letter):
	length = len(string)
	counter = 0
	index = 0
	while length > 0:
		if find(string, letter, index) != -1:
			counter += 1
			index = find(string, letter, index)
		string = string[1 : len(string)]
		length = len(string)

	return counter	
		
		
count_e = count("I revised this exercise to make it more readable", "e")
print count_e
		
import sys

def rotate_word(word, number):
	list = []
	new_word = []
	for i in word:
		a = ord(i)
		b = a + number
		while b > 122:
			b = b - 26
		new_word.append(b)
		
	for j in new_word:
		print chr(j),
		sys.stdout.write('')
	print "\n"

rotate_word("abcdefgh", 28)
		
		
#my verion is kinda dump, go check out rotate from author XD
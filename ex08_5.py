def rotate_word(s, n):
	s_c = "" #initialize
	i = 0 #initialize
	for c in s:
		if ord(c) >= ord('A') and ord(c) <= ord('Z'):
			i = (ord(c) - ord('A') + n ) % 26 + ord('A') 
		elif ord(c) >= ord('a') and ord(c) <= ord('z'):
			i = (ord(c) - ord('a') + n ) % 26 + ord('a')
		else:
			i = ord(c) # other characters does not change
		s_c +=  chr(i)
	return s_c
	
print (rotate_word("apple+apple", 3))
print (rotate_word("APPLE", 3))
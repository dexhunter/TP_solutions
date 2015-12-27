def is_palindrome(word):
		if word != word[::-1]:
			return False
		else:
			return True
	
print is_palindrome("redivider")
print is_palindrome("apple")
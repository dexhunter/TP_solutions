def is_palindrome(word):
	return word == word[::-1]

	
print is_palindrome("redivider")
print is_palindrome("apple")
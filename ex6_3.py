def is_palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False
		
print is_palindrome("helloollehr")
	
#another version

def is_palin(w):
	if w[-1] != w[-len(w)]:
		return False
	else:
		return is_palin(w[-len(w)+1:len(w)-1])	# This return is essential for successful run! Otherwise it is not a recursive call
	
result = is_palin("redividerr")
print result
# parameter is a string

def any_lowercase1(s):
	for c in s:
		if c.islower():
			return True #check every character in the string is a lowercase character and return a boolean value
		else:	
			return False
			
def any_lowercase2(s):
	for c in s:
		if 'c'.islower():  #always return a string 'true' since 'c' is a lowercase no matter how many characters are in the string
			return 'True'
		else:
			return 'False'
			
def any_lowercase3(s):
	for c in s:
		flag = c.islower() #check if the last character in the string is a lower case, return a boolean value
	return flag
	
def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower() #check if the last character in the string is a lower case, return a boolean value
	return flag
	
def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False #check if every character in the string is a lower case, return a boolean value False if not
	return True
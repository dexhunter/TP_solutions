#Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display

def right_justify(s):
	whitespace_num = 70 - len(s)
	s = ' ' * whitespace_num + s
	print s

right_justify("month")
right_justify("a")
right_justify("This is a test,This is a test,This is a test,This is a test,This is a") #string length = 69
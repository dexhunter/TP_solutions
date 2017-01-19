def is_palindrome(word):
	return word == word[::-1]
	
def is_palindrome_num(num):
	part_one = num[2:6]
	num = str(int(num) + 1)
	part_two = num[1:6]
	num = str(int(num) + 1)
	part_three = num[1:5]
	num = str(int(num) + 1)
	part_four = num
	if is_palindrome(part_one):
		if is_palindrome(part_two):
			if is_palindrome(part_three):
				if is_palindrome(part_four):
					return True
	return False
	
def check_num():
	for i in range(100000, 999999):
		if is_palindrome_num(str(i)):
			print i
			
			
check_num()
#ans: 198888, 199999
def is_reverse(a, b):
	return b == a[::-1]

def find_mom_and_my_age_difference():
	
	
	diff = 15
	while diff < 50:
		ctr = 0
		my_age = 0
		while my_age < 99:
			#print my_age
			mom_age = my_age + diff
			if is_reverse(str(my_age).zfill(2), str(mom_age)):
				ctr += 1
				if ctr == 8:
					return diff
			my_age += 1
		
		diff += 1

def find_my_age(n):
	mom_age = n
	my_age = 0
	ctr = 0
	while my_age < 99:
		if is_reverse(str(my_age).zfill(2), str(mom_age)):
			ctr += 1
			if ctr == 6:#reverse phenomena has happened six times before
				return my_age
		mom_age += 1
		my_age += 1

print find_my_age(find_mom_and_my_age_difference())	
#ans: 57 yrs old
'''
after read author's answer, I found there are two possibilities one is that kid's birthday is earlier than mom's, the other is mom's birthday is earlier than kid's but that will reuslt in a different situation. But my solution is enough to find the right answer.
'''
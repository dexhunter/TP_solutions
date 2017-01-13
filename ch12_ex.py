def sumall(*args):
# use of gather opeartion
# on page 142
	sum_result = 0
	for i in range(len(args)):
		sum_result = sum_result + args[i]
	return sum_result
	
print sumall(1,2,3,4)
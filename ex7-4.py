def eval_loop():
	flag = True
	while flag:
		x1 = raw_input("Do you want to evaluate the eqution? Type 'yes' or 'no'")
		if x1 == "yes":
			x2 = raw_input("Type the equation.")
			result = eval(x2)
			print result
		if x1 == "no":
			flag = False
	
eval_loop()
	
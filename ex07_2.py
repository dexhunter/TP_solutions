def eval_loop():
	while True:
		i = raw_input("Input: ")
		try:
			print(eval(i))
		except (NameError, SyntaxError):
			if i == 'done':
				break
			else:
				print i
			
	
import math #in case you need to evaluate some complex functions
eval_loop()
	
# 5_2_1 run python2
import math

def check_fermat(a, b, c, n):
	if n > 2 and a**n + b**n == c**n:
		print ("Fermat is wrong!")
	else:
		print ("Fermat is right on this!")
		

def run_cf():
	for a in range(1, 100):
		for b in range(1, 100):
			for c in range(1, 100):
				for n in range(3, 100):
					check_fermat(a, b, c, n)
				
		
		
		
# first test
check_fermat(2, 3, 4, 2)
check_fermat(3, 4, 5, 2) #n need to be more than 2!
		
# second test 
#run_cf()
# 5_2_2 run python2
def check_fermat_custom():
	a = input("Please in put a: ")
	b= input("Please in put b: ")
	c = input("Please in put c: ")
	n = input("Please input n: ")
	return check_fermat(a, b, c, n)
	
check_fermat_custom()	
	

	
	

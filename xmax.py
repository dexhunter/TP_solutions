def xmas_tri(i, t=0, nrow=0):
	"""Draw a Christmas triangle

		i : number of rows to print out
		t : the amount of asterix to initialize
		nrow : total number of rows
	"""
	if i == 0:
		return 0
	else:
		print ' ' * ( i + 1 + nrow) + 'x' * ( t * 2 + 1 )
		return xmas_tri( i - 1, t + 1 , nrow)


		
def xmas_trunk(n):
	node = n/2 + 1

	for i in range(n/4-1):
		print " " * (n-n/4) + "x" * node

		

def xmas_bot(n):
	node = n/2 + 1
	for i in range(n/2):
		print " " * (n-n/4)  + "x" * node

		
def xmas_draw(n):
	xmas_tri(n/3, 0, (n/3)*2)
	xmas_trunk(n)
	xmas_tri(n/3, n/3, (n/3) )
	xmas_trunk(n)
	xmas_tri(n/3, (n/3) * 2, 0)
	xmas_bot(n)
	
	




	

if __name__ == '__main__':
	n = input("Please give n: ")
	xmas_draw(n)

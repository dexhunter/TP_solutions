def do_twice(f,v):
	f(v)
	f(v)
	
def print_twice(s):
	print(s)
	print(s)

do_twice(print_twice,"spam")

def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
	
print ("--------cutting line---------")

do_four(print_twice,"four")
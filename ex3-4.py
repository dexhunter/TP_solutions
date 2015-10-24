def print_spam():
	print 'spam'

def do_twice(a, b):
	a(b)
	a(b)

def print_twice(s):
	print s
	
do_twice(print_twice, 'spam')
	
def do_four(a, b):
	do_twice(a, b)
	do_twice(a, b)
	
do_four(print_twice, 'open')
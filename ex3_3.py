#first one

def do_two(f):
	f()
	f()

def print_two(v):
	print (v*2)

	
def do_four(f):
	f()
	f()
	f()
	f()
	

def print_dash():
	print ( '-', end=' ' )

def print_line_short():
	print ("+", end=' ')
	do_four(print_dash)
	

def print_line():
	do_two(print_line_short)
	print ("+", end=' ')

def print_line_four():
	do_four(print_line_short)
	print ("+", end=' ')
	
def print_vbar():
	print(("|"+" "*9)*2+"|")

def print_vbar_four():
	print(("|"+" "*9)*4+"|")


def print_grid():
	print_line()
	print("")
	do_four(print_vbar)
	print_line()
	print("")
	do_four(print_vbar)
	print_line()
	

print_grid()

#second one

def print_grid_four():
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()
	print("")
	do_four(print_vbar_four)
	print_line_four()

print("")
print("---------cutting edge------------")

print_grid_four()
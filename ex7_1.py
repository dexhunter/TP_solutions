def mysqrt(a):
	epsilon = 0.00001
	x = 5.00000
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < epsilon:
			return y
			break
		x = y
		
import math
print mysqrt( 4 )

def test_square_root():
	print "a	mysqrt(a)	math.sqrt(a)	diff"
	print "-	---------	------------	----"
	for a in range(1, 10):
		print "%.1f	%.5f	        %.5f	        %f" % (a,mysqrt(a), math.sqrt(a), mysqrt(a)-math.sqrt(a))
		
test_square_root()
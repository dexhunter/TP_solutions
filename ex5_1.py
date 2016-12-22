import time
# time.time() return the time in seconds since the epoch as a floating point number

def chour(t):
	hour = t / 3600
	print("The number of hours has passed since epoch is %f" % hour)

def cminute(t):
	minute = t / 60
	print("The number of minutes has passed since epoch is %f" % minute)
	
def cseconds(t):
	seconds = t
	print("The number of seconds has passed since epoch is %f" % seconds)
	
def num_day():
	sec = time.time()
	num_day = sec / (60*60*24)
	print("The number of days has passed since epoch is %f" % num_day)

num_day()
chour(time.time())
cminute(time.time())
cseconds(time.time())
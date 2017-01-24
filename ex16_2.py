import time
from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta

def current_day():
	return (date.strftime(date.today(), "%A")) #strftime = string format time
	
def ObtainDate():
	while True:
		usrIn = input("Give a date in the format of yyyy-mm-dd: ")
		try:
			return datetime.strptime(usrIn, "%Y-%m-%d") # strptime = string parse time
		except ValueError:
			print ("Invalid format!\n")

def usr_info(birthday):
	'''Takes a birthday as input and prints the user's age and the number of days, hours, minutes and seconds until their next birthday

	birthday: yyyy-MM-dd %Y-%m-%d
	'''
	today = datetime.today()
	print ("Your age is: %d" % relativedelta(today, birthday).years)
	#print ("Your age is: %d" % (today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)))) #second way of writing
	next_birthday = birthday.replace(year=today.year)
	if next_birthday < today:
		next_birthday = birthday.replace(year=today.year + 1)
	duration = next_birthday - today
	print ("Time until your next birthday is: ", duration.days, " days.")

def double_day(bday1, bday2):
	''' The author wrote "For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day."
	But I do not know what does author mean by double day at all. So I looked up the answer and got the idea that double day is actually when the difference between birthday of first dude and second dude doubles. But I wonder if there are any meaning to calculate this.
	source: https://github.com/AllenDowney/ThinkPython2/blob/master/code/double.py
	
	update: okay, I understand it now after testing. It basically means that older dude lives twice amount of days than younger dude
	'''
	old_dude = min(bday1, bday2)
	young_dude = max(bday1, bday2)
	delta = young_dude + (young_dude - old_dude)
	return delta #return a timedelta object when old_dude lives twice amount of days as younger dude 
	
	
def n_day(bd1, bd2, n):
	'''A general version of double_day which computes the day when one person is n times older than the other.
	
	Return: timedelta
	'''
	old_dude = min(bd1, bd2)
	young_dude = max(bd1, bd2)
	delta = young_dude + n * (young_dude - old_dude)
	return delta
	
if __name__ == '__main__':
	print (date.today())
	print (current_day())
	birthday = ObtainDate()
	usr_info(birthday)
	# two day before I was born
	rday = datetime(1995, 12, 21)
	print("Double day is: ", double_day(rday, birthday))
	print("Ten times day is: ", n_day(rday, birthday, 10))

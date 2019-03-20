#Dalton Redman
time = eval(input("Please enter a random amount of seconds to solve: "))

days = 0
hours = 0
minute = 0

check1 = False
check2 = False
check3 = False

if(time >= 86400):
	x = time / 86400
	days = int(x)
	time = time - (days * 86400)
	check1 = True
	
if(time >= 3600 and time < 86400):
	x = time / 3600
	hours = int(x)
	time = time - (hours * 3600)
	check2 = True

if(time >= 60 and time < 3600):
	x = time / 60
	minute = int(x)
	time = time - (minute * 60)
	check3 = True
	
second = time

if(check1 == True):
	print("The converted value equals {} days, {} hours, {} minutes, and {} seconds".format(days,hours,minute,second))
elif(check2 == True):
	print("The converted value equals {} hours, {} minutes, and {} seconds".format(hours,minute,second))
elif(check3 == True):
	print("The converted value equals {} minutes and {} seconds".format(minute,second))
else:
	print("The converted value equals {} seconds".format(second))
	
input("hold")	
#Dalton Redman
year = eval(input("Please enter a year: "))

check1 = year % 100		#check for division (must be zero)
check2 = year % 400		#check for division	(must be zero)
check3 = year % 4		#check for division	(must be zero)

if(check1 == 0 and check2 == 0):
	print("{} is a leap year, and February has 29 days".format(year))
elif(check1 != 0 and check3 == 0):
	print("{} is a leap year, and February has 29 days".format(year))
else:
	print("{} is not a leap year, and February has 28 days".format(year))
	
input("hold")
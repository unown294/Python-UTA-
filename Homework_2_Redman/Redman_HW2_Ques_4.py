import random

Ran_number = random.randint(1,100)		#Random number to guess
test = True								#Check value for while loop
tries = 0								#Number of tries

while test == True:
	U_Number = int(input("Guess a number between 1 and 100: "))
	tries = tries + 1
	if(U_Number < Ran_number):
		print("Guess Higher")
	elif(U_Number > Ran_number):
		print("Guess Lower")
	elif(U_Number == Ran_number):
		print("Correct and it only took {} tries" .format(tries))
		test = False

input("\nHit enter to close")
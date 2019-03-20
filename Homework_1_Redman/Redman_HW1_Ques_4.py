#Dalton Redman
height = eval(input("Please enter in inches: "))
weight = eval(input("Please enter you weight in pounds: "))

BMI = weight * 703 / height ** 2

if(BMI >= 18.5 and BMI <= 25):
	print("Your BMI is {:.2f}, which is optimal for you".format(BMI))
if(BMI < 18.5):
	print("Your BMI is {:.2f}, but your underweight".format(BMI))
if(BMI > 25):
	print("Your BMI is {:.2f}, but this means your overweight".format(BMI))

input("press enter to stop holding")
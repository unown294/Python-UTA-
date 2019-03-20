grades = [0,0,0,0,0]

def calc_average(grades = []):
	sum = 0
	i = 0
	while(i < len(grades)):
		sum = sum + grades[i]
		i += 1 
	average = sum / len(grades)
	print("Your average test score is {:.0f}% out of {} tests".format(average, len(grades)))

def determining_grade(grades = []):
	i = 0
	letter_grade = ["","","","",""]
	while (i < len(grades)):
		if(grades[i] >= 90 and grades[i] <= 100):
			letter_grade[i] = "A"
		elif(grades[i] < 90 and grades[i] >=80):
			letter_grade[i] = "B"
		elif(grades[i] < 80 and grades[i] >=70):
			letter_grade[i] = "C"
		elif(grades[i] < 70 and grades[i] >=60):
			letter_grade[i] = "D"
		elif(grades[i] < 60 and grades[i] >=0):
			letter_grade[i] = "F"
		print("[Test {}] [{}%] Letter grade: {}".format(i+1,grades[i],letter_grade[i]))
		i += 1
		
for x in range(len(grades)):
	y = int(input("Please enter your {} test grade (0 - 100): ".format(x+1)))
	while(y < 0 or y > 100):
		y = int(input("Error: Please enter your {} test grade (0 - 100): ".format(x+1)))
	grades[x] = y

print()
determining_grade(grades)
calc_average(grades)

print()
input("Hit enter to close")
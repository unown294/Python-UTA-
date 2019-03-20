import pickle
import Employee

#### Editable Variables #####
FILENAME = 'contacts.dat'
LOOK = "look"
ADD = "add"
UPDATE = "update"
DELETE = "delete"
EXIT = "exit"
#############################

def main():
	x = True
	employee = read_dictionary()	
	
	while(x == True):
		print("COMMAND MENU\n{} - Search for an Employee\n{} - add a new employee\n{} - Update an existing Employee\n{} - Delete an employee from the list\n{} - Exit the program".format(LOOK.ljust(7),ADD.ljust(7),UPDATE.ljust(7),DELETE.ljust(7),EXIT.ljust(7)))
		response = str(input("\nCommand: "))
		if(response == LOOK):
			look(employee)
		elif(response == ADD):
			add(employee)
		elif(response == UPDATE):
			updater(employee)
		elif(response == DELETE):
			delete(employee)
		elif(response == EXIT):
			x = False
			exit(employee)
		else:
			print("\nPlease enter a valid response\n")
			
def add(employee):
	id = int(input("Please enter the ID of the new employee: "))
	name = str(input("Please enter the name of the Employee: "))
	dept = str(input("Please enter the department of the Employee: "))
	title = str(input("Please enter the job title of the Employee: "))
	
	new_employee = Employee.Employee(id, name, dept, title)				# Generates a New employee for the Dictionary
	
	if id not in employee:												# Adds the Newly generated employee to the dictionary
		employee[id] = new_employee
		print("\nNew employee has been added\n")
	else:
		print("\nEmployee ID is in use already, please use a different ID number\n")
	
def read_dictionary(): 													# Reads the current dictionary to check if its valid or needs to be generated
	# Testing to see if the File Exist
	try:
		input_file = open(FILENAME, 'rb')
		
		employee_list = pickle.load(input_file)
		
		input_file.close()
	# If list is not available, then generate a list and return it
	except IOError:
		employee_list = {}
		
	return employee_list

def updater(employee):
	id = int(input("Please enter the Employee's ID number you wish to update: "))
	
	if id in employee:
		name = str(input("Please enter the name of the Employee: "))
		dept = str(input("Please enter the department of the Employee: "))
		title = str(input("Please enter the job title of the Employee: "))
		
		update_employee = Employee.Employee(id, name, dept, title)
		employee[id] = update_employee
	else:
		print("This ID doesn't exist in our system, please check your ID if its correct")

def delete(employee):
	id = int(input("Please enter the Employee's ID number you wish to remove: "))
	
	if id in employee:
		del employee[id]
		print("\nEmployee has been removed from the system\n")
	else:
		print("\nEmployee doesn't exist in our system, please check if that Employee ID is correct\n")

def look(employee):		# Prints the desired ID if found in the dictionary
	id = int(input("Please enter the Employee's ID number: "))
	
	print()
	print(employee.get(id, "That Employee is not in the system"))
	print()
	
def exit(employee): 	# Saves all changes made to the dictionary before exiting
	output_file = open(FILENAME, 'wb')
	
	pickle.dump(employee, output_file)
	
	output_file.close()
	
			
main()

import random

insert = "1"
select = "2"
seek = "3"
update = "4"
remove = "5"
exit = "6"
blank = ""
text_name = "Name"
text_email = "email"
text_phone = "Phone"

######		Creates file if not available		###############
f = open("contact.txt","w")
f.close()
######		Creates file if not available		###############

def modify():
	x = 1

def search(name):
	x = True
	cursor = conn.execute("select * from Contact")
	for c in cursor:
		if(c[0] == name):
			print('{}: {}'.format(text_name,c[0]))		# Name
			print('{}: {}'.format(text_email,c[1]))		# email
			print('{}: {}'.format(text_phone,c[2]))		# Phone
			print()
	
def delete(name):
	conn.execute("DELETE FROM Contact WHERE name=?", name)
	conn.commit()
	
def add(name, email, phone):
    outfile = open('contact.txt', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('Contact # {}'.format(r+1))
    outfile.write('{}: {}\n'.format(text_name.rjust(8," "),name))
    outfile.write('{}: {}\n'.format(text_email.rjust(8," "),email))
    outfile.write('{}: {}\n'.format(text_phone.rjust(8," "),phone))
    outfile.write('{}'.format(blank.ljust(24, "-")))	

    # Close the file.
    outfile.close()

def show():
    infile = open('contact.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()
    print(file_contents)
		
	
def main():
	x = True
	y = True
	count = 0
	while x == True:
		print("  CHOICE MENU\n{}) Add a contact\n{}) Show the list of contacts\n{}) search for a name in the list\n{}) Modify a contact\n{}) Delete a contact from the list\n{}) Quit".format(insert,select,seek,update,remove,exit))
		response = str(input("\nCommand: "))
		if(response == select):
			show()
		elif(response == insert):			# For adding to the table
			while(y == True):
				name = input("Name: ")
				email = input("email: ")
				phone = input("phone: ")
				add(name, email, phone)
				response = input("Do you want to add another record?\nY = yes, anything else = no: ")
				if(response == "Y" or response == "y"):
					y = True
				else:
					y = False
		elif(response == remove):
			name = input("Enter the name you wish to delete: ")
			delete(name)
		elif(response == seek):
			name = input("Enter the name you wish to search for: ")
			search(name)
		elif(response == update):
			modify()
		elif(response == exit):
			x = False
			print("Exiting the program...")
		else:
			print("Please enter a valid response")
		count =+1
		y = True

main()

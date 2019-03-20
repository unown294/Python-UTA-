import sqlite3
import random
conn = sqlite3.connect('contact.db')

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

conn.execute('''
CREATE TABLE if not exists Contact
(
  contactID		INTEGER					NOT NULL,
  name			TEXT PRIMARY KEY        NOT NULL,
  email			TEXT	 	            NOT NULL,
  phone 		TEXT 	                NOT NULL
)
''')

def modify(name):
	cursor = conn.execute("select * from Contact")
	for c in cursor:
		if(c[1] == name):
			contactID = c[0]
			
			sql = 'DELETE FROM Contact WHERE name=?'
			cur = conn.cursor()
			cur.execute(sql, (name,))
						
			email = input("Please enter the new email: ")
			phone = input("Please enter the new phone: ")
			
			conn.execute("INSERT INTO Contact (contactID, name, email, phone) VALUES (?, ?, ?, ?)",(contactID, name, email, phone))
			conn.commit()

def search(name):
	cursor = conn.execute("select * from Contact")
	for c in cursor:
		if(c[1] == name):
			print('{}: {}'.format(text_name,c[1]))		# Name
			print('{}: {}'.format(text_email,c[2]))		# email
			print('{}: {}'.format(text_phone,c[3]))		# Phone
			print()
		cursor = conn.execute("select * from Contact")
	
def delete(name):
	sql = 'DELETE FROM Contact WHERE name=?'
	cur = conn.cursor()
	cur.execute(sql, (name,))
	conn.commit()
	
def add(name, email, phone):
	x = False
	cursor = conn.execute("select * from Contact")
	
	contactID = random.randint(1, 9999)
	
	for c in cursor:
		if(contactID == c[0]):
			x = True
	while(x == True):
		for c in cursor:
			if(contactID != c[0]):
				contactID = c+1
				x = False

	conn.execute("INSERT INTO Contact (contactID, name, email, phone) VALUES (?, ?, ?, ?)",(contactID, name, email, phone))
	conn.commit()

def show():
	print("List of contact(s)")
	print('{}'.format(blank.ljust(24, "-")))
	r = 0
	cursor = conn.execute("select * from Contact ORDER BY contactID ASC")
	for c in cursor:
		print('Contact # {}'.format(c[0]))
		print('{}: {}'.format(text_name.rjust(8," "),c[1]))		# Name
		print('{}: {}'.format(text_email.rjust(8," "),c[2]))		# email
		print('{}: {}'.format(text_phone.rjust(8," "),c[3]))		# Phone
		print('{}'.format(blank.ljust(24, "-")))				# Dash
		r = r + 1
	
def exit2():
    outfile = open('contact.txt', 'w')
    r = 0
    cursor = conn.execute("select * from Contact ORDER BY contactID ASC")
    for c in cursor:
        outfile.write('Contact # {}\n'.format(r+1))
        outfile.write('{}: {}\n'.format(text_name.rjust(8," "),c[1]))
        outfile.write('{}: {}\n'.format(text_email.rjust(8," "),c[2]))
        outfile.write('{}: {}\n'.format(text_phone.rjust(8," "),c[3]))
        outfile.write('{}\n'.format(blank.ljust(24, "-")))	
        r = r + 1
    # Close the file.
    outfile.close()
	
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
			name = input("What name would you like to update: ")
			modify(name)
		elif(response == exit):
			exit2()						#converts database to a text file
			x = False
			print("Exiting the program...")
		else:
			print("Please enter a valid response")
		count =+1
		y = True

main()

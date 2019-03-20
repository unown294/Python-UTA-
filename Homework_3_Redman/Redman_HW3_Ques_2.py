import sqlite3
import random
conn = sqlite3.connect('player_manager.db')
print('Opened database successfully')

############# Editable Commands ################
blank = ""
insert = "add"
select = "view"
remove = "del"
exit = "exit"
update = "update"
sort = "sort"
text = ['Name','Wins','Losses','Ties','Games']
################################################

##### Creates the File if not present ##########
conn.execute('''
CREATE TABLE if not exists Player
(
  playerID		INTEGER	 PRIMARY KEY	NOT NULL,
  name			TEXT        	        NOT NULL,
  wins			INTEGER 	            NOT NULL,
  losses 		INTEGER                 NOT NULL,
  ties	        INTEGER                 NOT NULL
)
''')

def view():
	cursor = conn.execute("select * from Player ORDER BY wins DESC")
	print("{:<10}{:>10}{:>10}{:>10}{:>10}".format(text[0],text[1],text[2],text[3],text[4]))
	print(blank.ljust(50,'-'))
	for c in cursor:
		print('{:<10}{:>10}{:>10}{:>10}{:>10}'.format(c[1],c[2],c[3],c[4],c[2]+c[3]+c[4]))

	
def add(ID, name, win, losses, ties):
	name = name.capitalize()
	conn.execute("INSERT INTO Player (playerID, name, wins, losses, ties) VALUES (?, ?, ?, ?, ?)",(ID, name, win, losses, ties))
	conn.commit()
	print("{} was added to the database".format(name.capitalize()))
	
def delete(name):
	sql = 'DELETE FROM Player WHERE name=?'
	cur = conn.cursor()
	cur.execute(sql, (name,))
	conn.commit()

def updater(name):
	cursor = conn.execute("select * from Player")
	for c in cursor:
		if(c[1] == name):
			playerID = c[0]
		
			sql = 'DELETE FROM Player WHERE name=?'
			cur = conn.cursor()
			cur.execute(sql, (name,))
						
			wins = input("Please enter the amount of wins for {}: ".format(name))
			losses = input("Please enter the amount of losses for {}: ".format(name))
			ties = input("Please enter the amount of ties for {}: ".format(name))
			
			conn.execute("INSERT INTO Player (playerID, name, wins, losses, ties) VALUES (?, ?, ?, ?, ?)",(playerID, name, wins, losses, ties))
			conn.commit()
	
def main():
	x = True
	t = False
	count = 0
	print("Player Manager\n")
	while x == True:
		if(count >= 1):
			print()
		print("COMMAND MENU\n{}- View players\n{}- Add a Player\n{}- Delete a player\n{}- Updates a user info\n{}- Exit Program".format(select.ljust(7),insert.ljust(7),remove.ljust(7),update.ljust(7),exit.ljust(7)))
		response = str(input("\nCommand: "))
		if(response == select):
			view()							# Prints the results of the database
		elif(response == insert):
			ID = random.randint(1,9999)		# Random number for ID
			name = input("Name: ")
			win = int(input("Wins: "))
			while(win < 0):
				win = int(input("Enter a value greater than 0. Wins: "))
			losses = int(input("Losses: "))
			while(losses < 0):
				losses = int(input("Enter a value greater than 0. Losses: "))
			ties = int(input("Ties: "))
			while(ties < 0):
				ties = int(input("Enter a value greater than 0. Ties: "))
			add(ID, name, win, losses, ties)
		elif(response == remove):
			name = input("Name: ")
			name = name.capitalize()
			delete(name)						# Deletes users
		elif(response == update):
			name = input("Please enter the player's name you wish to edit: ")
			name = name.capitalize()
			updater(name)						# Update the data base
		elif(response == exit):
			conn.commit()					# Exit the program
			conn.close()
			x = False
			print("Bye!")
		else:
			print("Please enter a valid response")
		count =+1

main()

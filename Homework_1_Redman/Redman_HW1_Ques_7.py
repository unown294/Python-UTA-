#Dalton Redman
print("Reboot the computer and try to connect.")								#Issue 1
response = input("Did that fix the problem: ")

if(response == "NO" or response == "no" or response == "No"):					#ISSUE 2
	print("Reboot the router and try to connect.")
	response2 = input("Did that fix the problem: ")
	
	if(response2 == "NO" or response2 == "no" or response2 == "No"):			#ISSUE 3
		print("Make sure the cable between the router and modem are plugged in firmly.")
		response3 = input("Did that fix the problem: ")
		
		if(response3 == "NO" or response3 == "no" or response3 == "No"):		#ISSUE 4
			print("Move the router to a new location.")
			response4 = input("Did that fix the problem: ")			
			
			if(response4 == "NO" or response4 == "no" or response4 == "No"):	#ISSUE 5
				print("Get a new router")
				input("hit enter to continue")
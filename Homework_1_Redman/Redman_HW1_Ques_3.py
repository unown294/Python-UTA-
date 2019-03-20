#Dalton Redman
weight = eval(input("Please enter the weight of your package in pounds: "))

#For no rate
if(weight <= 2):
	rate = 1.50 	# in dollars
	shipping_total = weight * rate
	print("Since your package weights {}, your shipping rate is ${:.2f}".format(weight,shipping_total))

#For a 10% rate
if(weight > 2 and weight <= 6):
	rate = 3.00 	# in dollars
	shipping_total = weight * rate
	print("Since your package weights {}, your shipping rate is ${:.2f}".format(weight,shipping_total))

#For a 20% rate
if(weight > 6 and weight <= 10):
	rate = 4.00 	# in dollars
	shipping_total = weight * rate
	print("Since your package weights {}, your shipping rate is ${:.2f}".format(weight,shipping_total))
	
#For a 30% rate
if(weight > 10):
	rate = 4.75 	# in dollars
	shipping_total = weight * rate
	print("Since your package weights {}, your shipping rate is ${:.2f}".format(weight,shipping_total))
	
input("hit enter to stop waiting")
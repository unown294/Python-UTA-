#Dalton Redman
quantity = eval(input("Please enter the quantity of software you wish to purchase: "))

PRICE = 99 	#in dollars

#For no discount
if(quantity <= 9):
	discount = 0 	# 0%
	discounted_P = PRICE - (PRICE * discount)
	discounted_total = discounted_P * quantity
	print("Since you purchased {} packages you total of ${:.2f}".format(quantity,discounted_total))

#For a 10% discount
if(quantity >= 10 and quantity <= 19):
	discount = .1 	# 10%
	discounted_P = PRICE - (PRICE * discount)
	discounted_total = discounted_P * quantity
	print("Since you purchased {} packages, you recieved a discount of 10% which resulted in a total of ${:.2f}".format(quantity,discounted_total))

#For a 20% discount
if(quantity >= 20 and quantity <= 49):
	discount = .2 	# discount of 20%
	discounted_P = PRICE - (PRICE * discount)
	discounted_total = discounted_P * quantity
	print("Since you purchased {} packages, you recieved a discount of 20% which resulted in a total of ${:.2f}".format(quantity,discounted_total))
	
#For a 30% discount
if(quantity >= 50 and quantity <= 99):
	discount = .3 	# 30%
	discounted_P = PRICE - (PRICE * discount)
	discounted_total = discounted_P * quantity
	print("Since you purchased {} packages, you recieved a discount of 30% which resulted in a total of ${:.2f}".format(quantity,discounted_total))

#For a 40% discount
if(quantity >= 100):
	discount = .4 	# 40%
	discounted_P = PRICE - (PRICE * discount)
	discounted_total = discounted_P * quantity
	print("Since you purchased {} packages, you recieved a discount of 40% which resulted in a total of ${:.2f}".format(quantity,discounted_total))
	
input("hit enter to stop waiting")
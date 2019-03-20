x = int(input("Please enter a number that isn't negative: "))
y = 1

while(x <= 0):
	print("The value you entered was negative")
	x = int(input("Please enter a number that isn't negative: "))

print("Solving {}!".format(x))
	
for x in range(1,x+1):
	y = x * y
	print("[{}] {}".format(x,y))
	
input("\nHit enter to close")
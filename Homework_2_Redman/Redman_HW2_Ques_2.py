import turtle

######################
#   standard mode	 #
# 0 - east			 #
# 90 - north		 #
# 180 - west		 #
# 270 - south		 #
######################
#   For Heading		 #
######################

north = 90
east = 0
south = 270
west = 180

squares = int(input("Imput how many squares you want:"))
e = 4   # is used to determine extended length
turtle.screensize(10,10)

for i in range(squares):
	z = 3 * i
	turtle.home
	turtle.setheading(north)
	turtle.forward(z+e)
	turtle.setheading(west)
	turtle.forward(z+e)
	turtle.setheading(south)
	turtle.forward(z+e)
	turtle.setheading(east)
	turtle.forward(z+e)
turtle.hideturtle()
	
input("hit enter to close")
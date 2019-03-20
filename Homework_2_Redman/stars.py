import turtle
import random

def sky(stars,south,north,east,west):
	turtle.up()
	
	turtle.home()					#black backdrop
	turtle.down()
	turtle.pencolor("black")
	turtle.fillcolor("black")
	turtle.begin_fill()
	turtle.setheading(north)
	turtle.forward(250)
	turtle.right(90)
	turtle.forward(190)
	turtle.right(90)
	turtle.forward(250)
	turtle.right(190)
	turtle.end_fill()
	
	for i in range(stars):  			#star generator
		turtle.up()
		turtle.pencolor("white")
		turtle.fillcolor("white")
		x = random.randint(0,190)
		y = random.randint(0,250)
		turtle.setpos(x,y)
		turtle.down()
		turtle.begin_fill()
		turtle.circle(0.5)
		turtle.end_fill()
		turtle.up()
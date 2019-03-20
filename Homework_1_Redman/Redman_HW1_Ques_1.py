#Dalton Redman
import turtle

#################################-----SHAPE NUMBER 1------###########################################################

turtle.begin_fill()				# First Square
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.left(90)					# Transition to next square
turtle.forward(100)

turtle.begin_fill()				# Second Square
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.hideturtle()

input("Press enter for next shape")

#################################-----SHAPE NUMBER 2------###########################################################

turtle.reset()

turtle.forward(100)			# Big triangle
turtle.left(109.471)
turtle.forward(150)
turtle.left(141.058)
turtle.forward(150)
turtle.left(109.471)

turtle.begin_fill()			# Small Triangle
turtle.forward(100)
turtle.left(135)
turtle.forward(70.711)
turtle.left(90)
turtle.forward(70.711)
turtle.end_fill()

turtle.hideturtle()

input("Press enter for next shape")

#################################-----SHAPE NUMBER 3------###########################################################

turtle.reset()

turtle.forward(100)				# First Square
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.left(90)					# Transition to next square
turtle.forward(100)

turtle.right(90)				# Second Square
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

turtle.up()						# Outer lines
turtle.left(180)
turtle.forward(100)
turtle.left(135)
turtle.down()
turtle.forward(141.42)
turtle.up()
turtle.left(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.down()
turtle.forward(141.42)

turtle.up()						#Inner Lines
turtle.left(45)
turtle.forward(100)
turtle.left(135)
turtle.down()
turtle.forward(282.84)

turtle.hideturtle()

input("Press enter for next shape")

#################################-----SHAPE NUMBER 4------###########################################################

turtle.reset()

turtle.circle(50)	        # Circle 1

turtle.up()                 # Transition to Circle 2
turtle.forward(62.5)
turtle.right(90)
turtle.forward(62.5)
turtle.left(90)

turtle.down()               # Circle 2
turtle.circle(50)

turtle.up()                 # Transition to circle 3
turtle.left(90)
turtle.forward(62.5)
turtle.right(90)
turtle.forward(62.5)

turtle.down()               # Circle 3
turtle.circle(50)

turtle.up()                 # Transition to Circle 4
turtle.forward(62.5)
turtle.right(90)
turtle.forward(62.5)
turtle.left(90)

turtle.down()               # Circle 4
turtle.circle(50)

turtle.up()                 # Transition to circle 5
turtle.left(90)
turtle.forward(62.5)
turtle.right(90)
turtle.forward(62.5)

turtle.down()               # Circle 5
turtle.circle(50)

turtle.hideturtle()

input("Press enter for next shape")

#################################-----SHAPE NUMBER 5------###########################################################

turtle.reset()

turtle.forward(50)				# Draws the compass
turtle.write("East", align = "left")
turtle.left(180)
turtle.forward(100)

turtle.write("West", align = "right")
turtle.left(180)
turtle.up()
turtle.forward(50)

turtle.down()
turtle.left(90)
turtle.forward(50)
turtle.write("North",align = "center")

turtle.left(180)
turtle.forward(100)
turtle.up()
turtle.forward(15)
turtle.down()
turtle.write("South",align = "center")
turtle.up()


turtle.home()					# Draws the center circle
turtle.down()
turtle.forward(10)
turtle.left(90)
turtle.circle(10)

turtle.hideturtle()

input("Press enter for next shape")

#################################-----SHAPE NUMBER 6------###########################################################

turtle.reset()

turtle.dot()				# Solid Lines  / Dot 1
turtle.left(45)
turtle.forward(70.71)
turtle.dot()				# Dot 2
turtle.right(135)
turtle.forward(100)
turtle.dot()				# Dot 3
turtle.right(135)
turtle.forward(141.42)
turtle.dot()				# Dot 4
turtle.left(135)
turtle.forward(100)
turtle.dot()				# Dot 5
turtle.left(135)
turtle.forward(70.71)

turtle.up()					# Transition to dash line
turtle.forward(70.71)
turtle.left(135)

turtle.down()				# Dash Line 1
turtle.forward(12.5)
turtle.up()
turtle.forward(8.33)
turtle.down()
turtle.forward(25)
turtle.up()
turtle.forward(8.33)
turtle.down()
turtle.forward(25)
turtle.up()
turtle.forward(8.33)
turtle.down()
turtle.forward(12.5)

turtle.up()					# Transition to 2nd Dash line
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.down()				# Dash Line 2
turtle.forward(12.5)
turtle.up()
turtle.forward(8.33)
turtle.down()
turtle.forward(25)
turtle.up()
turtle.forward(8.33)
turtle.down()
turtle.forward(25)
turtle.up()
turtle.forward(8.33)
turtle.down()
turtle.forward(12.5)

turtle.hideturtle()

input("Press enter to close program")
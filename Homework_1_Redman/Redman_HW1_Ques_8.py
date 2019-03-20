#Dalton Redman
# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction
test1 = False		  # Test case for a check 

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user.
angle = float(input("Enter the projectile's angle: "))
force = float(input("Enter the launch force (1-10): "))

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
	test1 = True
	print('Target hit!')
	
	
else:
	test1 = False						# used for my code
	print('You missed the target.')
	
		
		
#################################----- My Code ------###########################################################

#pytahgorean theorom for giving hints
OP = TARGET_LLEFT_Y
AD = TARGET_LLEFT_X
HY = (OP**2 + AD**2)**.5

Angle_estimate = OP / HY
BEST_ESTIMATE_FORCE = HY / FORCE_FACTOR

if(test1 == False):									# Checks the force amount
	if(force > BEST_ESTIMATE_FORCE):
		print("Try Using less force")
	elif(force < BEST_ESTIMATE_FORCE):
		print("Try using more force")
	else:
		print("you put the right amount of force")
		
if(test1 == False):
	if(turtle.xcor() <= TARGET_LLEFT_X):
		print("Try using smaller angle")
	elif(turtle.xcor() >= (TARGET_LLEFT_X + TARGET_WIDTH)):
		print("Try using a greater angle")

input("hold")
#################################----- My code ------###########################################################

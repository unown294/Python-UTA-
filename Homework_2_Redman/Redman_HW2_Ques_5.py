import turtle
import random
import stars
import buildings
import windows

######################
#   standard mode	 #
# 0 - east			 #
# 90 - north		 #
# 180 - west		 #
# 270 - south		 #
######################

north = 90
east = 0
south = 270
west = 180
star = 50 # how many stars are going to generated

# Draw calls
stars.sky(star,south,north,east,west)
buildings.buildings(south,north,east,west)
windows.windows(south,north,east,west)

input("Hit enter to close")

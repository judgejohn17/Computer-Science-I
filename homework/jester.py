#File: hexes.py
#Name: John J.
#Description: This program draws a jetser face wearing a hat. This program uses recursion to draw the face and hat 
from turtle import *

def initworld(size):
	"""Pre-conditions: The turtle is up and facing the top of the screen
	Post-conditions: The turtle is down, facing left, and ready to draw on a blank canvas"""
	setup(1000,1000)
	speed(100)
	left(90)
	down()

def drawRecJester(depth, size):
	"""Pre-conditions: The turtle is down, facing left, and ready to draw on a blank canvas
	Post-conditions: The turtle is down has drawn the correct number of squares and circles for the jester face"""
	if depth%2 == 0:
		color("red")
	if depth%2== 1:
		color("green")
	if depth == 0:
		right(90)
		circle(size/2)
		left(90)
	elif depth > 0:
		left(90)
		forward(size/2)
		right(90)
		forward(size)
		left(45)
		drawRecJester(depth-1, size/2)
		if depth%2 == 0:
			color("red")
		if depth%1 == 1:
			color("green")
		right(135)
		forward(size)
		left(45)
		drawRecJester(depth-1, size/2)
		if depth%2 == 0:
			color("red")
		if depth%2 == 1:
			color("green")
		right(135)
		forward(size)
		right(90)
		forward(size/2)
		right(90)

def main():
	"""Pre-conditions: the program opens and prompts the user with a command
	Post-conditions: the user has entered the intigers and the turtle will draw the jester"""
	input("Hit Enter to start...")
	depth = int( input("Enter 'depth' (a non-negative integer): ") )

	if depth < 0:
		print("Sorry. That integer was not non-negative. ")
		depth = int( input("Enter 'depth' (a non-negative integer): ") )

	size = int( input("Enter 'size' (a non-negative integer): ") )

	if size < 0:
		print("Sorry. That integer was not non-negative. ")
		size = int( input("Enter 'size' (a non-negative integer): ") )
		
	initworld(size)
	drawRecJester(depth, size)
	input("Hit Enter to end the program:")
    
main()
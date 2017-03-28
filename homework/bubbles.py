#File: bubbles.py
#Name: John J.
#Description: This program draws bubbles within a bounding box using recursion and then redrawing it using iterartivly it then shows the sum of the radi of the bubbles 


from turtle import *
from math import *
from random import *
import sys

def MAX_BUBBLES():
	return 500

def MIN_BUBBLES():
	return 0

def MAX_DISTANCE():
	return 20

def MIN_DISTANCE():
	return 1

def MAX_RADIUS():
	return 20

def MIN_RADIUS():
	return 1

def MAX_ANGLE():
	return 30

def randAngle():
	"""This function defines the value of 'angle' which is a random intiger between -MAX_ANGLE and MAX_ANGLE"""
	angle = randint(-MAX_ANGLE(),MAX_ANGLE())
	return angle

def randDistance():
	"""This function defines the value of 'distance' which is a random intiger between 
	MIN_DISTANCE and MAX_DISTANCE"""
	distance = randint(MIN_DISTANCE(),MAX_DISTANCE())
	return distance

def bubblePrompt():
	"""This function prompts the user for 'bubbles' which is the amount of bubbles they want which must 
	be between 0-500"""
	bubbles = int(input("Bubbles (0-500): "))
	if bubbles < MIN_BUBBLES() or bubbles > MAX_BUBBLES():
		print ("Bubbles must be between 0 and 500 inclusive.")
		sys.exit()
	else: 
		return bubbles

def totalRadius(total):
	"""This function calculates the 'total' or the total radius of all the bubbles, this is done by using a 
	string for the 'total' variable"""
	print("Total radius of the bubbles is " +str(total)+ " units")

def drawCircle():
	"""This function is responsible for both drawing the bubble and creating a random color by mixing 
	red, yellow, and blue"""
	color(random(),random(),random())
	begin_fill()
	radius = randint(MIN_RADIUS(),MAX_RADIUS()) 
	circle(radius)
	end_fill()
	return radius

def drawBubblesRec(bubbles,total):
	"""This function is responsible for drawing the recursive portion of the program by taking the value 
	of "bubbles' and subtracting one until it gets to the minimum value accepted"""
	if bubbles < MIN_BUBBLES():
		totalRadius(total)
	else:
		BOUNDING_BOX()
		down()
		total += drawCircle()
		up()
		left(randAngle())
		forward(randDistance())
		drawBubblesRec(bubbles-1,total)

def drawBubblesIter(bubbles,total):
	"""This function draws the iterative part of the program by operating a while loop that is true so 
	long as 'bubbles' stays above 0"""
	while bubbles > MIN_BUBBLES():
		BOUNDING_BOX()
		down()
		total += drawCircle()
		up()
		left(randAngle())
		forward(randDistance())
		bubbles-=1
	totalRadius(total)

def BOUNDING_BOX():
	"""This function keeps the bubbles from leaving the binding box. This is done by using the cordinate 
	system and not allowinf the turtle to make a bubble withen 30 from the edge"""
	x = int(xPos())
	y = int(yPos())
	if(x > 170 or x <- 170):
		right(180)
		up()
		forward(15)
		down()
	elif(y > 170 or y <- 170):
		right(180)
		up()
		forward(15)
		down()
	else:
		pass

def xPos():
	"""""This function returns the x value of the cordinate so that it can be 
	compared in the BOUNDING_BOX function"""
	(x,y) = position()
	return x

def yPos():
	"""""This function returns the y value of the cordinate so that it can 
	be compared in the BOUNDING_BOX function"""
	(x,y) = position()
	return y

def drawBoundary():
	"""This function draws the bounding box """
	up()
	speed(0)
	forward(200)
	down()
	right(90)
	forward(200)
	right(90)
	forward(400)
	right(90)
	forward(400)
	right(90)
	forward(400)
	right(90)
	forward(200)
	right(90)
	up()
	forward(200)

def main():
	input("Press Enter to start the program...")
	bubbles=bubblePrompt()
	hideturtle()
	drawBoundary()
	speed(0)
	drawBubblesRec(bubbles,0)
	input("Press Enter to draw the bubbles in an iterative function...")
	clear()
	reset()
	drawBoundary()
	speed(0)
	drawBubblesIter(bubbles,0)
	input("Press Enter to end the program...")
	bye()

main()

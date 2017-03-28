#File: hexes.py
#Name: John J.
#Description: This program draws 8 hexes 
from turtle import *     

def initialize():
	""""This function intitalizes the turtle by putting the turtles pen up
	and turning it to the left"""
	up()
	left(90)

def drawHexagon():
	"""This is the function that is responsible for drawing the hexagon
	it moves the turtle to the correct position to begin the hexagon and
	then draws all six sides"""
	forward(43.3)
	right (90)
	down()
	forward (25)
	left(60)
	for i in range(5):
		forward(50)
		left(60)
	forward(25)
	right(90)
	up()
	forward(43.3)
	left(180)

def rotate():
	"""This function rotates the turtle so that it is in the correct 
	position to begin to draw the next hexagon"""
	left(60)

def main():
	input("Hit Enter to start program")
	"""The main function is responsible for putting all the individual
	functions together and also tells the computer to execute the 
	drawHexagon command and rotate command six times"""
	initialize()
	for i in range(6):
		drawHexagon()
		rotate()
	input("Hit Enter to finish the program")
	
main()

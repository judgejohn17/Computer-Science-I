#Author: John Judge
#Title: letterHist.py
#Description: A supporting turtle plotter program for the first task

############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################

#prgram imports, classes, and function defintions here...
from wordData import *
import letterFreq
from turtle import *
from math import *

def setUp():
	"""
	Sets the turle up, yo. This Foshizzle is going to be set to speed(0) cause ain't nobody got time
	for that. But I heard you like turtles so I made my turtle a turtle! The pen also starts up.
	"""
	speed(0)
	shape("turtle")
	up()

def drawLabels():
	"""
	This draws the axis and labels them. It also creates the tile for the graph
	"""
	goto(-300,0)
	write("Frequency", font=("Arial", 16, "bold"))
	goto(0,300)
	write("Letter Frequencies", font=("Arial", 20, "bold"))
	goto(0,-300)
	write("Letters", font=("Arial", 16, "bold"))

def xAxis():
	"""
	This function will itterate through a list containing the albhapet. It will then write the character
	on the X Axis because they are the approprite labels
	"""
	goto(-200,-200)
	lst=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	down()
	i=0
	for i in range(0,26):
		forward(30)
		up()
		right(90)
		forward(15)
		write(lst[i], font=("Arial", 10))
		back(15)
		left(90)
		down()
		i+1

def yAxis(freqList, maxVal):
	"""
	This function takes in maxVal(the maximum value of frequencies) and freqList(a list of all the 
	frequencies in albabetical order). It then scales the y axis and provides the labels.
	"""
	goto(-200,-200)
	down()
	left(90)
	forward(400)
	increment=maxVal/10
	temp=increment
	back(400)
	for i in range (0,10):
		forward(40)
		left(90)
		forward(17)
		write(str(temp)[:5])
		back(17)
		right(90)
		temp+=increment




def drawBars(freqList, maxVal):
	"""
	This function is responsible for drawing the bars on the graph. It itterates through the list
	of frequencies and draws an appropritely sized bar for the scale.
	"""
	goto(-200,-200) 
	move = 0
	pixInc = maxVal/400
	for i in range(0, 26):
		fillcolor("Blue")
		#WHY DONT THEY HAVE EGG SHELL WHITE
		begin_fill()
		move = freqList[i] / pixInc
		forward(move)
		right(90)
		forward(30)
		right(90)
		forward(move)
		left(180)
		end_fill()

def letterFreqPlot(freqList):
	"""
	Its practically a main function that isnt called main. It calls all the other functions.
	"""
	maxVal = sorted(freqList)[25]
	setUp()
	drawLabels()
	xAxis()
	yAxis(freqList, maxVal)
	drawBars(freqList, maxVal)

if __name__ == '__main__':
	main()


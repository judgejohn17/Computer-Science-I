#File: Computer_Science.py
#Name: John J.
#Description: This program writes the words "COMPUTER SCIENCE" 
from turtle import*

def initialize():
	"""This function moves the turtle to the starting position which is 240 pixels to the left of center"""
	up()
	back(240)

def move():
	"""This function tells the turtle to move on to the starting position of the next letter. Every letter's
	starting position is in its bottom left hand corner"""
	up()
	forward(30)
	down()

def C():
	"""This function tells the turtle to draw a C"""
	down()
	forward(20)
	up()
	left(90)
	forward(20)
	down()
	left(90)
	forward(20)
	left(90)
	forward(20)
	left(90)
def O():
	"""This function tells the turtle to draw a O"""
	forward(20)
	left(90)
	forward(20)
	left(90)
	forward(20)
	left(90)
	forward(20)
	left(90)

def M():
	"""This function tells the turtle to draw an M"""
	left(90)
	forward(20)
	right(135)
	forward(18)
	left(90)
	forward(18)
	right(135)
	forward(20)
	up()
	right(90)
	forward(20)
	right(180)
	down()

def P():
	"""This function tells the turtle to draw a P"""
	left(90)
	forward(20)
	right(90)
	forward(20)
	right(90)
	forward(10)
	right(90)
	forward(20)
	up()
	left(90)
	forward(10)
	left(90)
	down()

def U():
	"""This function tells the turtle to draw a U"""
	forward(20)
	left(90)
	forward(20)
	up()
	left(90)
	forward(20)
	left(90)
	down()
	forward(20)
	left(90)

def T():
	"""This function tells the turtle to draw a T"""
	up()
	forward(10)
	left(90)
	down()
	forward(20)
	up()
	left(90)
	forward(10)
	right(180)
	down()
	forward(20)
	up()
	right(90)
	forward(20)
	right(90)
	forward(20)
	right(180)
	down()

def E():
	"""This function tells the turtle to draw an E"""
	left(90)
	forward(20)
	right(90)
	forward(20)
	up()
	right(90)
	forward(10)
	right(90)
	forward(10)
	down()
	forward(10)
	up()
	left(90)
	forward(10)
	left(90)
	down()
	forward(20)
	up()
	back(20)
	down()

def R():
	"""This function tells the turtle to draw an R"""
	left(90)
	forward(20)
	right(90)
	forward(20)
	right(90)
	forward(10)
	right(90)
	forward(20)
	left(153.4)
	forward(22.4)
	right(153.4)
	up()
	forward(20)
	right(180)
	down()

def Space():
	"""This function tells the turtle to create the space between the words COMPUTER and SCIENCE"""
	up()
	forward(20)
	down()

def S():
	"""This function tells the turtle to draw an S"""
	forward(20)
	left(90)
	forward(10)
	left(90)
	forward(20)
	right(90)
	forward(10)
	right(90)
	forward(20)
	up()
	right(90)
	forward(20)
	right(90)
	forward(20)
	right(180)
	down()

def I():
	"""This function tells the turtle to draw an I"""
	forward(20)
	up()
	left(90)
	forward(20)
	left(90)
	down()
	forward(20)
	up()
	back(10)
	down()
	left(90)
	forward(20)
	right(90)
	up()
	forward(10)
	right(180)
	down()

def N():
	"""This function tells the turtle to draw an N"""
	left(90)
	forward(20)
	right(135)
	forward(28.3)
	left(135)
	forward(20)
	up()
	left(90)
	forward(20)
	left(90)
	forward(20)
	left(90)
	down()

def main():
	"""The main function is responsible for putting all the individual
	functions together and telling the computer to run them in order"""
	input("Hit Enter to start the program")
	initialize()
	C()
	move()
	O()
	move()
	M()
	move()
	P()
	move()
	U()
	move()
	T()
	move()
	E()
	move()
	R()
	move()
	Space()
	S()
	move()
	C()
	move()
	I()
	move()
	E()
	move()
	N()
	move()
	C()
	move()
	E()
	input("Hit Enter to finish the program")

main()
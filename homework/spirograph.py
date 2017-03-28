#File: spirograph.py
#Name: John J.
#Description: This program draws a spirograph using recursion 
from turtle import *
from math import *

def x(p,R,r,t):
	"""pre-condition: x does not have a value assigned"""
	"""post-condition: returns value for x based on equation"""
	x = (R-r)*cos(t) - (r+p)*cos((R-r)/r*t)
	return x 

def y(p,R,r,t):
	"""pre-condition: y does not have a value assigned"""
	"""post-condition: returns value for y based on equation"""
	y = (R-r)*sin(t) - (r+p)*sin((R-r)/r*t)
	return y

def circleRec(p,R,r,t):
	"""pre-condition: The values for x and y have been assigned and the user has entered a value for p"""
	"""post-condition: The circles are drawn for the spirograph"""
	if t <= 0:
		pass
	else:
		down()
		goto(x(p,R,r,t) , y(p,R,r,t))
		circleRec(p,R,r,t-0.01)

def main():
	p = int( input("p (10-100): ") )
	while p < 10 or p > 100:
		print ("Incorrect value for p!")
		p = int( input("p: ") )

	R = 100
	r = 4
	t = 2*pi


	up()
	goto(x(p,R,r,t) , y(p,R,r,t))
	circleRec(p,R,r,t)

	input("Hit enter to close...")

main()

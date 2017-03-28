"""
File: variable_circles-sol.py
Language: python3
Author: John Judge 
Purpose: Draws a series of circles in a pattern to a certain detail.
"""

from turtle import *

def init(DIM, depth, circles):
    """
    Initialize the scene.  The window is DIM width and DIM/2 height and
    (depth) indicates the depth of recursion.
    
    DIM (int):  The square dimensions of the screen.
    depth (int):  The total depth of recursion.
    
    Preconditions: None
    Postconditions: Canvas is initialized, turtle in center, pen is up.
    """
    
    title("Variable Circles, Depth:" + str(depth) + "  Circles: " + str(circles))
    getscreen().setup(width=DIM, height=DIM)
    setworldcoordinates(-DIM, -DIM, DIM+1, DIM+1)
    up()
    setpos(-DIM, -DIM)
    write("Circles, Depth:" + str(depth) + "  Circles: " + str(circles), False, font=("Arial", 16, "bold"))
    setpos(0,0)
    speed(0)
    pensize(3)
    
def draw_circle_from_center(radius):
    """draw_circle draws a single circle of radius (radius).
    
    radius (int): the radius of the circle to be drawn
    
    Preconditions: pen is up, facing east at center of circle
    Postconditions: pen is up, facing east at center of circle
    """
    down()
    circle(radius)
    up()
    
def draw_all_rec(depth, radius, circles):
    """The recursive drawing function that takes the current depth of recursion
    (depth), the radius of the circle to draw (radius) and the number of circles
    to draw around each circle
    
    depth (int): the current depth of recursion
    radius (int): the radius of the circle/s to be drawn at this depth
    circles (int): the number of circles to make around the circumference of each circle
    
    Preconditions: depth > 0, radius > 0, pen is up and facing east at center of main circle
    Postconditions: pen is up and facing east at center of main circle
    """
    down()
    draw_circle_from_center
    up()
    if depth > 0 :
        if circles%2=1:
            pass
        if circles%2=0:
            pass
    else:
        down()
        draw_circle_from_center(radius-1)
        draw_all_rec(depth-1,radius/2,circles*2)
        up()

        

def main():
    """
    The main prompts for the depth of recursion (N) and invokes
    routines to circle drawing routine.
    """
    
    # initialization
    depth = int(input("Depth: "))
    circles = int(input("Circles: "))
    circles = (circles % 7)
    if circles < 1 :
        circles = 1
    DIM = 600
    init(DIM, depth, circles)
    
    # invoke the main drawing function
    draw_all_rec(depth-1, DIM/3, circles)
    
    # pause when finished for input
    input("Hit enter to close...")
    
main()
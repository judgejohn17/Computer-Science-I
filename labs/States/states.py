#File: states.py
#Name: John J.
#Description: This program uses the states.txt file to find the probability of two random people being in a room and being from the same state 

from rit_object import *
import random

class State(rit_object):
	"""
	This creates a class called State  with slots for the state name and population
	"""
	__slots__ = ('name', 'population')
	_type = (str, int)

def test(popu, states):
	"""
	The test function takes in an intiger for population called popu and the names of states. 
	It then calls findState for a random integer and then checks if it's in the set. If it isnt in
	the set, the state is added to the set. Finally it returns the count.
	"""
	double = True
	mySet = set()
	count = 0
	while double == True:
		name = findState(popu, states, random.randint(-1, popu))
		if (name in mySet):
			return count
		else:
			mySet.add(name)
			count += 1

def findState(popu, states, number):
	"""
	The findState function takes in a popu integer, the list of states, and a number
	which is used to tell which state that number is. It then returns the name
	of the state's the number by using a counter.
	"""
	i = len(states) - 1
	while popu > 0:
		if number > popu - states[i].population:
			return states[i].name
		else:
			popu = popu - states[i].population
			i = i - 1
def main():
	"""
	The main function takes in the filename and the test peramiters (testNum) from the user. 
	It then checks if the testNum is in the range. Next it opens the text file and puts the
	state's name and populations in the class' objects. It then calls the test function as many 
	times that the user inputed. It then prints the average amount of times the people are from
	the same state.
	"""
	filename = input("File Name: ")
	testNum = int(input("Number of tests(1-1000):"))
	if testNum <= 0 and testNum >= 1001:
		print("That integer is not in the possible range.")
		exit()

	sum = 0
	stateList = []

	with open(filename, 'r', encoding = 'utf-8') as infile:
		for line in infile:
			name, population = line.strip().split(' ')
			state = State(name, int(population))
			stateList.append(state)
			sum += int(population)
		#at this point, we have a list of State objects at stateList and
		#the sum of the total population at sum
	avg = 0
	for i in range(testNum):
		avg += test(sum, stateList)

	avg = avg/testNum
	print("The average is " + str(avg))
main()
#File: findFast.py
#Name: John J.
#Description: This program uses the fastSelect algarithm with an unsorted list to find the median of the data 

def getList():
	"""
	This function is responsible for opening the text file thats is used in conjunction with the 
	program. It takes the list and splits each line one by one and returns the new list.
	"""
	filename = input( '\nPlease specify a filename: ')
	aList = []
	useFile = open( filename )
	for line in useFile:
		s = line.split() 
		aList.append(int(s[1].strip()))
	return aList

def fastSelect ( aList, k ):
	"""
	This function is the actual fastSelect algarithm derived from the pseudocode given to us on the 
	lab handout. It takes the list returned by the getList function. A while loop keeps the function
	itterating through the list pivoting.
	"""
	while aList != [ ] :
		pivot = aList[ len( aList ) // 2 ]
		smallerList = [ ]
		for num in aList:
			if num < pivot:
				smallerList.append( num )
		largerList = [ ]
		for num in aList:
			if num > pivot:
				largerList.append( num )
		count = len(aList) - len( smallerList ) - len( largerList )
		m = len( smallerList )
		if ( k >= m and k < m + count ):
			return pivot
		if ( m > k ):
			aList = smallerList
		else:
			k = k - m - count
			aList = largerList

def findSumOfDistances(aList, k):
	summation = 0
	for place in aList:
		summation += abs(int(place) - int(k))
	return summation

def main():
	"""
	The main function is responsible for calling the other functions. Firstly it imports python's time
	command. It then asks for input and starts the clock as it runs through the program. It defines
	what medians and elapsed time are. It then prints the median and algorithm speed before asking to quit.
	"""
	import time
	aList = getList()
	input ( '\nHit Enter to begin:\n')
	k = len ( aList ) // 2 
	start_time = time.clock()
	median_find = fastSelect( aList, k )
	end_time = time.clock()
	elapsed_time = end_time - start_time
	sList = aList
	summation = findSumOfDistances(aList, k)
	print ( 'Optimal Location is:\n' + str( median_find ) + '\n' )
	print("Sum of distance is: " + str(summation))
	print ( 'Algorithm speed:\n' + str( elapsed_time ) + '\n')
	input ( 'Hit Enter to quit: ')
	quit()
main()
#Author: John Judge
#Title: wordLength.py
#Description: The main program for the third task

############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################

#prgram imports, classes, and function defintions here...
from wordData import *

def occurrencesInYear(word, year, words):
	"""
	Purpose: 
	Input: word,"The word in question passed as a string"
			year,"The year in question. This is an int"
			words,"The word data which is a dictionary (dict) that maps words(str) to a list of YearCount's
	Output: "The number of occurences of the word in the year (int)"
	"""
	lst = []
	if word not in words:
		return 0
	else:
		lst = words[word]
		for i in range(len(lst)):
			if lst[i].year == year:
				return lst[i].count
			else:
				pass
		return 0

def averageWordLength(year, words):
	"""
	Purpose: 
	Input: year,"The year in question (int)"
	words,"The words data which is a dictionary (dict) that maps words (strings) to a lsy of YearCount's"
	Output: "The average word length for the year in question (float)"
	"""
	averageLen=0
	count=0
	for word in words:
		for it in words[word]:
			if it.year == year:
				averageLen += len(word) * it.count
				count += it.count
	if count != 0:
		return averageLen/count
	else:
		return 0

def averageWordLengthYears(startYear, endYear, words):
	"""
	Purpose: 
	Input: startYear,"The start year, an (int)
			endYear,"The end year, likewise an (int)"
			words,"The words data which is a dictionary (dict) that maps words (strings) to a list of YearCount's
	Output: "The list of floats that contains the average word lengths by year in the increasing order for years between startYear and endYear- both inclusive"
	"""
	lst=[]
	#Steve, if you're grading this...Hi
	year = startYear
	#Itterate through all years
	for i in range(endYear+1 - startYear):
		val = averageWordLength(year, words)
		lst.append(val)
		year+= 1
	return lst
				
	
def main():
	"""
	docstring for main function here
	"""
	fileName = input("Enter word file: ")
	word = input("Enter word: ")
	year = input("Enter a year: ")
	words = wordData.readWordFile(fileName)
	occInYear = occurrencesInYear(word, int(year), words)
	print("The word ", word, " occured ", occInYear, " times in the year ", year)
	year = input("Enter a year: ")
	avgWordLen = averageWordLength(int(year), words)
	#Ever wonder if animals are just as smart as us but don't have the means build civilizations or communicate effectivly?
	print("The average word length for the year", year, "is ", avgWordLen, "letters")
	startYear = input("Enter a start year: ")
	endYear = input("Enter an end year: ")
	lengthsList = averageWordLengthYears(int(startYear), int(endYear), words)
	simplePlot.averageWordLengthPlot(int(startYear), int(endYear), lengthsList)
	#main's code body here...
if __name__ == '__main__':
	# run the main() only when directly invoking this module main()
#end of program file			
	main()
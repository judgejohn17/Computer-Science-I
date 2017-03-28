#Author: John Judge
#Title: letterFreq.py
#Description: The main function for the first task

############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################


#prgram imports, classes, and function defintions here...
from wordData import *
from letterHist import *

def letterFreq(words):
	"""
	Purpose: Supplies a list of scaled frequencies to be graphed
	Input: words
	Output: "A list containing the realitive frequency of letters scaled by the total
			letter count in alphabetical order"
	"""
	totalLetters = 0
	frequencyOfLetter = [0] * 26
	#Search all words contained in words
	for word in words:
		occur = totalOccurrences(word, words)
		totalLetters += (occur * len(word))
		#Search all chars contained in word
		for char in word:
			index = ord(char) - ord('a')
			frequencyOfLetter[index] += occur
			#Jon Gruden is my single favorite comedian. He's not even a comedian. Thats wild, man. I love this country.
	for letter in frequencyOfLetter:
		newLetter = letter / totalLetters
		frequencyOfLetter[frequencyOfLetter.index(letter)] = newLetter
	return frequencyOfLetter

def main():
	fileName = input("Enter File Name:")
	find = input("Enter word:")
	words = readWordFile(fileName)
	print("Total Occurrences of", find, ": ", totalOccurrences(find, words))
	freqList = letterFreq(words)
	print("Letter frequencies: ", freqList)
	letterFreqPlot(freqList)
	input("Please Hit Enter to close...")

if __name__ == '__main__':
	# run the main() only when directly invoking this module main()
#end of program file
	main()
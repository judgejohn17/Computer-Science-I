#Author: John Judge
#Title: wordFreq.py
#Description: The main program for the second task

############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################

#prgram imports, classes, and function defintions here...
from wordData import *

def wordFrequencies(words):
	"""
	Purpose: 
	Input: words, "a dictionary that maps words to a list of YearCount's
	Output: "A list of WordCount objects in decreasing order from most to least frequent"
	"""
	WordCountList = []
	#Search all words contained in words
	for word in words:
		val = totalOccurrences(word, words)
		newWord = WordCount(word, val)
		WordCountList.append(newWord)
	return sorted(WordCountList, key=lambda WordCount: WordCount.count, reverse=True)


def main():
	fileName = input("Enter word file: ")
	rank = input("Enter rank (1-3): ")
	words = wordData.readWordFile(fileName)
	freqList = wordFrequencies(words)
	print("Rank ", rank, ": ", freqList[int(rank)-1])
	simplePlot.wordFreqPlot(freqList)
if __name__ == '__main__':
	# run the main() only when directly invoking this module main()
#end of program file
	main()

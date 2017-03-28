#Author: John Judge
#Title: wordData.py
#Description: A supporting module used in all three tasks

############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
############################################################

#prgram imports, classes, and function defintions here...
from rit_object import *

class YearCount(rit_object):
	__slots__ = ('year','count')
	_types = (int, int)

class WordCount(rit_object):
	__slots__ = ('word','count')
	_types = (str, int)

def createYearCount(year, count):
	"""
	Purpose: Creates an empty YearCount class
	Input: YearCount class slots
	Output: "Empty YearCount class"
	"""
	return YearCount(year, count)

def createWordCount(word, count):
	"""
	Purpose: Creates an empty WordCount class
	Input: WordCount class slots
	Output: "Empty WordrCount class"
	"""
	return WordCount(word, count)

def readWordFile(fileName):
    #read in the entire unigram dataset
    """
    Purpose: Creates a list of the YearCount class containing word (str),year(int), and count(int)
    Input: filename("A string given the name of a unigram csv file")
    Output: "A dictionary mapping to the lists of YearCount objects. 
    For each word there is exactly one list of YearCount objects.
    Each YearCount object contains a year in which a word appeared
    and the count of the number of times the word appeared that year"
    """
    words={}
    with open(str(fileName), 'r', encoding = 'utf-8') as infile:
        for line in infile:
            word, year, count = line.strip().split(', ') 
            if word in words:
                val = YearCount(int(year), int(count))
                lst.append(val)
                words[word] = lst
            else:
                lst = []
                val = YearCount(int(year), int(count))
                lst.append(val)
                words[word] = YearCount(int(year), int(count))
    return words

def totalOccurrences(word, words):
    """
	Purpose: Combines the occurences of the word in each year to a total occurrence over all years
	Input: "word: The word for which to calculate the count. Not guaranteed to exist in words
			words: A dictionary mapping words to lists of YearCount objects"
	Output: "The total number of times that a word has appeared in a book in the entire dataset"	
	"""
    if word not in words:
        return 0
    count = 0
    for item in words[word]:
        #I've slept a total 4 hours in the last two days. Yesterday I didnt get to bed till 6 am. AM!
        count += item.count
    return count
"""
def main():
    fileName = input('Enter filename: ')
    print(readWordFile(fileName))

main()
"""
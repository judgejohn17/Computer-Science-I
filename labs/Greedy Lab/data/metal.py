"""
Author: Sean Strout (sps@cs.rit.edu)
Author: John Judge

This class represents the types of metal bars that Greedo can
store in his satchel.  Each type of bar is a separate Metal
object.  This module also has routines that work with metals,
e.g. creation, reading from a file, and sorting based on 
various criteria.

Language: Python 3
"""

from rit_object import *            # rit_object class

class Metal(rit_object):
    """
    Represents a single metal type, composed of:
    :slot name (str): The name of the metal
    :slot totalBars (int): The total number of bars
    :slot weightPerBar (int): The weight of a single bar
    :slot valuePerBar (int): The value of a single bar
    :slot valuePerWeight (float): The value per weight of the metal
    :slot barsTaken (int): The number of bars added to the satchel
    """
    __slots__ = ('name', 'totalBars', 'weightPerBar', 'valuePerBar', 'valuePerWeight', 'barsTaken')
    _type = (str, int, int, int, float, int)


def createMetal(name, totalBars, weightPerBar, valuePerBar):
    """
    Create and return a new Metal object.
    :param name (str): The name of the metal
    :param totalBars (int): The total number of bars
    :param weightPerBar (int): The weight of a single bar
    :param valuePerBar (int): The value of a single bar
    :return: A newly initialized Metal object
    :rtype: Metal
    """
    return Metal(name, totalBars, weightPerBar, valuePerBar, valuePerBar/weightPerBar, 0)

def readMetals(fileName):
    """
    Read the metals from a file whose format is:
        metalName totalBars weightPerBar valuePerBar
    :param fileName (str): The name of the file
    :return: A list of Metal objects
    :rtype: list
    """

    metList = []
    with open(str(fileName), encoding = 'utf-8') as infile:
        for line in infile:
            lst = line.split()
            metList.append(createMetal(lst[0], int(lst[1]), int(lst[2]), int(lst[3])))
    return metList

def sortMetalsByValuePerBar(metals):
    """
    Sort the metals by value per bar using insertion sort.  The list of
    metals is modified in place to be ordered by value per bar.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """

    for i in range(0, len(metals)):
      for j in range(i+1, len(metals)):
        if metals[i].valuePerWeight > metals[i].valuePerWeight:
            temp = metals[j]
            metals[j] = metals[i]
            metals[i] = temp

def sortMetalsByValuePerWeight(metals):
    """
    Sort the metals by value per bar using insertion sort.  The list of
    metals is modified in place to be ordered by value per bar.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """

    for obj in range(len(metals)-1):
        index = obj
        while index > -1 and metals[index].valuePerWeight > metals[index + 1].valuePerWeight:
            temp = metals[index]
            metals[index] = metals[index + 1]
            metals[index + 1] = temp
            index = index - 1

def printMetals(metals):
    """
    Display the metals to standard output.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """

    for i in metals:
        print(i)

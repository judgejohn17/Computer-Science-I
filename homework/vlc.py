#File: vlc.py
#Name: John J.
#Description: This program reads a text file and returns symbols's frequency as well as code words
from array_heap import*
from math import *
from rit_object import *

#########################################
#A CLASS TO REPRESENT THE DNA
#########################################
class Symbol(rit_object):
    __slots__ = ('name', 'frequency', 'codeword')
    _types = (str, int, str)
#######################################
#A marker to represent the DNA
#######################################
def CreateSymbol(name,frequency):
    symbl = Symbol(name, frequency, '');
    return symbl


class Node(rit_object):
    __slots__ = ('frequency', 'symbol')
    _types = (int, list)

def CreateNode(frequency, symbol):
    
    sym = []
    for i in symbol:
        sym.append(i)
    node = Node(frequency, sym)
    return node

def fileRead():
    """
    This function open, reads, and strips the text file
    """
    dnaData = {}
    fileName = input("Enter File Name: ")
    for line in open(fileName):
        line = line.strip()
        line = line.replace(" ","")# incase there is anymore white spaces...such a pain!
        for dna in line:
            if dna in dnaData:
                dnaData[dna] +=1
            else:
                dnaData[dna] = 1
    return dnaData

def symbol(dnaData):
    """
    This creates the list of what the symbols will be
    """
    dnaDataSymbol = []
    for key in dnaData:
        dnaDataSymbol.append(CreateSymbol(key,dnaData[key]))
    return dnaDataSymbol

def node(dnaDataSymbol):
    """
    This creates a node that holds the frequency and symbol
    """
    node = []
    for i in dnaDataSymbol:
        node.append(CreateNode(i.frequency,[i]))
    return node

def collectionNode(node,heap):
    """
    This node collects the nodes in a heap
    """
    for data in node:
        add(heap,data)
    return heap


def compareFunc(node1,node2):
    """
    A compare function that takes two nodes and compares if the first is smaller than the next
    """
    return node1.frequency < node2.frequency

def main():
    dnaData = fileRead()
    # puts symbols and frequencies into a dictionary and prints it out
    print(dnaData)
    # symbol returns a list of symbol objects
    dnaDataSymbol = symbol(dnaData)
    node1 = node(dnaDataSymbol)
    heap = createEmptyHeap(len(node1),compareFunc)
    collectionNode(node1,heap)

    while heap.size > 1:
        n1 = removeMin(heap)
        n2 = removeMin(heap)

        for el in n1.symbol:
            el.codeword = ('0' + str(el.codeword))


        for el in n2.symbol:
            el.codeword = ('1' + str(el.codeword))

        lst = []
        for el in n1.symbol:
            lst.append(el)

        for el in n2.symbol:
            lst.append(el)

        newNode = CreateNode( n1.frequency+n2.frequency , lst)
        add(heap,newNode)

    sum = 0.0
    sum2 = 0.0
    ran = 0
    for l in heap.array:
        if l == None:
            break
        ran = len(l.symbol)
        for el in l.symbol:
                print("Symbol: %2s " % el.name, end =' ')
                print("Codeword: %8s" % el.codeword, end=' ')
                print("Frequency: %5d" % el.frequency)
                sum = sum + (len(el.codeword) * el.frequency)
                sum2 = sum2 + el.frequency
        print()

    print('Average VLC codeword length: ' + str((sum/sum2)) + ' bits per symbol.')
    print('Average Fixed lengh codeword length: ' + str(ceil(log(ran, 2))) + ' bits per symbol.')


main()